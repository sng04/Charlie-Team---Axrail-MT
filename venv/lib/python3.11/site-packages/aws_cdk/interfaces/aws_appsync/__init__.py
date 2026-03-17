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
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.ApiCacheReference",
    jsii_struct_bases=[],
    name_mapping={"api_cache_id": "apiCacheId"},
)
class ApiCacheReference:
    def __init__(self, *, api_cache_id: builtins.str) -> None:
        '''A reference to a ApiCache resource.

        :param api_cache_id: The Id of the ApiCache resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            api_cache_reference = interfaces_appsync.ApiCacheReference(
                api_cache_id="apiCacheId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d2fc7495b4465ad3e37604f75a0bdb55af526cf724ce569c848502d42c82cd)
            check_type(argname="argument api_cache_id", value=api_cache_id, expected_type=type_hints["api_cache_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_cache_id": api_cache_id,
        }

    @builtins.property
    def api_cache_id(self) -> builtins.str:
        '''The Id of the ApiCache resource.'''
        result = self._values.get("api_cache_id")
        assert result is not None, "Required property 'api_cache_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiCacheReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.ApiKeyReference",
    jsii_struct_bases=[],
    name_mapping={"api_key_arn": "apiKeyArn"},
)
class ApiKeyReference:
    def __init__(self, *, api_key_arn: builtins.str) -> None:
        '''A reference to a ApiKey resource.

        :param api_key_arn: The Arn of the ApiKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            api_key_reference = interfaces_appsync.ApiKeyReference(
                api_key_arn="apiKeyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89c61b6d09e514f3580cb56bddf0fff5b1a35bd5f8b47cb4d6faa952954159c)
            check_type(argname="argument api_key_arn", value=api_key_arn, expected_type=type_hints["api_key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_key_arn": api_key_arn,
        }

    @builtins.property
    def api_key_arn(self) -> builtins.str:
        '''The Arn of the ApiKey resource.'''
        result = self._values.get("api_key_arn")
        assert result is not None, "Required property 'api_key_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.ApiReference",
    jsii_struct_bases=[],
    name_mapping={"api_arn": "apiArn"},
)
class ApiReference:
    def __init__(self, *, api_arn: builtins.str) -> None:
        '''A reference to a Api resource.

        :param api_arn: The ApiArn of the Api resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            api_reference = interfaces_appsync.ApiReference(
                api_arn="apiArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79c8673410d4f38d33e05a1bcd3d854adaf75733b4070c8fcabb34002bdd2838)
            check_type(argname="argument api_arn", value=api_arn, expected_type=type_hints["api_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_arn": api_arn,
        }

    @builtins.property
    def api_arn(self) -> builtins.str:
        '''The ApiArn of the Api resource.'''
        result = self._values.get("api_arn")
        assert result is not None, "Required property 'api_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.ChannelNamespaceReference",
    jsii_struct_bases=[],
    name_mapping={"channel_namespace_arn": "channelNamespaceArn"},
)
class ChannelNamespaceReference:
    def __init__(self, *, channel_namespace_arn: builtins.str) -> None:
        '''A reference to a ChannelNamespace resource.

        :param channel_namespace_arn: The ChannelNamespaceArn of the ChannelNamespace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            channel_namespace_reference = interfaces_appsync.ChannelNamespaceReference(
                channel_namespace_arn="channelNamespaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4450879002d785ef94c98f23cc335833b8852c62ed261a313f4ea3e8be23c4d5)
            check_type(argname="argument channel_namespace_arn", value=channel_namespace_arn, expected_type=type_hints["channel_namespace_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_namespace_arn": channel_namespace_arn,
        }

    @builtins.property
    def channel_namespace_arn(self) -> builtins.str:
        '''The ChannelNamespaceArn of the ChannelNamespace resource.'''
        result = self._values.get("channel_namespace_arn")
        assert result is not None, "Required property 'channel_namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelNamespaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.DataSourceReference",
    jsii_struct_bases=[],
    name_mapping={"data_source_arn": "dataSourceArn"},
)
class DataSourceReference:
    def __init__(self, *, data_source_arn: builtins.str) -> None:
        '''A reference to a DataSource resource.

        :param data_source_arn: The DataSourceArn of the DataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            data_source_reference = interfaces_appsync.DataSourceReference(
                data_source_arn="dataSourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3227f14688841f561fb95f56506b30d5d07adc83cd02cae423fb780c2a4d0ff)
            check_type(argname="argument data_source_arn", value=data_source_arn, expected_type=type_hints["data_source_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_arn": data_source_arn,
        }

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The DataSourceArn of the DataSource resource.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.DomainNameApiAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"api_association_identifier": "apiAssociationIdentifier"},
)
class DomainNameApiAssociationReference:
    def __init__(self, *, api_association_identifier: builtins.str) -> None:
        '''A reference to a DomainNameApiAssociation resource.

        :param api_association_identifier: The ApiAssociationIdentifier of the DomainNameApiAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            domain_name_api_association_reference = interfaces_appsync.DomainNameApiAssociationReference(
                api_association_identifier="apiAssociationIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e103b7d7d36de9f5882ad4406c8f135e6cecc8febc8fc79d7498edfe5c220e9)
            check_type(argname="argument api_association_identifier", value=api_association_identifier, expected_type=type_hints["api_association_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_association_identifier": api_association_identifier,
        }

    @builtins.property
    def api_association_identifier(self) -> builtins.str:
        '''The ApiAssociationIdentifier of the DomainNameApiAssociation resource.'''
        result = self._values.get("api_association_identifier")
        assert result is not None, "Required property 'api_association_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainNameApiAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.DomainNameReference",
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
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            domain_name_reference = interfaces_appsync.DomainNameReference(
                domain_name="domainName",
                domain_name_arn="domainNameArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d732985caffdd497b3ed4a91d071287c5f1c81bd5d8da79491b8bc806d43ff2e)
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
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.FunctionConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class FunctionConfigurationReference:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''A reference to a FunctionConfiguration resource.

        :param function_arn: The FunctionArn of the FunctionConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            function_configuration_reference = interfaces_appsync.FunctionConfigurationReference(
                function_arn="functionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__584cd85e85f52dd14687b3606b5f2e19f0f582d52dd451ec04ae6328b78a8a4e)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''The FunctionArn of the FunctionConfiguration resource.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.GraphQLApiReference",
    jsii_struct_bases=[],
    name_mapping={"graph_ql_api_arn": "graphQlApiArn"},
)
class GraphQLApiReference:
    def __init__(self, *, graph_ql_api_arn: builtins.str) -> None:
        '''A reference to a GraphQLApi resource.

        :param graph_ql_api_arn: The Arn of the GraphQLApi resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            graph_qLApi_reference = interfaces_appsync.GraphQLApiReference(
                graph_ql_api_arn="graphQlApiArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa4e6b2e6fad1b9dc5f2e746d6cf8738451a7c872f4d279c7ddf3b646087638)
            check_type(argname="argument graph_ql_api_arn", value=graph_ql_api_arn, expected_type=type_hints["graph_ql_api_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_ql_api_arn": graph_ql_api_arn,
        }

    @builtins.property
    def graph_ql_api_arn(self) -> builtins.str:
        '''The Arn of the GraphQLApi resource.'''
        result = self._values.get("graph_ql_api_arn")
        assert result is not None, "Required property 'graph_ql_api_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphQLApiReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.GraphQLSchemaReference",
    jsii_struct_bases=[],
    name_mapping={"graph_ql_schema_id": "graphQlSchemaId"},
)
class GraphQLSchemaReference:
    def __init__(self, *, graph_ql_schema_id: builtins.str) -> None:
        '''A reference to a GraphQLSchema resource.

        :param graph_ql_schema_id: The Id of the GraphQLSchema resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            graph_qLSchema_reference = interfaces_appsync.GraphQLSchemaReference(
                graph_ql_schema_id="graphQlSchemaId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bd5dd571f8b4430135f6ef4b48f3b83f94c2b988c05c45786a6a73ff7bc4a03)
            check_type(argname="argument graph_ql_schema_id", value=graph_ql_schema_id, expected_type=type_hints["graph_ql_schema_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_ql_schema_id": graph_ql_schema_id,
        }

    @builtins.property
    def graph_ql_schema_id(self) -> builtins.str:
        '''The Id of the GraphQLSchema resource.'''
        result = self._values.get("graph_ql_schema_id")
        assert result is not None, "Required property 'graph_ql_schema_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphQLSchemaReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appsync.IApiCacheRef")
class IApiCacheRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApiCache.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiCacheRef")
    def api_cache_ref(self) -> "ApiCacheReference":
        '''(experimental) A reference to a ApiCache resource.

        :stability: experimental
        '''
        ...


class _IApiCacheRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApiCache.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IApiCacheRef"

    @builtins.property
    @jsii.member(jsii_name="apiCacheRef")
    def api_cache_ref(self) -> "ApiCacheReference":
        '''(experimental) A reference to a ApiCache resource.

        :stability: experimental
        '''
        return typing.cast("ApiCacheReference", jsii.get(self, "apiCacheRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiCacheRef).__jsii_proxy_class__ = lambda : _IApiCacheRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appsync.IApiKeyRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IApiKeyRef"

    @builtins.property
    @jsii.member(jsii_name="apiKeyRef")
    def api_key_ref(self) -> "ApiKeyReference":
        '''(experimental) A reference to a ApiKey resource.

        :stability: experimental
        '''
        return typing.cast("ApiKeyReference", jsii.get(self, "apiKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiKeyRef).__jsii_proxy_class__ = lambda : _IApiKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appsync.IApiRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IApiRef"

    @builtins.property
    @jsii.member(jsii_name="apiRef")
    def api_ref(self) -> "ApiReference":
        '''(experimental) A reference to a Api resource.

        :stability: experimental
        '''
        return typing.cast("ApiReference", jsii.get(self, "apiRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiRef).__jsii_proxy_class__ = lambda : _IApiRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appsync.IChannelNamespaceRef")
class IChannelNamespaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelNamespace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelNamespaceRef")
    def channel_namespace_ref(self) -> "ChannelNamespaceReference":
        '''(experimental) A reference to a ChannelNamespace resource.

        :stability: experimental
        '''
        ...


class _IChannelNamespaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelNamespace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IChannelNamespaceRef"

    @builtins.property
    @jsii.member(jsii_name="channelNamespaceRef")
    def channel_namespace_ref(self) -> "ChannelNamespaceReference":
        '''(experimental) A reference to a ChannelNamespace resource.

        :stability: experimental
        '''
        return typing.cast("ChannelNamespaceReference", jsii.get(self, "channelNamespaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelNamespaceRef).__jsii_proxy_class__ = lambda : _IChannelNamespaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appsync.IDataSourceRef")
class IDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        ...


class _IDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        return typing.cast("DataSourceReference", jsii.get(self, "dataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSourceRef).__jsii_proxy_class__ = lambda : _IDataSourceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.IDomainNameApiAssociationRef"
)
class IDomainNameApiAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DomainNameApiAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainNameApiAssociationRef")
    def domain_name_api_association_ref(self) -> "DomainNameApiAssociationReference":
        '''(experimental) A reference to a DomainNameApiAssociation resource.

        :stability: experimental
        '''
        ...


class _IDomainNameApiAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DomainNameApiAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IDomainNameApiAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="domainNameApiAssociationRef")
    def domain_name_api_association_ref(self) -> "DomainNameApiAssociationReference":
        '''(experimental) A reference to a DomainNameApiAssociation resource.

        :stability: experimental
        '''
        return typing.cast("DomainNameApiAssociationReference", jsii.get(self, "domainNameApiAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainNameApiAssociationRef).__jsii_proxy_class__ = lambda : _IDomainNameApiAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appsync.IDomainNameRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IDomainNameRef"

    @builtins.property
    @jsii.member(jsii_name="domainNameRef")
    def domain_name_ref(self) -> "DomainNameReference":
        '''(experimental) A reference to a DomainName resource.

        :stability: experimental
        '''
        return typing.cast("DomainNameReference", jsii.get(self, "domainNameRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainNameRef).__jsii_proxy_class__ = lambda : _IDomainNameRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.IFunctionConfigurationRef"
)
class IFunctionConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FunctionConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="functionConfigurationRef")
    def function_configuration_ref(self) -> "FunctionConfigurationReference":
        '''(experimental) A reference to a FunctionConfiguration resource.

        :stability: experimental
        '''
        ...


class _IFunctionConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FunctionConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IFunctionConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="functionConfigurationRef")
    def function_configuration_ref(self) -> "FunctionConfigurationReference":
        '''(experimental) A reference to a FunctionConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("FunctionConfigurationReference", jsii.get(self, "functionConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFunctionConfigurationRef).__jsii_proxy_class__ = lambda : _IFunctionConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appsync.IGraphQLApiRef")
class IGraphQLApiRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GraphQLApi.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="graphQlApiRef")
    def graph_ql_api_ref(self) -> "GraphQLApiReference":
        '''(experimental) A reference to a GraphQLApi resource.

        :stability: experimental
        '''
        ...


class _IGraphQLApiRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GraphQLApi.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IGraphQLApiRef"

    @builtins.property
    @jsii.member(jsii_name="graphQlApiRef")
    def graph_ql_api_ref(self) -> "GraphQLApiReference":
        '''(experimental) A reference to a GraphQLApi resource.

        :stability: experimental
        '''
        return typing.cast("GraphQLApiReference", jsii.get(self, "graphQlApiRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphQLApiRef).__jsii_proxy_class__ = lambda : _IGraphQLApiRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appsync.IGraphQLSchemaRef")
class IGraphQLSchemaRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GraphQLSchema.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="graphQlSchemaRef")
    def graph_ql_schema_ref(self) -> "GraphQLSchemaReference":
        '''(experimental) A reference to a GraphQLSchema resource.

        :stability: experimental
        '''
        ...


class _IGraphQLSchemaRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GraphQLSchema.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IGraphQLSchemaRef"

    @builtins.property
    @jsii.member(jsii_name="graphQlSchemaRef")
    def graph_ql_schema_ref(self) -> "GraphQLSchemaReference":
        '''(experimental) A reference to a GraphQLSchema resource.

        :stability: experimental
        '''
        return typing.cast("GraphQLSchemaReference", jsii.get(self, "graphQlSchemaRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphQLSchemaRef).__jsii_proxy_class__ = lambda : _IGraphQLSchemaRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appsync.IResolverRef")
class IResolverRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Resolver.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resolverRef")
    def resolver_ref(self) -> "ResolverReference":
        '''(experimental) A reference to a Resolver resource.

        :stability: experimental
        '''
        ...


class _IResolverRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Resolver.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.IResolverRef"

    @builtins.property
    @jsii.member(jsii_name="resolverRef")
    def resolver_ref(self) -> "ResolverReference":
        '''(experimental) A reference to a Resolver resource.

        :stability: experimental
        '''
        return typing.cast("ResolverReference", jsii.get(self, "resolverRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolverRef).__jsii_proxy_class__ = lambda : _IResolverRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.ISourceApiAssociationRef"
)
class ISourceApiAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SourceApiAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sourceApiAssociationRef")
    def source_api_association_ref(self) -> "SourceApiAssociationReference":
        '''(experimental) A reference to a SourceApiAssociation resource.

        :stability: experimental
        '''
        ...


class _ISourceApiAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SourceApiAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appsync.ISourceApiAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="sourceApiAssociationRef")
    def source_api_association_ref(self) -> "SourceApiAssociationReference":
        '''(experimental) A reference to a SourceApiAssociation resource.

        :stability: experimental
        '''
        return typing.cast("SourceApiAssociationReference", jsii.get(self, "sourceApiAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISourceApiAssociationRef).__jsii_proxy_class__ = lambda : _ISourceApiAssociationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.ResolverReference",
    jsii_struct_bases=[],
    name_mapping={"resolver_arn": "resolverArn"},
)
class ResolverReference:
    def __init__(self, *, resolver_arn: builtins.str) -> None:
        '''A reference to a Resolver resource.

        :param resolver_arn: The ResolverArn of the Resolver resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            resolver_reference = interfaces_appsync.ResolverReference(
                resolver_arn="resolverArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92812c768af3e2f0949ca7f27bab78cb1a391010cbc482a7165bedce5ad96a40)
            check_type(argname="argument resolver_arn", value=resolver_arn, expected_type=type_hints["resolver_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resolver_arn": resolver_arn,
        }

    @builtins.property
    def resolver_arn(self) -> builtins.str:
        '''The ResolverArn of the Resolver resource.'''
        result = self._values.get("resolver_arn")
        assert result is not None, "Required property 'resolver_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appsync.SourceApiAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"association_arn": "associationArn"},
)
class SourceApiAssociationReference:
    def __init__(self, *, association_arn: builtins.str) -> None:
        '''A reference to a SourceApiAssociation resource.

        :param association_arn: The AssociationArn of the SourceApiAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appsync as interfaces_appsync
            
            source_api_association_reference = interfaces_appsync.SourceApiAssociationReference(
                association_arn="associationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79171cb2db974a7a2cf1f2fad295ec20b2577e125e56dd0209f349de14212d00)
            check_type(argname="argument association_arn", value=association_arn, expected_type=type_hints["association_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_arn": association_arn,
        }

    @builtins.property
    def association_arn(self) -> builtins.str:
        '''The AssociationArn of the SourceApiAssociation resource.'''
        result = self._values.get("association_arn")
        assert result is not None, "Required property 'association_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceApiAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiCacheReference",
    "ApiKeyReference",
    "ApiReference",
    "ChannelNamespaceReference",
    "DataSourceReference",
    "DomainNameApiAssociationReference",
    "DomainNameReference",
    "FunctionConfigurationReference",
    "GraphQLApiReference",
    "GraphQLSchemaReference",
    "IApiCacheRef",
    "IApiKeyRef",
    "IApiRef",
    "IChannelNamespaceRef",
    "IDataSourceRef",
    "IDomainNameApiAssociationRef",
    "IDomainNameRef",
    "IFunctionConfigurationRef",
    "IGraphQLApiRef",
    "IGraphQLSchemaRef",
    "IResolverRef",
    "ISourceApiAssociationRef",
    "ResolverReference",
    "SourceApiAssociationReference",
]

publication.publish()

def _typecheckingstub__02d2fc7495b4465ad3e37604f75a0bdb55af526cf724ce569c848502d42c82cd(
    *,
    api_cache_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89c61b6d09e514f3580cb56bddf0fff5b1a35bd5f8b47cb4d6faa952954159c(
    *,
    api_key_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c8673410d4f38d33e05a1bcd3d854adaf75733b4070c8fcabb34002bdd2838(
    *,
    api_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4450879002d785ef94c98f23cc335833b8852c62ed261a313f4ea3e8be23c4d5(
    *,
    channel_namespace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3227f14688841f561fb95f56506b30d5d07adc83cd02cae423fb780c2a4d0ff(
    *,
    data_source_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e103b7d7d36de9f5882ad4406c8f135e6cecc8febc8fc79d7498edfe5c220e9(
    *,
    api_association_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d732985caffdd497b3ed4a91d071287c5f1c81bd5d8da79491b8bc806d43ff2e(
    *,
    domain_name: builtins.str,
    domain_name_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__584cd85e85f52dd14687b3606b5f2e19f0f582d52dd451ec04ae6328b78a8a4e(
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa4e6b2e6fad1b9dc5f2e746d6cf8738451a7c872f4d279c7ddf3b646087638(
    *,
    graph_ql_api_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bd5dd571f8b4430135f6ef4b48f3b83f94c2b988c05c45786a6a73ff7bc4a03(
    *,
    graph_ql_schema_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92812c768af3e2f0949ca7f27bab78cb1a391010cbc482a7165bedce5ad96a40(
    *,
    resolver_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79171cb2db974a7a2cf1f2fad295ec20b2577e125e56dd0209f349de14212d00(
    *,
    association_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApiCacheRef, IApiKeyRef, IApiRef, IChannelNamespaceRef, IDataSourceRef, IDomainNameApiAssociationRef, IDomainNameRef, IFunctionConfigurationRef, IGraphQLApiRef, IGraphQLSchemaRef, IResolverRef, ISourceApiAssociationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
