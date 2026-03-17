r'''
# AWS::AppIntegrations Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_appintegrations as appintegrations
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AppIntegrations construct libraries](https://constructs.dev/search?q=appintegrations)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AppIntegrations resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppIntegrations.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AppIntegrations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppIntegrations.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
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

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_appintegrations import (
    ApplicationReference as _ApplicationReference_eb7f83ac,
    DataIntegrationReference as _DataIntegrationReference_82094d23,
    EventIntegrationReference as _EventIntegrationReference_2d3a8ab8,
    IApplicationRef as _IApplicationRef_f88446ed,
    IDataIntegrationRef as _IDataIntegrationRef_c5e65586,
    IEventIntegrationRef as _IEventIntegrationRef_d2c58e8f,
)


@jsii.implements(_IInspectable_c2943556, _IApplicationRef_f88446ed, _ITaggableV2_4e6798f8)
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnApplication",
):
    '''Creates and persists an Application resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html
    :cloudformationResource: AWS::AppIntegrations::Application
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appintegrations as appintegrations
        
        cfn_application = appintegrations.CfnApplication(self, "MyCfnApplication",
            application_source_config=appintegrations.CfnApplication.ApplicationSourceConfigProperty(
                external_url_config=appintegrations.CfnApplication.ExternalUrlConfigProperty(
                    access_url="accessUrl",
        
                    # the properties below are optional
                    approved_origins=["approvedOrigins"]
                )
            ),
            description="description",
            name="name",
            namespace="namespace",
        
            # the properties below are optional
            application_config=appintegrations.CfnApplication.ApplicationConfigProperty(
                contact_handling=appintegrations.CfnApplication.ContactHandlingProperty(
                    scope="scope"
                )
            ),
            iframe_config=appintegrations.CfnApplication.IframeConfigProperty(
                allow=["allow"],
                sandbox=["sandbox"]
            ),
            initialization_timeout=123,
            is_service=False,
            permissions=["permissions"],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        application_source_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.ApplicationSourceConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        description: builtins.str,
        name: builtins.str,
        namespace: builtins.str,
        application_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.ApplicationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        iframe_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.IframeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        initialization_timeout: typing.Optional[jsii.Number] = None,
        is_service: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AppIntegrations::Application``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_source_config: The configuration for where the application should be loaded from.
        :param description: The description of the application.
        :param name: The name of the application.
        :param namespace: The namespace of the application.
        :param application_config: 
        :param iframe_config: 
        :param initialization_timeout: The initialization timeout in milliseconds. Required when IsService is true.
        :param is_service: Indicates whether the application is a service. Default: - false
        :param permissions: The configuration of events or requests that the application has access to.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c1bbb1e03e672595eb80bdb7dcb70bb6e71fccf39633133ee8a5b86b6874772)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            application_source_config=application_source_config,
            description=description,
            name=name,
            namespace=namespace,
            application_config=application_config,
            iframe_config=iframe_config,
            initialization_timeout=initialization_timeout,
            is_service=is_service,
            permissions=permissions,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForApplication")
    @builtins.classmethod
    def arn_for_application(cls, resource: "_IApplicationRef_f88446ed") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b42f16ecbbfeacf4cebf72ced2a17f07f5a84908315be11f343c633d7813dc0)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForApplication", [resource]))

    @jsii.member(jsii_name="isCfnApplication")
    @builtins.classmethod
    def is_cfn_application(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnApplication.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b4e08f6d9252ec685994e80dfaccf256affaf78836001fbb59695c3e4fec6c4)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnApplication", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2397143274609e6f7787d10c8effb0139785b91de02a335ac411b9f6e4478fb6)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f2b0f5530bab214011baa3953ec2f0059bf19c5005c20b1a37a58186c8d1c94)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "_ApplicationReference_eb7f83ac":
        '''A reference to a Application resource.'''
        return typing.cast("_ApplicationReference_eb7f83ac", jsii.get(self, "applicationRef"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationArn")
    def attr_application_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Application.

        :cloudformationAttribute: ApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier for the Application.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="applicationSourceConfig")
    def application_source_config(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationSourceConfigProperty"]:
        '''The configuration for where the application should be loaded from.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationSourceConfigProperty"], jsii.get(self, "applicationSourceConfig"))

    @application_source_config.setter
    def application_source_config(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationSourceConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e6a672bbf82d8b3bb39f56510a2db6c1a10b1776e0b968cd61c6665d29508e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationSourceConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''The description of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87943d6227ebd97ed6b280da7778e22bd3c7bef93cf9ab4a400fe6c9240847b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__416a93fef610e4b348e491404913fee978fabfb7d56f70287417ddc540c85c77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        '''The namespace of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1133ff0df5163630ae65aa9c2ffa87e2e0db4c7e7d6a197c3a256bd17cc3a45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="applicationConfig")
    def application_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationConfigProperty"]], jsii.get(self, "applicationConfig"))

    @application_config.setter
    def application_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3caf601b0f569fd019f866e47cc5b0bb49379d4b882f320078ed605052b7ca7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="iframeConfig")
    def iframe_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IframeConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IframeConfigProperty"]], jsii.get(self, "iframeConfig"))

    @iframe_config.setter
    def iframe_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IframeConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__132e84c3b7d79e8adb5125bdb2456de645edaaaecf7c9ace8f172b799e55c46d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iframeConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="initializationTimeout")
    def initialization_timeout(self) -> typing.Optional[jsii.Number]:
        '''The initialization timeout in milliseconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initializationTimeout"))

    @initialization_timeout.setter
    def initialization_timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3537c46fc02c6c8123f54755ecdc6281ac08636fb1bb28aa4bd15f35b256420b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initializationTimeout", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="isService")
    def is_service(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether the application is a service.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "isService"))

    @is_service.setter
    def is_service(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__024ff94ee9a9dbd7a4348422377053fce4ef5b4393f67aa6561ab4f37e813332)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isService", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The configuration of events or requests that the application has access to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissions"))

    @permissions.setter
    def permissions(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aafc4daa721930073f0dbbb7da26dc3c3c3be9c01fc9424bbc85944b766472d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags used to organize, track, or control access for this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf726959aa4191428101440b70a3eb393290a7cdec2b995b07413ac05f6d0c28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnApplication.ApplicationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"contact_handling": "contactHandling"},
    )
    class ApplicationConfigProperty:
        def __init__(
            self,
            *,
            contact_handling: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.ContactHandlingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param contact_handling: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-applicationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                application_config_property = appintegrations.CfnApplication.ApplicationConfigProperty(
                    contact_handling=appintegrations.CfnApplication.ContactHandlingProperty(
                        scope="scope"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a200fd881a848470f5631cfc744a53d5588ec7b4c6cf9b16ad4a194b4b85b1d)
                check_type(argname="argument contact_handling", value=contact_handling, expected_type=type_hints["contact_handling"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if contact_handling is not None:
                self._values["contact_handling"] = contact_handling

        @builtins.property
        def contact_handling(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.ContactHandlingProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-applicationconfig.html#cfn-appintegrations-application-applicationconfig-contacthandling
            '''
            result = self._values.get("contact_handling")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.ContactHandlingProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnApplication.ApplicationSourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"external_url_config": "externalUrlConfig"},
    )
    class ApplicationSourceConfigProperty:
        def __init__(
            self,
            *,
            external_url_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.ExternalUrlConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The configuration for where the application should be loaded from.

            :param external_url_config: The external URL source for the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-applicationsourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                application_source_config_property = appintegrations.CfnApplication.ApplicationSourceConfigProperty(
                    external_url_config=appintegrations.CfnApplication.ExternalUrlConfigProperty(
                        access_url="accessUrl",
                
                        # the properties below are optional
                        approved_origins=["approvedOrigins"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__599151bfc17f24879de38cf44b4a12c218d6b40ffaf8a24fc33beaa3691268b7)
                check_type(argname="argument external_url_config", value=external_url_config, expected_type=type_hints["external_url_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "external_url_config": external_url_config,
            }

        @builtins.property
        def external_url_config(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnApplication.ExternalUrlConfigProperty"]:
            '''The external URL source for the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-applicationsourceconfig.html#cfn-appintegrations-application-applicationsourceconfig-externalurlconfig
            '''
            result = self._values.get("external_url_config")
            assert result is not None, "Required property 'external_url_config' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnApplication.ExternalUrlConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationSourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnApplication.ContactHandlingProperty",
        jsii_struct_bases=[],
        name_mapping={"scope": "scope"},
    )
    class ContactHandlingProperty:
        def __init__(self, *, scope: builtins.str) -> None:
            '''
            :param scope: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-contacthandling.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                contact_handling_property = appintegrations.CfnApplication.ContactHandlingProperty(
                    scope="scope"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b220c6975b2fa737bd89eee1ab6f116e5ebe4d905d6233b53e35f5b0b40f162e)
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "scope": scope,
            }

        @builtins.property
        def scope(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-contacthandling.html#cfn-appintegrations-application-contacthandling-scope
            '''
            result = self._values.get("scope")
            assert result is not None, "Required property 'scope' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContactHandlingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnApplication.ExternalUrlConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_url": "accessUrl",
            "approved_origins": "approvedOrigins",
        },
    )
    class ExternalUrlConfigProperty:
        def __init__(
            self,
            *,
            access_url: builtins.str,
            approved_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The external URL source for the application.

            :param access_url: The URL to access the application.
            :param approved_origins: Additional URLs to allow list if different than the access URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-externalurlconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                external_url_config_property = appintegrations.CfnApplication.ExternalUrlConfigProperty(
                    access_url="accessUrl",
                
                    # the properties below are optional
                    approved_origins=["approvedOrigins"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__685c9ea63d4a7f3b4f8c0ba5680f0ec9ac1f12cdeb524e0b6a869beee33009cc)
                check_type(argname="argument access_url", value=access_url, expected_type=type_hints["access_url"])
                check_type(argname="argument approved_origins", value=approved_origins, expected_type=type_hints["approved_origins"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "access_url": access_url,
            }
            if approved_origins is not None:
                self._values["approved_origins"] = approved_origins

        @builtins.property
        def access_url(self) -> builtins.str:
            '''The URL to access the application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-externalurlconfig.html#cfn-appintegrations-application-externalurlconfig-accessurl
            '''
            result = self._values.get("access_url")
            assert result is not None, "Required property 'access_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def approved_origins(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Additional URLs to allow list if different than the access URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-externalurlconfig.html#cfn-appintegrations-application-externalurlconfig-approvedorigins
            '''
            result = self._values.get("approved_origins")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExternalUrlConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnApplication.IframeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"allow": "allow", "sandbox": "sandbox"},
    )
    class IframeConfigProperty:
        def __init__(
            self,
            *,
            allow: typing.Optional[typing.Sequence[builtins.str]] = None,
            sandbox: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param allow: 
            :param sandbox: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-iframeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                iframe_config_property = appintegrations.CfnApplication.IframeConfigProperty(
                    allow=["allow"],
                    sandbox=["sandbox"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4e1d29a683508d5dce338ead2d5d12168d88348304cab46c45234c9c8e6d558)
                check_type(argname="argument allow", value=allow, expected_type=type_hints["allow"])
                check_type(argname="argument sandbox", value=sandbox, expected_type=type_hints["sandbox"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow is not None:
                self._values["allow"] = allow
            if sandbox is not None:
                self._values["sandbox"] = sandbox

        @builtins.property
        def allow(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-iframeconfig.html#cfn-appintegrations-application-iframeconfig-allow
            '''
            result = self._values.get("allow")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def sandbox(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-application-iframeconfig.html#cfn-appintegrations-application-iframeconfig-sandbox
            '''
            result = self._values.get("sandbox")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IframeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_source_config": "applicationSourceConfig",
        "description": "description",
        "name": "name",
        "namespace": "namespace",
        "application_config": "applicationConfig",
        "iframe_config": "iframeConfig",
        "initialization_timeout": "initializationTimeout",
        "is_service": "isService",
        "permissions": "permissions",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        application_source_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.ApplicationSourceConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        description: builtins.str,
        name: builtins.str,
        namespace: builtins.str,
        application_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.ApplicationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        iframe_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnApplication.IframeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        initialization_timeout: typing.Optional[jsii.Number] = None,
        is_service: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param application_source_config: The configuration for where the application should be loaded from.
        :param description: The description of the application.
        :param name: The name of the application.
        :param namespace: The namespace of the application.
        :param application_config: 
        :param iframe_config: 
        :param initialization_timeout: The initialization timeout in milliseconds. Required when IsService is true.
        :param is_service: Indicates whether the application is a service. Default: - false
        :param permissions: The configuration of events or requests that the application has access to.
        :param tags: The tags used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appintegrations as appintegrations
            
            cfn_application_props = appintegrations.CfnApplicationProps(
                application_source_config=appintegrations.CfnApplication.ApplicationSourceConfigProperty(
                    external_url_config=appintegrations.CfnApplication.ExternalUrlConfigProperty(
                        access_url="accessUrl",
            
                        # the properties below are optional
                        approved_origins=["approvedOrigins"]
                    )
                ),
                description="description",
                name="name",
                namespace="namespace",
            
                # the properties below are optional
                application_config=appintegrations.CfnApplication.ApplicationConfigProperty(
                    contact_handling=appintegrations.CfnApplication.ContactHandlingProperty(
                        scope="scope"
                    )
                ),
                iframe_config=appintegrations.CfnApplication.IframeConfigProperty(
                    allow=["allow"],
                    sandbox=["sandbox"]
                ),
                initialization_timeout=123,
                is_service=False,
                permissions=["permissions"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d2c7ce5dfd3af1b41c02f961c30070527579ac243574e11a9dfe26cc453fe9f)
            check_type(argname="argument application_source_config", value=application_source_config, expected_type=type_hints["application_source_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument application_config", value=application_config, expected_type=type_hints["application_config"])
            check_type(argname="argument iframe_config", value=iframe_config, expected_type=type_hints["iframe_config"])
            check_type(argname="argument initialization_timeout", value=initialization_timeout, expected_type=type_hints["initialization_timeout"])
            check_type(argname="argument is_service", value=is_service, expected_type=type_hints["is_service"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_source_config": application_source_config,
            "description": description,
            "name": name,
            "namespace": namespace,
        }
        if application_config is not None:
            self._values["application_config"] = application_config
        if iframe_config is not None:
            self._values["iframe_config"] = iframe_config
        if initialization_timeout is not None:
            self._values["initialization_timeout"] = initialization_timeout
        if is_service is not None:
            self._values["is_service"] = is_service
        if permissions is not None:
            self._values["permissions"] = permissions
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_source_config(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationSourceConfigProperty"]:
        '''The configuration for where the application should be loaded from.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-applicationsourceconfig
        '''
        result = self._values.get("application_source_config")
        assert result is not None, "Required property 'application_source_config' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationSourceConfigProperty"], result)

    @builtins.property
    def description(self) -> builtins.str:
        '''The description of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The namespace of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-namespace
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationConfigProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-applicationconfig
        '''
        result = self._values.get("application_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.ApplicationConfigProperty"]], result)

    @builtins.property
    def iframe_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IframeConfigProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-iframeconfig
        '''
        result = self._values.get("iframe_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnApplication.IframeConfigProperty"]], result)

    @builtins.property
    def initialization_timeout(self) -> typing.Optional[jsii.Number]:
        '''The initialization timeout in milliseconds.

        Required when IsService is true.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-initializationtimeout
        '''
        result = self._values.get("initialization_timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def is_service(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether the application is a service.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-isservice
        '''
        result = self._values.get("is_service")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def permissions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The configuration of events or requests that the application has access to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-permissions
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags used to organize, track, or control access for this resource.

        For example, { "tags": {"key1":"value1", "key2":"value2"} }.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-application.html#cfn-appintegrations-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IDataIntegrationRef_c5e65586, _ITaggable_36806126)
class CfnDataIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnDataIntegration",
):
    '''Creates and persists a DataIntegration resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html
    :cloudformationResource: AWS::AppIntegrations::DataIntegration
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appintegrations as appintegrations
        
        # filters: Any
        # object_configuration: Any
        
        cfn_data_integration = appintegrations.CfnDataIntegration(self, "MyCfnDataIntegration",
            kms_key="kmsKey",
            name="name",
            source_uri="sourceUri",
        
            # the properties below are optional
            description="description",
            file_configuration=appintegrations.CfnDataIntegration.FileConfigurationProperty(
                folders=["folders"],
        
                # the properties below are optional
                filters=filters
            ),
            object_configuration=object_configuration,
            schedule_config=appintegrations.CfnDataIntegration.ScheduleConfigProperty(
                schedule_expression="scheduleExpression",
        
                # the properties below are optional
                first_execution_from="firstExecutionFrom",
                object="object"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        kms_key: builtins.str,
        name: builtins.str,
        source_uri: builtins.str,
        description: typing.Optional[builtins.str] = None,
        file_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnDataIntegration.FileConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_configuration: typing.Any = None,
        schedule_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnDataIntegration.ScheduleConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AppIntegrations::DataIntegration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param kms_key: The KMS key for the DataIntegration.
        :param name: The name of the DataIntegration.
        :param source_uri: The URI of the data source.
        :param description: A description of the DataIntegration.
        :param file_configuration: The configuration for what files should be pulled from the source.
        :param object_configuration: The configuration for what data should be pulled from the source.
        :param schedule_config: The name of the data and how often it should be pulled from the source.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07830c24dc09b0662b03583ee4edbdbaeb4fabf95d85c4f4ed965ea9d0999f40)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataIntegrationProps(
            kms_key=kms_key,
            name=name,
            source_uri=source_uri,
            description=description,
            file_configuration=file_configuration,
            object_configuration=object_configuration,
            schedule_config=schedule_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDataIntegration")
    @builtins.classmethod
    def arn_for_data_integration(
        cls,
        resource: "_IDataIntegrationRef_c5e65586",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb0b9759bd2023f505f2c40dfbb3c1e7f83592a8fd9f1b8910eeb66076b8cde4)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDataIntegration", [resource]))

    @jsii.member(jsii_name="fromDataIntegrationArn")
    @builtins.classmethod
    def from_data_integration_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IDataIntegrationRef_c5e65586":
        '''Creates a new IDataIntegrationRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70d05e99699021c14d7f2458d9284b6643ee07c8bf98a6d7251ec619c575c220)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IDataIntegrationRef_c5e65586", jsii.sinvoke(cls, "fromDataIntegrationArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromDataIntegrationId")
    @builtins.classmethod
    def from_data_integration_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        data_integration_id: builtins.str,
    ) -> "_IDataIntegrationRef_c5e65586":
        '''Creates a new IDataIntegrationRef from a dataIntegrationId.

        :param scope: -
        :param id: -
        :param data_integration_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20305a315b3389b912aa7c2944c682e8c102efa0a52d1ebccfdcf5ad58d22c5b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument data_integration_id", value=data_integration_id, expected_type=type_hints["data_integration_id"])
        return typing.cast("_IDataIntegrationRef_c5e65586", jsii.sinvoke(cls, "fromDataIntegrationId", [scope, id, data_integration_id]))

    @jsii.member(jsii_name="isCfnDataIntegration")
    @builtins.classmethod
    def is_cfn_data_integration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDataIntegration.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b3be01c82f3ba80a719edb986c644415a8703b0921b82351ff4f69610ad6826)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDataIntegration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b6af7441719b460ee4641270770c612fb58e431a8fbcc3d0f99ddae2d585fb7)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c538be594c10bcec9c53489ef9157700761163aaf6bc0272307d9a7f7d936952)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDataIntegrationArn")
    def attr_data_integration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the DataIntegration.

        :cloudformationAttribute: DataIntegrationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataIntegrationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="dataIntegrationRef")
    def data_integration_ref(self) -> "_DataIntegrationReference_82094d23":
        '''A reference to a DataIntegration resource.'''
        return typing.cast("_DataIntegrationReference_82094d23", jsii.get(self, "dataIntegrationRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        '''The KMS key for the DataIntegration.'''
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a3cad25e2a72d7ef20681bd49e23420f83d37ece3e2e6187f06b562941a0afc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the DataIntegration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e51110622d3f4ff27df719656fd99fc526be5468469b3eea1ec762212e0d0d83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceUri")
    def source_uri(self) -> builtins.str:
        '''The URI of the data source.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceUri"))

    @source_uri.setter
    def source_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c40d38376f274efd003c192558a948691aa19100c92ffcb8b59fa6c6f3ab8dcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the DataIntegration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac6cbca81b19a3d28448d5b03b3556d234f451a65367c5aece805bf98e731c52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileConfiguration")
    def file_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.FileConfigurationProperty"]]:
        '''The configuration for what files should be pulled from the source.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.FileConfigurationProperty"]], jsii.get(self, "fileConfiguration"))

    @file_configuration.setter
    def file_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.FileConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa142812d7a4300d1fdf79595aa40d4ec698ff46a0af150d168d97ee958e67e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="objectConfiguration")
    def object_configuration(self) -> typing.Any:
        '''The configuration for what data should be pulled from the source.'''
        return typing.cast(typing.Any, jsii.get(self, "objectConfiguration"))

    @object_configuration.setter
    def object_configuration(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c4d150a6b38a21718340d0e7596e6fe23c488efff8579d0b26f44d2d887f87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "objectConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="scheduleConfig")
    def schedule_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.ScheduleConfigProperty"]]:
        '''The name of the data and how often it should be pulled from the source.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.ScheduleConfigProperty"]], jsii.get(self, "scheduleConfig"))

    @schedule_config.setter
    def schedule_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.ScheduleConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5245bc847871e6f3d723769c28404578dc706f908a62836394d9ef2b6acc8a92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scheduleConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d778105dbb9cf7d3e71800bafeafc79e0c6102ba3bccf8a3f96fd8b2c9aac3b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnDataIntegration.FileConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"folders": "folders", "filters": "filters"},
    )
    class FileConfigurationProperty:
        def __init__(
            self,
            *,
            folders: typing.Sequence[builtins.str],
            filters: typing.Any = None,
        ) -> None:
            '''The configuration for what files should be pulled from the source.

            :param folders: Identifiers for the source folders to pull all files from recursively.
            :param filters: Restrictions for what files should be pulled from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                # filters: Any
                
                file_configuration_property = appintegrations.CfnDataIntegration.FileConfigurationProperty(
                    folders=["folders"],
                
                    # the properties below are optional
                    filters=filters
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e7240d0935d712dd0763236cffe39f34c0eb20f0e4285482cf5e89018d193000)
                check_type(argname="argument folders", value=folders, expected_type=type_hints["folders"])
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "folders": folders,
            }
            if filters is not None:
                self._values["filters"] = filters

        @builtins.property
        def folders(self) -> typing.List[builtins.str]:
            '''Identifiers for the source folders to pull all files from recursively.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html#cfn-appintegrations-dataintegration-fileconfiguration-folders
            '''
            result = self._values.get("folders")
            assert result is not None, "Required property 'folders' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def filters(self) -> typing.Any:
            '''Restrictions for what files should be pulled from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-fileconfiguration.html#cfn-appintegrations-dataintegration-fileconfiguration-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnDataIntegration.ScheduleConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule_expression": "scheduleExpression",
            "first_execution_from": "firstExecutionFrom",
            "object": "object",
        },
    )
    class ScheduleConfigProperty:
        def __init__(
            self,
            *,
            schedule_expression: builtins.str,
            first_execution_from: typing.Optional[builtins.str] = None,
            object: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The name of the data and how often it should be pulled from the source.

            :param schedule_expression: How often the data should be pulled from data source.
            :param first_execution_from: The start date for objects to import in the first flow run as an Unix/epoch timestamp in milliseconds or in ISO-8601 format.
            :param object: The name of the object to pull from the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                schedule_config_property = appintegrations.CfnDataIntegration.ScheduleConfigProperty(
                    schedule_expression="scheduleExpression",
                
                    # the properties below are optional
                    first_execution_from="firstExecutionFrom",
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1fa0efcac2eeb739bb68a54b8c7816a32a28a265c96601fb14102a1f9a7db338)
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
                check_type(argname="argument first_execution_from", value=first_execution_from, expected_type=type_hints["first_execution_from"])
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }
            if first_execution_from is not None:
                self._values["first_execution_from"] = first_execution_from
            if object is not None:
                self._values["object"] = object

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''How often the data should be pulled from data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html#cfn-appintegrations-dataintegration-scheduleconfig-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def first_execution_from(self) -> typing.Optional[builtins.str]:
            '''The start date for objects to import in the first flow run as an Unix/epoch timestamp in milliseconds or in ISO-8601 format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html#cfn-appintegrations-dataintegration-scheduleconfig-firstexecutionfrom
            '''
            result = self._values.get("first_execution_from")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object(self) -> typing.Optional[builtins.str]:
            '''The name of the object to pull from the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-dataintegration-scheduleconfig.html#cfn-appintegrations-dataintegration-scheduleconfig-object
            '''
            result = self._values.get("object")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnDataIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "kms_key": "kmsKey",
        "name": "name",
        "source_uri": "sourceUri",
        "description": "description",
        "file_configuration": "fileConfiguration",
        "object_configuration": "objectConfiguration",
        "schedule_config": "scheduleConfig",
        "tags": "tags",
    },
)
class CfnDataIntegrationProps:
    def __init__(
        self,
        *,
        kms_key: builtins.str,
        name: builtins.str,
        source_uri: builtins.str,
        description: typing.Optional[builtins.str] = None,
        file_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnDataIntegration.FileConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        object_configuration: typing.Any = None,
        schedule_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnDataIntegration.ScheduleConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataIntegration``.

        :param kms_key: The KMS key for the DataIntegration.
        :param name: The name of the DataIntegration.
        :param source_uri: The URI of the data source.
        :param description: A description of the DataIntegration.
        :param file_configuration: The configuration for what files should be pulled from the source.
        :param object_configuration: The configuration for what data should be pulled from the source.
        :param schedule_config: The name of the data and how often it should be pulled from the source.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appintegrations as appintegrations
            
            # filters: Any
            # object_configuration: Any
            
            cfn_data_integration_props = appintegrations.CfnDataIntegrationProps(
                kms_key="kmsKey",
                name="name",
                source_uri="sourceUri",
            
                # the properties below are optional
                description="description",
                file_configuration=appintegrations.CfnDataIntegration.FileConfigurationProperty(
                    folders=["folders"],
            
                    # the properties below are optional
                    filters=filters
                ),
                object_configuration=object_configuration,
                schedule_config=appintegrations.CfnDataIntegration.ScheduleConfigProperty(
                    schedule_expression="scheduleExpression",
            
                    # the properties below are optional
                    first_execution_from="firstExecutionFrom",
                    object="object"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e7b2c594c26fb87f1ee6d6a6b7787330233c7a73e8ce2cfe23ce1b18ffe290)
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source_uri", value=source_uri, expected_type=type_hints["source_uri"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument file_configuration", value=file_configuration, expected_type=type_hints["file_configuration"])
            check_type(argname="argument object_configuration", value=object_configuration, expected_type=type_hints["object_configuration"])
            check_type(argname="argument schedule_config", value=schedule_config, expected_type=type_hints["schedule_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kms_key": kms_key,
            "name": name,
            "source_uri": source_uri,
        }
        if description is not None:
            self._values["description"] = description
        if file_configuration is not None:
            self._values["file_configuration"] = file_configuration
        if object_configuration is not None:
            self._values["object_configuration"] = object_configuration
        if schedule_config is not None:
            self._values["schedule_config"] = schedule_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def kms_key(self) -> builtins.str:
        '''The KMS key for the DataIntegration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-kmskey
        '''
        result = self._values.get("kms_key")
        assert result is not None, "Required property 'kms_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the DataIntegration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_uri(self) -> builtins.str:
        '''The URI of the data source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-sourceuri
        '''
        result = self._values.get("source_uri")
        assert result is not None, "Required property 'source_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the DataIntegration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.FileConfigurationProperty"]]:
        '''The configuration for what files should be pulled from the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-fileconfiguration
        '''
        result = self._values.get("file_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.FileConfigurationProperty"]], result)

    @builtins.property
    def object_configuration(self) -> typing.Any:
        '''The configuration for what data should be pulled from the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-objectconfiguration
        '''
        result = self._values.get("object_configuration")
        return typing.cast(typing.Any, result)

    @builtins.property
    def schedule_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.ScheduleConfigProperty"]]:
        '''The name of the data and how often it should be pulled from the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-scheduleconfig
        '''
        result = self._values.get("schedule_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnDataIntegration.ScheduleConfigProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-dataintegration.html#cfn-appintegrations-dataintegration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IEventIntegrationRef_d2c58e8f, _ITaggable_36806126)
class CfnEventIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnEventIntegration",
):
    '''Creates an event integration.

    You provide a name, description, and a reference to an Amazon EventBridge bus in your account and a partner event source that will push events to that bus. No objects are created in your account, only metadata that is persisted on the EventIntegration control plane.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html
    :cloudformationResource: AWS::AppIntegrations::EventIntegration
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appintegrations as appintegrations
        
        cfn_event_integration = appintegrations.CfnEventIntegration(self, "MyCfnEventIntegration",
            event_bridge_bus="eventBridgeBus",
            event_filter=appintegrations.CfnEventIntegration.EventFilterProperty(
                source="source"
            ),
            name="name",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        event_bridge_bus: builtins.str,
        event_filter: typing.Union["_IResolvable_da3f097b", typing.Union["CfnEventIntegration.EventFilterProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::AppIntegrations::EventIntegration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param event_bridge_bus: The Amazon EventBridge bus for the event integration.
        :param event_filter: The event integration filter.
        :param name: The name of the event integration.
        :param description: The event integration description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4a16fc332806342706d2878c9a173a25d599659c9ec58d0c31e1ae7a621e4f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventIntegrationProps(
            event_bridge_bus=event_bridge_bus,
            event_filter=event_filter,
            name=name,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForEventIntegration")
    @builtins.classmethod
    def arn_for_event_integration(
        cls,
        resource: "_IEventIntegrationRef_d2c58e8f",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a57514c5cab014194710e855520d84000c60bde7bdbcf3b9586223f3cb9d5ae1)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForEventIntegration", [resource]))

    @jsii.member(jsii_name="fromEventIntegrationArn")
    @builtins.classmethod
    def from_event_integration_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IEventIntegrationRef_d2c58e8f":
        '''Creates a new IEventIntegrationRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4585a8d0fffc3e813b27fd6176836fb851e8dc99a7f5986e1ac81b808e31071)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IEventIntegrationRef_d2c58e8f", jsii.sinvoke(cls, "fromEventIntegrationArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromEventIntegrationName")
    @builtins.classmethod
    def from_event_integration_name(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        event_integration_name: builtins.str,
    ) -> "_IEventIntegrationRef_d2c58e8f":
        '''Creates a new IEventIntegrationRef from a eventIntegrationName.

        :param scope: -
        :param id: -
        :param event_integration_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fc7a2e0941d7492b5dc210f140a9f33a60d60a6ccc985e636799c9a535d22b8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument event_integration_name", value=event_integration_name, expected_type=type_hints["event_integration_name"])
        return typing.cast("_IEventIntegrationRef_d2c58e8f", jsii.sinvoke(cls, "fromEventIntegrationName", [scope, id, event_integration_name]))

    @jsii.member(jsii_name="isCfnEventIntegration")
    @builtins.classmethod
    def is_cfn_event_integration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnEventIntegration.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8157effeb247ca9e399730fb309192297da614d0a45b1ebc8ca9a78c58b7f93)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnEventIntegration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b155f65b8c626e094fd78079276b84b0fcfa577110b2ffa5fd975593086533)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2dd2ffc1f659143f7a6cb15c06dae8c737a11c4d5a56af0a3337f921ebd81e1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEventIntegrationArn")
    def attr_event_integration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the event integration.

        :cloudformationAttribute: EventIntegrationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEventIntegrationArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="eventIntegrationRef")
    def event_integration_ref(self) -> "_EventIntegrationReference_2d3a8ab8":
        '''A reference to a EventIntegration resource.'''
        return typing.cast("_EventIntegrationReference_2d3a8ab8", jsii.get(self, "eventIntegrationRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="eventBridgeBus")
    def event_bridge_bus(self) -> builtins.str:
        '''The Amazon EventBridge bus for the event integration.'''
        return typing.cast(builtins.str, jsii.get(self, "eventBridgeBus"))

    @event_bridge_bus.setter
    def event_bridge_bus(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__454b16c02d23ad7183df72a0517049ca680971186fd144d912c66c66f41479b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventBridgeBus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventFilter")
    def event_filter(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnEventIntegration.EventFilterProperty"]:
        '''The event integration filter.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnEventIntegration.EventFilterProperty"], jsii.get(self, "eventFilter"))

    @event_filter.setter
    def event_filter(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnEventIntegration.EventFilterProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26c1d519a62cc46ab080cc71141eaf4a08280d9dfa5cc2110dd627f095a67241)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventFilter", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the event integration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e44ab4713818a147dca8ac5a9022090f6d871398c1671b532e61470fc234e20f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The event integration description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16fd4e12e97916052e3996eda8c3774583ca79f8ceda9b5fca42d81c38c9ad1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1545291bb728d092049a68fe1f3f167513ab081a64c955a81627589c9ef4bfa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appintegrations.CfnEventIntegration.EventFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"source": "source"},
    )
    class EventFilterProperty:
        def __init__(self, *, source: builtins.str) -> None:
            '''The event integration filter.

            :param source: The source of the events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appintegrations as appintegrations
                
                event_filter_property = appintegrations.CfnEventIntegration.EventFilterProperty(
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe2caaefe76d9510e6ff29f9afdf7706ad87988fce20dbb68ad8862bcbb22154)
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source": source,
            }

        @builtins.property
        def source(self) -> builtins.str:
            '''The source of the events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appintegrations-eventintegration-eventfilter.html#cfn-appintegrations-eventintegration-eventfilter-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appintegrations.CfnEventIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_bridge_bus": "eventBridgeBus",
        "event_filter": "eventFilter",
        "name": "name",
        "description": "description",
        "tags": "tags",
    },
)
class CfnEventIntegrationProps:
    def __init__(
        self,
        *,
        event_bridge_bus: builtins.str,
        event_filter: typing.Union["_IResolvable_da3f097b", typing.Union["CfnEventIntegration.EventFilterProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventIntegration``.

        :param event_bridge_bus: The Amazon EventBridge bus for the event integration.
        :param event_filter: The event integration filter.
        :param name: The name of the event integration.
        :param description: The event integration description.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appintegrations as appintegrations
            
            cfn_event_integration_props = appintegrations.CfnEventIntegrationProps(
                event_bridge_bus="eventBridgeBus",
                event_filter=appintegrations.CfnEventIntegration.EventFilterProperty(
                    source="source"
                ),
                name="name",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9153bde28b2e9d1843c748f4d513f8ac68ef7ba9754ea2cdad14193f14742d6)
            check_type(argname="argument event_bridge_bus", value=event_bridge_bus, expected_type=type_hints["event_bridge_bus"])
            check_type(argname="argument event_filter", value=event_filter, expected_type=type_hints["event_filter"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bridge_bus": event_bridge_bus,
            "event_filter": event_filter,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def event_bridge_bus(self) -> builtins.str:
        '''The Amazon EventBridge bus for the event integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventbridgebus
        '''
        result = self._values.get("event_bridge_bus")
        assert result is not None, "Required property 'event_bridge_bus' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_filter(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnEventIntegration.EventFilterProperty"]:
        '''The event integration filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-eventfilter
        '''
        result = self._values.get("event_filter")
        assert result is not None, "Required property 'event_filter' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnEventIntegration.EventFilterProperty"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the event integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The event integration description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appintegrations-eventintegration.html#cfn-appintegrations-eventintegration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnDataIntegration",
    "CfnDataIntegrationProps",
    "CfnEventIntegration",
    "CfnEventIntegrationProps",
]

publication.publish()

def _typecheckingstub__2c1bbb1e03e672595eb80bdb7dcb70bb6e71fccf39633133ee8a5b86b6874772(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_source_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationSourceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    description: builtins.str,
    name: builtins.str,
    namespace: builtins.str,
    application_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iframe_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.IframeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    initialization_timeout: typing.Optional[jsii.Number] = None,
    is_service: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b42f16ecbbfeacf4cebf72ced2a17f07f5a84908315be11f343c633d7813dc0(
    resource: _IApplicationRef_f88446ed,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4e08f6d9252ec685994e80dfaccf256affaf78836001fbb59695c3e4fec6c4(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2397143274609e6f7787d10c8effb0139785b91de02a335ac411b9f6e4478fb6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f2b0f5530bab214011baa3953ec2f0059bf19c5005c20b1a37a58186c8d1c94(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e6a672bbf82d8b3bb39f56510a2db6c1a10b1776e0b968cd61c6665d29508e7(
    value: typing.Union[_IResolvable_da3f097b, CfnApplication.ApplicationSourceConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87943d6227ebd97ed6b280da7778e22bd3c7bef93cf9ab4a400fe6c9240847b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__416a93fef610e4b348e491404913fee978fabfb7d56f70287417ddc540c85c77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1133ff0df5163630ae65aa9c2ffa87e2e0db4c7e7d6a197c3a256bd17cc3a45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3caf601b0f569fd019f866e47cc5b0bb49379d4b882f320078ed605052b7ca7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ApplicationConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__132e84c3b7d79e8adb5125bdb2456de645edaaaecf7c9ace8f172b799e55c46d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.IframeConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3537c46fc02c6c8123f54755ecdc6281ac08636fb1bb28aa4bd15f35b256420b(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__024ff94ee9a9dbd7a4348422377053fce4ef5b4393f67aa6561ab4f37e813332(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aafc4daa721930073f0dbbb7da26dc3c3c3be9c01fc9424bbc85944b766472d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf726959aa4191428101440b70a3eb393290a7cdec2b995b07413ac05f6d0c28(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a200fd881a848470f5631cfc744a53d5588ec7b4c6cf9b16ad4a194b4b85b1d(
    *,
    contact_handling: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ContactHandlingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__599151bfc17f24879de38cf44b4a12c218d6b40ffaf8a24fc33beaa3691268b7(
    *,
    external_url_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ExternalUrlConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b220c6975b2fa737bd89eee1ab6f116e5ebe4d905d6233b53e35f5b0b40f162e(
    *,
    scope: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__685c9ea63d4a7f3b4f8c0ba5680f0ec9ac1f12cdeb524e0b6a869beee33009cc(
    *,
    access_url: builtins.str,
    approved_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e1d29a683508d5dce338ead2d5d12168d88348304cab46c45234c9c8e6d558(
    *,
    allow: typing.Optional[typing.Sequence[builtins.str]] = None,
    sandbox: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d2c7ce5dfd3af1b41c02f961c30070527579ac243574e11a9dfe26cc453fe9f(
    *,
    application_source_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationSourceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    description: builtins.str,
    name: builtins.str,
    namespace: builtins.str,
    application_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    iframe_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.IframeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    initialization_timeout: typing.Optional[jsii.Number] = None,
    is_service: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    permissions: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07830c24dc09b0662b03583ee4edbdbaeb4fabf95d85c4f4ed965ea9d0999f40(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    kms_key: builtins.str,
    name: builtins.str,
    source_uri: builtins.str,
    description: typing.Optional[builtins.str] = None,
    file_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.FileConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_configuration: typing.Any = None,
    schedule_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.ScheduleConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb0b9759bd2023f505f2c40dfbb3c1e7f83592a8fd9f1b8910eeb66076b8cde4(
    resource: _IDataIntegrationRef_c5e65586,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d05e99699021c14d7f2458d9284b6643ee07c8bf98a6d7251ec619c575c220(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20305a315b3389b912aa7c2944c682e8c102efa0a52d1ebccfdcf5ad58d22c5b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    data_integration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b3be01c82f3ba80a719edb986c644415a8703b0921b82351ff4f69610ad6826(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b6af7441719b460ee4641270770c612fb58e431a8fbcc3d0f99ddae2d585fb7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c538be594c10bcec9c53489ef9157700761163aaf6bc0272307d9a7f7d936952(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a3cad25e2a72d7ef20681bd49e23420f83d37ece3e2e6187f06b562941a0afc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51110622d3f4ff27df719656fd99fc526be5468469b3eea1ec762212e0d0d83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c40d38376f274efd003c192558a948691aa19100c92ffcb8b59fa6c6f3ab8dcc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6cbca81b19a3d28448d5b03b3556d234f451a65367c5aece805bf98e731c52(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa142812d7a4300d1fdf79595aa40d4ec698ff46a0af150d168d97ee958e67e1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataIntegration.FileConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c4d150a6b38a21718340d0e7596e6fe23c488efff8579d0b26f44d2d887f87(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5245bc847871e6f3d723769c28404578dc706f908a62836394d9ef2b6acc8a92(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataIntegration.ScheduleConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d778105dbb9cf7d3e71800bafeafc79e0c6102ba3bccf8a3f96fd8b2c9aac3b2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7240d0935d712dd0763236cffe39f34c0eb20f0e4285482cf5e89018d193000(
    *,
    folders: typing.Sequence[builtins.str],
    filters: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa0efcac2eeb739bb68a54b8c7816a32a28a265c96601fb14102a1f9a7db338(
    *,
    schedule_expression: builtins.str,
    first_execution_from: typing.Optional[builtins.str] = None,
    object: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e7b2c594c26fb87f1ee6d6a6b7787330233c7a73e8ce2cfe23ce1b18ffe290(
    *,
    kms_key: builtins.str,
    name: builtins.str,
    source_uri: builtins.str,
    description: typing.Optional[builtins.str] = None,
    file_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.FileConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    object_configuration: typing.Any = None,
    schedule_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataIntegration.ScheduleConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4a16fc332806342706d2878c9a173a25d599659c9ec58d0c31e1ae7a621e4f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    event_bridge_bus: builtins.str,
    event_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventIntegration.EventFilterProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a57514c5cab014194710e855520d84000c60bde7bdbcf3b9586223f3cb9d5ae1(
    resource: _IEventIntegrationRef_d2c58e8f,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4585a8d0fffc3e813b27fd6176836fb851e8dc99a7f5986e1ac81b808e31071(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fc7a2e0941d7492b5dc210f140a9f33a60d60a6ccc985e636799c9a535d22b8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    event_integration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8157effeb247ca9e399730fb309192297da614d0a45b1ebc8ca9a78c58b7f93(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b155f65b8c626e094fd78079276b84b0fcfa577110b2ffa5fd975593086533(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2dd2ffc1f659143f7a6cb15c06dae8c737a11c4d5a56af0a3337f921ebd81e1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__454b16c02d23ad7183df72a0517049ca680971186fd144d912c66c66f41479b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26c1d519a62cc46ab080cc71141eaf4a08280d9dfa5cc2110dd627f095a67241(
    value: typing.Union[_IResolvable_da3f097b, CfnEventIntegration.EventFilterProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e44ab4713818a147dca8ac5a9022090f6d871398c1671b532e61470fc234e20f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16fd4e12e97916052e3996eda8c3774583ca79f8ceda9b5fca42d81c38c9ad1d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1545291bb728d092049a68fe1f3f167513ab081a64c955a81627589c9ef4bfa1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe2caaefe76d9510e6ff29f9afdf7706ad87988fce20dbb68ad8862bcbb22154(
    *,
    source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9153bde28b2e9d1843c748f4d513f8ac68ef7ba9754ea2cdad14193f14742d6(
    *,
    event_bridge_bus: builtins.str,
    event_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEventIntegration.EventFilterProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
