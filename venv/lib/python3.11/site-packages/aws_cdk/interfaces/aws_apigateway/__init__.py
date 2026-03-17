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
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.AccountReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class AccountReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a Account resource.

        :param account_id: The Id of the Account resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            account_reference = interfaces_apigateway.AccountReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35ad850c85a8d4afdd663227c7e32f94d8450f981a615d04890e872b21d1612d)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The Id of the Account resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.ApiKeyReference",
    jsii_struct_bases=[],
    name_mapping={"api_key_id": "apiKeyId"},
)
class ApiKeyReference:
    def __init__(self, *, api_key_id: builtins.str) -> None:
        '''A reference to a ApiKey resource.

        :param api_key_id: The APIKeyId of the ApiKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            api_key_reference = interfaces_apigateway.ApiKeyReference(
                api_key_id="apiKeyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c14fb5f90c77f82575a97f9a173c3410680639b45caef1bb8b8672340b4bf31)
            check_type(argname="argument api_key_id", value=api_key_id, expected_type=type_hints["api_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key_id": api_key_id,
        }

    @builtins.property
    def api_key_id(self) -> builtins.str:
        '''The APIKeyId of the ApiKey resource.'''
        result = self._values.get("api_key_id")
        assert result is not None, "Required property 'api_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.AuthorizerReference",
    jsii_struct_bases=[],
    name_mapping={"authorizer_id": "authorizerId", "rest_api_id": "restApiId"},
)
class AuthorizerReference:
    def __init__(
        self,
        *,
        authorizer_id: builtins.str,
        rest_api_id: builtins.str,
    ) -> None:
        '''A reference to a Authorizer resource.

        :param authorizer_id: The AuthorizerId of the Authorizer resource.
        :param rest_api_id: The RestApiId of the Authorizer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            authorizer_reference = interfaces_apigateway.AuthorizerReference(
                authorizer_id="authorizerId",
                rest_api_id="restApiId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d68d6630cf7fd51cb53d1150a586c3b490adb4d029b8db237f87f6cfd3208191)
            check_type(argname="argument authorizer_id", value=authorizer_id, expected_type=type_hints["authorizer_id"])
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorizer_id": authorizer_id,
            "rest_api_id": rest_api_id,
        }

    @builtins.property
    def authorizer_id(self) -> builtins.str:
        '''The AuthorizerId of the Authorizer resource.'''
        result = self._values.get("authorizer_id")
        assert result is not None, "Required property 'authorizer_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''The RestApiId of the Authorizer resource.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.BasePathMappingReference",
    jsii_struct_bases=[],
    name_mapping={"base_path": "basePath", "domain_name": "domainName"},
)
class BasePathMappingReference:
    def __init__(self, *, base_path: builtins.str, domain_name: builtins.str) -> None:
        '''A reference to a BasePathMapping resource.

        :param base_path: The BasePath of the BasePathMapping resource.
        :param domain_name: The DomainName of the BasePathMapping resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            base_path_mapping_reference = interfaces_apigateway.BasePathMappingReference(
                base_path="basePath",
                domain_name="domainName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6766e0e75fadfc941acafb7116bc52e0ea2debd27cb810b19e5837efdb4b86e3)
            check_type(argname="argument base_path", value=base_path, expected_type=type_hints["base_path"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "base_path": base_path,
            "domain_name": domain_name,
        }

    @builtins.property
    def base_path(self) -> builtins.str:
        '''The BasePath of the BasePathMapping resource.'''
        result = self._values.get("base_path")
        assert result is not None, "Required property 'base_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the BasePathMapping resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasePathMappingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.BasePathMappingV2Reference",
    jsii_struct_bases=[],
    name_mapping={"base_path_mapping_arn": "basePathMappingArn"},
)
class BasePathMappingV2Reference:
    def __init__(self, *, base_path_mapping_arn: builtins.str) -> None:
        '''A reference to a BasePathMappingV2 resource.

        :param base_path_mapping_arn: The BasePathMappingArn of the BasePathMappingV2 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            base_path_mapping_v2_reference = interfaces_apigateway.BasePathMappingV2Reference(
                base_path_mapping_arn="basePathMappingArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f95b02fe81974b197f19290ec8ad7f11678477fb4eeab26fec56c0fb5351a850)
            check_type(argname="argument base_path_mapping_arn", value=base_path_mapping_arn, expected_type=type_hints["base_path_mapping_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "base_path_mapping_arn": base_path_mapping_arn,
        }

    @builtins.property
    def base_path_mapping_arn(self) -> builtins.str:
        '''The BasePathMappingArn of the BasePathMappingV2 resource.'''
        result = self._values.get("base_path_mapping_arn")
        assert result is not None, "Required property 'base_path_mapping_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BasePathMappingV2Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.ClientCertificateReference",
    jsii_struct_bases=[],
    name_mapping={"client_certificate_id": "clientCertificateId"},
)
class ClientCertificateReference:
    def __init__(self, *, client_certificate_id: builtins.str) -> None:
        '''A reference to a ClientCertificate resource.

        :param client_certificate_id: The ClientCertificateId of the ClientCertificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            client_certificate_reference = interfaces_apigateway.ClientCertificateReference(
                client_certificate_id="clientCertificateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__833a4d31ace847ad4f8acfb3dd6ddac7e3fac64f42670367da4e70d2e3263a09)
            check_type(argname="argument client_certificate_id", value=client_certificate_id, expected_type=type_hints["client_certificate_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_certificate_id": client_certificate_id,
        }

    @builtins.property
    def client_certificate_id(self) -> builtins.str:
        '''The ClientCertificateId of the ClientCertificate resource.'''
        result = self._values.get("client_certificate_id")
        assert result is not None, "Required property 'client_certificate_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClientCertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.DeploymentReference",
    jsii_struct_bases=[],
    name_mapping={"deployment_id": "deploymentId", "rest_api_id": "restApiId"},
)
class DeploymentReference:
    def __init__(
        self,
        *,
        deployment_id: builtins.str,
        rest_api_id: builtins.str,
    ) -> None:
        '''A reference to a Deployment resource.

        :param deployment_id: The DeploymentId of the Deployment resource.
        :param rest_api_id: The RestApiId of the Deployment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            deployment_reference = interfaces_apigateway.DeploymentReference(
                deployment_id="deploymentId",
                rest_api_id="restApiId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41df7edc09bfa35e6c0eb5233570b5f5d4e6d255375a85ba37230fa1fbc86540)
            check_type(argname="argument deployment_id", value=deployment_id, expected_type=type_hints["deployment_id"])
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_id": deployment_id,
            "rest_api_id": rest_api_id,
        }

    @builtins.property
    def deployment_id(self) -> builtins.str:
        '''The DeploymentId of the Deployment resource.'''
        result = self._values.get("deployment_id")
        assert result is not None, "Required property 'deployment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''The RestApiId of the Deployment resource.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.DocumentationPartReference",
    jsii_struct_bases=[],
    name_mapping={
        "documentation_part_id": "documentationPartId",
        "rest_api_id": "restApiId",
    },
)
class DocumentationPartReference:
    def __init__(
        self,
        *,
        documentation_part_id: builtins.str,
        rest_api_id: builtins.str,
    ) -> None:
        '''A reference to a DocumentationPart resource.

        :param documentation_part_id: The DocumentationPartId of the DocumentationPart resource.
        :param rest_api_id: The RestApiId of the DocumentationPart resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            documentation_part_reference = interfaces_apigateway.DocumentationPartReference(
                documentation_part_id="documentationPartId",
                rest_api_id="restApiId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e560572f2b89e2ef2cf9d7b126db3ad6fac6770ea3c3de34b5b45e76ed0fd4e9)
            check_type(argname="argument documentation_part_id", value=documentation_part_id, expected_type=type_hints["documentation_part_id"])
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "documentation_part_id": documentation_part_id,
            "rest_api_id": rest_api_id,
        }

    @builtins.property
    def documentation_part_id(self) -> builtins.str:
        '''The DocumentationPartId of the DocumentationPart resource.'''
        result = self._values.get("documentation_part_id")
        assert result is not None, "Required property 'documentation_part_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''The RestApiId of the DocumentationPart resource.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DocumentationPartReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.DocumentationVersionReference",
    jsii_struct_bases=[],
    name_mapping={
        "documentation_version": "documentationVersion",
        "rest_api_id": "restApiId",
    },
)
class DocumentationVersionReference:
    def __init__(
        self,
        *,
        documentation_version: builtins.str,
        rest_api_id: builtins.str,
    ) -> None:
        '''A reference to a DocumentationVersion resource.

        :param documentation_version: The DocumentationVersion of the DocumentationVersion resource.
        :param rest_api_id: The RestApiId of the DocumentationVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            documentation_version_reference = interfaces_apigateway.DocumentationVersionReference(
                documentation_version="documentationVersion",
                rest_api_id="restApiId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebe125bb5075aaf5d4213def6adf1eff51805a5ca591bf88080533e0f6fad9b2)
            check_type(argname="argument documentation_version", value=documentation_version, expected_type=type_hints["documentation_version"])
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "documentation_version": documentation_version,
            "rest_api_id": rest_api_id,
        }

    @builtins.property
    def documentation_version(self) -> builtins.str:
        '''The DocumentationVersion of the DocumentationVersion resource.'''
        result = self._values.get("documentation_version")
        assert result is not None, "Required property 'documentation_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''The RestApiId of the DocumentationVersion resource.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DocumentationVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.DomainNameAccessAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name_access_association_arn": "domainNameAccessAssociationArn",
    },
)
class DomainNameAccessAssociationReference:
    def __init__(self, *, domain_name_access_association_arn: builtins.str) -> None:
        '''A reference to a DomainNameAccessAssociation resource.

        :param domain_name_access_association_arn: The DomainNameAccessAssociationArn of the DomainNameAccessAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            domain_name_access_association_reference = interfaces_apigateway.DomainNameAccessAssociationReference(
                domain_name_access_association_arn="domainNameAccessAssociationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6106393b25c71c75f181d6e2216433d64ca457d3aa5346d3c08c9c5c8f76ccb9)
            check_type(argname="argument domain_name_access_association_arn", value=domain_name_access_association_arn, expected_type=type_hints["domain_name_access_association_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name_access_association_arn": domain_name_access_association_arn,
        }

    @builtins.property
    def domain_name_access_association_arn(self) -> builtins.str:
        '''The DomainNameAccessAssociationArn of the DomainNameAccessAssociation resource.'''
        result = self._values.get("domain_name_access_association_arn")
        assert result is not None, "Required property 'domain_name_access_association_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainNameAccessAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.DomainNameReference",
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
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            domain_name_reference = interfaces_apigateway.DomainNameReference(
                domain_name="domainName",
                domain_name_arn="domainNameArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3cfd08bdbde02f2db8ac69a08bf7a53178de565b3b2d57297f61f0af460b23c)
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.DomainNameV2Reference",
    jsii_struct_bases=[],
    name_mapping={"domain_name_arn": "domainNameArn"},
)
class DomainNameV2Reference:
    def __init__(self, *, domain_name_arn: builtins.str) -> None:
        '''A reference to a DomainNameV2 resource.

        :param domain_name_arn: The DomainNameArn of the DomainNameV2 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            domain_name_v2_reference = interfaces_apigateway.DomainNameV2Reference(
                domain_name_arn="domainNameArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efdeb9f0ad3160236b8f4e14e4cdf544ab705171d9308fa88175fa01b8d92c49)
            check_type(argname="argument domain_name_arn", value=domain_name_arn, expected_type=type_hints["domain_name_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name_arn": domain_name_arn,
        }

    @builtins.property
    def domain_name_arn(self) -> builtins.str:
        '''The DomainNameArn of the DomainNameV2 resource.'''
        result = self._values.get("domain_name_arn")
        assert result is not None, "Required property 'domain_name_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainNameV2Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.GatewayResponseReference",
    jsii_struct_bases=[],
    name_mapping={"gateway_response_id": "gatewayResponseId"},
)
class GatewayResponseReference:
    def __init__(self, *, gateway_response_id: builtins.str) -> None:
        '''A reference to a GatewayResponse resource.

        :param gateway_response_id: The Id of the GatewayResponse resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            gateway_response_reference = interfaces_apigateway.GatewayResponseReference(
                gateway_response_id="gatewayResponseId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0794adc65f2a9a99dd04ff2f904cf838d512203fc37eac299e09871ce11fe9f)
            check_type(argname="argument gateway_response_id", value=gateway_response_id, expected_type=type_hints["gateway_response_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_response_id": gateway_response_id,
        }

    @builtins.property
    def gateway_response_id(self) -> builtins.str:
        '''The Id of the GatewayResponse resource.'''
        result = self._values.get("gateway_response_id")
        assert result is not None, "Required property 'gateway_response_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayResponseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IAccountRef")
class IAccountRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Account.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accountRef")
    def account_ref(self) -> "AccountReference":
        '''(experimental) A reference to a Account resource.

        :stability: experimental
        '''
        ...


class _IAccountRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Account.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IAccountRef"

    @builtins.property
    @jsii.member(jsii_name="accountRef")
    def account_ref(self) -> "AccountReference":
        '''(experimental) A reference to a Account resource.

        :stability: experimental
        '''
        return typing.cast("AccountReference", jsii.get(self, "accountRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccountRef).__jsii_proxy_class__ = lambda : _IAccountRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IApiKeyRef")
class IApiKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApiKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiKeyRef")
    def api_key_ref(self) -> "ApiKeyReference":
        '''(experimental) A reference to a ApiKey resource.

        :stability: experimental
        '''
        ...


class _IApiKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApiKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IApiKeyRef"

    @builtins.property
    @jsii.member(jsii_name="apiKeyRef")
    def api_key_ref(self) -> "ApiKeyReference":
        '''(experimental) A reference to a ApiKey resource.

        :stability: experimental
        '''
        return typing.cast("ApiKeyReference", jsii.get(self, "apiKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiKeyRef).__jsii_proxy_class__ = lambda : _IApiKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IAuthorizerRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IAuthorizerRef"

    @builtins.property
    @jsii.member(jsii_name="authorizerRef")
    def authorizer_ref(self) -> "AuthorizerReference":
        '''(experimental) A reference to a Authorizer resource.

        :stability: experimental
        '''
        return typing.cast("AuthorizerReference", jsii.get(self, "authorizerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAuthorizerRef).__jsii_proxy_class__ = lambda : _IAuthorizerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IBasePathMappingRef")
class IBasePathMappingRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BasePathMapping.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="basePathMappingRef")
    def base_path_mapping_ref(self) -> "BasePathMappingReference":
        '''(experimental) A reference to a BasePathMapping resource.

        :stability: experimental
        '''
        ...


class _IBasePathMappingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BasePathMapping.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IBasePathMappingRef"

    @builtins.property
    @jsii.member(jsii_name="basePathMappingRef")
    def base_path_mapping_ref(self) -> "BasePathMappingReference":
        '''(experimental) A reference to a BasePathMapping resource.

        :stability: experimental
        '''
        return typing.cast("BasePathMappingReference", jsii.get(self, "basePathMappingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBasePathMappingRef).__jsii_proxy_class__ = lambda : _IBasePathMappingRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IBasePathMappingV2Ref"
)
class IBasePathMappingV2Ref(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BasePathMappingV2.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="basePathMappingV2Ref")
    def base_path_mapping_v2_ref(self) -> "BasePathMappingV2Reference":
        '''(experimental) A reference to a BasePathMappingV2 resource.

        :stability: experimental
        '''
        ...


class _IBasePathMappingV2RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BasePathMappingV2.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IBasePathMappingV2Ref"

    @builtins.property
    @jsii.member(jsii_name="basePathMappingV2Ref")
    def base_path_mapping_v2_ref(self) -> "BasePathMappingV2Reference":
        '''(experimental) A reference to a BasePathMappingV2 resource.

        :stability: experimental
        '''
        return typing.cast("BasePathMappingV2Reference", jsii.get(self, "basePathMappingV2Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBasePathMappingV2Ref).__jsii_proxy_class__ = lambda : _IBasePathMappingV2RefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IClientCertificateRef"
)
class IClientCertificateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClientCertificate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clientCertificateRef")
    def client_certificate_ref(self) -> "ClientCertificateReference":
        '''(experimental) A reference to a ClientCertificate resource.

        :stability: experimental
        '''
        ...


class _IClientCertificateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClientCertificate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IClientCertificateRef"

    @builtins.property
    @jsii.member(jsii_name="clientCertificateRef")
    def client_certificate_ref(self) -> "ClientCertificateReference":
        '''(experimental) A reference to a ClientCertificate resource.

        :stability: experimental
        '''
        return typing.cast("ClientCertificateReference", jsii.get(self, "clientCertificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClientCertificateRef).__jsii_proxy_class__ = lambda : _IClientCertificateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IDeploymentRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IDeploymentRef"

    @builtins.property
    @jsii.member(jsii_name="deploymentRef")
    def deployment_ref(self) -> "DeploymentReference":
        '''(experimental) A reference to a Deployment resource.

        :stability: experimental
        '''
        return typing.cast("DeploymentReference", jsii.get(self, "deploymentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeploymentRef).__jsii_proxy_class__ = lambda : _IDeploymentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IDocumentationPartRef"
)
class IDocumentationPartRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentationPart.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="documentationPartRef")
    def documentation_part_ref(self) -> "DocumentationPartReference":
        '''(experimental) A reference to a DocumentationPart resource.

        :stability: experimental
        '''
        ...


class _IDocumentationPartRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentationPart.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IDocumentationPartRef"

    @builtins.property
    @jsii.member(jsii_name="documentationPartRef")
    def documentation_part_ref(self) -> "DocumentationPartReference":
        '''(experimental) A reference to a DocumentationPart resource.

        :stability: experimental
        '''
        return typing.cast("DocumentationPartReference", jsii.get(self, "documentationPartRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDocumentationPartRef).__jsii_proxy_class__ = lambda : _IDocumentationPartRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IDocumentationVersionRef"
)
class IDocumentationVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentationVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="documentationVersionRef")
    def documentation_version_ref(self) -> "DocumentationVersionReference":
        '''(experimental) A reference to a DocumentationVersion resource.

        :stability: experimental
        '''
        ...


class _IDocumentationVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentationVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IDocumentationVersionRef"

    @builtins.property
    @jsii.member(jsii_name="documentationVersionRef")
    def documentation_version_ref(self) -> "DocumentationVersionReference":
        '''(experimental) A reference to a DocumentationVersion resource.

        :stability: experimental
        '''
        return typing.cast("DocumentationVersionReference", jsii.get(self, "documentationVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDocumentationVersionRef).__jsii_proxy_class__ = lambda : _IDocumentationVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IDomainNameAccessAssociationRef"
)
class IDomainNameAccessAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DomainNameAccessAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainNameAccessAssociationRef")
    def domain_name_access_association_ref(
        self,
    ) -> "DomainNameAccessAssociationReference":
        '''(experimental) A reference to a DomainNameAccessAssociation resource.

        :stability: experimental
        '''
        ...


class _IDomainNameAccessAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DomainNameAccessAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IDomainNameAccessAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="domainNameAccessAssociationRef")
    def domain_name_access_association_ref(
        self,
    ) -> "DomainNameAccessAssociationReference":
        '''(experimental) A reference to a DomainNameAccessAssociation resource.

        :stability: experimental
        '''
        return typing.cast("DomainNameAccessAssociationReference", jsii.get(self, "domainNameAccessAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainNameAccessAssociationRef).__jsii_proxy_class__ = lambda : _IDomainNameAccessAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IDomainNameRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IDomainNameRef"

    @builtins.property
    @jsii.member(jsii_name="domainNameRef")
    def domain_name_ref(self) -> "DomainNameReference":
        '''(experimental) A reference to a DomainName resource.

        :stability: experimental
        '''
        return typing.cast("DomainNameReference", jsii.get(self, "domainNameRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainNameRef).__jsii_proxy_class__ = lambda : _IDomainNameRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IDomainNameV2Ref")
class IDomainNameV2Ref(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DomainNameV2.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainNameV2Ref")
    def domain_name_v2_ref(self) -> "DomainNameV2Reference":
        '''(experimental) A reference to a DomainNameV2 resource.

        :stability: experimental
        '''
        ...


class _IDomainNameV2RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DomainNameV2.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IDomainNameV2Ref"

    @builtins.property
    @jsii.member(jsii_name="domainNameV2Ref")
    def domain_name_v2_ref(self) -> "DomainNameV2Reference":
        '''(experimental) A reference to a DomainNameV2 resource.

        :stability: experimental
        '''
        return typing.cast("DomainNameV2Reference", jsii.get(self, "domainNameV2Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainNameV2Ref).__jsii_proxy_class__ = lambda : _IDomainNameV2RefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IGatewayResponseRef")
class IGatewayResponseRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GatewayResponse.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gatewayResponseRef")
    def gateway_response_ref(self) -> "GatewayResponseReference":
        '''(experimental) A reference to a GatewayResponse resource.

        :stability: experimental
        '''
        ...


class _IGatewayResponseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GatewayResponse.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IGatewayResponseRef"

    @builtins.property
    @jsii.member(jsii_name="gatewayResponseRef")
    def gateway_response_ref(self) -> "GatewayResponseReference":
        '''(experimental) A reference to a GatewayResponse resource.

        :stability: experimental
        '''
        return typing.cast("GatewayResponseReference", jsii.get(self, "gatewayResponseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGatewayResponseRef).__jsii_proxy_class__ = lambda : _IGatewayResponseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IMethodRef")
class IMethodRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Method.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="methodRef")
    def method_ref(self) -> "MethodReference":
        '''(experimental) A reference to a Method resource.

        :stability: experimental
        '''
        ...


class _IMethodRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Method.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IMethodRef"

    @builtins.property
    @jsii.member(jsii_name="methodRef")
    def method_ref(self) -> "MethodReference":
        '''(experimental) A reference to a Method resource.

        :stability: experimental
        '''
        return typing.cast("MethodReference", jsii.get(self, "methodRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMethodRef).__jsii_proxy_class__ = lambda : _IMethodRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IModelRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IModelRef"

    @builtins.property
    @jsii.member(jsii_name="modelRef")
    def model_ref(self) -> "ModelReference":
        '''(experimental) A reference to a Model resource.

        :stability: experimental
        '''
        return typing.cast("ModelReference", jsii.get(self, "modelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelRef).__jsii_proxy_class__ = lambda : _IModelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IRequestValidatorRef")
class IRequestValidatorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RequestValidator.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="requestValidatorRef")
    def request_validator_ref(self) -> "RequestValidatorReference":
        '''(experimental) A reference to a RequestValidator resource.

        :stability: experimental
        '''
        ...


class _IRequestValidatorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RequestValidator.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IRequestValidatorRef"

    @builtins.property
    @jsii.member(jsii_name="requestValidatorRef")
    def request_validator_ref(self) -> "RequestValidatorReference":
        '''(experimental) A reference to a RequestValidator resource.

        :stability: experimental
        '''
        return typing.cast("RequestValidatorReference", jsii.get(self, "requestValidatorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRequestValidatorRef).__jsii_proxy_class__ = lambda : _IRequestValidatorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IResourceRef")
class IResourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Resource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceRef")
    def resource_ref(self) -> "ResourceReference":
        '''(experimental) A reference to a Resource resource.

        :stability: experimental
        '''
        ...


class _IResourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Resource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IResourceRef"

    @builtins.property
    @jsii.member(jsii_name="resourceRef")
    def resource_ref(self) -> "ResourceReference":
        '''(experimental) A reference to a Resource resource.

        :stability: experimental
        '''
        return typing.cast("ResourceReference", jsii.get(self, "resourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceRef).__jsii_proxy_class__ = lambda : _IResourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IRestApiRef")
class IRestApiRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RestApi.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="restApiRef")
    def rest_api_ref(self) -> "RestApiReference":
        '''(experimental) A reference to a RestApi resource.

        :stability: experimental
        '''
        ...


class _IRestApiRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RestApi.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IRestApiRef"

    @builtins.property
    @jsii.member(jsii_name="restApiRef")
    def rest_api_ref(self) -> "RestApiReference":
        '''(experimental) A reference to a RestApi resource.

        :stability: experimental
        '''
        return typing.cast("RestApiReference", jsii.get(self, "restApiRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRestApiRef).__jsii_proxy_class__ = lambda : _IRestApiRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IStageRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IStageRef"

    @builtins.property
    @jsii.member(jsii_name="stageRef")
    def stage_ref(self) -> "StageReference":
        '''(experimental) A reference to a Stage resource.

        :stability: experimental
        '''
        return typing.cast("StageReference", jsii.get(self, "stageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStageRef).__jsii_proxy_class__ = lambda : _IStageRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IUsagePlanKeyRef")
class IUsagePlanKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UsagePlanKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="usagePlanKeyRef")
    def usage_plan_key_ref(self) -> "UsagePlanKeyReference":
        '''(experimental) A reference to a UsagePlanKey resource.

        :stability: experimental
        '''
        ...


class _IUsagePlanKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UsagePlanKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IUsagePlanKeyRef"

    @builtins.property
    @jsii.member(jsii_name="usagePlanKeyRef")
    def usage_plan_key_ref(self) -> "UsagePlanKeyReference":
        '''(experimental) A reference to a UsagePlanKey resource.

        :stability: experimental
        '''
        return typing.cast("UsagePlanKeyReference", jsii.get(self, "usagePlanKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUsagePlanKeyRef).__jsii_proxy_class__ = lambda : _IUsagePlanKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IUsagePlanRef")
class IUsagePlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UsagePlan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="usagePlanRef")
    def usage_plan_ref(self) -> "UsagePlanReference":
        '''(experimental) A reference to a UsagePlan resource.

        :stability: experimental
        '''
        ...


class _IUsagePlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UsagePlan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IUsagePlanRef"

    @builtins.property
    @jsii.member(jsii_name="usagePlanRef")
    def usage_plan_ref(self) -> "UsagePlanReference":
        '''(experimental) A reference to a UsagePlan resource.

        :stability: experimental
        '''
        return typing.cast("UsagePlanReference", jsii.get(self, "usagePlanRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUsagePlanRef).__jsii_proxy_class__ = lambda : _IUsagePlanRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apigateway.IVpcLinkRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apigateway.IVpcLinkRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.MethodReference",
    jsii_struct_bases=[],
    name_mapping={
        "http_method": "httpMethod",
        "resource_id": "resourceId",
        "rest_api_id": "restApiId",
    },
)
class MethodReference:
    def __init__(
        self,
        *,
        http_method: builtins.str,
        resource_id: builtins.str,
        rest_api_id: builtins.str,
    ) -> None:
        '''A reference to a Method resource.

        :param http_method: The HttpMethod of the Method resource.
        :param resource_id: The ResourceId of the Method resource.
        :param rest_api_id: The RestApiId of the Method resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            method_reference = interfaces_apigateway.MethodReference(
                http_method="httpMethod",
                resource_id="resourceId",
                rest_api_id="restApiId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5471de6448c6a98b106411dd178fa7fd8cb73c7dd1a3fef6529bbdf9997cc7f)
            check_type(argname="argument http_method", value=http_method, expected_type=type_hints["http_method"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "http_method": http_method,
            "resource_id": resource_id,
            "rest_api_id": rest_api_id,
        }

    @builtins.property
    def http_method(self) -> builtins.str:
        '''The HttpMethod of the Method resource.'''
        result = self._values.get("http_method")
        assert result is not None, "Required property 'http_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The ResourceId of the Method resource.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''The RestApiId of the Method resource.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MethodReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.ModelReference",
    jsii_struct_bases=[],
    name_mapping={"model_name": "modelName"},
)
class ModelReference:
    def __init__(self, *, model_name: builtins.str) -> None:
        '''A reference to a Model resource.

        :param model_name: The Name of the Model resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            model_reference = interfaces_apigateway.ModelReference(
                model_name="modelName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cfb24f7bc22c4ad00aa79fe8d034af1451928e06020737c3c4b7d883464dc74)
            check_type(argname="argument model_name", value=model_name, expected_type=type_hints["model_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_name": model_name,
        }

    @builtins.property
    def model_name(self) -> builtins.str:
        '''The Name of the Model resource.'''
        result = self._values.get("model_name")
        assert result is not None, "Required property 'model_name' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.RequestValidatorReference",
    jsii_struct_bases=[],
    name_mapping={"request_validator_id": "requestValidatorId"},
)
class RequestValidatorReference:
    def __init__(self, *, request_validator_id: builtins.str) -> None:
        '''A reference to a RequestValidator resource.

        :param request_validator_id: The RequestValidatorId of the RequestValidator resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            request_validator_reference = interfaces_apigateway.RequestValidatorReference(
                request_validator_id="requestValidatorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e1e9f49ce58c81e43ec3b2b2cd1bb6a576cc7b7a689517c6e0868806e589d54)
            check_type(argname="argument request_validator_id", value=request_validator_id, expected_type=type_hints["request_validator_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "request_validator_id": request_validator_id,
        }

    @builtins.property
    def request_validator_id(self) -> builtins.str:
        '''The RequestValidatorId of the RequestValidator resource.'''
        result = self._values.get("request_validator_id")
        assert result is not None, "Required property 'request_validator_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequestValidatorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.ResourceReference",
    jsii_struct_bases=[],
    name_mapping={"resource_id": "resourceId", "rest_api_id": "restApiId"},
)
class ResourceReference:
    def __init__(self, *, resource_id: builtins.str, rest_api_id: builtins.str) -> None:
        '''A reference to a Resource resource.

        :param resource_id: The ResourceId of the Resource resource.
        :param rest_api_id: The RestApiId of the Resource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            resource_reference = interfaces_apigateway.ResourceReference(
                resource_id="resourceId",
                rest_api_id="restApiId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c96766a4836c31a83c71f4581f65ba6df3d7168e8612c77be432a5231cc8a139)
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_id": resource_id,
            "rest_api_id": rest_api_id,
        }

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The ResourceId of the Resource resource.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''The RestApiId of the Resource resource.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.RestApiReference",
    jsii_struct_bases=[],
    name_mapping={"rest_api_id": "restApiId"},
)
class RestApiReference:
    def __init__(self, *, rest_api_id: builtins.str) -> None:
        '''A reference to a RestApi resource.

        :param rest_api_id: The RestApiId of the RestApi resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            rest_api_reference = interfaces_apigateway.RestApiReference(
                rest_api_id="restApiId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f50e97a7ff39a04a4cb7b5b1d56756f31a0bdc603e2bf040faff4e10d3db75cc)
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rest_api_id": rest_api_id,
        }

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''The RestApiId of the RestApi resource.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RestApiReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.StageReference",
    jsii_struct_bases=[],
    name_mapping={"rest_api_id": "restApiId", "stage_name": "stageName"},
)
class StageReference:
    def __init__(self, *, rest_api_id: builtins.str, stage_name: builtins.str) -> None:
        '''A reference to a Stage resource.

        :param rest_api_id: The RestApiId of the Stage resource.
        :param stage_name: The StageName of the Stage resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            stage_reference = interfaces_apigateway.StageReference(
                rest_api_id="restApiId",
                stage_name="stageName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd36a616e20efa65f223605e5bb009363951f1b892efd5b29bc5c17057ca4c05)
            check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
            check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rest_api_id": rest_api_id,
            "stage_name": stage_name,
        }

    @builtins.property
    def rest_api_id(self) -> builtins.str:
        '''The RestApiId of the Stage resource.'''
        result = self._values.get("rest_api_id")
        assert result is not None, "Required property 'rest_api_id' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.UsagePlanKeyReference",
    jsii_struct_bases=[],
    name_mapping={"usage_plan_key_id": "usagePlanKeyId"},
)
class UsagePlanKeyReference:
    def __init__(self, *, usage_plan_key_id: builtins.str) -> None:
        '''A reference to a UsagePlanKey resource.

        :param usage_plan_key_id: The Id of the UsagePlanKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            usage_plan_key_reference = interfaces_apigateway.UsagePlanKeyReference(
                usage_plan_key_id="usagePlanKeyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73eddfd8633befc6345b1dba1acc78cd212a7eab142b24d7c64aa4873edad449)
            check_type(argname="argument usage_plan_key_id", value=usage_plan_key_id, expected_type=type_hints["usage_plan_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "usage_plan_key_id": usage_plan_key_id,
        }

    @builtins.property
    def usage_plan_key_id(self) -> builtins.str:
        '''The Id of the UsagePlanKey resource.'''
        result = self._values.get("usage_plan_key_id")
        assert result is not None, "Required property 'usage_plan_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsagePlanKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.UsagePlanReference",
    jsii_struct_bases=[],
    name_mapping={"usage_plan_id": "usagePlanId"},
)
class UsagePlanReference:
    def __init__(self, *, usage_plan_id: builtins.str) -> None:
        '''A reference to a UsagePlan resource.

        :param usage_plan_id: The Id of the UsagePlan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            usage_plan_reference = interfaces_apigateway.UsagePlanReference(
                usage_plan_id="usagePlanId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bac89cc2201c9ebe8c37950d5404e6f0c1bbaf50fcf69202fddad94bb0dd24d)
            check_type(argname="argument usage_plan_id", value=usage_plan_id, expected_type=type_hints["usage_plan_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "usage_plan_id": usage_plan_id,
        }

    @builtins.property
    def usage_plan_id(self) -> builtins.str:
        '''The Id of the UsagePlan resource.'''
        result = self._values.get("usage_plan_id")
        assert result is not None, "Required property 'usage_plan_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsagePlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apigateway.VpcLinkReference",
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
            from aws_cdk.interfaces import aws_apigateway as interfaces_apigateway
            
            vpc_link_reference = interfaces_apigateway.VpcLinkReference(
                vpc_link_id="vpcLinkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8140e6df02e70da7a09adbdd959b7e3344c924f03a62ae10089f7e97c71385c8)
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
    "AccountReference",
    "ApiKeyReference",
    "AuthorizerReference",
    "BasePathMappingReference",
    "BasePathMappingV2Reference",
    "ClientCertificateReference",
    "DeploymentReference",
    "DocumentationPartReference",
    "DocumentationVersionReference",
    "DomainNameAccessAssociationReference",
    "DomainNameReference",
    "DomainNameV2Reference",
    "GatewayResponseReference",
    "IAccountRef",
    "IApiKeyRef",
    "IAuthorizerRef",
    "IBasePathMappingRef",
    "IBasePathMappingV2Ref",
    "IClientCertificateRef",
    "IDeploymentRef",
    "IDocumentationPartRef",
    "IDocumentationVersionRef",
    "IDomainNameAccessAssociationRef",
    "IDomainNameRef",
    "IDomainNameV2Ref",
    "IGatewayResponseRef",
    "IMethodRef",
    "IModelRef",
    "IRequestValidatorRef",
    "IResourceRef",
    "IRestApiRef",
    "IStageRef",
    "IUsagePlanKeyRef",
    "IUsagePlanRef",
    "IVpcLinkRef",
    "MethodReference",
    "ModelReference",
    "RequestValidatorReference",
    "ResourceReference",
    "RestApiReference",
    "StageReference",
    "UsagePlanKeyReference",
    "UsagePlanReference",
    "VpcLinkReference",
]

publication.publish()

def _typecheckingstub__35ad850c85a8d4afdd663227c7e32f94d8450f981a615d04890e872b21d1612d(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c14fb5f90c77f82575a97f9a173c3410680639b45caef1bb8b8672340b4bf31(
    *,
    api_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d68d6630cf7fd51cb53d1150a586c3b490adb4d029b8db237f87f6cfd3208191(
    *,
    authorizer_id: builtins.str,
    rest_api_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6766e0e75fadfc941acafb7116bc52e0ea2debd27cb810b19e5837efdb4b86e3(
    *,
    base_path: builtins.str,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f95b02fe81974b197f19290ec8ad7f11678477fb4eeab26fec56c0fb5351a850(
    *,
    base_path_mapping_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__833a4d31ace847ad4f8acfb3dd6ddac7e3fac64f42670367da4e70d2e3263a09(
    *,
    client_certificate_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41df7edc09bfa35e6c0eb5233570b5f5d4e6d255375a85ba37230fa1fbc86540(
    *,
    deployment_id: builtins.str,
    rest_api_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e560572f2b89e2ef2cf9d7b126db3ad6fac6770ea3c3de34b5b45e76ed0fd4e9(
    *,
    documentation_part_id: builtins.str,
    rest_api_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe125bb5075aaf5d4213def6adf1eff51805a5ca591bf88080533e0f6fad9b2(
    *,
    documentation_version: builtins.str,
    rest_api_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6106393b25c71c75f181d6e2216433d64ca457d3aa5346d3c08c9c5c8f76ccb9(
    *,
    domain_name_access_association_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3cfd08bdbde02f2db8ac69a08bf7a53178de565b3b2d57297f61f0af460b23c(
    *,
    domain_name: builtins.str,
    domain_name_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efdeb9f0ad3160236b8f4e14e4cdf544ab705171d9308fa88175fa01b8d92c49(
    *,
    domain_name_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0794adc65f2a9a99dd04ff2f904cf838d512203fc37eac299e09871ce11fe9f(
    *,
    gateway_response_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5471de6448c6a98b106411dd178fa7fd8cb73c7dd1a3fef6529bbdf9997cc7f(
    *,
    http_method: builtins.str,
    resource_id: builtins.str,
    rest_api_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cfb24f7bc22c4ad00aa79fe8d034af1451928e06020737c3c4b7d883464dc74(
    *,
    model_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e1e9f49ce58c81e43ec3b2b2cd1bb6a576cc7b7a689517c6e0868806e589d54(
    *,
    request_validator_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c96766a4836c31a83c71f4581f65ba6df3d7168e8612c77be432a5231cc8a139(
    *,
    resource_id: builtins.str,
    rest_api_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f50e97a7ff39a04a4cb7b5b1d56756f31a0bdc603e2bf040faff4e10d3db75cc(
    *,
    rest_api_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd36a616e20efa65f223605e5bb009363951f1b892efd5b29bc5c17057ca4c05(
    *,
    rest_api_id: builtins.str,
    stage_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73eddfd8633befc6345b1dba1acc78cd212a7eab142b24d7c64aa4873edad449(
    *,
    usage_plan_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bac89cc2201c9ebe8c37950d5404e6f0c1bbaf50fcf69202fddad94bb0dd24d(
    *,
    usage_plan_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8140e6df02e70da7a09adbdd959b7e3344c924f03a62ae10089f7e97c71385c8(
    *,
    vpc_link_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccountRef, IApiKeyRef, IAuthorizerRef, IBasePathMappingRef, IBasePathMappingV2Ref, IClientCertificateRef, IDeploymentRef, IDocumentationPartRef, IDocumentationVersionRef, IDomainNameAccessAssociationRef, IDomainNameRef, IDomainNameV2Ref, IGatewayResponseRef, IMethodRef, IModelRef, IRequestValidatorRef, IResourceRef, IRestApiRef, IStageRef, IUsagePlanKeyRef, IUsagePlanRef, IVpcLinkRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
