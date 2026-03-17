r'''
# AWS::APS Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_aps as aps
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for APS construct libraries](https://constructs.dev/search?q=aps)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::APS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_APS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::APS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_APS.html).

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
from ..interfaces.aws_aps import (
    AnomalyDetectorReference as _AnomalyDetectorReference_1ffc0c63,
    IAnomalyDetectorRef as _IAnomalyDetectorRef_fef2b996,
    IResourcePolicyRef as _IResourcePolicyRef_1aa7c1a2,
    IRuleGroupsNamespaceRef as _IRuleGroupsNamespaceRef_7b589be9,
    IScraperRef as _IScraperRef_2b17ef67,
    IWorkspaceRef as _IWorkspaceRef_d8b2b588,
    ResourcePolicyReference as _ResourcePolicyReference_162e786c,
    RuleGroupsNamespaceReference as _RuleGroupsNamespaceReference_9d4673a3,
    ScraperReference as _ScraperReference_c6b43df1,
    WorkspaceReference as _WorkspaceReference_4f6a6126,
)


@jsii.implements(_IInspectable_c2943556, _IAnomalyDetectorRef_fef2b996, _ITaggableV2_4e6798f8)
class CfnAnomalyDetector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnAnomalyDetector",
):
    '''Anomaly detection uses the Random Cut Forest algorithm for time-series analysis.

    The anomaly detector analyzes Amazon Managed Service for Prometheus metrics to identify unusual patterns and behaviors.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-anomalydetector.html
    :cloudformationResource: AWS::APS::AnomalyDetector
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_anomaly_detector = aps.CfnAnomalyDetector(self, "MyCfnAnomalyDetector",
            alias="alias",
            configuration=aps.CfnAnomalyDetector.AnomalyDetectorConfigurationProperty(
                random_cut_forest=aps.CfnAnomalyDetector.RandomCutForestConfigurationProperty(
                    query="query",
        
                    # the properties below are optional
                    ignore_near_expected_from_above=aps.CfnAnomalyDetector.IgnoreNearExpectedProperty(
                        amount=123,
                        ratio=123
                    ),
                    ignore_near_expected_from_below=aps.CfnAnomalyDetector.IgnoreNearExpectedProperty(
                        amount=123,
                        ratio=123
                    ),
                    sample_size=123,
                    shingle_size=123
                )
            ),
            workspace="workspace",
        
            # the properties below are optional
            evaluation_interval_in_seconds=123,
            labels=[aps.CfnAnomalyDetector.LabelProperty(
                key="key",
                value="value"
            )],
            missing_data_action=aps.CfnAnomalyDetector.MissingDataActionProperty(
                mark_as_anomaly=False,
                skip=False
            ),
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
        alias: builtins.str,
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnomalyDetector.AnomalyDetectorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        workspace: builtins.str,
        evaluation_interval_in_seconds: typing.Optional[jsii.Number] = None,
        labels: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnomalyDetector.LabelProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        missing_data_action: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnomalyDetector.MissingDataActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::APS::AnomalyDetector``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alias: The user-friendly name of the anomaly detector.
        :param configuration: The algorithm configuration of the anomaly detector.
        :param workspace: An Amazon Managed Service for Prometheus workspace is a logical and isolated Prometheus server dedicated to ingesting, storing, and querying your Prometheus-compatible metrics.
        :param evaluation_interval_in_seconds: The frequency, in seconds, at which the anomaly detector evaluates metrics. Default: - 60
        :param labels: The Amazon Managed Service for Prometheus metric labels associated with the anomaly detector.
        :param missing_data_action: The action taken when data is missing during evaluation.
        :param tags: The tags applied to the anomaly detector.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58b3184629f18780da9f7c9eb2f8acdbdbb5190c9fc3ae41fdbbe34341ba0f26)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAnomalyDetectorProps(
            alias=alias,
            configuration=configuration,
            workspace=workspace,
            evaluation_interval_in_seconds=evaluation_interval_in_seconds,
            labels=labels,
            missing_data_action=missing_data_action,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAnomalyDetector")
    @builtins.classmethod
    def arn_for_anomaly_detector(
        cls,
        resource: "_IAnomalyDetectorRef_fef2b996",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__114e115249b8e928b79f5b7cb5e3fed1d136c04a5ab6a491f1bfee0b570b9121)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAnomalyDetector", [resource]))

    @jsii.member(jsii_name="isCfnAnomalyDetector")
    @builtins.classmethod
    def is_cfn_anomaly_detector(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAnomalyDetector.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3babfb32b6d802220d9f08593ab6b583376e7a9fb6a2c4f8866b55e479ece522)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAnomalyDetector", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36a9fa3c67c466703717001e2774dacca3fa612b6ec02f8b6361ad6736da0ec7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1edc3473fdf33536207faf87047c2bef23ac4e4aecad53d1e0338308f0e5ab91)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorRef")
    def anomaly_detector_ref(self) -> "_AnomalyDetectorReference_1ffc0c63":
        '''A reference to a AnomalyDetector resource.'''
        return typing.cast("_AnomalyDetectorReference_1ffc0c63", jsii.get(self, "anomalyDetectorRef"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the anomaly detector.

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
    @jsii.member(jsii_name="alias")
    def alias(self) -> builtins.str:
        '''The user-friendly name of the anomaly detector.'''
        return typing.cast(builtins.str, jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe3aa1b72ccc7677675b2ae76ae8e5e1dfd2146dae8eba7520a981184cdf780d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.AnomalyDetectorConfigurationProperty"]:
        '''The algorithm configuration of the anomaly detector.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.AnomalyDetectorConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.AnomalyDetectorConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1394fe6b497d7add7f3c437f746b83234bfd1714418b007d2ca77fcaf2e486fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workspace")
    def workspace(self) -> builtins.str:
        '''An Amazon Managed Service for Prometheus workspace is a logical and isolated Prometheus server dedicated to ingesting, storing, and querying your Prometheus-compatible metrics.'''
        return typing.cast(builtins.str, jsii.get(self, "workspace"))

    @workspace.setter
    def workspace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51d01d3c64410491a2005087b379e01fe1749ffd4be8e8dae194b7cc8e5e19b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspace", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="evaluationIntervalInSeconds")
    def evaluation_interval_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The frequency, in seconds, at which the anomaly detector evaluates metrics.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "evaluationIntervalInSeconds"))

    @evaluation_interval_in_seconds.setter
    def evaluation_interval_in_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce3cb5189478c72429dee4d6fa1ed9635e537559491f15b775c279a89020cb75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationIntervalInSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.LabelProperty"]]]]:
        '''The Amazon Managed Service for Prometheus metric labels associated with the anomaly detector.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.LabelProperty"]]]], jsii.get(self, "labels"))

    @labels.setter
    def labels(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.LabelProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d15555eb30ee6b4decc1dba71c708714ce1a7f00e658c2ce9c617f35dbea119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="missingDataAction")
    def missing_data_action(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.MissingDataActionProperty"]]:
        '''The action taken when data is missing during evaluation.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.MissingDataActionProperty"]], jsii.get(self, "missingDataAction"))

    @missing_data_action.setter
    def missing_data_action(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.MissingDataActionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e639ced06e0101ba2e1108f2a5748e988f60e8c6ecadbb32ca0f2dc6162a53e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "missingDataAction", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags applied to the anomaly detector.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8b42c0f027d8c1c104a6037d9c3752efbfb2ae169c30d63f35dee5bad63b3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnAnomalyDetector.AnomalyDetectorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"random_cut_forest": "randomCutForest"},
    )
    class AnomalyDetectorConfigurationProperty:
        def __init__(
            self,
            *,
            random_cut_forest: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnomalyDetector.RandomCutForestConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The configuration for the anomaly detection algorithm.

            :param random_cut_forest: The Random Cut Forest algorithm configuration for anomaly detection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-anomalydetectorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                anomaly_detector_configuration_property = aps.CfnAnomalyDetector.AnomalyDetectorConfigurationProperty(
                    random_cut_forest=aps.CfnAnomalyDetector.RandomCutForestConfigurationProperty(
                        query="query",
                
                        # the properties below are optional
                        ignore_near_expected_from_above=aps.CfnAnomalyDetector.IgnoreNearExpectedProperty(
                            amount=123,
                            ratio=123
                        ),
                        ignore_near_expected_from_below=aps.CfnAnomalyDetector.IgnoreNearExpectedProperty(
                            amount=123,
                            ratio=123
                        ),
                        sample_size=123,
                        shingle_size=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aca672630a5e19c23bb68b82c63c873a7687610464d166cef0da5d6cde142082)
                check_type(argname="argument random_cut_forest", value=random_cut_forest, expected_type=type_hints["random_cut_forest"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "random_cut_forest": random_cut_forest,
            }

        @builtins.property
        def random_cut_forest(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.RandomCutForestConfigurationProperty"]:
            '''The Random Cut Forest algorithm configuration for anomaly detection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-anomalydetectorconfiguration.html#cfn-aps-anomalydetector-anomalydetectorconfiguration-randomcutforest
            '''
            result = self._values.get("random_cut_forest")
            assert result is not None, "Required property 'random_cut_forest' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.RandomCutForestConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnomalyDetectorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnAnomalyDetector.IgnoreNearExpectedProperty",
        jsii_struct_bases=[],
        name_mapping={"amount": "amount", "ratio": "ratio"},
    )
    class IgnoreNearExpectedProperty:
        def __init__(
            self,
            *,
            amount: typing.Optional[jsii.Number] = None,
            ratio: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration for threshold settings that determine when values near expected values should be ignored during anomaly detection.

            :param amount: The absolute amount by which values can differ from expected values before being considered anomalous.
            :param ratio: The ratio by which values can differ from expected values before being considered anomalous.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-ignorenearexpected.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                ignore_near_expected_property = aps.CfnAnomalyDetector.IgnoreNearExpectedProperty(
                    amount=123,
                    ratio=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3e1cf276ea5a24efc7ebe9d526fad4e86dd66a3f55ea5a0dcb3a617b8d62dff)
                check_type(argname="argument amount", value=amount, expected_type=type_hints["amount"])
                check_type(argname="argument ratio", value=ratio, expected_type=type_hints["ratio"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if amount is not None:
                self._values["amount"] = amount
            if ratio is not None:
                self._values["ratio"] = ratio

        @builtins.property
        def amount(self) -> typing.Optional[jsii.Number]:
            '''The absolute amount by which values can differ from expected values before being considered anomalous.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-ignorenearexpected.html#cfn-aps-anomalydetector-ignorenearexpected-amount
            '''
            result = self._values.get("amount")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def ratio(self) -> typing.Optional[jsii.Number]:
            '''The ratio by which values can differ from expected values before being considered anomalous.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-ignorenearexpected.html#cfn-aps-anomalydetector-ignorenearexpected-ratio
            '''
            result = self._values.get("ratio")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IgnoreNearExpectedProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnAnomalyDetector.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class LabelProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The Amazon Managed Service for Prometheus metric labels associated with the anomaly detector.

            :param key: The key of the label.
            :param value: The value for this label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-label.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                label_property = aps.CfnAnomalyDetector.LabelProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3f784d604d60c49dd5fb567dcfedcd9d16e2ce47ba899589a373c9322818035a)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key of the label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-label.html#cfn-aps-anomalydetector-label-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value for this label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-label.html#cfn-aps-anomalydetector-label-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnAnomalyDetector.MissingDataActionProperty",
        jsii_struct_bases=[],
        name_mapping={"mark_as_anomaly": "markAsAnomaly", "skip": "skip"},
    )
    class MissingDataActionProperty:
        def __init__(
            self,
            *,
            mark_as_anomaly: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            skip: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''Specifies the action to take when data is missing during anomaly detection evaluation.

            :param mark_as_anomaly: Marks missing data points as anomalies.
            :param skip: Skips evaluation when data is missing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-missingdataaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                missing_data_action_property = aps.CfnAnomalyDetector.MissingDataActionProperty(
                    mark_as_anomaly=False,
                    skip=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e5b8457b72ba87aa14000e26b68e021fa4b19e4e88f3a022910dcd18542039d0)
                check_type(argname="argument mark_as_anomaly", value=mark_as_anomaly, expected_type=type_hints["mark_as_anomaly"])
                check_type(argname="argument skip", value=skip, expected_type=type_hints["skip"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if mark_as_anomaly is not None:
                self._values["mark_as_anomaly"] = mark_as_anomaly
            if skip is not None:
                self._values["skip"] = skip

        @builtins.property
        def mark_as_anomaly(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''Marks missing data points as anomalies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-missingdataaction.html#cfn-aps-anomalydetector-missingdataaction-markasanomaly
            '''
            result = self._values.get("mark_as_anomaly")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def skip(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''Skips evaluation when data is missing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-missingdataaction.html#cfn-aps-anomalydetector-missingdataaction-skip
            '''
            result = self._values.get("skip")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MissingDataActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnAnomalyDetector.RandomCutForestConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "query": "query",
            "ignore_near_expected_from_above": "ignoreNearExpectedFromAbove",
            "ignore_near_expected_from_below": "ignoreNearExpectedFromBelow",
            "sample_size": "sampleSize",
            "shingle_size": "shingleSize",
        },
    )
    class RandomCutForestConfigurationProperty:
        def __init__(
            self,
            *,
            query: builtins.str,
            ignore_near_expected_from_above: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnomalyDetector.IgnoreNearExpectedProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ignore_near_expected_from_below: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnomalyDetector.IgnoreNearExpectedProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sample_size: typing.Optional[jsii.Number] = None,
            shingle_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration for the Random Cut Forest algorithm used for anomaly detection in time-series data.

            :param query: The Prometheus query used to retrieve the time-series data for anomaly detection. .. epigraph:: Random Cut Forest queries must be wrapped by a supported PromQL aggregation operator. For more information, see `Aggregation operators <https://docs.aws.amazon.com/https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators>`_ on the *Prometheus docs* website. *Supported PromQL aggregation operators* : ``avg`` , ``count`` , ``group`` , ``max`` , ``min`` , ``quantile`` , ``stddev`` , ``stdvar`` , and ``sum`` .
            :param ignore_near_expected_from_above: Configuration for ignoring values that are near expected values from above during anomaly detection.
            :param ignore_near_expected_from_below: Configuration for ignoring values that are near expected values from below during anomaly detection.
            :param sample_size: The number of data points sampled from the input stream for the Random Cut Forest algorithm. The default number is 256 consecutive data points. Default: - 256
            :param shingle_size: The number of consecutive data points used to create a shingle for the Random Cut Forest algorithm. The default number is 8 consecutive data points. Default: - 8

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-randomcutforestconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                random_cut_forest_configuration_property = aps.CfnAnomalyDetector.RandomCutForestConfigurationProperty(
                    query="query",
                
                    # the properties below are optional
                    ignore_near_expected_from_above=aps.CfnAnomalyDetector.IgnoreNearExpectedProperty(
                        amount=123,
                        ratio=123
                    ),
                    ignore_near_expected_from_below=aps.CfnAnomalyDetector.IgnoreNearExpectedProperty(
                        amount=123,
                        ratio=123
                    ),
                    sample_size=123,
                    shingle_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__83993f42a131a948093792cb8cd7b4f710c6b4dffce6b17f386497f1cbe514ea)
                check_type(argname="argument query", value=query, expected_type=type_hints["query"])
                check_type(argname="argument ignore_near_expected_from_above", value=ignore_near_expected_from_above, expected_type=type_hints["ignore_near_expected_from_above"])
                check_type(argname="argument ignore_near_expected_from_below", value=ignore_near_expected_from_below, expected_type=type_hints["ignore_near_expected_from_below"])
                check_type(argname="argument sample_size", value=sample_size, expected_type=type_hints["sample_size"])
                check_type(argname="argument shingle_size", value=shingle_size, expected_type=type_hints["shingle_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "query": query,
            }
            if ignore_near_expected_from_above is not None:
                self._values["ignore_near_expected_from_above"] = ignore_near_expected_from_above
            if ignore_near_expected_from_below is not None:
                self._values["ignore_near_expected_from_below"] = ignore_near_expected_from_below
            if sample_size is not None:
                self._values["sample_size"] = sample_size
            if shingle_size is not None:
                self._values["shingle_size"] = shingle_size

        @builtins.property
        def query(self) -> builtins.str:
            '''The Prometheus query used to retrieve the time-series data for anomaly detection.

            .. epigraph::

               Random Cut Forest queries must be wrapped by a supported PromQL aggregation operator. For more information, see `Aggregation operators <https://docs.aws.amazon.com/https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators>`_ on the *Prometheus docs* website.

               *Supported PromQL aggregation operators* : ``avg`` , ``count`` , ``group`` , ``max`` , ``min`` , ``quantile`` , ``stddev`` , ``stdvar`` , and ``sum`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-randomcutforestconfiguration.html#cfn-aps-anomalydetector-randomcutforestconfiguration-query
            '''
            result = self._values.get("query")
            assert result is not None, "Required property 'query' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ignore_near_expected_from_above(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.IgnoreNearExpectedProperty"]]:
            '''Configuration for ignoring values that are near expected values from above during anomaly detection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-randomcutforestconfiguration.html#cfn-aps-anomalydetector-randomcutforestconfiguration-ignorenearexpectedfromabove
            '''
            result = self._values.get("ignore_near_expected_from_above")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.IgnoreNearExpectedProperty"]], result)

        @builtins.property
        def ignore_near_expected_from_below(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.IgnoreNearExpectedProperty"]]:
            '''Configuration for ignoring values that are near expected values from below during anomaly detection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-randomcutforestconfiguration.html#cfn-aps-anomalydetector-randomcutforestconfiguration-ignorenearexpectedfrombelow
            '''
            result = self._values.get("ignore_near_expected_from_below")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.IgnoreNearExpectedProperty"]], result)

        @builtins.property
        def sample_size(self) -> typing.Optional[jsii.Number]:
            '''The number of data points sampled from the input stream for the Random Cut Forest algorithm.

            The default number is 256 consecutive data points.

            :default: - 256

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-randomcutforestconfiguration.html#cfn-aps-anomalydetector-randomcutforestconfiguration-samplesize
            '''
            result = self._values.get("sample_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def shingle_size(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive data points used to create a shingle for the Random Cut Forest algorithm.

            The default number is 8 consecutive data points.

            :default: - 8

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-anomalydetector-randomcutforestconfiguration.html#cfn-aps-anomalydetector-randomcutforestconfiguration-shinglesize
            '''
            result = self._values.get("shingle_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RandomCutForestConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnAnomalyDetectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "configuration": "configuration",
        "workspace": "workspace",
        "evaluation_interval_in_seconds": "evaluationIntervalInSeconds",
        "labels": "labels",
        "missing_data_action": "missingDataAction",
        "tags": "tags",
    },
)
class CfnAnomalyDetectorProps:
    def __init__(
        self,
        *,
        alias: builtins.str,
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnomalyDetector.AnomalyDetectorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        workspace: builtins.str,
        evaluation_interval_in_seconds: typing.Optional[jsii.Number] = None,
        labels: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnomalyDetector.LabelProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        missing_data_action: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnomalyDetector.MissingDataActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnomalyDetector``.

        :param alias: The user-friendly name of the anomaly detector.
        :param configuration: The algorithm configuration of the anomaly detector.
        :param workspace: An Amazon Managed Service for Prometheus workspace is a logical and isolated Prometheus server dedicated to ingesting, storing, and querying your Prometheus-compatible metrics.
        :param evaluation_interval_in_seconds: The frequency, in seconds, at which the anomaly detector evaluates metrics. Default: - 60
        :param labels: The Amazon Managed Service for Prometheus metric labels associated with the anomaly detector.
        :param missing_data_action: The action taken when data is missing during evaluation.
        :param tags: The tags applied to the anomaly detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-anomalydetector.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_anomaly_detector_props = aps.CfnAnomalyDetectorProps(
                alias="alias",
                configuration=aps.CfnAnomalyDetector.AnomalyDetectorConfigurationProperty(
                    random_cut_forest=aps.CfnAnomalyDetector.RandomCutForestConfigurationProperty(
                        query="query",
            
                        # the properties below are optional
                        ignore_near_expected_from_above=aps.CfnAnomalyDetector.IgnoreNearExpectedProperty(
                            amount=123,
                            ratio=123
                        ),
                        ignore_near_expected_from_below=aps.CfnAnomalyDetector.IgnoreNearExpectedProperty(
                            amount=123,
                            ratio=123
                        ),
                        sample_size=123,
                        shingle_size=123
                    )
                ),
                workspace="workspace",
            
                # the properties below are optional
                evaluation_interval_in_seconds=123,
                labels=[aps.CfnAnomalyDetector.LabelProperty(
                    key="key",
                    value="value"
                )],
                missing_data_action=aps.CfnAnomalyDetector.MissingDataActionProperty(
                    mark_as_anomaly=False,
                    skip=False
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be017a909bcb870b1880c9bb2c099abc51df504e0f9199ca315deb7fa50b9d6b)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument workspace", value=workspace, expected_type=type_hints["workspace"])
            check_type(argname="argument evaluation_interval_in_seconds", value=evaluation_interval_in_seconds, expected_type=type_hints["evaluation_interval_in_seconds"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument missing_data_action", value=missing_data_action, expected_type=type_hints["missing_data_action"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias": alias,
            "configuration": configuration,
            "workspace": workspace,
        }
        if evaluation_interval_in_seconds is not None:
            self._values["evaluation_interval_in_seconds"] = evaluation_interval_in_seconds
        if labels is not None:
            self._values["labels"] = labels
        if missing_data_action is not None:
            self._values["missing_data_action"] = missing_data_action
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def alias(self) -> builtins.str:
        '''The user-friendly name of the anomaly detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-anomalydetector.html#cfn-aps-anomalydetector-alias
        '''
        result = self._values.get("alias")
        assert result is not None, "Required property 'alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.AnomalyDetectorConfigurationProperty"]:
        '''The algorithm configuration of the anomaly detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-anomalydetector.html#cfn-aps-anomalydetector-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.AnomalyDetectorConfigurationProperty"], result)

    @builtins.property
    def workspace(self) -> builtins.str:
        '''An Amazon Managed Service for Prometheus workspace is a logical and isolated Prometheus server dedicated to ingesting, storing, and querying your Prometheus-compatible metrics.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-anomalydetector.html#cfn-aps-anomalydetector-workspace
        '''
        result = self._values.get("workspace")
        assert result is not None, "Required property 'workspace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def evaluation_interval_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The frequency, in seconds, at which the anomaly detector evaluates metrics.

        :default: - 60

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-anomalydetector.html#cfn-aps-anomalydetector-evaluationintervalinseconds
        '''
        result = self._values.get("evaluation_interval_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def labels(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.LabelProperty"]]]]:
        '''The Amazon Managed Service for Prometheus metric labels associated with the anomaly detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-anomalydetector.html#cfn-aps-anomalydetector-labels
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.LabelProperty"]]]], result)

    @builtins.property
    def missing_data_action(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.MissingDataActionProperty"]]:
        '''The action taken when data is missing during evaluation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-anomalydetector.html#cfn-aps-anomalydetector-missingdataaction
        '''
        result = self._values.get("missing_data_action")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnomalyDetector.MissingDataActionProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags applied to the anomaly detector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-anomalydetector.html#cfn-aps-anomalydetector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnomalyDetectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IResourcePolicyRef_1aa7c1a2)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnResourcePolicy",
):
    '''Use resource-based policies to grant permissions to other AWS accounts or services to access your workspace.

    Only Prometheus-compatible APIs can be used for workspace sharing. You can add non-Prometheus-compatible APIs to the policy, but they will be ignored. For more information, see `Prometheus-compatible APIs <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-APIReference-Prometheus-Compatible-Apis.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

    If your workspace uses customer-managed AWS  keys for encryption, you must grant the principals in your resource-based policy access to those AWS  keys. You can do this by creating AWS  grants. For more information, see `CreateGrant <https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html>`_ in the *AWS  API Reference* and `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

    For more information about working with IAM , see `Using Amazon Managed Service for Prometheus with IAM <https://docs.aws.amazon.com/prometheus/latest/userguide/security_iam_service-with-iam.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-resourcepolicy.html
    :cloudformationResource: AWS::APS::ResourcePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_resource_policy = aps.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            policy_document="policyDocument",
            workspace_arn="workspaceArn"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        policy_document: builtins.str,
        workspace_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::APS::ResourcePolicy``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: The JSON to use as the Resource-based Policy.
        :param workspace_arn: An ARN identifying a Workspace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54f89d9ee1d6d400f40f83801fe40dee056ce969e9e0501ca1390285aab7cb82)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(
            policy_document=policy_document, workspace_arn=workspace_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnResourcePolicy")
    @builtins.classmethod
    def is_cfn_resource_policy(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnResourcePolicy.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2353f37144a75d2ea8089f4e00cd676ce44deb9aaee1ea5d95d4d42ecf5445b)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnResourcePolicy", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fd684bb5425ae9b9586530c2118e55043226673b8740171d3f7c2b1fbd03b3d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__96c6a584b0420e6cc37e76ad4b000bc6d8f4137f577bf7075b4ec87bab8717d9)
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
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "_ResourcePolicyReference_162e786c":
        '''A reference to a ResourcePolicy resource.'''
        return typing.cast("_ResourcePolicyReference_162e786c", jsii.get(self, "resourcePolicyRef"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> builtins.str:
        '''The JSON to use as the Resource-based Policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d726921aa53fc43f461134d2df5d60edb5d56b4fa67ef6e4e82d305af7b7eba5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workspaceArn")
    def workspace_arn(self) -> builtins.str:
        '''An ARN identifying a Workspace.'''
        return typing.cast(builtins.str, jsii.get(self, "workspaceArn"))

    @workspace_arn.setter
    def workspace_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f020f5d54f91c35f0b4332b16391ef6561cfc07a46cc5fc1e48d4acdb82a4b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy_document": "policyDocument",
        "workspace_arn": "workspaceArn",
    },
)
class CfnResourcePolicyProps:
    def __init__(
        self,
        *,
        policy_document: builtins.str,
        workspace_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param policy_document: The JSON to use as the Resource-based Policy.
        :param workspace_arn: An ARN identifying a Workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_resource_policy_props = aps.CfnResourcePolicyProps(
                policy_document="policyDocument",
                workspace_arn="workspaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb05747fc90b1776c66fd40ec5d261399f93ac6b367fc973d5df8b912bd30997)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument workspace_arn", value=workspace_arn, expected_type=type_hints["workspace_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "workspace_arn": workspace_arn,
        }

    @builtins.property
    def policy_document(self) -> builtins.str:
        '''The JSON to use as the Resource-based Policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-resourcepolicy.html#cfn-aps-resourcepolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_arn(self) -> builtins.str:
        '''An ARN identifying a Workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-resourcepolicy.html#cfn-aps-resourcepolicy-workspacearn
        '''
        result = self._values.get("workspace_arn")
        assert result is not None, "Required property 'workspace_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IRuleGroupsNamespaceRef_7b589be9, _ITaggable_36806126)
class CfnRuleGroupsNamespace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnRuleGroupsNamespace",
):
    '''The definition of a rule groups namespace in an Amazon Managed Service for Prometheus workspace.

    A rule groups namespace is associated with exactly one rules file. A workspace can have multiple rule groups namespaces. For more information about rules files, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ , in the *Amazon Managed Service for Prometheus User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html
    :cloudformationResource: AWS::APS::RuleGroupsNamespace
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_rule_groups_namespace = aps.CfnRuleGroupsNamespace(self, "MyCfnRuleGroupsNamespace",
            data="data",
            name="name",
            workspace="workspace",
        
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
        data: builtins.str,
        name: builtins.str,
        workspace: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::APS::RuleGroupsNamespace``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data: The rules file used in the namespace. For more details about the rules file, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param name: The name of the rule groups namespace.
        :param workspace: The ID of the workspace to add the rule groups namespace.
        :param tags: The list of tag keys and values that are associated with the rule groups namespace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d681a4d4a1e9d9052c98f45bf8b21257e825ee8185b30ea4b6f887fc7416b1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuleGroupsNamespaceProps(
            data=data, name=name, workspace=workspace, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForRuleGroupsNamespace")
    @builtins.classmethod
    def arn_for_rule_groups_namespace(
        cls,
        resource: "_IRuleGroupsNamespaceRef_7b589be9",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61dec5652442e30c74dbfed7f2f112f1c34f77b348a643313ec2df915c902ada)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForRuleGroupsNamespace", [resource]))

    @jsii.member(jsii_name="isCfnRuleGroupsNamespace")
    @builtins.classmethod
    def is_cfn_rule_groups_namespace(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRuleGroupsNamespace.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c082b51948289cdbcbe8597af29e57d1b030d4a63972c4107a81d92696db1d1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRuleGroupsNamespace", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f066376b2a4b15a103f9a01bca66f252615381ddc55bd5508262712fd03eec2d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__501ad912878791d9cc1a45e52a9642fb0747f4ddf4482708286f9bfde7e036de)
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
        '''The ARN of the rule groups namespace.

        For example, ``arn:aws:aps:<region>:123456789012:rulegroupsnamespace/ws-example1-1234-abcd-5678-ef90abcd1234/rulesfile1`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="ruleGroupsNamespaceRef")
    def rule_groups_namespace_ref(self) -> "_RuleGroupsNamespaceReference_9d4673a3":
        '''A reference to a RuleGroupsNamespace resource.'''
        return typing.cast("_RuleGroupsNamespaceReference_9d4673a3", jsii.get(self, "ruleGroupsNamespaceRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> builtins.str:
        '''The rules file used in the namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "data"))

    @data.setter
    def data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__327e955bc86deb15923357f0f050e077304b8dbbb2c9baba9d84a13c5d7b695d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "data", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the rule groups namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f3851e1fa5b758763dff1a85515e41a8c57e1b4da81b2e677f003890944957f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workspace")
    def workspace(self) -> builtins.str:
        '''The ID of the workspace to add the rule groups namespace.'''
        return typing.cast(builtins.str, jsii.get(self, "workspace"))

    @workspace.setter
    def workspace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f899db17dfa1e1837e2b90cca5f83f23f67ca015116201811ad84d044e9ebe95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspace", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The list of tag keys and values that are associated with the rule groups namespace.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9af819e60d52c87c9369e4854d0dfc8d4917db97219839fbc11cf2bdad55659)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnRuleGroupsNamespaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "data": "data",
        "name": "name",
        "workspace": "workspace",
        "tags": "tags",
    },
)
class CfnRuleGroupsNamespaceProps:
    def __init__(
        self,
        *,
        data: builtins.str,
        name: builtins.str,
        workspace: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuleGroupsNamespace``.

        :param data: The rules file used in the namespace. For more details about the rules file, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param name: The name of the rule groups namespace.
        :param workspace: The ID of the workspace to add the rule groups namespace.
        :param tags: The list of tag keys and values that are associated with the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_rule_groups_namespace_props = aps.CfnRuleGroupsNamespaceProps(
                data="data",
                name="name",
                workspace="workspace",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ba9f13df78597d09b62adc5501ac56c5fedca3215c115e02cb7e3be9e440366)
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument workspace", value=workspace, expected_type=type_hints["workspace"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data": data,
            "name": name,
            "workspace": workspace,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data(self) -> builtins.str:
        '''The rules file used in the namespace.

        For more details about the rules file, see `Creating a rules file <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-data
        '''
        result = self._values.get("data")
        assert result is not None, "Required property 'data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace(self) -> builtins.str:
        '''The ID of the workspace to add the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-workspace
        '''
        result = self._values.get("workspace")
        assert result is not None, "Required property 'workspace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The list of tag keys and values that are associated with the rule groups namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-rulegroupsnamespace.html#cfn-aps-rulegroupsnamespace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuleGroupsNamespaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IScraperRef_2b17ef67, _ITaggableV2_4e6798f8)
class CfnScraper(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnScraper",
):
    '''A scraper is a fully-managed agentless collector that discovers and pulls metrics automatically.

    A scraper pulls metrics from Prometheus-compatible sources within an Amazon EKS cluster, and sends them to your Amazon Managed Service for Prometheus workspace. Scrapers are flexible. You can configure the scraper to control what metrics are collected, the frequency of collection, what transformations are applied to the metrics, and more.

    An IAM role will be created for you that Amazon Managed Service for Prometheus uses to access the metrics in your cluster. You must configure this role with a policy that allows it to scrape metrics from your cluster. For more information, see `Configuring your Amazon EKS cluster <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-eks-setup>`_ in the *Amazon Managed Service for Prometheus User Guide* .

    The ``scrapeConfiguration`` parameter contains the YAML configuration for the scraper.
    .. epigraph::

       For more information about collectors, including what metrics are collected, and how to configure the scraper, see `Using an AWS managed collector <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html
    :cloudformationResource: AWS::APS::Scraper
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_scraper = aps.CfnScraper(self, "MyCfnScraper",
            destination=aps.CfnScraper.DestinationProperty(
                amp_configuration=aps.CfnScraper.AmpConfigurationProperty(
                    workspace_arn="workspaceArn"
                )
            ),
            scrape_configuration=aps.CfnScraper.ScrapeConfigurationProperty(
                configuration_blob="configurationBlob"
            ),
            source=aps.CfnScraper.SourceProperty(
                eks_configuration=aps.CfnScraper.EksConfigurationProperty(
                    cluster_arn="clusterArn",
                    subnet_ids=["subnetIds"],
        
                    # the properties below are optional
                    security_group_ids=["securityGroupIds"]
                ),
                vpc_configuration=aps.CfnScraper.VpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            ),
        
            # the properties below are optional
            alias="alias",
            role_configuration=aps.CfnScraper.RoleConfigurationProperty(
                source_role_arn="sourceRoleArn",
                target_role_arn="targetRoleArn"
            ),
            scraper_logging_configuration=aps.CfnScraper.ScraperLoggingConfigurationProperty(
                logging_destination=aps.CfnScraper.ScraperLoggingDestinationProperty(
                    cloud_watch_logs=aps.CfnScraper.CloudWatchLogDestinationProperty(
                        log_group_arn="logGroupArn"
                    )
                ),
                scraper_components=[aps.CfnScraper.ScraperComponentProperty(
                    type="type",
        
                    # the properties below are optional
                    config=aps.CfnScraper.ComponentConfigProperty(
                        options={
                            "options_key": "options"
                        }
                    )
                )]
            ),
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
        destination: typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.DestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        scrape_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.ScrapeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        source: typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
        alias: typing.Optional[builtins.str] = None,
        role_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.RoleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        scraper_logging_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.ScraperLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::APS::Scraper``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination: The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.
        :param scrape_configuration: The configuration in use by the scraper.
        :param source: The Amazon EKS cluster from which the scraper collects metrics.
        :param alias: An optional user-assigned scraper alias.
        :param role_configuration: The role configuration in an Amazon Managed Service for Prometheus scraper.
        :param scraper_logging_configuration: The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.
        :param tags: (Optional) The list of tag keys and values associated with the scraper.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d4cb1653b22b80f73c5fa4972418519c1d58f8ac033d22184f1b74ee25bf2b0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScraperProps(
            destination=destination,
            scrape_configuration=scrape_configuration,
            source=source,
            alias=alias,
            role_configuration=role_configuration,
            scraper_logging_configuration=scraper_logging_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForScraper")
    @builtins.classmethod
    def arn_for_scraper(cls, resource: "_IScraperRef_2b17ef67") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d13ca5c90dffa472e2c1b90166865a8eadf1584a016d1e7bf43dfa45975425b3)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForScraper", [resource]))

    @jsii.member(jsii_name="isCfnScraper")
    @builtins.classmethod
    def is_cfn_scraper(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnScraper.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6666769e6fd345f7b06db92777e9fba61080e45fac0ba311dcb3ffa01dab3d6)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnScraper", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58ef0eaaf8983b897d546f9e872b3a951993e032cd8b5f5f1725e32854f8d096)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d151b530ba64dde831142e12510e32c75c01b169477c6e43bf92c26ab330e2ae)
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
        '''The Amazon Resource Name (ARN) of the scraper.

        For example, ``arn:aws:aps:<region>:123456798012:scraper/s-example1-1234-abcd-5678-ef9012abcd34`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRoleArn")
    def attr_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that provides permissions for the scraper to discover and collect metrics on your behalf.

        For example, ``arn:aws:iam::123456789012:role/service-role/AmazonGrafanaServiceRole-12example`` .

        :cloudformationAttribute: RoleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrScraperId")
    def attr_scraper_id(self) -> builtins.str:
        '''The ID of the scraper.

        For example, ``s-example1-1234-abcd-5678-ef9012abcd34`` .

        :cloudformationAttribute: ScraperId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrScraperId"))

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
    @jsii.member(jsii_name="scraperRef")
    def scraper_ref(self) -> "_ScraperReference_c6b43df1":
        '''A reference to a Scraper resource.'''
        return typing.cast("_ScraperReference_c6b43df1", jsii.get(self, "scraperRef"))

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnScraper.DestinationProperty"]:
        '''The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnScraper.DestinationProperty"], jsii.get(self, "destination"))

    @destination.setter
    def destination(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnScraper.DestinationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d835d9e17a3614f6837476fe3d3de37c4e38685abfd4cc8e4e49236802dfc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scrapeConfiguration")
    def scrape_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnScraper.ScrapeConfigurationProperty"]:
        '''The configuration in use by the scraper.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnScraper.ScrapeConfigurationProperty"], jsii.get(self, "scrapeConfiguration"))

    @scrape_configuration.setter
    def scrape_configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnScraper.ScrapeConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a91c6d3e6031af4c2e1ba10ae98234919eb5f1efa54c12c929f7141e223af9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scrapeConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnScraper.SourceProperty"]:
        '''The Amazon EKS cluster from which the scraper collects metrics.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnScraper.SourceProperty"], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnScraper.SourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4baaa2665d7ddf1c8e51575f5139441f25d102954ee91a2fcbf97644019a8c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        '''An optional user-assigned scraper alias.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36b98e11e4ea8701c0469eb24a036fb1452c2573d264405f3d5237c104fd77a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleConfiguration")
    def role_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.RoleConfigurationProperty"]]:
        '''The role configuration in an Amazon Managed Service for Prometheus scraper.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.RoleConfigurationProperty"]], jsii.get(self, "roleConfiguration"))

    @role_configuration.setter
    def role_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.RoleConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8492f7c00f66de3309f136730786a3ad81d27f787146130fdb2b6191464e92c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scraperLoggingConfiguration")
    def scraper_logging_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.ScraperLoggingConfigurationProperty"]]:
        '''The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.ScraperLoggingConfigurationProperty"]], jsii.get(self, "scraperLoggingConfiguration"))

    @scraper_logging_configuration.setter
    def scraper_logging_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.ScraperLoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98c937c38a5c278540b0a6d9654c4dc0d8dbc46a2f3145fd9275f2a8fd9ce000)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scraperLoggingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''(Optional) The list of tag keys and values associated with the scraper.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__265ada3fe1d3014c11a5af4d87c8e4b691d29a917e8643b804a82b7c3223573f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.AmpConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"workspace_arn": "workspaceArn"},
    )
    class AmpConfigurationProperty:
        def __init__(self, *, workspace_arn: builtins.str) -> None:
            '''The ``AmpConfiguration`` structure defines the Amazon Managed Service for Prometheus instance a scraper should send metrics to.

            :param workspace_arn: ARN of the Amazon Managed Service for Prometheus workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-ampconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                amp_configuration_property = aps.CfnScraper.AmpConfigurationProperty(
                    workspace_arn="workspaceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__02c8f0a43ed30375a3d1b283c2450f310915b0f0fcff6103d168cb18a16bfc4f)
                check_type(argname="argument workspace_arn", value=workspace_arn, expected_type=type_hints["workspace_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workspace_arn": workspace_arn,
            }

        @builtins.property
        def workspace_arn(self) -> builtins.str:
            '''ARN of the Amazon Managed Service for Prometheus workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-ampconfiguration.html#cfn-aps-scraper-ampconfiguration-workspacearn
            '''
            result = self._values.get("workspace_arn")
            assert result is not None, "Required property 'workspace_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmpConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.CloudWatchLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_arn": "logGroupArn"},
    )
    class CloudWatchLogDestinationProperty:
        def __init__(
            self,
            *,
            log_group_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a cloudwatch logs destination for scraper logging.

            :param log_group_arn: ARN of the CloudWatch log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-cloudwatchlogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                cloud_watch_log_destination_property = aps.CfnScraper.CloudWatchLogDestinationProperty(
                    log_group_arn="logGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d4d1b8a234d9b0461189ac94d16b7043b8e40fc1a62680a811ba8396bc54a5d6)
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_arn is not None:
                self._values["log_group_arn"] = log_group_arn

        @builtins.property
        def log_group_arn(self) -> typing.Optional[builtins.str]:
            '''ARN of the CloudWatch log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-cloudwatchlogdestination.html#cfn-aps-scraper-cloudwatchlogdestination-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.ComponentConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"options": "options"},
    )
    class ComponentConfigProperty:
        def __init__(
            self,
            *,
            options: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''Configuration settings for a scraper component.

            :param options: Configuration options for the scraper component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-componentconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                component_config_property = aps.CfnScraper.ComponentConfigProperty(
                    options={
                        "options_key": "options"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c81abd8a9526f73204a9bfa774d69e9b3ec81f7592dafabd756679cc66dcb1e1)
                check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if options is not None:
                self._values["options"] = options

        @builtins.property
        def options(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]]:
            '''Configuration options for the scraper component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-componentconfig.html#cfn-aps-scraper-componentconfig-options
            '''
            result = self._values.get("options")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComponentConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"amp_configuration": "ampConfiguration"},
    )
    class DestinationProperty:
        def __init__(
            self,
            *,
            amp_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.AmpConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Where to send the metrics from a scraper.

            :param amp_configuration: The Amazon Managed Service for Prometheus workspace to send metrics to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                destination_property = aps.CfnScraper.DestinationProperty(
                    amp_configuration=aps.CfnScraper.AmpConfigurationProperty(
                        workspace_arn="workspaceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9dfeb013903b3b566e12e34ac903da7aaad96412ee8622e798d0f4931b78c31)
                check_type(argname="argument amp_configuration", value=amp_configuration, expected_type=type_hints["amp_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "amp_configuration": amp_configuration,
            }

        @builtins.property
        def amp_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnScraper.AmpConfigurationProperty"]:
            '''The Amazon Managed Service for Prometheus workspace to send metrics to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-destination.html#cfn-aps-scraper-destination-ampconfiguration
            '''
            result = self._values.get("amp_configuration")
            assert result is not None, "Required property 'amp_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnScraper.AmpConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.EksConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_arn": "clusterArn",
            "subnet_ids": "subnetIds",
            "security_group_ids": "securityGroupIds",
        },
    )
    class EksConfigurationProperty:
        def __init__(
            self,
            *,
            cluster_arn: builtins.str,
            subnet_ids: typing.Sequence[builtins.str],
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The ``EksConfiguration`` structure describes the connection to the Amazon EKS cluster from which a scraper collects metrics.

            :param cluster_arn: ARN of the Amazon EKS cluster.
            :param subnet_ids: A list of subnet IDs for the Amazon EKS cluster VPC configuration.
            :param security_group_ids: A list of the security group IDs for the Amazon EKS cluster VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                eks_configuration_property = aps.CfnScraper.EksConfigurationProperty(
                    cluster_arn="clusterArn",
                    subnet_ids=["subnetIds"],
                
                    # the properties below are optional
                    security_group_ids=["securityGroupIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d84c728405d664f762d3c86aae8f989f77a50273eb74e76dce90e3e0305f06a9)
                check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_arn": cluster_arn,
                "subnet_ids": subnet_ids,
            }
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids

        @builtins.property
        def cluster_arn(self) -> builtins.str:
            '''ARN of the Amazon EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html#cfn-aps-scraper-eksconfiguration-clusterarn
            '''
            result = self._values.get("cluster_arn")
            assert result is not None, "Required property 'cluster_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''A list of subnet IDs for the Amazon EKS cluster VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html#cfn-aps-scraper-eksconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the security group IDs for the Amazon EKS cluster VPC configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-eksconfiguration.html#cfn-aps-scraper-eksconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.RoleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_role_arn": "sourceRoleArn",
            "target_role_arn": "targetRoleArn",
        },
    )
    class RoleConfigurationProperty:
        def __init__(
            self,
            *,
            source_role_arn: typing.Optional[builtins.str] = None,
            target_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The role configuration in an Amazon Managed Service for Prometheus scraper.

            :param source_role_arn: The ARN of the source role.
            :param target_role_arn: The ARN of the target role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-roleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                role_configuration_property = aps.CfnScraper.RoleConfigurationProperty(
                    source_role_arn="sourceRoleArn",
                    target_role_arn="targetRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86bf03aa28256ae3502c8e0745b810c6f1fe11b530f463788b7c7ffd32d996d1)
                check_type(argname="argument source_role_arn", value=source_role_arn, expected_type=type_hints["source_role_arn"])
                check_type(argname="argument target_role_arn", value=target_role_arn, expected_type=type_hints["target_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source_role_arn is not None:
                self._values["source_role_arn"] = source_role_arn
            if target_role_arn is not None:
                self._values["target_role_arn"] = target_role_arn

        @builtins.property
        def source_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the source role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-roleconfiguration.html#cfn-aps-scraper-roleconfiguration-sourcerolearn
            '''
            result = self._values.get("source_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the target role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-roleconfiguration.html#cfn-aps-scraper-roleconfiguration-targetrolearn
            '''
            result = self._values.get("target_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.ScrapeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"configuration_blob": "configurationBlob"},
    )
    class ScrapeConfigurationProperty:
        def __init__(self, *, configuration_blob: builtins.str) -> None:
            '''A scrape configuration for a scraper, base 64 encoded.

            For more information, see `Scraper configuration <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-collector-how-to.html#AMP-collector-configuration>`_ in the *Amazon Managed Service for Prometheus User Guide* .

            :param configuration_blob: The base 64 encoded scrape configuration file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                scrape_configuration_property = aps.CfnScraper.ScrapeConfigurationProperty(
                    configuration_blob="configurationBlob"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__61507a1463486662c27c8fec99a5cb181f22e5f346b7bb6d10823ad9b7102b72)
                check_type(argname="argument configuration_blob", value=configuration_blob, expected_type=type_hints["configuration_blob"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_blob": configuration_blob,
            }

        @builtins.property
        def configuration_blob(self) -> builtins.str:
            '''The base 64 encoded scrape configuration file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapeconfiguration.html#cfn-aps-scraper-scrapeconfiguration-configurationblob
            '''
            result = self._values.get("configuration_blob")
            assert result is not None, "Required property 'configuration_blob' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScrapeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.ScraperComponentProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "config": "config"},
    )
    class ScraperComponentProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.ComponentConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A component of a Amazon Managed Service for Prometheus scraper that can be configured for logging.

            :param type: The type of the scraper component.
            :param config: The configuration settings for the scraper component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapercomponent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                scraper_component_property = aps.CfnScraper.ScraperComponentProperty(
                    type="type",
                
                    # the properties below are optional
                    config=aps.CfnScraper.ComponentConfigProperty(
                        options={
                            "options_key": "options"
                        }
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be259f573540cfe3fb130cbc10c656811dffac0fb6663b27b9f4982549990b6a)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument config", value=config, expected_type=type_hints["config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if config is not None:
                self._values["config"] = config

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the scraper component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapercomponent.html#cfn-aps-scraper-scrapercomponent-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.ComponentConfigProperty"]]:
            '''The configuration settings for the scraper component.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scrapercomponent.html#cfn-aps-scraper-scrapercomponent-config
            '''
            result = self._values.get("config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.ComponentConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScraperComponentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.ScraperLoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "logging_destination": "loggingDestination",
            "scraper_components": "scraperComponents",
        },
    )
    class ScraperLoggingConfigurationProperty:
        def __init__(
            self,
            *,
            logging_destination: typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.ScraperLoggingDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            scraper_components: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.ScraperComponentProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Configuration for scraper logging.

            :param logging_destination: Destination for scraper logging.
            :param scraper_components: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scraperloggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                scraper_logging_configuration_property = aps.CfnScraper.ScraperLoggingConfigurationProperty(
                    logging_destination=aps.CfnScraper.ScraperLoggingDestinationProperty(
                        cloud_watch_logs=aps.CfnScraper.CloudWatchLogDestinationProperty(
                            log_group_arn="logGroupArn"
                        )
                    ),
                    scraper_components=[aps.CfnScraper.ScraperComponentProperty(
                        type="type",
                
                        # the properties below are optional
                        config=aps.CfnScraper.ComponentConfigProperty(
                            options={
                                "options_key": "options"
                            }
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ea5221003b2ff43404935c67045669a8a84790d807c849eadd6df28ea9b60feb)
                check_type(argname="argument logging_destination", value=logging_destination, expected_type=type_hints["logging_destination"])
                check_type(argname="argument scraper_components", value=scraper_components, expected_type=type_hints["scraper_components"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "logging_destination": logging_destination,
                "scraper_components": scraper_components,
            }

        @builtins.property
        def logging_destination(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnScraper.ScraperLoggingDestinationProperty"]:
            '''Destination for scraper logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scraperloggingconfiguration.html#cfn-aps-scraper-scraperloggingconfiguration-loggingdestination
            '''
            result = self._values.get("logging_destination")
            assert result is not None, "Required property 'logging_destination' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnScraper.ScraperLoggingDestinationProperty"], result)

        @builtins.property
        def scraper_components(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnScraper.ScraperComponentProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scraperloggingconfiguration.html#cfn-aps-scraper-scraperloggingconfiguration-scrapercomponents
            '''
            result = self._values.get("scraper_components")
            assert result is not None, "Required property 'scraper_components' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnScraper.ScraperComponentProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScraperLoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.ScraperLoggingDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_logs": "cloudWatchLogs"},
    )
    class ScraperLoggingDestinationProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.CloudWatchLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The destination where scraper logs are sent.

            :param cloud_watch_logs: The CloudWatch Logs configuration for the scraper logging destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scraperloggingdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                scraper_logging_destination_property = aps.CfnScraper.ScraperLoggingDestinationProperty(
                    cloud_watch_logs=aps.CfnScraper.CloudWatchLogDestinationProperty(
                        log_group_arn="logGroupArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63a27055fededd95d1bc1fba74349c5f0f37894ed254d1e1ce3d670ded2f515f)
                check_type(argname="argument cloud_watch_logs", value=cloud_watch_logs, expected_type=type_hints["cloud_watch_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_logs is not None:
                self._values["cloud_watch_logs"] = cloud_watch_logs

        @builtins.property
        def cloud_watch_logs(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.CloudWatchLogDestinationProperty"]]:
            '''The CloudWatch Logs configuration for the scraper logging destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-scraperloggingdestination.html#cfn-aps-scraper-scraperloggingdestination-cloudwatchlogs
            '''
            result = self._values.get("cloud_watch_logs")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.CloudWatchLogDestinationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScraperLoggingDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "eks_configuration": "eksConfiguration",
            "vpc_configuration": "vpcConfiguration",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            eks_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.EksConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            vpc_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.VpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source of collected metrics for a scraper.

            :param eks_configuration: The Amazon EKS cluster from which a scraper collects metrics.
            :param vpc_configuration: Configuration for VPC metrics source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                source_property = aps.CfnScraper.SourceProperty(
                    eks_configuration=aps.CfnScraper.EksConfigurationProperty(
                        cluster_arn="clusterArn",
                        subnet_ids=["subnetIds"],
                
                        # the properties below are optional
                        security_group_ids=["securityGroupIds"]
                    ),
                    vpc_configuration=aps.CfnScraper.VpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__655e83ac40d7d6fcc3362aa2c25fcfadc0beb5744ef393de105d7d152821a330)
                check_type(argname="argument eks_configuration", value=eks_configuration, expected_type=type_hints["eks_configuration"])
                check_type(argname="argument vpc_configuration", value=vpc_configuration, expected_type=type_hints["vpc_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if eks_configuration is not None:
                self._values["eks_configuration"] = eks_configuration
            if vpc_configuration is not None:
                self._values["vpc_configuration"] = vpc_configuration

        @builtins.property
        def eks_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.EksConfigurationProperty"]]:
            '''The Amazon EKS cluster from which a scraper collects metrics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-source.html#cfn-aps-scraper-source-eksconfiguration
            '''
            result = self._values.get("eks_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.EksConfigurationProperty"]], result)

        @builtins.property
        def vpc_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.VpcConfigurationProperty"]]:
            '''Configuration for VPC metrics source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-source.html#cfn-aps-scraper-source-vpcconfiguration
            '''
            result = self._values.get("vpc_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.VpcConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnScraper.VpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''Configuration for VPC metrics source.

            :param security_group_ids: List of security group IDs.
            :param subnet_ids: List of subnet IDs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-vpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                vpc_configuration_property = aps.CfnScraper.VpcConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d146d8aa0a745fdc1f1efcc28a958a65b5bbc1a22d0e9673168bcec89aea649)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''List of security group IDs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-vpcconfiguration.html#cfn-aps-scraper-vpcconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''List of subnet IDs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-scraper-vpcconfiguration.html#cfn-aps-scraper-vpcconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnScraperProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "scrape_configuration": "scrapeConfiguration",
        "source": "source",
        "alias": "alias",
        "role_configuration": "roleConfiguration",
        "scraper_logging_configuration": "scraperLoggingConfiguration",
        "tags": "tags",
    },
)
class CfnScraperProps:
    def __init__(
        self,
        *,
        destination: typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.DestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        scrape_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.ScrapeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        source: typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
        alias: typing.Optional[builtins.str] = None,
        role_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.RoleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        scraper_logging_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnScraper.ScraperLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnScraper``.

        :param destination: The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.
        :param scrape_configuration: The configuration in use by the scraper.
        :param source: The Amazon EKS cluster from which the scraper collects metrics.
        :param alias: An optional user-assigned scraper alias.
        :param role_configuration: The role configuration in an Amazon Managed Service for Prometheus scraper.
        :param scraper_logging_configuration: The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.
        :param tags: (Optional) The list of tag keys and values associated with the scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_scraper_props = aps.CfnScraperProps(
                destination=aps.CfnScraper.DestinationProperty(
                    amp_configuration=aps.CfnScraper.AmpConfigurationProperty(
                        workspace_arn="workspaceArn"
                    )
                ),
                scrape_configuration=aps.CfnScraper.ScrapeConfigurationProperty(
                    configuration_blob="configurationBlob"
                ),
                source=aps.CfnScraper.SourceProperty(
                    eks_configuration=aps.CfnScraper.EksConfigurationProperty(
                        cluster_arn="clusterArn",
                        subnet_ids=["subnetIds"],
            
                        # the properties below are optional
                        security_group_ids=["securityGroupIds"]
                    ),
                    vpc_configuration=aps.CfnScraper.VpcConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_ids=["subnetIds"]
                    )
                ),
            
                # the properties below are optional
                alias="alias",
                role_configuration=aps.CfnScraper.RoleConfigurationProperty(
                    source_role_arn="sourceRoleArn",
                    target_role_arn="targetRoleArn"
                ),
                scraper_logging_configuration=aps.CfnScraper.ScraperLoggingConfigurationProperty(
                    logging_destination=aps.CfnScraper.ScraperLoggingDestinationProperty(
                        cloud_watch_logs=aps.CfnScraper.CloudWatchLogDestinationProperty(
                            log_group_arn="logGroupArn"
                        )
                    ),
                    scraper_components=[aps.CfnScraper.ScraperComponentProperty(
                        type="type",
            
                        # the properties below are optional
                        config=aps.CfnScraper.ComponentConfigProperty(
                            options={
                                "options_key": "options"
                            }
                        )
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f302dfc2aa92636b313e32f5d91a0ccfd79ebde0259b977f6291d4c8329455d7)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument scrape_configuration", value=scrape_configuration, expected_type=type_hints["scrape_configuration"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument role_configuration", value=role_configuration, expected_type=type_hints["role_configuration"])
            check_type(argname="argument scraper_logging_configuration", value=scraper_logging_configuration, expected_type=type_hints["scraper_logging_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "scrape_configuration": scrape_configuration,
            "source": source,
        }
        if alias is not None:
            self._values["alias"] = alias
        if role_configuration is not None:
            self._values["role_configuration"] = role_configuration
        if scraper_logging_configuration is not None:
            self._values["scraper_logging_configuration"] = scraper_logging_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnScraper.DestinationProperty"]:
        '''The Amazon Managed Service for Prometheus workspace the scraper sends metrics to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-destination
        '''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnScraper.DestinationProperty"], result)

    @builtins.property
    def scrape_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnScraper.ScrapeConfigurationProperty"]:
        '''The configuration in use by the scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-scrapeconfiguration
        '''
        result = self._values.get("scrape_configuration")
        assert result is not None, "Required property 'scrape_configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnScraper.ScrapeConfigurationProperty"], result)

    @builtins.property
    def source(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnScraper.SourceProperty"]:
        '''The Amazon EKS cluster from which the scraper collects metrics.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnScraper.SourceProperty"], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''An optional user-assigned scraper alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-alias
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.RoleConfigurationProperty"]]:
        '''The role configuration in an Amazon Managed Service for Prometheus scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-roleconfiguration
        '''
        result = self._values.get("role_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.RoleConfigurationProperty"]], result)

    @builtins.property
    def scraper_logging_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.ScraperLoggingConfigurationProperty"]]:
        '''The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-scraperloggingconfiguration
        '''
        result = self._values.get("scraper_logging_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnScraper.ScraperLoggingConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''(Optional) The list of tag keys and values associated with the scraper.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-scraper.html#cfn-aps-scraper-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScraperProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IWorkspaceRef_d8b2b588, _ITaggable_36806126)
class CfnWorkspace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace",
):
    '''An Amazon Managed Service for Prometheus workspace is a logical and isolated Prometheus server dedicated to ingesting, storing, and querying your Prometheus-compatible metrics.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html
    :cloudformationResource: AWS::APS::Workspace
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_aps as aps
        
        cfn_workspace = aps.CfnWorkspace(self, "MyCfnWorkspace",
            alert_manager_definition="alertManagerDefinition",
            alias="alias",
            kms_key_arn="kmsKeyArn",
            logging_configuration=aps.CfnWorkspace.LoggingConfigurationProperty(
                log_group_arn="logGroupArn"
            ),
            query_logging_configuration=aps.CfnWorkspace.QueryLoggingConfigurationProperty(
                destinations=[aps.CfnWorkspace.LoggingDestinationProperty(
                    cloud_watch_logs=aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                        log_group_arn="logGroupArn"
                    ),
                    filters=aps.CfnWorkspace.LoggingFilterProperty(
                        qsp_threshold=123
                    )
                )]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            workspace_configuration=aps.CfnWorkspace.WorkspaceConfigurationProperty(
                limits_per_label_sets=[aps.CfnWorkspace.LimitsPerLabelSetProperty(
                    label_set=[aps.CfnWorkspace.LabelProperty(
                        name="name",
                        value="value"
                    )],
                    limits=aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                        max_series=123
                    )
                )],
                retention_period_in_days=123
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        alert_manager_definition: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        query_logging_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.QueryLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        workspace_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.WorkspaceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::APS::Workspace``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alert_manager_definition: The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace. For details about the alert manager definition, see `Creating an alert manager configuration files <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html>`_ in the *Amazon Managed Service for Prometheus User Guide* . The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the ``- |-`` ). ``Workspace: Type: AWS::APS::Workspace .... Properties: .... AlertManagerDefinition: Fn::Sub: - |- alertmanager_config: | templates: - 'default_template' route: receiver: example-sns receivers: - name: example-sns sns_configs: - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}' -``
        :param alias: The alias that is assigned to this workspace to help identify it. It does not need to be unique.
        :param kms_key_arn: (optional) The ARN for a customer managed AWS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param logging_configuration: Contains information about the logging configuration for the workspace.
        :param query_logging_configuration: The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.
        :param tags: The list of tag keys and values that are associated with the workspace.
        :param workspace_configuration: Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d7d4de6c2c3c0a6cc1f746f35f29f98344da5c5d59e48a9d1e788ab80e3ef9b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkspaceProps(
            alert_manager_definition=alert_manager_definition,
            alias=alias,
            kms_key_arn=kms_key_arn,
            logging_configuration=logging_configuration,
            query_logging_configuration=query_logging_configuration,
            tags=tags,
            workspace_configuration=workspace_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForWorkspace")
    @builtins.classmethod
    def arn_for_workspace(cls, resource: "_IWorkspaceRef_d8b2b588") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3d6e079335cf4fb62650b716c0e1e39e889e44a3c76895cf3db3d9711219145)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForWorkspace", [resource]))

    @jsii.member(jsii_name="isCfnWorkspace")
    @builtins.classmethod
    def is_cfn_workspace(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnWorkspace.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__490b818275597aad87e1201e93dad0f3f96ca81aa2b2e7254029ea1f42a73cb3)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnWorkspace", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ea1a406920301232e7f737fa791c75b19a41702c2a8761c41de9163390ebcdf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__391b593ff5f1b04fd33a43b56be0c4a7f41dd147af44a0bc665b22d97e9640c8)
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
        '''The ARN of the workspace.

        For example, ``arn:aws:aps:<region>:123456789012:workspace/ws-example1-1234-abcd-5678-ef90abcd1234`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPrometheusEndpoint")
    def attr_prometheus_endpoint(self) -> builtins.str:
        '''The Prometheus endpoint available for this workspace.

        For example, ``https://aps-workspaces.<region>.amazonaws.com/workspaces/ws-example1-1234-abcd-5678-ef90abcd1234/api/v1/`` .

        :cloudformationAttribute: PrometheusEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPrometheusEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkspaceId")
    def attr_workspace_id(self) -> builtins.str:
        '''The unique ID for the workspace.

        For example, ``ws-example1-1234-abcd-5678-ef90abcd1234`` .

        :cloudformationAttribute: WorkspaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkspaceId"))

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
    @jsii.member(jsii_name="workspaceRef")
    def workspace_ref(self) -> "_WorkspaceReference_4f6a6126":
        '''A reference to a Workspace resource.'''
        return typing.cast("_WorkspaceReference_4f6a6126", jsii.get(self, "workspaceRef"))

    @builtins.property
    @jsii.member(jsii_name="alertManagerDefinition")
    def alert_manager_definition(self) -> typing.Optional[builtins.str]:
        '''The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alertManagerDefinition"))

    @alert_manager_definition.setter
    def alert_manager_definition(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c2399f13a196d4fdd83827148d3942b4231e42e722c32b0c66a56f8425f5d1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alertManagerDefinition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="alias")
    def alias(self) -> typing.Optional[builtins.str]:
        '''The alias that is assigned to this workspace to help identify it.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "alias"))

    @alias.setter
    def alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69c703012a200792f370b43791a7b9e6c8ab12b196993de037a82396c6c51b3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''(optional) The ARN for a customer managed AWS  key to use for encrypting data within your workspace.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e1bc26d25cdad92f552b6ceb5e8a4ae6d459a5f2737ae032c5a2f069eedf68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LoggingConfigurationProperty"]]:
        '''Contains information about the logging configuration for the workspace.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LoggingConfigurationProperty"]], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab06dccfc037b2ba3e02b4a3154224a63edcfe3fc06381ff9162c2c33a94b712)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="queryLoggingConfiguration")
    def query_logging_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.QueryLoggingConfigurationProperty"]]:
        '''The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.QueryLoggingConfigurationProperty"]], jsii.get(self, "queryLoggingConfiguration"))

    @query_logging_configuration.setter
    def query_logging_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.QueryLoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6591166b06ced49bc35c6390884a7a1c30cea4102022183768ac43e25c00f9fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryLoggingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The list of tag keys and values that are associated with the workspace.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb4e1977fb1f7aad47144a42af408e41c9d01794f3569a614a9ed54effb1c1e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workspaceConfiguration")
    def workspace_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.WorkspaceConfigurationProperty"]]:
        '''Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.WorkspaceConfigurationProperty"]], jsii.get(self, "workspaceConfiguration"))

    @workspace_configuration.setter
    def workspace_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.WorkspaceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dc44ff5af32b5cdcf5234cdf89709e32cf5a9217d64f6f2b6625191085cd191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workspaceConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.CloudWatchLogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_arn": "logGroupArn"},
    )
    class CloudWatchLogDestinationProperty:
        def __init__(self, *, log_group_arn: builtins.str) -> None:
            '''Configuration details for logging to CloudWatch Logs.

            :param log_group_arn: The ARN of the CloudWatch log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-cloudwatchlogdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                cloud_watch_log_destination_property = aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                    log_group_arn="logGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__925c774442f9150193a5d3bfa3fb05562aec6581139c1378b5f09e1c30fb40ee)
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_arn": log_group_arn,
            }

        @builtins.property
        def log_group_arn(self) -> builtins.str:
            '''The ARN of the CloudWatch log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-cloudwatchlogdestination.html#cfn-aps-workspace-cloudwatchlogdestination-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            assert result is not None, "Required property 'log_group_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LabelProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class LabelProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''A label is a name:value pair used to add context to ingested metrics.

            This structure defines the name and value for one label that is used in a label set. You can set ingestion limits on time series that match defined label sets, to help prevent a workspace from being overwhelmed with unexpected spikes in time series ingestion.

            :param name: The name for this label.
            :param value: The value for this label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-label.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                label_property = aps.CfnWorkspace.LabelProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b34eb56a3257d05ed157ec9252590ce797546e9e647035e7f3e639a6629c1cd3)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name for this label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-label.html#cfn-aps-workspace-label-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value for this label.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-label.html#cfn-aps-workspace-label-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LimitsPerLabelSetEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"max_series": "maxSeries"},
    )
    class LimitsPerLabelSetEntryProperty:
        def __init__(self, *, max_series: typing.Optional[jsii.Number] = None) -> None:
            '''This structure contains the limits that apply to time series that match one label set.

            :param max_series: The maximum number of active series that can be ingested that match this label set. Setting this to 0 causes no label set limit to be enforced, but it does cause Amazon Managed Service for Prometheus to vend label set metrics to CloudWatch

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelsetentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                limits_per_label_set_entry_property = aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                    max_series=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86191e69da536181f19aaae8e8a81e682e12b975b6edce1319b4d4a8b451cb95)
                check_type(argname="argument max_series", value=max_series, expected_type=type_hints["max_series"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_series is not None:
                self._values["max_series"] = max_series

        @builtins.property
        def max_series(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of active series that can be ingested that match this label set.

            Setting this to 0 causes no label set limit to be enforced, but it does cause Amazon Managed Service for Prometheus to vend label set metrics to CloudWatch

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelsetentry.html#cfn-aps-workspace-limitsperlabelsetentry-maxseries
            '''
            result = self._values.get("max_series")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LimitsPerLabelSetEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LimitsPerLabelSetProperty",
        jsii_struct_bases=[],
        name_mapping={"label_set": "labelSet", "limits": "limits"},
    )
    class LimitsPerLabelSetProperty:
        def __init__(
            self,
            *,
            label_set: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.LabelProperty", typing.Dict[builtins.str, typing.Any]]]]],
            limits: typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.LimitsPerLabelSetEntryProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''This defines a label set for the workspace, and defines the ingestion limit for active time series that match that label set.

            Each label name in a label set must be unique.

            :param label_set: This defines one label set that will have an enforced ingestion limit. You can set ingestion limits on time series that match defined label sets, to help prevent a workspace from being overwhelmed with unexpected spikes in time series ingestion. Label values accept all UTF-8 characters with one exception. If the label name is metric name label ``__ *name* __`` , then the *metric* part of the name must conform to the following pattern: ``[a-zA-Z_:][a-zA-Z0-9_:]*``
            :param limits: This structure contains the information about the limits that apply to time series that match this label set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                limits_per_label_set_property = aps.CfnWorkspace.LimitsPerLabelSetProperty(
                    label_set=[aps.CfnWorkspace.LabelProperty(
                        name="name",
                        value="value"
                    )],
                    limits=aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                        max_series=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d8045fc76bdfc4af5de994e0ebe3331fd81257f1ae53d90373a7ad960b0bca7)
                check_type(argname="argument label_set", value=label_set, expected_type=type_hints["label_set"])
                check_type(argname="argument limits", value=limits, expected_type=type_hints["limits"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "label_set": label_set,
                "limits": limits,
            }

        @builtins.property
        def label_set(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LabelProperty"]]]:
            '''This defines one label set that will have an enforced ingestion limit.

            You can set ingestion limits on time series that match defined label sets, to help prevent a workspace from being overwhelmed with unexpected spikes in time series ingestion.

            Label values accept all UTF-8 characters with one exception. If the label name is metric name label ``__ *name* __`` , then the *metric* part of the name must conform to the following pattern: ``[a-zA-Z_:][a-zA-Z0-9_:]*``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelset.html#cfn-aps-workspace-limitsperlabelset-labelset
            '''
            result = self._values.get("label_set")
            assert result is not None, "Required property 'label_set' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LabelProperty"]]], result)

        @builtins.property
        def limits(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LimitsPerLabelSetEntryProperty"]:
            '''This structure contains the information about the limits that apply to time series that match this label set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-limitsperlabelset.html#cfn-aps-workspace-limitsperlabelset-limits
            '''
            result = self._values.get("limits")
            assert result is not None, "Required property 'limits' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LimitsPerLabelSetEntryProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LimitsPerLabelSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_arn": "logGroupArn"},
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the rules and alerting logging configuration for the workspace.

            .. epigraph::

               These logging configurations are only for rules and alerting logs.

            :param log_group_arn: The ARN of the CloudWatch log group to which the vended log data will be published. This log group must exist prior to calling this operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                logging_configuration_property = aps.CfnWorkspace.LoggingConfigurationProperty(
                    log_group_arn="logGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa0678eca2188c6c3220d708f7d16298acecab165f03de8b400d1fada6a4b9d9)
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_arn is not None:
                self._values["log_group_arn"] = log_group_arn

        @builtins.property
        def log_group_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the CloudWatch log group to which the vended log data will be published.

            This log group must exist prior to calling this operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingconfiguration.html#cfn-aps-workspace-loggingconfiguration-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LoggingDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_logs": "cloudWatchLogs", "filters": "filters"},
    )
    class LoggingDestinationProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.CloudWatchLogDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            filters: typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.LoggingFilterProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The logging destination in an Amazon Managed Service for Prometheus workspace.

            :param cloud_watch_logs: Configuration details for logging to CloudWatch Logs.
            :param filters: Filtering criteria that determine which queries are logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                logging_destination_property = aps.CfnWorkspace.LoggingDestinationProperty(
                    cloud_watch_logs=aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                        log_group_arn="logGroupArn"
                    ),
                    filters=aps.CfnWorkspace.LoggingFilterProperty(
                        qsp_threshold=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cce5991812152322bf70db3d7cea0d7bb3cda26bb6b0e82d9bd091ef05995168)
                check_type(argname="argument cloud_watch_logs", value=cloud_watch_logs, expected_type=type_hints["cloud_watch_logs"])
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch_logs": cloud_watch_logs,
                "filters": filters,
            }

        @builtins.property
        def cloud_watch_logs(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnWorkspace.CloudWatchLogDestinationProperty"]:
            '''Configuration details for logging to CloudWatch Logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingdestination.html#cfn-aps-workspace-loggingdestination-cloudwatchlogs
            '''
            result = self._values.get("cloud_watch_logs")
            assert result is not None, "Required property 'cloud_watch_logs' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnWorkspace.CloudWatchLogDestinationProperty"], result)

        @builtins.property
        def filters(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LoggingFilterProperty"]:
            '''Filtering criteria that determine which queries are logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingdestination.html#cfn-aps-workspace-loggingdestination-filters
            '''
            result = self._values.get("filters")
            assert result is not None, "Required property 'filters' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LoggingFilterProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.LoggingFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"qsp_threshold": "qspThreshold"},
    )
    class LoggingFilterProperty:
        def __init__(self, *, qsp_threshold: jsii.Number) -> None:
            '''Filtering criteria that determine which queries are logged.

            :param qsp_threshold: The Query Samples Processed (QSP) threshold above which queries will be logged. Queries processing more samples than this threshold will be captured in logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                logging_filter_property = aps.CfnWorkspace.LoggingFilterProperty(
                    qsp_threshold=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f1710f9a533b3c78aa9735866c9480208fe7ceb912d68581872b145d4c634fd)
                check_type(argname="argument qsp_threshold", value=qsp_threshold, expected_type=type_hints["qsp_threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "qsp_threshold": qsp_threshold,
            }

        @builtins.property
        def qsp_threshold(self) -> jsii.Number:
            '''The Query Samples Processed (QSP) threshold above which queries will be logged.

            Queries processing more samples than this threshold will be captured in logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-loggingfilter.html#cfn-aps-workspace-loggingfilter-qspthreshold
            '''
            result = self._values.get("qsp_threshold")
            assert result is not None, "Required property 'qsp_threshold' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.QueryLoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"destinations": "destinations"},
    )
    class QueryLoggingConfigurationProperty:
        def __init__(
            self,
            *,
            destinations: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.LoggingDestinationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The query logging configuration in an Amazon Managed Service for Prometheus workspace.

            :param destinations: Defines a destination and its associated filtering criteria for query logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-queryloggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                query_logging_configuration_property = aps.CfnWorkspace.QueryLoggingConfigurationProperty(
                    destinations=[aps.CfnWorkspace.LoggingDestinationProperty(
                        cloud_watch_logs=aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                            log_group_arn="logGroupArn"
                        ),
                        filters=aps.CfnWorkspace.LoggingFilterProperty(
                            qsp_threshold=123
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__59e9b7a5bb1ecf6d3e6bf0c4d2f497bea98d1fe68b36d502a98c9b336781a58a)
                check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destinations": destinations,
            }

        @builtins.property
        def destinations(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LoggingDestinationProperty"]]]:
            '''Defines a destination and its associated filtering criteria for query logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-queryloggingconfiguration.html#cfn-aps-workspace-queryloggingconfiguration-destinations
            '''
            result = self._values.get("destinations")
            assert result is not None, "Required property 'destinations' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LoggingDestinationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryLoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_aps.CfnWorkspace.WorkspaceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "limits_per_label_sets": "limitsPerLabelSets",
            "retention_period_in_days": "retentionPeriodInDays",
        },
    )
    class WorkspaceConfigurationProperty:
        def __init__(
            self,
            *,
            limits_per_label_sets: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.LimitsPerLabelSetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            retention_period_in_days: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.

            :param limits_per_label_sets: This is an array of structures, where each structure defines a label set for the workspace, and defines the ingestion limit for active time series for each of those label sets. Each label name in a label set must be unique.
            :param retention_period_in_days: Specifies how many days that metrics will be retained in the workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-workspaceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_aps as aps
                
                workspace_configuration_property = aps.CfnWorkspace.WorkspaceConfigurationProperty(
                    limits_per_label_sets=[aps.CfnWorkspace.LimitsPerLabelSetProperty(
                        label_set=[aps.CfnWorkspace.LabelProperty(
                            name="name",
                            value="value"
                        )],
                        limits=aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                            max_series=123
                        )
                    )],
                    retention_period_in_days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d8bd4b9a39be1594ef4681992e92f89f24816c775c0e0c40e340be13e59392a)
                check_type(argname="argument limits_per_label_sets", value=limits_per_label_sets, expected_type=type_hints["limits_per_label_sets"])
                check_type(argname="argument retention_period_in_days", value=retention_period_in_days, expected_type=type_hints["retention_period_in_days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if limits_per_label_sets is not None:
                self._values["limits_per_label_sets"] = limits_per_label_sets
            if retention_period_in_days is not None:
                self._values["retention_period_in_days"] = retention_period_in_days

        @builtins.property
        def limits_per_label_sets(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LimitsPerLabelSetProperty"]]]]:
            '''This is an array of structures, where each structure defines a label set for the workspace, and defines the ingestion limit for active time series for each of those label sets.

            Each label name in a label set must be unique.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-workspaceconfiguration.html#cfn-aps-workspace-workspaceconfiguration-limitsperlabelsets
            '''
            result = self._values.get("limits_per_label_sets")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LimitsPerLabelSetProperty"]]]], result)

        @builtins.property
        def retention_period_in_days(self) -> typing.Optional[jsii.Number]:
            '''Specifies how many days that metrics will be retained in the workspace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-aps-workspace-workspaceconfiguration.html#cfn-aps-workspace-workspaceconfiguration-retentionperiodindays
            '''
            result = self._values.get("retention_period_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkspaceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_aps.CfnWorkspaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "alert_manager_definition": "alertManagerDefinition",
        "alias": "alias",
        "kms_key_arn": "kmsKeyArn",
        "logging_configuration": "loggingConfiguration",
        "query_logging_configuration": "queryLoggingConfiguration",
        "tags": "tags",
        "workspace_configuration": "workspaceConfiguration",
    },
)
class CfnWorkspaceProps:
    def __init__(
        self,
        *,
        alert_manager_definition: typing.Optional[builtins.str] = None,
        alias: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        logging_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        query_logging_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.QueryLoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        workspace_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkspace.WorkspaceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkspace``.

        :param alert_manager_definition: The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace. For details about the alert manager definition, see `Creating an alert manager configuration files <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html>`_ in the *Amazon Managed Service for Prometheus User Guide* . The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the ``- |-`` ). ``Workspace: Type: AWS::APS::Workspace .... Properties: .... AlertManagerDefinition: Fn::Sub: - |- alertmanager_config: | templates: - 'default_template' route: receiver: example-sns receivers: - name: example-sns sns_configs: - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}' -``
        :param alias: The alias that is assigned to this workspace to help identify it. It does not need to be unique.
        :param kms_key_arn: (optional) The ARN for a customer managed AWS key to use for encrypting data within your workspace. For more information about using your own key in your workspace, see `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .
        :param logging_configuration: Contains information about the logging configuration for the workspace.
        :param query_logging_configuration: The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.
        :param tags: The list of tag keys and values that are associated with the workspace.
        :param workspace_configuration: Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_aps as aps
            
            cfn_workspace_props = aps.CfnWorkspaceProps(
                alert_manager_definition="alertManagerDefinition",
                alias="alias",
                kms_key_arn="kmsKeyArn",
                logging_configuration=aps.CfnWorkspace.LoggingConfigurationProperty(
                    log_group_arn="logGroupArn"
                ),
                query_logging_configuration=aps.CfnWorkspace.QueryLoggingConfigurationProperty(
                    destinations=[aps.CfnWorkspace.LoggingDestinationProperty(
                        cloud_watch_logs=aps.CfnWorkspace.CloudWatchLogDestinationProperty(
                            log_group_arn="logGroupArn"
                        ),
                        filters=aps.CfnWorkspace.LoggingFilterProperty(
                            qsp_threshold=123
                        )
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                workspace_configuration=aps.CfnWorkspace.WorkspaceConfigurationProperty(
                    limits_per_label_sets=[aps.CfnWorkspace.LimitsPerLabelSetProperty(
                        label_set=[aps.CfnWorkspace.LabelProperty(
                            name="name",
                            value="value"
                        )],
                        limits=aps.CfnWorkspace.LimitsPerLabelSetEntryProperty(
                            max_series=123
                        )
                    )],
                    retention_period_in_days=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e95bd874171795b8c6f6104e5fee9fa1d8f50cb6e1edc6d2cc01a77eb0f50a)
            check_type(argname="argument alert_manager_definition", value=alert_manager_definition, expected_type=type_hints["alert_manager_definition"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument query_logging_configuration", value=query_logging_configuration, expected_type=type_hints["query_logging_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument workspace_configuration", value=workspace_configuration, expected_type=type_hints["workspace_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alert_manager_definition is not None:
            self._values["alert_manager_definition"] = alert_manager_definition
        if alias is not None:
            self._values["alias"] = alias
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if query_logging_configuration is not None:
            self._values["query_logging_configuration"] = query_logging_configuration
        if tags is not None:
            self._values["tags"] = tags
        if workspace_configuration is not None:
            self._values["workspace_configuration"] = workspace_configuration

    @builtins.property
    def alert_manager_definition(self) -> typing.Optional[builtins.str]:
        '''The alert manager definition, a YAML configuration for the alert manager in your Amazon Managed Service for Prometheus workspace.

        For details about the alert manager definition, see `Creating an alert manager configuration files <https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-alertmanager-config.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

        The following example shows part of a CloudFormation YAML file with an embedded alert manager definition (following the ``- |-`` ).

        ``Workspace: Type: AWS::APS::Workspace .... Properties: .... AlertManagerDefinition: Fn::Sub: - |- alertmanager_config: | templates: - 'default_template' route: receiver: example-sns receivers: - name: example-sns sns_configs: - topic_arn: 'arn:aws:sns:${AWS::Region}:${AWS::AccountId}:${TopicName}' -``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alertmanagerdefinition
        '''
        result = self._values.get("alert_manager_definition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def alias(self) -> typing.Optional[builtins.str]:
        '''The alias that is assigned to this workspace to help identify it.

        It does not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-alias
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''(optional) The ARN for a customer managed AWS  key to use for encrypting data within your workspace.

        For more information about using your own key in your workspace, see `Encryption at rest <https://docs.aws.amazon.com/prometheus/latest/userguide/encryption-at-rest-Amazon-Service-Prometheus.html>`_ in the *Amazon Managed Service for Prometheus User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LoggingConfigurationProperty"]]:
        '''Contains information about the logging configuration for the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.LoggingConfigurationProperty"]], result)

    @builtins.property
    def query_logging_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.QueryLoggingConfigurationProperty"]]:
        '''The definition of logging configuration in an Amazon Managed Service for Prometheus workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-queryloggingconfiguration
        '''
        result = self._values.get("query_logging_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.QueryLoggingConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The list of tag keys and values that are associated with the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def workspace_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.WorkspaceConfigurationProperty"]]:
        '''Use this structure to define label sets and the ingestion limits for time series that match label sets, and to specify the retention period of the workspace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-aps-workspace.html#cfn-aps-workspace-workspaceconfiguration
        '''
        result = self._values.get("workspace_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkspace.WorkspaceConfigurationProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkspaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAnomalyDetector",
    "CfnAnomalyDetectorProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
    "CfnRuleGroupsNamespace",
    "CfnRuleGroupsNamespaceProps",
    "CfnScraper",
    "CfnScraperProps",
    "CfnWorkspace",
    "CfnWorkspaceProps",
]

publication.publish()

def _typecheckingstub__58b3184629f18780da9f7c9eb2f8acdbdbb5190c9fc3ae41fdbbe34341ba0f26(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.AnomalyDetectorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    workspace: builtins.str,
    evaluation_interval_in_seconds: typing.Optional[jsii.Number] = None,
    labels: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.LabelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    missing_data_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MissingDataActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__114e115249b8e928b79f5b7cb5e3fed1d136c04a5ab6a491f1bfee0b570b9121(
    resource: _IAnomalyDetectorRef_fef2b996,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3babfb32b6d802220d9f08593ab6b583376e7a9fb6a2c4f8866b55e479ece522(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36a9fa3c67c466703717001e2774dacca3fa612b6ec02f8b6361ad6736da0ec7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1edc3473fdf33536207faf87047c2bef23ac4e4aecad53d1e0338308f0e5ab91(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe3aa1b72ccc7677675b2ae76ae8e5e1dfd2146dae8eba7520a981184cdf780d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1394fe6b497d7add7f3c437f746b83234bfd1714418b007d2ca77fcaf2e486fa(
    value: typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.AnomalyDetectorConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51d01d3c64410491a2005087b379e01fe1749ffd4be8e8dae194b7cc8e5e19b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce3cb5189478c72429dee4d6fa1ed9635e537559491f15b775c279a89020cb75(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d15555eb30ee6b4decc1dba71c708714ce1a7f00e658c2ce9c617f35dbea119(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.LabelProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e639ced06e0101ba2e1108f2a5748e988f60e8c6ecadbb32ca0f2dc6162a53e8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnomalyDetector.MissingDataActionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8b42c0f027d8c1c104a6037d9c3752efbfb2ae169c30d63f35dee5bad63b3f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca672630a5e19c23bb68b82c63c873a7687610464d166cef0da5d6cde142082(
    *,
    random_cut_forest: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.RandomCutForestConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3e1cf276ea5a24efc7ebe9d526fad4e86dd66a3f55ea5a0dcb3a617b8d62dff(
    *,
    amount: typing.Optional[jsii.Number] = None,
    ratio: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f784d604d60c49dd5fb567dcfedcd9d16e2ce47ba899589a373c9322818035a(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b8457b72ba87aa14000e26b68e021fa4b19e4e88f3a022910dcd18542039d0(
    *,
    mark_as_anomaly: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    skip: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83993f42a131a948093792cb8cd7b4f710c6b4dffce6b17f386497f1cbe514ea(
    *,
    query: builtins.str,
    ignore_near_expected_from_above: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.IgnoreNearExpectedProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ignore_near_expected_from_below: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.IgnoreNearExpectedProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sample_size: typing.Optional[jsii.Number] = None,
    shingle_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be017a909bcb870b1880c9bb2c099abc51df504e0f9199ca315deb7fa50b9d6b(
    *,
    alias: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.AnomalyDetectorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    workspace: builtins.str,
    evaluation_interval_in_seconds: typing.Optional[jsii.Number] = None,
    labels: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.LabelProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    missing_data_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnomalyDetector.MissingDataActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f89d9ee1d6d400f40f83801fe40dee056ce969e9e0501ca1390285aab7cb82(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: builtins.str,
    workspace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2353f37144a75d2ea8089f4e00cd676ce44deb9aaee1ea5d95d4d42ecf5445b(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fd684bb5425ae9b9586530c2118e55043226673b8740171d3f7c2b1fbd03b3d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c6a584b0420e6cc37e76ad4b000bc6d8f4137f577bf7075b4ec87bab8717d9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d726921aa53fc43f461134d2df5d60edb5d56b4fa67ef6e4e82d305af7b7eba5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f020f5d54f91c35f0b4332b16391ef6561cfc07a46cc5fc1e48d4acdb82a4b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb05747fc90b1776c66fd40ec5d261399f93ac6b367fc973d5df8b912bd30997(
    *,
    policy_document: builtins.str,
    workspace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02d681a4d4a1e9d9052c98f45bf8b21257e825ee8185b30ea4b6f887fc7416b1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data: builtins.str,
    name: builtins.str,
    workspace: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61dec5652442e30c74dbfed7f2f112f1c34f77b348a643313ec2df915c902ada(
    resource: _IRuleGroupsNamespaceRef_7b589be9,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c082b51948289cdbcbe8597af29e57d1b030d4a63972c4107a81d92696db1d1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f066376b2a4b15a103f9a01bca66f252615381ddc55bd5508262712fd03eec2d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__501ad912878791d9cc1a45e52a9642fb0747f4ddf4482708286f9bfde7e036de(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__327e955bc86deb15923357f0f050e077304b8dbbb2c9baba9d84a13c5d7b695d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f3851e1fa5b758763dff1a85515e41a8c57e1b4da81b2e677f003890944957f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f899db17dfa1e1837e2b90cca5f83f23f67ca015116201811ad84d044e9ebe95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9af819e60d52c87c9369e4854d0dfc8d4917db97219839fbc11cf2bdad55659(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ba9f13df78597d09b62adc5501ac56c5fedca3215c115e02cb7e3be9e440366(
    *,
    data: builtins.str,
    name: builtins.str,
    workspace: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4cb1653b22b80f73c5fa4972418519c1d58f8ac033d22184f1b74ee25bf2b0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScrapeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    alias: typing.Optional[builtins.str] = None,
    role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.RoleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scraper_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScraperLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d13ca5c90dffa472e2c1b90166865a8eadf1584a016d1e7bf43dfa45975425b3(
    resource: _IScraperRef_2b17ef67,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6666769e6fd345f7b06db92777e9fba61080e45fac0ba311dcb3ffa01dab3d6(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ef0eaaf8983b897d546f9e872b3a951993e032cd8b5f5f1725e32854f8d096(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d151b530ba64dde831142e12510e32c75c01b169477c6e43bf92c26ab330e2ae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d835d9e17a3614f6837476fe3d3de37c4e38685abfd4cc8e4e49236802dfc0(
    value: typing.Union[_IResolvable_da3f097b, CfnScraper.DestinationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a91c6d3e6031af4c2e1ba10ae98234919eb5f1efa54c12c929f7141e223af9(
    value: typing.Union[_IResolvable_da3f097b, CfnScraper.ScrapeConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4baaa2665d7ddf1c8e51575f5139441f25d102954ee91a2fcbf97644019a8c48(
    value: typing.Union[_IResolvable_da3f097b, CfnScraper.SourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b98e11e4ea8701c0469eb24a036fb1452c2573d264405f3d5237c104fd77a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8492f7c00f66de3309f136730786a3ad81d27f787146130fdb2b6191464e92c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScraper.RoleConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c937c38a5c278540b0a6d9654c4dc0d8dbc46a2f3145fd9275f2a8fd9ce000(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnScraper.ScraperLoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__265ada3fe1d3014c11a5af4d87c8e4b691d29a917e8643b804a82b7c3223573f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02c8f0a43ed30375a3d1b283c2450f310915b0f0fcff6103d168cb18a16bfc4f(
    *,
    workspace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4d1b8a234d9b0461189ac94d16b7043b8e40fc1a62680a811ba8396bc54a5d6(
    *,
    log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c81abd8a9526f73204a9bfa774d69e9b3ec81f7592dafabd756679cc66dcb1e1(
    *,
    options: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9dfeb013903b3b566e12e34ac903da7aaad96412ee8622e798d0f4931b78c31(
    *,
    amp_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.AmpConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84c728405d664f762d3c86aae8f989f77a50273eb74e76dce90e3e0305f06a9(
    *,
    cluster_arn: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86bf03aa28256ae3502c8e0745b810c6f1fe11b530f463788b7c7ffd32d996d1(
    *,
    source_role_arn: typing.Optional[builtins.str] = None,
    target_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61507a1463486662c27c8fec99a5cb181f22e5f346b7bb6d10823ad9b7102b72(
    *,
    configuration_blob: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be259f573540cfe3fb130cbc10c656811dffac0fb6663b27b9f4982549990b6a(
    *,
    type: builtins.str,
    config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ComponentConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea5221003b2ff43404935c67045669a8a84790d807c849eadd6df28ea9b60feb(
    *,
    logging_destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScraperLoggingDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    scraper_components: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScraperComponentProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63a27055fededd95d1bc1fba74349c5f0f37894ed254d1e1ce3d670ded2f515f(
    *,
    cloud_watch_logs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.CloudWatchLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__655e83ac40d7d6fcc3362aa2c25fcfadc0beb5744ef393de105d7d152821a330(
    *,
    eks_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.EksConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.VpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d146d8aa0a745fdc1f1efcc28a958a65b5bbc1a22d0e9673168bcec89aea649(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f302dfc2aa92636b313e32f5d91a0ccfd79ebde0259b977f6291d4c8329455d7(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    scrape_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScrapeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    alias: typing.Optional[builtins.str] = None,
    role_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.RoleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scraper_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnScraper.ScraperLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d7d4de6c2c3c0a6cc1f746f35f29f98344da5c5d59e48a9d1e788ab80e3ef9b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alert_manager_definition: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    query_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.QueryLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    workspace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.WorkspaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3d6e079335cf4fb62650b716c0e1e39e889e44a3c76895cf3db3d9711219145(
    resource: _IWorkspaceRef_d8b2b588,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__490b818275597aad87e1201e93dad0f3f96ca81aa2b2e7254029ea1f42a73cb3(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea1a406920301232e7f737fa791c75b19a41702c2a8761c41de9163390ebcdf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391b593ff5f1b04fd33a43b56be0c4a7f41dd147af44a0bc665b22d97e9640c8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c2399f13a196d4fdd83827148d3942b4231e42e722c32b0c66a56f8425f5d1a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69c703012a200792f370b43791a7b9e6c8ab12b196993de037a82396c6c51b3d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e1bc26d25cdad92f552b6ceb5e8a4ae6d459a5f2737ae032c5a2f069eedf68(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab06dccfc037b2ba3e02b4a3154224a63edcfe3fc06381ff9162c2c33a94b712(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.LoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6591166b06ced49bc35c6390884a7a1c30cea4102022183768ac43e25c00f9fc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.QueryLoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb4e1977fb1f7aad47144a42af408e41c9d01794f3569a614a9ed54effb1c1e5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dc44ff5af32b5cdcf5234cdf89709e32cf5a9217d64f6f2b6625191085cd191(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkspace.WorkspaceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__925c774442f9150193a5d3bfa3fb05562aec6581139c1378b5f09e1c30fb40ee(
    *,
    log_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34eb56a3257d05ed157ec9252590ce797546e9e647035e7f3e639a6629c1cd3(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86191e69da536181f19aaae8e8a81e682e12b975b6edce1319b4d4a8b451cb95(
    *,
    max_series: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d8045fc76bdfc4af5de994e0ebe3331fd81257f1ae53d90373a7ad960b0bca7(
    *,
    label_set: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LabelProperty, typing.Dict[builtins.str, typing.Any]]]]],
    limits: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LimitsPerLabelSetEntryProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa0678eca2188c6c3220d708f7d16298acecab165f03de8b400d1fada6a4b9d9(
    *,
    log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cce5991812152322bf70db3d7cea0d7bb3cda26bb6b0e82d9bd091ef05995168(
    *,
    cloud_watch_logs: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.CloudWatchLogDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    filters: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingFilterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f1710f9a533b3c78aa9735866c9480208fe7ceb912d68581872b145d4c634fd(
    *,
    qsp_threshold: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e9b7a5bb1ecf6d3e6bf0c4d2f497bea98d1fe68b36d502a98c9b336781a58a(
    *,
    destinations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d8bd4b9a39be1594ef4681992e92f89f24816c775c0e0c40e340be13e59392a(
    *,
    limits_per_label_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LimitsPerLabelSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    retention_period_in_days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e95bd874171795b8c6f6104e5fee9fa1d8f50cb6e1edc6d2cc01a77eb0f50a(
    *,
    alert_manager_definition: typing.Optional[builtins.str] = None,
    alias: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    query_logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.QueryLoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    workspace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkspace.WorkspaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
