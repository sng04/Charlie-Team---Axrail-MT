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
    jsii_type="aws-cdk-lib.interfaces.aws_route53.CidrCollectionReference",
    jsii_struct_bases=[],
    name_mapping={
        "cidr_collection_arn": "cidrCollectionArn",
        "cidr_collection_id": "cidrCollectionId",
    },
)
class CidrCollectionReference:
    def __init__(
        self,
        *,
        cidr_collection_arn: builtins.str,
        cidr_collection_id: builtins.str,
    ) -> None:
        '''A reference to a CidrCollection resource.

        :param cidr_collection_arn: The ARN of the CidrCollection resource.
        :param cidr_collection_id: The Id of the CidrCollection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            cidr_collection_reference = interfaces_route53.CidrCollectionReference(
                cidr_collection_arn="cidrCollectionArn",
                cidr_collection_id="cidrCollectionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a29c970e3dc59eb61f1e0e1c4183e889924847e040535cfbaa68366929f5a856)
            check_type(argname="argument cidr_collection_arn", value=cidr_collection_arn, expected_type=type_hints["cidr_collection_arn"])
            check_type(argname="argument cidr_collection_id", value=cidr_collection_id, expected_type=type_hints["cidr_collection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidr_collection_arn": cidr_collection_arn,
            "cidr_collection_id": cidr_collection_id,
        }

    @builtins.property
    def cidr_collection_arn(self) -> builtins.str:
        '''The ARN of the CidrCollection resource.'''
        result = self._values.get("cidr_collection_arn")
        assert result is not None, "Required property 'cidr_collection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr_collection_id(self) -> builtins.str:
        '''The Id of the CidrCollection resource.'''
        result = self._values.get("cidr_collection_id")
        assert result is not None, "Required property 'cidr_collection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CidrCollectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.DNSSECReference",
    jsii_struct_bases=[],
    name_mapping={"hosted_zone_id": "hostedZoneId"},
)
class DNSSECReference:
    def __init__(self, *, hosted_zone_id: builtins.str) -> None:
        '''A reference to a DNSSEC resource.

        :param hosted_zone_id: The HostedZoneId of the DNSSEC resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            d_nSSECReference = interfaces_route53.DNSSECReference(
                hosted_zone_id="hostedZoneId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5f748a2bea377e2fd2ed6d48058439646815e844893d9564084429051caf8f4)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''The HostedZoneId of the DNSSEC resource.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DNSSECReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.HealthCheckReference",
    jsii_struct_bases=[],
    name_mapping={"health_check_id": "healthCheckId"},
)
class HealthCheckReference:
    def __init__(self, *, health_check_id: builtins.str) -> None:
        '''A reference to a HealthCheck resource.

        :param health_check_id: The HealthCheckId of the HealthCheck resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            health_check_reference = interfaces_route53.HealthCheckReference(
                health_check_id="healthCheckId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93a61fcf52d45a4375dfb1ae5d0b7b0555ae1091958107075e82bc35ca0d0275)
            check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "health_check_id": health_check_id,
        }

    @builtins.property
    def health_check_id(self) -> builtins.str:
        '''The HealthCheckId of the HealthCheck resource.'''
        result = self._values.get("health_check_id")
        assert result is not None, "Required property 'health_check_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HealthCheckReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.HostedZoneReference",
    jsii_struct_bases=[],
    name_mapping={"hosted_zone_id": "hostedZoneId"},
)
class HostedZoneReference:
    def __init__(self, *, hosted_zone_id: builtins.str) -> None:
        '''A reference to a HostedZone resource.

        :param hosted_zone_id: The Id of the HostedZone resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            hosted_zone_reference = interfaces_route53.HostedZoneReference(
                hosted_zone_id="hostedZoneId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b4ca2affe8c503a8b4867d3e31a36ed15f0aa004cff0a9202da3d2bbbb7fe4c)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''The Id of the HostedZone resource.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.ICidrCollectionRef")
class ICidrCollectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CidrCollection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cidrCollectionRef")
    def cidr_collection_ref(self) -> "CidrCollectionReference":
        '''(experimental) A reference to a CidrCollection resource.

        :stability: experimental
        '''
        ...


