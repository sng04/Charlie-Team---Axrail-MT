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
    jsii_type="aws-cdk-lib.interfaces.aws_resiliencehub.AppReference",
    jsii_struct_bases=[],
    name_mapping={"app_arn": "appArn"},
)
class AppReference:
    def __init__(self, *, app_arn: builtins.str) -> None:
        '''A reference to a App resource.

        :param app_arn: The AppArn of the App resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_resiliencehub as interfaces_resiliencehub
            
            app_reference = interfaces_resiliencehub.AppReference(
                app_arn="appArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cb61fa3c20dcbe83a92f4ce83d1c1e8ab107f3593a79fcdd68c7997d55cbac7)
            check_type(argname="argument app_arn", value=app_arn, expected_type=type_hints["app_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_arn": app_arn,
        }

    @builtins.property
    def app_arn(self) -> builtins.str:
        '''The AppArn of the App resource.'''
        result = self._values.get("app_arn")
        assert result is not None, "Required property 'app_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_resiliencehub.IAppRef")
class IAppRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        ...


class _IAppRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_resiliencehub.IAppRef"

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        return typing.cast("AppReference", jsii.get(self, "appRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppRef).__jsii_proxy_class__ = lambda : _IAppRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_resiliencehub.IResiliencyPolicyRef"
)
class IResiliencyPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResiliencyPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resiliencyPolicyRef")
    def resiliency_policy_ref(self) -> "ResiliencyPolicyReference":
        '''(experimental) A reference to a ResiliencyPolicy resource.

        :stability: experimental
        '''
        ...


class _IResiliencyPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResiliencyPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_resiliencehub.IResiliencyPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resiliencyPolicyRef")
    def resiliency_policy_ref(self) -> "ResiliencyPolicyReference":
        '''(experimental) A reference to a ResiliencyPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResiliencyPolicyReference", jsii.get(self, "resiliencyPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResiliencyPolicyRef).__jsii_proxy_class__ = lambda : _IResiliencyPolicyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_resiliencehub.ResiliencyPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_arn": "policyArn"},
)
class ResiliencyPolicyReference:
    def __init__(self, *, policy_arn: builtins.str) -> None:
        '''A reference to a ResiliencyPolicy resource.

        :param policy_arn: The PolicyArn of the ResiliencyPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_resiliencehub as interfaces_resiliencehub
            
            resiliency_policy_reference = interfaces_resiliencehub.ResiliencyPolicyReference(
                policy_arn="policyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__858c1cc5b4c4e16bc1082dfc336cca315132234ba3d88ac972d29352636242ea)
            check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_arn": policy_arn,
        }

    @builtins.property
    def policy_arn(self) -> builtins.str:
        '''The PolicyArn of the ResiliencyPolicy resource.'''
        result = self._values.get("policy_arn")
        assert result is not None, "Required property 'policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResiliencyPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppReference",
    "IAppRef",
    "IResiliencyPolicyRef",
    "ResiliencyPolicyReference",
]

publication.publish()

def _typecheckingstub__3cb61fa3c20dcbe83a92f4ce83d1c1e8ab107f3593a79fcdd68c7997d55cbac7(
    *,
    app_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__858c1cc5b4c4e16bc1082dfc336cca315132234ba3d88ac972d29352636242ea(
    *,
    policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAppRef, IResiliencyPolicyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
