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
    jsii_type="aws-cdk-lib.interfaces.aws_bcmdataexports.ExportReference",
    jsii_struct_bases=[],
    name_mapping={"export_arn": "exportArn"},
)
class ExportReference:
    def __init__(self, *, export_arn: builtins.str) -> None:
        '''A reference to a Export resource.

        :param export_arn: The ExportArn of the Export resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bcmdataexports as interfaces_bcmdataexports
            
            export_reference = interfaces_bcmdataexports.ExportReference(
                export_arn="exportArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ea2d494cfbedb7e7bbc05c48e544f2907a445229bf8b40001a183b8de9d1170)
            check_type(argname="argument export_arn", value=export_arn, expected_type=type_hints["export_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "export_arn": export_arn,
        }

    @builtins.property
    def export_arn(self) -> builtins.str:
        '''The ExportArn of the Export resource.'''
        result = self._values.get("export_arn")
        assert result is not None, "Required property 'export_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExportReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bcmdataexports.IExportRef")
class IExportRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Export.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="exportRef")
    def export_ref(self) -> "ExportReference":
        '''(experimental) A reference to a Export resource.

        :stability: experimental
        '''
        ...


class _IExportRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Export.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bcmdataexports.IExportRef"

    @builtins.property
    @jsii.member(jsii_name="exportRef")
    def export_ref(self) -> "ExportReference":
        '''(experimental) A reference to a Export resource.

        :stability: experimental
        '''
        return typing.cast("ExportReference", jsii.get(self, "exportRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExportRef).__jsii_proxy_class__ = lambda : _IExportRefProxy


__all__ = [
    "ExportReference",
    "IExportRef",
]

publication.publish()

def _typecheckingstub__3ea2d494cfbedb7e7bbc05c48e544f2907a445229bf8b40001a183b8de9d1170(
    *,
    export_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IExportRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
