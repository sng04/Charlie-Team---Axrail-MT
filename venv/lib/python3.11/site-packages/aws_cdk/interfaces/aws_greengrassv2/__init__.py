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
    jsii_type="aws-cdk-lib.interfaces.aws_greengrassv2.ComponentVersionReference",
    jsii_struct_bases=[],
    name_mapping={"component_version_arn": "componentVersionArn"},
)
class ComponentVersionReference:
    def __init__(self, *, component_version_arn: builtins.str) -> None:
        '''A reference to a ComponentVersion resource.

        :param component_version_arn: The Arn of the ComponentVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrassv2 as interfaces_greengrassv2
            
            component_version_reference = interfaces_greengrassv2.ComponentVersionReference(
                component_version_arn="componentVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b561ccf5eed9b336d8c813bd63f949e53a31db1f1003b887c6411feb0176920e)
            check_type(argname="argument component_version_arn", value=component_version_arn, expected_type=type_hints["component_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "component_version_arn": component_version_arn,
        }

    @builtins.property
    def component_version_arn(self) -> builtins.str:
        '''The Arn of the ComponentVersion resource.'''
        result = self._values.get("component_version_arn")
        assert result is not None, "Required property 'component_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComponentVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrassv2.DeploymentReference",
    jsii_struct_bases=[],
    name_mapping={"deployment_id": "deploymentId"},
)
class DeploymentReference:
    def __init__(self, *, deployment_id: builtins.str) -> None:
        '''A reference to a Deployment resource.

        :param deployment_id: The DeploymentId of the Deployment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrassv2 as interfaces_greengrassv2
            
            deployment_reference = interfaces_greengrassv2.DeploymentReference(
                deployment_id="deploymentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb98e887b4cc39f031bbc779f448bed967d9c4873a11f351be83a169aa26c03b)
            check_type(argname="argument deployment_id", value=deployment_id, expected_type=type_hints["deployment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_id": deployment_id,
        }

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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrassv2.IComponentVersionRef"
)
class IComponentVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ComponentVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="componentVersionRef")
    def component_version_ref(self) -> "ComponentVersionReference":
        '''(experimental) A reference to a ComponentVersion resource.

        :stability: experimental
        '''
        ...


class _IComponentVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ComponentVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrassv2.IComponentVersionRef"

    @builtins.property
    @jsii.member(jsii_name="componentVersionRef")
    def component_version_ref(self) -> "ComponentVersionReference":
        '''(experimental) A reference to a ComponentVersion resource.

        :stability: experimental
        '''
        return typing.cast("ComponentVersionReference", jsii.get(self, "componentVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IComponentVersionRef).__jsii_proxy_class__ = lambda : _IComponentVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_greengrassv2.IDeploymentRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrassv2.IDeploymentRef"

    @builtins.property
    @jsii.member(jsii_name="deploymentRef")
    def deployment_ref(self) -> "DeploymentReference":
        '''(experimental) A reference to a Deployment resource.

        :stability: experimental
        '''
        return typing.cast("DeploymentReference", jsii.get(self, "deploymentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeploymentRef).__jsii_proxy_class__ = lambda : _IDeploymentRefProxy


__all__ = [
    "ComponentVersionReference",
    "DeploymentReference",
    "IComponentVersionRef",
    "IDeploymentRef",
]

publication.publish()

def _typecheckingstub__b561ccf5eed9b336d8c813bd63f949e53a31db1f1003b887c6411feb0176920e(
    *,
    component_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb98e887b4cc39f031bbc779f448bed967d9c4873a11f351be83a169aa26c03b(
    *,
    deployment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IComponentVersionRef, IDeploymentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
