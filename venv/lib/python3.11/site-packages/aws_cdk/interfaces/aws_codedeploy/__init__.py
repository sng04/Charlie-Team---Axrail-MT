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
    jsii_type="aws-cdk-lib.interfaces.aws_codedeploy.ApplicationReference",
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
            from aws_cdk.interfaces import aws_codedeploy as interfaces_codedeploy
            
            application_reference = interfaces_codedeploy.ApplicationReference(
                application_name="applicationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__418c8f26c4d68b972ebffadc2241204b3326ab58afc0941988bf813d3f798885)
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
    jsii_type="aws-cdk-lib.interfaces.aws_codedeploy.DeploymentConfigReference",
    jsii_struct_bases=[],
    name_mapping={"deployment_config_name": "deploymentConfigName"},
)
class DeploymentConfigReference:
    def __init__(self, *, deployment_config_name: builtins.str) -> None:
        '''A reference to a DeploymentConfig resource.

        :param deployment_config_name: The DeploymentConfigName of the DeploymentConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codedeploy as interfaces_codedeploy
            
            deployment_config_reference = interfaces_codedeploy.DeploymentConfigReference(
                deployment_config_name="deploymentConfigName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5f932da1842dc9d191290d12508917bcda09a6cf6732df837bea4171333d29)
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_config_name": deployment_config_name,
        }

    @builtins.property
    def deployment_config_name(self) -> builtins.str:
        '''The DeploymentConfigName of the DeploymentConfig resource.'''
        result = self._values.get("deployment_config_name")
        assert result is not None, "Required property 'deployment_config_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codedeploy.DeploymentGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "deployment_group_name": "deploymentGroupName",
    },
)
class DeploymentGroupReference:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        deployment_group_name: builtins.str,
    ) -> None:
        '''A reference to a DeploymentGroup resource.

        :param application_name: The ApplicationName of the DeploymentGroup resource.
        :param deployment_group_name: The DeploymentGroupName of the DeploymentGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codedeploy as interfaces_codedeploy
            
            deployment_group_reference = interfaces_codedeploy.DeploymentGroupReference(
                application_name="applicationName",
                deployment_group_name="deploymentGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c560dfbd151d8fb2d2f16ee5760ff9916205046ef068a01bf7cbad08a59f075f)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "deployment_group_name": deployment_group_name,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The ApplicationName of the DeploymentGroup resource.'''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_group_name(self) -> builtins.str:
        '''The DeploymentGroupName of the DeploymentGroup resource.'''
        result = self._values.get("deployment_group_name")
        assert result is not None, "Required property 'deployment_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeploymentGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codedeploy.IApplicationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codedeploy.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codedeploy.IDeploymentConfigRef")
class IDeploymentConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeploymentConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigRef")
    def deployment_config_ref(self) -> "DeploymentConfigReference":
        '''(experimental) A reference to a DeploymentConfig resource.

        :stability: experimental
        '''
        ...


class _IDeploymentConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeploymentConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codedeploy.IDeploymentConfigRef"

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigRef")
    def deployment_config_ref(self) -> "DeploymentConfigReference":
        '''(experimental) A reference to a DeploymentConfig resource.

        :stability: experimental
        '''
        return typing.cast("DeploymentConfigReference", jsii.get(self, "deploymentConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeploymentConfigRef).__jsii_proxy_class__ = lambda : _IDeploymentConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codedeploy.IDeploymentGroupRef")
class IDeploymentGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeploymentGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupRef")
    def deployment_group_ref(self) -> "DeploymentGroupReference":
        '''(experimental) A reference to a DeploymentGroup resource.

        :stability: experimental
        '''
        ...


class _IDeploymentGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeploymentGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codedeploy.IDeploymentGroupRef"

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupRef")
    def deployment_group_ref(self) -> "DeploymentGroupReference":
        '''(experimental) A reference to a DeploymentGroup resource.

        :stability: experimental
        '''
        return typing.cast("DeploymentGroupReference", jsii.get(self, "deploymentGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeploymentGroupRef).__jsii_proxy_class__ = lambda : _IDeploymentGroupRefProxy


__all__ = [
    "ApplicationReference",
    "DeploymentConfigReference",
    "DeploymentGroupReference",
    "IApplicationRef",
    "IDeploymentConfigRef",
    "IDeploymentGroupRef",
]

publication.publish()

def _typecheckingstub__418c8f26c4d68b972ebffadc2241204b3326ab58afc0941988bf813d3f798885(
    *,
    application_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5f932da1842dc9d191290d12508917bcda09a6cf6732df837bea4171333d29(
    *,
    deployment_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c560dfbd151d8fb2d2f16ee5760ff9916205046ef068a01bf7cbad08a59f075f(
    *,
    application_name: builtins.str,
    deployment_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IDeploymentConfigRef, IDeploymentGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
