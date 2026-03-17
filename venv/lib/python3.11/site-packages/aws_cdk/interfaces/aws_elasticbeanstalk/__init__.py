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
    jsii_type="aws-cdk-lib.interfaces.aws_elasticbeanstalk.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_name": "applicationName"},
)
class ApplicationReference:
    def __init__(self, *, application_name: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_name: The ApplicationName of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticbeanstalk as interfaces_elasticbeanstalk
            
            application_reference = interfaces_elasticbeanstalk.ApplicationReference(
                application_name="applicationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__361e92117390b891b5e48bec5672a740ea30d6530dcb0753e9a405d9350c1f3c)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The ApplicationName of the Application resource.'''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticbeanstalk.ApplicationVersionReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "application_version_id": "applicationVersionId",
    },
)
class ApplicationVersionReference:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        application_version_id: builtins.str,
    ) -> None:
        '''A reference to a ApplicationVersion resource.

        :param application_name: The ApplicationName of the ApplicationVersion resource.
        :param application_version_id: The Id of the ApplicationVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticbeanstalk as interfaces_elasticbeanstalk
            
            application_version_reference = interfaces_elasticbeanstalk.ApplicationVersionReference(
                application_name="applicationName",
                application_version_id="applicationVersionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59354b85b5ff150bc5217e71aedd3ca99338b6679bc96cf318da8c085359af41)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument application_version_id", value=application_version_id, expected_type=type_hints["application_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "application_version_id": application_version_id,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The ApplicationName of the ApplicationVersion resource.'''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_version_id(self) -> builtins.str:
        '''The Id of the ApplicationVersion resource.'''
        result = self._values.get("application_version_id")
        assert result is not None, "Required property 'application_version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticbeanstalk.ConfigurationTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "template_name": "templateName",
    },
)
class ConfigurationTemplateReference:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        template_name: builtins.str,
    ) -> None:
        '''A reference to a ConfigurationTemplate resource.

        :param application_name: The ApplicationName of the ConfigurationTemplate resource.
        :param template_name: The TemplateName of the ConfigurationTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticbeanstalk as interfaces_elasticbeanstalk
            
            configuration_template_reference = interfaces_elasticbeanstalk.ConfigurationTemplateReference(
                application_name="applicationName",
                template_name="templateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__668def1580a51981c6f182721c5b6f337af94f860fd1689a4d8172ae44f8ec78)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "template_name": template_name,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The ApplicationName of the ConfigurationTemplate resource.'''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_name(self) -> builtins.str:
        '''The TemplateName of the ConfigurationTemplate resource.'''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticbeanstalk.EnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={"environment_name": "environmentName"},
)
class EnvironmentReference:
    def __init__(self, *, environment_name: builtins.str) -> None:
        '''A reference to a Environment resource.

        :param environment_name: The EnvironmentName of the Environment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticbeanstalk as interfaces_elasticbeanstalk
            
            environment_reference = interfaces_elasticbeanstalk.EnvironmentReference(
                environment_name="environmentName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2da4e65e9b05270b2b716cebf27923127e88d79f3186599842ab6947f964a97)
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment_name": environment_name,
        }

    @builtins.property
    def environment_name(self) -> builtins.str:
        '''The EnvironmentName of the Environment resource.'''
        result = self._values.get("environment_name")
        assert result is not None, "Required property 'environment_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticbeanstalk.IApplicationRef"
)
class IApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        ...


class _IApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticbeanstalk.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticbeanstalk.IApplicationVersionRef"
)
class IApplicationVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationVersionRef")
    def application_version_ref(self) -> "ApplicationVersionReference":
        '''(experimental) A reference to a ApplicationVersion resource.

        :stability: experimental
        '''
        ...


class _IApplicationVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticbeanstalk.IApplicationVersionRef"

    @builtins.property
    @jsii.member(jsii_name="applicationVersionRef")
    def application_version_ref(self) -> "ApplicationVersionReference":
        '''(experimental) A reference to a ApplicationVersion resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationVersionReference", jsii.get(self, "applicationVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationVersionRef).__jsii_proxy_class__ = lambda : _IApplicationVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticbeanstalk.IConfigurationTemplateRef"
)
class IConfigurationTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationTemplateRef")
    def configuration_template_ref(self) -> "ConfigurationTemplateReference":
        '''(experimental) A reference to a ConfigurationTemplate resource.

        :stability: experimental
        '''
        ...


class _IConfigurationTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticbeanstalk.IConfigurationTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="configurationTemplateRef")
    def configuration_template_ref(self) -> "ConfigurationTemplateReference":
        '''(experimental) A reference to a ConfigurationTemplate resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationTemplateReference", jsii.get(self, "configurationTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationTemplateRef).__jsii_proxy_class__ = lambda : _IConfigurationTemplateRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticbeanstalk.IEnvironmentRef"
)
class IEnvironmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticbeanstalk.IEnvironmentRef"

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentReference", jsii.get(self, "environmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentRef).__jsii_proxy_class__ = lambda : _IEnvironmentRefProxy


__all__ = [
    "ApplicationReference",
    "ApplicationVersionReference",
    "ConfigurationTemplateReference",
    "EnvironmentReference",
    "IApplicationRef",
    "IApplicationVersionRef",
    "IConfigurationTemplateRef",
    "IEnvironmentRef",
]

publication.publish()

def _typecheckingstub__361e92117390b891b5e48bec5672a740ea30d6530dcb0753e9a405d9350c1f3c(
    *,
    application_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59354b85b5ff150bc5217e71aedd3ca99338b6679bc96cf318da8c085359af41(
    *,
    application_name: builtins.str,
    application_version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__668def1580a51981c6f182721c5b6f337af94f860fd1689a4d8172ae44f8ec78(
    *,
    application_name: builtins.str,
    template_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2da4e65e9b05270b2b716cebf27923127e88d79f3186599842ab6947f964a97(
    *,
    environment_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IApplicationVersionRef, IConfigurationTemplateRef, IEnvironmentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
