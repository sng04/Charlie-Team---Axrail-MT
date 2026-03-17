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
    jsii_type="aws-cdk-lib.interfaces.aws_s3express.AccessPointReference",
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
            from aws_cdk.interfaces import aws_s3express as interfaces_s3express
            
            access_point_reference = interfaces_s3express.AccessPointReference(
                access_point_arn="accessPointArn",
                access_point_name="accessPointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eb085e56bc68e5d3131ce5030da78e2ee159353ae2c8ce481b7dc5ba1655d05)
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3express.BucketPolicyReference",
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
            from aws_cdk.interfaces import aws_s3express as interfaces_s3express
            
            bucket_policy_reference = interfaces_s3express.BucketPolicyReference(
                bucket="bucket"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e686e7abdd45aed4db358b05a1d1c91778357522a88e6fa6fa1328bae08d9498)
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
    jsii_type="aws-cdk-lib.interfaces.aws_s3express.DirectoryBucketReference",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "directory_bucket_arn": "directoryBucketArn",
    },
)
class DirectoryBucketReference:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        directory_bucket_arn: builtins.str,
    ) -> None:
        '''A reference to a DirectoryBucket resource.

        :param bucket_name: The BucketName of the DirectoryBucket resource.
        :param directory_bucket_arn: The ARN of the DirectoryBucket resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3express as interfaces_s3express
            
            directory_bucket_reference = interfaces_s3express.DirectoryBucketReference(
                bucket_name="bucketName",
                directory_bucket_arn="directoryBucketArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80a070b2a63fef6757c9e6a31c46cd8b63cc246084f59e36aa783585d69f07c4)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument directory_bucket_arn", value=directory_bucket_arn, expected_type=type_hints["directory_bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
            "directory_bucket_arn": directory_bucket_arn,
        }

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The BucketName of the DirectoryBucket resource.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_bucket_arn(self) -> builtins.str:
        '''The ARN of the DirectoryBucket resource.'''
        result = self._values.get("directory_bucket_arn")
        assert result is not None, "Required property 'directory_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectoryBucketReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3express.IAccessPointRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3express.IAccessPointRef"

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "AccessPointReference":
        '''(experimental) A reference to a AccessPoint resource.

        :stability: experimental
        '''
        return typing.cast("AccessPointReference", jsii.get(self, "accessPointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPointRef).__jsii_proxy_class__ = lambda : _IAccessPointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3express.IBucketPolicyRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3express.IBucketPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="bucketPolicyRef")
    def bucket_policy_ref(self) -> "BucketPolicyReference":
        '''(experimental) A reference to a BucketPolicy resource.

        :stability: experimental
        '''
        return typing.cast("BucketPolicyReference", jsii.get(self, "bucketPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBucketPolicyRef).__jsii_proxy_class__ = lambda : _IBucketPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3express.IDirectoryBucketRef")
class IDirectoryBucketRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DirectoryBucket.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="directoryBucketRef")
    def directory_bucket_ref(self) -> "DirectoryBucketReference":
        '''(experimental) A reference to a DirectoryBucket resource.

        :stability: experimental
        '''
        ...


class _IDirectoryBucketRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DirectoryBucket.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3express.IDirectoryBucketRef"

    @builtins.property
    @jsii.member(jsii_name="directoryBucketRef")
    def directory_bucket_ref(self) -> "DirectoryBucketReference":
        '''(experimental) A reference to a DirectoryBucket resource.

        :stability: experimental
        '''
        return typing.cast("DirectoryBucketReference", jsii.get(self, "directoryBucketRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDirectoryBucketRef).__jsii_proxy_class__ = lambda : _IDirectoryBucketRefProxy


__all__ = [
    "AccessPointReference",
    "BucketPolicyReference",
    "DirectoryBucketReference",
    "IAccessPointRef",
    "IBucketPolicyRef",
    "IDirectoryBucketRef",
]

publication.publish()

def _typecheckingstub__8eb085e56bc68e5d3131ce5030da78e2ee159353ae2c8ce481b7dc5ba1655d05(
    *,
    access_point_arn: builtins.str,
    access_point_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e686e7abdd45aed4db358b05a1d1c91778357522a88e6fa6fa1328bae08d9498(
    *,
    bucket: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80a070b2a63fef6757c9e6a31c46cd8b63cc246084f59e36aa783585d69f07c4(
    *,
    bucket_name: builtins.str,
    directory_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessPointRef, IBucketPolicyRef, IDirectoryBucketRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
