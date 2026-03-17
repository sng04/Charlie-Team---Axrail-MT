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
    jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.CampaignReference",
    jsii_struct_bases=[],
    name_mapping={"campaign_arn": "campaignArn", "campaign_name": "campaignName"},
)
class CampaignReference:
    def __init__(
        self,
        *,
        campaign_arn: builtins.str,
        campaign_name: builtins.str,
    ) -> None:
        '''A reference to a Campaign resource.

        :param campaign_arn: The ARN of the Campaign resource.
        :param campaign_name: The Name of the Campaign resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotfleetwise as interfaces_iotfleetwise
            
            campaign_reference = interfaces_iotfleetwise.CampaignReference(
                campaign_arn="campaignArn",
                campaign_name="campaignName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abc62ce3a2eacc41973eb932cb914110df6dc4f94aa69bbc965f10b97056a756)
            check_type(argname="argument campaign_arn", value=campaign_arn, expected_type=type_hints["campaign_arn"])
            check_type(argname="argument campaign_name", value=campaign_name, expected_type=type_hints["campaign_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "campaign_arn": campaign_arn,
            "campaign_name": campaign_name,
        }

    @builtins.property
    def campaign_arn(self) -> builtins.str:
        '''The ARN of the Campaign resource.'''
        result = self._values.get("campaign_arn")
        assert result is not None, "Required property 'campaign_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def campaign_name(self) -> builtins.str:
        '''The Name of the Campaign resource.'''
        result = self._values.get("campaign_name")
        assert result is not None, "Required property 'campaign_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CampaignReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.DecoderManifestReference",
    jsii_struct_bases=[],
    name_mapping={
        "decoder_manifest_arn": "decoderManifestArn",
        "decoder_manifest_name": "decoderManifestName",
    },
)
class DecoderManifestReference:
    def __init__(
        self,
        *,
        decoder_manifest_arn: builtins.str,
        decoder_manifest_name: builtins.str,
    ) -> None:
        '''A reference to a DecoderManifest resource.

        :param decoder_manifest_arn: The ARN of the DecoderManifest resource.
        :param decoder_manifest_name: The Name of the DecoderManifest resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotfleetwise as interfaces_iotfleetwise
            
            decoder_manifest_reference = interfaces_iotfleetwise.DecoderManifestReference(
                decoder_manifest_arn="decoderManifestArn",
                decoder_manifest_name="decoderManifestName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8b332dc87c650b4957bb4734c63a524f7479215b9b9ebea23f3040cb605f988)
            check_type(argname="argument decoder_manifest_arn", value=decoder_manifest_arn, expected_type=type_hints["decoder_manifest_arn"])
            check_type(argname="argument decoder_manifest_name", value=decoder_manifest_name, expected_type=type_hints["decoder_manifest_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "decoder_manifest_arn": decoder_manifest_arn,
            "decoder_manifest_name": decoder_manifest_name,
        }

    @builtins.property
    def decoder_manifest_arn(self) -> builtins.str:
        '''The ARN of the DecoderManifest resource.'''
        result = self._values.get("decoder_manifest_arn")
        assert result is not None, "Required property 'decoder_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def decoder_manifest_name(self) -> builtins.str:
        '''The Name of the DecoderManifest resource.'''
        result = self._values.get("decoder_manifest_name")
        assert result is not None, "Required property 'decoder_manifest_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DecoderManifestReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.FleetReference",
    jsii_struct_bases=[],
    name_mapping={"fleet_arn": "fleetArn", "fleet_id": "fleetId"},
)
class FleetReference:
    def __init__(self, *, fleet_arn: builtins.str, fleet_id: builtins.str) -> None:
        '''A reference to a Fleet resource.

        :param fleet_arn: The ARN of the Fleet resource.
        :param fleet_id: The Id of the Fleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotfleetwise as interfaces_iotfleetwise
            
            fleet_reference = interfaces_iotfleetwise.FleetReference(
                fleet_arn="fleetArn",
                fleet_id="fleetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e0609989cc7ef5b004c59e00dddcd2a8df28f027b02b4a7e0375d119d6cb1f6)
            check_type(argname="argument fleet_arn", value=fleet_arn, expected_type=type_hints["fleet_arn"])
            check_type(argname="argument fleet_id", value=fleet_id, expected_type=type_hints["fleet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_arn": fleet_arn,
            "fleet_id": fleet_id,
        }

    @builtins.property
    def fleet_arn(self) -> builtins.str:
        '''The ARN of the Fleet resource.'''
        result = self._values.get("fleet_arn")
        assert result is not None, "Required property 'fleet_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fleet_id(self) -> builtins.str:
        '''The Id of the Fleet resource.'''
        result = self._values.get("fleet_id")
        assert result is not None, "Required property 'fleet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.ICampaignRef")
class ICampaignRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Campaign.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="campaignRef")
    def campaign_ref(self) -> "CampaignReference":
        '''(experimental) A reference to a Campaign resource.

        :stability: experimental
        '''
        ...


class _ICampaignRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Campaign.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotfleetwise.ICampaignRef"

    @builtins.property
    @jsii.member(jsii_name="campaignRef")
    def campaign_ref(self) -> "CampaignReference":
        '''(experimental) A reference to a Campaign resource.

        :stability: experimental
        '''
        return typing.cast("CampaignReference", jsii.get(self, "campaignRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICampaignRef).__jsii_proxy_class__ = lambda : _ICampaignRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.IDecoderManifestRef"
)
class IDecoderManifestRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DecoderManifest.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="decoderManifestRef")
    def decoder_manifest_ref(self) -> "DecoderManifestReference":
        '''(experimental) A reference to a DecoderManifest resource.

        :stability: experimental
        '''
        ...


class _IDecoderManifestRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DecoderManifest.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotfleetwise.IDecoderManifestRef"

    @builtins.property
    @jsii.member(jsii_name="decoderManifestRef")
    def decoder_manifest_ref(self) -> "DecoderManifestReference":
        '''(experimental) A reference to a DecoderManifest resource.

        :stability: experimental
        '''
        return typing.cast("DecoderManifestReference", jsii.get(self, "decoderManifestRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDecoderManifestRef).__jsii_proxy_class__ = lambda : _IDecoderManifestRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.IFleetRef")
class IFleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        ...


class _IFleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotfleetwise.IFleetRef"

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        return typing.cast("FleetReference", jsii.get(self, "fleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFleetRef).__jsii_proxy_class__ = lambda : _IFleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.IModelManifestRef")
class IModelManifestRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ModelManifest.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelManifestRef")
    def model_manifest_ref(self) -> "ModelManifestReference":
        '''(experimental) A reference to a ModelManifest resource.

        :stability: experimental
        '''
        ...


class _IModelManifestRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ModelManifest.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotfleetwise.IModelManifestRef"

    @builtins.property
    @jsii.member(jsii_name="modelManifestRef")
    def model_manifest_ref(self) -> "ModelManifestReference":
        '''(experimental) A reference to a ModelManifest resource.

        :stability: experimental
        '''
        return typing.cast("ModelManifestReference", jsii.get(self, "modelManifestRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelManifestRef).__jsii_proxy_class__ = lambda : _IModelManifestRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.ISignalCatalogRef")
class ISignalCatalogRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SignalCatalog.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="signalCatalogRef")
    def signal_catalog_ref(self) -> "SignalCatalogReference":
        '''(experimental) A reference to a SignalCatalog resource.

        :stability: experimental
        '''
        ...


class _ISignalCatalogRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SignalCatalog.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotfleetwise.ISignalCatalogRef"

    @builtins.property
    @jsii.member(jsii_name="signalCatalogRef")
    def signal_catalog_ref(self) -> "SignalCatalogReference":
        '''(experimental) A reference to a SignalCatalog resource.

        :stability: experimental
        '''
        return typing.cast("SignalCatalogReference", jsii.get(self, "signalCatalogRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISignalCatalogRef).__jsii_proxy_class__ = lambda : _ISignalCatalogRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.IStateTemplateRef")
class IStateTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StateTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stateTemplateRef")
    def state_template_ref(self) -> "StateTemplateReference":
        '''(experimental) A reference to a StateTemplate resource.

        :stability: experimental
        '''
        ...


class _IStateTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StateTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotfleetwise.IStateTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="stateTemplateRef")
    def state_template_ref(self) -> "StateTemplateReference":
        '''(experimental) A reference to a StateTemplate resource.

        :stability: experimental
        '''
        return typing.cast("StateTemplateReference", jsii.get(self, "stateTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStateTemplateRef).__jsii_proxy_class__ = lambda : _IStateTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.IVehicleRef")
class IVehicleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Vehicle.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vehicleRef")
    def vehicle_ref(self) -> "VehicleReference":
        '''(experimental) A reference to a Vehicle resource.

        :stability: experimental
        '''
        ...


class _IVehicleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Vehicle.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotfleetwise.IVehicleRef"

    @builtins.property
    @jsii.member(jsii_name="vehicleRef")
    def vehicle_ref(self) -> "VehicleReference":
        '''(experimental) A reference to a Vehicle resource.

        :stability: experimental
        '''
        return typing.cast("VehicleReference", jsii.get(self, "vehicleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVehicleRef).__jsii_proxy_class__ = lambda : _IVehicleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.ModelManifestReference",
    jsii_struct_bases=[],
    name_mapping={
        "model_manifest_arn": "modelManifestArn",
        "model_manifest_name": "modelManifestName",
    },
)
class ModelManifestReference:
    def __init__(
        self,
        *,
        model_manifest_arn: builtins.str,
        model_manifest_name: builtins.str,
    ) -> None:
        '''A reference to a ModelManifest resource.

        :param model_manifest_arn: The ARN of the ModelManifest resource.
        :param model_manifest_name: The Name of the ModelManifest resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotfleetwise as interfaces_iotfleetwise
            
            model_manifest_reference = interfaces_iotfleetwise.ModelManifestReference(
                model_manifest_arn="modelManifestArn",
                model_manifest_name="modelManifestName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4303e142edab0f0c5eb3c9461f6c56820799360689aca63aaa6a668d84b2a93a)
            check_type(argname="argument model_manifest_arn", value=model_manifest_arn, expected_type=type_hints["model_manifest_arn"])
            check_type(argname="argument model_manifest_name", value=model_manifest_name, expected_type=type_hints["model_manifest_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_manifest_arn": model_manifest_arn,
            "model_manifest_name": model_manifest_name,
        }

    @builtins.property
    def model_manifest_arn(self) -> builtins.str:
        '''The ARN of the ModelManifest resource.'''
        result = self._values.get("model_manifest_arn")
        assert result is not None, "Required property 'model_manifest_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_manifest_name(self) -> builtins.str:
        '''The Name of the ModelManifest resource.'''
        result = self._values.get("model_manifest_name")
        assert result is not None, "Required property 'model_manifest_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelManifestReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.SignalCatalogReference",
    jsii_struct_bases=[],
    name_mapping={
        "signal_catalog_arn": "signalCatalogArn",
        "signal_catalog_name": "signalCatalogName",
    },
)
class SignalCatalogReference:
    def __init__(
        self,
        *,
        signal_catalog_arn: builtins.str,
        signal_catalog_name: builtins.str,
    ) -> None:
        '''A reference to a SignalCatalog resource.

        :param signal_catalog_arn: The ARN of the SignalCatalog resource.
        :param signal_catalog_name: The Name of the SignalCatalog resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotfleetwise as interfaces_iotfleetwise
            
            signal_catalog_reference = interfaces_iotfleetwise.SignalCatalogReference(
                signal_catalog_arn="signalCatalogArn",
                signal_catalog_name="signalCatalogName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98e9822856469d474940f4c2ac25de3c10953f46dd1d0c442a1a314b4b6e9476)
            check_type(argname="argument signal_catalog_arn", value=signal_catalog_arn, expected_type=type_hints["signal_catalog_arn"])
            check_type(argname="argument signal_catalog_name", value=signal_catalog_name, expected_type=type_hints["signal_catalog_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "signal_catalog_arn": signal_catalog_arn,
            "signal_catalog_name": signal_catalog_name,
        }

    @builtins.property
    def signal_catalog_arn(self) -> builtins.str:
        '''The ARN of the SignalCatalog resource.'''
        result = self._values.get("signal_catalog_arn")
        assert result is not None, "Required property 'signal_catalog_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_catalog_name(self) -> builtins.str:
        '''The Name of the SignalCatalog resource.'''
        result = self._values.get("signal_catalog_name")
        assert result is not None, "Required property 'signal_catalog_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalCatalogReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.StateTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "state_template_arn": "stateTemplateArn",
        "state_template_name": "stateTemplateName",
    },
)
class StateTemplateReference:
    def __init__(
        self,
        *,
        state_template_arn: builtins.str,
        state_template_name: builtins.str,
    ) -> None:
        '''A reference to a StateTemplate resource.

        :param state_template_arn: The ARN of the StateTemplate resource.
        :param state_template_name: The Name of the StateTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotfleetwise as interfaces_iotfleetwise
            
            state_template_reference = interfaces_iotfleetwise.StateTemplateReference(
                state_template_arn="stateTemplateArn",
                state_template_name="stateTemplateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1087b3d664239f66965dd186def702c54e8343ca53339db0ed9ed72438c8e638)
            check_type(argname="argument state_template_arn", value=state_template_arn, expected_type=type_hints["state_template_arn"])
            check_type(argname="argument state_template_name", value=state_template_name, expected_type=type_hints["state_template_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "state_template_arn": state_template_arn,
            "state_template_name": state_template_name,
        }

    @builtins.property
    def state_template_arn(self) -> builtins.str:
        '''The ARN of the StateTemplate resource.'''
        result = self._values.get("state_template_arn")
        assert result is not None, "Required property 'state_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def state_template_name(self) -> builtins.str:
        '''The Name of the StateTemplate resource.'''
        result = self._values.get("state_template_name")
        assert result is not None, "Required property 'state_template_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StateTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotfleetwise.VehicleReference",
    jsii_struct_bases=[],
    name_mapping={"vehicle_arn": "vehicleArn", "vehicle_name": "vehicleName"},
)
class VehicleReference:
    def __init__(
        self,
        *,
        vehicle_arn: builtins.str,
        vehicle_name: builtins.str,
    ) -> None:
        '''A reference to a Vehicle resource.

        :param vehicle_arn: The ARN of the Vehicle resource.
        :param vehicle_name: The Name of the Vehicle resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotfleetwise as interfaces_iotfleetwise
            
            vehicle_reference = interfaces_iotfleetwise.VehicleReference(
                vehicle_arn="vehicleArn",
                vehicle_name="vehicleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61d06ffc90ff9869984bafa037edf58645afe38a2d5c4db478b3c1e90a67194c)
            check_type(argname="argument vehicle_arn", value=vehicle_arn, expected_type=type_hints["vehicle_arn"])
            check_type(argname="argument vehicle_name", value=vehicle_name, expected_type=type_hints["vehicle_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vehicle_arn": vehicle_arn,
            "vehicle_name": vehicle_name,
        }

    @builtins.property
    def vehicle_arn(self) -> builtins.str:
        '''The ARN of the Vehicle resource.'''
        result = self._values.get("vehicle_arn")
        assert result is not None, "Required property 'vehicle_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vehicle_name(self) -> builtins.str:
        '''The Name of the Vehicle resource.'''
        result = self._values.get("vehicle_name")
        assert result is not None, "Required property 'vehicle_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VehicleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CampaignReference",
    "DecoderManifestReference",
    "FleetReference",
    "ICampaignRef",
    "IDecoderManifestRef",
    "IFleetRef",
    "IModelManifestRef",
    "ISignalCatalogRef",
    "IStateTemplateRef",
    "IVehicleRef",
    "ModelManifestReference",
    "SignalCatalogReference",
    "StateTemplateReference",
    "VehicleReference",
]

publication.publish()

def _typecheckingstub__abc62ce3a2eacc41973eb932cb914110df6dc4f94aa69bbc965f10b97056a756(
    *,
    campaign_arn: builtins.str,
    campaign_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8b332dc87c650b4957bb4734c63a524f7479215b9b9ebea23f3040cb605f988(
    *,
    decoder_manifest_arn: builtins.str,
    decoder_manifest_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e0609989cc7ef5b004c59e00dddcd2a8df28f027b02b4a7e0375d119d6cb1f6(
    *,
    fleet_arn: builtins.str,
    fleet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4303e142edab0f0c5eb3c9461f6c56820799360689aca63aaa6a668d84b2a93a(
    *,
    model_manifest_arn: builtins.str,
    model_manifest_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98e9822856469d474940f4c2ac25de3c10953f46dd1d0c442a1a314b4b6e9476(
    *,
    signal_catalog_arn: builtins.str,
    signal_catalog_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1087b3d664239f66965dd186def702c54e8343ca53339db0ed9ed72438c8e638(
    *,
    state_template_arn: builtins.str,
    state_template_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61d06ffc90ff9869984bafa037edf58645afe38a2d5c4db478b3c1e90a67194c(
    *,
    vehicle_arn: builtins.str,
    vehicle_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICampaignRef, IDecoderManifestRef, IFleetRef, IModelManifestRef, ISignalCatalogRef, IStateTemplateRef, IVehicleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
