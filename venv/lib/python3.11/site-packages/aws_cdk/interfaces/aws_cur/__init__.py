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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cur.IReportDefinitionRef")
class IReportDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReportDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="reportDefinitionRef")
    def report_definition_ref(self) -> "ReportDefinitionReference":
        '''(experimental) A reference to a ReportDefinition resource.

        :stability: experimental
        '''
        ...


class _IReportDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReportDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cur.IReportDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="reportDefinitionRef")
    def report_definition_ref(self) -> "ReportDefinitionReference":
        '''(experimental) A reference to a ReportDefinition resource.

        :stability: experimental
        '''
        return typing.cast("ReportDefinitionReference", jsii.get(self, "reportDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReportDefinitionRef).__jsii_proxy_class__ = lambda : _IReportDefinitionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cur.ReportDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"report_name": "reportName"},
)
class ReportDefinitionReference:
    def __init__(self, *, report_name: builtins.str) -> None:
        '''A reference to a ReportDefinition resource.

        :param report_name: The ReportName of the ReportDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cur as interfaces_cur
            
            report_definition_reference = interfaces_cur.ReportDefinitionReference(
                report_name="reportName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5479e749f145637b989c2bf3c9669c12a107e68b04a8bcac6fc35e7a472367cc)
            check_type(argname="argument report_name", value=report_name, expected_type=type_hints["report_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "report_name": report_name,
        }

    @builtins.property
    def report_name(self) -> builtins.str:
        '''The ReportName of the ReportDefinition resource.'''
        result = self._values.get("report_name")
        assert result is not None, "Required property 'report_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReportDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IReportDefinitionRef",
    "ReportDefinitionReference",
]

publication.publish()

def _typecheckingstub__5479e749f145637b989c2bf3c9669c12a107e68b04a8bcac6fc35e7a472367cc(
    *,
    report_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IReportDefinitionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
