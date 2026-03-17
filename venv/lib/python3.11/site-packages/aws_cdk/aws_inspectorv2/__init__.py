r'''
# AWS::InspectorV2 Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_inspectorv2 as inspector
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for InspectorV2 construct libraries](https://constructs.dev/search?q=inspectorv2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::InspectorV2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_InspectorV2.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::InspectorV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_InspectorV2.html).

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
from ..interfaces.aws_inspectorv2 import (
    CisScanConfigurationReference as _CisScanConfigurationReference_a54cc7e6,
    CodeSecurityIntegrationReference as _CodeSecurityIntegrationReference_0787ed51,
    CodeSecurityScanConfigurationReference as _CodeSecurityScanConfigurationReference_b4a97ccc,
    FilterReference as _FilterReference_d368c0f2,
    ICisScanConfigurationRef as _ICisScanConfigurationRef_8f6555b3,
    ICodeSecurityIntegrationRef as _ICodeSecurityIntegrationRef_b418c2a5,
    ICodeSecurityScanConfigurationRef as _ICodeSecurityScanConfigurationRef_4a00a90e,
    IFilterRef as _IFilterRef_37875571,
)


@jsii.implements(_IInspectable_c2943556, _ICisScanConfigurationRef_8f6555b3, _ITaggableV2_4e6798f8)
class CfnCisScanConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration",
):
    '''The CIS scan configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html
    :cloudformationResource: AWS::InspectorV2::CisScanConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_inspectorv2 as inspectorv2
        
        # one_time: Any
        
        cfn_cis_scan_configuration = inspectorv2.CfnCisScanConfiguration(self, "MyCfnCisScanConfiguration",
            scan_name="scanName",
            schedule=inspectorv2.CfnCisScanConfiguration.ScheduleProperty(
                daily=inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty(
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                ),
                monthly=inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty(
                    day="day",
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                ),
                one_time=one_time,
                weekly=inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty(
                    days=["days"],
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                )
            ),
            security_level="securityLevel",
            targets=inspectorv2.CfnCisScanConfiguration.CisTargetsProperty(
                account_ids=["accountIds"],
                target_resource_tags={
                    "target_resource_tags_key": ["targetResourceTags"]
                }
            ),
        
            # the properties below are optional
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
        scan_name: builtins.str,
        schedule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]],
        security_level: builtins.str,
        targets: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.CisTargetsProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::InspectorV2::CisScanConfiguration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param scan_name: The name of the CIS scan configuration.
        :param schedule: The CIS scan configuration's schedule.
        :param security_level: The CIS scan configuration's CIS Benchmark level.
        :param targets: The CIS scan configuration's targets.
        :param tags: The CIS scan configuration's tags.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee74cd979e0690afc5238694387a2bb443783c172f8af7544b4b5c468df80b9c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCisScanConfigurationProps(
            scan_name=scan_name,
            schedule=schedule,
            security_level=security_level,
            targets=targets,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForCisScanConfiguration")
    @builtins.classmethod
    def arn_for_cis_scan_configuration(
        cls,
        resource: "_ICisScanConfigurationRef_8f6555b3",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17bb5d9e0d4a2d165ecc0f9d6c045ff79fb5bd35d06a65c705104aaf297f5690)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForCisScanConfiguration", [resource]))

    @jsii.member(jsii_name="isCfnCisScanConfiguration")
    @builtins.classmethod
    def is_cfn_cis_scan_configuration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnCisScanConfiguration.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0157dbe9d0e6a256bfb1f48831eecbee74bad3bf884fbf7b8719bed932bc494b)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnCisScanConfiguration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c340cf5a8052b5b5d1021305af92e23dcb4f62645a1014b0a49bb031d376ee8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__daf01f89651352328420f5a52535d8376706a979b3cb022464732eddc33e94c8)
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
        '''The CIS scan configuration's scan configuration ARN.

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
    @jsii.member(jsii_name="cisScanConfigurationRef")
    def cis_scan_configuration_ref(self) -> "_CisScanConfigurationReference_a54cc7e6":
        '''A reference to a CisScanConfiguration resource.'''
        return typing.cast("_CisScanConfigurationReference_a54cc7e6", jsii.get(self, "cisScanConfigurationRef"))

    @builtins.property
    @jsii.member(jsii_name="scanName")
    def scan_name(self) -> builtins.str:
        '''The name of the CIS scan configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "scanName"))

    @scan_name.setter
    def scan_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f6f074ec34751eb6d66964ee6738d096c1429db3564cba2005e530e659871bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.ScheduleProperty"]:
        '''The CIS scan configuration's schedule.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.ScheduleProperty"], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.ScheduleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17c38c82086f8ffe9712e88585d2f980663e72bbb5b6ac70574594200cb759c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityLevel")
    def security_level(self) -> builtins.str:
        '''The CIS scan configuration's CIS Benchmark level.'''
        return typing.cast(builtins.str, jsii.get(self, "securityLevel"))

    @security_level.setter
    def security_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53a976b81d95f07052322a80e8b1ff546ae083bdb3cb3d358b91e5b7e50b0909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityLevel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.CisTargetsProperty"]:
        '''The CIS scan configuration's targets.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.CisTargetsProperty"], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.CisTargetsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8afffccf2a9a470f423d247abd4a6dfe735dc39c53a2abe26c8cdb1844ec12a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The CIS scan configuration's tags.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b4e1fac23c27cbc692267473e4cf9258b43062b9aea2a43b116dcfb105adb0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.CisTargetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_ids": "accountIds",
            "target_resource_tags": "targetResourceTags",
        },
    )
    class CisTargetsProperty:
        def __init__(
            self,
            *,
            account_ids: typing.Sequence[builtins.str],
            target_resource_tags: typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Sequence[builtins.str]]],
        ) -> None:
            '''The CIS targets.

            :param account_ids: The CIS target account ids.
            :param target_resource_tags: The CIS target resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-cistargets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                cis_targets_property = inspectorv2.CfnCisScanConfiguration.CisTargetsProperty(
                    account_ids=["accountIds"],
                    target_resource_tags={
                        "target_resource_tags_key": ["targetResourceTags"]
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48b07d123221faefb49073a28736f1aec9dc2a488247f39ec213274809cd3b6a)
                check_type(argname="argument account_ids", value=account_ids, expected_type=type_hints["account_ids"])
                check_type(argname="argument target_resource_tags", value=target_resource_tags, expected_type=type_hints["target_resource_tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_ids": account_ids,
                "target_resource_tags": target_resource_tags,
            }

        @builtins.property
        def account_ids(self) -> typing.List[builtins.str]:
            '''The CIS target account ids.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-cistargets.html#cfn-inspectorv2-cisscanconfiguration-cistargets-accountids
            '''
            result = self._values.get("account_ids")
            assert result is not None, "Required property 'account_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def target_resource_tags(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.List[builtins.str]]]:
            '''The CIS target resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-cistargets.html#cfn-inspectorv2-cisscanconfiguration-cistargets-targetresourcetags
            '''
            result = self._values.get("target_resource_tags")
            assert result is not None, "Required property 'target_resource_tags' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.List[builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CisTargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"start_time": "startTime"},
    )
    class DailyScheduleProperty:
        def __init__(
            self,
            *,
            start_time: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.TimeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A daily schedule.

            :param start_time: The schedule start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-dailyschedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                daily_schedule_property = inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty(
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bd3a6a48de82a0a7da55bb17cc5099cc069382b4a48c7b97e3ef62fa2f60aa59)
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "start_time": start_time,
            }

        @builtins.property
        def start_time(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.TimeProperty"]:
            '''The schedule start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-dailyschedule.html#cfn-inspectorv2-cisscanconfiguration-dailyschedule-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.TimeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DailyScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"day": "day", "start_time": "startTime"},
    )
    class MonthlyScheduleProperty:
        def __init__(
            self,
            *,
            day: builtins.str,
            start_time: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.TimeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A monthly schedule.

            :param day: The monthly schedule's day.
            :param start_time: The monthly schedule's start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                monthly_schedule_property = inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty(
                    day="day",
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__100314319c9ea946d9251b6fcc3341b05bf63331e32e3a7f7aa894b6b8421861)
                check_type(argname="argument day", value=day, expected_type=type_hints["day"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "day": day,
                "start_time": start_time,
            }

        @builtins.property
        def day(self) -> builtins.str:
            '''The monthly schedule's day.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule.html#cfn-inspectorv2-cisscanconfiguration-monthlyschedule-day
            '''
            result = self._values.get("day")
            assert result is not None, "Required property 'day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.TimeProperty"]:
            '''The monthly schedule's start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule.html#cfn-inspectorv2-cisscanconfiguration-monthlyschedule-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.TimeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonthlyScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "daily": "daily",
            "monthly": "monthly",
            "one_time": "oneTime",
            "weekly": "weekly",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            daily: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.DailyScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            monthly: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.MonthlyScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            one_time: typing.Any = None,
            weekly: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.WeeklyScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The schedule the CIS scan configuration runs on.

            Each CIS scan configuration has exactly one type of schedule.

            :param daily: A daily schedule.
            :param monthly: A monthly schedule.
            :param one_time: A one time schedule.
            :param weekly: A weekly schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                # one_time: Any
                
                schedule_property = inspectorv2.CfnCisScanConfiguration.ScheduleProperty(
                    daily=inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty(
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    ),
                    monthly=inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty(
                        day="day",
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    ),
                    one_time=one_time,
                    weekly=inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty(
                        days=["days"],
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db99f3a188203b64b30f42f8814cca36f1b859733833ecc2b25042b4eb91d395)
                check_type(argname="argument daily", value=daily, expected_type=type_hints["daily"])
                check_type(argname="argument monthly", value=monthly, expected_type=type_hints["monthly"])
                check_type(argname="argument one_time", value=one_time, expected_type=type_hints["one_time"])
                check_type(argname="argument weekly", value=weekly, expected_type=type_hints["weekly"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if daily is not None:
                self._values["daily"] = daily
            if monthly is not None:
                self._values["monthly"] = monthly
            if one_time is not None:
                self._values["one_time"] = one_time
            if weekly is not None:
                self._values["weekly"] = weekly

        @builtins.property
        def daily(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.DailyScheduleProperty"]]:
            '''A daily schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html#cfn-inspectorv2-cisscanconfiguration-schedule-daily
            '''
            result = self._values.get("daily")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.DailyScheduleProperty"]], result)

        @builtins.property
        def monthly(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.MonthlyScheduleProperty"]]:
            '''A monthly schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html#cfn-inspectorv2-cisscanconfiguration-schedule-monthly
            '''
            result = self._values.get("monthly")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.MonthlyScheduleProperty"]], result)

        @builtins.property
        def one_time(self) -> typing.Any:
            '''A one time schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html#cfn-inspectorv2-cisscanconfiguration-schedule-onetime
            '''
            result = self._values.get("one_time")
            return typing.cast(typing.Any, result)

        @builtins.property
        def weekly(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.WeeklyScheduleProperty"]]:
            '''A weekly schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html#cfn-inspectorv2-cisscanconfiguration-schedule-weekly
            '''
            result = self._values.get("weekly")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.WeeklyScheduleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.TimeProperty",
        jsii_struct_bases=[],
        name_mapping={"time_of_day": "timeOfDay", "time_zone": "timeZone"},
    )
    class TimeProperty:
        def __init__(
            self,
            *,
            time_of_day: builtins.str,
            time_zone: builtins.str,
        ) -> None:
            '''The time.

            :param time_of_day: The time of day in 24-hour format (00:00).
            :param time_zone: The timezone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-time.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                time_property = inspectorv2.CfnCisScanConfiguration.TimeProperty(
                    time_of_day="timeOfDay",
                    time_zone="timeZone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2452dd795ce037d8e45e12f3b1e33517e2f22095c208d70f01cce9d97cc7f45)
                check_type(argname="argument time_of_day", value=time_of_day, expected_type=type_hints["time_of_day"])
                check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "time_of_day": time_of_day,
                "time_zone": time_zone,
            }

        @builtins.property
        def time_of_day(self) -> builtins.str:
            '''The time of day in 24-hour format (00:00).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-time.html#cfn-inspectorv2-cisscanconfiguration-time-timeofday
            '''
            result = self._values.get("time_of_day")
            assert result is not None, "Required property 'time_of_day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_zone(self) -> builtins.str:
            '''The timezone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-time.html#cfn-inspectorv2-cisscanconfiguration-time-timezone
            '''
            result = self._values.get("time_zone")
            assert result is not None, "Required property 'time_zone' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"days": "days", "start_time": "startTime"},
    )
    class WeeklyScheduleProperty:
        def __init__(
            self,
            *,
            days: typing.Sequence[builtins.str],
            start_time: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.TimeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A weekly schedule.

            :param days: The weekly schedule's days.
            :param start_time: The weekly schedule's start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                weekly_schedule_property = inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty(
                    days=["days"],
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d30b6b9756e498926a5cf63c7bbf5e7f937d68b176005d1670779697c6b3abb4)
                check_type(argname="argument days", value=days, expected_type=type_hints["days"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "days": days,
                "start_time": start_time,
            }

        @builtins.property
        def days(self) -> typing.List[builtins.str]:
            '''The weekly schedule's days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule.html#cfn-inspectorv2-cisscanconfiguration-weeklyschedule-days
            '''
            result = self._values.get("days")
            assert result is not None, "Required property 'days' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def start_time(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.TimeProperty"]:
            '''The weekly schedule's start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule.html#cfn-inspectorv2-cisscanconfiguration-weeklyschedule-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.TimeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WeeklyScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "scan_name": "scanName",
        "schedule": "schedule",
        "security_level": "securityLevel",
        "targets": "targets",
        "tags": "tags",
    },
)
class CfnCisScanConfigurationProps:
    def __init__(
        self,
        *,
        scan_name: builtins.str,
        schedule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]],
        security_level: builtins.str,
        targets: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCisScanConfiguration.CisTargetsProperty", typing.Dict[builtins.str, typing.Any]]],
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCisScanConfiguration``.

        :param scan_name: The name of the CIS scan configuration.
        :param schedule: The CIS scan configuration's schedule.
        :param security_level: The CIS scan configuration's CIS Benchmark level.
        :param targets: The CIS scan configuration's targets.
        :param tags: The CIS scan configuration's tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_inspectorv2 as inspectorv2
            
            # one_time: Any
            
            cfn_cis_scan_configuration_props = inspectorv2.CfnCisScanConfigurationProps(
                scan_name="scanName",
                schedule=inspectorv2.CfnCisScanConfiguration.ScheduleProperty(
                    daily=inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty(
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    ),
                    monthly=inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty(
                        day="day",
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    ),
                    one_time=one_time,
                    weekly=inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty(
                        days=["days"],
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    )
                ),
                security_level="securityLevel",
                targets=inspectorv2.CfnCisScanConfiguration.CisTargetsProperty(
                    account_ids=["accountIds"],
                    target_resource_tags={
                        "target_resource_tags_key": ["targetResourceTags"]
                    }
                ),
            
                # the properties below are optional
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f0430cb9cf97c73c0c85526ac298bc695a6c9d3bf5e578a6d9b5c85d5623dc)
            check_type(argname="argument scan_name", value=scan_name, expected_type=type_hints["scan_name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument security_level", value=security_level, expected_type=type_hints["security_level"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scan_name": scan_name,
            "schedule": schedule,
            "security_level": security_level,
            "targets": targets,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def scan_name(self) -> builtins.str:
        '''The name of the CIS scan configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-scanname
        '''
        result = self._values.get("scan_name")
        assert result is not None, "Required property 'scan_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.ScheduleProperty"]:
        '''The CIS scan configuration's schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-schedule
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.ScheduleProperty"], result)

    @builtins.property
    def security_level(self) -> builtins.str:
        '''The CIS scan configuration's CIS Benchmark level.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-securitylevel
        '''
        result = self._values.get("security_level")
        assert result is not None, "Required property 'security_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.CisTargetsProperty"]:
        '''The CIS scan configuration's targets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-targets
        '''
        result = self._values.get("targets")
        assert result is not None, "Required property 'targets' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCisScanConfiguration.CisTargetsProperty"], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The CIS scan configuration's tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCisScanConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ICodeSecurityIntegrationRef_b418c2a5, _ITaggableV2_4e6798f8)
class CfnCodeSecurityIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityIntegration",
):
    '''Creates a code security integration with a source code repository provider.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityintegration.html
    :cloudformationResource: AWS::InspectorV2::CodeSecurityIntegration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_inspectorv2 as inspectorv2
        
        cfn_code_security_integration = inspectorv2.CfnCodeSecurityIntegration(self, "MyCfnCodeSecurityIntegration",
            create_integration_details=inspectorv2.CfnCodeSecurityIntegration.CreateDetailsProperty(
                gitlab_self_managed=inspectorv2.CfnCodeSecurityIntegration.CreateGitLabSelfManagedIntegrationDetailProperty(
                    access_token="accessToken",
                    instance_url="instanceUrl"
                )
            ),
            name="name",
            tags={
                "tags_key": "tags"
            },
            type="type",
            update_integration_details=inspectorv2.CfnCodeSecurityIntegration.UpdateDetailsProperty(
                github=inspectorv2.CfnCodeSecurityIntegration.UpdateGitHubIntegrationDetailProperty(
                    code="code",
                    installation_id="installationId"
                ),
                gitlab_self_managed=inspectorv2.CfnCodeSecurityIntegration.UpdateGitLabSelfManagedIntegrationDetailProperty(
                    auth_code="authCode"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        create_integration_details: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityIntegration.CreateDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        update_integration_details: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityIntegration.UpdateDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::InspectorV2::CodeSecurityIntegration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param create_integration_details: Contains details required to create a code security integration with a specific repository provider.
        :param name: The name of the code security integration.
        :param tags: The tags to apply to the code security integration.
        :param type: The type of repository provider for the integration.
        :param update_integration_details: The updated integration details specific to the repository provider type.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80799b4356912cf375014b9f868e52ed37e885f4e1f3c1ddd85598a234badc5f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCodeSecurityIntegrationProps(
            create_integration_details=create_integration_details,
            name=name,
            tags=tags,
            type=type,
            update_integration_details=update_integration_details,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForCodeSecurityIntegration")
    @builtins.classmethod
    def arn_for_code_security_integration(
        cls,
        resource: "_ICodeSecurityIntegrationRef_b418c2a5",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ca7e2752a7e90b087558c274f5098a9e8bc7c5d74e989dc2358c5a144c1d57e)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForCodeSecurityIntegration", [resource]))

    @jsii.member(jsii_name="isCfnCodeSecurityIntegration")
    @builtins.classmethod
    def is_cfn_code_security_integration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnCodeSecurityIntegration.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b98f80c5b07b3b4699f81f95546fed657ea28fce1615629bee70f86785ce350f)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnCodeSecurityIntegration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2b41111bd2e5e5f072f8545fffa3c791a4d0e501f547576454bf1a1f74205d6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a995b0a871c5ed338d9451bbbe7895dc95cb1d56fb43ef4d2d9d854ffdeb8a66)
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
        '''The Amazon Resource Name (ARN) of the code security integration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAuthorizationUrl")
    def attr_authorization_url(self) -> builtins.str:
        '''The URL used to authorize the integration with the repository provider.

        :cloudformationAttribute: AuthorizationUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAuthorizationUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the code security integration was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The timestamp when the code security integration was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the integration.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''The reason for the current status of the code security integration.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

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
    @jsii.member(jsii_name="codeSecurityIntegrationRef")
    def code_security_integration_ref(
        self,
    ) -> "_CodeSecurityIntegrationReference_0787ed51":
        '''A reference to a CodeSecurityIntegration resource.'''
        return typing.cast("_CodeSecurityIntegrationReference_0787ed51", jsii.get(self, "codeSecurityIntegrationRef"))

    @builtins.property
    @jsii.member(jsii_name="createIntegrationDetails")
    def create_integration_details(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.CreateDetailsProperty"]]:
        '''Contains details required to create a code security integration with a specific repository provider.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.CreateDetailsProperty"]], jsii.get(self, "createIntegrationDetails"))

    @create_integration_details.setter
    def create_integration_details(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.CreateDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95bada6a0a63eed0487660762db52cf7634424d68b180f5bdde1aa127cbc6ca1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createIntegrationDetails", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the code security integration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62c672b1420b745cd7e45b7351f3382ced028744668c9771a1148fe207c23267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags to apply to the code security integration.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56217870c5b8873ef3b3750235b4baa957fcd999c408c688e231f957b297af0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of repository provider for the integration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e81de92c5a50f951f013bc7d558d9d09c3c119459f7f1a04ca44ba5291a994ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="updateIntegrationDetails")
    def update_integration_details(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.UpdateDetailsProperty"]]:
        '''The updated integration details specific to the repository provider type.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.UpdateDetailsProperty"]], jsii.get(self, "updateIntegrationDetails"))

    @update_integration_details.setter
    def update_integration_details(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.UpdateDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c450107a89d380f98e1bb112fb4f8df187acd5d7b74c42bca8a125923588adc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "updateIntegrationDetails", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityIntegration.CreateDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"gitlab_self_managed": "gitlabSelfManaged"},
    )
    class CreateDetailsProperty:
        def __init__(
            self,
            *,
            gitlab_self_managed: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityIntegration.CreateGitLabSelfManagedIntegrationDetailProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains details required to create a code security integration with a specific repository provider.

            :param gitlab_self_managed: Details specific to creating an integration with a self-managed GitLab instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-createdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                create_details_property = inspectorv2.CfnCodeSecurityIntegration.CreateDetailsProperty(
                    gitlab_self_managed=inspectorv2.CfnCodeSecurityIntegration.CreateGitLabSelfManagedIntegrationDetailProperty(
                        access_token="accessToken",
                        instance_url="instanceUrl"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2262215d3482ab65dacec2a9b346848e87bce266386fcf679cd7607f925a41a9)
                check_type(argname="argument gitlab_self_managed", value=gitlab_self_managed, expected_type=type_hints["gitlab_self_managed"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "gitlab_self_managed": gitlab_self_managed,
            }

        @builtins.property
        def gitlab_self_managed(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.CreateGitLabSelfManagedIntegrationDetailProperty"]:
            '''Details specific to creating an integration with a self-managed GitLab instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-createdetails.html#cfn-inspectorv2-codesecurityintegration-createdetails-gitlabselfmanaged
            '''
            result = self._values.get("gitlab_self_managed")
            assert result is not None, "Required property 'gitlab_self_managed' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.CreateGitLabSelfManagedIntegrationDetailProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreateDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityIntegration.CreateGitLabSelfManagedIntegrationDetailProperty",
        jsii_struct_bases=[],
        name_mapping={"access_token": "accessToken", "instance_url": "instanceUrl"},
    )
    class CreateGitLabSelfManagedIntegrationDetailProperty:
        def __init__(
            self,
            *,
            access_token: builtins.str,
            instance_url: builtins.str,
        ) -> None:
            '''Contains details required to create an integration with a self-managed GitLab instance.

            :param access_token: The personal access token used to authenticate with the self-managed GitLab instance.
            :param instance_url: The URL of the self-managed GitLab instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                create_git_lab_self_managed_integration_detail_property = inspectorv2.CfnCodeSecurityIntegration.CreateGitLabSelfManagedIntegrationDetailProperty(
                    access_token="accessToken",
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0bbc1b28a8c4770b506b8b2fbbfde8238181c9ccb84cf76f6b88eefb2a36575c)
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "access_token": access_token,
                "instance_url": instance_url,
            }

        @builtins.property
        def access_token(self) -> builtins.str:
            '''The personal access token used to authenticate with the self-managed GitLab instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail.html#cfn-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-accesstoken
            '''
            result = self._values.get("access_token")
            assert result is not None, "Required property 'access_token' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''The URL of the self-managed GitLab instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail.html#cfn-inspectorv2-codesecurityintegration-creategitlabselfmanagedintegrationdetail-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreateGitLabSelfManagedIntegrationDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityIntegration.UpdateDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"github": "github", "gitlab_self_managed": "gitlabSelfManaged"},
    )
    class UpdateDetailsProperty:
        def __init__(
            self,
            *,
            github: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityIntegration.UpdateGitHubIntegrationDetailProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            gitlab_self_managed: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityIntegration.UpdateGitLabSelfManagedIntegrationDetailProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains details required to update a code security integration with a specific repository provider.

            :param github: Details specific to updating an integration with GitHub.
            :param gitlab_self_managed: Details specific to updating an integration with a self-managed GitLab instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-updatedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                update_details_property = inspectorv2.CfnCodeSecurityIntegration.UpdateDetailsProperty(
                    github=inspectorv2.CfnCodeSecurityIntegration.UpdateGitHubIntegrationDetailProperty(
                        code="code",
                        installation_id="installationId"
                    ),
                    gitlab_self_managed=inspectorv2.CfnCodeSecurityIntegration.UpdateGitLabSelfManagedIntegrationDetailProperty(
                        auth_code="authCode"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__49eb1e2e3f4009317c4c9d3bde00d5f76e2edded22c78e79a48f4596be9ae8b8)
                check_type(argname="argument github", value=github, expected_type=type_hints["github"])
                check_type(argname="argument gitlab_self_managed", value=gitlab_self_managed, expected_type=type_hints["gitlab_self_managed"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if github is not None:
                self._values["github"] = github
            if gitlab_self_managed is not None:
                self._values["gitlab_self_managed"] = gitlab_self_managed

        @builtins.property
        def github(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.UpdateGitHubIntegrationDetailProperty"]]:
            '''Details specific to updating an integration with GitHub.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-updatedetails.html#cfn-inspectorv2-codesecurityintegration-updatedetails-github
            '''
            result = self._values.get("github")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.UpdateGitHubIntegrationDetailProperty"]], result)

        @builtins.property
        def gitlab_self_managed(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.UpdateGitLabSelfManagedIntegrationDetailProperty"]]:
            '''Details specific to updating an integration with a self-managed GitLab instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-updatedetails.html#cfn-inspectorv2-codesecurityintegration-updatedetails-gitlabselfmanaged
            '''
            result = self._values.get("gitlab_self_managed")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.UpdateGitLabSelfManagedIntegrationDetailProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityIntegration.UpdateGitHubIntegrationDetailProperty",
        jsii_struct_bases=[],
        name_mapping={"code": "code", "installation_id": "installationId"},
    )
    class UpdateGitHubIntegrationDetailProperty:
        def __init__(
            self,
            *,
            code: builtins.str,
            installation_id: builtins.str,
        ) -> None:
            '''Contains details required to update an integration with GitHub.

            :param code: The authorization code received from GitHub to update the integration.
            :param installation_id: The installation ID of the GitHub App associated with the integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                update_git_hub_integration_detail_property = inspectorv2.CfnCodeSecurityIntegration.UpdateGitHubIntegrationDetailProperty(
                    code="code",
                    installation_id="installationId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b3487b0f19d852a82df38914d0b6e860cbf9001a42d8401b18e0a1768ad4cb7)
                check_type(argname="argument code", value=code, expected_type=type_hints["code"])
                check_type(argname="argument installation_id", value=installation_id, expected_type=type_hints["installation_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "code": code,
                "installation_id": installation_id,
            }

        @builtins.property
        def code(self) -> builtins.str:
            '''The authorization code received from GitHub to update the integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail.html#cfn-inspectorv2-codesecurityintegration-updategithubintegrationdetail-code
            '''
            result = self._values.get("code")
            assert result is not None, "Required property 'code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def installation_id(self) -> builtins.str:
            '''The installation ID of the GitHub App associated with the integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-updategithubintegrationdetail.html#cfn-inspectorv2-codesecurityintegration-updategithubintegrationdetail-installationid
            '''
            result = self._values.get("installation_id")
            assert result is not None, "Required property 'installation_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateGitHubIntegrationDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityIntegration.UpdateGitLabSelfManagedIntegrationDetailProperty",
        jsii_struct_bases=[],
        name_mapping={"auth_code": "authCode"},
    )
    class UpdateGitLabSelfManagedIntegrationDetailProperty:
        def __init__(self, *, auth_code: builtins.str) -> None:
            '''Contains details required to update an integration with a self-managed GitLab instance.

            :param auth_code: The authorization code received from the self-managed GitLab instance to update the integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                update_git_lab_self_managed_integration_detail_property = inspectorv2.CfnCodeSecurityIntegration.UpdateGitLabSelfManagedIntegrationDetailProperty(
                    auth_code="authCode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e29538aad68be3e1d38e6aa515bc380b1c5dbb5fcc5c4ed65df930696a81461)
                check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "auth_code": auth_code,
            }

        @builtins.property
        def auth_code(self) -> builtins.str:
            '''The authorization code received from the self-managed GitLab instance to update the integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail.html#cfn-inspectorv2-codesecurityintegration-updategitlabselfmanagedintegrationdetail-authcode
            '''
            result = self._values.get("auth_code")
            assert result is not None, "Required property 'auth_code' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpdateGitLabSelfManagedIntegrationDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "create_integration_details": "createIntegrationDetails",
        "name": "name",
        "tags": "tags",
        "type": "type",
        "update_integration_details": "updateIntegrationDetails",
    },
)
class CfnCodeSecurityIntegrationProps:
    def __init__(
        self,
        *,
        create_integration_details: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityIntegration.CreateDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        type: typing.Optional[builtins.str] = None,
        update_integration_details: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityIntegration.UpdateDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCodeSecurityIntegration``.

        :param create_integration_details: Contains details required to create a code security integration with a specific repository provider.
        :param name: The name of the code security integration.
        :param tags: The tags to apply to the code security integration.
        :param type: The type of repository provider for the integration.
        :param update_integration_details: The updated integration details specific to the repository provider type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityintegration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_inspectorv2 as inspectorv2
            
            cfn_code_security_integration_props = inspectorv2.CfnCodeSecurityIntegrationProps(
                create_integration_details=inspectorv2.CfnCodeSecurityIntegration.CreateDetailsProperty(
                    gitlab_self_managed=inspectorv2.CfnCodeSecurityIntegration.CreateGitLabSelfManagedIntegrationDetailProperty(
                        access_token="accessToken",
                        instance_url="instanceUrl"
                    )
                ),
                name="name",
                tags={
                    "tags_key": "tags"
                },
                type="type",
                update_integration_details=inspectorv2.CfnCodeSecurityIntegration.UpdateDetailsProperty(
                    github=inspectorv2.CfnCodeSecurityIntegration.UpdateGitHubIntegrationDetailProperty(
                        code="code",
                        installation_id="installationId"
                    ),
                    gitlab_self_managed=inspectorv2.CfnCodeSecurityIntegration.UpdateGitLabSelfManagedIntegrationDetailProperty(
                        auth_code="authCode"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71aafe099f5a07cc45a5a16ed7c8165fc3beaaf581b2a7075ad79583b48897ae)
            check_type(argname="argument create_integration_details", value=create_integration_details, expected_type=type_hints["create_integration_details"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument update_integration_details", value=update_integration_details, expected_type=type_hints["update_integration_details"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if create_integration_details is not None:
            self._values["create_integration_details"] = create_integration_details
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type
        if update_integration_details is not None:
            self._values["update_integration_details"] = update_integration_details

    @builtins.property
    def create_integration_details(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.CreateDetailsProperty"]]:
        '''Contains details required to create a code security integration with a specific repository provider.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityintegration.html#cfn-inspectorv2-codesecurityintegration-createintegrationdetails
        '''
        result = self._values.get("create_integration_details")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.CreateDetailsProperty"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the code security integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityintegration.html#cfn-inspectorv2-codesecurityintegration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags to apply to the code security integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityintegration.html#cfn-inspectorv2-codesecurityintegration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of repository provider for the integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityintegration.html#cfn-inspectorv2-codesecurityintegration-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update_integration_details(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.UpdateDetailsProperty"]]:
        '''The updated integration details specific to the repository provider type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityintegration.html#cfn-inspectorv2-codesecurityintegration-updateintegrationdetails
        '''
        result = self._values.get("update_integration_details")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityIntegration.UpdateDetailsProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeSecurityIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ICodeSecurityScanConfigurationRef_4a00a90e, _ITaggableV2_4e6798f8)
class CfnCodeSecurityScanConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityScanConfiguration",
):
    '''Creates a scan configuration for code security scanning.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityscanconfiguration.html
    :cloudformationResource: AWS::InspectorV2::CodeSecurityScanConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_inspectorv2 as inspectorv2
        
        cfn_code_security_scan_configuration = inspectorv2.CfnCodeSecurityScanConfiguration(self, "MyCfnCodeSecurityScanConfiguration",
            configuration=inspectorv2.CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty(
                rule_set_categories=["ruleSetCategories"],
        
                # the properties below are optional
                continuous_integration_scan_configuration=inspectorv2.CfnCodeSecurityScanConfiguration.ContinuousIntegrationScanConfigurationProperty(
                    supported_events=["supportedEvents"]
                ),
                periodic_scan_configuration=inspectorv2.CfnCodeSecurityScanConfiguration.PeriodicScanConfigurationProperty(
                    frequency="frequency",
                    frequency_expression="frequencyExpression"
                )
            ),
            level="level",
            name="name",
            scope_settings=inspectorv2.CfnCodeSecurityScanConfiguration.ScopeSettingsProperty(
                project_selection_scope="projectSelectionScope"
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
        configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        scope_settings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityScanConfiguration.ScopeSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::InspectorV2::CodeSecurityScanConfiguration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: The configuration settings for the code security scan.
        :param level: The security level for the scan configuration.
        :param name: The name of the scan configuration.
        :param scope_settings: The scope settings that define which repositories will be scanned.
        :param tags: The tags to apply to the scan configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8087fd99eb325ae09773df4a6c219dda10efe85e43341cb1f5b576a1e88cef)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCodeSecurityScanConfigurationProps(
            configuration=configuration,
            level=level,
            name=name,
            scope_settings=scope_settings,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForCodeSecurityScanConfiguration")
    @builtins.classmethod
    def arn_for_code_security_scan_configuration(
        cls,
        resource: "_ICodeSecurityScanConfigurationRef_4a00a90e",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e2ba232f61f3996b58dc5cfd25237fcbd03e5685907e35ac8cd5f40d55260b)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForCodeSecurityScanConfiguration", [resource]))

    @jsii.member(jsii_name="isCfnCodeSecurityScanConfiguration")
    @builtins.classmethod
    def is_cfn_code_security_scan_configuration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnCodeSecurityScanConfiguration.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1f6d967d4a3eb9c698e7e4d9da2813e02cf4fa4c7e56bc813ceb4ed4d3d1817)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnCodeSecurityScanConfiguration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb6f2f1a541e759bd4ebb9f175ef2898e08b44a5a2f74698a104ebf563f6050)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ba67d1221ac83994db1e0ae5a5f4d8d289116bd2bbba3ba9086ac33ff847516)
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
        '''The Amazon Resource Name (ARN) of the scan configuration.

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
    @jsii.member(jsii_name="codeSecurityScanConfigurationRef")
    def code_security_scan_configuration_ref(
        self,
    ) -> "_CodeSecurityScanConfigurationReference_b4a97ccc":
        '''A reference to a CodeSecurityScanConfiguration resource.'''
        return typing.cast("_CodeSecurityScanConfigurationReference_b4a97ccc", jsii.get(self, "codeSecurityScanConfigurationRef"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty"]]:
        '''The configuration settings for the code security scan.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty"]], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45b63b68b5efac81af01f69f6fc536a7e0c56ab5d78f7c4d82199c868ce47b16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> typing.Optional[builtins.str]:
        '''The security level for the scan configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "level"))

    @level.setter
    def level(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80291f0cd7a0cb5b5f295442d46a5d028aa373ed833a3fb0e3b6091879e1a69b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the scan configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10ce312b3f34f6350a3d1ee625199c03f68c9cb605f5e399d8d24b0f3374d219)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scopeSettings")
    def scope_settings(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.ScopeSettingsProperty"]]:
        '''The scope settings that define which repositories will be scanned.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.ScopeSettingsProperty"]], jsii.get(self, "scopeSettings"))

    @scope_settings.setter
    def scope_settings(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.ScopeSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2418e2e1becb18ab1d3613df2cc71f18c45d161aa5b3aa4b796643c5c109a1b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scopeSettings", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags to apply to the scan configuration.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9428e2a90cc0578e6f07997b18e25682dcdf69843515552c29dd20aa94e714a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rule_set_categories": "ruleSetCategories",
            "continuous_integration_scan_configuration": "continuousIntegrationScanConfiguration",
            "periodic_scan_configuration": "periodicScanConfiguration",
        },
    )
    class CodeSecurityScanConfigurationProperty:
        def __init__(
            self,
            *,
            rule_set_categories: typing.Sequence[builtins.str],
            continuous_integration_scan_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityScanConfiguration.ContinuousIntegrationScanConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            periodic_scan_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityScanConfiguration.PeriodicScanConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains the configuration settings for code security scans.

            :param rule_set_categories: The categories of security rules to be applied during the scan.
            :param continuous_integration_scan_configuration: Configuration settings for continuous integration scans that run automatically when code changes are made.
            :param periodic_scan_configuration: Configuration settings for periodic scans that run on a scheduled basis.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                code_security_scan_configuration_property = inspectorv2.CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty(
                    rule_set_categories=["ruleSetCategories"],
                
                    # the properties below are optional
                    continuous_integration_scan_configuration=inspectorv2.CfnCodeSecurityScanConfiguration.ContinuousIntegrationScanConfigurationProperty(
                        supported_events=["supportedEvents"]
                    ),
                    periodic_scan_configuration=inspectorv2.CfnCodeSecurityScanConfiguration.PeriodicScanConfigurationProperty(
                        frequency="frequency",
                        frequency_expression="frequencyExpression"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e69a31a73796f4b8caaf249f9369b948bbd3cba1089b94bed6018c89696c89cc)
                check_type(argname="argument rule_set_categories", value=rule_set_categories, expected_type=type_hints["rule_set_categories"])
                check_type(argname="argument continuous_integration_scan_configuration", value=continuous_integration_scan_configuration, expected_type=type_hints["continuous_integration_scan_configuration"])
                check_type(argname="argument periodic_scan_configuration", value=periodic_scan_configuration, expected_type=type_hints["periodic_scan_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rule_set_categories": rule_set_categories,
            }
            if continuous_integration_scan_configuration is not None:
                self._values["continuous_integration_scan_configuration"] = continuous_integration_scan_configuration
            if periodic_scan_configuration is not None:
                self._values["periodic_scan_configuration"] = periodic_scan_configuration

        @builtins.property
        def rule_set_categories(self) -> typing.List[builtins.str]:
            '''The categories of security rules to be applied during the scan.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-rulesetcategories
            '''
            result = self._values.get("rule_set_categories")
            assert result is not None, "Required property 'rule_set_categories' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def continuous_integration_scan_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.ContinuousIntegrationScanConfigurationProperty"]]:
            '''Configuration settings for continuous integration scans that run automatically when code changes are made.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-continuousintegrationscanconfiguration
            '''
            result = self._values.get("continuous_integration_scan_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.ContinuousIntegrationScanConfigurationProperty"]], result)

        @builtins.property
        def periodic_scan_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.PeriodicScanConfigurationProperty"]]:
            '''Configuration settings for periodic scans that run on a scheduled basis.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-codesecurityscanconfiguration-periodicscanconfiguration
            '''
            result = self._values.get("periodic_scan_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.PeriodicScanConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeSecurityScanConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityScanConfiguration.ContinuousIntegrationScanConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"supported_events": "supportedEvents"},
    )
    class ContinuousIntegrationScanConfigurationProperty:
        def __init__(self, *, supported_events: typing.Sequence[builtins.str]) -> None:
            '''Configuration settings for continuous integration scans that run automatically when code changes are made.

            :param supported_events: The repository events that trigger continuous integration scans, such as pull requests or commits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                continuous_integration_scan_configuration_property = inspectorv2.CfnCodeSecurityScanConfiguration.ContinuousIntegrationScanConfigurationProperty(
                    supported_events=["supportedEvents"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__04bdb61b43cbfbc6d92a4c02a47e71f63015162a7acf1e60ef409eebcd21a9f2)
                check_type(argname="argument supported_events", value=supported_events, expected_type=type_hints["supported_events"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "supported_events": supported_events,
            }

        @builtins.property
        def supported_events(self) -> typing.List[builtins.str]:
            '''The repository events that trigger continuous integration scans, such as pull requests or commits.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-continuousintegrationscanconfiguration-supportedevents
            '''
            result = self._values.get("supported_events")
            assert result is not None, "Required property 'supported_events' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContinuousIntegrationScanConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityScanConfiguration.PeriodicScanConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "frequency": "frequency",
            "frequency_expression": "frequencyExpression",
        },
    )
    class PeriodicScanConfigurationProperty:
        def __init__(
            self,
            *,
            frequency: typing.Optional[builtins.str] = None,
            frequency_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration settings for periodic scans that run on a scheduled basis.

            :param frequency: The frequency at which periodic scans are performed (such as weekly or monthly). If you don't provide the ``frequencyExpression`` Amazon Inspector chooses day for the scan to run. If you provide the ``frequencyExpression`` , the schedule must match the specified ``frequency`` .
            :param frequency_expression: The schedule expression for periodic scans, in cron format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                periodic_scan_configuration_property = inspectorv2.CfnCodeSecurityScanConfiguration.PeriodicScanConfigurationProperty(
                    frequency="frequency",
                    frequency_expression="frequencyExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__901beb5d14c9e234fd835b4523197f824e50f091ed2dcfbca59aef2f1f023dde)
                check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
                check_type(argname="argument frequency_expression", value=frequency_expression, expected_type=type_hints["frequency_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if frequency is not None:
                self._values["frequency"] = frequency
            if frequency_expression is not None:
                self._values["frequency_expression"] = frequency_expression

        @builtins.property
        def frequency(self) -> typing.Optional[builtins.str]:
            '''The frequency at which periodic scans are performed (such as weekly or monthly).

            If you don't provide the ``frequencyExpression`` Amazon Inspector chooses day for the scan to run. If you provide the ``frequencyExpression`` , the schedule must match the specified ``frequency`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-frequency
            '''
            result = self._values.get("frequency")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def frequency_expression(self) -> typing.Optional[builtins.str]:
            '''The schedule expression for periodic scans, in cron format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-periodicscanconfiguration-frequencyexpression
            '''
            result = self._values.get("frequency_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PeriodicScanConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityScanConfiguration.ScopeSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"project_selection_scope": "projectSelectionScope"},
    )
    class ScopeSettingsProperty:
        def __init__(
            self,
            *,
            project_selection_scope: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The scope settings that define which repositories will be scanned.

            If the ``ScopeSetting`` parameter is ``ALL`` the scan configuration applies to all existing and future projects imported into Amazon Inspector .

            :param project_selection_scope: The scope of projects to be selected for scanning within the integrated repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-scopesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                scope_settings_property = inspectorv2.CfnCodeSecurityScanConfiguration.ScopeSettingsProperty(
                    project_selection_scope="projectSelectionScope"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__911607f762372da4ac39dfe813875203be92e9a87447c67741aae32d569743dc)
                check_type(argname="argument project_selection_scope", value=project_selection_scope, expected_type=type_hints["project_selection_scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if project_selection_scope is not None:
                self._values["project_selection_scope"] = project_selection_scope

        @builtins.property
        def project_selection_scope(self) -> typing.Optional[builtins.str]:
            '''The scope of projects to be selected for scanning within the integrated repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-codesecurityscanconfiguration-scopesettings.html#cfn-inspectorv2-codesecurityscanconfiguration-scopesettings-projectselectionscope
            '''
            result = self._values.get("project_selection_scope")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScopeSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCodeSecurityScanConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "level": "level",
        "name": "name",
        "scope_settings": "scopeSettings",
        "tags": "tags",
    },
)
class CfnCodeSecurityScanConfigurationProps:
    def __init__(
        self,
        *,
        configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        level: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        scope_settings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeSecurityScanConfiguration.ScopeSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCodeSecurityScanConfiguration``.

        :param configuration: The configuration settings for the code security scan.
        :param level: The security level for the scan configuration.
        :param name: The name of the scan configuration.
        :param scope_settings: The scope settings that define which repositories will be scanned.
        :param tags: The tags to apply to the scan configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityscanconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_inspectorv2 as inspectorv2
            
            cfn_code_security_scan_configuration_props = inspectorv2.CfnCodeSecurityScanConfigurationProps(
                configuration=inspectorv2.CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty(
                    rule_set_categories=["ruleSetCategories"],
            
                    # the properties below are optional
                    continuous_integration_scan_configuration=inspectorv2.CfnCodeSecurityScanConfiguration.ContinuousIntegrationScanConfigurationProperty(
                        supported_events=["supportedEvents"]
                    ),
                    periodic_scan_configuration=inspectorv2.CfnCodeSecurityScanConfiguration.PeriodicScanConfigurationProperty(
                        frequency="frequency",
                        frequency_expression="frequencyExpression"
                    )
                ),
                level="level",
                name="name",
                scope_settings=inspectorv2.CfnCodeSecurityScanConfiguration.ScopeSettingsProperty(
                    project_selection_scope="projectSelectionScope"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ea2faaa39ad7a4370f1a43aa967ae3ded5ad2ac9c212905e92dd56f603ec204)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scope_settings", value=scope_settings, expected_type=type_hints["scope_settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if configuration is not None:
            self._values["configuration"] = configuration
        if level is not None:
            self._values["level"] = level
        if name is not None:
            self._values["name"] = name
        if scope_settings is not None:
            self._values["scope_settings"] = scope_settings
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty"]]:
        '''The configuration settings for the code security scan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-configuration
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty"]], result)

    @builtins.property
    def level(self) -> typing.Optional[builtins.str]:
        '''The security level for the scan configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-level
        '''
        result = self._values.get("level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the scan configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope_settings(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.ScopeSettingsProperty"]]:
        '''The scope settings that define which repositories will be scanned.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-scopesettings
        '''
        result = self._values.get("scope_settings")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeSecurityScanConfiguration.ScopeSettingsProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags to apply to the scan configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-codesecurityscanconfiguration.html#cfn-inspectorv2-codesecurityscanconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeSecurityScanConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IFilterRef_37875571, _ITaggableV2_4e6798f8)
class CfnFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter",
):
    '''Details about a filter.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html
    :cloudformationResource: AWS::InspectorV2::Filter
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_inspectorv2 as inspectorv2
        
        cfn_filter = inspectorv2.CfnFilter(self, "MyCfnFilter",
            filter_action="filterAction",
            filter_criteria=inspectorv2.CfnFilter.FilterCriteriaProperty(
                aws_account_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                code_vulnerability_detector_name=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                code_vulnerability_detector_tags=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                code_vulnerability_file_path=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                component_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                component_type=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ec2_instance_image_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ec2_instance_subnet_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ec2_instance_vpc_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_architecture=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_hash=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_pushed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )],
                ecr_image_registry=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_repository_name=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_tags=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                epss_score=[inspectorv2.CfnFilter.NumberFilterProperty(
                    lower_inclusive=123,
                    upper_inclusive=123
                )],
                exploit_available=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_arn=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_status=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_type=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                first_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )],
                fix_available=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                inspector_score=[inspectorv2.CfnFilter.NumberFilterProperty(
                    lower_inclusive=123,
                    upper_inclusive=123
                )],
                lambda_function_execution_role_arn=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                lambda_function_last_modified_at=[inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )],
                lambda_function_layers=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                lambda_function_name=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                lambda_function_runtime=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                last_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )],
                network_protocol=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                port_range=[inspectorv2.CfnFilter.PortRangeFilterProperty(
                    begin_inclusive=123,
                    end_inclusive=123
                )],
                related_vulnerabilities=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_tags=[inspectorv2.CfnFilter.MapFilterProperty(
                    comparison="comparison",
        
                    # the properties below are optional
                    key="key",
                    value="value"
                )],
                resource_type=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                severity=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                title=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                updated_at=[inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )],
                vendor_severity=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                vulnerability_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                vulnerability_source=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                vulnerable_packages=[inspectorv2.CfnFilter.PackageFilterProperty(
                    architecture=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    epoch=inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    ),
                    file_path=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    name=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    release=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    source_lambda_layer_arn=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    source_layer_hash=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    version=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )
                )]
            ),
            name="name",
        
            # the properties below are optional
            description="description",
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
        filter_action: builtins.str,
        filter_criteria: typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.FilterCriteriaProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::InspectorV2::Filter``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param filter_action: The action that is to be applied to the findings that match the filter.
        :param filter_criteria: Details on the filter criteria associated with this filter.
        :param name: The name of the filter.
        :param description: A description of the filter.
        :param tags: The tags attached to the filter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76aaac8f8d755716225a5dd2d4902f3e7ec007381fa82a2d163553362c975c9d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFilterProps(
            filter_action=filter_action,
            filter_criteria=filter_criteria,
            name=name,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForFilter")
    @builtins.classmethod
    def arn_for_filter(cls, resource: "_IFilterRef_37875571") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704d307380b328e752813838e45cc7632f81ee6e606de43e80cdab6fbc9f46bb)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForFilter", [resource]))

    @jsii.member(jsii_name="isCfnFilter")
    @builtins.classmethod
    def is_cfn_filter(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFilter.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e088efafc9f496c3c6fa7871d5344534a4487772b0dada5b37c9bf1911c2234)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFilter", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daeca541bed43f62727b37c4048db034533d9b1614725f3cf4c361b77df5323e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__02055b54b230012a61c4a22e04d2fc0ffa08a47a06385a880a1db32a3f55f237)
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
        '''The Amazon Resource Number (ARN) associated with this filter.

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
    @jsii.member(jsii_name="filterRef")
    def filter_ref(self) -> "_FilterReference_d368c0f2":
        '''A reference to a Filter resource.'''
        return typing.cast("_FilterReference_d368c0f2", jsii.get(self, "filterRef"))

    @builtins.property
    @jsii.member(jsii_name="filterAction")
    def filter_action(self) -> builtins.str:
        '''The action that is to be applied to the findings that match the filter.'''
        return typing.cast(builtins.str, jsii.get(self, "filterAction"))

    @filter_action.setter
    def filter_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a72dbbaedc7eb8a3b6da0867d3f429993d1cdfe3b095a514d2cb82730c01b31d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterAction", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="filterCriteria")
    def filter_criteria(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnFilter.FilterCriteriaProperty"]:
        '''Details on the filter criteria associated with this filter.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnFilter.FilterCriteriaProperty"], jsii.get(self, "filterCriteria"))

    @filter_criteria.setter
    def filter_criteria(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnFilter.FilterCriteriaProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b566081cfe458076187f61e1afab9cbbb5fb2cdd114aad2fa6e38280867325e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterCriteria", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the filter.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b0548c4926be9ebf2a0675883b51af78c4f6a9c034f4d0fb7a9ebfd7ad038ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the filter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29a0d69128962a2d8d478ff9197ec92d930e2284a9cbff6337d95fb1932925d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags attached to the filter.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d85ec3c1992f35abc960573e86c94eb9d5f4d6c6fd9f47728ef03d5078212f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.DateFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_inclusive": "endInclusive",
            "start_inclusive": "startInclusive",
        },
    )
    class DateFilterProperty:
        def __init__(
            self,
            *,
            end_inclusive: typing.Optional[jsii.Number] = None,
            start_inclusive: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains details on the time range used to filter findings.

            :param end_inclusive: A timestamp representing the end of the time period filtered on.
            :param start_inclusive: A timestamp representing the start of the time period filtered on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                date_filter_property = inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__412cca739fbade26efa876445772a168ea693eb111b9385ae83d92127bd547b5)
                check_type(argname="argument end_inclusive", value=end_inclusive, expected_type=type_hints["end_inclusive"])
                check_type(argname="argument start_inclusive", value=start_inclusive, expected_type=type_hints["start_inclusive"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if end_inclusive is not None:
                self._values["end_inclusive"] = end_inclusive
            if start_inclusive is not None:
                self._values["start_inclusive"] = start_inclusive

        @builtins.property
        def end_inclusive(self) -> typing.Optional[jsii.Number]:
            '''A timestamp representing the end of the time period filtered on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html#cfn-inspectorv2-filter-datefilter-endinclusive
            '''
            result = self._values.get("end_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def start_inclusive(self) -> typing.Optional[jsii.Number]:
            '''A timestamp representing the start of the time period filtered on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html#cfn-inspectorv2-filter-datefilter-startinclusive
            '''
            result = self._values.get("start_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.FilterCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_account_id": "awsAccountId",
            "code_vulnerability_detector_name": "codeVulnerabilityDetectorName",
            "code_vulnerability_detector_tags": "codeVulnerabilityDetectorTags",
            "code_vulnerability_file_path": "codeVulnerabilityFilePath",
            "component_id": "componentId",
            "component_type": "componentType",
            "ec2_instance_image_id": "ec2InstanceImageId",
            "ec2_instance_subnet_id": "ec2InstanceSubnetId",
            "ec2_instance_vpc_id": "ec2InstanceVpcId",
            "ecr_image_architecture": "ecrImageArchitecture",
            "ecr_image_hash": "ecrImageHash",
            "ecr_image_pushed_at": "ecrImagePushedAt",
            "ecr_image_registry": "ecrImageRegistry",
            "ecr_image_repository_name": "ecrImageRepositoryName",
            "ecr_image_tags": "ecrImageTags",
            "epss_score": "epssScore",
            "exploit_available": "exploitAvailable",
            "finding_arn": "findingArn",
            "finding_status": "findingStatus",
            "finding_type": "findingType",
            "first_observed_at": "firstObservedAt",
            "fix_available": "fixAvailable",
            "inspector_score": "inspectorScore",
            "lambda_function_execution_role_arn": "lambdaFunctionExecutionRoleArn",
            "lambda_function_last_modified_at": "lambdaFunctionLastModifiedAt",
            "lambda_function_layers": "lambdaFunctionLayers",
            "lambda_function_name": "lambdaFunctionName",
            "lambda_function_runtime": "lambdaFunctionRuntime",
            "last_observed_at": "lastObservedAt",
            "network_protocol": "networkProtocol",
            "port_range": "portRange",
            "related_vulnerabilities": "relatedVulnerabilities",
            "resource_id": "resourceId",
            "resource_tags": "resourceTags",
            "resource_type": "resourceType",
            "severity": "severity",
            "title": "title",
            "updated_at": "updatedAt",
            "vendor_severity": "vendorSeverity",
            "vulnerability_id": "vulnerabilityId",
            "vulnerability_source": "vulnerabilitySource",
            "vulnerable_packages": "vulnerablePackages",
        },
    )
    class FilterCriteriaProperty:
        def __init__(
            self,
            *,
            aws_account_id: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            code_vulnerability_detector_name: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            code_vulnerability_detector_tags: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            code_vulnerability_file_path: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            component_id: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            component_type: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ec2_instance_image_id: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ec2_instance_subnet_id: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ec2_instance_vpc_id: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_architecture: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_hash: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_pushed_at: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_registry: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_repository_name: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_tags: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            epss_score: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            exploit_available: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_arn: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_status: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_type: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            first_observed_at: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            fix_available: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            inspector_score: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            lambda_function_execution_role_arn: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            lambda_function_last_modified_at: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            lambda_function_layers: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            lambda_function_name: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            lambda_function_runtime: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            last_observed_at: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_protocol: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            port_range: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.PortRangeFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            related_vulnerabilities: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_id: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_tags: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.MapFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_type: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            severity: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            title: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            updated_at: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vendor_severity: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vulnerability_id: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vulnerability_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vulnerable_packages: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.PackageFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Details on the criteria used to define the filter.

            :param aws_account_id: Details of the AWS account IDs used to filter findings.
            :param code_vulnerability_detector_name: 
            :param code_vulnerability_detector_tags: 
            :param code_vulnerability_file_path: 
            :param component_id: Details of the component IDs used to filter findings.
            :param component_type: Details of the component types used to filter findings.
            :param ec2_instance_image_id: Details of the Amazon EC2 instance image IDs used to filter findings.
            :param ec2_instance_subnet_id: Details of the Amazon EC2 instance subnet IDs used to filter findings.
            :param ec2_instance_vpc_id: Details of the Amazon EC2 instance VPC IDs used to filter findings.
            :param ecr_image_architecture: Details of the Amazon ECR image architecture types used to filter findings.
            :param ecr_image_hash: Details of the Amazon ECR image hashes used to filter findings.
            :param ecr_image_pushed_at: Details on the Amazon ECR image push date and time used to filter findings.
            :param ecr_image_registry: Details on the Amazon ECR registry used to filter findings.
            :param ecr_image_repository_name: Details on the name of the Amazon ECR repository used to filter findings.
            :param ecr_image_tags: The tags attached to the Amazon ECR container image.
            :param epss_score: 
            :param exploit_available: 
            :param finding_arn: Details on the finding ARNs used to filter findings.
            :param finding_status: Details on the finding status types used to filter findings.
            :param finding_type: Details on the finding types used to filter findings.
            :param first_observed_at: Details on the date and time a finding was first seen used to filter findings.
            :param fix_available: 
            :param inspector_score: The Amazon Inspector score to filter on.
            :param lambda_function_execution_role_arn: 
            :param lambda_function_last_modified_at: 
            :param lambda_function_layers: 
            :param lambda_function_name: 
            :param lambda_function_runtime: 
            :param last_observed_at: Details on the date and time a finding was last seen used to filter findings.
            :param network_protocol: Details on network protocol used to filter findings.
            :param port_range: Details on the port ranges used to filter findings.
            :param related_vulnerabilities: Details on the related vulnerabilities used to filter findings.
            :param resource_id: Details on the resource IDs used to filter findings.
            :param resource_tags: Details on the resource tags used to filter findings.
            :param resource_type: Details on the resource types used to filter findings.
            :param severity: Details on the severity used to filter findings.
            :param title: Details on the finding title used to filter findings.
            :param updated_at: Details on the date and time a finding was last updated at used to filter findings.
            :param vendor_severity: Details on the vendor severity used to filter findings.
            :param vulnerability_id: Details on the vulnerability ID used to filter findings.
            :param vulnerability_source: Details on the vulnerability score to filter findings by.
            :param vulnerable_packages: Details on the vulnerable packages used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                filter_criteria_property = inspectorv2.CfnFilter.FilterCriteriaProperty(
                    aws_account_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    code_vulnerability_detector_name=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    code_vulnerability_detector_tags=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    code_vulnerability_file_path=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    component_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    component_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_image_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_subnet_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_vpc_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_architecture=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_hash=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_pushed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    ecr_image_registry=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_repository_name=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_tags=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    epss_score=[inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    )],
                    exploit_available=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_arn=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_status=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    first_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    fix_available=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    inspector_score=[inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    )],
                    lambda_function_execution_role_arn=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    lambda_function_last_modified_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    lambda_function_layers=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    lambda_function_name=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    lambda_function_runtime=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    last_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    network_protocol=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    port_range=[inspectorv2.CfnFilter.PortRangeFilterProperty(
                        begin_inclusive=123,
                        end_inclusive=123
                    )],
                    related_vulnerabilities=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_tags=[inspectorv2.CfnFilter.MapFilterProperty(
                        comparison="comparison",
                
                        # the properties below are optional
                        key="key",
                        value="value"
                    )],
                    resource_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    severity=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    title=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    updated_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    vendor_severity=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerability_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerability_source=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerable_packages=[inspectorv2.CfnFilter.PackageFilterProperty(
                        architecture=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        epoch=inspectorv2.CfnFilter.NumberFilterProperty(
                            lower_inclusive=123,
                            upper_inclusive=123
                        ),
                        file_path=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        name=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        release=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        source_lambda_layer_arn=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        source_layer_hash=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        version=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8bf898b4c669bfc838bf91c83d3735a9d69065b37baef35430be61dc52e3c81a)
                check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
                check_type(argname="argument code_vulnerability_detector_name", value=code_vulnerability_detector_name, expected_type=type_hints["code_vulnerability_detector_name"])
                check_type(argname="argument code_vulnerability_detector_tags", value=code_vulnerability_detector_tags, expected_type=type_hints["code_vulnerability_detector_tags"])
                check_type(argname="argument code_vulnerability_file_path", value=code_vulnerability_file_path, expected_type=type_hints["code_vulnerability_file_path"])
                check_type(argname="argument component_id", value=component_id, expected_type=type_hints["component_id"])
                check_type(argname="argument component_type", value=component_type, expected_type=type_hints["component_type"])
                check_type(argname="argument ec2_instance_image_id", value=ec2_instance_image_id, expected_type=type_hints["ec2_instance_image_id"])
                check_type(argname="argument ec2_instance_subnet_id", value=ec2_instance_subnet_id, expected_type=type_hints["ec2_instance_subnet_id"])
                check_type(argname="argument ec2_instance_vpc_id", value=ec2_instance_vpc_id, expected_type=type_hints["ec2_instance_vpc_id"])
                check_type(argname="argument ecr_image_architecture", value=ecr_image_architecture, expected_type=type_hints["ecr_image_architecture"])
                check_type(argname="argument ecr_image_hash", value=ecr_image_hash, expected_type=type_hints["ecr_image_hash"])
                check_type(argname="argument ecr_image_pushed_at", value=ecr_image_pushed_at, expected_type=type_hints["ecr_image_pushed_at"])
                check_type(argname="argument ecr_image_registry", value=ecr_image_registry, expected_type=type_hints["ecr_image_registry"])
                check_type(argname="argument ecr_image_repository_name", value=ecr_image_repository_name, expected_type=type_hints["ecr_image_repository_name"])
                check_type(argname="argument ecr_image_tags", value=ecr_image_tags, expected_type=type_hints["ecr_image_tags"])
                check_type(argname="argument epss_score", value=epss_score, expected_type=type_hints["epss_score"])
                check_type(argname="argument exploit_available", value=exploit_available, expected_type=type_hints["exploit_available"])
                check_type(argname="argument finding_arn", value=finding_arn, expected_type=type_hints["finding_arn"])
                check_type(argname="argument finding_status", value=finding_status, expected_type=type_hints["finding_status"])
                check_type(argname="argument finding_type", value=finding_type, expected_type=type_hints["finding_type"])
                check_type(argname="argument first_observed_at", value=first_observed_at, expected_type=type_hints["first_observed_at"])
                check_type(argname="argument fix_available", value=fix_available, expected_type=type_hints["fix_available"])
                check_type(argname="argument inspector_score", value=inspector_score, expected_type=type_hints["inspector_score"])
                check_type(argname="argument lambda_function_execution_role_arn", value=lambda_function_execution_role_arn, expected_type=type_hints["lambda_function_execution_role_arn"])
                check_type(argname="argument lambda_function_last_modified_at", value=lambda_function_last_modified_at, expected_type=type_hints["lambda_function_last_modified_at"])
                check_type(argname="argument lambda_function_layers", value=lambda_function_layers, expected_type=type_hints["lambda_function_layers"])
                check_type(argname="argument lambda_function_name", value=lambda_function_name, expected_type=type_hints["lambda_function_name"])
                check_type(argname="argument lambda_function_runtime", value=lambda_function_runtime, expected_type=type_hints["lambda_function_runtime"])
                check_type(argname="argument last_observed_at", value=last_observed_at, expected_type=type_hints["last_observed_at"])
                check_type(argname="argument network_protocol", value=network_protocol, expected_type=type_hints["network_protocol"])
                check_type(argname="argument port_range", value=port_range, expected_type=type_hints["port_range"])
                check_type(argname="argument related_vulnerabilities", value=related_vulnerabilities, expected_type=type_hints["related_vulnerabilities"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
                check_type(argname="argument vendor_severity", value=vendor_severity, expected_type=type_hints["vendor_severity"])
                check_type(argname="argument vulnerability_id", value=vulnerability_id, expected_type=type_hints["vulnerability_id"])
                check_type(argname="argument vulnerability_source", value=vulnerability_source, expected_type=type_hints["vulnerability_source"])
                check_type(argname="argument vulnerable_packages", value=vulnerable_packages, expected_type=type_hints["vulnerable_packages"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_account_id is not None:
                self._values["aws_account_id"] = aws_account_id
            if code_vulnerability_detector_name is not None:
                self._values["code_vulnerability_detector_name"] = code_vulnerability_detector_name
            if code_vulnerability_detector_tags is not None:
                self._values["code_vulnerability_detector_tags"] = code_vulnerability_detector_tags
            if code_vulnerability_file_path is not None:
                self._values["code_vulnerability_file_path"] = code_vulnerability_file_path
            if component_id is not None:
                self._values["component_id"] = component_id
            if component_type is not None:
                self._values["component_type"] = component_type
            if ec2_instance_image_id is not None:
                self._values["ec2_instance_image_id"] = ec2_instance_image_id
            if ec2_instance_subnet_id is not None:
                self._values["ec2_instance_subnet_id"] = ec2_instance_subnet_id
            if ec2_instance_vpc_id is not None:
                self._values["ec2_instance_vpc_id"] = ec2_instance_vpc_id
            if ecr_image_architecture is not None:
                self._values["ecr_image_architecture"] = ecr_image_architecture
            if ecr_image_hash is not None:
                self._values["ecr_image_hash"] = ecr_image_hash
            if ecr_image_pushed_at is not None:
                self._values["ecr_image_pushed_at"] = ecr_image_pushed_at
            if ecr_image_registry is not None:
                self._values["ecr_image_registry"] = ecr_image_registry
            if ecr_image_repository_name is not None:
                self._values["ecr_image_repository_name"] = ecr_image_repository_name
            if ecr_image_tags is not None:
                self._values["ecr_image_tags"] = ecr_image_tags
            if epss_score is not None:
                self._values["epss_score"] = epss_score
            if exploit_available is not None:
                self._values["exploit_available"] = exploit_available
            if finding_arn is not None:
                self._values["finding_arn"] = finding_arn
            if finding_status is not None:
                self._values["finding_status"] = finding_status
            if finding_type is not None:
                self._values["finding_type"] = finding_type
            if first_observed_at is not None:
                self._values["first_observed_at"] = first_observed_at
            if fix_available is not None:
                self._values["fix_available"] = fix_available
            if inspector_score is not None:
                self._values["inspector_score"] = inspector_score
            if lambda_function_execution_role_arn is not None:
                self._values["lambda_function_execution_role_arn"] = lambda_function_execution_role_arn
            if lambda_function_last_modified_at is not None:
                self._values["lambda_function_last_modified_at"] = lambda_function_last_modified_at
            if lambda_function_layers is not None:
                self._values["lambda_function_layers"] = lambda_function_layers
            if lambda_function_name is not None:
                self._values["lambda_function_name"] = lambda_function_name
            if lambda_function_runtime is not None:
                self._values["lambda_function_runtime"] = lambda_function_runtime
            if last_observed_at is not None:
                self._values["last_observed_at"] = last_observed_at
            if network_protocol is not None:
                self._values["network_protocol"] = network_protocol
            if port_range is not None:
                self._values["port_range"] = port_range
            if related_vulnerabilities is not None:
                self._values["related_vulnerabilities"] = related_vulnerabilities
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if resource_tags is not None:
                self._values["resource_tags"] = resource_tags
            if resource_type is not None:
                self._values["resource_type"] = resource_type
            if severity is not None:
                self._values["severity"] = severity
            if title is not None:
                self._values["title"] = title
            if updated_at is not None:
                self._values["updated_at"] = updated_at
            if vendor_severity is not None:
                self._values["vendor_severity"] = vendor_severity
            if vulnerability_id is not None:
                self._values["vulnerability_id"] = vulnerability_id
            if vulnerability_source is not None:
                self._values["vulnerability_source"] = vulnerability_source
            if vulnerable_packages is not None:
                self._values["vulnerable_packages"] = vulnerable_packages

        @builtins.property
        def aws_account_id(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the AWS account IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-awsaccountid
            '''
            result = self._values.get("aws_account_id")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def code_vulnerability_detector_name(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-codevulnerabilitydetectorname
            '''
            result = self._values.get("code_vulnerability_detector_name")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def code_vulnerability_detector_tags(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-codevulnerabilitydetectortags
            '''
            result = self._values.get("code_vulnerability_detector_tags")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def code_vulnerability_file_path(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-codevulnerabilityfilepath
            '''
            result = self._values.get("code_vulnerability_file_path")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def component_id(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the component IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-componentid
            '''
            result = self._values.get("component_id")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def component_type(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the component types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-componenttype
            '''
            result = self._values.get("component_type")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ec2_instance_image_id(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon EC2 instance image IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ec2instanceimageid
            '''
            result = self._values.get("ec2_instance_image_id")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ec2_instance_subnet_id(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon EC2 instance subnet IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ec2instancesubnetid
            '''
            result = self._values.get("ec2_instance_subnet_id")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ec2_instance_vpc_id(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon EC2 instance VPC IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ec2instancevpcid
            '''
            result = self._values.get("ec2_instance_vpc_id")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_architecture(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon ECR image architecture types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagearchitecture
            '''
            result = self._values.get("ecr_image_architecture")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_hash(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon ECR image hashes used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagehash
            '''
            result = self._values.get("ecr_image_hash")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_pushed_at(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]]:
            '''Details on the Amazon ECR image push date and time used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagepushedat
            '''
            result = self._values.get("ecr_image_pushed_at")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_registry(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the Amazon ECR registry used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimageregistry
            '''
            result = self._values.get("ecr_image_registry")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_repository_name(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the name of the Amazon ECR repository used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagerepositoryname
            '''
            result = self._values.get("ecr_image_repository_name")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_tags(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''The tags attached to the Amazon ECR container image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagetags
            '''
            result = self._values.get("ecr_image_tags")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def epss_score(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.NumberFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-epssscore
            '''
            result = self._values.get("epss_score")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.NumberFilterProperty"]]]], result)

        @builtins.property
        def exploit_available(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-exploitavailable
            '''
            result = self._values.get("exploit_available")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_arn(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the finding ARNs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-findingarn
            '''
            result = self._values.get("finding_arn")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_status(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the finding status types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-findingstatus
            '''
            result = self._values.get("finding_status")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_type(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the finding types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-findingtype
            '''
            result = self._values.get("finding_type")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def first_observed_at(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]]:
            '''Details on the date and time a finding was first seen used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-firstobservedat
            '''
            result = self._values.get("first_observed_at")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]], result)

        @builtins.property
        def fix_available(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-fixavailable
            '''
            result = self._values.get("fix_available")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def inspector_score(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.NumberFilterProperty"]]]]:
            '''The Amazon Inspector score to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-inspectorscore
            '''
            result = self._values.get("inspector_score")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.NumberFilterProperty"]]]], result)

        @builtins.property
        def lambda_function_execution_role_arn(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-lambdafunctionexecutionrolearn
            '''
            result = self._values.get("lambda_function_execution_role_arn")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def lambda_function_last_modified_at(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-lambdafunctionlastmodifiedat
            '''
            result = self._values.get("lambda_function_last_modified_at")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]], result)

        @builtins.property
        def lambda_function_layers(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-lambdafunctionlayers
            '''
            result = self._values.get("lambda_function_layers")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def lambda_function_name(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-lambdafunctionname
            '''
            result = self._values.get("lambda_function_name")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def lambda_function_runtime(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-lambdafunctionruntime
            '''
            result = self._values.get("lambda_function_runtime")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def last_observed_at(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]]:
            '''Details on the date and time a finding was last seen used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-lastobservedat
            '''
            result = self._values.get("last_observed_at")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]], result)

        @builtins.property
        def network_protocol(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on network protocol used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-networkprotocol
            '''
            result = self._values.get("network_protocol")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def port_range(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.PortRangeFilterProperty"]]]]:
            '''Details on the port ranges used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-portrange
            '''
            result = self._values.get("port_range")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.PortRangeFilterProperty"]]]], result)

        @builtins.property
        def related_vulnerabilities(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the related vulnerabilities used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-relatedvulnerabilities
            '''
            result = self._values.get("related_vulnerabilities")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_id(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the resource IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_tags(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.MapFilterProperty"]]]]:
            '''Details on the resource tags used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-resourcetags
            '''
            result = self._values.get("resource_tags")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.MapFilterProperty"]]]], result)

        @builtins.property
        def resource_type(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the resource types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-resourcetype
            '''
            result = self._values.get("resource_type")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def severity(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the severity used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-severity
            '''
            result = self._values.get("severity")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def title(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the finding title used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def updated_at(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]]:
            '''Details on the date and time a finding was last updated at used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.DateFilterProperty"]]]], result)

        @builtins.property
        def vendor_severity(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the vendor severity used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vendorseverity
            '''
            result = self._values.get("vendor_severity")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def vulnerability_id(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the vulnerability ID used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vulnerabilityid
            '''
            result = self._values.get("vulnerability_id")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def vulnerability_source(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the vulnerability score to filter findings by.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vulnerabilitysource
            '''
            result = self._values.get("vulnerability_source")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def vulnerable_packages(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.PackageFilterProperty"]]]]:
            '''Details on the vulnerable packages used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vulnerablepackages
            '''
            result = self._values.get("vulnerable_packages")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFilter.PackageFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.MapFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "key": "key", "value": "value"},
    )
    class MapFilterProperty:
        def __init__(
            self,
            *,
            comparison: builtins.str,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that describes details of a map filter.

            :param comparison: The operator to use when comparing values in the filter.
            :param key: The tag key used in the filter.
            :param value: The tag value used in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                map_filter_property = inspectorv2.CfnFilter.MapFilterProperty(
                    comparison="comparison",
                
                    # the properties below are optional
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__009bff3f64987bf2b6fbf83e6b34fdd47b0110d9ba805cb04cf145bbb5b29475)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison": comparison,
            }
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def comparison(self) -> builtins.str:
            '''The operator to use when comparing values in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html#cfn-inspectorv2-filter-mapfilter-comparison
            '''
            result = self._values.get("comparison")
            assert result is not None, "Required property 'comparison' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The tag key used in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html#cfn-inspectorv2-filter-mapfilter-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag value used in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html#cfn-inspectorv2-filter-mapfilter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MapFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.NumberFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lower_inclusive": "lowerInclusive",
            "upper_inclusive": "upperInclusive",
        },
    )
    class NumberFilterProperty:
        def __init__(
            self,
            *,
            lower_inclusive: typing.Optional[jsii.Number] = None,
            upper_inclusive: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An object that describes the details of a number filter.

            :param lower_inclusive: The lowest number to be included in the filter.
            :param upper_inclusive: The highest number to be included in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                number_filter_property = inspectorv2.CfnFilter.NumberFilterProperty(
                    lower_inclusive=123,
                    upper_inclusive=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6efc9c4516b1a3e22589ec1e26597252a4352fc85020ac641e71757b7752878)
                check_type(argname="argument lower_inclusive", value=lower_inclusive, expected_type=type_hints["lower_inclusive"])
                check_type(argname="argument upper_inclusive", value=upper_inclusive, expected_type=type_hints["upper_inclusive"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lower_inclusive is not None:
                self._values["lower_inclusive"] = lower_inclusive
            if upper_inclusive is not None:
                self._values["upper_inclusive"] = upper_inclusive

        @builtins.property
        def lower_inclusive(self) -> typing.Optional[jsii.Number]:
            '''The lowest number to be included in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html#cfn-inspectorv2-filter-numberfilter-lowerinclusive
            '''
            result = self._values.get("lower_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def upper_inclusive(self) -> typing.Optional[jsii.Number]:
            '''The highest number to be included in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html#cfn-inspectorv2-filter-numberfilter-upperinclusive
            '''
            result = self._values.get("upper_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NumberFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.PackageFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "architecture": "architecture",
            "epoch": "epoch",
            "file_path": "filePath",
            "name": "name",
            "release": "release",
            "source_lambda_layer_arn": "sourceLambdaLayerArn",
            "source_layer_hash": "sourceLayerHash",
            "version": "version",
        },
    )
    class PackageFilterProperty:
        def __init__(
            self,
            *,
            architecture: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            epoch: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            file_path: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            release: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            source_lambda_layer_arn: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            source_layer_hash: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            version: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information on the details of a package filter.

            :param architecture: An object that contains details on the package architecture type to filter on.
            :param epoch: An object that contains details on the package epoch to filter on.
            :param file_path: 
            :param name: An object that contains details on the name of the package to filter on.
            :param release: An object that contains details on the package release to filter on.
            :param source_lambda_layer_arn: 
            :param source_layer_hash: An object that contains details on the source layer hash to filter on.
            :param version: The package version to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                package_filter_property = inspectorv2.CfnFilter.PackageFilterProperty(
                    architecture=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    epoch=inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    ),
                    file_path=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    name=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    release=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    source_lambda_layer_arn=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    source_layer_hash=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    version=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1bffc1f427079a7381e5366b9fd38ff4f23a9a2d0463f6c7f0250a60e1c3aa65)
                check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
                check_type(argname="argument epoch", value=epoch, expected_type=type_hints["epoch"])
                check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument release", value=release, expected_type=type_hints["release"])
                check_type(argname="argument source_lambda_layer_arn", value=source_lambda_layer_arn, expected_type=type_hints["source_lambda_layer_arn"])
                check_type(argname="argument source_layer_hash", value=source_layer_hash, expected_type=type_hints["source_layer_hash"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if architecture is not None:
                self._values["architecture"] = architecture
            if epoch is not None:
                self._values["epoch"] = epoch
            if file_path is not None:
                self._values["file_path"] = file_path
            if name is not None:
                self._values["name"] = name
            if release is not None:
                self._values["release"] = release
            if source_lambda_layer_arn is not None:
                self._values["source_lambda_layer_arn"] = source_lambda_layer_arn
            if source_layer_hash is not None:
                self._values["source_layer_hash"] = source_layer_hash
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def architecture(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]:
            '''An object that contains details on the package architecture type to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-architecture
            '''
            result = self._values.get("architecture")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def epoch(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.NumberFilterProperty"]]:
            '''An object that contains details on the package epoch to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-epoch
            '''
            result = self._values.get("epoch")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.NumberFilterProperty"]], result)

        @builtins.property
        def file_path(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-filepath
            '''
            result = self._values.get("file_path")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def name(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]:
            '''An object that contains details on the name of the package to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def release(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]:
            '''An object that contains details on the package release to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-release
            '''
            result = self._values.get("release")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def source_lambda_layer_arn(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-sourcelambdalayerarn
            '''
            result = self._values.get("source_lambda_layer_arn")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def source_layer_hash(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]:
            '''An object that contains details on the source layer hash to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-sourcelayerhash
            '''
            result = self._values.get("source_layer_hash")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def version(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]]:
            '''The package version to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFilter.StringFilterProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PackageFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.PortRangeFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "begin_inclusive": "beginInclusive",
            "end_inclusive": "endInclusive",
        },
    )
    class PortRangeFilterProperty:
        def __init__(
            self,
            *,
            begin_inclusive: typing.Optional[jsii.Number] = None,
            end_inclusive: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An object that describes the details of a port range filter.

            :param begin_inclusive: The port number the port range begins at.
            :param end_inclusive: The port number the port range ends at.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                port_range_filter_property = inspectorv2.CfnFilter.PortRangeFilterProperty(
                    begin_inclusive=123,
                    end_inclusive=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57f27af64057bdc90d805dc1f14192e3d6ecef8b43899ee7e276ad4a39443097)
                check_type(argname="argument begin_inclusive", value=begin_inclusive, expected_type=type_hints["begin_inclusive"])
                check_type(argname="argument end_inclusive", value=end_inclusive, expected_type=type_hints["end_inclusive"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if begin_inclusive is not None:
                self._values["begin_inclusive"] = begin_inclusive
            if end_inclusive is not None:
                self._values["end_inclusive"] = end_inclusive

        @builtins.property
        def begin_inclusive(self) -> typing.Optional[jsii.Number]:
            '''The port number the port range begins at.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html#cfn-inspectorv2-filter-portrangefilter-begininclusive
            '''
            result = self._values.get("begin_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def end_inclusive(self) -> typing.Optional[jsii.Number]:
            '''The port number the port range ends at.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html#cfn-inspectorv2-filter-portrangefilter-endinclusive
            '''
            result = self._values.get("end_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortRangeFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.StringFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "value": "value"},
    )
    class StringFilterProperty:
        def __init__(self, *, comparison: builtins.str, value: builtins.str) -> None:
            '''An object that describes the details of a string filter.

            :param comparison: The operator to use when comparing values in the filter.
            :param value: The value to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                string_filter_property = inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d081b1255c15164560e59790e612b8f1e2382868fcbfff794be0ca61435dbce0)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison": comparison,
                "value": value,
            }

        @builtins.property
        def comparison(self) -> builtins.str:
            '''The operator to use when comparing values in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html#cfn-inspectorv2-filter-stringfilter-comparison
            '''
            result = self._values.get("comparison")
            assert result is not None, "Required property 'comparison' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html#cfn-inspectorv2-filter-stringfilter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StringFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "filter_action": "filterAction",
        "filter_criteria": "filterCriteria",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnFilterProps:
    def __init__(
        self,
        *,
        filter_action: builtins.str,
        filter_criteria: typing.Union["_IResolvable_da3f097b", typing.Union["CfnFilter.FilterCriteriaProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFilter``.

        :param filter_action: The action that is to be applied to the findings that match the filter.
        :param filter_criteria: Details on the filter criteria associated with this filter.
        :param name: The name of the filter.
        :param description: A description of the filter.
        :param tags: The tags attached to the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_inspectorv2 as inspectorv2
            
            cfn_filter_props = inspectorv2.CfnFilterProps(
                filter_action="filterAction",
                filter_criteria=inspectorv2.CfnFilter.FilterCriteriaProperty(
                    aws_account_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    code_vulnerability_detector_name=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    code_vulnerability_detector_tags=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    code_vulnerability_file_path=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    component_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    component_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_image_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_subnet_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_vpc_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_architecture=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_hash=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_pushed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    ecr_image_registry=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_repository_name=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_tags=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    epss_score=[inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    )],
                    exploit_available=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_arn=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_status=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    first_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    fix_available=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    inspector_score=[inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    )],
                    lambda_function_execution_role_arn=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    lambda_function_last_modified_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    lambda_function_layers=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    lambda_function_name=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    lambda_function_runtime=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    last_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    network_protocol=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    port_range=[inspectorv2.CfnFilter.PortRangeFilterProperty(
                        begin_inclusive=123,
                        end_inclusive=123
                    )],
                    related_vulnerabilities=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_tags=[inspectorv2.CfnFilter.MapFilterProperty(
                        comparison="comparison",
            
                        # the properties below are optional
                        key="key",
                        value="value"
                    )],
                    resource_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    severity=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    title=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    updated_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    vendor_severity=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerability_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerability_source=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerable_packages=[inspectorv2.CfnFilter.PackageFilterProperty(
                        architecture=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        epoch=inspectorv2.CfnFilter.NumberFilterProperty(
                            lower_inclusive=123,
                            upper_inclusive=123
                        ),
                        file_path=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        name=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        release=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        source_lambda_layer_arn=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        source_layer_hash=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        version=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        )
                    )]
                ),
                name="name",
            
                # the properties below are optional
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__701269c3a3c8675419393e41eacb02f94675d9b8c43500c7ae0bd7ea72e3129f)
            check_type(argname="argument filter_action", value=filter_action, expected_type=type_hints["filter_action"])
            check_type(argname="argument filter_criteria", value=filter_criteria, expected_type=type_hints["filter_criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_action": filter_action,
            "filter_criteria": filter_criteria,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def filter_action(self) -> builtins.str:
        '''The action that is to be applied to the findings that match the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-filteraction
        '''
        result = self._values.get("filter_action")
        assert result is not None, "Required property 'filter_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_criteria(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnFilter.FilterCriteriaProperty"]:
        '''Details on the filter criteria associated with this filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-filtercriteria
        '''
        result = self._values.get("filter_criteria")
        assert result is not None, "Required property 'filter_criteria' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnFilter.FilterCriteriaProperty"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags attached to the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCisScanConfiguration",
    "CfnCisScanConfigurationProps",
    "CfnCodeSecurityIntegration",
    "CfnCodeSecurityIntegrationProps",
    "CfnCodeSecurityScanConfiguration",
    "CfnCodeSecurityScanConfigurationProps",
    "CfnFilter",
    "CfnFilterProps",
]

publication.publish()

def _typecheckingstub__ee74cd979e0690afc5238694387a2bb443783c172f8af7544b4b5c468df80b9c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    scan_name: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    security_level: builtins.str,
    targets: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.CisTargetsProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17bb5d9e0d4a2d165ecc0f9d6c045ff79fb5bd35d06a65c705104aaf297f5690(
    resource: _ICisScanConfigurationRef_8f6555b3,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0157dbe9d0e6a256bfb1f48831eecbee74bad3bf884fbf7b8719bed932bc494b(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c340cf5a8052b5b5d1021305af92e23dcb4f62645a1014b0a49bb031d376ee8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf01f89651352328420f5a52535d8376706a979b3cb022464732eddc33e94c8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f6f074ec34751eb6d66964ee6738d096c1429db3564cba2005e530e659871bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17c38c82086f8ffe9712e88585d2f980663e72bbb5b6ac70574594200cb759c2(
    value: typing.Union[_IResolvable_da3f097b, CfnCisScanConfiguration.ScheduleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53a976b81d95f07052322a80e8b1ff546ae083bdb3cb3d358b91e5b7e50b0909(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8afffccf2a9a470f423d247abd4a6dfe735dc39c53a2abe26c8cdb1844ec12a2(
    value: typing.Union[_IResolvable_da3f097b, CfnCisScanConfiguration.CisTargetsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b4e1fac23c27cbc692267473e4cf9258b43062b9aea2a43b116dcfb105adb0d(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b07d123221faefb49073a28736f1aec9dc2a488247f39ec213274809cd3b6a(
    *,
    account_ids: typing.Sequence[builtins.str],
    target_resource_tags: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Sequence[builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3a6a48de82a0a7da55bb17cc5099cc069382b4a48c7b97e3ef62fa2f60aa59(
    *,
    start_time: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.TimeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__100314319c9ea946d9251b6fcc3341b05bf63331e32e3a7f7aa894b6b8421861(
    *,
    day: builtins.str,
    start_time: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.TimeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db99f3a188203b64b30f42f8814cca36f1b859733833ecc2b25042b4eb91d395(
    *,
    daily: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.DailyScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    monthly: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.MonthlyScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    one_time: typing.Any = None,
    weekly: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.WeeklyScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2452dd795ce037d8e45e12f3b1e33517e2f22095c208d70f01cce9d97cc7f45(
    *,
    time_of_day: builtins.str,
    time_zone: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30b6b9756e498926a5cf63c7bbf5e7f937d68b176005d1670779697c6b3abb4(
    *,
    days: typing.Sequence[builtins.str],
    start_time: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.TimeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f0430cb9cf97c73c0c85526ac298bc695a6c9d3bf5e578a6d9b5c85d5623dc(
    *,
    scan_name: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    security_level: builtins.str,
    targets: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.CisTargetsProperty, typing.Dict[builtins.str, typing.Any]]],
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80799b4356912cf375014b9f868e52ed37e885f4e1f3c1ddd85598a234badc5f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    create_integration_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityIntegration.CreateDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
    update_integration_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityIntegration.UpdateDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ca7e2752a7e90b087558c274f5098a9e8bc7c5d74e989dc2358c5a144c1d57e(
    resource: _ICodeSecurityIntegrationRef_b418c2a5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b98f80c5b07b3b4699f81f95546fed657ea28fce1615629bee70f86785ce350f(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2b41111bd2e5e5f072f8545fffa3c791a4d0e501f547576454bf1a1f74205d6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a995b0a871c5ed338d9451bbbe7895dc95cb1d56fb43ef4d2d9d854ffdeb8a66(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95bada6a0a63eed0487660762db52cf7634424d68b180f5bdde1aa127cbc6ca1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCodeSecurityIntegration.CreateDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62c672b1420b745cd7e45b7351f3382ced028744668c9771a1148fe207c23267(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56217870c5b8873ef3b3750235b4baa957fcd999c408c688e231f957b297af0b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81de92c5a50f951f013bc7d558d9d09c3c119459f7f1a04ca44ba5291a994ee(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c450107a89d380f98e1bb112fb4f8df187acd5d7b74c42bca8a125923588adc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCodeSecurityIntegration.UpdateDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2262215d3482ab65dacec2a9b346848e87bce266386fcf679cd7607f925a41a9(
    *,
    gitlab_self_managed: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityIntegration.CreateGitLabSelfManagedIntegrationDetailProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bbc1b28a8c4770b506b8b2fbbfde8238181c9ccb84cf76f6b88eefb2a36575c(
    *,
    access_token: builtins.str,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49eb1e2e3f4009317c4c9d3bde00d5f76e2edded22c78e79a48f4596be9ae8b8(
    *,
    github: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityIntegration.UpdateGitHubIntegrationDetailProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    gitlab_self_managed: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityIntegration.UpdateGitLabSelfManagedIntegrationDetailProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3487b0f19d852a82df38914d0b6e860cbf9001a42d8401b18e0a1768ad4cb7(
    *,
    code: builtins.str,
    installation_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e29538aad68be3e1d38e6aa515bc380b1c5dbb5fcc5c4ed65df930696a81461(
    *,
    auth_code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71aafe099f5a07cc45a5a16ed7c8165fc3beaaf581b2a7075ad79583b48897ae(
    *,
    create_integration_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityIntegration.CreateDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    type: typing.Optional[builtins.str] = None,
    update_integration_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityIntegration.UpdateDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8087fd99eb325ae09773df4a6c219dda10efe85e43341cb1f5b576a1e88cef(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    level: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    scope_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityScanConfiguration.ScopeSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e2ba232f61f3996b58dc5cfd25237fcbd03e5685907e35ac8cd5f40d55260b(
    resource: _ICodeSecurityScanConfigurationRef_4a00a90e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1f6d967d4a3eb9c698e7e4d9da2813e02cf4fa4c7e56bc813ceb4ed4d3d1817(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb6f2f1a541e759bd4ebb9f175ef2898e08b44a5a2f74698a104ebf563f6050(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ba67d1221ac83994db1e0ae5a5f4d8d289116bd2bbba3ba9086ac33ff847516(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b63b68b5efac81af01f69f6fc536a7e0c56ab5d78f7c4d82199c868ce47b16(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80291f0cd7a0cb5b5f295442d46a5d028aa373ed833a3fb0e3b6091879e1a69b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ce312b3f34f6350a3d1ee625199c03f68c9cb605f5e399d8d24b0f3374d219(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2418e2e1becb18ab1d3613df2cc71f18c45d161aa5b3aa4b796643c5c109a1b8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCodeSecurityScanConfiguration.ScopeSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9428e2a90cc0578e6f07997b18e25682dcdf69843515552c29dd20aa94e714a3(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e69a31a73796f4b8caaf249f9369b948bbd3cba1089b94bed6018c89696c89cc(
    *,
    rule_set_categories: typing.Sequence[builtins.str],
    continuous_integration_scan_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityScanConfiguration.ContinuousIntegrationScanConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    periodic_scan_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityScanConfiguration.PeriodicScanConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04bdb61b43cbfbc6d92a4c02a47e71f63015162a7acf1e60ef409eebcd21a9f2(
    *,
    supported_events: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901beb5d14c9e234fd835b4523197f824e50f091ed2dcfbca59aef2f1f023dde(
    *,
    frequency: typing.Optional[builtins.str] = None,
    frequency_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911607f762372da4ac39dfe813875203be92e9a87447c67741aae32d569743dc(
    *,
    project_selection_scope: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ea2faaa39ad7a4370f1a43aa967ae3ded5ad2ac9c212905e92dd56f603ec204(
    *,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityScanConfiguration.CodeSecurityScanConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    level: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    scope_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeSecurityScanConfiguration.ScopeSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76aaac8f8d755716225a5dd2d4902f3e7ec007381fa82a2d163553362c975c9d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    filter_action: builtins.str,
    filter_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.FilterCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__704d307380b328e752813838e45cc7632f81ee6e606de43e80cdab6fbc9f46bb(
    resource: _IFilterRef_37875571,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e088efafc9f496c3c6fa7871d5344534a4487772b0dada5b37c9bf1911c2234(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daeca541bed43f62727b37c4048db034533d9b1614725f3cf4c361b77df5323e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02055b54b230012a61c4a22e04d2fc0ffa08a47a06385a880a1db32a3f55f237(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72dbbaedc7eb8a3b6da0867d3f429993d1cdfe3b095a514d2cb82730c01b31d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b566081cfe458076187f61e1afab9cbbb5fb2cdd114aad2fa6e38280867325e5(
    value: typing.Union[_IResolvable_da3f097b, CfnFilter.FilterCriteriaProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b0548c4926be9ebf2a0675883b51af78c4f6a9c034f4d0fb7a9ebfd7ad038ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29a0d69128962a2d8d478ff9197ec92d930e2284a9cbff6337d95fb1932925d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d85ec3c1992f35abc960573e86c94eb9d5f4d6c6fd9f47728ef03d5078212f1(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__412cca739fbade26efa876445772a168ea693eb111b9385ae83d92127bd547b5(
    *,
    end_inclusive: typing.Optional[jsii.Number] = None,
    start_inclusive: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bf898b4c669bfc838bf91c83d3735a9d69065b37baef35430be61dc52e3c81a(
    *,
    aws_account_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    code_vulnerability_detector_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    code_vulnerability_detector_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    code_vulnerability_file_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    component_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    component_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_image_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_subnet_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_vpc_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_architecture: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_hash: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_pushed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_registry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_repository_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    epss_score: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    exploit_available: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    first_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    fix_available: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    inspector_score: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    lambda_function_execution_role_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    lambda_function_last_modified_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    lambda_function_layers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    lambda_function_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    lambda_function_runtime: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    last_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_protocol: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.PortRangeFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    related_vulnerabilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.MapFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    severity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    title: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vendor_severity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vulnerability_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vulnerability_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vulnerable_packages: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.PackageFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009bff3f64987bf2b6fbf83e6b34fdd47b0110d9ba805cb04cf145bbb5b29475(
    *,
    comparison: builtins.str,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6efc9c4516b1a3e22589ec1e26597252a4352fc85020ac641e71757b7752878(
    *,
    lower_inclusive: typing.Optional[jsii.Number] = None,
    upper_inclusive: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bffc1f427079a7381e5366b9fd38ff4f23a9a2d0463f6c7f0250a60e1c3aa65(
    *,
    architecture: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    epoch: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    file_path: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    release: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_lambda_layer_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_layer_hash: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f27af64057bdc90d805dc1f14192e3d6ecef8b43899ee7e276ad4a39443097(
    *,
    begin_inclusive: typing.Optional[jsii.Number] = None,
    end_inclusive: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d081b1255c15164560e59790e612b8f1e2382868fcbfff794be0ca61435dbce0(
    *,
    comparison: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__701269c3a3c8675419393e41eacb02f94675d9b8c43500c7ae0bd7ea72e3129f(
    *,
    filter_action: builtins.str,
    filter_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.FilterCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
