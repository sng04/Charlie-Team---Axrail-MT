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
    jsii_type="aws-cdk-lib.interfaces.aws_b2bi.CapabilityReference",
    jsii_struct_bases=[],
    name_mapping={"capability_arn": "capabilityArn", "capability_id": "capabilityId"},
)
class CapabilityReference:
    def __init__(
        self,
        *,
        capability_arn: builtins.str,
        capability_id: builtins.str,
    ) -> None:
        '''A reference to a Capability resource.

        :param capability_arn: The ARN of the Capability resource.
        :param capability_id: The CapabilityId of the Capability resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_b2bi as interfaces_b2bi
            
            capability_reference = interfaces_b2bi.CapabilityReference(
                capability_arn="capabilityArn",
                capability_id="capabilityId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a2e713a60e2fb71716a0df56c864fe973cc3b50fabe2de48c98f74f6f0bce1)
            check_type(argname="argument capability_arn", value=capability_arn, expected_type=type_hints["capability_arn"])
            check_type(argname="argument capability_id", value=capability_id, expected_type=type_hints["capability_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capability_arn": capability_arn,
            "capability_id": capability_id,
        }

    @builtins.property
    def capability_arn(self) -> builtins.str:
        '''The ARN of the Capability resource.'''
        result = self._values.get("capability_arn")
        assert result is not None, "Required property 'capability_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capability_id(self) -> builtins.str:
        '''The CapabilityId of the Capability resource.'''
        result = self._values.get("capability_id")
        assert result is not None, "Required property 'capability_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapabilityReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_b2bi.ICapabilityRef")
class ICapabilityRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Capability.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="capabilityRef")
    def capability_ref(self) -> "CapabilityReference":
        '''(experimental) A reference to a Capability resource.

        :stability: experimental
        '''
        ...


class _ICapabilityRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Capability.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_b2bi.ICapabilityRef"

    @builtins.property
    @jsii.member(jsii_name="capabilityRef")
    def capability_ref(self) -> "CapabilityReference":
        '''(experimental) A reference to a Capability resource.

        :stability: experimental
        '''
        return typing.cast("CapabilityReference", jsii.get(self, "capabilityRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICapabilityRef).__jsii_proxy_class__ = lambda : _ICapabilityRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_b2bi.IPartnershipRef")
class IPartnershipRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Partnership.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="partnershipRef")
    def partnership_ref(self) -> "PartnershipReference":
        '''(experimental) A reference to a Partnership resource.

        :stability: experimental
        '''
        ...


class _IPartnershipRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Partnership.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_b2bi.IPartnershipRef"

    @builtins.property
    @jsii.member(jsii_name="partnershipRef")
    def partnership_ref(self) -> "PartnershipReference":
        '''(experimental) A reference to a Partnership resource.

        :stability: experimental
        '''
        return typing.cast("PartnershipReference", jsii.get(self, "partnershipRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPartnershipRef).__jsii_proxy_class__ = lambda : _IPartnershipRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_b2bi.IProfileRef")
class IProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Profile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "ProfileReference":
        '''(experimental) A reference to a Profile resource.

        :stability: experimental
        '''
        ...


class _IProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Profile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_b2bi.IProfileRef"

    @builtins.property
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "ProfileReference":
        '''(experimental) A reference to a Profile resource.

        :stability: experimental
        '''
        return typing.cast("ProfileReference", jsii.get(self, "profileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfileRef).__jsii_proxy_class__ = lambda : _IProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_b2bi.ITransformerRef")
class ITransformerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Transformer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transformerRef")
    def transformer_ref(self) -> "TransformerReference":
        '''(experimental) A reference to a Transformer resource.

        :stability: experimental
        '''
        ...


class _ITransformerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Transformer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_b2bi.ITransformerRef"

    @builtins.property
    @jsii.member(jsii_name="transformerRef")
    def transformer_ref(self) -> "TransformerReference":
        '''(experimental) A reference to a Transformer resource.

        :stability: experimental
        '''
        return typing.cast("TransformerReference", jsii.get(self, "transformerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransformerRef).__jsii_proxy_class__ = lambda : _ITransformerRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_b2bi.PartnershipReference",
    jsii_struct_bases=[],
    name_mapping={
        "partnership_arn": "partnershipArn",
        "partnership_id": "partnershipId",
    },
)
class PartnershipReference:
    def __init__(
        self,
        *,
        partnership_arn: builtins.str,
        partnership_id: builtins.str,
    ) -> None:
        '''A reference to a Partnership resource.

        :param partnership_arn: The ARN of the Partnership resource.
        :param partnership_id: The PartnershipId of the Partnership resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_b2bi as interfaces_b2bi
            
            partnership_reference = interfaces_b2bi.PartnershipReference(
                partnership_arn="partnershipArn",
                partnership_id="partnershipId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c687603cc7d0acc0f23a4ca99e3f0df0b1bc82d6783113da186d59156d95882)
            check_type(argname="argument partnership_arn", value=partnership_arn, expected_type=type_hints["partnership_arn"])
            check_type(argname="argument partnership_id", value=partnership_id, expected_type=type_hints["partnership_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "partnership_arn": partnership_arn,
            "partnership_id": partnership_id,
        }

    @builtins.property
    def partnership_arn(self) -> builtins.str:
        '''The ARN of the Partnership resource.'''
        result = self._values.get("partnership_arn")
        assert result is not None, "Required property 'partnership_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partnership_id(self) -> builtins.str:
        '''The PartnershipId of the Partnership resource.'''
        result = self._values.get("partnership_id")
        assert result is not None, "Required property 'partnership_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PartnershipReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_b2bi.ProfileReference",
    jsii_struct_bases=[],
    name_mapping={"profile_arn": "profileArn", "profile_id": "profileId"},
)
class ProfileReference:
    def __init__(self, *, profile_arn: builtins.str, profile_id: builtins.str) -> None:
        '''A reference to a Profile resource.

        :param profile_arn: The ARN of the Profile resource.
        :param profile_id: The ProfileId of the Profile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_b2bi as interfaces_b2bi
            
            profile_reference = interfaces_b2bi.ProfileReference(
                profile_arn="profileArn",
                profile_id="profileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__277efee3c1b4f9109a4066cc871dc08b73bf9f1b20febefe61b2f996c14d0180)
            check_type(argname="argument profile_arn", value=profile_arn, expected_type=type_hints["profile_arn"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile_arn": profile_arn,
            "profile_id": profile_id,
        }

    @builtins.property
    def profile_arn(self) -> builtins.str:
        '''The ARN of the Profile resource.'''
        result = self._values.get("profile_arn")
        assert result is not None, "Required property 'profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''The ProfileId of the Profile resource.'''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_b2bi.TransformerReference",
    jsii_struct_bases=[],
    name_mapping={
        "transformer_arn": "transformerArn",
        "transformer_id": "transformerId",
    },
)
class TransformerReference:
    def __init__(
        self,
        *,
        transformer_arn: builtins.str,
        transformer_id: builtins.str,
    ) -> None:
        '''A reference to a Transformer resource.

        :param transformer_arn: The ARN of the Transformer resource.
        :param transformer_id: The TransformerId of the Transformer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_b2bi as interfaces_b2bi
            
            transformer_reference = interfaces_b2bi.TransformerReference(
                transformer_arn="transformerArn",
                transformer_id="transformerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68f8457e823d166b77ba434475d778e2f7ce6a5eff2edd07b9978da7bfc984ea)
            check_type(argname="argument transformer_arn", value=transformer_arn, expected_type=type_hints["transformer_arn"])
            check_type(argname="argument transformer_id", value=transformer_id, expected_type=type_hints["transformer_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transformer_arn": transformer_arn,
            "transformer_id": transformer_id,
        }

    @builtins.property
    def transformer_arn(self) -> builtins.str:
        '''The ARN of the Transformer resource.'''
        result = self._values.get("transformer_arn")
        assert result is not None, "Required property 'transformer_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transformer_id(self) -> builtins.str:
        '''The TransformerId of the Transformer resource.'''
        result = self._values.get("transformer_id")
        assert result is not None, "Required property 'transformer_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransformerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CapabilityReference",
    "ICapabilityRef",
    "IPartnershipRef",
    "IProfileRef",
    "ITransformerRef",
    "PartnershipReference",
    "ProfileReference",
    "TransformerReference",
]

publication.publish()

def _typecheckingstub__e6a2e713a60e2fb71716a0df56c864fe973cc3b50fabe2de48c98f74f6f0bce1(
    *,
    capability_arn: builtins.str,
    capability_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c687603cc7d0acc0f23a4ca99e3f0df0b1bc82d6783113da186d59156d95882(
    *,
    partnership_arn: builtins.str,
    partnership_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__277efee3c1b4f9109a4066cc871dc08b73bf9f1b20febefe61b2f996c14d0180(
    *,
    profile_arn: builtins.str,
    profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68f8457e823d166b77ba434475d778e2f7ce6a5eff2edd07b9978da7bfc984ea(
    *,
    transformer_arn: builtins.str,
    transformer_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICapabilityRef, IPartnershipRef, IProfileRef, ITransformerRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
