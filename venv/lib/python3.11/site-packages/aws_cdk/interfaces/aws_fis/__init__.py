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
    jsii_type="aws-cdk-lib.interfaces.aws_fis.ExperimentTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"experiment_template_id": "experimentTemplateId"},
)
class ExperimentTemplateReference:
    def __init__(self, *, experiment_template_id: builtins.str) -> None:
        '''A reference to a ExperimentTemplate resource.

        :param experiment_template_id: The Id of the ExperimentTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fis as interfaces_fis
            
            experiment_template_reference = interfaces_fis.ExperimentTemplateReference(
                experiment_template_id="experimentTemplateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__482182b8d8fc0401579869c38f6085fb823e0e006b2b6f794c30a68f6d3fee35)
            check_type(argname="argument experiment_template_id", value=experiment_template_id, expected_type=type_hints["experiment_template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "experiment_template_id": experiment_template_id,
        }

    @builtins.property
    def experiment_template_id(self) -> builtins.str:
        '''The Id of the ExperimentTemplate resource.'''
        result = self._values.get("experiment_template_id")
        assert result is not None, "Required property 'experiment_template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExperimentTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_fis.IExperimentTemplateRef")
class IExperimentTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ExperimentTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="experimentTemplateRef")
    def experiment_template_ref(self) -> "ExperimentTemplateReference":
        '''(experimental) A reference to a ExperimentTemplate resource.

        :stability: experimental
        '''
        ...


class _IExperimentTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ExperimentTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fis.IExperimentTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="experimentTemplateRef")
    def experiment_template_ref(self) -> "ExperimentTemplateReference":
        '''(experimental) A reference to a ExperimentTemplate resource.

        :stability: experimental
        '''
        return typing.cast("ExperimentTemplateReference", jsii.get(self, "experimentTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExperimentTemplateRef).__jsii_proxy_class__ = lambda : _IExperimentTemplateRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_fis.ITargetAccountConfigurationRef"
)
class ITargetAccountConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TargetAccountConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="targetAccountConfigurationRef")
    def target_account_configuration_ref(self) -> "TargetAccountConfigurationReference":
        '''(experimental) A reference to a TargetAccountConfiguration resource.

        :stability: experimental
        '''
        ...


class _ITargetAccountConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TargetAccountConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_fis.ITargetAccountConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="targetAccountConfigurationRef")
    def target_account_configuration_ref(self) -> "TargetAccountConfigurationReference":
        '''(experimental) A reference to a TargetAccountConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("TargetAccountConfigurationReference", jsii.get(self, "targetAccountConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITargetAccountConfigurationRef).__jsii_proxy_class__ = lambda : _ITargetAccountConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_fis.TargetAccountConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "experiment_template_id": "experimentTemplateId",
    },
)
class TargetAccountConfigurationReference:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        experiment_template_id: builtins.str,
    ) -> None:
        '''A reference to a TargetAccountConfiguration resource.

        :param account_id: The AccountId of the TargetAccountConfiguration resource.
        :param experiment_template_id: The ExperimentTemplateId of the TargetAccountConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_fis as interfaces_fis
            
            target_account_configuration_reference = interfaces_fis.TargetAccountConfigurationReference(
                account_id="accountId",
                experiment_template_id="experimentTemplateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05b8063efc01ff6825227e909f83dd27b05413f12fa9122fa3fc71de0f9c2cfd)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument experiment_template_id", value=experiment_template_id, expected_type=type_hints["experiment_template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "experiment_template_id": experiment_template_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the TargetAccountConfiguration resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def experiment_template_id(self) -> builtins.str:
        '''The ExperimentTemplateId of the TargetAccountConfiguration resource.'''
        result = self._values.get("experiment_template_id")
        assert result is not None, "Required property 'experiment_template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetAccountConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ExperimentTemplateReference",
    "IExperimentTemplateRef",
    "ITargetAccountConfigurationRef",
    "TargetAccountConfigurationReference",
]

publication.publish()

def _typecheckingstub__482182b8d8fc0401579869c38f6085fb823e0e006b2b6f794c30a68f6d3fee35(
    *,
    experiment_template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b8063efc01ff6825227e909f83dd27b05413f12fa9122fa3fc71de0f9c2cfd(
    *,
    account_id: builtins.str,
    experiment_template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IExperimentTemplateRef, ITargetAccountConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
