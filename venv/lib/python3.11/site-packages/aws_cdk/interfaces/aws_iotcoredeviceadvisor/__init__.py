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
    jsii_type="aws-cdk-lib.interfaces.aws_iotcoredeviceadvisor.ISuiteDefinitionRef"
)
class ISuiteDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SuiteDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="suiteDefinitionRef")
    def suite_definition_ref(self) -> "SuiteDefinitionReference":
        '''(experimental) A reference to a SuiteDefinition resource.

        :stability: experimental
        '''
        ...


class _ISuiteDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SuiteDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotcoredeviceadvisor.ISuiteDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="suiteDefinitionRef")
    def suite_definition_ref(self) -> "SuiteDefinitionReference":
        '''(experimental) A reference to a SuiteDefinition resource.

        :stability: experimental
        '''
        return typing.cast("SuiteDefinitionReference", jsii.get(self, "suiteDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISuiteDefinitionRef).__jsii_proxy_class__ = lambda : _ISuiteDefinitionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotcoredeviceadvisor.SuiteDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "suite_definition_arn": "suiteDefinitionArn",
        "suite_definition_id": "suiteDefinitionId",
    },
)
class SuiteDefinitionReference:
    def __init__(
        self,
        *,
        suite_definition_arn: builtins.str,
        suite_definition_id: builtins.str,
    ) -> None:
        '''A reference to a SuiteDefinition resource.

        :param suite_definition_arn: The ARN of the SuiteDefinition resource.
        :param suite_definition_id: The SuiteDefinitionId of the SuiteDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotcoredeviceadvisor as interfaces_iotcoredeviceadvisor
            
            suite_definition_reference = interfaces_iotcoredeviceadvisor.SuiteDefinitionReference(
                suite_definition_arn="suiteDefinitionArn",
                suite_definition_id="suiteDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac8e6b1353d4f6664c1430b58486ab949bb856c6b254f1ff93640441e3af416f)
            check_type(argname="argument suite_definition_arn", value=suite_definition_arn, expected_type=type_hints["suite_definition_arn"])
            check_type(argname="argument suite_definition_id", value=suite_definition_id, expected_type=type_hints["suite_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "suite_definition_arn": suite_definition_arn,
            "suite_definition_id": suite_definition_id,
        }

    @builtins.property
    def suite_definition_arn(self) -> builtins.str:
        '''The ARN of the SuiteDefinition resource.'''
        result = self._values.get("suite_definition_arn")
        assert result is not None, "Required property 'suite_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def suite_definition_id(self) -> builtins.str:
        '''The SuiteDefinitionId of the SuiteDefinition resource.'''
        result = self._values.get("suite_definition_id")
        assert result is not None, "Required property 'suite_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SuiteDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ISuiteDefinitionRef",
    "SuiteDefinitionReference",
]

publication.publish()

def _typecheckingstub__ac8e6b1353d4f6664c1430b58486ab949bb856c6b254f1ff93640441e3af416f(
    *,
    suite_definition_arn: builtins.str,
    suite_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ISuiteDefinitionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
