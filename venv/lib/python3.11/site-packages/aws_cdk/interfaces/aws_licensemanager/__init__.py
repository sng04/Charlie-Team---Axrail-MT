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
    jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.GrantReference",
    jsii_struct_bases=[],
    name_mapping={"grant_arn": "grantArn"},
)
class GrantReference:
    def __init__(self, *, grant_arn: builtins.str) -> None:
        '''A reference to a Grant resource.

        :param grant_arn: The GrantArn of the Grant resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_licensemanager as interfaces_licensemanager
            
            grant_reference = interfaces_licensemanager.GrantReference(
                grant_arn="grantArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__509345cf0b8df3531dd2233cb8ca72a49893c49948d88feade0b6e134b33772d)
            check_type(argname="argument grant_arn", value=grant_arn, expected_type=type_hints["grant_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "grant_arn": grant_arn,
        }

    @builtins.property
    def grant_arn(self) -> builtins.str:
        '''The GrantArn of the Grant resource.'''
        result = self._values.get("grant_arn")
        assert result is not None, "Required property 'grant_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GrantReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.IGrantRef")
class IGrantRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Grant.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="grantRef")
    def grant_ref(self) -> "GrantReference":
        '''(experimental) A reference to a Grant resource.

        :stability: experimental
        '''
        ...


class _IGrantRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Grant.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_licensemanager.IGrantRef"

    @builtins.property
    @jsii.member(jsii_name="grantRef")
    def grant_ref(self) -> "GrantReference":
        '''(experimental) A reference to a Grant resource.

        :stability: experimental
        '''
        return typing.cast("GrantReference", jsii.get(self, "grantRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGrantRef).__jsii_proxy_class__ = lambda : _IGrantRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.ILicenseRef")
class ILicenseRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a License.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="licenseRef")
    def license_ref(self) -> "LicenseReference":
        '''(experimental) A reference to a License resource.

        :stability: experimental
        '''
        ...


class _ILicenseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a License.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_licensemanager.ILicenseRef"

    @builtins.property
    @jsii.member(jsii_name="licenseRef")
    def license_ref(self) -> "LicenseReference":
        '''(experimental) A reference to a License resource.

        :stability: experimental
        '''
        return typing.cast("LicenseReference", jsii.get(self, "licenseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILicenseRef).__jsii_proxy_class__ = lambda : _ILicenseRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_licensemanager.LicenseReference",
    jsii_struct_bases=[],
    name_mapping={"license_arn": "licenseArn"},
)
class LicenseReference:
    def __init__(self, *, license_arn: builtins.str) -> None:
        '''A reference to a License resource.

        :param license_arn: The LicenseArn of the License resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_licensemanager as interfaces_licensemanager
            
            license_reference = interfaces_licensemanager.LicenseReference(
                license_arn="licenseArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ce44a0b5c8ac0b1ac5b4c7e7e57091674992170e45de59a47767d1279342850)
            check_type(argname="argument license_arn", value=license_arn, expected_type=type_hints["license_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "license_arn": license_arn,
        }

    @builtins.property
    def license_arn(self) -> builtins.str:
        '''The LicenseArn of the License resource.'''
        result = self._values.get("license_arn")
        assert result is not None, "Required property 'license_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LicenseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GrantReference",
    "IGrantRef",
    "ILicenseRef",
    "LicenseReference",
]

publication.publish()

def _typecheckingstub__509345cf0b8df3531dd2233cb8ca72a49893c49948d88feade0b6e134b33772d(
    *,
    grant_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ce44a0b5c8ac0b1ac5b4c7e7e57091674992170e45de59a47767d1279342850(
    *,
    license_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGrantRef, ILicenseRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
