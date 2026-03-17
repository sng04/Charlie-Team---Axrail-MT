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
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_id": "applicationId"},
)
class ApplicationReference:
    def __init__(self, *, application_id: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_id: The ApplicationId of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appconfig as interfaces_appconfig
            
            application_reference = interfaces_appconfig.ApplicationReference(
                application_id="applicationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7897eb149d1f049c9474b1cc9cde497acc7eef83b557fd5e69865922db577813)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Application resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.ConfigurationProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration_profile_id": "configurationProfileId",
    },
)
class ConfigurationProfileReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
    ) -> None:
        '''A reference to a ConfigurationProfile resource.

        :param application_id: The ApplicationId of the ConfigurationProfile resource.
        :param configuration_profile_id: The ConfigurationProfileId of the ConfigurationProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appconfig as interfaces_appconfig
            
            configuration_profile_reference = interfaces_appconfig.ConfigurationProfileReference(
                application_id="applicationId",
                configuration_profile_id="configurationProfileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__196a649cb6c8bc25d8b70a62cca359e16bc48f7cbc911cefc2c922986a508932)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument configuration_profile_id", value=configuration_profile_id, expected_type=type_hints["configuration_profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the ConfigurationProfile resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_profile_id(self) -> builtins.str:
        '''The ConfigurationProfileId of the ConfigurationProfile resource.'''
        result = self._values.get("configuration_profile_id")
        assert result is not None, "Required property 'configuration_profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.DeploymentReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "deployment_number": "deploymentNumber",
        "environment_id": "environmentId",
    },
)
class DeploymentReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        deployment_number: builtins.str,
        environment_id: builtins.str,
    ) -> None:
        '''A reference to a Deployment resource.

        :param application_id: The ApplicationId of the Deployment resource.
        :param deployment_number: The DeploymentNumber of the Deployment resource.
        :param environment_id: The EnvironmentId of the Deployment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appconfig as interfaces_appconfig
            
            deployment_reference = interfaces_appconfig.DeploymentReference(
                application_id="applicationId",
                deployment_number="deploymentNumber",
                environment_id="environmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3e55ba941a1da007e8831ae6e5ecb2628164a77f73db6a0cb54cab47f747f15)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument deployment_number", value=deployment_number, expected_type=type_hints["deployment_number"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "deployment_number": deployment_number,
            "environment_id": environment_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Deployment resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_number(self) -> builtins.str:
        '''The DeploymentNumber of the Deployment resource.'''
        result = self._values.get("deployment_number")
        assert result is not None, "Required property 'deployment_number' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''The EnvironmentId of the Deployment resource.'''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.DeploymentStrategyReference",
    jsii_struct_bases=[],
    name_mapping={"deployment_strategy_id": "deploymentStrategyId"},
)
class DeploymentStrategyReference:
    def __init__(self, *, deployment_strategy_id: builtins.str) -> None:
        '''A reference to a DeploymentStrategy resource.

        :param deployment_strategy_id: The Id of the DeploymentStrategy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appconfig as interfaces_appconfig
            
            deployment_strategy_reference = interfaces_appconfig.DeploymentStrategyReference(
                deployment_strategy_id="deploymentStrategyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__026929d86c5cf003577354c6fd4824313f828abc9fa63f8c14581f710b6b7cbb)
            check_type(argname="argument deployment_strategy_id", value=deployment_strategy_id, expected_type=type_hints["deployment_strategy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_strategy_id": deployment_strategy_id,
        }

    @builtins.property
    def deployment_strategy_id(self) -> builtins.str:
        '''The Id of the DeploymentStrategy resource.'''
        result = self._values.get("deployment_strategy_id")
        assert result is not None, "Required property 'deployment_strategy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentStrategyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.EnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "environment_id": "environmentId",
    },
)
class EnvironmentReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        environment_id: builtins.str,
    ) -> None:
        '''A reference to a Environment resource.

        :param application_id: The ApplicationId of the Environment resource.
        :param environment_id: The EnvironmentId of the Environment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appconfig as interfaces_appconfig
            
            environment_reference = interfaces_appconfig.EnvironmentReference(
                application_id="applicationId",
                environment_id="environmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d864f328e31745137bf18010cdd90ca921175c6eb59dea6ebef0e3cd9f50963f)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "environment_id": environment_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Environment resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''The EnvironmentId of the Environment resource.'''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.ExtensionAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "extension_association_arn": "extensionAssociationArn",
        "extension_association_id": "extensionAssociationId",
    },
)
class ExtensionAssociationReference:
    def __init__(
        self,
        *,
        extension_association_arn: builtins.str,
        extension_association_id: builtins.str,
    ) -> None:
        '''A reference to a ExtensionAssociation resource.

        :param extension_association_arn: The ARN of the ExtensionAssociation resource.
        :param extension_association_id: The Id of the ExtensionAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appconfig as interfaces_appconfig
            
            extension_association_reference = interfaces_appconfig.ExtensionAssociationReference(
                extension_association_arn="extensionAssociationArn",
                extension_association_id="extensionAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10652230237f0fd40d5218c4e7677bbb09b1c6ca5ed3c7fc2394c9e2b9d792d3)
            check_type(argname="argument extension_association_arn", value=extension_association_arn, expected_type=type_hints["extension_association_arn"])
            check_type(argname="argument extension_association_id", value=extension_association_id, expected_type=type_hints["extension_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "extension_association_arn": extension_association_arn,
            "extension_association_id": extension_association_id,
        }

    @builtins.property
    def extension_association_arn(self) -> builtins.str:
        '''The ARN of the ExtensionAssociation resource.'''
        result = self._values.get("extension_association_arn")
        assert result is not None, "Required property 'extension_association_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def extension_association_id(self) -> builtins.str:
        '''The Id of the ExtensionAssociation resource.'''
        result = self._values.get("extension_association_id")
        assert result is not None, "Required property 'extension_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtensionAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.ExtensionReference",
    jsii_struct_bases=[],
    name_mapping={"extension_arn": "extensionArn", "extension_id": "extensionId"},
)
class ExtensionReference:
    def __init__(
        self,
        *,
        extension_arn: builtins.str,
        extension_id: builtins.str,
    ) -> None:
        '''A reference to a Extension resource.

        :param extension_arn: The ARN of the Extension resource.
        :param extension_id: The Id of the Extension resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appconfig as interfaces_appconfig
            
            extension_reference = interfaces_appconfig.ExtensionReference(
                extension_arn="extensionArn",
                extension_id="extensionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf99e33e03afa132b00013dc1ec538306dcdc67ccae0e38cfa412052055ea336)
            check_type(argname="argument extension_arn", value=extension_arn, expected_type=type_hints["extension_arn"])
            check_type(argname="argument extension_id", value=extension_id, expected_type=type_hints["extension_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "extension_arn": extension_arn,
            "extension_id": extension_id,
        }

    @builtins.property
    def extension_arn(self) -> builtins.str:
        '''The ARN of the Extension resource.'''
        result = self._values.get("extension_arn")
        assert result is not None, "Required property 'extension_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def extension_id(self) -> builtins.str:
        '''The Id of the Extension resource.'''
        result = self._values.get("extension_id")
        assert result is not None, "Required property 'extension_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtensionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.HostedConfigurationVersionReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "configuration_profile_id": "configurationProfileId",
        "version_number": "versionNumber",
    },
)
class HostedConfigurationVersionReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        configuration_profile_id: builtins.str,
        version_number: builtins.str,
    ) -> None:
        '''A reference to a HostedConfigurationVersion resource.

        :param application_id: The ApplicationId of the HostedConfigurationVersion resource.
        :param configuration_profile_id: The ConfigurationProfileId of the HostedConfigurationVersion resource.
        :param version_number: The VersionNumber of the HostedConfigurationVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appconfig as interfaces_appconfig
            
            hosted_configuration_version_reference = interfaces_appconfig.HostedConfigurationVersionReference(
                application_id="applicationId",
                configuration_profile_id="configurationProfileId",
                version_number="versionNumber"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1125b772c448b6fa13e89374f217c3b5cc8085c39232473151424bcc5ee95e37)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument configuration_profile_id", value=configuration_profile_id, expected_type=type_hints["configuration_profile_id"])
            check_type(argname="argument version_number", value=version_number, expected_type=type_hints["version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "configuration_profile_id": configuration_profile_id,
            "version_number": version_number,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the HostedConfigurationVersion resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_profile_id(self) -> builtins.str:
        '''The ConfigurationProfileId of the HostedConfigurationVersion resource.'''
        result = self._values.get("configuration_profile_id")
        assert result is not None, "Required property 'configuration_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_number(self) -> builtins.str:
        '''The VersionNumber of the HostedConfigurationVersion resource.'''
        result = self._values.get("version_number")
        assert result is not None, "Required property 'version_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedConfigurationVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appconfig.IApplicationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appconfig.IApplicationRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.IConfigurationProfileRef"
)
class IConfigurationProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationProfileRef")
    def configuration_profile_ref(self) -> "ConfigurationProfileReference":
        '''(experimental) A reference to a ConfigurationProfile resource.

        :stability: experimental
        '''
        ...


class _IConfigurationProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appconfig.IConfigurationProfileRef"

    @builtins.property
    @jsii.member(jsii_name="configurationProfileRef")
    def configuration_profile_ref(self) -> "ConfigurationProfileReference":
        '''(experimental) A reference to a ConfigurationProfile resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationProfileReference", jsii.get(self, "configurationProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationProfileRef).__jsii_proxy_class__ = lambda : _IConfigurationProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appconfig.IDeploymentRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appconfig.IDeploymentRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.IDeploymentStrategyRef"
)
class IDeploymentStrategyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeploymentStrategy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyRef")
    def deployment_strategy_ref(self) -> "DeploymentStrategyReference":
        '''(experimental) A reference to a DeploymentStrategy resource.

        :stability: experimental
        '''
        ...


