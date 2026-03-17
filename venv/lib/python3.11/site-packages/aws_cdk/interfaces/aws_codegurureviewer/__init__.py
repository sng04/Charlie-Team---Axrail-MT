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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_codegurureviewer.IRepositoryAssociationRef"
)
class IRepositoryAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RepositoryAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="repositoryAssociationRef")
    def repository_association_ref(self) -> "RepositoryAssociationReference":
        '''(experimental) A reference to a RepositoryAssociation resource.

        :stability: experimental
        '''
        ...


class _IRepositoryAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RepositoryAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codegurureviewer.IRepositoryAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="repositoryAssociationRef")
    def repository_association_ref(self) -> "RepositoryAssociationReference":
        '''(experimental) A reference to a RepositoryAssociation resource.

        :stability: experimental
        '''
        return typing.cast("RepositoryAssociationReference", jsii.get(self, "repositoryAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRepositoryAssociationRef).__jsii_proxy_class__ = lambda : _IRepositoryAssociationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codegurureviewer.RepositoryAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"association_arn": "associationArn"},
)
class RepositoryAssociationReference:
    def __init__(self, *, association_arn: builtins.str) -> None:
        '''A reference to a RepositoryAssociation resource.

        :param association_arn: The AssociationArn of the RepositoryAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codegurureviewer as interfaces_codegurureviewer
            
            repository_association_reference = interfaces_codegurureviewer.RepositoryAssociationReference(
                association_arn="associationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e2099ad89f99f82740ae17690776222bb1e1e24db471751f263482a817bd0b5)
            check_type(argname="argument association_arn", value=association_arn, expected_type=type_hints["association_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_arn": association_arn,
        }

    @builtins.property
    def association_arn(self) -> builtins.str:
        '''The AssociationArn of the RepositoryAssociation resource.'''
        result = self._values.get("association_arn")
        assert result is not None, "Required property 'association_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IRepositoryAssociationRef",
    "RepositoryAssociationReference",
]

publication.publish()

def _typecheckingstub__3e2099ad89f99f82740ae17690776222bb1e1e24db471751f263482a817bd0b5(
    *,
    association_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IRepositoryAssociationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
