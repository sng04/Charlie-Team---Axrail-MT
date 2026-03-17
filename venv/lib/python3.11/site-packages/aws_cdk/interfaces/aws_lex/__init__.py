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
    jsii_type="aws-cdk-lib.interfaces.aws_lex.BotAliasReference",
    jsii_struct_bases=[],
    name_mapping={
        "bot_alias_arn": "botAliasArn",
        "bot_alias_id": "botAliasId",
        "bot_id": "botId",
    },
)
class BotAliasReference:
    def __init__(
        self,
        *,
        bot_alias_arn: builtins.str,
        bot_alias_id: builtins.str,
        bot_id: builtins.str,
    ) -> None:
        '''A reference to a BotAlias resource.

        :param bot_alias_arn: The ARN of the BotAlias resource.
        :param bot_alias_id: The BotAliasId of the BotAlias resource.
        :param bot_id: The BotId of the BotAlias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lex as interfaces_lex
            
            bot_alias_reference = interfaces_lex.BotAliasReference(
                bot_alias_arn="botAliasArn",
                bot_alias_id="botAliasId",
                bot_id="botId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da0b54ad485285304e48bef3ec6372c1dfecfd8d84af5c6a4f2d8b56fc0b8fe)
            check_type(argname="argument bot_alias_arn", value=bot_alias_arn, expected_type=type_hints["bot_alias_arn"])
            check_type(argname="argument bot_alias_id", value=bot_alias_id, expected_type=type_hints["bot_alias_id"])
            check_type(argname="argument bot_id", value=bot_id, expected_type=type_hints["bot_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bot_alias_arn": bot_alias_arn,
            "bot_alias_id": bot_alias_id,
            "bot_id": bot_id,
        }

    @builtins.property
    def bot_alias_arn(self) -> builtins.str:
        '''The ARN of the BotAlias resource.'''
        result = self._values.get("bot_alias_arn")
        assert result is not None, "Required property 'bot_alias_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bot_alias_id(self) -> builtins.str:
        '''The BotAliasId of the BotAlias resource.'''
        result = self._values.get("bot_alias_id")
        assert result is not None, "Required property 'bot_alias_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bot_id(self) -> builtins.str:
        '''The BotId of the BotAlias resource.'''
        result = self._values.get("bot_id")
        assert result is not None, "Required property 'bot_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BotAliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lex.BotReference",
    jsii_struct_bases=[],
    name_mapping={"bot_arn": "botArn", "bot_id": "botId"},
)
class BotReference:
    def __init__(self, *, bot_arn: builtins.str, bot_id: builtins.str) -> None:
        '''A reference to a Bot resource.

        :param bot_arn: The ARN of the Bot resource.
        :param bot_id: The Id of the Bot resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lex as interfaces_lex
            
            bot_reference = interfaces_lex.BotReference(
                bot_arn="botArn",
                bot_id="botId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5282e11e9199ed0f9be5be574675194a595b2077a284ee6b24496d3e2a5002f0)
            check_type(argname="argument bot_arn", value=bot_arn, expected_type=type_hints["bot_arn"])
            check_type(argname="argument bot_id", value=bot_id, expected_type=type_hints["bot_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bot_arn": bot_arn,
            "bot_id": bot_id,
        }

    @builtins.property
    def bot_arn(self) -> builtins.str:
        '''The ARN of the Bot resource.'''
        result = self._values.get("bot_arn")
        assert result is not None, "Required property 'bot_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bot_id(self) -> builtins.str:
        '''The Id of the Bot resource.'''
        result = self._values.get("bot_id")
        assert result is not None, "Required property 'bot_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BotReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lex.BotVersionReference",
    jsii_struct_bases=[],
    name_mapping={"bot_id": "botId", "bot_version": "botVersion"},
)
class BotVersionReference:
    def __init__(self, *, bot_id: builtins.str, bot_version: builtins.str) -> None:
        '''A reference to a BotVersion resource.

        :param bot_id: The BotId of the BotVersion resource.
        :param bot_version: The BotVersion of the BotVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lex as interfaces_lex
            
            bot_version_reference = interfaces_lex.BotVersionReference(
                bot_id="botId",
                bot_version="botVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf71d040e6c79ce911d970fafd1623f1fad9a813be670b74ecf8da62fba7280)
            check_type(argname="argument bot_id", value=bot_id, expected_type=type_hints["bot_id"])
            check_type(argname="argument bot_version", value=bot_version, expected_type=type_hints["bot_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bot_id": bot_id,
            "bot_version": bot_version,
        }

    @builtins.property
    def bot_id(self) -> builtins.str:
        '''The BotId of the BotVersion resource.'''
        result = self._values.get("bot_id")
        assert result is not None, "Required property 'bot_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bot_version(self) -> builtins.str:
        '''The BotVersion of the BotVersion resource.'''
        result = self._values.get("bot_version")
        assert result is not None, "Required property 'bot_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BotVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lex.IBotAliasRef")
class IBotAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BotAlias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="botAliasRef")
    def bot_alias_ref(self) -> "BotAliasReference":
        '''(experimental) A reference to a BotAlias resource.

        :stability: experimental
        '''
        ...


class _IBotAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BotAlias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lex.IBotAliasRef"

    @builtins.property
    @jsii.member(jsii_name="botAliasRef")
    def bot_alias_ref(self) -> "BotAliasReference":
        '''(experimental) A reference to a BotAlias resource.

        :stability: experimental
        '''
        return typing.cast("BotAliasReference", jsii.get(self, "botAliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBotAliasRef).__jsii_proxy_class__ = lambda : _IBotAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lex.IBotRef")
class IBotRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Bot.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="botRef")
    def bot_ref(self) -> "BotReference":
        '''(experimental) A reference to a Bot resource.

        :stability: experimental
        '''
        ...


class _IBotRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Bot.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lex.IBotRef"

    @builtins.property
    @jsii.member(jsii_name="botRef")
    def bot_ref(self) -> "BotReference":
        '''(experimental) A reference to a Bot resource.

        :stability: experimental
        '''
        return typing.cast("BotReference", jsii.get(self, "botRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBotRef).__jsii_proxy_class__ = lambda : _IBotRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lex.IBotVersionRef")
class IBotVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BotVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="botVersionRef")
    def bot_version_ref(self) -> "BotVersionReference":
        '''(experimental) A reference to a BotVersion resource.

        :stability: experimental
        '''
        ...


class _IBotVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BotVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lex.IBotVersionRef"

    @builtins.property
    @jsii.member(jsii_name="botVersionRef")
    def bot_version_ref(self) -> "BotVersionReference":
        '''(experimental) A reference to a BotVersion resource.

        :stability: experimental
        '''
        return typing.cast("BotVersionReference", jsii.get(self, "botVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBotVersionRef).__jsii_proxy_class__ = lambda : _IBotVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lex.IResourcePolicyRef")
class IResourcePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        ...


class _IResourcePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lex.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lex.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"resource_policy_id": "resourcePolicyId"},
)
class ResourcePolicyReference:
    def __init__(self, *, resource_policy_id: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param resource_policy_id: The Id of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lex as interfaces_lex
            
            resource_policy_reference = interfaces_lex.ResourcePolicyReference(
                resource_policy_id="resourcePolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bff46812e15d2537c9c276eefdad3ebc99c271e88aafcdf42f6aa95711e4a1d)
            check_type(argname="argument resource_policy_id", value=resource_policy_id, expected_type=type_hints["resource_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_policy_id": resource_policy_id,
        }

    @builtins.property
    def resource_policy_id(self) -> builtins.str:
        '''The Id of the ResourcePolicy resource.'''
        result = self._values.get("resource_policy_id")
        assert result is not None, "Required property 'resource_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BotAliasReference",
    "BotReference",
    "BotVersionReference",
    "IBotAliasRef",
    "IBotRef",
    "IBotVersionRef",
    "IResourcePolicyRef",
    "ResourcePolicyReference",
]

publication.publish()

def _typecheckingstub__1da0b54ad485285304e48bef3ec6372c1dfecfd8d84af5c6a4f2d8b56fc0b8fe(
    *,
    bot_alias_arn: builtins.str,
    bot_alias_id: builtins.str,
    bot_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5282e11e9199ed0f9be5be574675194a595b2077a284ee6b24496d3e2a5002f0(
    *,
    bot_arn: builtins.str,
    bot_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf71d040e6c79ce911d970fafd1623f1fad9a813be670b74ecf8da62fba7280(
    *,
    bot_id: builtins.str,
    bot_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bff46812e15d2537c9c276eefdad3ebc99c271e88aafcdf42f6aa95711e4a1d(
    *,
    resource_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBotAliasRef, IBotRef, IBotVersionRef, IResourcePolicyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
