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
    jsii_type="aws-cdk-lib.interfaces.aws_codepipeline.CustomActionTypeReference",
    jsii_struct_bases=[],
    name_mapping={
        "category": "category",
        "provider": "provider",
        "version": "version",
    },
)
class CustomActionTypeReference:
    def __init__(
        self,
        *,
        category: builtins.str,
        provider: builtins.str,
        version: builtins.str,
    ) -> None:
        '''A reference to a CustomActionType resource.

        :param category: The Category of the CustomActionType resource.
        :param provider: The Provider of the CustomActionType resource.
        :param version: The Version of the CustomActionType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codepipeline as interfaces_codepipeline
            
            custom_action_type_reference = interfaces_codepipeline.CustomActionTypeReference(
                category="category",
                provider="provider",
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92f86c00e45a61fb81c94d6efcc7b15211b3c4c43e0ec65aa654975593bc6272)
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "category": category,
            "provider": provider,
            "version": version,
        }

    @builtins.property
    def category(self) -> builtins.str:
        '''The Category of the CustomActionType resource.'''
        result = self._values.get("category")
        assert result is not None, "Required property 'category' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provider(self) -> builtins.str:
        '''The Provider of the CustomActionType resource.'''
        result = self._values.get("provider")
        assert result is not None, "Required property 'provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The Version of the CustomActionType resource.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomActionTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_codepipeline.ICustomActionTypeRef"
)
class ICustomActionTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomActionType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customActionTypeRef")
    def custom_action_type_ref(self) -> "CustomActionTypeReference":
        '''(experimental) A reference to a CustomActionType resource.

        :stability: experimental
        '''
        ...


class _ICustomActionTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomActionType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codepipeline.ICustomActionTypeRef"

    @builtins.property
    @jsii.member(jsii_name="customActionTypeRef")
    def custom_action_type_ref(self) -> "CustomActionTypeReference":
        '''(experimental) A reference to a CustomActionType resource.

        :stability: experimental
        '''
        return typing.cast("CustomActionTypeReference", jsii.get(self, "customActionTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomActionTypeRef).__jsii_proxy_class__ = lambda : _ICustomActionTypeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codepipeline.IPipelineRef")
class IPipelineRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Pipeline.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pipelineRef")
    def pipeline_ref(self) -> "PipelineReference":
        '''(experimental) A reference to a Pipeline resource.

        :stability: experimental
        '''
        ...


class _IPipelineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Pipeline.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codepipeline.IPipelineRef"

    @builtins.property
    @jsii.member(jsii_name="pipelineRef")
    def pipeline_ref(self) -> "PipelineReference":
        '''(experimental) A reference to a Pipeline resource.

        :stability: experimental
        '''
        return typing.cast("PipelineReference", jsii.get(self, "pipelineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPipelineRef).__jsii_proxy_class__ = lambda : _IPipelineRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codepipeline.IWebhookRef")
class IWebhookRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Webhook.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="webhookRef")
    def webhook_ref(self) -> "WebhookReference":
        '''(experimental) A reference to a Webhook resource.

        :stability: experimental
        '''
        ...


class _IWebhookRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Webhook.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codepipeline.IWebhookRef"

    @builtins.property
    @jsii.member(jsii_name="webhookRef")
    def webhook_ref(self) -> "WebhookReference":
        '''(experimental) A reference to a Webhook resource.

        :stability: experimental
        '''
        return typing.cast("WebhookReference", jsii.get(self, "webhookRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWebhookRef).__jsii_proxy_class__ = lambda : _IWebhookRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codepipeline.PipelineReference",
    jsii_struct_bases=[],
    name_mapping={"pipeline_name": "pipelineName"},
)
class PipelineReference:
    def __init__(self, *, pipeline_name: builtins.str) -> None:
        '''A reference to a Pipeline resource.

        :param pipeline_name: The Name of the Pipeline resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codepipeline as interfaces_codepipeline
            
            pipeline_reference = interfaces_codepipeline.PipelineReference(
                pipeline_name="pipelineName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa099517d79cc704f4edb70aa548901841938ff855915f72a8b83d5ffd3cc124)
            check_type(argname="argument pipeline_name", value=pipeline_name, expected_type=type_hints["pipeline_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pipeline_name": pipeline_name,
        }

    @builtins.property
    def pipeline_name(self) -> builtins.str:
        '''The Name of the Pipeline resource.'''
        result = self._values.get("pipeline_name")
        assert result is not None, "Required property 'pipeline_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codepipeline.WebhookReference",
    jsii_struct_bases=[],
    name_mapping={"webhook_name": "webhookName"},
)
class WebhookReference:
    def __init__(self, *, webhook_name: builtins.str) -> None:
        '''A reference to a Webhook resource.

        :param webhook_name: The Name of the Webhook resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codepipeline as interfaces_codepipeline
            
            webhook_reference = interfaces_codepipeline.WebhookReference(
                webhook_name="webhookName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9bf91bcd59a23afc69aebe9df6f0e55e1421bec01f1ae86241d173c8d51a7ae)
            check_type(argname="argument webhook_name", value=webhook_name, expected_type=type_hints["webhook_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "webhook_name": webhook_name,
        }

    @builtins.property
    def webhook_name(self) -> builtins.str:
        '''The Name of the Webhook resource.'''
        result = self._values.get("webhook_name")
        assert result is not None, "Required property 'webhook_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebhookReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CustomActionTypeReference",
    "ICustomActionTypeRef",
    "IPipelineRef",
    "IWebhookRef",
    "PipelineReference",
    "WebhookReference",
]

publication.publish()

def _typecheckingstub__92f86c00e45a61fb81c94d6efcc7b15211b3c4c43e0ec65aa654975593bc6272(
    *,
    category: builtins.str,
    provider: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa099517d79cc704f4edb70aa548901841938ff855915f72a8b83d5ffd3cc124(
    *,
    pipeline_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9bf91bcd59a23afc69aebe9df6f0e55e1421bec01f1ae86241d173c8d51a7ae(
    *,
    webhook_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICustomActionTypeRef, IPipelineRef, IWebhookRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