class _IDeploymentStrategyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeploymentStrategy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appconfig.IDeploymentStrategyRef"

    @builtins.property
    @jsii.member(jsii_name="deploymentStrategyRef")
    def deployment_strategy_ref(self) -> "DeploymentStrategyReference":
        '''(experimental) A reference to a DeploymentStrategy resource.

        :stability: experimental
        '''
        return typing.cast("DeploymentStrategyReference", jsii.get(self, "deploymentStrategyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeploymentStrategyRef).__jsii_proxy_class__ = lambda : _IDeploymentStrategyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appconfig.IEnvironmentRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appconfig.IEnvironmentRef"

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentReference", jsii.get(self, "environmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentRef).__jsii_proxy_class__ = lambda : _IEnvironmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.IExtensionAssociationRef"
)
class IExtensionAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ExtensionAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="extensionAssociationRef")
    def extension_association_ref(self) -> "ExtensionAssociationReference":
        '''(experimental) A reference to a ExtensionAssociation resource.

        :stability: experimental
        '''
        ...


class _IExtensionAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ExtensionAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appconfig.IExtensionAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="extensionAssociationRef")
    def extension_association_ref(self) -> "ExtensionAssociationReference":
        '''(experimental) A reference to a ExtensionAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ExtensionAssociationReference", jsii.get(self, "extensionAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExtensionAssociationRef).__jsii_proxy_class__ = lambda : _IExtensionAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appconfig.IExtensionRef")
class IExtensionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Extension.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="extensionRef")
    def extension_ref(self) -> "ExtensionReference":
        '''(experimental) A reference to a Extension resource.

        :stability: experimental
        '''
        ...


class _IExtensionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Extension.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appconfig.IExtensionRef"

    @builtins.property
    @jsii.member(jsii_name="extensionRef")
    def extension_ref(self) -> "ExtensionReference":
        '''(experimental) A reference to a Extension resource.

        :stability: experimental
        '''
        return typing.cast("ExtensionReference", jsii.get(self, "extensionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExtensionRef).__jsii_proxy_class__ = lambda : _IExtensionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appconfig.IHostedConfigurationVersionRef"
)
class IHostedConfigurationVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HostedConfigurationVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hostedConfigurationVersionRef")
    def hosted_configuration_version_ref(self) -> "HostedConfigurationVersionReference":
        '''(experimental) A reference to a HostedConfigurationVersion resource.

        :stability: experimental
        '''
        ...


class _IHostedConfigurationVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HostedConfigurationVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appconfig.IHostedConfigurationVersionRef"

    @builtins.property
    @jsii.member(jsii_name="hostedConfigurationVersionRef")
    def hosted_configuration_version_ref(self) -> "HostedConfigurationVersionReference":
        '''(experimental) A reference to a HostedConfigurationVersion resource.

        :stability: experimental
        '''
        return typing.cast("HostedConfigurationVersionReference", jsii.get(self, "hostedConfigurationVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHostedConfigurationVersionRef).__jsii_proxy_class__ = lambda : _IHostedConfigurationVersionRefProxy


__all__ = [
    "ApplicationReference",
    "ConfigurationProfileReference",
    "DeploymentReference",
    "DeploymentStrategyReference",
    "EnvironmentReference",
    "ExtensionAssociationReference",
    "ExtensionReference",
    "HostedConfigurationVersionReference",
    "IApplicationRef",
    "IConfigurationProfileRef",
    "IDeploymentRef",
    "IDeploymentStrategyRef",
    "IEnvironmentRef",
    "IExtensionAssociationRef",
    "IExtensionRef",
    "IHostedConfigurationVersionRef",
]

publication.publish()

def _typecheckingstub__7897eb149d1f049c9474b1cc9cde497acc7eef83b557fd5e69865922db577813(
    *,
    application_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__196a649cb6c8bc25d8b70a62cca359e16bc48f7cbc911cefc2c922986a508932(
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3e55ba941a1da007e8831ae6e5ecb2628164a77f73db6a0cb54cab47f747f15(
    *,
    application_id: builtins.str,
    deployment_number: builtins.str,
    environment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__026929d86c5cf003577354c6fd4824313f828abc9fa63f8c14581f710b6b7cbb(
    *,
    deployment_strategy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d864f328e31745137bf18010cdd90ca921175c6eb59dea6ebef0e3cd9f50963f(
    *,
    application_id: builtins.str,
    environment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10652230237f0fd40d5218c4e7677bbb09b1c6ca5ed3c7fc2394c9e2b9d792d3(
    *,
    extension_association_arn: builtins.str,
    extension_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf99e33e03afa132b00013dc1ec538306dcdc67ccae0e38cfa412052055ea336(
    *,
    extension_arn: builtins.str,
    extension_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1125b772c448b6fa13e89374f217c3b5cc8085c39232473151424bcc5ee95e37(
    *,
    application_id: builtins.str,
    configuration_profile_id: builtins.str,
    version_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IConfigurationProfileRef, IDeploymentRef, IDeploymentStrategyRef, IEnvironmentRef, IExtensionAssociationRef, IExtensionRef, IHostedConfigurationVersionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
