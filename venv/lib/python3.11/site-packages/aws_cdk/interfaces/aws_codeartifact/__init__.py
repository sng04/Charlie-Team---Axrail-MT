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
    jsii_type="aws-cdk-lib.interfaces.aws_codeartifact.DomainReference",
    jsii_struct_bases=[],
    name_mapping={"domain_arn": "domainArn"},
)
class DomainReference:
    def __init__(self, *, domain_arn: builtins.str) -> None:
        '''A reference to a Domain resource.

        :param domain_arn: The Arn of the Domain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codeartifact as interfaces_codeartifact
            
            domain_reference = interfaces_codeartifact.DomainReference(
                domain_arn="domainArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41a2e8adc93f09fb495f7cafe9ae47b5cb2f2d6edea7fe9c7dbb518b41e6db00)
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_arn": domain_arn,
        }

    @builtins.property
    def domain_arn(self) -> builtins.str:
        '''The Arn of the Domain resource.'''
        result = self._values.get("domain_arn")
        assert result is not None, "Required property 'domain_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codeartifact.IDomainRef")
class IDomainRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        ...


class _IDomainRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codeartifact.IDomainRef"

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        return typing.cast("DomainReference", jsii.get(self, "domainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainRef).__jsii_proxy_class__ = lambda : _IDomainRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codeartifact.IPackageGroupRef")
class IPackageGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PackageGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="packageGroupRef")
    def package_group_ref(self) -> "PackageGroupReference":
        '''(experimental) A reference to a PackageGroup resource.

        :stability: experimental
        '''
        ...


class _IPackageGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PackageGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codeartifact.IPackageGroupRef"

    @builtins.property
    @jsii.member(jsii_name="packageGroupRef")
    def package_group_ref(self) -> "PackageGroupReference":
        '''(experimental) A reference to a PackageGroup resource.

        :stability: experimental
        '''
        return typing.cast("PackageGroupReference", jsii.get(self, "packageGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPackageGroupRef).__jsii_proxy_class__ = lambda : _IPackageGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codeartifact.IRepositoryRef")
class IRepositoryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Repository.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="repositoryRef")
    def repository_ref(self) -> "RepositoryReference":
        '''(experimental) A reference to a Repository resource.

        :stability: experimental
        '''
        ...


class _IRepositoryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Repository.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codeartifact.IRepositoryRef"

    @builtins.property
    @jsii.member(jsii_name="repositoryRef")
    def repository_ref(self) -> "RepositoryReference":
        '''(experimental) A reference to a Repository resource.

        :stability: experimental
        '''
        return typing.cast("RepositoryReference", jsii.get(self, "repositoryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRepositoryRef).__jsii_proxy_class__ = lambda : _IRepositoryRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codeartifact.PackageGroupReference",
    jsii_struct_bases=[],
    name_mapping={"package_group_arn": "packageGroupArn"},
)
class PackageGroupReference:
    def __init__(self, *, package_group_arn: builtins.str) -> None:
        '''A reference to a PackageGroup resource.

        :param package_group_arn: The Arn of the PackageGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codeartifact as interfaces_codeartifact
            
            package_group_reference = interfaces_codeartifact.PackageGroupReference(
                package_group_arn="packageGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcf0233cf76c4025a2de7a970fe5dd735d68a73f6df3513d8f4449cdab70a95a)
            check_type(argname="argument package_group_arn", value=package_group_arn, expected_type=type_hints["package_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package_group_arn": package_group_arn,
        }

    @builtins.property
    def package_group_arn(self) -> builtins.str:
        '''The Arn of the PackageGroup resource.'''
        result = self._values.get("package_group_arn")
        assert result is not None, "Required property 'package_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PackageGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codeartifact.RepositoryReference",
    jsii_struct_bases=[],
    name_mapping={"repository_arn": "repositoryArn"},
)
class RepositoryReference:
    def __init__(self, *, repository_arn: builtins.str) -> None:
        '''A reference to a Repository resource.

        :param repository_arn: The Arn of the Repository resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codeartifact as interfaces_codeartifact
            
            repository_reference = interfaces_codeartifact.RepositoryReference(
                repository_arn="repositoryArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3ccba1a8433ca9aaff095ed9b4ae410a100b0bc85a8b0656f6d4b5fa262c53d)
            check_type(argname="argument repository_arn", value=repository_arn, expected_type=type_hints["repository_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_arn": repository_arn,
        }

    @builtins.property
    def repository_arn(self) -> builtins.str:
        '''The Arn of the Repository resource.'''
        result = self._values.get("repository_arn")
        assert result is not None, "Required property 'repository_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DomainReference",
    "IDomainRef",
    "IPackageGroupRef",
    "IRepositoryRef",
    "PackageGroupReference",
    "RepositoryReference",
]

publication.publish()

def _typecheckingstub__41a2e8adc93f09fb495f7cafe9ae47b5cb2f2d6edea7fe9c7dbb518b41e6db00(
    *,
    domain_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcf0233cf76c4025a2de7a970fe5dd735d68a73f6df3513d8f4449cdab70a95a(
    *,
    package_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ccba1a8433ca9aaff095ed9b4ae410a100b0bc85a8b0656f6d4b5fa262c53d(
    *,
    repository_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDomainRef, IPackageGroupRef, IRepositoryRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
