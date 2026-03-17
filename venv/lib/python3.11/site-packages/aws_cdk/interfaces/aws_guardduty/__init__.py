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
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.DetectorReference",
    jsii_struct_bases=[],
    name_mapping={"detector_id": "detectorId"},
)
class DetectorReference:
    def __init__(self, *, detector_id: builtins.str) -> None:
        '''A reference to a Detector resource.

        :param detector_id: The Id of the Detector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            detector_reference = interfaces_guardduty.DetectorReference(
                detector_id="detectorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6848940a92fe8e3f1b7d2a28726632a221ce0a619e2c64e5df120828856586d)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
        }

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The Id of the Detector resource.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DetectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.FilterReference",
    jsii_struct_bases=[],
    name_mapping={"detector_id": "detectorId", "filter_name": "filterName"},
)
class FilterReference:
    def __init__(self, *, detector_id: builtins.str, filter_name: builtins.str) -> None:
        '''A reference to a Filter resource.

        :param detector_id: The DetectorId of the Filter resource.
        :param filter_name: The Name of the Filter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            filter_reference = interfaces_guardduty.FilterReference(
                detector_id="detectorId",
                filter_name="filterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a6a0607715206f75856f58b609f4d0f2ab541e158d64ff80aed19f11b6e800)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "filter_name": filter_name,
        }

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The DetectorId of the Filter resource.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_name(self) -> builtins.str:
        '''The Name of the Filter resource.'''
        result = self._values.get("filter_name")
        assert result is not None, "Required property 'filter_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FilterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IDetectorRef")
class IDetectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Detector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="detectorRef")
    def detector_ref(self) -> "DetectorReference":
        '''(experimental) A reference to a Detector resource.

        :stability: experimental
        '''
        ...


class _IDetectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Detector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.IDetectorRef"

    @builtins.property
    @jsii.member(jsii_name="detectorRef")
    def detector_ref(self) -> "DetectorReference":
        '''(experimental) A reference to a Detector resource.

        :stability: experimental
        '''
        return typing.cast("DetectorReference", jsii.get(self, "detectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDetectorRef).__jsii_proxy_class__ = lambda : _IDetectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IFilterRef")
class IFilterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Filter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="filterRef")
    def filter_ref(self) -> "FilterReference":
        '''(experimental) A reference to a Filter resource.

        :stability: experimental
        '''
        ...


