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
    jsii_type="aws-cdk-lib.interfaces.aws_panorama.ApplicationInstanceReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_instance_arn": "applicationInstanceArn",
        "application_instance_id": "applicationInstanceId",
    },
)
class ApplicationInstanceReference:
    def __init__(
        self,
        *,
        application_instance_arn: builtins.str,
        application_instance_id: builtins.str,
    ) -> None:
        '''A reference to a ApplicationInstance resource.

        :param application_instance_arn: The ARN of the ApplicationInstance resource.
        :param application_instance_id: The ApplicationInstanceId of the ApplicationInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_panorama as interfaces_panorama
            
            application_instance_reference = interfaces_panorama.ApplicationInstanceReference(
                application_instance_arn="applicationInstanceArn",
                application_instance_id="applicationInstanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6dfaa8f537f90aa738e82382bd835aeb181bd9d40328bc04994dc253d685f8)
            check_type(argname="argument application_instance_arn", value=application_instance_arn, expected_type=type_hints["application_instance_arn"])
            check_type(argname="argument application_instance_id", value=application_instance_id, expected_type=type_hints["application_instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_instance_arn": application_instance_arn,
            "application_instance_id": application_instance_id,
        }

    @builtins.property
    def application_instance_arn(self) -> builtins.str:
        '''The ARN of the ApplicationInstance resource.'''
        result = self._values.get("application_instance_arn")
        assert result is not None, "Required property 'application_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_instance_id(self) -> builtins.str:
        '''The ApplicationInstanceId of the ApplicationInstance resource.'''
        result = self._values.get("application_instance_id")
        assert result is not None, "Required property 'application_instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_panorama.IApplicationInstanceRef"
)
class IApplicationInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationInstanceRef")
    def application_instance_ref(self) -> "ApplicationInstanceReference":
        '''(experimental) A reference to a ApplicationInstance resource.

        :stability: experimental
        '''
        ...


class _IApplicationInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_panorama.IApplicationInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="applicationInstanceRef")
    def application_instance_ref(self) -> "ApplicationInstanceReference":
        '''(experimental) A reference to a ApplicationInstance resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationInstanceReference", jsii.get(self, "applicationInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationInstanceRef).__jsii_proxy_class__ = lambda : _IApplicationInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_panorama.IPackageRef")
class IPackageRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Package.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="packageRef")
    def package_ref(self) -> "PackageReference":
        '''(experimental) A reference to a Package resource.

        :stability: experimental
        '''
        ...


class _IPackageRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Package.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_panorama.IPackageRef"

    @builtins.property
    @jsii.member(jsii_name="packageRef")
    def package_ref(self) -> "PackageReference":
        '''(experimental) A reference to a Package resource.

        :stability: experimental
        '''
        return typing.cast("PackageReference", jsii.get(self, "packageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPackageRef).__jsii_proxy_class__ = lambda : _IPackageRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_panorama.IPackageVersionRef")
class IPackageVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PackageVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="packageVersionRef")
    def package_version_ref(self) -> "PackageVersionReference":
        '''(experimental) A reference to a PackageVersion resource.

        :stability: experimental
        '''
        ...


class _IPackageVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PackageVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_panorama.IPackageVersionRef"

    @builtins.property
    @jsii.member(jsii_name="packageVersionRef")
    def package_version_ref(self) -> "PackageVersionReference":
        '''(experimental) A reference to a PackageVersion resource.

        :stability: experimental
        '''
        return typing.cast("PackageVersionReference", jsii.get(self, "packageVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPackageVersionRef).__jsii_proxy_class__ = lambda : _IPackageVersionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_panorama.PackageReference",
    jsii_struct_bases=[],
    name_mapping={"package_arn": "packageArn", "package_id": "packageId"},
)
class PackageReference:
    def __init__(self, *, package_arn: builtins.str, package_id: builtins.str) -> None:
        '''A reference to a Package resource.

        :param package_arn: The ARN of the Package resource.
        :param package_id: The PackageId of the Package resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_panorama as interfaces_panorama
            
            package_reference = interfaces_panorama.PackageReference(
                package_arn="packageArn",
                package_id="packageId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__605f9abe0963dfdef5a4c1848987a62e79ae98f13697abc2b2af77153e3391ef)
            check_type(argname="argument package_arn", value=package_arn, expected_type=type_hints["package_arn"])
            check_type(argname="argument package_id", value=package_id, expected_type=type_hints["package_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package_arn": package_arn,
            "package_id": package_id,
        }

    @builtins.property
    def package_arn(self) -> builtins.str:
        '''The ARN of the Package resource.'''
        result = self._values.get("package_arn")
        assert result is not None, "Required property 'package_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def package_id(self) -> builtins.str:
        '''The PackageId of the Package resource.'''
        result = self._values.get("package_id")
        assert result is not None, "Required property 'package_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PackageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_panorama.PackageVersionReference",
    jsii_struct_bases=[],
    name_mapping={
        "package_id": "packageId",
        "package_version": "packageVersion",
        "patch_version": "patchVersion",
    },
)
class PackageVersionReference:
    def __init__(
        self,
        *,
        package_id: builtins.str,
        package_version: builtins.str,
        patch_version: builtins.str,
    ) -> None:
        '''A reference to a PackageVersion resource.

        :param package_id: The PackageId of the PackageVersion resource.
        :param package_version: The PackageVersion of the PackageVersion resource.
        :param patch_version: The PatchVersion of the PackageVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_panorama as interfaces_panorama
            
            package_version_reference = interfaces_panorama.PackageVersionReference(
                package_id="packageId",
                package_version="packageVersion",
                patch_version="patchVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a03fa07d03ba5a5975cf882c650b846855e6c7a271fc90267dc94589fb751155)
            check_type(argname="argument package_id", value=package_id, expected_type=type_hints["package_id"])
            check_type(argname="argument package_version", value=package_version, expected_type=type_hints["package_version"])
            check_type(argname="argument patch_version", value=patch_version, expected_type=type_hints["patch_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package_id": package_id,
            "package_version": package_version,
            "patch_version": patch_version,
        }

    @builtins.property
    def package_id(self) -> builtins.str:
        '''The PackageId of the PackageVersion resource.'''
        result = self._values.get("package_id")
        assert result is not None, "Required property 'package_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def package_version(self) -> builtins.str:
        '''The PackageVersion of the PackageVersion resource.'''
        result = self._values.get("package_version")
        assert result is not None, "Required property 'package_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def patch_version(self) -> builtins.str:
        '''The PatchVersion of the PackageVersion resource.'''
        result = self._values.get("patch_version")
        assert result is not None, "Required property 'patch_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PackageVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApplicationInstanceReference",
    "IApplicationInstanceRef",
    "IPackageRef",
    "IPackageVersionRef",
    "PackageReference",
    "PackageVersionReference",
]

publication.publish()

def _typecheckingstub__5e6dfaa8f537f90aa738e82382bd835aeb181bd9d40328bc04994dc253d685f8(
    *,
    application_instance_arn: builtins.str,
    application_instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__605f9abe0963dfdef5a4c1848987a62e79ae98f13697abc2b2af77153e3391ef(
    *,
    package_arn: builtins.str,
    package_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a03fa07d03ba5a5975cf882c650b846855e6c7a271fc90267dc94589fb751155(
    *,
    package_id: builtins.str,
    package_version: builtins.str,
    patch_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationInstanceRef, IPackageRef, IPackageVersionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
