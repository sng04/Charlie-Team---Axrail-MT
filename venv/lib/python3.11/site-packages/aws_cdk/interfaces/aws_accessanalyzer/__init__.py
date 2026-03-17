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
    jsii_type="aws-cdk-lib.interfaces.aws_accessanalyzer.AnalyzerReference",
    jsii_struct_bases=[],
    name_mapping={"analyzer_arn": "analyzerArn"},
)
class AnalyzerReference:
    def __init__(self, *, analyzer_arn: builtins.str) -> None:
        '''A reference to a Analyzer resource.

        :param analyzer_arn: The Arn of the Analyzer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_accessanalyzer as interfaces_accessanalyzer
            
            analyzer_reference = interfaces_accessanalyzer.AnalyzerReference(
                analyzer_arn="analyzerArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4d375974cd2ef13d3347c0db5ce73a696e350281dee5af93d3a748a4376541c)
            check_type(argname="argument analyzer_arn", value=analyzer_arn, expected_type=type_hints["analyzer_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "analyzer_arn": analyzer_arn,
        }

    @builtins.property
    def analyzer_arn(self) -> builtins.str:
        '''The Arn of the Analyzer resource.'''
        result = self._values.get("analyzer_arn")
        assert result is not None, "Required property 'analyzer_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalyzerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_accessanalyzer.IAnalyzerRef")
class IAnalyzerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Analyzer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="analyzerRef")
    def analyzer_ref(self) -> "AnalyzerReference":
        '''(experimental) A reference to a Analyzer resource.

        :stability: experimental
        '''
        ...


class _IAnalyzerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Analyzer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_accessanalyzer.IAnalyzerRef"

    @builtins.property
    @jsii.member(jsii_name="analyzerRef")
    def analyzer_ref(self) -> "AnalyzerReference":
        '''(experimental) A reference to a Analyzer resource.

        :stability: experimental
        '''
        return typing.cast("AnalyzerReference", jsii.get(self, "analyzerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnalyzerRef).__jsii_proxy_class__ = lambda : _IAnalyzerRefProxy


__all__ = [
    "AnalyzerReference",
    "IAnalyzerRef",
]

publication.publish()

def _typecheckingstub__d4d375974cd2ef13d3347c0db5ce73a696e350281dee5af93d3a748a4376541c(
    *,
    analyzer_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAnalyzerRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
