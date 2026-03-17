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
    jsii_type="aws-cdk-lib.interfaces.aws_s3.AccessGrantReference",
    jsii_struct_bases=[],
    name_mapping={
        "access_grant_arn": "accessGrantArn",
        "access_grant_id": "accessGrantId",
    },
)
class AccessGrantReference:
    def __init__(
        self,
        *,
        access_grant_arn: builtins.str,
        access_grant_id: builtins.str,
    ) -> None:
        '''A reference to a AccessGrant resource.

        :param access_grant_arn: The ARN of the AccessGrant resource.
        :param access_grant_id: The AccessGrantId of the AccessGrant resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            access_grant_reference = interfaces_s3.AccessGrantReference(
                access_grant_arn="accessGrantArn",
                access_grant_id="accessGrantId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2b9d960ce14e960f08458c9ac22e2b78d14384f82fbd6476384932f77dbc8cf)
            check_type(argname="argument access_grant_arn", value=access_grant_arn, expected_type=type_hints["access_grant_arn"])
            check_type(argname="argument access_grant_id", value=access_grant_id, expected_type=type_hints["access_grant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_grant_arn": access_grant_arn,
            "access_grant_id": access_grant_id,
        }

    @builtins.property
    def access_grant_arn(self) -> builtins.str:
        '''The ARN of the AccessGrant resource.'''
        result = self._values.get("access_grant_arn")
        assert result is not None, "Required property 'access_grant_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_grant_id(self) -> builtins.str:
        '''The AccessGrantId of the AccessGrant resource.'''
        result = self._values.get("access_grant_id")
        assert result is not None, "Required property 'access_grant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGrantReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3.AccessGrantsInstanceReference",
    jsii_struct_bases=[],
    name_mapping={"access_grants_instance_arn": "accessGrantsInstanceArn"},
)
class AccessGrantsInstanceReference:
    def __init__(self, *, access_grants_instance_arn: builtins.str) -> None:
        '''A reference to a AccessGrantsInstance resource.

        :param access_grants_instance_arn: The AccessGrantsInstanceArn of the AccessGrantsInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            access_grants_instance_reference = interfaces_s3.AccessGrantsInstanceReference(
                access_grants_instance_arn="accessGrantsInstanceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6882e22550c905206235673e76562dae233a359ecba7d4a358b594f17e669437)
            check_type(argname="argument access_grants_instance_arn", value=access_grants_instance_arn, expected_type=type_hints["access_grants_instance_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_grants_instance_arn": access_grants_instance_arn,
        }

    @builtins.property
    def access_grants_instance_arn(self) -> builtins.str:
        '''The AccessGrantsInstanceArn of the AccessGrantsInstance resource.'''
        result = self._values.get("access_grants_instance_arn")
        assert result is not None, "Required property 'access_grants_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGrantsInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3.AccessGrantsLocationReference",
    jsii_struct_bases=[],
    name_mapping={
        "access_grants_location_arn": "accessGrantsLocationArn",
        "access_grants_location_id": "accessGrantsLocationId",
    },
)
class AccessGrantsLocationReference:
    def __init__(
        self,
        *,
        access_grants_location_arn: builtins.str,
        access_grants_location_id: builtins.str,
    ) -> None:
        '''A reference to a AccessGrantsLocation resource.

        :param access_grants_location_arn: The ARN of the AccessGrantsLocation resource.
        :param access_grants_location_id: The AccessGrantsLocationId of the AccessGrantsLocation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            access_grants_location_reference = interfaces_s3.AccessGrantsLocationReference(
                access_grants_location_arn="accessGrantsLocationArn",
                access_grants_location_id="accessGrantsLocationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0b00f27a86590451e707e5f9757bcdd3bfbbc7e059e60a4d272b8f3522770cc)
            check_type(argname="argument access_grants_location_arn", value=access_grants_location_arn, expected_type=type_hints["access_grants_location_arn"])
            check_type(argname="argument access_grants_location_id", value=access_grants_location_id, expected_type=type_hints["access_grants_location_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_grants_location_arn": access_grants_location_arn,
            "access_grants_location_id": access_grants_location_id,
        }

    @builtins.property
    def access_grants_location_arn(self) -> builtins.str:
        '''The ARN of the AccessGrantsLocation resource.'''
        result = self._values.get("access_grants_location_arn")
        assert result is not None, "Required property 'access_grants_location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_grants_location_id(self) -> builtins.str:
        '''The AccessGrantsLocationId of the AccessGrantsLocation resource.'''
        result = self._values.get("access_grants_location_id")
        assert result is not None, "Required property 'access_grants_location_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessGrantsLocationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3.AccessPointReference",
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
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            access_point_reference = interfaces_s3.AccessPointReference(
                access_point_arn="accessPointArn",
                access_point_name="accessPointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70bc662d8702c2672c8da085db71b2c5a2f5ee3a7194eef2874c223c0294491c)
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
    jsii_type="aws-cdk-lib.interfaces.aws_s3.BucketPolicyReference",
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
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            bucket_policy_reference = interfaces_s3.BucketPolicyReference(
                bucket="bucket"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__648001e44782b37217f2dad0940d8392cd3a2df9ae248c11eafad2237b8432c1)
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
    jsii_type="aws-cdk-lib.interfaces.aws_s3.BucketReference",
    jsii_struct_bases=[],
    name_mapping={"bucket_arn": "bucketArn", "bucket_name": "bucketName"},
)
class BucketReference:
    def __init__(self, *, bucket_arn: builtins.str, bucket_name: builtins.str) -> None:
        '''A reference to a Bucket resource.

        :param bucket_arn: The ARN of the Bucket resource.
        :param bucket_name: The BucketName of the Bucket resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            bucket_reference = interfaces_s3.BucketReference(
                bucket_arn="bucketArn",
                bucket_name="bucketName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c390862ed887d712b51bf2a68505e2d7c3438e2ed55aefc40c7d935daca5c7e5)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "bucket_name": bucket_name,
        }

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''The ARN of the Bucket resource.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The BucketName of the Bucket resource.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BucketReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3.IAccessGrantRef")
class IAccessGrantRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessGrant.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessGrantRef")
    def access_grant_ref(self) -> "AccessGrantReference":
        '''(experimental) A reference to a AccessGrant resource.

        :stability: experimental
        '''
        ...


class _IAccessGrantRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessGrant.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IAccessGrantRef"

    @builtins.property
    @jsii.member(jsii_name="accessGrantRef")
    def access_grant_ref(self) -> "AccessGrantReference":
        '''(experimental) A reference to a AccessGrant resource.

        :stability: experimental
        '''
        return typing.cast("AccessGrantReference", jsii.get(self, "accessGrantRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessGrantRef).__jsii_proxy_class__ = lambda : _IAccessGrantRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3.IAccessGrantsInstanceRef")
class IAccessGrantsInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessGrantsInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessGrantsInstanceRef")
    def access_grants_instance_ref(self) -> "AccessGrantsInstanceReference":
        '''(experimental) A reference to a AccessGrantsInstance resource.

        :stability: experimental
        '''
        ...


class _IAccessGrantsInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessGrantsInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IAccessGrantsInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="accessGrantsInstanceRef")
    def access_grants_instance_ref(self) -> "AccessGrantsInstanceReference":
        '''(experimental) A reference to a AccessGrantsInstance resource.

        :stability: experimental
        '''
        return typing.cast("AccessGrantsInstanceReference", jsii.get(self, "accessGrantsInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessGrantsInstanceRef).__jsii_proxy_class__ = lambda : _IAccessGrantsInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3.IAccessGrantsLocationRef")
class IAccessGrantsLocationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessGrantsLocation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessGrantsLocationRef")
    def access_grants_location_ref(self) -> "AccessGrantsLocationReference":
        '''(experimental) A reference to a AccessGrantsLocation resource.

        :stability: experimental
        '''
        ...


class _IAccessGrantsLocationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessGrantsLocation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IAccessGrantsLocationRef"

    @builtins.property
    @jsii.member(jsii_name="accessGrantsLocationRef")
    def access_grants_location_ref(self) -> "AccessGrantsLocationReference":
        '''(experimental) A reference to a AccessGrantsLocation resource.

        :stability: experimental
        '''
        return typing.cast("AccessGrantsLocationReference", jsii.get(self, "accessGrantsLocationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessGrantsLocationRef).__jsii_proxy_class__ = lambda : _IAccessGrantsLocationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3.IAccessPointRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IAccessPointRef"

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "AccessPointReference":
        '''(experimental) A reference to a AccessPoint resource.

        :stability: experimental
        '''
        return typing.cast("AccessPointReference", jsii.get(self, "accessPointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPointRef).__jsii_proxy_class__ = lambda : _IAccessPointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3.IBucketPolicyRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IBucketPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="bucketPolicyRef")
    def bucket_policy_ref(self) -> "BucketPolicyReference":
        '''(experimental) A reference to a BucketPolicy resource.

        :stability: experimental
        '''
        return typing.cast("BucketPolicyReference", jsii.get(self, "bucketPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBucketPolicyRef).__jsii_proxy_class__ = lambda : _IBucketPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3.IBucketRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IBucketRef"

    @builtins.property
    @jsii.member(jsii_name="bucketRef")
    def bucket_ref(self) -> "BucketReference":
        '''(experimental) A reference to a Bucket resource.

        :stability: experimental
        '''
        return typing.cast("BucketReference", jsii.get(self, "bucketRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBucketRef).__jsii_proxy_class__ = lambda : _IBucketRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_s3.IMultiRegionAccessPointPolicyRef"
)
class IMultiRegionAccessPointPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MultiRegionAccessPointPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="multiRegionAccessPointPolicyRef")
    def multi_region_access_point_policy_ref(
        self,
    ) -> "MultiRegionAccessPointPolicyReference":
        '''(experimental) A reference to a MultiRegionAccessPointPolicy resource.

        :stability: experimental
        '''
        ...


class _IMultiRegionAccessPointPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MultiRegionAccessPointPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IMultiRegionAccessPointPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="multiRegionAccessPointPolicyRef")
    def multi_region_access_point_policy_ref(
        self,
    ) -> "MultiRegionAccessPointPolicyReference":
        '''(experimental) A reference to a MultiRegionAccessPointPolicy resource.

        :stability: experimental
        '''
        return typing.cast("MultiRegionAccessPointPolicyReference", jsii.get(self, "multiRegionAccessPointPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMultiRegionAccessPointPolicyRef).__jsii_proxy_class__ = lambda : _IMultiRegionAccessPointPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3.IMultiRegionAccessPointRef")
class IMultiRegionAccessPointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MultiRegionAccessPoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="multiRegionAccessPointRef")
    def multi_region_access_point_ref(self) -> "MultiRegionAccessPointReference":
        '''(experimental) A reference to a MultiRegionAccessPoint resource.

        :stability: experimental
        '''
        ...


class _IMultiRegionAccessPointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MultiRegionAccessPoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IMultiRegionAccessPointRef"

    @builtins.property
    @jsii.member(jsii_name="multiRegionAccessPointRef")
    def multi_region_access_point_ref(self) -> "MultiRegionAccessPointReference":
        '''(experimental) A reference to a MultiRegionAccessPoint resource.

        :stability: experimental
        '''
        return typing.cast("MultiRegionAccessPointReference", jsii.get(self, "multiRegionAccessPointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMultiRegionAccessPointRef).__jsii_proxy_class__ = lambda : _IMultiRegionAccessPointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3.IStorageLensGroupRef")
class IStorageLensGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StorageLensGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="storageLensGroupRef")
    def storage_lens_group_ref(self) -> "StorageLensGroupReference":
        '''(experimental) A reference to a StorageLensGroup resource.

        :stability: experimental
        '''
        ...


class _IStorageLensGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StorageLensGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IStorageLensGroupRef"

    @builtins.property
    @jsii.member(jsii_name="storageLensGroupRef")
    def storage_lens_group_ref(self) -> "StorageLensGroupReference":
        '''(experimental) A reference to a StorageLensGroup resource.

        :stability: experimental
        '''
        return typing.cast("StorageLensGroupReference", jsii.get(self, "storageLensGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStorageLensGroupRef).__jsii_proxy_class__ = lambda : _IStorageLensGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3.IStorageLensRef")
class IStorageLensRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StorageLens.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="storageLensRef")
    def storage_lens_ref(self) -> "StorageLensReference":
        '''(experimental) A reference to a StorageLens resource.

        :stability: experimental
        '''
        ...


class _IStorageLensRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StorageLens.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3.IStorageLensRef"

    @builtins.property
    @jsii.member(jsii_name="storageLensRef")
    def storage_lens_ref(self) -> "StorageLensReference":
        '''(experimental) A reference to a StorageLens resource.

        :stability: experimental
        '''
        return typing.cast("StorageLensReference", jsii.get(self, "storageLensRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStorageLensRef).__jsii_proxy_class__ = lambda : _IStorageLensRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3.MultiRegionAccessPointPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"mrap_name": "mrapName"},
)
class MultiRegionAccessPointPolicyReference:
    def __init__(self, *, mrap_name: builtins.str) -> None:
        '''A reference to a MultiRegionAccessPointPolicy resource.

        :param mrap_name: The MrapName of the MultiRegionAccessPointPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            multi_region_access_point_policy_reference = interfaces_s3.MultiRegionAccessPointPolicyReference(
                mrap_name="mrapName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83698ccd203d7ef0aaeaede8ccc9068d56382ec5d05eba2f67bb5b98e53b201d)
            check_type(argname="argument mrap_name", value=mrap_name, expected_type=type_hints["mrap_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mrap_name": mrap_name,
        }

    @builtins.property
    def mrap_name(self) -> builtins.str:
        '''The MrapName of the MultiRegionAccessPointPolicy resource.'''
        result = self._values.get("mrap_name")
        assert result is not None, "Required property 'mrap_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultiRegionAccessPointPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3.MultiRegionAccessPointReference",
    jsii_struct_bases=[],
    name_mapping={"multi_region_access_point_name": "multiRegionAccessPointName"},
)
class MultiRegionAccessPointReference:
    def __init__(self, *, multi_region_access_point_name: builtins.str) -> None:
        '''A reference to a MultiRegionAccessPoint resource.

        :param multi_region_access_point_name: The Name of the MultiRegionAccessPoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            multi_region_access_point_reference = interfaces_s3.MultiRegionAccessPointReference(
                multi_region_access_point_name="multiRegionAccessPointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6c8b17851d17a7c93d55c2b7eaa2f77a8f92c96887adecbf9996904e252221e)
            check_type(argname="argument multi_region_access_point_name", value=multi_region_access_point_name, expected_type=type_hints["multi_region_access_point_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "multi_region_access_point_name": multi_region_access_point_name,
        }

    @builtins.property
    def multi_region_access_point_name(self) -> builtins.str:
        '''The Name of the MultiRegionAccessPoint resource.'''
        result = self._values.get("multi_region_access_point_name")
        assert result is not None, "Required property 'multi_region_access_point_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultiRegionAccessPointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3.StorageLensGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "storage_lens_group_arn": "storageLensGroupArn",
        "storage_lens_group_name": "storageLensGroupName",
    },
)
class StorageLensGroupReference:
    def __init__(
        self,
        *,
        storage_lens_group_arn: builtins.str,
        storage_lens_group_name: builtins.str,
    ) -> None:
        '''A reference to a StorageLensGroup resource.

        :param storage_lens_group_arn: The ARN of the StorageLensGroup resource.
        :param storage_lens_group_name: The Name of the StorageLensGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            storage_lens_group_reference = interfaces_s3.StorageLensGroupReference(
                storage_lens_group_arn="storageLensGroupArn",
                storage_lens_group_name="storageLensGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99bdd92fd550c1ad5d4db9a599187e4998a22d114151485e67bcf0c0c70fa9a)
            check_type(argname="argument storage_lens_group_arn", value=storage_lens_group_arn, expected_type=type_hints["storage_lens_group_arn"])
            check_type(argname="argument storage_lens_group_name", value=storage_lens_group_name, expected_type=type_hints["storage_lens_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_lens_group_arn": storage_lens_group_arn,
            "storage_lens_group_name": storage_lens_group_name,
        }

    @builtins.property
    def storage_lens_group_arn(self) -> builtins.str:
        '''The ARN of the StorageLensGroup resource.'''
        result = self._values.get("storage_lens_group_arn")
        assert result is not None, "Required property 'storage_lens_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_lens_group_name(self) -> builtins.str:
        '''The Name of the StorageLensGroup resource.'''
        result = self._values.get("storage_lens_group_name")
        assert result is not None, "Required property 'storage_lens_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageLensGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3.StorageLensReference",
    jsii_struct_bases=[],
    name_mapping={"storage_lens_id": "storageLensId"},
)
class StorageLensReference:
    def __init__(self, *, storage_lens_id: builtins.str) -> None:
        '''A reference to a StorageLens resource.

        :param storage_lens_id: The StorageLensConfiguration/Id of the StorageLens resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3 as interfaces_s3
            
            storage_lens_reference = interfaces_s3.StorageLensReference(
                storage_lens_id="storageLensId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48afede48fab0fc852739a5bf1354f8c3adb42f983e3f8b4a4c446a1bcc765a9)
            check_type(argname="argument storage_lens_id", value=storage_lens_id, expected_type=type_hints["storage_lens_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_lens_id": storage_lens_id,
        }

    @builtins.property
    def storage_lens_id(self) -> builtins.str:
        '''The StorageLensConfiguration/Id of the StorageLens resource.'''
        result = self._values.get("storage_lens_id")
        assert result is not None, "Required property 'storage_lens_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageLensReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessGrantReference",
    "AccessGrantsInstanceReference",
    "AccessGrantsLocationReference",
    "AccessPointReference",
    "BucketPolicyReference",
    "BucketReference",
    "IAccessGrantRef",
    "IAccessGrantsInstanceRef",
    "IAccessGrantsLocationRef",
    "IAccessPointRef",
    "IBucketPolicyRef",
    "IBucketRef",
    "IMultiRegionAccessPointPolicyRef",
    "IMultiRegionAccessPointRef",
    "IStorageLensGroupRef",
    "IStorageLensRef",
    "MultiRegionAccessPointPolicyReference",
    "MultiRegionAccessPointReference",
    "StorageLensGroupReference",
    "StorageLensReference",
]

publication.publish()

def _typecheckingstub__d2b9d960ce14e960f08458c9ac22e2b78d14384f82fbd6476384932f77dbc8cf(
    *,
    access_grant_arn: builtins.str,
    access_grant_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6882e22550c905206235673e76562dae233a359ecba7d4a358b594f17e669437(
    *,
    access_grants_instance_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b00f27a86590451e707e5f9757bcdd3bfbbc7e059e60a4d272b8f3522770cc(
    *,
    access_grants_location_arn: builtins.str,
    access_grants_location_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70bc662d8702c2672c8da085db71b2c5a2f5ee3a7194eef2874c223c0294491c(
    *,
    access_point_arn: builtins.str,
    access_point_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__648001e44782b37217f2dad0940d8392cd3a2df9ae248c11eafad2237b8432c1(
    *,
    bucket: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c390862ed887d712b51bf2a68505e2d7c3438e2ed55aefc40c7d935daca5c7e5(
    *,
    bucket_arn: builtins.str,
    bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83698ccd203d7ef0aaeaede8ccc9068d56382ec5d05eba2f67bb5b98e53b201d(
    *,
    mrap_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6c8b17851d17a7c93d55c2b7eaa2f77a8f92c96887adecbf9996904e252221e(
    *,
    multi_region_access_point_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99bdd92fd550c1ad5d4db9a599187e4998a22d114151485e67bcf0c0c70fa9a(
    *,
    storage_lens_group_arn: builtins.str,
    storage_lens_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48afede48fab0fc852739a5bf1354f8c3adb42f983e3f8b4a4c446a1bcc765a9(
    *,
    storage_lens_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessGrantRef, IAccessGrantsInstanceRef, IAccessGrantsLocationRef, IAccessPointRef, IBucketPolicyRef, IBucketRef, IMultiRegionAccessPointPolicyRef, IMultiRegionAccessPointRef, IStorageLensGroupRef, IStorageLensRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
