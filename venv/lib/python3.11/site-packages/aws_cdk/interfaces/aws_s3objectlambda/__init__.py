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
    jsii_type="aws-cdk-lib.interfaces.aws_s3objectlambda.AccessPointPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"object_lambda_access_point": "objectLambdaAccessPoint"},
)
class AccessPointPolicyReference:
    def __init__(self, *, object_lambda_access_point: builtins.str) -> None:
        '''A reference to a AccessPointPolicy resource.

        :param object_lambda_access_point: The ObjectLambdaAccessPoint of the AccessPointPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3objectlambda as interfaces_s3objectlambda
            
            access_point_policy_reference = interfaces_s3objectlambda.AccessPointPolicyReference(
                object_lambda_access_point="objectLambdaAccessPoint"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__909a661757d989e0befef656781ae2b5e97361787fabf9a767ed6ec028d9caa2)
            check_type(argname="argument object_lambda_access_point", value=object_lambda_access_point, expected_type=type_hints["object_lambda_access_point"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "object_lambda_access_point": object_lambda_access_point,
        }

    @builtins.property
    def object_lambda_access_point(self) -> builtins.str:
        '''The ObjectLambdaAccessPoint of the AccessPointPolicy resource.'''
        result = self._values.get("object_lambda_access_point")
        assert result is not None, "Required property 'object_lambda_access_point' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPointPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3objectlambda.AccessPointReference",
    jsii_struct_bases=[],
    name_mapping={
        "access_point_arn": "accessPointArn",
        "access_point_name": "accessPointName",
    },
)
class AccessPointReference:
    def __init__(
        self,
        *,
        access_point_arn: builtins.str,
        access_point_name: builtins.str,
    ) -> None:
        '''A reference to a AccessPoint resource.

        :param access_point_arn: The ARN of the AccessPoint resource.
        :param access_point_name: The Name of the AccessPoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3objectlambda as interfaces_s3objectlambda
            
            access_point_reference = interfaces_s3objectlambda.AccessPointReference(
                access_point_arn="accessPointArn",
                access_point_name="accessPointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b16c8e6440e9841e7612789b0a7521eb3e03486c4222cf27a954c084bdb95bd7)
            check_type(argname="argument access_point_arn", value=access_point_arn, expected_type=type_hints["access_point_arn"])
            check_type(argname="argument access_point_name", value=access_point_name, expected_type=type_hints["access_point_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_point_arn": access_point_arn,
            "access_point_name": access_point_name,
        }

    @builtins.property
    def access_point_arn(self) -> builtins.str:
        '''The ARN of the AccessPoint resource.'''
        result = self._values.get("access_point_arn")
        assert result is not None, "Required property 'access_point_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_point_name(self) -> builtins.str:
        '''The Name of the AccessPoint resource.'''
        result = self._values.get("access_point_name")
        assert result is not None, "Required property 'access_point_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_s3objectlambda.IAccessPointPolicyRef"
)
class IAccessPointPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPointPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessPointPolicyRef")
    def access_point_policy_ref(self) -> "AccessPointPolicyReference":
        '''(experimental) A reference to a AccessPointPolicy resource.

        :stability: experimental
        '''
        ...


class _IAccessPointPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPointPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3objectlambda.IAccessPointPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="accessPointPolicyRef")
    def access_point_policy_ref(self) -> "AccessPointPolicyReference":
        '''(experimental) A reference to a AccessPointPolicy resource.

        :stability: experimental
        '''
        return typing.cast("AccessPointPolicyReference", jsii.get(self, "accessPointPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPointPolicyRef).__jsii_proxy_class__ = lambda : _IAccessPointPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3objectlambda.IAccessPointRef")
class IAccessPointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "AccessPointReference":
        '''(experimental) A reference to a AccessPoint resource.

        :stability: experimental
        '''
        ...


class _IAccessPointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3objectlambda.IAccessPointRef"

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "AccessPointReference":
        '''(experimental) A reference to a AccessPoint resource.

        :stability: experimental
        '''
        return typing.cast("AccessPointReference", jsii.get(self, "accessPointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPointRef).__jsii_proxy_class__ = lambda : _IAccessPointRefProxy


__all__ = [
    "AccessPointPolicyReference",
    "AccessPointReference",
    "IAccessPointPolicyRef",
    "IAccessPointRef",
]

publication.publish()

def _typecheckingstub__909a661757d989e0befef656781ae2b5e97361787fabf9a767ed6ec028d9caa2(
    *,
    object_lambda_access_point: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b16c8e6440e9841e7612789b0a7521eb3e03486c4222cf27a954c084bdb95bd7(
    *,
    access_point_arn: builtins.str,
    access_point_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessPointPolicyRef, IAccessPointRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
