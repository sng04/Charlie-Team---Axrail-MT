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
    jsii_type="aws-cdk-lib.interfaces.aws_m2.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_arn": "applicationArn"},
)
class ApplicationReference:
    def __init__(self, *, application_arn: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_arn: The ApplicationArn of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_m2 as interfaces_m2
            
            application_reference = interfaces_m2.ApplicationReference(
                application_arn="applicationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77586d2283f53dae8fe3468bf4af628757cef7faae5ddbe1d044a53eb7e04d5f)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ApplicationArn of the Application resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_m2.DeploymentReference",
    jsii_struct_bases=[],
    name_mapping={"application_id": "applicationId"},
)
class DeploymentReference:
    def __init__(self, *, application_id: builtins.str) -> None:
        '''A reference to a Deployment resource.

        :param application_id: The ApplicationId of the Deployment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_m2 as interfaces_m2
            
            deployment_reference = interfaces_m2.DeploymentReference(
                application_id="applicationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd9436bd12baf97b13fde300d01d90ff60e82bba2fc973a77ac20037b850428d)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Deployment resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_m2.EnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={"environment_arn": "environmentArn"},
)
class EnvironmentReference:
    def __init__(self, *, environment_arn: builtins.str) -> None:
        '''A reference to a Environment resource.

        :param environment_arn: The EnvironmentArn of the Environment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_m2 as interfaces_m2
            
            environment_reference = interfaces_m2.EnvironmentReference(
                environment_arn="environmentArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd5ec1aac66edf34d1d2747a9c80344b878233fe69c015794f7b2ce302b9b2c4)
            check_type(argname="argument environment_arn", value=environment_arn, expected_type=type_hints["environment_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment_arn": environment_arn,
        }

    @builtins.property
    def environment_arn(self) -> builtins.str:
        '''The EnvironmentArn of the Environment resource.'''
        result = self._values.get("environment_arn")
        assert result is not None, "Required property 'environment_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_m2.IApplicationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_m2.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_m2.IDeploymentRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_m2.IDeploymentRef"

    @builtins.property
    @jsii.member(jsii_name="deploymentRef")
    def deployment_ref(self) -> "DeploymentReference":
        '''(experimental) A reference to a Deployment resource.

        :stability: experimental
        '''
        return typing.cast("DeploymentReference", jsii.get(self, "deploymentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeploymentRef).__jsii_proxy_class__ = lambda : _IDeploymentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_m2.IEnvironmentRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_m2.IEnvironmentRef"

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
    "DeploymentReference",
    "EnvironmentReference",
    "IApplicationRef",
    "IDeploymentRef",
    "IEnvironmentRef",
]

publication.publish()

def _typecheckingstub__77586d2283f53dae8fe3468bf4af628757cef7faae5ddbe1d044a53eb7e04d5f(
    *,
    application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd9436bd12baf97b13fde300d01d90ff60e82bba2fc973a77ac20037b850428d(
    *,
    application_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd5ec1aac66edf34d1d2747a9c80344b878233fe69c015794f7b2ce302b9b2c4(
    *,
    environment_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IDeploymentRef, IEnvironmentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
