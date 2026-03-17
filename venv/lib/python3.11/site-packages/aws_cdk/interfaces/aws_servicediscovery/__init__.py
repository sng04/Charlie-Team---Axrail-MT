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
    jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.HttpNamespaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "http_namespace_arn": "httpNamespaceArn",
        "http_namespace_id": "httpNamespaceId",
    },
)
class HttpNamespaceReference:
    def __init__(
        self,
        *,
        http_namespace_arn: builtins.str,
        http_namespace_id: builtins.str,
    ) -> None:
        '''A reference to a HttpNamespace resource.

        :param http_namespace_arn: The ARN of the HttpNamespace resource.
        :param http_namespace_id: The Id of the HttpNamespace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicediscovery as interfaces_servicediscovery
            
            http_namespace_reference = interfaces_servicediscovery.HttpNamespaceReference(
                http_namespace_arn="httpNamespaceArn",
                http_namespace_id="httpNamespaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47957067bc6a34b9e1d55ef91eda7d10378a02ce1bc0ee39770e7bd28e834179)
            check_type(argname="argument http_namespace_arn", value=http_namespace_arn, expected_type=type_hints["http_namespace_arn"])
            check_type(argname="argument http_namespace_id", value=http_namespace_id, expected_type=type_hints["http_namespace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http_namespace_arn": http_namespace_arn,
            "http_namespace_id": http_namespace_id,
        }

    @builtins.property
    def http_namespace_arn(self) -> builtins.str:
        '''The ARN of the HttpNamespace resource.'''
        result = self._values.get("http_namespace_arn")
        assert result is not None, "Required property 'http_namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_namespace_id(self) -> builtins.str:
        '''The Id of the HttpNamespace resource.'''
        result = self._values.get("http_namespace_id")
        assert result is not None, "Required property 'http_namespace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpNamespaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.IHttpNamespaceRef"
)
class IHttpNamespaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HttpNamespace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="httpNamespaceRef")
    def http_namespace_ref(self) -> "HttpNamespaceReference":
        '''(experimental) A reference to a HttpNamespace resource.

        :stability: experimental
        '''
        ...


class _IHttpNamespaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HttpNamespace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicediscovery.IHttpNamespaceRef"

    @builtins.property
    @jsii.member(jsii_name="httpNamespaceRef")
    def http_namespace_ref(self) -> "HttpNamespaceReference":
        '''(experimental) A reference to a HttpNamespace resource.

        :stability: experimental
        '''
        return typing.cast("HttpNamespaceReference", jsii.get(self, "httpNamespaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHttpNamespaceRef).__jsii_proxy_class__ = lambda : _IHttpNamespaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.IInstanceRef")
class IInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Instance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        ...


class _IInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Instance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicediscovery.IInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        return typing.cast("InstanceReference", jsii.get(self, "instanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceRef).__jsii_proxy_class__ = lambda : _IInstanceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.IPrivateDnsNamespaceRef"
)
class IPrivateDnsNamespaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PrivateDnsNamespace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="privateDnsNamespaceRef")
    def private_dns_namespace_ref(self) -> "PrivateDnsNamespaceReference":
        '''(experimental) A reference to a PrivateDnsNamespace resource.

        :stability: experimental
        '''
        ...


class _IPrivateDnsNamespaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PrivateDnsNamespace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicediscovery.IPrivateDnsNamespaceRef"

    @builtins.property
    @jsii.member(jsii_name="privateDnsNamespaceRef")
    def private_dns_namespace_ref(self) -> "PrivateDnsNamespaceReference":
        '''(experimental) A reference to a PrivateDnsNamespace resource.

        :stability: experimental
        '''
        return typing.cast("PrivateDnsNamespaceReference", jsii.get(self, "privateDnsNamespaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrivateDnsNamespaceRef).__jsii_proxy_class__ = lambda : _IPrivateDnsNamespaceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.IPublicDnsNamespaceRef"
)
class IPublicDnsNamespaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PublicDnsNamespace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="publicDnsNamespaceRef")
    def public_dns_namespace_ref(self) -> "PublicDnsNamespaceReference":
        '''(experimental) A reference to a PublicDnsNamespace resource.

        :stability: experimental
        '''
        ...


class _IPublicDnsNamespaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PublicDnsNamespace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicediscovery.IPublicDnsNamespaceRef"

    @builtins.property
    @jsii.member(jsii_name="publicDnsNamespaceRef")
    def public_dns_namespace_ref(self) -> "PublicDnsNamespaceReference":
        '''(experimental) A reference to a PublicDnsNamespace resource.

        :stability: experimental
        '''
        return typing.cast("PublicDnsNamespaceReference", jsii.get(self, "publicDnsNamespaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicDnsNamespaceRef).__jsii_proxy_class__ = lambda : _IPublicDnsNamespaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.IServiceRef")
class IServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        ...


class _IServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicediscovery.IServiceRef"

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        return typing.cast("ServiceReference", jsii.get(self, "serviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceRef).__jsii_proxy_class__ = lambda : _IServiceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.InstanceReference",
    jsii_struct_bases=[],
    name_mapping={"instance_id": "instanceId"},
)
class InstanceReference:
    def __init__(self, *, instance_id: builtins.str) -> None:
        '''A reference to a Instance resource.

        :param instance_id: The InstanceId of the Instance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicediscovery as interfaces_servicediscovery
            
            instance_reference = interfaces_servicediscovery.InstanceReference(
                instance_id="instanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4bdbb3373e9830f3c521133ba4f1fb36534ea7576b70ee0f70b1dbd5f00a679)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
        }

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The InstanceId of the Instance resource.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.PrivateDnsNamespaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "private_dns_namespace_arn": "privateDnsNamespaceArn",
        "private_dns_namespace_id": "privateDnsNamespaceId",
    },
)
class PrivateDnsNamespaceReference:
    def __init__(
        self,
        *,
        private_dns_namespace_arn: builtins.str,
        private_dns_namespace_id: builtins.str,
    ) -> None:
        '''A reference to a PrivateDnsNamespace resource.

        :param private_dns_namespace_arn: The ARN of the PrivateDnsNamespace resource.
        :param private_dns_namespace_id: The Id of the PrivateDnsNamespace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicediscovery as interfaces_servicediscovery
            
            private_dns_namespace_reference = interfaces_servicediscovery.PrivateDnsNamespaceReference(
                private_dns_namespace_arn="privateDnsNamespaceArn",
                private_dns_namespace_id="privateDnsNamespaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fd94864c7119ffead276f089d29d85ce74636b6b3d29bc9b9db0398d5022155)
            check_type(argname="argument private_dns_namespace_arn", value=private_dns_namespace_arn, expected_type=type_hints["private_dns_namespace_arn"])
            check_type(argname="argument private_dns_namespace_id", value=private_dns_namespace_id, expected_type=type_hints["private_dns_namespace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "private_dns_namespace_arn": private_dns_namespace_arn,
            "private_dns_namespace_id": private_dns_namespace_id,
        }

    @builtins.property
    def private_dns_namespace_arn(self) -> builtins.str:
        '''The ARN of the PrivateDnsNamespace resource.'''
        result = self._values.get("private_dns_namespace_arn")
        assert result is not None, "Required property 'private_dns_namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_dns_namespace_id(self) -> builtins.str:
        '''The Id of the PrivateDnsNamespace resource.'''
        result = self._values.get("private_dns_namespace_id")
        assert result is not None, "Required property 'private_dns_namespace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateDnsNamespaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.PublicDnsNamespaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "public_dns_namespace_arn": "publicDnsNamespaceArn",
        "public_dns_namespace_id": "publicDnsNamespaceId",
    },
)
class PublicDnsNamespaceReference:
    def __init__(
        self,
        *,
        public_dns_namespace_arn: builtins.str,
        public_dns_namespace_id: builtins.str,
    ) -> None:
        '''A reference to a PublicDnsNamespace resource.

        :param public_dns_namespace_arn: The ARN of the PublicDnsNamespace resource.
        :param public_dns_namespace_id: The Id of the PublicDnsNamespace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicediscovery as interfaces_servicediscovery
            
            public_dns_namespace_reference = interfaces_servicediscovery.PublicDnsNamespaceReference(
                public_dns_namespace_arn="publicDnsNamespaceArn",
                public_dns_namespace_id="publicDnsNamespaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5972cd83451540060dec01c3df997dc5976bb676dfadf18570fab68342417ac)
            check_type(argname="argument public_dns_namespace_arn", value=public_dns_namespace_arn, expected_type=type_hints["public_dns_namespace_arn"])
            check_type(argname="argument public_dns_namespace_id", value=public_dns_namespace_id, expected_type=type_hints["public_dns_namespace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_dns_namespace_arn": public_dns_namespace_arn,
            "public_dns_namespace_id": public_dns_namespace_id,
        }

    @builtins.property
    def public_dns_namespace_arn(self) -> builtins.str:
        '''The ARN of the PublicDnsNamespace resource.'''
        result = self._values.get("public_dns_namespace_arn")
        assert result is not None, "Required property 'public_dns_namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_dns_namespace_id(self) -> builtins.str:
        '''The Id of the PublicDnsNamespace resource.'''
        result = self._values.get("public_dns_namespace_id")
        assert result is not None, "Required property 'public_dns_namespace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicDnsNamespaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicediscovery.ServiceReference",
    jsii_struct_bases=[],
    name_mapping={"service_arn": "serviceArn", "service_id": "serviceId"},
)
class ServiceReference:
    def __init__(self, *, service_arn: builtins.str, service_id: builtins.str) -> None:
        '''A reference to a Service resource.

        :param service_arn: The ARN of the Service resource.
        :param service_id: The Id of the Service resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicediscovery as interfaces_servicediscovery
            
            service_reference = interfaces_servicediscovery.ServiceReference(
                service_arn="serviceArn",
                service_id="serviceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21202898ea0609748504f68db105edd6506044d97fd7d4c3b9b5caeee87efd85)
            check_type(argname="argument service_arn", value=service_arn, expected_type=type_hints["service_arn"])
            check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_arn": service_arn,
            "service_id": service_id,
        }

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''The ARN of the Service resource.'''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_id(self) -> builtins.str:
        '''The Id of the Service resource.'''
        result = self._values.get("service_id")
        assert result is not None, "Required property 'service_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HttpNamespaceReference",
    "IHttpNamespaceRef",
    "IInstanceRef",
    "IPrivateDnsNamespaceRef",
    "IPublicDnsNamespaceRef",
    "IServiceRef",
    "InstanceReference",
    "PrivateDnsNamespaceReference",
    "PublicDnsNamespaceReference",
    "ServiceReference",
]

publication.publish()

def _typecheckingstub__47957067bc6a34b9e1d55ef91eda7d10378a02ce1bc0ee39770e7bd28e834179(
    *,
    http_namespace_arn: builtins.str,
    http_namespace_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4bdbb3373e9830f3c521133ba4f1fb36534ea7576b70ee0f70b1dbd5f00a679(
    *,
    instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fd94864c7119ffead276f089d29d85ce74636b6b3d29bc9b9db0398d5022155(
    *,
    private_dns_namespace_arn: builtins.str,
    private_dns_namespace_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5972cd83451540060dec01c3df997dc5976bb676dfadf18570fab68342417ac(
    *,
    public_dns_namespace_arn: builtins.str,
    public_dns_namespace_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21202898ea0609748504f68db105edd6506044d97fd7d4c3b9b5caeee87efd85(
    *,
    service_arn: builtins.str,
    service_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IHttpNamespaceRef, IInstanceRef, IPrivateDnsNamespaceRef, IPublicDnsNamespaceRef, IServiceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
