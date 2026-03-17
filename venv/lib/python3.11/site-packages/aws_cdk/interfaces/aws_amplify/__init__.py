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
    jsii_type="aws-cdk-lib.interfaces.aws_amplify.AppReference",
    jsii_struct_bases=[],
    name_mapping={"app_arn": "appArn"},
)
class AppReference:
    def __init__(self, *, app_arn: builtins.str) -> None:
        '''A reference to a App resource.

        :param app_arn: The Arn of the App resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_amplify as interfaces_amplify
            
            app_reference = interfaces_amplify.AppReference(
                app_arn="appArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3f5f75b3136b3257fafea47a1cb21c6949a62fbdcd1ccbfc6a668de4d87e657)
            check_type(argname="argument app_arn", value=app_arn, expected_type=type_hints["app_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_arn": app_arn,
        }

    @builtins.property
    def app_arn(self) -> builtins.str:
        '''The Arn of the App resource.'''
        result = self._values.get("app_arn")
        assert result is not None, "Required property 'app_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_amplify.BranchReference",
    jsii_struct_bases=[],
    name_mapping={"branch_arn": "branchArn"},
)
class BranchReference:
    def __init__(self, *, branch_arn: builtins.str) -> None:
        '''A reference to a Branch resource.

        :param branch_arn: The Arn of the Branch resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_amplify as interfaces_amplify
            
            branch_reference = interfaces_amplify.BranchReference(
                branch_arn="branchArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1345457bf42bf8b5ab573d52d56a0e612e3a953d8b9aa6c5bd0f92cbe79d405)
            check_type(argname="argument branch_arn", value=branch_arn, expected_type=type_hints["branch_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "branch_arn": branch_arn,
        }

    @builtins.property
    def branch_arn(self) -> builtins.str:
        '''The Arn of the Branch resource.'''
        result = self._values.get("branch_arn")
        assert result is not None, "Required property 'branch_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BranchReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_amplify.DomainReference",
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
            from aws_cdk.interfaces import aws_amplify as interfaces_amplify
            
            domain_reference = interfaces_amplify.DomainReference(
                domain_arn="domainArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c9905854ff8dd39e3209f2f3215976ebe6df84235c273eb22124aec84898e5d)
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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_amplify.IAppRef")
class IAppRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        ...


class _IAppRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_amplify.IAppRef"

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        return typing.cast("AppReference", jsii.get(self, "appRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppRef).__jsii_proxy_class__ = lambda : _IAppRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_amplify.IBranchRef")
class IBranchRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Branch.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="branchRef")
    def branch_ref(self) -> "BranchReference":
        '''(experimental) A reference to a Branch resource.

        :stability: experimental
        '''
        ...


class _IBranchRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Branch.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_amplify.IBranchRef"

    @builtins.property
    @jsii.member(jsii_name="branchRef")
    def branch_ref(self) -> "BranchReference":
        '''(experimental) A reference to a Branch resource.

        :stability: experimental
        '''
        return typing.cast("BranchReference", jsii.get(self, "branchRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBranchRef).__jsii_proxy_class__ = lambda : _IBranchRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_amplify.IDomainRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_amplify.IDomainRef"

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        return typing.cast("DomainReference", jsii.get(self, "domainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainRef).__jsii_proxy_class__ = lambda : _IDomainRefProxy


__all__ = [
    "AppReference",
    "BranchReference",
    "DomainReference",
    "IAppRef",
    "IBranchRef",
    "IDomainRef",
]

publication.publish()

def _typecheckingstub__f3f5f75b3136b3257fafea47a1cb21c6949a62fbdcd1ccbfc6a668de4d87e657(
    *,
    app_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1345457bf42bf8b5ab573d52d56a0e612e3a953d8b9aa6c5bd0f92cbe79d405(
    *,
    branch_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c9905854ff8dd39e3209f2f3215976ebe6df84235c273eb22124aec84898e5d(
    *,
    domain_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAppRef, IBranchRef, IDomainRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
