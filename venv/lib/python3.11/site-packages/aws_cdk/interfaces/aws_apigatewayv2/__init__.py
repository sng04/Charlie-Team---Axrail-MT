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
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.ApiGatewayManagedOverridesReference",
    jsii_struct_bases=[],
    name_mapping={"api_gateway_managed_overrides_id": "apiGatewayManagedOverridesId"},
)
class ApiGatewayManagedOverridesReference:
    def __init__(self, *, api_gateway_managed_overrides_id: builtins.str) -> None:
        '''A reference to a ApiGatewayManagedOverrides resource.

        :param api_gateway_managed_overrides_id: The Id of the ApiGatewayManagedOverrides resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            api_gateway_managed_overrides_reference = interfaces_apigatewayv2.ApiGatewayManagedOverridesReference(
                api_gateway_managed_overrides_id="apiGatewayManagedOverridesId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a533b68d10ff8dc8d4bd6c48b560a6ddf51af3e13d11233b0e2728f05085cc1d)
            check_type(argname="argument api_gateway_managed_overrides_id", value=api_gateway_managed_overrides_id, expected_type=type_hints["api_gateway_managed_overrides_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_gateway_managed_overrides_id": api_gateway_managed_overrides_id,
        }

    @builtins.property
    def api_gateway_managed_overrides_id(self) -> builtins.str:
        '''The Id of the ApiGatewayManagedOverrides resource.'''
        result = self._values.get("api_gateway_managed_overrides_id")
        assert result is not None, "Required property 'api_gateway_managed_overrides_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiGatewayManagedOverridesReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.ApiMappingReference",
    jsii_struct_bases=[],
    name_mapping={"api_mapping_id": "apiMappingId", "domain_name": "domainName"},
)
class ApiMappingReference:
    def __init__(
        self,
        *,
        api_mapping_id: builtins.str,
        domain_name: builtins.str,
    ) -> None:
        '''A reference to a ApiMapping resource.

        :param api_mapping_id: The ApiMappingId of the ApiMapping resource.
        :param domain_name: The DomainName of the ApiMapping resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            api_mapping_reference = interfaces_apigatewayv2.ApiMappingReference(
                api_mapping_id="apiMappingId",
                domain_name="domainName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__205243ab94e4c0f3e23746a158d49e0123f145e32d1e02109d2343158096bfa8)
            check_type(argname="argument api_mapping_id", value=api_mapping_id, expected_type=type_hints["api_mapping_id"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_mapping_id": api_mapping_id,
            "domain_name": domain_name,
        }

    @builtins.property
    def api_mapping_id(self) -> builtins.str:
        '''The ApiMappingId of the ApiMapping resource.'''
        result = self._values.get("api_mapping_id")
        assert result is not None, "Required property 'api_mapping_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the ApiMapping resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiMappingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.ApiReference",
    jsii_struct_bases=[],
    name_mapping={"api_id": "apiId"},
)
class ApiReference:
    def __init__(self, *, api_id: builtins.str) -> None:
        '''A reference to a Api resource.

        :param api_id: The ApiId of the Api resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            api_reference = interfaces_apigatewayv2.ApiReference(
                api_id="apiId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__020cf6cefb4ddec6969b2bf9d470c483fd69e1db121b162ae77cdc7f2ca404ca)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The ApiId of the Api resource.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.AuthorizerReference",
    jsii_struct_bases=[],
    name_mapping={"api_id": "apiId", "authorizer_id": "authorizerId"},
)
class AuthorizerReference:
    def __init__(self, *, api_id: builtins.str, authorizer_id: builtins.str) -> None:
        '''A reference to a Authorizer resource.

        :param api_id: The ApiId of the Authorizer resource.
        :param authorizer_id: The AuthorizerId of the Authorizer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            authorizer_reference = interfaces_apigatewayv2.AuthorizerReference(
                api_id="apiId",
                authorizer_id="authorizerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e02579340b70d1c4bd0627efd74d8fae1dafd730a8cfc4e302a7ef54eca86b30)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument authorizer_id", value=authorizer_id, expected_type=type_hints["authorizer_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "authorizer_id": authorizer_id,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The ApiId of the Authorizer resource.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_id(self) -> builtins.str:
        '''The AuthorizerId of the Authorizer resource.'''
        result = self._values.get("authorizer_id")
        assert result is not None, "Required property 'authorizer_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.DeploymentReference",
    jsii_struct_bases=[],
    name_mapping={"api_id": "apiId", "deployment_id": "deploymentId"},
)
class DeploymentReference:
    def __init__(self, *, api_id: builtins.str, deployment_id: builtins.str) -> None:
        '''A reference to a Deployment resource.

        :param api_id: The ApiId of the Deployment resource.
        :param deployment_id: The DeploymentId of the Deployment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            deployment_reference = interfaces_apigatewayv2.DeploymentReference(
                api_id="apiId",
                deployment_id="deploymentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__593d3d2e939caff97ef3533c1ce017e9e071f5b02e04ab5bcf1eaa69fe310b11)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument deployment_id", value=deployment_id, expected_type=type_hints["deployment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "deployment_id": deployment_id,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The ApiId of the Deployment resource.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_id(self) -> builtins.str:
        '''The DeploymentId of the Deployment resource.'''
        result = self._values.get("deployment_id")
        assert result is not None, "Required property 'deployment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.DomainNameReference",
    jsii_struct_bases=[],
    name_mapping={"domain_name": "domainName", "domain_name_arn": "domainNameArn"},
)
class DomainNameReference:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        domain_name_arn: builtins.str,
    ) -> None:
        '''A reference to a DomainName resource.

        :param domain_name: The DomainName of the DomainName resource.
        :param domain_name_arn: The ARN of the DomainName resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            domain_name_reference = interfaces_apigatewayv2.DomainNameReference(
                domain_name="domainName",
                domain_name_arn="domainNameArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38c85d5ef1e910b443c592bd33d3b8062b711c8fcc92d3ec7581053dd7e16aa2)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument domain_name_arn", value=domain_name_arn, expected_type=type_hints["domain_name_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "domain_name_arn": domain_name_arn,
        }

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the DomainName resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name_arn(self) -> builtins.str:
        '''The ARN of the DomainName resource.'''
        result = self._values.get("domain_name_arn")
        assert result is not None, "Required property 'domain_name_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainNameReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IApiGatewayManagedOverridesRef"
)
class IApiGatewayManagedOverridesRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApiGatewayManagedOverrides.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiGatewayManagedOverridesRef")
    def api_gateway_managed_overrides_ref(
        self,
    ) -> "ApiGatewayManagedOverridesReference":
        '''(experimental) A reference to a ApiGatewayManagedOverrides resource.

        :stability: experimental
        '''
        ...


class _IApiGatewayManagedOverridesRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApiGatewayManagedOverrides.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IApiGatewayManagedOverridesRef"

    @builtins.property
    @jsii.member(jsii_name="apiGatewayManagedOverridesRef")
    def api_gateway_managed_overrides_ref(
        self,
    ) -> "ApiGatewayManagedOverridesReference":
        '''(experimental) A reference to a ApiGatewayManagedOverrides resource.

        :stability: experimental
        '''
        return typing.cast("ApiGatewayManagedOverridesReference", jsii.get(self, "apiGatewayManagedOverridesRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiGatewayManagedOverridesRef).__jsii_proxy_class__ = lambda : _IApiGatewayManagedOverridesRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IApiMappingRef")
class IApiMappingRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApiMapping.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiMappingRef")
    def api_mapping_ref(self) -> "ApiMappingReference":
        '''(experimental) A reference to a ApiMapping resource.

        :stability: experimental
        '''
        ...


class _IApiMappingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApiMapping.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IApiMappingRef"

    @builtins.property
    @jsii.member(jsii_name="apiMappingRef")
    def api_mapping_ref(self) -> "ApiMappingReference":
        '''(experimental) A reference to a ApiMapping resource.

        :stability: experimental
        '''
        return typing.cast("ApiMappingReference", jsii.get(self, "apiMappingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiMappingRef).__jsii_proxy_class__ = lambda : _IApiMappingRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IApiRef")
class IApiRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Api.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiRef")
    def api_ref(self) -> "ApiReference":
        '''(experimental) A reference to a Api resource.

        :stability: experimental
        '''
        ...


class _IApiRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Api.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IApiRef"

    @builtins.property
    @jsii.member(jsii_name="apiRef")
    def api_ref(self) -> "ApiReference":
        '''(experimental) A reference to a Api resource.

        :stability: experimental
        '''
        return typing.cast("ApiReference", jsii.get(self, "apiRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiRef).__jsii_proxy_class__ = lambda : _IApiRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IAuthorizerRef")
class IAuthorizerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Authorizer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="authorizerRef")
    def authorizer_ref(self) -> "AuthorizerReference":
        '''(experimental) A reference to a Authorizer resource.

        :stability: experimental
        '''
        ...


class _IAuthorizerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Authorizer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IAuthorizerRef"

    @builtins.property
    @jsii.member(jsii_name="authorizerRef")
    def authorizer_ref(self) -> "AuthorizerReference":
        '''(experimental) A reference to a Authorizer resource.

        :stability: experimental
        '''
        return typing.cast("AuthorizerReference", jsii.get(self, "authorizerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAuthorizerRef).__jsii_proxy_class__ = lambda : _IAuthorizerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IDeploymentRef")
class IDeploymentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Deployment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deploymentRef")
    def deployment_ref(self) -> "DeploymentReference":
        '''(experimental) A reference to a Deployment resource.

        :stability: experimental
        '''
        ...


class _IDeploymentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Deployment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IDeploymentRef"

    @builtins.property
    @jsii.member(jsii_name="deploymentRef")
    def deployment_ref(self) -> "DeploymentReference":
        '''(experimental) A reference to a Deployment resource.

        :stability: experimental
        '''
        return typing.cast("DeploymentReference", jsii.get(self, "deploymentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeploymentRef).__jsii_proxy_class__ = lambda : _IDeploymentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IDomainNameRef")
class IDomainNameRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DomainName.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainNameRef")
    def domain_name_ref(self) -> "DomainNameReference":
        '''(experimental) A reference to a DomainName resource.

        :stability: experimental
        '''
        ...


class _IDomainNameRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DomainName.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IDomainNameRef"

    @builtins.property
    @jsii.member(jsii_name="domainNameRef")
    def domain_name_ref(self) -> "DomainNameReference":
        '''(experimental) A reference to a DomainName resource.

        :stability: experimental
        '''
        return typing.cast("DomainNameReference", jsii.get(self, "domainNameRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainNameRef).__jsii_proxy_class__ = lambda : _IDomainNameRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IIntegrationRef")
class IIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        ...


class _IIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationReference", jsii.get(self, "integrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationRef).__jsii_proxy_class__ = lambda : _IIntegrationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IIntegrationResponseRef"
)
class IIntegrationResponseRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IntegrationResponse.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="integrationResponseRef")
    def integration_response_ref(self) -> "IntegrationResponseReference":
        '''(experimental) A reference to a IntegrationResponse resource.

        :stability: experimental
        '''
        ...


class _IIntegrationResponseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IntegrationResponse.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IIntegrationResponseRef"

    @builtins.property
    @jsii.member(jsii_name="integrationResponseRef")
    def integration_response_ref(self) -> "IntegrationResponseReference":
        '''(experimental) A reference to a IntegrationResponse resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationResponseReference", jsii.get(self, "integrationResponseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationResponseRef).__jsii_proxy_class__ = lambda : _IIntegrationResponseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IModelRef")
class IModelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Model.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelRef")
    def model_ref(self) -> "ModelReference":
        '''(experimental) A reference to a Model resource.

        :stability: experimental
        '''
        ...


class _IModelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Model.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IModelRef"

    @builtins.property
    @jsii.member(jsii_name="modelRef")
    def model_ref(self) -> "ModelReference":
        '''(experimental) A reference to a Model resource.

        :stability: experimental
        '''
        return typing.cast("ModelReference", jsii.get(self, "modelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelRef).__jsii_proxy_class__ = lambda : _IModelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IRouteRef")
class IRouteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Route.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeRef")
    def route_ref(self) -> "RouteReference":
        '''(experimental) A reference to a Route resource.

        :stability: experimental
        '''
        ...


class _IRouteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Route.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IRouteRef"

    @builtins.property
    @jsii.member(jsii_name="routeRef")
    def route_ref(self) -> "RouteReference":
        '''(experimental) A reference to a Route resource.

        :stability: experimental
        '''
        return typing.cast("RouteReference", jsii.get(self, "routeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteRef).__jsii_proxy_class__ = lambda : _IRouteRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IRouteResponseRef")
class IRouteResponseRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouteResponse.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeResponseRef")
    def route_response_ref(self) -> "RouteResponseReference":
        '''(experimental) A reference to a RouteResponse resource.

        :stability: experimental
        '''
        ...


class _IRouteResponseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouteResponse.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IRouteResponseRef"

    @builtins.property
    @jsii.member(jsii_name="routeResponseRef")
    def route_response_ref(self) -> "RouteResponseReference":
        '''(experimental) A reference to a RouteResponse resource.

        :stability: experimental
        '''
        return typing.cast("RouteResponseReference", jsii.get(self, "routeResponseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteResponseRef).__jsii_proxy_class__ = lambda : _IRouteResponseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IRoutingRuleRef")
class IRoutingRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RoutingRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routingRuleRef")
    def routing_rule_ref(self) -> "RoutingRuleReference":
        '''(experimental) A reference to a RoutingRule resource.

        :stability: experimental
        '''
        ...


class _IRoutingRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RoutingRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IRoutingRuleRef"

    @builtins.property
    @jsii.member(jsii_name="routingRuleRef")
    def routing_rule_ref(self) -> "RoutingRuleReference":
        '''(experimental) A reference to a RoutingRule resource.

        :stability: experimental
        '''
        return typing.cast("RoutingRuleReference", jsii.get(self, "routingRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRoutingRuleRef).__jsii_proxy_class__ = lambda : _IRoutingRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IStageRef")
class IStageRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Stage.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stageRef")
    def stage_ref(self) -> "StageReference":
        '''(experimental) A reference to a Stage resource.

        :stability: experimental
        '''
        ...


class _IStageRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Stage.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IStageRef"

    @builtins.property
    @jsii.member(jsii_name="stageRef")
    def stage_ref(self) -> "StageReference":
        '''(experimental) A reference to a Stage resource.

        :stability: experimental
        '''
        return typing.cast("StageReference", jsii.get(self, "stageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStageRef).__jsii_proxy_class__ = lambda : _IStageRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IVpcLinkRef")
class IVpcLinkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VpcLink.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcLinkRef")
    def vpc_link_ref(self) -> "VpcLinkReference":
        '''(experimental) A reference to a VpcLink resource.

        :stability: experimental
        '''
        ...


class _IVpcLinkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VpcLink.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigatewayv2.IVpcLinkRef"

    @builtins.property
    @jsii.member(jsii_name="vpcLinkRef")
    def vpc_link_ref(self) -> "VpcLinkReference":
        '''(experimental) A reference to a VpcLink resource.

        :stability: experimental
        '''
        return typing.cast("VpcLinkReference", jsii.get(self, "vpcLinkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVpcLinkRef).__jsii_proxy_class__ = lambda : _IVpcLinkRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IntegrationReference",
    jsii_struct_bases=[],
    name_mapping={"api_id": "apiId", "integration_id": "integrationId"},
)
class IntegrationReference:
    def __init__(self, *, api_id: builtins.str, integration_id: builtins.str) -> None:
        '''A reference to a Integration resource.

        :param api_id: The ApiId of the Integration resource.
        :param integration_id: The IntegrationId of the Integration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            integration_reference = interfaces_apigatewayv2.IntegrationReference(
                api_id="apiId",
                integration_id="integrationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2f805926ee6d5a18e437dd239b61746ad3640ce6152c74b85a5ba50d6995f1a)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument integration_id", value=integration_id, expected_type=type_hints["integration_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "integration_id": integration_id,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The ApiId of the Integration resource.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_id(self) -> builtins.str:
        '''The IntegrationId of the Integration resource.'''
        result = self._values.get("integration_id")
        assert result is not None, "Required property 'integration_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.IntegrationResponseReference",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "integration_id": "integrationId",
        "integration_response_id": "integrationResponseId",
    },
)
class IntegrationResponseReference:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        integration_id: builtins.str,
        integration_response_id: builtins.str,
    ) -> None:
        '''A reference to a IntegrationResponse resource.

        :param api_id: The ApiId of the IntegrationResponse resource.
        :param integration_id: The IntegrationId of the IntegrationResponse resource.
        :param integration_response_id: The IntegrationResponseId of the IntegrationResponse resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            integration_response_reference = interfaces_apigatewayv2.IntegrationResponseReference(
                api_id="apiId",
                integration_id="integrationId",
                integration_response_id="integrationResponseId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62d43af7d1f33435e00ca8cffb84740c7a5b2797730196cdc2980641539e93ec)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument integration_id", value=integration_id, expected_type=type_hints["integration_id"])
            check_type(argname="argument integration_response_id", value=integration_response_id, expected_type=type_hints["integration_response_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "integration_id": integration_id,
            "integration_response_id": integration_response_id,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The ApiId of the IntegrationResponse resource.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_id(self) -> builtins.str:
        '''The IntegrationId of the IntegrationResponse resource.'''
        result = self._values.get("integration_id")
        assert result is not None, "Required property 'integration_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_response_id(self) -> builtins.str:
        '''The IntegrationResponseId of the IntegrationResponse resource.'''
        result = self._values.get("integration_response_id")
        assert result is not None, "Required property 'integration_response_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationResponseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.ModelReference",
    jsii_struct_bases=[],
    name_mapping={"api_id": "apiId", "model_id": "modelId"},
)
class ModelReference:
    def __init__(self, *, api_id: builtins.str, model_id: builtins.str) -> None:
        '''A reference to a Model resource.

        :param api_id: The ApiId of the Model resource.
        :param model_id: The ModelId of the Model resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            model_reference = interfaces_apigatewayv2.ModelReference(
                api_id="apiId",
                model_id="modelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__312b6260e192c317d46825f46d64f3fa208bd5849a27e6a8f9f5147ba63dfbcc)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "model_id": model_id,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The ApiId of the Model resource.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_id(self) -> builtins.str:
        '''The ModelId of the Model resource.'''
        result = self._values.get("model_id")
        assert result is not None, "Required property 'model_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.RouteReference",
    jsii_struct_bases=[],
    name_mapping={"api_id": "apiId", "route_id": "routeId"},
)
class RouteReference:
    def __init__(self, *, api_id: builtins.str, route_id: builtins.str) -> None:
        '''A reference to a Route resource.

        :param api_id: The ApiId of the Route resource.
        :param route_id: The RouteId of the Route resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            route_reference = interfaces_apigatewayv2.RouteReference(
                api_id="apiId",
                route_id="routeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00a6d488d61a830320ed07c930904f816e9ebc91c1c792f6ef75af4feda8979f)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument route_id", value=route_id, expected_type=type_hints["route_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "route_id": route_id,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The ApiId of the Route resource.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_id(self) -> builtins.str:
        '''The RouteId of the Route resource.'''
        result = self._values.get("route_id")
        assert result is not None, "Required property 'route_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.RouteResponseReference",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "route_id": "routeId",
        "route_response_id": "routeResponseId",
    },
)
class RouteResponseReference:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        route_id: builtins.str,
        route_response_id: builtins.str,
    ) -> None:
        '''A reference to a RouteResponse resource.

        :param api_id: The ApiId of the RouteResponse resource.
        :param route_id: The RouteId of the RouteResponse resource.
        :param route_response_id: The RouteResponseId of the RouteResponse resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            route_response_reference = interfaces_apigatewayv2.RouteResponseReference(
                api_id="apiId",
                route_id="routeId",
                route_response_id="routeResponseId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76af7410f481bf417dd6ce36a3c6f84bdae5f646db9b847ab5148f3167b88e9f)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument route_id", value=route_id, expected_type=type_hints["route_id"])
            check_type(argname="argument route_response_id", value=route_response_id, expected_type=type_hints["route_response_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "route_id": route_id,
            "route_response_id": route_response_id,
        }

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The ApiId of the RouteResponse resource.'''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_id(self) -> builtins.str:
        '''The RouteId of the RouteResponse resource.'''
        result = self._values.get("route_id")
        assert result is not None, "Required property 'route_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_response_id(self) -> builtins.str:
        '''The RouteResponseId of the RouteResponse resource.'''
        result = self._values.get("route_response_id")
        assert result is not None, "Required property 'route_response_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteResponseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.RoutingRuleReference",
    jsii_struct_bases=[],
    name_mapping={"routing_rule_arn": "routingRuleArn"},
)
class RoutingRuleReference:
    def __init__(self, *, routing_rule_arn: builtins.str) -> None:
        '''A reference to a RoutingRule resource.

        :param routing_rule_arn: The RoutingRuleArn of the RoutingRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            routing_rule_reference = interfaces_apigatewayv2.RoutingRuleReference(
                routing_rule_arn="routingRuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b414cc5aebd58b5078df3cfcec68e706708dafa722e76ae034b0567f9cdee822)
            check_type(argname="argument routing_rule_arn", value=routing_rule_arn, expected_type=type_hints["routing_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "routing_rule_arn": routing_rule_arn,
        }

    @builtins.property
    def routing_rule_arn(self) -> builtins.str:
        '''The RoutingRuleArn of the RoutingRule resource.'''
        result = self._values.get("routing_rule_arn")
        assert result is not None, "Required property 'routing_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoutingRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.StageReference",
    jsii_struct_bases=[],
    name_mapping={"stage_name": "stageName"},
)
class StageReference:
    def __init__(self, *, stage_name: builtins.str) -> None:
        '''A reference to a Stage resource.

        :param stage_name: The StageName of the Stage resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            stage_reference = interfaces_apigatewayv2.StageReference(
                stage_name="stageName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be0fe02777445259bb9740baea840d3e2b479e563294c5907864f7e331741cb6)
            check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stage_name": stage_name,
        }

    @builtins.property
    def stage_name(self) -> builtins.str:
        '''The StageName of the Stage resource.'''
        result = self._values.get("stage_name")
        assert result is not None, "Required property 'stage_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigatewayv2.VpcLinkReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_link_id": "vpcLinkId"},
)
class VpcLinkReference:
    def __init__(self, *, vpc_link_id: builtins.str) -> None:
        '''A reference to a VpcLink resource.

        :param vpc_link_id: The VpcLinkId of the VpcLink resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigatewayv2 as interfaces_apigatewayv2
            
            vpc_link_reference = interfaces_apigatewayv2.VpcLinkReference(
                vpc_link_id="vpcLinkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b83e841c31043c01aed344fbe7a443be81265bcb06f5ed800112fffe3cbe904f)
            check_type(argname="argument vpc_link_id", value=vpc_link_id, expected_type=type_hints["vpc_link_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_link_id": vpc_link_id,
        }

    @builtins.property
    def vpc_link_id(self) -> builtins.str:
        '''The VpcLinkId of the VpcLink resource.'''
        result = self._values.get("vpc_link_id")
        assert result is not None, "Required property 'vpc_link_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcLinkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiGatewayManagedOverridesReference",
    "ApiMappingReference",
    "ApiReference",
    "AuthorizerReference",
    "DeploymentReference",
    "DomainNameReference",
    "IApiGatewayManagedOverridesRef",
    "IApiMappingRef",
    "IApiRef",
    "IAuthorizerRef",
    "IDeploymentRef",
    "IDomainNameRef",
    "IIntegrationRef",
    "IIntegrationResponseRef",
    "IModelRef",
    "IRouteRef",
    "IRouteResponseRef",
    "IRoutingRuleRef",
    "IStageRef",
    "IVpcLinkRef",
    "IntegrationReference",
    "IntegrationResponseReference",
    "ModelReference",
    "RouteReference",
    "RouteResponseReference",
    "RoutingRuleReference",
    "StageReference",
    "VpcLinkReference",
]

publication.publish()

def _typecheckingstub__a533b68d10ff8dc8d4bd6c48b560a6ddf51af3e13d11233b0e2728f05085cc1d(
    *,
    api_gateway_managed_overrides_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__205243ab94e4c0f3e23746a158d49e0123f145e32d1e02109d2343158096bfa8(
    *,
    api_mapping_id: builtins.str,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__020cf6cefb4ddec6969b2bf9d470c483fd69e1db121b162ae77cdc7f2ca404ca(
    *,
    api_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e02579340b70d1c4bd0627efd74d8fae1dafd730a8cfc4e302a7ef54eca86b30(
    *,
    api_id: builtins.str,
    authorizer_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__593d3d2e939caff97ef3533c1ce017e9e071f5b02e04ab5bcf1eaa69fe310b11(
    *,
    api_id: builtins.str,
    deployment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38c85d5ef1e910b443c592bd33d3b8062b711c8fcc92d3ec7581053dd7e16aa2(
    *,
    domain_name: builtins.str,
    domain_name_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2f805926ee6d5a18e437dd239b61746ad3640ce6152c74b85a5ba50d6995f1a(
    *,
    api_id: builtins.str,
    integration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62d43af7d1f33435e00ca8cffb84740c7a5b2797730196cdc2980641539e93ec(
    *,
    api_id: builtins.str,
    integration_id: builtins.str,
    integration_response_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__312b6260e192c317d46825f46d64f3fa208bd5849a27e6a8f9f5147ba63dfbcc(
    *,
    api_id: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a6d488d61a830320ed07c930904f816e9ebc91c1c792f6ef75af4feda8979f(
    *,
    api_id: builtins.str,
    route_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76af7410f481bf417dd6ce36a3c6f84bdae5f646db9b847ab5148f3167b88e9f(
    *,
    api_id: builtins.str,
    route_id: builtins.str,
    route_response_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b414cc5aebd58b5078df3cfcec68e706708dafa722e76ae034b0567f9cdee822(
    *,
    routing_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be0fe02777445259bb9740baea840d3e2b479e563294c5907864f7e331741cb6(
    *,
    stage_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b83e841c31043c01aed344fbe7a443be81265bcb06f5ed800112fffe3cbe904f(
    *,
    vpc_link_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApiGatewayManagedOverridesRef, IApiMappingRef, IApiRef, IAuthorizerRef, IDeploymentRef, IDomainNameRef, IIntegrationRef, IIntegrationResponseRef, IModelRef, IRouteRef, IRouteResponseRef, IRoutingRuleRef, IStageRef, IVpcLinkRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
