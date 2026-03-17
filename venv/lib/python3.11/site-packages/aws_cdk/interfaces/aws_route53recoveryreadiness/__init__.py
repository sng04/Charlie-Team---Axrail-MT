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
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoveryreadiness.CellReference",
    jsii_struct_bases=[],
    name_mapping={"cell_arn": "cellArn", "cell_name": "cellName"},
)
class CellReference:
    def __init__(self, *, cell_arn: builtins.str, cell_name: builtins.str) -> None:
        '''A reference to a Cell resource.

        :param cell_arn: The ARN of the Cell resource.
        :param cell_name: The CellName of the Cell resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53recoveryreadiness as interfaces_route53recoveryreadiness
            
            cell_reference = interfaces_route53recoveryreadiness.CellReference(
                cell_arn="cellArn",
                cell_name="cellName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e358b8991d80ff68622d3a3d32622a01159eebcb8a6c0f34ffa360e940931bce)
            check_type(argname="argument cell_arn", value=cell_arn, expected_type=type_hints["cell_arn"])
            check_type(argname="argument cell_name", value=cell_name, expected_type=type_hints["cell_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cell_arn": cell_arn,
            "cell_name": cell_name,
        }

    @builtins.property
    def cell_arn(self) -> builtins.str:
        '''The ARN of the Cell resource.'''
        result = self._values.get("cell_arn")
        assert result is not None, "Required property 'cell_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cell_name(self) -> builtins.str:
        '''The CellName of the Cell resource.'''
        result = self._values.get("cell_name")
        assert result is not None, "Required property 'cell_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CellReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoveryreadiness.ICellRef"
)
class ICellRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Cell.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cellRef")
    def cell_ref(self) -> "CellReference":
        '''(experimental) A reference to a Cell resource.

        :stability: experimental
        '''
        ...


class _ICellRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Cell.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53recoveryreadiness.ICellRef"

    @builtins.property
    @jsii.member(jsii_name="cellRef")
    def cell_ref(self) -> "CellReference":
        '''(experimental) A reference to a Cell resource.

        :stability: experimental
        '''
        return typing.cast("CellReference", jsii.get(self, "cellRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICellRef).__jsii_proxy_class__ = lambda : _ICellRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoveryreadiness.IReadinessCheckRef"
)
class IReadinessCheckRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReadinessCheck.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="readinessCheckRef")
    def readiness_check_ref(self) -> "ReadinessCheckReference":
        '''(experimental) A reference to a ReadinessCheck resource.

        :stability: experimental
        '''
        ...


class _IReadinessCheckRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReadinessCheck.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53recoveryreadiness.IReadinessCheckRef"

    @builtins.property
    @jsii.member(jsii_name="readinessCheckRef")
    def readiness_check_ref(self) -> "ReadinessCheckReference":
        '''(experimental) A reference to a ReadinessCheck resource.

        :stability: experimental
        '''
        return typing.cast("ReadinessCheckReference", jsii.get(self, "readinessCheckRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReadinessCheckRef).__jsii_proxy_class__ = lambda : _IReadinessCheckRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoveryreadiness.IRecoveryGroupRef"
)
class IRecoveryGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RecoveryGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="recoveryGroupRef")
    def recovery_group_ref(self) -> "RecoveryGroupReference":
        '''(experimental) A reference to a RecoveryGroup resource.

        :stability: experimental
        '''
        ...


class _IRecoveryGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RecoveryGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53recoveryreadiness.IRecoveryGroupRef"

    @builtins.property
    @jsii.member(jsii_name="recoveryGroupRef")
    def recovery_group_ref(self) -> "RecoveryGroupReference":
        '''(experimental) A reference to a RecoveryGroup resource.

        :stability: experimental
        '''
        return typing.cast("RecoveryGroupReference", jsii.get(self, "recoveryGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRecoveryGroupRef).__jsii_proxy_class__ = lambda : _IRecoveryGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoveryreadiness.IResourceSetRef"
)
class IResourceSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceSetRef")
    def resource_set_ref(self) -> "ResourceSetReference":
        '''(experimental) A reference to a ResourceSet resource.

        :stability: experimental
        '''
        ...


class _IResourceSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53recoveryreadiness.IResourceSetRef"

    @builtins.property
    @jsii.member(jsii_name="resourceSetRef")
    def resource_set_ref(self) -> "ResourceSetReference":
        '''(experimental) A reference to a ResourceSet resource.

        :stability: experimental
        '''
        return typing.cast("ResourceSetReference", jsii.get(self, "resourceSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceSetRef).__jsii_proxy_class__ = lambda : _IResourceSetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoveryreadiness.ReadinessCheckReference",
    jsii_struct_bases=[],
    name_mapping={
        "readiness_check_arn": "readinessCheckArn",
        "readiness_check_name": "readinessCheckName",
    },
)
class ReadinessCheckReference:
    def __init__(
        self,
        *,
        readiness_check_arn: builtins.str,
        readiness_check_name: builtins.str,
    ) -> None:
        '''A reference to a ReadinessCheck resource.

        :param readiness_check_arn: The ARN of the ReadinessCheck resource.
        :param readiness_check_name: The ReadinessCheckName of the ReadinessCheck resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53recoveryreadiness as interfaces_route53recoveryreadiness
            
            readiness_check_reference = interfaces_route53recoveryreadiness.ReadinessCheckReference(
                readiness_check_arn="readinessCheckArn",
                readiness_check_name="readinessCheckName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bececdbdce22a5416f98f7c557e0fa4672dfae0f84db728756dacc691f3616b2)
            check_type(argname="argument readiness_check_arn", value=readiness_check_arn, expected_type=type_hints["readiness_check_arn"])
            check_type(argname="argument readiness_check_name", value=readiness_check_name, expected_type=type_hints["readiness_check_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "readiness_check_arn": readiness_check_arn,
            "readiness_check_name": readiness_check_name,
        }

    @builtins.property
    def readiness_check_arn(self) -> builtins.str:
        '''The ARN of the ReadinessCheck resource.'''
        result = self._values.get("readiness_check_arn")
        assert result is not None, "Required property 'readiness_check_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def readiness_check_name(self) -> builtins.str:
        '''The ReadinessCheckName of the ReadinessCheck resource.'''
        result = self._values.get("readiness_check_name")
        assert result is not None, "Required property 'readiness_check_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReadinessCheckReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoveryreadiness.RecoveryGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "recovery_group_arn": "recoveryGroupArn",
        "recovery_group_name": "recoveryGroupName",
    },
)
class RecoveryGroupReference:
    def __init__(
        self,
        *,
        recovery_group_arn: builtins.str,
        recovery_group_name: builtins.str,
    ) -> None:
        '''A reference to a RecoveryGroup resource.

        :param recovery_group_arn: The ARN of the RecoveryGroup resource.
        :param recovery_group_name: The RecoveryGroupName of the RecoveryGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53recoveryreadiness as interfaces_route53recoveryreadiness
            
            recovery_group_reference = interfaces_route53recoveryreadiness.RecoveryGroupReference(
                recovery_group_arn="recoveryGroupArn",
                recovery_group_name="recoveryGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae4f9cd7795ce2da436403dc23261ff1b1339f52c7afd8110fd87e2194ebcc8b)
            check_type(argname="argument recovery_group_arn", value=recovery_group_arn, expected_type=type_hints["recovery_group_arn"])
            check_type(argname="argument recovery_group_name", value=recovery_group_name, expected_type=type_hints["recovery_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "recovery_group_arn": recovery_group_arn,
            "recovery_group_name": recovery_group_name,
        }

    @builtins.property
    def recovery_group_arn(self) -> builtins.str:
        '''The ARN of the RecoveryGroup resource.'''
        result = self._values.get("recovery_group_arn")
        assert result is not None, "Required property 'recovery_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recovery_group_name(self) -> builtins.str:
        '''The RecoveryGroupName of the RecoveryGroup resource.'''
        result = self._values.get("recovery_group_name")
        assert result is not None, "Required property 'recovery_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecoveryGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoveryreadiness.ResourceSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "resource_set_arn": "resourceSetArn",
        "resource_set_name": "resourceSetName",
    },
)
class ResourceSetReference:
    def __init__(
        self,
        *,
        resource_set_arn: builtins.str,
        resource_set_name: builtins.str,
    ) -> None:
        '''A reference to a ResourceSet resource.

        :param resource_set_arn: The ARN of the ResourceSet resource.
        :param resource_set_name: The ResourceSetName of the ResourceSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53recoveryreadiness as interfaces_route53recoveryreadiness
            
            resource_set_reference = interfaces_route53recoveryreadiness.ResourceSetReference(
                resource_set_arn="resourceSetArn",
                resource_set_name="resourceSetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__901ceac13d97a7fd218012e01dbcce75535cff01938b14ed8d55fab25c745760)
            check_type(argname="argument resource_set_arn", value=resource_set_arn, expected_type=type_hints["resource_set_arn"])
            check_type(argname="argument resource_set_name", value=resource_set_name, expected_type=type_hints["resource_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_set_arn": resource_set_arn,
            "resource_set_name": resource_set_name,
        }

    @builtins.property
    def resource_set_arn(self) -> builtins.str:
        '''The ARN of the ResourceSet resource.'''
        result = self._values.get("resource_set_arn")
        assert result is not None, "Required property 'resource_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_set_name(self) -> builtins.str:
        '''The ResourceSetName of the ResourceSet resource.'''
        result = self._values.get("resource_set_name")
        assert result is not None, "Required property 'resource_set_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CellReference",
    "ICellRef",
    "IReadinessCheckRef",
    "IRecoveryGroupRef",
    "IResourceSetRef",
    "ReadinessCheckReference",
    "RecoveryGroupReference",
    "ResourceSetReference",
]

publication.publish()

def _typecheckingstub__e358b8991d80ff68622d3a3d32622a01159eebcb8a6c0f34ffa360e940931bce(
    *,
    cell_arn: builtins.str,
    cell_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bececdbdce22a5416f98f7c557e0fa4672dfae0f84db728756dacc691f3616b2(
    *,
    readiness_check_arn: builtins.str,
    readiness_check_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae4f9cd7795ce2da436403dc23261ff1b1339f52c7afd8110fd87e2194ebcc8b(
    *,
    recovery_group_arn: builtins.str,
    recovery_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901ceac13d97a7fd218012e01dbcce75535cff01938b14ed8d55fab25c745760(
    *,
    resource_set_arn: builtins.str,
    resource_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICellRef, IReadinessCheckRef, IRecoveryGroupRef, IResourceSetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