class _ICidrCollectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CidrCollection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.ICidrCollectionRef"

    @builtins.property
    @jsii.member(jsii_name="cidrCollectionRef")
    def cidr_collection_ref(self) -> "CidrCollectionReference":
        '''(experimental) A reference to a CidrCollection resource.

        :stability: experimental
        '''
        return typing.cast("CidrCollectionReference", jsii.get(self, "cidrCollectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICidrCollectionRef).__jsii_proxy_class__ = lambda : _ICidrCollectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IDNSSECRef")
class IDNSSECRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DNSSEC.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dnssecRef")
    def dnssec_ref(self) -> "DNSSECReference":
        '''(experimental) A reference to a DNSSEC resource.

        :stability: experimental
        '''
        ...


class _IDNSSECRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DNSSEC.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IDNSSECRef"

    @builtins.property
    @jsii.member(jsii_name="dnssecRef")
    def dnssec_ref(self) -> "DNSSECReference":
        '''(experimental) A reference to a DNSSEC resource.

        :stability: experimental
        '''
        return typing.cast("DNSSECReference", jsii.get(self, "dnssecRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDNSSECRef).__jsii_proxy_class__ = lambda : _IDNSSECRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IHealthCheckRef")
class IHealthCheckRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HealthCheck.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="healthCheckRef")
    def health_check_ref(self) -> "HealthCheckReference":
        '''(experimental) A reference to a HealthCheck resource.

        :stability: experimental
        '''
        ...


class _IHealthCheckRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HealthCheck.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IHealthCheckRef"

    @builtins.property
    @jsii.member(jsii_name="healthCheckRef")
    def health_check_ref(self) -> "HealthCheckReference":
        '''(experimental) A reference to a HealthCheck resource.

        :stability: experimental
        '''
        return typing.cast("HealthCheckReference", jsii.get(self, "healthCheckRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHealthCheckRef).__jsii_proxy_class__ = lambda : _IHealthCheckRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IHostedZoneRef")
class IHostedZoneRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HostedZone.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hostedZoneRef")
    def hosted_zone_ref(self) -> "HostedZoneReference":
        '''(experimental) A reference to a HostedZone resource.

        :stability: experimental
        '''
        ...


class _IHostedZoneRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HostedZone.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IHostedZoneRef"

    @builtins.property
    @jsii.member(jsii_name="hostedZoneRef")
    def hosted_zone_ref(self) -> "HostedZoneReference":
        '''(experimental) A reference to a HostedZone resource.

        :stability: experimental
        '''
        return typing.cast("HostedZoneReference", jsii.get(self, "hostedZoneRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHostedZoneRef).__jsii_proxy_class__ = lambda : _IHostedZoneRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IKeySigningKeyRef")
class IKeySigningKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a KeySigningKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyRef")
    def key_signing_key_ref(self) -> "KeySigningKeyReference":
        '''(experimental) A reference to a KeySigningKey resource.

        :stability: experimental
        '''
        ...


class _IKeySigningKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a KeySigningKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IKeySigningKeyRef"

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyRef")
    def key_signing_key_ref(self) -> "KeySigningKeyReference":
        '''(experimental) A reference to a KeySigningKey resource.

        :stability: experimental
        '''
        return typing.cast("KeySigningKeyReference", jsii.get(self, "keySigningKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKeySigningKeyRef).__jsii_proxy_class__ = lambda : _IKeySigningKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IRecordSetGroupRef")
class IRecordSetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RecordSetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="recordSetGroupRef")
    def record_set_group_ref(self) -> "RecordSetGroupReference":
        '''(experimental) A reference to a RecordSetGroup resource.

        :stability: experimental
        '''
        ...


class _IRecordSetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RecordSetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IRecordSetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="recordSetGroupRef")
    def record_set_group_ref(self) -> "RecordSetGroupReference":
        '''(experimental) A reference to a RecordSetGroup resource.

        :stability: experimental
        '''
        return typing.cast("RecordSetGroupReference", jsii.get(self, "recordSetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRecordSetGroupRef).__jsii_proxy_class__ = lambda : _IRecordSetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53.IRecordSetRef")
class IRecordSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RecordSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="recordSetRef")
    def record_set_ref(self) -> "RecordSetReference":
        '''(experimental) A reference to a RecordSet resource.

        :stability: experimental
        '''
        ...


class _IRecordSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RecordSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53.IRecordSetRef"

    @builtins.property
    @jsii.member(jsii_name="recordSetRef")
    def record_set_ref(self) -> "RecordSetReference":
        '''(experimental) A reference to a RecordSet resource.

        :stability: experimental
        '''
        return typing.cast("RecordSetReference", jsii.get(self, "recordSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRecordSetRef).__jsii_proxy_class__ = lambda : _IRecordSetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.KeySigningKeyReference",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone_id": "hostedZoneId",
        "key_signing_key_name": "keySigningKeyName",
    },
)
class KeySigningKeyReference:
    def __init__(
        self,
        *,
        hosted_zone_id: builtins.str,
        key_signing_key_name: builtins.str,
    ) -> None:
        '''A reference to a KeySigningKey resource.

        :param hosted_zone_id: The HostedZoneId of the KeySigningKey resource.
        :param key_signing_key_name: The Name of the KeySigningKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            key_signing_key_reference = interfaces_route53.KeySigningKeyReference(
                hosted_zone_id="hostedZoneId",
                key_signing_key_name="keySigningKeyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__740b6b79569b61714dbaad1664d38c2e457f5ba4d550ba6271197a8fd1b8e59d)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument key_signing_key_name", value=key_signing_key_name, expected_type=type_hints["key_signing_key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
            "key_signing_key_name": key_signing_key_name,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''The HostedZoneId of the KeySigningKey resource.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_signing_key_name(self) -> builtins.str:
        '''The Name of the KeySigningKey resource.'''
        result = self._values.get("key_signing_key_name")
        assert result is not None, "Required property 'key_signing_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeySigningKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.RecordSetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"record_set_group_id": "recordSetGroupId"},
)
class RecordSetGroupReference:
    def __init__(self, *, record_set_group_id: builtins.str) -> None:
        '''A reference to a RecordSetGroup resource.

        :param record_set_group_id: The Id of the RecordSetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            record_set_group_reference = interfaces_route53.RecordSetGroupReference(
                record_set_group_id="recordSetGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__843f82028bf43583ae47be1e10363ba4894e39f9bd7f71769ddfdced48189b19)
            check_type(argname="argument record_set_group_id", value=record_set_group_id, expected_type=type_hints["record_set_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_set_group_id": record_set_group_id,
        }

    @builtins.property
    def record_set_group_id(self) -> builtins.str:
        '''The Id of the RecordSetGroup resource.'''
        result = self._values.get("record_set_group_id")
        assert result is not None, "Required property 'record_set_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordSetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53.RecordSetReference",
    jsii_struct_bases=[],
    name_mapping={"record_set_name": "recordSetName"},
)
class RecordSetReference:
    def __init__(self, *, record_set_name: builtins.str) -> None:
        '''A reference to a RecordSet resource.

        :param record_set_name: The Name of the RecordSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53 as interfaces_route53
            
            record_set_reference = interfaces_route53.RecordSetReference(
                record_set_name="recordSetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__309b4ebd3a2bc9de4559b92e46a6d5aa5ef18238d81d559d28fffaf3353eda80)
            check_type(argname="argument record_set_name", value=record_set_name, expected_type=type_hints["record_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "record_set_name": record_set_name,
        }

    @builtins.property
    def record_set_name(self) -> builtins.str:
        '''The Name of the RecordSet resource.'''
        result = self._values.get("record_set_name")
        assert result is not None, "Required property 'record_set_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CidrCollectionReference",
    "DNSSECReference",
    "HealthCheckReference",
    "HostedZoneReference",
    "ICidrCollectionRef",
    "IDNSSECRef",
    "IHealthCheckRef",
    "IHostedZoneRef",
    "IKeySigningKeyRef",
    "IRecordSetGroupRef",
    "IRecordSetRef",
    "KeySigningKeyReference",
    "RecordSetGroupReference",
    "RecordSetReference",
]

publication.publish()

def _typecheckingstub__a29c970e3dc59eb61f1e0e1c4183e889924847e040535cfbaa68366929f5a856(
    *,
    cidr_collection_arn: builtins.str,
    cidr_collection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5f748a2bea377e2fd2ed6d48058439646815e844893d9564084429051caf8f4(
    *,
    hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93a61fcf52d45a4375dfb1ae5d0b7b0555ae1091958107075e82bc35ca0d0275(
    *,
    health_check_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b4ca2affe8c503a8b4867d3e31a36ed15f0aa004cff0a9202da3d2bbbb7fe4c(
    *,
    hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740b6b79569b61714dbaad1664d38c2e457f5ba4d550ba6271197a8fd1b8e59d(
    *,
    hosted_zone_id: builtins.str,
    key_signing_key_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843f82028bf43583ae47be1e10363ba4894e39f9bd7f71769ddfdced48189b19(
    *,
    record_set_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__309b4ebd3a2bc9de4559b92e46a6d5aa5ef18238d81d559d28fffaf3353eda80(
    *,
    record_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICidrCollectionRef, IDNSSECRef, IHealthCheckRef, IHostedZoneRef, IKeySigningKeyRef, IRecordSetGroupRef, IRecordSetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
