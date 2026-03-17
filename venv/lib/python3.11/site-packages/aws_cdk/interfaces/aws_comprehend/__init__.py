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
    jsii_type="aws-cdk-lib.interfaces.aws_comprehend.DocumentClassifierReference",
    jsii_struct_bases=[],
    name_mapping={"document_classifier_arn": "documentClassifierArn"},
)
class DocumentClassifierReference:
    def __init__(self, *, document_classifier_arn: builtins.str) -> None:
        '''A reference to a DocumentClassifier resource.

        :param document_classifier_arn: The Arn of the DocumentClassifier resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_comprehend as interfaces_comprehend
            
            document_classifier_reference = interfaces_comprehend.DocumentClassifierReference(
                document_classifier_arn="documentClassifierArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9fa934fd61e384a4f96df7d216e90fb61ab7b36d10b061f5c8f65018a486c69)
            check_type(argname="argument document_classifier_arn", value=document_classifier_arn, expected_type=type_hints["document_classifier_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "document_classifier_arn": document_classifier_arn,
        }

    @builtins.property
    def document_classifier_arn(self) -> builtins.str:
        '''The Arn of the DocumentClassifier resource.'''
        result = self._values.get("document_classifier_arn")
        assert result is not None, "Required property 'document_classifier_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DocumentClassifierReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_comprehend.FlywheelReference",
    jsii_struct_bases=[],
    name_mapping={"flywheel_arn": "flywheelArn"},
)
class FlywheelReference:
    def __init__(self, *, flywheel_arn: builtins.str) -> None:
        '''A reference to a Flywheel resource.

        :param flywheel_arn: The Arn of the Flywheel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_comprehend as interfaces_comprehend
            
            flywheel_reference = interfaces_comprehend.FlywheelReference(
                flywheel_arn="flywheelArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__324b0a4251a268a7d0e2108be6b77682a5cf7efd9bb727770aa1bb1d59102a8f)
            check_type(argname="argument flywheel_arn", value=flywheel_arn, expected_type=type_hints["flywheel_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flywheel_arn": flywheel_arn,
        }

    @builtins.property
    def flywheel_arn(self) -> builtins.str:
        '''The Arn of the Flywheel resource.'''
        result = self._values.get("flywheel_arn")
        assert result is not None, "Required property 'flywheel_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlywheelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_comprehend.IDocumentClassifierRef"
)
class IDocumentClassifierRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentClassifier.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="documentClassifierRef")
    def document_classifier_ref(self) -> "DocumentClassifierReference":
        '''(experimental) A reference to a DocumentClassifier resource.

        :stability: experimental
        '''
        ...


class _IDocumentClassifierRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DocumentClassifier.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_comprehend.IDocumentClassifierRef"

    @builtins.property
    @jsii.member(jsii_name="documentClassifierRef")
    def document_classifier_ref(self) -> "DocumentClassifierReference":
        '''(experimental) A reference to a DocumentClassifier resource.

        :stability: experimental
        '''
        return typing.cast("DocumentClassifierReference", jsii.get(self, "documentClassifierRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDocumentClassifierRef).__jsii_proxy_class__ = lambda : _IDocumentClassifierRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_comprehend.IFlywheelRef")
class IFlywheelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Flywheel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flywheelRef")
    def flywheel_ref(self) -> "FlywheelReference":
        '''(experimental) A reference to a Flywheel resource.

        :stability: experimental
        '''
        ...


class _IFlywheelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Flywheel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_comprehend.IFlywheelRef"

    @builtins.property
    @jsii.member(jsii_name="flywheelRef")
    def flywheel_ref(self) -> "FlywheelReference":
        '''(experimental) A reference to a Flywheel resource.

        :stability: experimental
        '''
        return typing.cast("FlywheelReference", jsii.get(self, "flywheelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlywheelRef).__jsii_proxy_class__ = lambda : _IFlywheelRefProxy


__all__ = [
    "DocumentClassifierReference",
    "FlywheelReference",
    "IDocumentClassifierRef",
    "IFlywheelRef",
]

publication.publish()

def _typecheckingstub__e9fa934fd61e384a4f96df7d216e90fb61ab7b36d10b061f5c8f65018a486c69(
    *,
    document_classifier_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324b0a4251a268a7d0e2108be6b77682a5cf7efd9bb727770aa1bb1d59102a8f(
    *,
    flywheel_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDocumentClassifierRef, IFlywheelRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
