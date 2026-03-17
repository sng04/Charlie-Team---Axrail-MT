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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_secretsmanager.IResourcePolicyRef"
)
class IResourcePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        ...


class _IResourcePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_secretsmanager.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_secretsmanager.IRotationScheduleRef"
)
class IRotationScheduleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RotationSchedule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="rotationScheduleRef")
    def rotation_schedule_ref(self) -> "RotationScheduleReference":
        '''(experimental) A reference to a RotationSchedule resource.

        :stability: experimental
        '''
        ...


class _IRotationScheduleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RotationSchedule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_secretsmanager.IRotationScheduleRef"

    @builtins.property
    @jsii.member(jsii_name="rotationScheduleRef")
    def rotation_schedule_ref(self) -> "RotationScheduleReference":
        '''(experimental) A reference to a RotationSchedule resource.

        :stability: experimental
        '''
        return typing.cast("RotationScheduleReference", jsii.get(self, "rotationScheduleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRotationScheduleRef).__jsii_proxy_class__ = lambda : _IRotationScheduleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_secretsmanager.ISecretRef")
class ISecretRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Secret.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(self) -> "SecretReference":
        '''(experimental) A reference to a Secret resource.

        :stability: experimental
        '''
        ...


class _ISecretRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Secret.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_secretsmanager.ISecretRef"

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(self) -> "SecretReference":
        '''(experimental) A reference to a Secret resource.

        :stability: experimental
        '''
        return typing.cast("SecretReference", jsii.get(self, "secretRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecretRef).__jsii_proxy_class__ = lambda : _ISecretRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_secretsmanager.ISecretTargetAttachmentRef"
)
class ISecretTargetAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecretTargetAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="secretTargetAttachmentRef")
    def secret_target_attachment_ref(self) -> "SecretTargetAttachmentReference":
        '''(experimental) A reference to a SecretTargetAttachment resource.

        :stability: experimental
        '''
        ...


class _ISecretTargetAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecretTargetAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_secretsmanager.ISecretTargetAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="secretTargetAttachmentRef")
    def secret_target_attachment_ref(self) -> "SecretTargetAttachmentReference":
        '''(experimental) A reference to a SecretTargetAttachment resource.

        :stability: experimental
        '''
        return typing.cast("SecretTargetAttachmentReference", jsii.get(self, "secretTargetAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecretTargetAttachmentRef).__jsii_proxy_class__ = lambda : _ISecretTargetAttachmentRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_secretsmanager.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"secret_id": "secretId"},
)
class ResourcePolicyReference:
    def __init__(self, *, secret_id: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param secret_id: The SecretId of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_secretsmanager as interfaces_secretsmanager
            
            resource_policy_reference = interfaces_secretsmanager.ResourcePolicyReference(
                secret_id="secretId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0ca96091907390a9b4159a50654cd69c9b77b7c347601999dae8b82c4aea6a9)
            check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_id": secret_id,
        }

    @builtins.property
    def secret_id(self) -> builtins.str:
        '''The SecretId of the ResourcePolicy resource.'''
        result = self._values.get("secret_id")
        assert result is not None, "Required property 'secret_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_secretsmanager.RotationScheduleReference",
    jsii_struct_bases=[],
    name_mapping={"rotation_schedule_id": "rotationScheduleId"},
)
class RotationScheduleReference:
    def __init__(self, *, rotation_schedule_id: builtins.str) -> None:
        '''A reference to a RotationSchedule resource.

        :param rotation_schedule_id: The Id of the RotationSchedule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_secretsmanager as interfaces_secretsmanager
            
            rotation_schedule_reference = interfaces_secretsmanager.RotationScheduleReference(
                rotation_schedule_id="rotationScheduleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a481f4d9172d19acd5eb5e9cfba83a71e1c2531a77b74666f66c54d530ec4177)
            check_type(argname="argument rotation_schedule_id", value=rotation_schedule_id, expected_type=type_hints["rotation_schedule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rotation_schedule_id": rotation_schedule_id,
        }

    @builtins.property
    def rotation_schedule_id(self) -> builtins.str:
        '''The Id of the RotationSchedule resource.'''
        result = self._values.get("rotation_schedule_id")
        assert result is not None, "Required property 'rotation_schedule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RotationScheduleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_secretsmanager.SecretReference",
    jsii_struct_bases=[],
    name_mapping={"secret_id": "secretId"},
)
class SecretReference:
    def __init__(self, *, secret_id: builtins.str) -> None:
        '''A reference to a Secret resource.

        :param secret_id: The Id of the Secret resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_secretsmanager as interfaces_secretsmanager
            
            secret_reference = interfaces_secretsmanager.SecretReference(
                secret_id="secretId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b324ea23961f09929b42f934498dca8c7d62f0978eebebc57a34b4668d706fb8)
            check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_id": secret_id,
        }

    @builtins.property
    def secret_id(self) -> builtins.str:
        '''The Id of the Secret resource.'''
        result = self._values.get("secret_id")
        assert result is not None, "Required property 'secret_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_secretsmanager.SecretTargetAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"secret_id": "secretId"},
)
class SecretTargetAttachmentReference:
    def __init__(self, *, secret_id: builtins.str) -> None:
        '''A reference to a SecretTargetAttachment resource.

        :param secret_id: The SecretId of the SecretTargetAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_secretsmanager as interfaces_secretsmanager
            
            secret_target_attachment_reference = interfaces_secretsmanager.SecretTargetAttachmentReference(
                secret_id="secretId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f70d28228dde47c628bc306d8f6780dee467d05d857b0b0b777cf8e3509c39b2)
            check_type(argname="argument secret_id", value=secret_id, expected_type=type_hints["secret_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_id": secret_id,
        }

    @builtins.property
    def secret_id(self) -> builtins.str:
        '''The SecretId of the SecretTargetAttachment resource.'''
        result = self._values.get("secret_id")
        assert result is not None, "Required property 'secret_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecretTargetAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IResourcePolicyRef",
    "IRotationScheduleRef",
    "ISecretRef",
    "ISecretTargetAttachmentRef",
    "ResourcePolicyReference",
    "RotationScheduleReference",
    "SecretReference",
    "SecretTargetAttachmentReference",
]

publication.publish()

def _typecheckingstub__a0ca96091907390a9b4159a50654cd69c9b77b7c347601999dae8b82c4aea6a9(
    *,
    secret_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a481f4d9172d19acd5eb5e9cfba83a71e1c2531a77b74666f66c54d530ec4177(
    *,
    rotation_schedule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b324ea23961f09929b42f934498dca8c7d62f0978eebebc57a34b4668d706fb8(
    *,
    secret_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f70d28228dde47c628bc306d8f6780dee467d05d857b0b0b777cf8e3509c39b2(
    *,
    secret_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IResourcePolicyRef, IRotationScheduleRef, ISecretRef, ISecretTargetAttachmentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
