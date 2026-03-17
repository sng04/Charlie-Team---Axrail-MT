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
    jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.AlarmMuteRuleReference",
    jsii_struct_bases=[],
    name_mapping={"alarm_mute_rule_arn": "alarmMuteRuleArn"},
)
class AlarmMuteRuleReference:
    def __init__(self, *, alarm_mute_rule_arn: builtins.str) -> None:
        '''A reference to a AlarmMuteRule resource.

        :param alarm_mute_rule_arn: The Arn of the AlarmMuteRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudwatch as interfaces_cloudwatch
            
            alarm_mute_rule_reference = interfaces_cloudwatch.AlarmMuteRuleReference(
                alarm_mute_rule_arn="alarmMuteRuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a96a894c3e3ce3a85ad1fdae64962a99174f720bb052efd2e1096d6fde57c59)
            check_type(argname="argument alarm_mute_rule_arn", value=alarm_mute_rule_arn, expected_type=type_hints["alarm_mute_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_mute_rule_arn": alarm_mute_rule_arn,
        }

    @builtins.property
    def alarm_mute_rule_arn(self) -> builtins.str:
        '''The Arn of the AlarmMuteRule resource.'''
        result = self._values.get("alarm_mute_rule_arn")
        assert result is not None, "Required property 'alarm_mute_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmMuteRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.AlarmReference",
    jsii_struct_bases=[],
    name_mapping={"alarm_arn": "alarmArn", "alarm_name": "alarmName"},
)
class AlarmReference:
    def __init__(self, *, alarm_arn: builtins.str, alarm_name: builtins.str) -> None:
        '''A reference to a Alarm resource.

        :param alarm_arn: The ARN of the Alarm resource.
        :param alarm_name: The AlarmName of the Alarm resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudwatch as interfaces_cloudwatch
            
            alarm_reference = interfaces_cloudwatch.AlarmReference(
                alarm_arn="alarmArn",
                alarm_name="alarmName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a217ba13c11edc5835368167ddbaa01cba65af05c8b67482c46acd94b5fc5758)
            check_type(argname="argument alarm_arn", value=alarm_arn, expected_type=type_hints["alarm_arn"])
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_arn": alarm_arn,
            "alarm_name": alarm_name,
        }

    @builtins.property
    def alarm_arn(self) -> builtins.str:
        '''The ARN of the Alarm resource.'''
        result = self._values.get("alarm_arn")
        assert result is not None, "Required property 'alarm_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarm_name(self) -> builtins.str:
        '''The AlarmName of the Alarm resource.'''
        result = self._values.get("alarm_name")
        assert result is not None, "Required property 'alarm_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.AnomalyDetectorReference",
    jsii_struct_bases=[],
    name_mapping={"anomaly_detector_id": "anomalyDetectorId"},
)
class AnomalyDetectorReference:
    def __init__(self, *, anomaly_detector_id: builtins.str) -> None:
        '''A reference to a AnomalyDetector resource.

        :param anomaly_detector_id: The Id of the AnomalyDetector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudwatch as interfaces_cloudwatch
            
            anomaly_detector_reference = interfaces_cloudwatch.AnomalyDetectorReference(
                anomaly_detector_id="anomalyDetectorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08bbcba6a5b09a6a3e92c9b464ff62ea24aa01e023d7db746485a8f8bc579a4d)
            check_type(argname="argument anomaly_detector_id", value=anomaly_detector_id, expected_type=type_hints["anomaly_detector_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "anomaly_detector_id": anomaly_detector_id,
        }

    @builtins.property
    def anomaly_detector_id(self) -> builtins.str:
        '''The Id of the AnomalyDetector resource.'''
        result = self._values.get("anomaly_detector_id")
        assert result is not None, "Required property 'anomaly_detector_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnomalyDetectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.CompositeAlarmReference",
    jsii_struct_bases=[],
    name_mapping={
        "alarm_name": "alarmName",
        "composite_alarm_arn": "compositeAlarmArn",
    },
)
class CompositeAlarmReference:
    def __init__(
        self,
        *,
        alarm_name: builtins.str,
        composite_alarm_arn: builtins.str,
    ) -> None:
        '''A reference to a CompositeAlarm resource.

        :param alarm_name: The AlarmName of the CompositeAlarm resource.
        :param composite_alarm_arn: The ARN of the CompositeAlarm resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudwatch as interfaces_cloudwatch
            
            composite_alarm_reference = interfaces_cloudwatch.CompositeAlarmReference(
                alarm_name="alarmName",
                composite_alarm_arn="compositeAlarmArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1042889d771e7e4d3b68678612b0204f4e8b84ad00f0672fd7f96a4d3095e8e8)
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
            check_type(argname="argument composite_alarm_arn", value=composite_alarm_arn, expected_type=type_hints["composite_alarm_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_name": alarm_name,
            "composite_alarm_arn": composite_alarm_arn,
        }

    @builtins.property
    def alarm_name(self) -> builtins.str:
        '''The AlarmName of the CompositeAlarm resource.'''
        result = self._values.get("alarm_name")
        assert result is not None, "Required property 'alarm_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def composite_alarm_arn(self) -> builtins.str:
        '''The ARN of the CompositeAlarm resource.'''
        result = self._values.get("composite_alarm_arn")
        assert result is not None, "Required property 'composite_alarm_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CompositeAlarmReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.DashboardReference",
    jsii_struct_bases=[],
    name_mapping={"dashboard_name": "dashboardName"},
)
class DashboardReference:
    def __init__(self, *, dashboard_name: builtins.str) -> None:
        '''A reference to a Dashboard resource.

        :param dashboard_name: The DashboardName of the Dashboard resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudwatch as interfaces_cloudwatch
            
            dashboard_reference = interfaces_cloudwatch.DashboardReference(
                dashboard_name="dashboardName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8a69e4049e357c44415bff967a5b2a7dd2e87def21cda4b468303b1a5be2771)
            check_type(argname="argument dashboard_name", value=dashboard_name, expected_type=type_hints["dashboard_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dashboard_name": dashboard_name,
        }

    @builtins.property
    def dashboard_name(self) -> builtins.str:
        '''The DashboardName of the Dashboard resource.'''
        result = self._values.get("dashboard_name")
        assert result is not None, "Required property 'dashboard_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.IAlarmMuteRuleRef")
class IAlarmMuteRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AlarmMuteRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="alarmMuteRuleRef")
    def alarm_mute_rule_ref(self) -> "AlarmMuteRuleReference":
        '''(experimental) A reference to a AlarmMuteRule resource.

        :stability: experimental
        '''
        ...


class _IAlarmMuteRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AlarmMuteRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudwatch.IAlarmMuteRuleRef"

    @builtins.property
    @jsii.member(jsii_name="alarmMuteRuleRef")
    def alarm_mute_rule_ref(self) -> "AlarmMuteRuleReference":
        '''(experimental) A reference to a AlarmMuteRule resource.

        :stability: experimental
        '''
        return typing.cast("AlarmMuteRuleReference", jsii.get(self, "alarmMuteRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarmMuteRuleRef).__jsii_proxy_class__ = lambda : _IAlarmMuteRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.IAlarmRef")
class IAlarmRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Alarm.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="alarmRef")
    def alarm_ref(self) -> "AlarmReference":
        '''(experimental) A reference to a Alarm resource.

        :stability: experimental
        '''
        ...


class _IAlarmRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Alarm.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudwatch.IAlarmRef"

    @builtins.property
    @jsii.member(jsii_name="alarmRef")
    def alarm_ref(self) -> "AlarmReference":
        '''(experimental) A reference to a Alarm resource.

        :stability: experimental
        '''
        return typing.cast("AlarmReference", jsii.get(self, "alarmRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarmRef).__jsii_proxy_class__ = lambda : _IAlarmRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.IAnomalyDetectorRef")
class IAnomalyDetectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AnomalyDetector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorRef")
    def anomaly_detector_ref(self) -> "AnomalyDetectorReference":
        '''(experimental) A reference to a AnomalyDetector resource.

        :stability: experimental
        '''
        ...


class _IAnomalyDetectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AnomalyDetector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudwatch.IAnomalyDetectorRef"

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorRef")
    def anomaly_detector_ref(self) -> "AnomalyDetectorReference":
        '''(experimental) A reference to a AnomalyDetector resource.

        :stability: experimental
        '''
        return typing.cast("AnomalyDetectorReference", jsii.get(self, "anomalyDetectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnomalyDetectorRef).__jsii_proxy_class__ = lambda : _IAnomalyDetectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.ICompositeAlarmRef")
class ICompositeAlarmRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CompositeAlarm.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="compositeAlarmRef")
    def composite_alarm_ref(self) -> "CompositeAlarmReference":
        '''(experimental) A reference to a CompositeAlarm resource.

        :stability: experimental
        '''
        ...


class _ICompositeAlarmRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CompositeAlarm.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudwatch.ICompositeAlarmRef"

    @builtins.property
    @jsii.member(jsii_name="compositeAlarmRef")
    def composite_alarm_ref(self) -> "CompositeAlarmReference":
        '''(experimental) A reference to a CompositeAlarm resource.

        :stability: experimental
        '''
        return typing.cast("CompositeAlarmReference", jsii.get(self, "compositeAlarmRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICompositeAlarmRef).__jsii_proxy_class__ = lambda : _ICompositeAlarmRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.IDashboardRef")
class IDashboardRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Dashboard.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dashboardRef")
    def dashboard_ref(self) -> "DashboardReference":
        '''(experimental) A reference to a Dashboard resource.

        :stability: experimental
        '''
        ...


class _IDashboardRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Dashboard.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudwatch.IDashboardRef"

    @builtins.property
    @jsii.member(jsii_name="dashboardRef")
    def dashboard_ref(self) -> "DashboardReference":
        '''(experimental) A reference to a Dashboard resource.

        :stability: experimental
        '''
        return typing.cast("DashboardReference", jsii.get(self, "dashboardRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDashboardRef).__jsii_proxy_class__ = lambda : _IDashboardRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.IInsightRuleRef")
class IInsightRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InsightRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="insightRuleRef")
    def insight_rule_ref(self) -> "InsightRuleReference":
        '''(experimental) A reference to a InsightRule resource.

        :stability: experimental
        '''
        ...


class _IInsightRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InsightRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudwatch.IInsightRuleRef"

    @builtins.property
    @jsii.member(jsii_name="insightRuleRef")
    def insight_rule_ref(self) -> "InsightRuleReference":
        '''(experimental) A reference to a InsightRule resource.

        :stability: experimental
        '''
        return typing.cast("InsightRuleReference", jsii.get(self, "insightRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInsightRuleRef).__jsii_proxy_class__ = lambda : _IInsightRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.IMetricStreamRef")
class IMetricStreamRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MetricStream.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="metricStreamRef")
    def metric_stream_ref(self) -> "MetricStreamReference":
        '''(experimental) A reference to a MetricStream resource.

        :stability: experimental
        '''
        ...


class _IMetricStreamRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MetricStream.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudwatch.IMetricStreamRef"

    @builtins.property
    @jsii.member(jsii_name="metricStreamRef")
    def metric_stream_ref(self) -> "MetricStreamReference":
        '''(experimental) A reference to a MetricStream resource.

        :stability: experimental
        '''
        return typing.cast("MetricStreamReference", jsii.get(self, "metricStreamRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMetricStreamRef).__jsii_proxy_class__ = lambda : _IMetricStreamRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.InsightRuleReference",
    jsii_struct_bases=[],
    name_mapping={"insight_rule_arn": "insightRuleArn"},
)
class InsightRuleReference:
    def __init__(self, *, insight_rule_arn: builtins.str) -> None:
        '''A reference to a InsightRule resource.

        :param insight_rule_arn: The Arn of the InsightRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudwatch as interfaces_cloudwatch
            
            insight_rule_reference = interfaces_cloudwatch.InsightRuleReference(
                insight_rule_arn="insightRuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c9eaae14b7b5fd4caa9ee9685f1e4ff2ed87f7d35cc2260e8e46c3852afb6be)
            check_type(argname="argument insight_rule_arn", value=insight_rule_arn, expected_type=type_hints["insight_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "insight_rule_arn": insight_rule_arn,
        }

    @builtins.property
    def insight_rule_arn(self) -> builtins.str:
        '''The Arn of the InsightRule resource.'''
        result = self._values.get("insight_rule_arn")
        assert result is not None, "Required property 'insight_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InsightRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudwatch.MetricStreamReference",
    jsii_struct_bases=[],
    name_mapping={
        "metric_stream_arn": "metricStreamArn",
        "metric_stream_name": "metricStreamName",
    },
)
class MetricStreamReference:
    def __init__(
        self,
        *,
        metric_stream_arn: builtins.str,
        metric_stream_name: builtins.str,
    ) -> None:
        '''A reference to a MetricStream resource.

        :param metric_stream_arn: The ARN of the MetricStream resource.
        :param metric_stream_name: The Name of the MetricStream resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudwatch as interfaces_cloudwatch
            
            metric_stream_reference = interfaces_cloudwatch.MetricStreamReference(
                metric_stream_arn="metricStreamArn",
                metric_stream_name="metricStreamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd4b5eb67c7a5b2c989d807371acca126080a0b48d263d4d19312a05a27ad715)
            check_type(argname="argument metric_stream_arn", value=metric_stream_arn, expected_type=type_hints["metric_stream_arn"])
            check_type(argname="argument metric_stream_name", value=metric_stream_name, expected_type=type_hints["metric_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_stream_arn": metric_stream_arn,
            "metric_stream_name": metric_stream_name,
        }

    @builtins.property
    def metric_stream_arn(self) -> builtins.str:
        '''The ARN of the MetricStream resource.'''
        result = self._values.get("metric_stream_arn")
        assert result is not None, "Required property 'metric_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric_stream_name(self) -> builtins.str:
        '''The Name of the MetricStream resource.'''
        result = self._values.get("metric_stream_name")
        assert result is not None, "Required property 'metric_stream_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricStreamReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AlarmMuteRuleReference",
    "AlarmReference",
    "AnomalyDetectorReference",
    "CompositeAlarmReference",
    "DashboardReference",
    "IAlarmMuteRuleRef",
    "IAlarmRef",
    "IAnomalyDetectorRef",
    "ICompositeAlarmRef",
    "IDashboardRef",
    "IInsightRuleRef",
    "IMetricStreamRef",
    "InsightRuleReference",
    "MetricStreamReference",
]

publication.publish()

def _typecheckingstub__3a96a894c3e3ce3a85ad1fdae64962a99174f720bb052efd2e1096d6fde57c59(
    *,
    alarm_mute_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a217ba13c11edc5835368167ddbaa01cba65af05c8b67482c46acd94b5fc5758(
    *,
    alarm_arn: builtins.str,
    alarm_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bbcba6a5b09a6a3e92c9b464ff62ea24aa01e023d7db746485a8f8bc579a4d(
    *,
    anomaly_detector_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1042889d771e7e4d3b68678612b0204f4e8b84ad00f0672fd7f96a4d3095e8e8(
    *,
    alarm_name: builtins.str,
    composite_alarm_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8a69e4049e357c44415bff967a5b2a7dd2e87def21cda4b468303b1a5be2771(
    *,
    dashboard_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c9eaae14b7b5fd4caa9ee9685f1e4ff2ed87f7d35cc2260e8e46c3852afb6be(
    *,
    insight_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd4b5eb67c7a5b2c989d807371acca126080a0b48d263d4d19312a05a27ad715(
    *,
    metric_stream_arn: builtins.str,
    metric_stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAlarmMuteRuleRef, IAlarmRef, IAnomalyDetectorRef, ICompositeAlarmRef, IDashboardRef, IInsightRuleRef, IMetricStreamRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
