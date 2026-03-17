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
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.AccessPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"access_policy_name": "accessPolicyName", "type": "type"},
)
class AccessPolicyReference:
    def __init__(self, *, access_policy_name: builtins.str, type: builtins.str) -> None:
        '''A reference to a AccessPolicy resource.

        :param access_policy_name: The Name of the AccessPolicy resource.
        :param type: The Type of the AccessPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchserverless as interfaces_opensearchserverless
            
            access_policy_reference = interfaces_opensearchserverless.AccessPolicyReference(
                access_policy_name="accessPolicyName",
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__884b1febac0e45274b13db6e6fff887e454adae7740f43545bdcb8f934db5374)
            check_type(argname="argument access_policy_name", value=access_policy_name, expected_type=type_hints["access_policy_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_policy_name": access_policy_name,
            "type": type,
        }

    @builtins.property
    def access_policy_name(self) -> builtins.str:
        '''The Name of the AccessPolicy resource.'''
        result = self._values.get("access_policy_name")
        assert result is not None, "Required property 'access_policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The Type of the AccessPolicy resource.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.CollectionGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "collection_group_arn": "collectionGroupArn",
        "collection_group_id": "collectionGroupId",
    },
)
class CollectionGroupReference:
    def __init__(
        self,
        *,
        collection_group_arn: builtins.str,
        collection_group_id: builtins.str,
    ) -> None:
        '''A reference to a CollectionGroup resource.

        :param collection_group_arn: The ARN of the CollectionGroup resource.
        :param collection_group_id: The Id of the CollectionGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchserverless as interfaces_opensearchserverless
            
            collection_group_reference = interfaces_opensearchserverless.CollectionGroupReference(
                collection_group_arn="collectionGroupArn",
                collection_group_id="collectionGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c739f7c4af23f34b25c875fb65df26ed250d3ce2ec367efa27222334a2988e46)
            check_type(argname="argument collection_group_arn", value=collection_group_arn, expected_type=type_hints["collection_group_arn"])
            check_type(argname="argument collection_group_id", value=collection_group_id, expected_type=type_hints["collection_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collection_group_arn": collection_group_arn,
            "collection_group_id": collection_group_id,
        }

    @builtins.property
    def collection_group_arn(self) -> builtins.str:
        '''The ARN of the CollectionGroup resource.'''
        result = self._values.get("collection_group_arn")
        assert result is not None, "Required property 'collection_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collection_group_id(self) -> builtins.str:
        '''The Id of the CollectionGroup resource.'''
        result = self._values.get("collection_group_id")
        assert result is not None, "Required property 'collection_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CollectionGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.CollectionReference",
    jsii_struct_bases=[],
    name_mapping={"collection_arn": "collectionArn", "collection_id": "collectionId"},
)
class CollectionReference:
    def __init__(
        self,
        *,
        collection_arn: builtins.str,
        collection_id: builtins.str,
    ) -> None:
        '''A reference to a Collection resource.

        :param collection_arn: The ARN of the Collection resource.
        :param collection_id: The Id of the Collection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchserverless as interfaces_opensearchserverless
            
            collection_reference = interfaces_opensearchserverless.CollectionReference(
                collection_arn="collectionArn",
                collection_id="collectionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0d1637ffbe962d4f161b7af695510fbe2ac28d49df39a4d165b29bb398d5948)
            check_type(argname="argument collection_arn", value=collection_arn, expected_type=type_hints["collection_arn"])
            check_type(argname="argument collection_id", value=collection_id, expected_type=type_hints["collection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collection_arn": collection_arn,
            "collection_id": collection_id,
        }

    @builtins.property
    def collection_arn(self) -> builtins.str:
        '''The ARN of the Collection resource.'''
        result = self._values.get("collection_arn")
        assert result is not None, "Required property 'collection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collection_id(self) -> builtins.str:
        '''The Id of the Collection resource.'''
        result = self._values.get("collection_id")
        assert result is not None, "Required property 'collection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CollectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.IAccessPolicyRef"
)
class IAccessPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessPolicyRef")
    def access_policy_ref(self) -> "AccessPolicyReference":
        '''(experimental) A reference to a AccessPolicy resource.

        :stability: experimental
        '''
        ...


class _IAccessPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchserverless.IAccessPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="accessPolicyRef")
    def access_policy_ref(self) -> "AccessPolicyReference":
        '''(experimental) A reference to a AccessPolicy resource.

        :stability: experimental
        '''
        return typing.cast("AccessPolicyReference", jsii.get(self, "accessPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPolicyRef).__jsii_proxy_class__ = lambda : _IAccessPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.ICollectionGroupRef"
)
class ICollectionGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CollectionGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="collectionGroupRef")
    def collection_group_ref(self) -> "CollectionGroupReference":
        '''(experimental) A reference to a CollectionGroup resource.

        :stability: experimental
        '''
        ...


class _ICollectionGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CollectionGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchserverless.ICollectionGroupRef"

    @builtins.property
    @jsii.member(jsii_name="collectionGroupRef")
    def collection_group_ref(self) -> "CollectionGroupReference":
        '''(experimental) A reference to a CollectionGroup resource.

        :stability: experimental
        '''
        return typing.cast("CollectionGroupReference", jsii.get(self, "collectionGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICollectionGroupRef).__jsii_proxy_class__ = lambda : _ICollectionGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.ICollectionRef"
)
class ICollectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Collection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="collectionRef")
    def collection_ref(self) -> "CollectionReference":
        '''(experimental) A reference to a Collection resource.

        :stability: experimental
        '''
        ...


class _ICollectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Collection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchserverless.ICollectionRef"

    @builtins.property
    @jsii.member(jsii_name="collectionRef")
    def collection_ref(self) -> "CollectionReference":
        '''(experimental) A reference to a Collection resource.

        :stability: experimental
        '''
        return typing.cast("CollectionReference", jsii.get(self, "collectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICollectionRef).__jsii_proxy_class__ = lambda : _ICollectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.IIndexRef")
class IIndexRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        ...


class _IIndexRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchserverless.IIndexRef"

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        return typing.cast("IndexReference", jsii.get(self, "indexRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIndexRef).__jsii_proxy_class__ = lambda : _IIndexRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.ILifecyclePolicyRef"
)
class ILifecyclePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LifecyclePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicyRef")
    def lifecycle_policy_ref(self) -> "LifecyclePolicyReference":
        '''(experimental) A reference to a LifecyclePolicy resource.

        :stability: experimental
        '''
        ...


class _ILifecyclePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LifecyclePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchserverless.ILifecyclePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicyRef")
    def lifecycle_policy_ref(self) -> "LifecyclePolicyReference":
        '''(experimental) A reference to a LifecyclePolicy resource.

        :stability: experimental
        '''
        return typing.cast("LifecyclePolicyReference", jsii.get(self, "lifecyclePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILifecyclePolicyRef).__jsii_proxy_class__ = lambda : _ILifecyclePolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.ISecurityConfigRef"
)
class ISecurityConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityConfigRef")
    def security_config_ref(self) -> "SecurityConfigReference":
        '''(experimental) A reference to a SecurityConfig resource.

        :stability: experimental
        '''
        ...


class _ISecurityConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchserverless.ISecurityConfigRef"

    @builtins.property
    @jsii.member(jsii_name="securityConfigRef")
    def security_config_ref(self) -> "SecurityConfigReference":
        '''(experimental) A reference to a SecurityConfig resource.

        :stability: experimental
        '''
        return typing.cast("SecurityConfigReference", jsii.get(self, "securityConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityConfigRef).__jsii_proxy_class__ = lambda : _ISecurityConfigRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.ISecurityPolicyRef"
)
class ISecurityPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityPolicyRef")
    def security_policy_ref(self) -> "SecurityPolicyReference":
        '''(experimental) A reference to a SecurityPolicy resource.

        :stability: experimental
        '''
        ...


class _ISecurityPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchserverless.ISecurityPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="securityPolicyRef")
    def security_policy_ref(self) -> "SecurityPolicyReference":
        '''(experimental) A reference to a SecurityPolicy resource.

        :stability: experimental
        '''
        return typing.cast("SecurityPolicyReference", jsii.get(self, "securityPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityPolicyRef).__jsii_proxy_class__ = lambda : _ISecurityPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.IVpcEndpointRef"
)
class IVpcEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VpcEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointRef")
    def vpc_endpoint_ref(self) -> "VpcEndpointReference":
        '''(experimental) A reference to a VpcEndpoint resource.

        :stability: experimental
        '''
        ...


class _IVpcEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VpcEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opensearchserverless.IVpcEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointRef")
    def vpc_endpoint_ref(self) -> "VpcEndpointReference":
        '''(experimental) A reference to a VpcEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("VpcEndpointReference", jsii.get(self, "vpcEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVpcEndpointRef).__jsii_proxy_class__ = lambda : _IVpcEndpointRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.IndexReference",
    jsii_struct_bases=[],
    name_mapping={
        "collection_endpoint": "collectionEndpoint",
        "index_name": "indexName",
    },
)
class IndexReference:
    def __init__(
        self,
        *,
        collection_endpoint: builtins.str,
        index_name: builtins.str,
    ) -> None:
        '''A reference to a Index resource.

        :param collection_endpoint: The CollectionEndpoint of the Index resource.
        :param index_name: The IndexName of the Index resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchserverless as interfaces_opensearchserverless
            
            index_reference = interfaces_opensearchserverless.IndexReference(
                collection_endpoint="collectionEndpoint",
                index_name="indexName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf3db2e251e120a85c5a4a474fb7a1e1736793520a4ea61671be9939f6460570)
            check_type(argname="argument collection_endpoint", value=collection_endpoint, expected_type=type_hints["collection_endpoint"])
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collection_endpoint": collection_endpoint,
            "index_name": index_name,
        }

    @builtins.property
    def collection_endpoint(self) -> builtins.str:
        '''The CollectionEndpoint of the Index resource.'''
        result = self._values.get("collection_endpoint")
        assert result is not None, "Required property 'collection_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_name(self) -> builtins.str:
        '''The IndexName of the Index resource.'''
        result = self._values.get("index_name")
        assert result is not None, "Required property 'index_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IndexReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.LifecyclePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"lifecycle_policy_name": "lifecyclePolicyName", "type": "type"},
)
class LifecyclePolicyReference:
    def __init__(
        self,
        *,
        lifecycle_policy_name: builtins.str,
        type: builtins.str,
    ) -> None:
        '''A reference to a LifecyclePolicy resource.

        :param lifecycle_policy_name: The Name of the LifecyclePolicy resource.
        :param type: The Type of the LifecyclePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchserverless as interfaces_opensearchserverless
            
            lifecycle_policy_reference = interfaces_opensearchserverless.LifecyclePolicyReference(
                lifecycle_policy_name="lifecyclePolicyName",
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a4e4ca557ce34920b2d88a43ff7aa9bf1f0cb1e6d6aa445629d7d0ced14af67)
            check_type(argname="argument lifecycle_policy_name", value=lifecycle_policy_name, expected_type=type_hints["lifecycle_policy_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lifecycle_policy_name": lifecycle_policy_name,
            "type": type,
        }

    @builtins.property
    def lifecycle_policy_name(self) -> builtins.str:
        '''The Name of the LifecyclePolicy resource.'''
        result = self._values.get("lifecycle_policy_name")
        assert result is not None, "Required property 'lifecycle_policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The Type of the LifecyclePolicy resource.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LifecyclePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.SecurityConfigReference",
    jsii_struct_bases=[],
    name_mapping={"security_config_id": "securityConfigId"},
)
class SecurityConfigReference:
    def __init__(self, *, security_config_id: builtins.str) -> None:
        '''A reference to a SecurityConfig resource.

        :param security_config_id: The Id of the SecurityConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchserverless as interfaces_opensearchserverless
            
            security_config_reference = interfaces_opensearchserverless.SecurityConfigReference(
                security_config_id="securityConfigId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef152ac0903e5421e3a855d153d56824ef0f9065aa3c1c0ecd08843a03556fd0)
            check_type(argname="argument security_config_id", value=security_config_id, expected_type=type_hints["security_config_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_config_id": security_config_id,
        }

    @builtins.property
    def security_config_id(self) -> builtins.str:
        '''The Id of the SecurityConfig resource.'''
        result = self._values.get("security_config_id")
        assert result is not None, "Required property 'security_config_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.SecurityPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"security_policy_name": "securityPolicyName", "type": "type"},
)
class SecurityPolicyReference:
    def __init__(
        self,
        *,
        security_policy_name: builtins.str,
        type: builtins.str,
    ) -> None:
        '''A reference to a SecurityPolicy resource.

        :param security_policy_name: The Name of the SecurityPolicy resource.
        :param type: The Type of the SecurityPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchserverless as interfaces_opensearchserverless
            
            security_policy_reference = interfaces_opensearchserverless.SecurityPolicyReference(
                security_policy_name="securityPolicyName",
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2caf24de5f6e303c90fa3f4fb522cf353e016c2aefd5fb670977579cd021b79b)
            check_type(argname="argument security_policy_name", value=security_policy_name, expected_type=type_hints["security_policy_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_policy_name": security_policy_name,
            "type": type,
        }

    @builtins.property
    def security_policy_name(self) -> builtins.str:
        '''The Name of the SecurityPolicy resource.'''
        result = self._values.get("security_policy_name")
        assert result is not None, "Required property 'security_policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The Type of the SecurityPolicy resource.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opensearchserverless.VpcEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_endpoint_id": "vpcEndpointId"},
)
class VpcEndpointReference:
    def __init__(self, *, vpc_endpoint_id: builtins.str) -> None:
        '''A reference to a VpcEndpoint resource.

        :param vpc_endpoint_id: The Id of the VpcEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opensearchserverless as interfaces_opensearchserverless
            
            vpc_endpoint_reference = interfaces_opensearchserverless.VpcEndpointReference(
                vpc_endpoint_id="vpcEndpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b08dfe0437caf78c6728ccbe3f060d9d69e6b653518ea92835805c9321335a30)
            check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_endpoint_id": vpc_endpoint_id,
        }

    @builtins.property
    def vpc_endpoint_id(self) -> builtins.str:
        '''The Id of the VpcEndpoint resource.'''
        result = self._values.get("vpc_endpoint_id")
        assert result is not None, "Required property 'vpc_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessPolicyReference",
    "CollectionGroupReference",
    "CollectionReference",
    "IAccessPolicyRef",
    "ICollectionGroupRef",
    "ICollectionRef",
    "IIndexRef",
    "ILifecyclePolicyRef",
    "ISecurityConfigRef",
    "ISecurityPolicyRef",
    "IVpcEndpointRef",
    "IndexReference",
    "LifecyclePolicyReference",
    "SecurityConfigReference",
    "SecurityPolicyReference",
    "VpcEndpointReference",
]

publication.publish()

def _typecheckingstub__884b1febac0e45274b13db6e6fff887e454adae7740f43545bdcb8f934db5374(
    *,
    access_policy_name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c739f7c4af23f34b25c875fb65df26ed250d3ce2ec367efa27222334a2988e46(
    *,
    collection_group_arn: builtins.str,
    collection_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0d1637ffbe962d4f161b7af695510fbe2ac28d49df39a4d165b29bb398d5948(
    *,
    collection_arn: builtins.str,
    collection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf3db2e251e120a85c5a4a474fb7a1e1736793520a4ea61671be9939f6460570(
    *,
    collection_endpoint: builtins.str,
    index_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4e4ca557ce34920b2d88a43ff7aa9bf1f0cb1e6d6aa445629d7d0ced14af67(
    *,
    lifecycle_policy_name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef152ac0903e5421e3a855d153d56824ef0f9065aa3c1c0ecd08843a03556fd0(
    *,
    security_config_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2caf24de5f6e303c90fa3f4fb522cf353e016c2aefd5fb670977579cd021b79b(
    *,
    security_policy_name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b08dfe0437caf78c6728ccbe3f060d9d69e6b653518ea92835805c9321335a30(
    *,
    vpc_endpoint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessPolicyRef, ICollectionGroupRef, ICollectionRef, IIndexRef, ILifecyclePolicyRef, ISecurityConfigRef, ISecurityPolicyRef, IVpcEndpointRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
