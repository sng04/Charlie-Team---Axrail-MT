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
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.AnycastIpListReference",
    jsii_struct_bases=[],
    name_mapping={"anycast_ip_list_id": "anycastIpListId"},
)
class AnycastIpListReference:
    def __init__(self, *, anycast_ip_list_id: builtins.str) -> None:
        '''A reference to a AnycastIpList resource.

        :param anycast_ip_list_id: The Id of the AnycastIpList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            anycast_ip_list_reference = interfaces_cloudfront.AnycastIpListReference(
                anycast_ip_list_id="anycastIpListId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0935893f040727b890159b2a61c53744a19e903fa583f51fd1335094286a882)
            check_type(argname="argument anycast_ip_list_id", value=anycast_ip_list_id, expected_type=type_hints["anycast_ip_list_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "anycast_ip_list_id": anycast_ip_list_id,
        }

    @builtins.property
    def anycast_ip_list_id(self) -> builtins.str:
        '''The Id of the AnycastIpList resource.'''
        result = self._values.get("anycast_ip_list_id")
        assert result is not None, "Required property 'anycast_ip_list_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnycastIpListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.CachePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"cache_policy_id": "cachePolicyId"},
)
class CachePolicyReference:
    def __init__(self, *, cache_policy_id: builtins.str) -> None:
        '''A reference to a CachePolicy resource.

        :param cache_policy_id: The Id of the CachePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            cache_policy_reference = interfaces_cloudfront.CachePolicyReference(
                cache_policy_id="cachePolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eafc53ec8d44d91d599196eff2812b8d3e750f75445fecc22787175206a425f4)
            check_type(argname="argument cache_policy_id", value=cache_policy_id, expected_type=type_hints["cache_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cache_policy_id": cache_policy_id,
        }

    @builtins.property
    def cache_policy_id(self) -> builtins.str:
        '''The Id of the CachePolicy resource.'''
        result = self._values.get("cache_policy_id")
        assert result is not None, "Required property 'cache_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CachePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.CloudFrontOriginAccessIdentityReference",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_front_origin_access_identity_id": "cloudFrontOriginAccessIdentityId",
    },
)
class CloudFrontOriginAccessIdentityReference:
    def __init__(self, *, cloud_front_origin_access_identity_id: builtins.str) -> None:
        '''A reference to a CloudFrontOriginAccessIdentity resource.

        :param cloud_front_origin_access_identity_id: The Id of the CloudFrontOriginAccessIdentity resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            cloud_front_origin_access_identity_reference = interfaces_cloudfront.CloudFrontOriginAccessIdentityReference(
                cloud_front_origin_access_identity_id="cloudFrontOriginAccessIdentityId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac62879d2ba5cdd6aa45b9be7d13a0247d5901fc9a2cbb8b4ce248ceeae24403)
            check_type(argname="argument cloud_front_origin_access_identity_id", value=cloud_front_origin_access_identity_id, expected_type=type_hints["cloud_front_origin_access_identity_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_front_origin_access_identity_id": cloud_front_origin_access_identity_id,
        }

    @builtins.property
    def cloud_front_origin_access_identity_id(self) -> builtins.str:
        '''The Id of the CloudFrontOriginAccessIdentity resource.'''
        result = self._values.get("cloud_front_origin_access_identity_id")
        assert result is not None, "Required property 'cloud_front_origin_access_identity_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFrontOriginAccessIdentityReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.ConnectionFunctionReference",
    jsii_struct_bases=[],
    name_mapping={
        "connection_function_arn": "connectionFunctionArn",
        "connection_function_id": "connectionFunctionId",
    },
)
class ConnectionFunctionReference:
    def __init__(
        self,
        *,
        connection_function_arn: builtins.str,
        connection_function_id: builtins.str,
    ) -> None:
        '''A reference to a ConnectionFunction resource.

        :param connection_function_arn: The ARN of the ConnectionFunction resource.
        :param connection_function_id: The Id of the ConnectionFunction resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            connection_function_reference = interfaces_cloudfront.ConnectionFunctionReference(
                connection_function_arn="connectionFunctionArn",
                connection_function_id="connectionFunctionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd7b0bb64cedf15636618e6b755d87dc4aca386789f0be0876627def8997a3ad)
            check_type(argname="argument connection_function_arn", value=connection_function_arn, expected_type=type_hints["connection_function_arn"])
            check_type(argname="argument connection_function_id", value=connection_function_id, expected_type=type_hints["connection_function_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_function_arn": connection_function_arn,
            "connection_function_id": connection_function_id,
        }

    @builtins.property
    def connection_function_arn(self) -> builtins.str:
        '''The ARN of the ConnectionFunction resource.'''
        result = self._values.get("connection_function_arn")
        assert result is not None, "Required property 'connection_function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_function_id(self) -> builtins.str:
        '''The Id of the ConnectionFunction resource.'''
        result = self._values.get("connection_function_id")
        assert result is not None, "Required property 'connection_function_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionFunctionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.ConnectionGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "connection_group_arn": "connectionGroupArn",
        "connection_group_id": "connectionGroupId",
    },
)
class ConnectionGroupReference:
    def __init__(
        self,
        *,
        connection_group_arn: builtins.str,
        connection_group_id: builtins.str,
    ) -> None:
        '''A reference to a ConnectionGroup resource.

        :param connection_group_arn: The ARN of the ConnectionGroup resource.
        :param connection_group_id: The Id of the ConnectionGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            connection_group_reference = interfaces_cloudfront.ConnectionGroupReference(
                connection_group_arn="connectionGroupArn",
                connection_group_id="connectionGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03040cdfe38372fca8182c71a8a7787ed0a443239bca593242923e506cd17202)
            check_type(argname="argument connection_group_arn", value=connection_group_arn, expected_type=type_hints["connection_group_arn"])
            check_type(argname="argument connection_group_id", value=connection_group_id, expected_type=type_hints["connection_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_group_arn": connection_group_arn,
            "connection_group_id": connection_group_id,
        }

    @builtins.property
    def connection_group_arn(self) -> builtins.str:
        '''The ARN of the ConnectionGroup resource.'''
        result = self._values.get("connection_group_arn")
        assert result is not None, "Required property 'connection_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_group_id(self) -> builtins.str:
        '''The Id of the ConnectionGroup resource.'''
        result = self._values.get("connection_group_id")
        assert result is not None, "Required property 'connection_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.ContinuousDeploymentPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"continuous_deployment_policy_id": "continuousDeploymentPolicyId"},
)
class ContinuousDeploymentPolicyReference:
    def __init__(self, *, continuous_deployment_policy_id: builtins.str) -> None:
        '''A reference to a ContinuousDeploymentPolicy resource.

        :param continuous_deployment_policy_id: The Id of the ContinuousDeploymentPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            continuous_deployment_policy_reference = interfaces_cloudfront.ContinuousDeploymentPolicyReference(
                continuous_deployment_policy_id="continuousDeploymentPolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45ecf47f2529275c1a72313ada238b7dd48f33d72dcbaad3303f04dc5489a6c4)
            check_type(argname="argument continuous_deployment_policy_id", value=continuous_deployment_policy_id, expected_type=type_hints["continuous_deployment_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "continuous_deployment_policy_id": continuous_deployment_policy_id,
        }

    @builtins.property
    def continuous_deployment_policy_id(self) -> builtins.str:
        '''The Id of the ContinuousDeploymentPolicy resource.'''
        result = self._values.get("continuous_deployment_policy_id")
        assert result is not None, "Required property 'continuous_deployment_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContinuousDeploymentPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.DistributionReference",
    jsii_struct_bases=[],
    name_mapping={"distribution_id": "distributionId"},
)
class DistributionReference:
    def __init__(self, *, distribution_id: builtins.str) -> None:
        '''A reference to a Distribution resource.

        :param distribution_id: The Id of the Distribution resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            distribution_reference = interfaces_cloudfront.DistributionReference(
                distribution_id="distributionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f97cc6a786fec9feb4764e7b259ccc05ed440a2e51df2dded3b144c438636683)
            check_type(argname="argument distribution_id", value=distribution_id, expected_type=type_hints["distribution_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "distribution_id": distribution_id,
        }

    @builtins.property
    def distribution_id(self) -> builtins.str:
        '''The Id of the Distribution resource.'''
        result = self._values.get("distribution_id")
        assert result is not None, "Required property 'distribution_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.DistributionTenantReference",
    jsii_struct_bases=[],
    name_mapping={
        "distribution_tenant_arn": "distributionTenantArn",
        "distribution_tenant_id": "distributionTenantId",
    },
)
class DistributionTenantReference:
    def __init__(
        self,
        *,
        distribution_tenant_arn: builtins.str,
        distribution_tenant_id: builtins.str,
    ) -> None:
        '''A reference to a DistributionTenant resource.

        :param distribution_tenant_arn: The ARN of the DistributionTenant resource.
        :param distribution_tenant_id: The Id of the DistributionTenant resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            distribution_tenant_reference = interfaces_cloudfront.DistributionTenantReference(
                distribution_tenant_arn="distributionTenantArn",
                distribution_tenant_id="distributionTenantId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d850f4f750196ae341c242dc801ed452e2f72f450f61ca0bec654fc3744e247)
            check_type(argname="argument distribution_tenant_arn", value=distribution_tenant_arn, expected_type=type_hints["distribution_tenant_arn"])
            check_type(argname="argument distribution_tenant_id", value=distribution_tenant_id, expected_type=type_hints["distribution_tenant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "distribution_tenant_arn": distribution_tenant_arn,
            "distribution_tenant_id": distribution_tenant_id,
        }

    @builtins.property
    def distribution_tenant_arn(self) -> builtins.str:
        '''The ARN of the DistributionTenant resource.'''
        result = self._values.get("distribution_tenant_arn")
        assert result is not None, "Required property 'distribution_tenant_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def distribution_tenant_id(self) -> builtins.str:
        '''The Id of the DistributionTenant resource.'''
        result = self._values.get("distribution_tenant_id")
        assert result is not None, "Required property 'distribution_tenant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributionTenantReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.FunctionReference",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class FunctionReference:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''A reference to a Function resource.

        :param function_arn: The FunctionARN of the Function resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            function_reference = interfaces_cloudfront.FunctionReference(
                function_arn="functionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32506104c4cd233c3476b42913670893c3370f22bfb6aca3a771d89e4c4cd669)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''The FunctionARN of the Function resource.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IAnycastIpListRef")
class IAnycastIpListRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AnycastIpList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="anycastIpListRef")
    def anycast_ip_list_ref(self) -> "AnycastIpListReference":
        '''(experimental) A reference to a AnycastIpList resource.

        :stability: experimental
        '''
        ...


class _IAnycastIpListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AnycastIpList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IAnycastIpListRef"

    @builtins.property
    @jsii.member(jsii_name="anycastIpListRef")
    def anycast_ip_list_ref(self) -> "AnycastIpListReference":
        '''(experimental) A reference to a AnycastIpList resource.

        :stability: experimental
        '''
        return typing.cast("AnycastIpListReference", jsii.get(self, "anycastIpListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnycastIpListRef).__jsii_proxy_class__ = lambda : _IAnycastIpListRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.ICachePolicyRef")
class ICachePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CachePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cachePolicyRef")
    def cache_policy_ref(self) -> "CachePolicyReference":
        '''(experimental) A reference to a CachePolicy resource.

        :stability: experimental
        '''
        ...


class _ICachePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CachePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.ICachePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="cachePolicyRef")
    def cache_policy_ref(self) -> "CachePolicyReference":
        '''(experimental) A reference to a CachePolicy resource.

        :stability: experimental
        '''
        return typing.cast("CachePolicyReference", jsii.get(self, "cachePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICachePolicyRef).__jsii_proxy_class__ = lambda : _ICachePolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.ICloudFrontOriginAccessIdentityRef"
)
class ICloudFrontOriginAccessIdentityRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CloudFrontOriginAccessIdentity.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cloudFrontOriginAccessIdentityRef")
    def cloud_front_origin_access_identity_ref(
        self,
    ) -> "CloudFrontOriginAccessIdentityReference":
        '''(experimental) A reference to a CloudFrontOriginAccessIdentity resource.

        :stability: experimental
        '''
        ...


class _ICloudFrontOriginAccessIdentityRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CloudFrontOriginAccessIdentity.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.ICloudFrontOriginAccessIdentityRef"

    @builtins.property
    @jsii.member(jsii_name="cloudFrontOriginAccessIdentityRef")
    def cloud_front_origin_access_identity_ref(
        self,
    ) -> "CloudFrontOriginAccessIdentityReference":
        '''(experimental) A reference to a CloudFrontOriginAccessIdentity resource.

        :stability: experimental
        '''
        return typing.cast("CloudFrontOriginAccessIdentityReference", jsii.get(self, "cloudFrontOriginAccessIdentityRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICloudFrontOriginAccessIdentityRef).__jsii_proxy_class__ = lambda : _ICloudFrontOriginAccessIdentityRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IConnectionFunctionRef"
)
class IConnectionFunctionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectionFunction.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionFunctionRef")
    def connection_function_ref(self) -> "ConnectionFunctionReference":
        '''(experimental) A reference to a ConnectionFunction resource.

        :stability: experimental
        '''
        ...


class _IConnectionFunctionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectionFunction.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IConnectionFunctionRef"

    @builtins.property
    @jsii.member(jsii_name="connectionFunctionRef")
    def connection_function_ref(self) -> "ConnectionFunctionReference":
        '''(experimental) A reference to a ConnectionFunction resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionFunctionReference", jsii.get(self, "connectionFunctionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionFunctionRef).__jsii_proxy_class__ = lambda : _IConnectionFunctionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IConnectionGroupRef")
class IConnectionGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectionGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionGroupRef")
    def connection_group_ref(self) -> "ConnectionGroupReference":
        '''(experimental) A reference to a ConnectionGroup resource.

        :stability: experimental
        '''
        ...


class _IConnectionGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectionGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IConnectionGroupRef"

    @builtins.property
    @jsii.member(jsii_name="connectionGroupRef")
    def connection_group_ref(self) -> "ConnectionGroupReference":
        '''(experimental) A reference to a ConnectionGroup resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionGroupReference", jsii.get(self, "connectionGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionGroupRef).__jsii_proxy_class__ = lambda : _IConnectionGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IContinuousDeploymentPolicyRef"
)
class IContinuousDeploymentPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContinuousDeploymentPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="continuousDeploymentPolicyRef")
    def continuous_deployment_policy_ref(self) -> "ContinuousDeploymentPolicyReference":
        '''(experimental) A reference to a ContinuousDeploymentPolicy resource.

        :stability: experimental
        '''
        ...


class _IContinuousDeploymentPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContinuousDeploymentPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IContinuousDeploymentPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="continuousDeploymentPolicyRef")
    def continuous_deployment_policy_ref(self) -> "ContinuousDeploymentPolicyReference":
        '''(experimental) A reference to a ContinuousDeploymentPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ContinuousDeploymentPolicyReference", jsii.get(self, "continuousDeploymentPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContinuousDeploymentPolicyRef).__jsii_proxy_class__ = lambda : _IContinuousDeploymentPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IDistributionRef")
class IDistributionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Distribution.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="distributionRef")
    def distribution_ref(self) -> "DistributionReference":
        '''(experimental) A reference to a Distribution resource.

        :stability: experimental
        '''
        ...


class _IDistributionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Distribution.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IDistributionRef"

    @builtins.property
    @jsii.member(jsii_name="distributionRef")
    def distribution_ref(self) -> "DistributionReference":
        '''(experimental) A reference to a Distribution resource.

        :stability: experimental
        '''
        return typing.cast("DistributionReference", jsii.get(self, "distributionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDistributionRef).__jsii_proxy_class__ = lambda : _IDistributionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IDistributionTenantRef"
)
class IDistributionTenantRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DistributionTenant.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="distributionTenantRef")
    def distribution_tenant_ref(self) -> "DistributionTenantReference":
        '''(experimental) A reference to a DistributionTenant resource.

        :stability: experimental
        '''
        ...


class _IDistributionTenantRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DistributionTenant.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IDistributionTenantRef"

    @builtins.property
    @jsii.member(jsii_name="distributionTenantRef")
    def distribution_tenant_ref(self) -> "DistributionTenantReference":
        '''(experimental) A reference to a DistributionTenant resource.

        :stability: experimental
        '''
        return typing.cast("DistributionTenantReference", jsii.get(self, "distributionTenantRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDistributionTenantRef).__jsii_proxy_class__ = lambda : _IDistributionTenantRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IFunctionRef")
class IFunctionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Function.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="functionRef")
    def function_ref(self) -> "FunctionReference":
        '''(experimental) A reference to a Function resource.

        :stability: experimental
        '''
        ...


class _IFunctionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Function.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IFunctionRef"

    @builtins.property
    @jsii.member(jsii_name="functionRef")
    def function_ref(self) -> "FunctionReference":
        '''(experimental) A reference to a Function resource.

        :stability: experimental
        '''
        return typing.cast("FunctionReference", jsii.get(self, "functionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFunctionRef).__jsii_proxy_class__ = lambda : _IFunctionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IKeyGroupRef")
class IKeyGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a KeyGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="keyGroupRef")
    def key_group_ref(self) -> "KeyGroupReference":
        '''(experimental) A reference to a KeyGroup resource.

        :stability: experimental
        '''
        ...


class _IKeyGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a KeyGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IKeyGroupRef"

    @builtins.property
    @jsii.member(jsii_name="keyGroupRef")
    def key_group_ref(self) -> "KeyGroupReference":
        '''(experimental) A reference to a KeyGroup resource.

        :stability: experimental
        '''
        return typing.cast("KeyGroupReference", jsii.get(self, "keyGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKeyGroupRef).__jsii_proxy_class__ = lambda : _IKeyGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IKeyValueStoreRef")
class IKeyValueStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a KeyValueStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="keyValueStoreRef")
    def key_value_store_ref(self) -> "KeyValueStoreReference":
        '''(experimental) A reference to a KeyValueStore resource.

        :stability: experimental
        '''
        ...


class _IKeyValueStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a KeyValueStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IKeyValueStoreRef"

    @builtins.property
    @jsii.member(jsii_name="keyValueStoreRef")
    def key_value_store_ref(self) -> "KeyValueStoreReference":
        '''(experimental) A reference to a KeyValueStore resource.

        :stability: experimental
        '''
        return typing.cast("KeyValueStoreReference", jsii.get(self, "keyValueStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKeyValueStoreRef).__jsii_proxy_class__ = lambda : _IKeyValueStoreRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IMonitoringSubscriptionRef"
)
class IMonitoringSubscriptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MonitoringSubscription.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="monitoringSubscriptionRef")
    def monitoring_subscription_ref(self) -> "MonitoringSubscriptionReference":
        '''(experimental) A reference to a MonitoringSubscription resource.

        :stability: experimental
        '''
        ...


class _IMonitoringSubscriptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MonitoringSubscription.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IMonitoringSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="monitoringSubscriptionRef")
    def monitoring_subscription_ref(self) -> "MonitoringSubscriptionReference":
        '''(experimental) A reference to a MonitoringSubscription resource.

        :stability: experimental
        '''
        return typing.cast("MonitoringSubscriptionReference", jsii.get(self, "monitoringSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMonitoringSubscriptionRef).__jsii_proxy_class__ = lambda : _IMonitoringSubscriptionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IOriginAccessControlRef"
)
class IOriginAccessControlRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OriginAccessControl.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="originAccessControlRef")
    def origin_access_control_ref(self) -> "OriginAccessControlReference":
        '''(experimental) A reference to a OriginAccessControl resource.

        :stability: experimental
        '''
        ...


class _IOriginAccessControlRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OriginAccessControl.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IOriginAccessControlRef"

    @builtins.property
    @jsii.member(jsii_name="originAccessControlRef")
    def origin_access_control_ref(self) -> "OriginAccessControlReference":
        '''(experimental) A reference to a OriginAccessControl resource.

        :stability: experimental
        '''
        return typing.cast("OriginAccessControlReference", jsii.get(self, "originAccessControlRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOriginAccessControlRef).__jsii_proxy_class__ = lambda : _IOriginAccessControlRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IOriginRequestPolicyRef"
)
class IOriginRequestPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OriginRequestPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="originRequestPolicyRef")
    def origin_request_policy_ref(self) -> "OriginRequestPolicyReference":
        '''(experimental) A reference to a OriginRequestPolicy resource.

        :stability: experimental
        '''
        ...


class _IOriginRequestPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OriginRequestPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IOriginRequestPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="originRequestPolicyRef")
    def origin_request_policy_ref(self) -> "OriginRequestPolicyReference":
        '''(experimental) A reference to a OriginRequestPolicy resource.

        :stability: experimental
        '''
        return typing.cast("OriginRequestPolicyReference", jsii.get(self, "originRequestPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOriginRequestPolicyRef).__jsii_proxy_class__ = lambda : _IOriginRequestPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IPublicKeyRef")
class IPublicKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PublicKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="publicKeyRef")
    def public_key_ref(self) -> "PublicKeyReference":
        '''(experimental) A reference to a PublicKey resource.

        :stability: experimental
        '''
        ...


class _IPublicKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PublicKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IPublicKeyRef"

    @builtins.property
    @jsii.member(jsii_name="publicKeyRef")
    def public_key_ref(self) -> "PublicKeyReference":
        '''(experimental) A reference to a PublicKey resource.

        :stability: experimental
        '''
        return typing.cast("PublicKeyReference", jsii.get(self, "publicKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicKeyRef).__jsii_proxy_class__ = lambda : _IPublicKeyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IRealtimeLogConfigRef"
)
class IRealtimeLogConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RealtimeLogConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="realtimeLogConfigRef")
    def realtime_log_config_ref(self) -> "RealtimeLogConfigReference":
        '''(experimental) A reference to a RealtimeLogConfig resource.

        :stability: experimental
        '''
        ...


class _IRealtimeLogConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RealtimeLogConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IRealtimeLogConfigRef"

    @builtins.property
    @jsii.member(jsii_name="realtimeLogConfigRef")
    def realtime_log_config_ref(self) -> "RealtimeLogConfigReference":
        '''(experimental) A reference to a RealtimeLogConfig resource.

        :stability: experimental
        '''
        return typing.cast("RealtimeLogConfigReference", jsii.get(self, "realtimeLogConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRealtimeLogConfigRef).__jsii_proxy_class__ = lambda : _IRealtimeLogConfigRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IResponseHeadersPolicyRef"
)
class IResponseHeadersPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResponseHeadersPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="responseHeadersPolicyRef")
    def response_headers_policy_ref(self) -> "ResponseHeadersPolicyReference":
        '''(experimental) A reference to a ResponseHeadersPolicy resource.

        :stability: experimental
        '''
        ...


class _IResponseHeadersPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResponseHeadersPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IResponseHeadersPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="responseHeadersPolicyRef")
    def response_headers_policy_ref(self) -> "ResponseHeadersPolicyReference":
        '''(experimental) A reference to a ResponseHeadersPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResponseHeadersPolicyReference", jsii.get(self, "responseHeadersPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResponseHeadersPolicyRef).__jsii_proxy_class__ = lambda : _IResponseHeadersPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IStreamingDistributionRef"
)
class IStreamingDistributionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StreamingDistribution.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="streamingDistributionRef")
    def streaming_distribution_ref(self) -> "StreamingDistributionReference":
        '''(experimental) A reference to a StreamingDistribution resource.

        :stability: experimental
        '''
        ...


