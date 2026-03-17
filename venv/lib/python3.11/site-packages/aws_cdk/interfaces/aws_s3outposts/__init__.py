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
    jsii_type="aws-cdk-lib.interfaces.aws_s3outposts.AccessPointReference",
    jsii_struct_bases=[],
    name_mapping={"access_point_arn": "accessPointArn"},
)
class AccessPointReference:
    def __init__(self, *, access_point_arn: builtins.str) -> None:
        '''A reference to a AccessPoint resource.

        :param access_point_arn: The Arn of the AccessPoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3outposts as interfaces_s3outposts
            
            access_point_reference = interfaces_s3outposts.AccessPointReference(
                access_point_arn="accessPointArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4909cf7e4a0399664dcf214d83d3cd26820cc66f2196b79b057a75fcac5da1c5)
            check_type(argname="argument access_point_arn", value=access_point_arn, expected_type=type_hints["access_point_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_point_arn": access_point_arn,
        }

    @builtins.property
    def access_point_arn(self) -> builtins.str:
        '''The Arn of the AccessPoint resource.'''
        result = self._values.get("access_point_arn")
        assert result is not None, "Required property 'access_point_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3outposts.BucketPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket"},
)
class BucketPolicyReference:
    def __init__(self, *, bucket: builtins.str) -> None:
        '''A reference to a BucketPolicy resource.

        :param bucket: The Bucket of the BucketPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3outposts as interfaces_s3outposts
            
            bucket_policy_reference = interfaces_s3outposts.BucketPolicyReference(
                bucket="bucket"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9791e5e1b1b6b43c769ea51553ca55ec554ecbbb4c7a3bdba7f9f4bc18bca40)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }

    @builtins.property
    def bucket(self) -> builtins.str:
        '''The Bucket of the BucketPolicy resource.'''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BucketPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3outposts.BucketReference",
    jsii_struct_bases=[],
    name_mapping={"bucket_arn": "bucketArn"},
)
class BucketReference:
    def __init__(self, *, bucket_arn: builtins.str) -> None:
        '''A reference to a Bucket resource.

        :param bucket_arn: The Arn of the Bucket resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3outposts as interfaces_s3outposts
            
            bucket_reference = interfaces_s3outposts.BucketReference(
                bucket_arn="bucketArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8da3fedb3a159ae87c04a7a0dd00cd92b64e81f8d749c2d30b678f4b96c48d5)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
        }

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''The Arn of the Bucket resource.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BucketReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3outposts.EndpointReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_arn": "endpointArn"},
)
class EndpointReference:
    def __init__(self, *, endpoint_arn: builtins.str) -> None:
        '''A reference to a Endpoint resource.

        :param endpoint_arn: The Arn of the Endpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3outposts as interfaces_s3outposts
            
            endpoint_reference = interfaces_s3outposts.EndpointReference(
                endpoint_arn="endpointArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c031f3efdcb0359e74443e471c3d35e5929746fab402cc5e269d9be817976ad)
            check_type(argname="argument endpoint_arn", value=endpoint_arn, expected_type=type_hints["endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_arn": endpoint_arn,
        }

    @builtins.property
    def endpoint_arn(self) -> builtins.str:
        '''The Arn of the Endpoint resource.'''
        result = self._values.get("endpoint_arn")
        assert result is not None, "Required property 'endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3outposts.IAccessPointRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3outposts.IAccessPointRef"

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "AccessPointReference":
        '''(experimental) A reference to a AccessPoint resource.

        :stability: experimental
        '''
        return typing.cast("AccessPointReference", jsii.get(self, "accessPointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPointRef).__jsii_proxy_class__ = lambda : _IAccessPointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3outposts.IBucketPolicyRef")
class IBucketPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BucketPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="bucketPolicyRef")
    def bucket_policy_ref(self) -> "BucketPolicyReference":
        '''(experimental) A reference to a BucketPolicy resource.

        :stability: experimental
        '''
        ...


class _IBucketPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BucketPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3outposts.IBucketPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="bucketPolicyRef")
    def bucket_policy_ref(self) -> "BucketPolicyReference":
        '''(experimental) A reference to a BucketPolicy resource.

        :stability: experimental
        '''
        return typing.cast("BucketPolicyReference", jsii.get(self, "bucketPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBucketPolicyRef).__jsii_proxy_class__ = lambda : _IBucketPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3outposts.IBucketRef")
class IBucketRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Bucket.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="bucketRef")
    def bucket_ref(self) -> "BucketReference":
        '''(experimental) A reference to a Bucket resource.

        :stability: experimental
        '''
        ...


class _IBucketRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Bucket.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3outposts.IBucketRef"

    @builtins.property
    @jsii.member(jsii_name="bucketRef")
    def bucket_ref(self) -> "BucketReference":
        '''(experimental) A reference to a Bucket resource.

        :stability: experimental
        '''
        return typing.cast("BucketReference", jsii.get(self, "bucketRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBucketRef).__jsii_proxy_class__ = lambda : _IBucketRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3outposts.IEndpointRef")
class IEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        ...


class _IEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3outposts.IEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        return typing.cast("EndpointReference", jsii.get(self, "endpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointRef).__jsii_proxy_class__ = lambda : _IEndpointRefProxy


__all__ = [
    "AccessPointReference",
    "BucketPolicyReference",
    "BucketReference",
    "EndpointReference",
    "IAccessPointRef",
    "IBucketPolicyRef",
    "IBucketRef",
    "IEndpointRef",
]

publication.publish()

def _typecheckingstub__4909cf7e4a0399664dcf214d83d3cd26820cc66f2196b79b057a75fcac5da1c5(
    *,
    access_point_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9791e5e1b1b6b43c769ea51553ca55ec554ecbbb4c7a3bdba7f9f4bc18bca40(
    *,
    bucket: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8da3fedb3a159ae87c04a7a0dd00cd92b64e81f8d749c2d30b678f4b96c48d5(
    *,
    bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c031f3efdcb0359e74443e471c3d35e5929746fab402cc5e269d9be817976ad(
    *,
    endpoint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessPointRef, IBucketPolicyRef, IBucketRef, IEndpointRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
