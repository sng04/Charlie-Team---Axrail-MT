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
    jsii_type="aws-cdk-lib.interfaces.aws_proton.EnvironmentAccountConnectionReference",
    jsii_struct_bases=[],
    name_mapping={
        "environment_account_connection_arn": "environmentAccountConnectionArn",
    },
)
class EnvironmentAccountConnectionReference:
    def __init__(self, *, environment_account_connection_arn: builtins.str) -> None:
        '''A reference to a EnvironmentAccountConnection resource.

        :param environment_account_connection_arn: The Arn of the EnvironmentAccountConnection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_proton as interfaces_proton
            
            environment_account_connection_reference = interfaces_proton.EnvironmentAccountConnectionReference(
                environment_account_connection_arn="environmentAccountConnectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f44078276965ae3e1d8d189a402c9dd3fd0304733c78c66b8ab98329803a1c)
            check_type(argname="argument environment_account_connection_arn", value=environment_account_connection_arn, expected_type=type_hints["environment_account_connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment_account_connection_arn": environment_account_connection_arn,
        }

    @builtins.property
    def environment_account_connection_arn(self) -> builtins.str:
        '''The Arn of the EnvironmentAccountConnection resource.'''
        result = self._values.get("environment_account_connection_arn")
        assert result is not None, "Required property 'environment_account_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentAccountConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_proton.EnvironmentTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"environment_template_arn": "environmentTemplateArn"},
)
class EnvironmentTemplateReference:
    def __init__(self, *, environment_template_arn: builtins.str) -> None:
        '''A reference to a EnvironmentTemplate resource.

        :param environment_template_arn: The Arn of the EnvironmentTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_proton as interfaces_proton
            
            environment_template_reference = interfaces_proton.EnvironmentTemplateReference(
                environment_template_arn="environmentTemplateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__499f57f059835807064b105e85f93e531d93b728d39c8bc512eb6d78ec398d64)
            check_type(argname="argument environment_template_arn", value=environment_template_arn, expected_type=type_hints["environment_template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment_template_arn": environment_template_arn,
        }

    @builtins.property
    def environment_template_arn(self) -> builtins.str:
        '''The Arn of the EnvironmentTemplate resource.'''
        result = self._values.get("environment_template_arn")
        assert result is not None, "Required property 'environment_template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_proton.IEnvironmentAccountConnectionRef"
)
class IEnvironmentAccountConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentAccountConnection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentAccountConnectionRef")
    def environment_account_connection_ref(
        self,
    ) -> "EnvironmentAccountConnectionReference":
        '''(experimental) A reference to a EnvironmentAccountConnection resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentAccountConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentAccountConnection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_proton.IEnvironmentAccountConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="environmentAccountConnectionRef")
    def environment_account_connection_ref(
        self,
    ) -> "EnvironmentAccountConnectionReference":
        '''(experimental) A reference to a EnvironmentAccountConnection resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentAccountConnectionReference", jsii.get(self, "environmentAccountConnectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentAccountConnectionRef).__jsii_proxy_class__ = lambda : _IEnvironmentAccountConnectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_proton.IEnvironmentTemplateRef")
class IEnvironmentTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentTemplateRef")
    def environment_template_ref(self) -> "EnvironmentTemplateReference":
        '''(experimental) A reference to a EnvironmentTemplate resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_proton.IEnvironmentTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="environmentTemplateRef")
    def environment_template_ref(self) -> "EnvironmentTemplateReference":
        '''(experimental) A reference to a EnvironmentTemplate resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentTemplateReference", jsii.get(self, "environmentTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentTemplateRef).__jsii_proxy_class__ = lambda : _IEnvironmentTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_proton.IServiceTemplateRef")
class IServiceTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceTemplateRef")
    def service_template_ref(self) -> "ServiceTemplateReference":
        '''(experimental) A reference to a ServiceTemplate resource.

        :stability: experimental
        '''
        ...


class _IServiceTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_proton.IServiceTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="serviceTemplateRef")
    def service_template_ref(self) -> "ServiceTemplateReference":
        '''(experimental) A reference to a ServiceTemplate resource.

        :stability: experimental
        '''
        return typing.cast("ServiceTemplateReference", jsii.get(self, "serviceTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceTemplateRef).__jsii_proxy_class__ = lambda : _IServiceTemplateRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_proton.ServiceTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"service_template_arn": "serviceTemplateArn"},
)
class ServiceTemplateReference:
    def __init__(self, *, service_template_arn: builtins.str) -> None:
        '''A reference to a ServiceTemplate resource.

        :param service_template_arn: The Arn of the ServiceTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_proton as interfaces_proton
            
            service_template_reference = interfaces_proton.ServiceTemplateReference(
                service_template_arn="serviceTemplateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__061482c5b153f4054896b834efe17e8014b87a5780786d3d28b2fb1b9a9d0d5d)
            check_type(argname="argument service_template_arn", value=service_template_arn, expected_type=type_hints["service_template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_template_arn": service_template_arn,
        }

    @builtins.property
    def service_template_arn(self) -> builtins.str:
        '''The Arn of the ServiceTemplate resource.'''
        result = self._values.get("service_template_arn")
        assert result is not None, "Required property 'service_template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EnvironmentAccountConnectionReference",
    "EnvironmentTemplateReference",
    "IEnvironmentAccountConnectionRef",
    "IEnvironmentTemplateRef",
    "IServiceTemplateRef",
    "ServiceTemplateReference",
]

publication.publish()

def _typecheckingstub__f1f44078276965ae3e1d8d189a402c9dd3fd0304733c78c66b8ab98329803a1c(
    *,
    environment_account_connection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499f57f059835807064b105e85f93e531d93b728d39c8bc512eb6d78ec398d64(
    *,
    environment_template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__061482c5b153f4054896b834efe17e8014b87a5780786d3d28b2fb1b9a9d0d5d(
    *,
    service_template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IEnvironmentAccountConnectionRef, IEnvironmentTemplateRef, IServiceTemplateRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