class _IStreamingDistributionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StreamingDistribution.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IStreamingDistributionRef"

    @builtins.property
    @jsii.member(jsii_name="streamingDistributionRef")
    def streaming_distribution_ref(self) -> "StreamingDistributionReference":
        '''(experimental) A reference to a StreamingDistribution resource.

        :stability: experimental
        '''
        return typing.cast("StreamingDistributionReference", jsii.get(self, "streamingDistributionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStreamingDistributionRef).__jsii_proxy_class__ = lambda : _IStreamingDistributionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.ITrustStoreRef")
class ITrustStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrustStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trustStoreRef")
    def trust_store_ref(self) -> "TrustStoreReference":
        '''(experimental) A reference to a TrustStore resource.

        :stability: experimental
        '''
        ...


class _ITrustStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrustStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.ITrustStoreRef"

    @builtins.property
    @jsii.member(jsii_name="trustStoreRef")
    def trust_store_ref(self) -> "TrustStoreReference":
        '''(experimental) A reference to a TrustStore resource.

        :stability: experimental
        '''
        return typing.cast("TrustStoreReference", jsii.get(self, "trustStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrustStoreRef).__jsii_proxy_class__ = lambda : _ITrustStoreRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.IVpcOriginRef")
class IVpcOriginRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VpcOrigin.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcOriginRef")
    def vpc_origin_ref(self) -> "VpcOriginReference":
        '''(experimental) A reference to a VpcOrigin resource.

        :stability: experimental
        '''
        ...


class _IVpcOriginRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VpcOrigin.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudfront.IVpcOriginRef"

    @builtins.property
    @jsii.member(jsii_name="vpcOriginRef")
    def vpc_origin_ref(self) -> "VpcOriginReference":
        '''(experimental) A reference to a VpcOrigin resource.

        :stability: experimental
        '''
        return typing.cast("VpcOriginReference", jsii.get(self, "vpcOriginRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVpcOriginRef).__jsii_proxy_class__ = lambda : _IVpcOriginRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.KeyGroupReference",
    jsii_struct_bases=[],
    name_mapping={"key_group_id": "keyGroupId"},
)
class KeyGroupReference:
    def __init__(self, *, key_group_id: builtins.str) -> None:
        '''A reference to a KeyGroup resource.

        :param key_group_id: The Id of the KeyGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            key_group_reference = interfaces_cloudfront.KeyGroupReference(
                key_group_id="keyGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__464ae77084d63c7646b271a3e37cb2e98cacce805a2d61d9f5dbdda96f46dff5)
            check_type(argname="argument key_group_id", value=key_group_id, expected_type=type_hints["key_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_group_id": key_group_id,
        }

    @builtins.property
    def key_group_id(self) -> builtins.str:
        '''The Id of the KeyGroup resource.'''
        result = self._values.get("key_group_id")
        assert result is not None, "Required property 'key_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.KeyValueStoreReference",
    jsii_struct_bases=[],
    name_mapping={
        "key_value_store_arn": "keyValueStoreArn",
        "key_value_store_name": "keyValueStoreName",
    },
)
class KeyValueStoreReference:
    def __init__(
        self,
        *,
        key_value_store_arn: builtins.str,
        key_value_store_name: builtins.str,
    ) -> None:
        '''A reference to a KeyValueStore resource.

        :param key_value_store_arn: The ARN of the KeyValueStore resource.
        :param key_value_store_name: The Name of the KeyValueStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            key_value_store_reference = interfaces_cloudfront.KeyValueStoreReference(
                key_value_store_arn="keyValueStoreArn",
                key_value_store_name="keyValueStoreName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d2ab8f161da96de4216494194339f84571b4f0f1cfe710f61f155cda66cbac5)
            check_type(argname="argument key_value_store_arn", value=key_value_store_arn, expected_type=type_hints["key_value_store_arn"])
            check_type(argname="argument key_value_store_name", value=key_value_store_name, expected_type=type_hints["key_value_store_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_value_store_arn": key_value_store_arn,
            "key_value_store_name": key_value_store_name,
        }

    @builtins.property
    def key_value_store_arn(self) -> builtins.str:
        '''The ARN of the KeyValueStore resource.'''
        result = self._values.get("key_value_store_arn")
        assert result is not None, "Required property 'key_value_store_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_value_store_name(self) -> builtins.str:
        '''The Name of the KeyValueStore resource.'''
        result = self._values.get("key_value_store_name")
        assert result is not None, "Required property 'key_value_store_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyValueStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.MonitoringSubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={"distribution_id": "distributionId"},
)
class MonitoringSubscriptionReference:
    def __init__(self, *, distribution_id: builtins.str) -> None:
        '''A reference to a MonitoringSubscription resource.

        :param distribution_id: The DistributionId of the MonitoringSubscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            monitoring_subscription_reference = interfaces_cloudfront.MonitoringSubscriptionReference(
                distribution_id="distributionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d5bb5962d3c7a0d02baa196ea6a6d69ae11b813483a64036a3f44a0ae233a1b)
            check_type(argname="argument distribution_id", value=distribution_id, expected_type=type_hints["distribution_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "distribution_id": distribution_id,
        }

    @builtins.property
    def distribution_id(self) -> builtins.str:
        '''The DistributionId of the MonitoringSubscription resource.'''
        result = self._values.get("distribution_id")
        assert result is not None, "Required property 'distribution_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitoringSubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.OriginAccessControlReference",
    jsii_struct_bases=[],
    name_mapping={"origin_access_control_id": "originAccessControlId"},
)
class OriginAccessControlReference:
    def __init__(self, *, origin_access_control_id: builtins.str) -> None:
        '''A reference to a OriginAccessControl resource.

        :param origin_access_control_id: The Id of the OriginAccessControl resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            origin_access_control_reference = interfaces_cloudfront.OriginAccessControlReference(
                origin_access_control_id="originAccessControlId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429e437a384e20047c9d315562ddd9afc7c6dd4195379b01aac06dbca9a4ed7f)
            check_type(argname="argument origin_access_control_id", value=origin_access_control_id, expected_type=type_hints["origin_access_control_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "origin_access_control_id": origin_access_control_id,
        }

    @builtins.property
    def origin_access_control_id(self) -> builtins.str:
        '''The Id of the OriginAccessControl resource.'''
        result = self._values.get("origin_access_control_id")
        assert result is not None, "Required property 'origin_access_control_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginAccessControlReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.OriginRequestPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"origin_request_policy_id": "originRequestPolicyId"},
)
class OriginRequestPolicyReference:
    def __init__(self, *, origin_request_policy_id: builtins.str) -> None:
        '''A reference to a OriginRequestPolicy resource.

        :param origin_request_policy_id: The Id of the OriginRequestPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            origin_request_policy_reference = interfaces_cloudfront.OriginRequestPolicyReference(
                origin_request_policy_id="originRequestPolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea02d8cc04a4b9b5e9d8c6b151d0cec103783598556595ac38e67940c74abe9f)
            check_type(argname="argument origin_request_policy_id", value=origin_request_policy_id, expected_type=type_hints["origin_request_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "origin_request_policy_id": origin_request_policy_id,
        }

    @builtins.property
    def origin_request_policy_id(self) -> builtins.str:
        '''The Id of the OriginRequestPolicy resource.'''
        result = self._values.get("origin_request_policy_id")
        assert result is not None, "Required property 'origin_request_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginRequestPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.PublicKeyReference",
    jsii_struct_bases=[],
    name_mapping={"public_key_id": "publicKeyId"},
)
class PublicKeyReference:
    def __init__(self, *, public_key_id: builtins.str) -> None:
        '''A reference to a PublicKey resource.

        :param public_key_id: The Id of the PublicKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            public_key_reference = interfaces_cloudfront.PublicKeyReference(
                public_key_id="publicKeyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71250d930f6cbefe85b005d8166f7ddd62c5ea16b33c52aa38ec5d4681c2d375)
            check_type(argname="argument public_key_id", value=public_key_id, expected_type=type_hints["public_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_key_id": public_key_id,
        }

    @builtins.property
    def public_key_id(self) -> builtins.str:
        '''The Id of the PublicKey resource.'''
        result = self._values.get("public_key_id")
        assert result is not None, "Required property 'public_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.RealtimeLogConfigReference",
    jsii_struct_bases=[],
    name_mapping={"realtime_log_config_arn": "realtimeLogConfigArn"},
)
class RealtimeLogConfigReference:
    def __init__(self, *, realtime_log_config_arn: builtins.str) -> None:
        '''A reference to a RealtimeLogConfig resource.

        :param realtime_log_config_arn: The Arn of the RealtimeLogConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            realtime_log_config_reference = interfaces_cloudfront.RealtimeLogConfigReference(
                realtime_log_config_arn="realtimeLogConfigArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e47f76633903c72c57cd74c16acb44209796d52559c9feb527ba4eabfd8fe49)
            check_type(argname="argument realtime_log_config_arn", value=realtime_log_config_arn, expected_type=type_hints["realtime_log_config_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "realtime_log_config_arn": realtime_log_config_arn,
        }

    @builtins.property
    def realtime_log_config_arn(self) -> builtins.str:
        '''The Arn of the RealtimeLogConfig resource.'''
        result = self._values.get("realtime_log_config_arn")
        assert result is not None, "Required property 'realtime_log_config_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RealtimeLogConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.ResponseHeadersPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"response_headers_policy_id": "responseHeadersPolicyId"},
)
class ResponseHeadersPolicyReference:
    def __init__(self, *, response_headers_policy_id: builtins.str) -> None:
        '''A reference to a ResponseHeadersPolicy resource.

        :param response_headers_policy_id: The Id of the ResponseHeadersPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            response_headers_policy_reference = interfaces_cloudfront.ResponseHeadersPolicyReference(
                response_headers_policy_id="responseHeadersPolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fef3bb5e942491b4c267ba48598eda169bb96e3379b4df3fb4e54758952407d5)
            check_type(argname="argument response_headers_policy_id", value=response_headers_policy_id, expected_type=type_hints["response_headers_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "response_headers_policy_id": response_headers_policy_id,
        }

    @builtins.property
    def response_headers_policy_id(self) -> builtins.str:
        '''The Id of the ResponseHeadersPolicy resource.'''
        result = self._values.get("response_headers_policy_id")
        assert result is not None, "Required property 'response_headers_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResponseHeadersPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.StreamingDistributionReference",
    jsii_struct_bases=[],
    name_mapping={"streaming_distribution_id": "streamingDistributionId"},
)
class StreamingDistributionReference:
    def __init__(self, *, streaming_distribution_id: builtins.str) -> None:
        '''A reference to a StreamingDistribution resource.

        :param streaming_distribution_id: The Id of the StreamingDistribution resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            streaming_distribution_reference = interfaces_cloudfront.StreamingDistributionReference(
                streaming_distribution_id="streamingDistributionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b0342b4ece7f7cd84a2ff3923fb6055994a168bcd5e993a8ba1befb62dced2a)
            check_type(argname="argument streaming_distribution_id", value=streaming_distribution_id, expected_type=type_hints["streaming_distribution_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "streaming_distribution_id": streaming_distribution_id,
        }

    @builtins.property
    def streaming_distribution_id(self) -> builtins.str:
        '''The Id of the StreamingDistribution resource.'''
        result = self._values.get("streaming_distribution_id")
        assert result is not None, "Required property 'streaming_distribution_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamingDistributionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.TrustStoreReference",
    jsii_struct_bases=[],
    name_mapping={
        "trust_store_arn": "trustStoreArn",
        "trust_store_id": "trustStoreId",
    },
)
class TrustStoreReference:
    def __init__(
        self,
        *,
        trust_store_arn: builtins.str,
        trust_store_id: builtins.str,
    ) -> None:
        '''A reference to a TrustStore resource.

        :param trust_store_arn: The ARN of the TrustStore resource.
        :param trust_store_id: The Id of the TrustStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            trust_store_reference = interfaces_cloudfront.TrustStoreReference(
                trust_store_arn="trustStoreArn",
                trust_store_id="trustStoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ea92e634c7fa221353c2d687de12f6ab13af0db86b5e21a3c35016b0e6bd651)
            check_type(argname="argument trust_store_arn", value=trust_store_arn, expected_type=type_hints["trust_store_arn"])
            check_type(argname="argument trust_store_id", value=trust_store_id, expected_type=type_hints["trust_store_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trust_store_arn": trust_store_arn,
            "trust_store_id": trust_store_id,
        }

    @builtins.property
    def trust_store_arn(self) -> builtins.str:
        '''The ARN of the TrustStore resource.'''
        result = self._values.get("trust_store_arn")
        assert result is not None, "Required property 'trust_store_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trust_store_id(self) -> builtins.str:
        '''The Id of the TrustStore resource.'''
        result = self._values.get("trust_store_id")
        assert result is not None, "Required property 'trust_store_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrustStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudfront.VpcOriginReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_origin_arn": "vpcOriginArn", "vpc_origin_id": "vpcOriginId"},
)
class VpcOriginReference:
    def __init__(
        self,
        *,
        vpc_origin_arn: builtins.str,
        vpc_origin_id: builtins.str,
    ) -> None:
        '''A reference to a VpcOrigin resource.

        :param vpc_origin_arn: The ARN of the VpcOrigin resource.
        :param vpc_origin_id: The Id of the VpcOrigin resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudfront as interfaces_cloudfront
            
            vpc_origin_reference = interfaces_cloudfront.VpcOriginReference(
                vpc_origin_arn="vpcOriginArn",
                vpc_origin_id="vpcOriginId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69b032e15f12676ea4499a1b53874c8d182ed57bcf8be49701395b5cf79741f1)
            check_type(argname="argument vpc_origin_arn", value=vpc_origin_arn, expected_type=type_hints["vpc_origin_arn"])
            check_type(argname="argument vpc_origin_id", value=vpc_origin_id, expected_type=type_hints["vpc_origin_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_origin_arn": vpc_origin_arn,
            "vpc_origin_id": vpc_origin_id,
        }

    @builtins.property
    def vpc_origin_arn(self) -> builtins.str:
        '''The ARN of the VpcOrigin resource.'''
        result = self._values.get("vpc_origin_arn")
        assert result is not None, "Required property 'vpc_origin_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_origin_id(self) -> builtins.str:
        '''The Id of the VpcOrigin resource.'''
        result = self._values.get("vpc_origin_id")
        assert result is not None, "Required property 'vpc_origin_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcOriginReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AnycastIpListReference",
    "CachePolicyReference",
    "CloudFrontOriginAccessIdentityReference",
    "ConnectionFunctionReference",
    "ConnectionGroupReference",
    "ContinuousDeploymentPolicyReference",
    "DistributionReference",
    "DistributionTenantReference",
    "FunctionReference",
    "IAnycastIpListRef",
    "ICachePolicyRef",
    "ICloudFrontOriginAccessIdentityRef",
    "IConnectionFunctionRef",
    "IConnectionGroupRef",
    "IContinuousDeploymentPolicyRef",
    "IDistributionRef",
    "IDistributionTenantRef",
    "IFunctionRef",
    "IKeyGroupRef",
    "IKeyValueStoreRef",
    "IMonitoringSubscriptionRef",
    "IOriginAccessControlRef",
    "IOriginRequestPolicyRef",
    "IPublicKeyRef",
    "IRealtimeLogConfigRef",
    "IResponseHeadersPolicyRef",
    "IStreamingDistributionRef",
    "ITrustStoreRef",
    "IVpcOriginRef",
    "KeyGroupReference",
    "KeyValueStoreReference",
    "MonitoringSubscriptionReference",
    "OriginAccessControlReference",
    "OriginRequestPolicyReference",
    "PublicKeyReference",
    "RealtimeLogConfigReference",
    "ResponseHeadersPolicyReference",
    "StreamingDistributionReference",
    "TrustStoreReference",
    "VpcOriginReference",
]

publication.publish()

def _typecheckingstub__b0935893f040727b890159b2a61c53744a19e903fa583f51fd1335094286a882(
    *,
    anycast_ip_list_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eafc53ec8d44d91d599196eff2812b8d3e750f75445fecc22787175206a425f4(
    *,
    cache_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac62879d2ba5cdd6aa45b9be7d13a0247d5901fc9a2cbb8b4ce248ceeae24403(
    *,
    cloud_front_origin_access_identity_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd7b0bb64cedf15636618e6b755d87dc4aca386789f0be0876627def8997a3ad(
    *,
    connection_function_arn: builtins.str,
    connection_function_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03040cdfe38372fca8182c71a8a7787ed0a443239bca593242923e506cd17202(
    *,
    connection_group_arn: builtins.str,
    connection_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ecf47f2529275c1a72313ada238b7dd48f33d72dcbaad3303f04dc5489a6c4(
    *,
    continuous_deployment_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f97cc6a786fec9feb4764e7b259ccc05ed440a2e51df2dded3b144c438636683(
    *,
    distribution_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d850f4f750196ae341c242dc801ed452e2f72f450f61ca0bec654fc3744e247(
    *,
    distribution_tenant_arn: builtins.str,
    distribution_tenant_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32506104c4cd233c3476b42913670893c3370f22bfb6aca3a771d89e4c4cd669(
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__464ae77084d63c7646b271a3e37cb2e98cacce805a2d61d9f5dbdda96f46dff5(
    *,
    key_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d2ab8f161da96de4216494194339f84571b4f0f1cfe710f61f155cda66cbac5(
    *,
    key_value_store_arn: builtins.str,
    key_value_store_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d5bb5962d3c7a0d02baa196ea6a6d69ae11b813483a64036a3f44a0ae233a1b(
    *,
    distribution_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429e437a384e20047c9d315562ddd9afc7c6dd4195379b01aac06dbca9a4ed7f(
    *,
    origin_access_control_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea02d8cc04a4b9b5e9d8c6b151d0cec103783598556595ac38e67940c74abe9f(
    *,
    origin_request_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71250d930f6cbefe85b005d8166f7ddd62c5ea16b33c52aa38ec5d4681c2d375(
    *,
    public_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e47f76633903c72c57cd74c16acb44209796d52559c9feb527ba4eabfd8fe49(
    *,
    realtime_log_config_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fef3bb5e942491b4c267ba48598eda169bb96e3379b4df3fb4e54758952407d5(
    *,
    response_headers_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b0342b4ece7f7cd84a2ff3923fb6055994a168bcd5e993a8ba1befb62dced2a(
    *,
    streaming_distribution_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea92e634c7fa221353c2d687de12f6ab13af0db86b5e21a3c35016b0e6bd651(
    *,
    trust_store_arn: builtins.str,
    trust_store_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69b032e15f12676ea4499a1b53874c8d182ed57bcf8be49701395b5cf79741f1(
    *,
    vpc_origin_arn: builtins.str,
    vpc_origin_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAnycastIpListRef, ICachePolicyRef, ICloudFrontOriginAccessIdentityRef, IConnectionFunctionRef, IConnectionGroupRef, IContinuousDeploymentPolicyRef, IDistributionRef, IDistributionTenantRef, IFunctionRef, IKeyGroupRef, IKeyValueStoreRef, IMonitoringSubscriptionRef, IOriginAccessControlRef, IOriginRequestPolicyRef, IPublicKeyRef, IRealtimeLogConfigRef, IResponseHeadersPolicyRef, IStreamingDistributionRef, ITrustStoreRef, IVpcOriginRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
