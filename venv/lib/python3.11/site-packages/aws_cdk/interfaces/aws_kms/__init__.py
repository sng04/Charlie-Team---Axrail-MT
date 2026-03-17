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
    jsii_type="aws-cdk-lib.interfaces.aws_kms.AliasReference",
    jsii_struct_bases=[],
    name_mapping={"alias_name": "aliasName"},
)
class AliasReference:
    def __init__(self, *, alias_name: builtins.str) -> None:
        '''A reference to a Alias resource.

        :param alias_name: The AliasName of the Alias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kms as interfaces_kms
            
            alias_reference = interfaces_kms.AliasReference(
                alias_name="aliasName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d3faf725255f465ef6e4a27ba2219f10943780e7f60a70b90aebb2102696f26)
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_name": alias_name,
        }

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''The AliasName of the Alias resource.'''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kms.IAliasRef")
class IAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Alias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aliasRef")
    def alias_ref(self) -> "AliasReference":
        '''(experimental) A reference to a Alias resource.

        :stability: experimental
        '''
        ...


class _IAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Alias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kms.IAliasRef"

    @builtins.property
    @jsii.member(jsii_name="aliasRef")
    def alias_ref(self) -> "AliasReference":
        '''(experimental) A reference to a Alias resource.

        :stability: experimental
        '''
        return typing.cast("AliasReference", jsii.get(self, "aliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAliasRef).__jsii_proxy_class__ = lambda : _IAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kms.IKeyRef")
class IKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Key.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="keyRef")
    def key_ref(self) -> "KeyReference":
        '''(experimental) A reference to a Key resource.

        :stability: experimental
        '''
        ...


class _IKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Key.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kms.IKeyRef"

    @builtins.property
    @jsii.member(jsii_name="keyRef")
    def key_ref(self) -> "KeyReference":
        '''(experimental) A reference to a Key resource.

        :stability: experimental
        '''
        return typing.cast("KeyReference", jsii.get(self, "keyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKeyRef).__jsii_proxy_class__ = lambda : _IKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kms.IReplicaKeyRef")
class IReplicaKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicaKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="replicaKeyRef")
    def replica_key_ref(self) -> "ReplicaKeyReference":
        '''(experimental) A reference to a ReplicaKey resource.

        :stability: experimental
        '''
        ...


class _IReplicaKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicaKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kms.IReplicaKeyRef"

    @builtins.property
    @jsii.member(jsii_name="replicaKeyRef")
    def replica_key_ref(self) -> "ReplicaKeyReference":
        '''(experimental) A reference to a ReplicaKey resource.

        :stability: experimental
        '''
        return typing.cast("ReplicaKeyReference", jsii.get(self, "replicaKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReplicaKeyRef).__jsii_proxy_class__ = lambda : _IReplicaKeyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kms.KeyReference",
    jsii_struct_bases=[],
    name_mapping={"key_arn": "keyArn", "key_id": "keyId"},
)
class KeyReference:
    def __init__(self, *, key_arn: builtins.str, key_id: builtins.str) -> None:
        '''A reference to a Key resource.

        :param key_arn: The ARN of the Key resource.
        :param key_id: The KeyId of the Key resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kms as interfaces_kms
            
            key_reference = interfaces_kms.KeyReference(
                key_arn="keyArn",
                key_id="keyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f039db5a692a3771431da3afdfa15c79aa03c9c8fc164515c7aa79a58eab76a9)
            check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_arn": key_arn,
            "key_id": key_id,
        }

    @builtins.property
    def key_arn(self) -> builtins.str:
        '''The ARN of the Key resource.'''
        result = self._values.get("key_arn")
        assert result is not None, "Required property 'key_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_id(self) -> builtins.str:
        '''The KeyId of the Key resource.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kms.ReplicaKeyReference",
    jsii_struct_bases=[],
    name_mapping={"key_id": "keyId", "replica_key_arn": "replicaKeyArn"},
)
class ReplicaKeyReference:
    def __init__(self, *, key_id: builtins.str, replica_key_arn: builtins.str) -> None:
        '''A reference to a ReplicaKey resource.

        :param key_id: The KeyId of the ReplicaKey resource.
        :param replica_key_arn: The ARN of the ReplicaKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kms as interfaces_kms
            
            replica_key_reference = interfaces_kms.ReplicaKeyReference(
                key_id="keyId",
                replica_key_arn="replicaKeyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67eaf72b0e4babc458d0a9e15aad8ebbd586bae93c4dc4be24f6d0c4269035d6)
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
            check_type(argname="argument replica_key_arn", value=replica_key_arn, expected_type=type_hints["replica_key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_id": key_id,
            "replica_key_arn": replica_key_arn,
        }

    @builtins.property
    def key_id(self) -> builtins.str:
        '''The KeyId of the ReplicaKey resource.'''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replica_key_arn(self) -> builtins.str:
        '''The ARN of the ReplicaKey resource.'''
        result = self._values.get("replica_key_arn")
        assert result is not None, "Required property 'replica_key_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicaKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AliasReference",
    "IAliasRef",
    "IKeyRef",
    "IReplicaKeyRef",
    "KeyReference",
    "ReplicaKeyReference",
]

publication.publish()

def _typecheckingstub__7d3faf725255f465ef6e4a27ba2219f10943780e7f60a70b90aebb2102696f26(
    *,
    alias_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f039db5a692a3771431da3afdfa15c79aa03c9c8fc164515c7aa79a58eab76a9(
    *,
    key_arn: builtins.str,
    key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67eaf72b0e4babc458d0a9e15aad8ebbd586bae93c4dc4be24f6d0c4269035d6(
    *,
    key_id: builtins.str,
    replica_key_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAliasRef, IKeyRef, IReplicaKeyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
