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
    jsii_type="aws-cdk-lib.interfaces.aws_lookoutmetrics.AlertReference",
    jsii_struct_bases=[],
    name_mapping={"alert_arn": "alertArn"},
)
class AlertReference:
    def __init__(self, *, alert_arn: builtins.str) -> None:
        '''A reference to a Alert resource.

        :param alert_arn: The ARN of the Alert resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lookoutmetrics as interfaces_lookoutmetrics
            
            alert_reference = interfaces_lookoutmetrics.AlertReference(
                alert_arn="alertArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0174632c125fced856edd39640dbde3d250284032b3c662039d9ab935bd4677)
            check_type(argname="argument alert_arn", value=alert_arn, expected_type=type_hints["alert_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alert_arn": alert_arn,
        }

    @builtins.property
    def alert_arn(self) -> builtins.str:
        '''The ARN of the Alert resource.'''
        result = self._values.get("alert_arn")
        assert result is not None, "Required property 'alert_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlertReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lookoutmetrics.AnomalyDetectorReference",
    jsii_struct_bases=[],
    name_mapping={"anomaly_detector_arn": "anomalyDetectorArn"},
)
class AnomalyDetectorReference:
    def __init__(self, *, anomaly_detector_arn: builtins.str) -> None:
        '''A reference to a AnomalyDetector resource.

        :param anomaly_detector_arn: The ARN of the AnomalyDetector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lookoutmetrics as interfaces_lookoutmetrics
            
            anomaly_detector_reference = interfaces_lookoutmetrics.AnomalyDetectorReference(
                anomaly_detector_arn="anomalyDetectorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7b49b95901b1b5a14c5b6e2caedb2b40a4cee9806cb52f9cf1a8ee489c402dc)
            check_type(argname="argument anomaly_detector_arn", value=anomaly_detector_arn, expected_type=type_hints["anomaly_detector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "anomaly_detector_arn": anomaly_detector_arn,
        }

    @builtins.property
    def anomaly_detector_arn(self) -> builtins.str:
        '''The ARN of the AnomalyDetector resource.'''
        result = self._values.get("anomaly_detector_arn")
        assert result is not None, "Required property 'anomaly_detector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnomalyDetectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lookoutmetrics.IAlertRef")
class IAlertRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Alert.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="alertRef")
    def alert_ref(self) -> "AlertReference":
        '''(experimental) A reference to a Alert resource.

        :stability: experimental
        '''
        ...


class _IAlertRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Alert.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lookoutmetrics.IAlertRef"

    @builtins.property
    @jsii.member(jsii_name="alertRef")
    def alert_ref(self) -> "AlertReference":
        '''(experimental) A reference to a Alert resource.

        :stability: experimental
        '''
        return typing.cast("AlertReference", jsii.get(self, "alertRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlertRef).__jsii_proxy_class__ = lambda : _IAlertRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_lookoutmetrics.IAnomalyDetectorRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lookoutmetrics.IAnomalyDetectorRef"

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorRef")
    def anomaly_detector_ref(self) -> "AnomalyDetectorReference":
        '''(experimental) A reference to a AnomalyDetector resource.

        :stability: experimental
        '''
        return typing.cast("AnomalyDetectorReference", jsii.get(self, "anomalyDetectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnomalyDetectorRef).__jsii_proxy_class__ = lambda : _IAnomalyDetectorRefProxy


__all__ = [
    "AlertReference",
    "AnomalyDetectorReference",
    "IAlertRef",
    "IAnomalyDetectorRef",
]

publication.publish()

def _typecheckingstub__b0174632c125fced856edd39640dbde3d250284032b3c662039d9ab935bd4677(
    *,
    alert_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b49b95901b1b5a14c5b6e2caedb2b40a4cee9806cb52f9cf1a8ee489c402dc(
    *,
    anomaly_detector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAlertRef, IAnomalyDetectorRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
