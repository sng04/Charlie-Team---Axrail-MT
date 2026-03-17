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
    jsii_type="aws-cdk-lib.interfaces.aws_directoryservice.IMicrosoftADRef"
)
class IMicrosoftADRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MicrosoftAD.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="microsoftAdRef")
    def microsoft_ad_ref(self) -> "MicrosoftADReference":
        '''(experimental) A reference to a MicrosoftAD resource.

        :stability: experimental
        '''
        ...


class _IMicrosoftADRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MicrosoftAD.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_directoryservice.IMicrosoftADRef"

    @builtins.property
    @jsii.member(jsii_name="microsoftAdRef")
    def microsoft_ad_ref(self) -> "MicrosoftADReference":
        '''(experimental) A reference to a MicrosoftAD resource.

        :stability: experimental
        '''
        return typing.cast("MicrosoftADReference", jsii.get(self, "microsoftAdRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMicrosoftADRef).__jsii_proxy_class__ = lambda : _IMicrosoftADRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_directoryservice.ISimpleADRef")
class ISimpleADRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SimpleAD.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="simpleAdRef")
    def simple_ad_ref(self) -> "SimpleADReference":
        '''(experimental) A reference to a SimpleAD resource.

        :stability: experimental
        '''
        ...


class _ISimpleADRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SimpleAD.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_directoryservice.ISimpleADRef"

    @builtins.property
    @jsii.member(jsii_name="simpleAdRef")
    def simple_ad_ref(self) -> "SimpleADReference":
        '''(experimental) A reference to a SimpleAD resource.

        :stability: experimental
        '''
        return typing.cast("SimpleADReference", jsii.get(self, "simpleAdRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISimpleADRef).__jsii_proxy_class__ = lambda : _ISimpleADRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_directoryservice.MicrosoftADReference",
    jsii_struct_bases=[],
    name_mapping={"microsoft_ad_id": "microsoftAdId"},
)
class MicrosoftADReference:
    def __init__(self, *, microsoft_ad_id: builtins.str) -> None:
        '''A reference to a MicrosoftAD resource.

        :param microsoft_ad_id: The Id of the MicrosoftAD resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_directoryservice as interfaces_directoryservice
            
            microsoft_aDReference = interfaces_directoryservice.MicrosoftADReference(
                microsoft_ad_id="microsoftAdId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e89a67e404d7f77c2063c54e192002b94a4b20d770557217c128057a6746b79a)
            check_type(argname="argument microsoft_ad_id", value=microsoft_ad_id, expected_type=type_hints["microsoft_ad_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "microsoft_ad_id": microsoft_ad_id,
        }

    @builtins.property
    def microsoft_ad_id(self) -> builtins.str:
        '''The Id of the MicrosoftAD resource.'''
        result = self._values.get("microsoft_ad_id")
        assert result is not None, "Required property 'microsoft_ad_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MicrosoftADReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_directoryservice.SimpleADReference",
    jsii_struct_bases=[],
    name_mapping={"directory_id": "directoryId"},
)
class SimpleADReference:
    def __init__(self, *, directory_id: builtins.str) -> None:
        '''A reference to a SimpleAD resource.

        :param directory_id: The DirectoryId of the SimpleAD resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_directoryservice as interfaces_directoryservice
            
            simple_aDReference = interfaces_directoryservice.SimpleADReference(
                directory_id="directoryId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed7c4f6b0a89bc57c8092879a5a4c884781c85adac2c56af06ffe47903f7d596)
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory_id": directory_id,
        }

    @builtins.property
    def directory_id(self) -> builtins.str:
        '''The DirectoryId of the SimpleAD resource.'''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SimpleADReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IMicrosoftADRef",
    "ISimpleADRef",
    "MicrosoftADReference",
    "SimpleADReference",
]

publication.publish()

def _typecheckingstub__e89a67e404d7f77c2063c54e192002b94a4b20d770557217c128057a6746b79a(
    *,
    microsoft_ad_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed7c4f6b0a89bc57c8092879a5a4c884781c85adac2c56af06ffe47903f7d596(
    *,
    directory_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IMicrosoftADRef, ISimpleADRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
