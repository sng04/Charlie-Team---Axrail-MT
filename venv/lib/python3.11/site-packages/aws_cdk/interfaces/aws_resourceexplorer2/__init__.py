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
    jsii_type="aws-cdk-lib.interfaces.aws_resourceexplorer2.DefaultViewAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"associated_aws_principal": "associatedAwsPrincipal"},
)
class DefaultViewAssociationReference:
    def __init__(self, *, associated_aws_principal: builtins.str) -> None:
        '''A reference to a DefaultViewAssociation resource.

        :param associated_aws_principal: The AssociatedAwsPrincipal of the DefaultViewAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_resourceexplorer2 as interfaces_resourceexplorer2
            
            default_view_association_reference = interfaces_resourceexplorer2.DefaultViewAssociationReference(
                associated_aws_principal="associatedAwsPrincipal"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b08810f946f0fb1b570baf7b85f43e0860ef69f9324c1bfc8cfd13ab2dcd64be)
            check_type(argname="argument associated_aws_principal", value=associated_aws_principal, expected_type=type_hints["associated_aws_principal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "associated_aws_principal": associated_aws_principal,
        }

    @builtins.property
    def associated_aws_principal(self) -> builtins.str:
        '''The AssociatedAwsPrincipal of the DefaultViewAssociation resource.'''
        result = self._values.get("associated_aws_principal")
        assert result is not None, "Required property 'associated_aws_principal' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DefaultViewAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_resourceexplorer2.IDefaultViewAssociationRef"
)
class IDefaultViewAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DefaultViewAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="defaultViewAssociationRef")
    def default_view_association_ref(self) -> "DefaultViewAssociationReference":
        '''(experimental) A reference to a DefaultViewAssociation resource.

        :stability: experimental
        '''
        ...


class _IDefaultViewAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DefaultViewAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_resourceexplorer2.IDefaultViewAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="defaultViewAssociationRef")
    def default_view_association_ref(self) -> "DefaultViewAssociationReference":
        '''(experimental) A reference to a DefaultViewAssociation resource.

        :stability: experimental
        '''
        return typing.cast("DefaultViewAssociationReference", jsii.get(self, "defaultViewAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDefaultViewAssociationRef).__jsii_proxy_class__ = lambda : _IDefaultViewAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_resourceexplorer2.IIndexRef")
class IIndexRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        ...


class _IIndexRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_resourceexplorer2.IIndexRef"

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        return typing.cast("IndexReference", jsii.get(self, "indexRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIndexRef).__jsii_proxy_class__ = lambda : _IIndexRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_resourceexplorer2.IViewRef")
class IViewRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a View.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="viewRef")
    def view_ref(self) -> "ViewReference":
        '''(experimental) A reference to a View resource.

        :stability: experimental
        '''
        ...


class _IViewRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a View.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_resourceexplorer2.IViewRef"

    @builtins.property
    @jsii.member(jsii_name="viewRef")
    def view_ref(self) -> "ViewReference":
        '''(experimental) A reference to a View resource.

        :stability: experimental
        '''
        return typing.cast("ViewReference", jsii.get(self, "viewRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IViewRef).__jsii_proxy_class__ = lambda : _IViewRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_resourceexplorer2.IndexReference",
    jsii_struct_bases=[],
    name_mapping={"index_arn": "indexArn"},
)
class IndexReference:
    def __init__(self, *, index_arn: builtins.str) -> None:
        '''A reference to a Index resource.

        :param index_arn: The Arn of the Index resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_resourceexplorer2 as interfaces_resourceexplorer2
            
            index_reference = interfaces_resourceexplorer2.IndexReference(
                index_arn="indexArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a1353eb6e2d887bce17fbab1e3e3d4177baffd8356bf99106755d5ecd0bf19a)
            check_type(argname="argument index_arn", value=index_arn, expected_type=type_hints["index_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "index_arn": index_arn,
        }

    @builtins.property
    def index_arn(self) -> builtins.str:
        '''The Arn of the Index resource.'''
        result = self._values.get("index_arn")
        assert result is not None, "Required property 'index_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IndexReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_resourceexplorer2.ViewReference",
    jsii_struct_bases=[],
    name_mapping={"view_arn": "viewArn"},
)
class ViewReference:
    def __init__(self, *, view_arn: builtins.str) -> None:
        '''A reference to a View resource.

        :param view_arn: The ViewArn of the View resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_resourceexplorer2 as interfaces_resourceexplorer2
            
            view_reference = interfaces_resourceexplorer2.ViewReference(
                view_arn="viewArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8553b12cc1b9d847467eaf5575a7d5d4915ade244c2062fb46bebe9d148e22f3)
            check_type(argname="argument view_arn", value=view_arn, expected_type=type_hints["view_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "view_arn": view_arn,
        }

    @builtins.property
    def view_arn(self) -> builtins.str:
        '''The ViewArn of the View resource.'''
        result = self._values.get("view_arn")
        assert result is not None, "Required property 'view_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ViewReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DefaultViewAssociationReference",
    "IDefaultViewAssociationRef",
    "IIndexRef",
    "IViewRef",
    "IndexReference",
    "ViewReference",
]

publication.publish()

def _typecheckingstub__b08810f946f0fb1b570baf7b85f43e0860ef69f9324c1bfc8cfd13ab2dcd64be(
    *,
    associated_aws_principal: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a1353eb6e2d887bce17fbab1e3e3d4177baffd8356bf99106755d5ecd0bf19a(
    *,
    index_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8553b12cc1b9d847467eaf5575a7d5d4915ade244c2062fb46bebe9d148e22f3(
    *,
    view_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDefaultViewAssociationRef, IIndexRef, IViewRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