class _IFilterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Filter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.IFilterRef"

    @builtins.property
    @jsii.member(jsii_name="filterRef")
    def filter_ref(self) -> "FilterReference":
        '''(experimental) A reference to a Filter resource.

        :stability: experimental
        '''
        return typing.cast("FilterReference", jsii.get(self, "filterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFilterRef).__jsii_proxy_class__ = lambda : _IFilterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IIPSetRef")
class IIPSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipSetRef")
    def ip_set_ref(self) -> "IPSetReference":
        '''(experimental) A reference to a IPSet resource.

        :stability: experimental
        '''
        ...


class _IIPSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.IIPSetRef"

    @builtins.property
    @jsii.member(jsii_name="ipSetRef")
    def ip_set_ref(self) -> "IPSetReference":
        '''(experimental) A reference to a IPSet resource.

        :stability: experimental
        '''
        return typing.cast("IPSetReference", jsii.get(self, "ipSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPSetRef).__jsii_proxy_class__ = lambda : _IIPSetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IMalwareProtectionPlanRef"
)
class IMalwareProtectionPlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MalwareProtectionPlan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="malwareProtectionPlanRef")
    def malware_protection_plan_ref(self) -> "MalwareProtectionPlanReference":
        '''(experimental) A reference to a MalwareProtectionPlan resource.

        :stability: experimental
        '''
        ...


class _IMalwareProtectionPlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MalwareProtectionPlan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.IMalwareProtectionPlanRef"

    @builtins.property
    @jsii.member(jsii_name="malwareProtectionPlanRef")
    def malware_protection_plan_ref(self) -> "MalwareProtectionPlanReference":
        '''(experimental) A reference to a MalwareProtectionPlan resource.

        :stability: experimental
        '''
        return typing.cast("MalwareProtectionPlanReference", jsii.get(self, "malwareProtectionPlanRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMalwareProtectionPlanRef).__jsii_proxy_class__ = lambda : _IMalwareProtectionPlanRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IMasterRef")
class IMasterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Master.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="masterRef")
    def master_ref(self) -> "MasterReference":
        '''(experimental) A reference to a Master resource.

        :stability: experimental
        '''
        ...


class _IMasterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Master.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.IMasterRef"

    @builtins.property
    @jsii.member(jsii_name="masterRef")
    def master_ref(self) -> "MasterReference":
        '''(experimental) A reference to a Master resource.

        :stability: experimental
        '''
        return typing.cast("MasterReference", jsii.get(self, "masterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMasterRef).__jsii_proxy_class__ = lambda : _IMasterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IMemberRef")
class IMemberRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Member.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="memberRef")
    def member_ref(self) -> "MemberReference":
        '''(experimental) A reference to a Member resource.

        :stability: experimental
        '''
        ...


class _IMemberRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Member.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.IMemberRef"

    @builtins.property
    @jsii.member(jsii_name="memberRef")
    def member_ref(self) -> "MemberReference":
        '''(experimental) A reference to a Member resource.

        :stability: experimental
        '''
        return typing.cast("MemberReference", jsii.get(self, "memberRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMemberRef).__jsii_proxy_class__ = lambda : _IMemberRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IPSetReference",
    jsii_struct_bases=[],
    name_mapping={"detector_id": "detectorId", "ip_set_id": "ipSetId"},
)
class IPSetReference:
    def __init__(self, *, detector_id: builtins.str, ip_set_id: builtins.str) -> None:
        '''A reference to a IPSet resource.

        :param detector_id: The DetectorId of the IPSet resource.
        :param ip_set_id: The Id of the IPSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            i_pSet_reference = {
                "detector_id": "detectorId",
                "ip_set_id": "ipSetId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92295c4c80bd4b1d49687be1b4b124ec6aa6a5aae9d1493831e74ffd7e126607)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument ip_set_id", value=ip_set_id, expected_type=type_hints["ip_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "ip_set_id": ip_set_id,
        }

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The DetectorId of the IPSet resource.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_set_id(self) -> builtins.str:
        '''The Id of the IPSet resource.'''
        result = self._values.get("ip_set_id")
        assert result is not None, "Required property 'ip_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IPublishingDestinationRef"
)
class IPublishingDestinationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PublishingDestination.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="publishingDestinationRef")
    def publishing_destination_ref(self) -> "PublishingDestinationReference":
        '''(experimental) A reference to a PublishingDestination resource.

        :stability: experimental
        '''
        ...


class _IPublishingDestinationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PublishingDestination.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.IPublishingDestinationRef"

    @builtins.property
    @jsii.member(jsii_name="publishingDestinationRef")
    def publishing_destination_ref(self) -> "PublishingDestinationReference":
        '''(experimental) A reference to a PublishingDestination resource.

        :stability: experimental
        '''
        return typing.cast("PublishingDestinationReference", jsii.get(self, "publishingDestinationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublishingDestinationRef).__jsii_proxy_class__ = lambda : _IPublishingDestinationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IThreatEntitySetRef")
class IThreatEntitySetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ThreatEntitySet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="threatEntitySetRef")
    def threat_entity_set_ref(self) -> "ThreatEntitySetReference":
        '''(experimental) A reference to a ThreatEntitySet resource.

        :stability: experimental
        '''
        ...


class _IThreatEntitySetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ThreatEntitySet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.IThreatEntitySetRef"

    @builtins.property
    @jsii.member(jsii_name="threatEntitySetRef")
    def threat_entity_set_ref(self) -> "ThreatEntitySetReference":
        '''(experimental) A reference to a ThreatEntitySet resource.

        :stability: experimental
        '''
        return typing.cast("ThreatEntitySetReference", jsii.get(self, "threatEntitySetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThreatEntitySetRef).__jsii_proxy_class__ = lambda : _IThreatEntitySetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_guardduty.IThreatIntelSetRef")
class IThreatIntelSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ThreatIntelSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="threatIntelSetRef")
    def threat_intel_set_ref(self) -> "ThreatIntelSetReference":
        '''(experimental) A reference to a ThreatIntelSet resource.

        :stability: experimental
        '''
        ...


class _IThreatIntelSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ThreatIntelSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.IThreatIntelSetRef"

    @builtins.property
    @jsii.member(jsii_name="threatIntelSetRef")
    def threat_intel_set_ref(self) -> "ThreatIntelSetReference":
        '''(experimental) A reference to a ThreatIntelSet resource.

        :stability: experimental
        '''
        return typing.cast("ThreatIntelSetReference", jsii.get(self, "threatIntelSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThreatIntelSetRef).__jsii_proxy_class__ = lambda : _IThreatIntelSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_guardduty.ITrustedEntitySetRef")
class ITrustedEntitySetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrustedEntitySet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trustedEntitySetRef")
    def trusted_entity_set_ref(self) -> "TrustedEntitySetReference":
        '''(experimental) A reference to a TrustedEntitySet resource.

        :stability: experimental
        '''
        ...


class _ITrustedEntitySetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrustedEntitySet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_guardduty.ITrustedEntitySetRef"

    @builtins.property
    @jsii.member(jsii_name="trustedEntitySetRef")
    def trusted_entity_set_ref(self) -> "TrustedEntitySetReference":
        '''(experimental) A reference to a TrustedEntitySet resource.

        :stability: experimental
        '''
        return typing.cast("TrustedEntitySetReference", jsii.get(self, "trustedEntitySetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrustedEntitySetRef).__jsii_proxy_class__ = lambda : _ITrustedEntitySetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.MalwareProtectionPlanReference",
    jsii_struct_bases=[],
    name_mapping={
        "malware_protection_plan_arn": "malwareProtectionPlanArn",
        "malware_protection_plan_id": "malwareProtectionPlanId",
    },
)
class MalwareProtectionPlanReference:
    def __init__(
        self,
        *,
        malware_protection_plan_arn: builtins.str,
        malware_protection_plan_id: builtins.str,
    ) -> None:
        '''A reference to a MalwareProtectionPlan resource.

        :param malware_protection_plan_arn: The ARN of the MalwareProtectionPlan resource.
        :param malware_protection_plan_id: The MalwareProtectionPlanId of the MalwareProtectionPlan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            malware_protection_plan_reference = interfaces_guardduty.MalwareProtectionPlanReference(
                malware_protection_plan_arn="malwareProtectionPlanArn",
                malware_protection_plan_id="malwareProtectionPlanId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf739c1a65de202429a81c2fe429c52e9f56cca3f91ae8a0289abff4cc071e18)
            check_type(argname="argument malware_protection_plan_arn", value=malware_protection_plan_arn, expected_type=type_hints["malware_protection_plan_arn"])
            check_type(argname="argument malware_protection_plan_id", value=malware_protection_plan_id, expected_type=type_hints["malware_protection_plan_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "malware_protection_plan_arn": malware_protection_plan_arn,
            "malware_protection_plan_id": malware_protection_plan_id,
        }

    @builtins.property
    def malware_protection_plan_arn(self) -> builtins.str:
        '''The ARN of the MalwareProtectionPlan resource.'''
        result = self._values.get("malware_protection_plan_arn")
        assert result is not None, "Required property 'malware_protection_plan_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def malware_protection_plan_id(self) -> builtins.str:
        '''The MalwareProtectionPlanId of the MalwareProtectionPlan resource.'''
        result = self._values.get("malware_protection_plan_id")
        assert result is not None, "Required property 'malware_protection_plan_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MalwareProtectionPlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.MasterReference",
    jsii_struct_bases=[],
    name_mapping={"detector_id": "detectorId", "master_id": "masterId"},
)
class MasterReference:
    def __init__(self, *, detector_id: builtins.str, master_id: builtins.str) -> None:
        '''A reference to a Master resource.

        :param detector_id: The DetectorId of the Master resource.
        :param master_id: The MasterId of the Master resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            master_reference = interfaces_guardduty.MasterReference(
                detector_id="detectorId",
                master_id="masterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8925c87309782f1d27c270c8ef60db4201e6d039d173f7a922e65624c31e698d)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument master_id", value=master_id, expected_type=type_hints["master_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "master_id": master_id,
        }

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The DetectorId of the Master resource.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def master_id(self) -> builtins.str:
        '''The MasterId of the Master resource.'''
        result = self._values.get("master_id")
        assert result is not None, "Required property 'master_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MasterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.MemberReference",
    jsii_struct_bases=[],
    name_mapping={"detector_id": "detectorId", "member_id": "memberId"},
)
class MemberReference:
    def __init__(self, *, detector_id: builtins.str, member_id: builtins.str) -> None:
        '''A reference to a Member resource.

        :param detector_id: The DetectorId of the Member resource.
        :param member_id: The MemberId of the Member resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            member_reference = interfaces_guardduty.MemberReference(
                detector_id="detectorId",
                member_id="memberId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe3803ae846d896367d0ee685365bdf27278225aabe845f4e5c38236a035fb2c)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "member_id": member_id,
        }

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The DetectorId of the Member resource.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_id(self) -> builtins.str:
        '''The MemberId of the Member resource.'''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MemberReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.PublishingDestinationReference",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "publishing_destination_id": "publishingDestinationId",
    },
)
class PublishingDestinationReference:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        publishing_destination_id: builtins.str,
    ) -> None:
        '''A reference to a PublishingDestination resource.

        :param detector_id: The DetectorId of the PublishingDestination resource.
        :param publishing_destination_id: The Id of the PublishingDestination resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            publishing_destination_reference = interfaces_guardduty.PublishingDestinationReference(
                detector_id="detectorId",
                publishing_destination_id="publishingDestinationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1954f15495f4cad5d31e277ccfc284aa7f40f23cb69b85bdde91bf1eaac051c2)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument publishing_destination_id", value=publishing_destination_id, expected_type=type_hints["publishing_destination_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "publishing_destination_id": publishing_destination_id,
        }

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The DetectorId of the PublishingDestination resource.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publishing_destination_id(self) -> builtins.str:
        '''The Id of the PublishingDestination resource.'''
        result = self._values.get("publishing_destination_id")
        assert result is not None, "Required property 'publishing_destination_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublishingDestinationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.ThreatEntitySetReference",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "threat_entity_set_id": "threatEntitySetId",
    },
)
class ThreatEntitySetReference:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        threat_entity_set_id: builtins.str,
    ) -> None:
        '''A reference to a ThreatEntitySet resource.

        :param detector_id: The DetectorId of the ThreatEntitySet resource.
        :param threat_entity_set_id: The Id of the ThreatEntitySet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            threat_entity_set_reference = interfaces_guardduty.ThreatEntitySetReference(
                detector_id="detectorId",
                threat_entity_set_id="threatEntitySetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aae63dd921bfcf536f90c2c782a441d5c2789e4a69148a93c1b8ba5394eb4557)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument threat_entity_set_id", value=threat_entity_set_id, expected_type=type_hints["threat_entity_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "threat_entity_set_id": threat_entity_set_id,
        }

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The DetectorId of the ThreatEntitySet resource.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threat_entity_set_id(self) -> builtins.str:
        '''The Id of the ThreatEntitySet resource.'''
        result = self._values.get("threat_entity_set_id")
        assert result is not None, "Required property 'threat_entity_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThreatEntitySetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.ThreatIntelSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "threat_intel_set_id": "threatIntelSetId",
    },
)
class ThreatIntelSetReference:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        threat_intel_set_id: builtins.str,
    ) -> None:
        '''A reference to a ThreatIntelSet resource.

        :param detector_id: The DetectorId of the ThreatIntelSet resource.
        :param threat_intel_set_id: The Id of the ThreatIntelSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            threat_intel_set_reference = interfaces_guardduty.ThreatIntelSetReference(
                detector_id="detectorId",
                threat_intel_set_id="threatIntelSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece76fe64cc90a7d7106df815cf9342cfa0797da775897e9160e724be24c64b4)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument threat_intel_set_id", value=threat_intel_set_id, expected_type=type_hints["threat_intel_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "threat_intel_set_id": threat_intel_set_id,
        }

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The DetectorId of the ThreatIntelSet resource.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def threat_intel_set_id(self) -> builtins.str:
        '''The Id of the ThreatIntelSet resource.'''
        result = self._values.get("threat_intel_set_id")
        assert result is not None, "Required property 'threat_intel_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThreatIntelSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_guardduty.TrustedEntitySetReference",
    jsii_struct_bases=[],
    name_mapping={
        "detector_id": "detectorId",
        "trusted_entity_set_id": "trustedEntitySetId",
    },
)
class TrustedEntitySetReference:
    def __init__(
        self,
        *,
        detector_id: builtins.str,
        trusted_entity_set_id: builtins.str,
    ) -> None:
        '''A reference to a TrustedEntitySet resource.

        :param detector_id: The DetectorId of the TrustedEntitySet resource.
        :param trusted_entity_set_id: The Id of the TrustedEntitySet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_guardduty as interfaces_guardduty
            
            trusted_entity_set_reference = interfaces_guardduty.TrustedEntitySetReference(
                detector_id="detectorId",
                trusted_entity_set_id="trustedEntitySetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__092bff2af5d8810173beb35221a3505f0dcd23bb88ae6dc1a71baf99b6e9476b)
            check_type(argname="argument detector_id", value=detector_id, expected_type=type_hints["detector_id"])
            check_type(argname="argument trusted_entity_set_id", value=trusted_entity_set_id, expected_type=type_hints["trusted_entity_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_id": detector_id,
            "trusted_entity_set_id": trusted_entity_set_id,
        }

    @builtins.property
    def detector_id(self) -> builtins.str:
        '''The DetectorId of the TrustedEntitySet resource.'''
        result = self._values.get("detector_id")
        assert result is not None, "Required property 'detector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trusted_entity_set_id(self) -> builtins.str:
        '''The Id of the TrustedEntitySet resource.'''
        result = self._values.get("trusted_entity_set_id")
        assert result is not None, "Required property 'trusted_entity_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrustedEntitySetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DetectorReference",
    "FilterReference",
    "IDetectorRef",
    "IFilterRef",
    "IIPSetRef",
    "IMalwareProtectionPlanRef",
    "IMasterRef",
    "IMemberRef",
    "IPSetReference",
    "IPublishingDestinationRef",
    "IThreatEntitySetRef",
    "IThreatIntelSetRef",
    "ITrustedEntitySetRef",
    "MalwareProtectionPlanReference",
    "MasterReference",
    "MemberReference",
    "PublishingDestinationReference",
    "ThreatEntitySetReference",
    "ThreatIntelSetReference",
    "TrustedEntitySetReference",
]

publication.publish()

def _typecheckingstub__a6848940a92fe8e3f1b7d2a28726632a221ce0a619e2c64e5df120828856586d(
    *,
    detector_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a6a0607715206f75856f58b609f4d0f2ab541e158d64ff80aed19f11b6e800(
    *,
    detector_id: builtins.str,
    filter_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92295c4c80bd4b1d49687be1b4b124ec6aa6a5aae9d1493831e74ffd7e126607(
    *,
    detector_id: builtins.str,
    ip_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf739c1a65de202429a81c2fe429c52e9f56cca3f91ae8a0289abff4cc071e18(
    *,
    malware_protection_plan_arn: builtins.str,
    malware_protection_plan_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8925c87309782f1d27c270c8ef60db4201e6d039d173f7a922e65624c31e698d(
    *,
    detector_id: builtins.str,
    master_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe3803ae846d896367d0ee685365bdf27278225aabe845f4e5c38236a035fb2c(
    *,
    detector_id: builtins.str,
    member_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1954f15495f4cad5d31e277ccfc284aa7f40f23cb69b85bdde91bf1eaac051c2(
    *,
    detector_id: builtins.str,
    publishing_destination_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aae63dd921bfcf536f90c2c782a441d5c2789e4a69148a93c1b8ba5394eb4557(
    *,
    detector_id: builtins.str,
    threat_entity_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece76fe64cc90a7d7106df815cf9342cfa0797da775897e9160e724be24c64b4(
    *,
    detector_id: builtins.str,
    threat_intel_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092bff2af5d8810173beb35221a3505f0dcd23bb88ae6dc1a71baf99b6e9476b(
    *,
    detector_id: builtins.str,
    trusted_entity_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDetectorRef, IFilterRef, IIPSetRef, IMalwareProtectionPlanRef, IMasterRef, IMemberRef, IPublishingDestinationRef, IThreatEntitySetRef, IThreatIntelSetRef, ITrustedEntitySetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
