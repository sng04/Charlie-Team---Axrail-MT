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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_invoicing.IInvoiceUnitRef")
class IInvoiceUnitRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InvoiceUnit.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="invoiceUnitRef")
    def invoice_unit_ref(self) -> "InvoiceUnitReference":
        '''(experimental) A reference to a InvoiceUnit resource.

        :stability: experimental
        '''
        ...


class _IInvoiceUnitRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InvoiceUnit.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_invoicing.IInvoiceUnitRef"

    @builtins.property
    @jsii.member(jsii_name="invoiceUnitRef")
    def invoice_unit_ref(self) -> "InvoiceUnitReference":
        '''(experimental) A reference to a InvoiceUnit resource.

        :stability: experimental
        '''
        return typing.cast("InvoiceUnitReference", jsii.get(self, "invoiceUnitRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInvoiceUnitRef).__jsii_proxy_class__ = lambda : _IInvoiceUnitRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_invoicing.InvoiceUnitReference",
    jsii_struct_bases=[],
    name_mapping={"invoice_unit_arn": "invoiceUnitArn"},
)
class InvoiceUnitReference:
    def __init__(self, *, invoice_unit_arn: builtins.str) -> None:
        '''A reference to a InvoiceUnit resource.

        :param invoice_unit_arn: The InvoiceUnitArn of the InvoiceUnit resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_invoicing as interfaces_invoicing
            
            invoice_unit_reference = interfaces_invoicing.InvoiceUnitReference(
                invoice_unit_arn="invoiceUnitArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e1bc14d8a543b4d8a37813d74724155f93908a344cc67210c22eb17864474bc)
            check_type(argname="argument invoice_unit_arn", value=invoice_unit_arn, expected_type=type_hints["invoice_unit_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "invoice_unit_arn": invoice_unit_arn,
        }

    @builtins.property
    def invoice_unit_arn(self) -> builtins.str:
        '''The InvoiceUnitArn of the InvoiceUnit resource.'''
        result = self._values.get("invoice_unit_arn")
        assert result is not None, "Required property 'invoice_unit_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InvoiceUnitReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IInvoiceUnitRef",
    "InvoiceUnitReference",
]

publication.publish()

def _typecheckingstub__9e1bc14d8a543b4d8a37813d74724155f93908a344cc67210c22eb17864474bc(
    *,
    invoice_unit_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IInvoiceUnitRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
