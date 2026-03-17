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
    jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.ConfigurationSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_arn": "configurationSetArn",
        "configuration_set_name": "configurationSetName",
    },
)
class ConfigurationSetReference:
    def __init__(
        self,
        *,
        configuration_set_arn: builtins.str,
        configuration_set_name: builtins.str,
    ) -> None:
        '''A reference to a ConfigurationSet resource.

        :param configuration_set_arn: The ARN of the ConfigurationSet resource.
        :param configuration_set_name: The ConfigurationSetName of the ConfigurationSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_smsvoice as interfaces_smsvoice
            
            configuration_set_reference = interfaces_smsvoice.ConfigurationSetReference(
                configuration_set_arn="configurationSetArn",
                configuration_set_name="configurationSetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfb39e554f6e12d2e0f782656ac6a33ba83d6aeeaeb2487ee28801dbe15f558d)
            check_type(argname="argument configuration_set_arn", value=configuration_set_arn, expected_type=type_hints["configuration_set_arn"])
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_set_arn": configuration_set_arn,
            "configuration_set_name": configuration_set_name,
        }

    @builtins.property
    def configuration_set_arn(self) -> builtins.str:
        '''The ARN of the ConfigurationSet resource.'''
        result = self._values.get("configuration_set_arn")
        assert result is not None, "Required property 'configuration_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_set_name(self) -> builtins.str:
        '''The ConfigurationSetName of the ConfigurationSet resource.'''
        result = self._values.get("configuration_set_name")
        assert result is not None, "Required property 'configuration_set_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.IConfigurationSetRef")
class IConfigurationSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationSetRef")
    def configuration_set_ref(self) -> "ConfigurationSetReference":
        '''(experimental) A reference to a ConfigurationSet resource.

        :stability: experimental
        '''
        ...


class _IConfigurationSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_smsvoice.IConfigurationSetRef"

    @builtins.property
    @jsii.member(jsii_name="configurationSetRef")
    def configuration_set_ref(self) -> "ConfigurationSetReference":
        '''(experimental) A reference to a ConfigurationSet resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationSetReference", jsii.get(self, "configurationSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationSetRef).__jsii_proxy_class__ = lambda : _IConfigurationSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.IOptOutListRef")
class IOptOutListRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OptOutList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="optOutListRef")
    def opt_out_list_ref(self) -> "OptOutListReference":
        '''(experimental) A reference to a OptOutList resource.

        :stability: experimental
        '''
        ...


class _IOptOutListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OptOutList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_smsvoice.IOptOutListRef"

    @builtins.property
    @jsii.member(jsii_name="optOutListRef")
    def opt_out_list_ref(self) -> "OptOutListReference":
        '''(experimental) A reference to a OptOutList resource.

        :stability: experimental
        '''
        return typing.cast("OptOutListReference", jsii.get(self, "optOutListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOptOutListRef).__jsii_proxy_class__ = lambda : _IOptOutListRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.IPhoneNumberRef")
class IPhoneNumberRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PhoneNumber.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="phoneNumberRef")
    def phone_number_ref(self) -> "PhoneNumberReference":
        '''(experimental) A reference to a PhoneNumber resource.

        :stability: experimental
        '''
        ...


class _IPhoneNumberRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PhoneNumber.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_smsvoice.IPhoneNumberRef"

    @builtins.property
    @jsii.member(jsii_name="phoneNumberRef")
    def phone_number_ref(self) -> "PhoneNumberReference":
        '''(experimental) A reference to a PhoneNumber resource.

        :stability: experimental
        '''
        return typing.cast("PhoneNumberReference", jsii.get(self, "phoneNumberRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPhoneNumberRef).__jsii_proxy_class__ = lambda : _IPhoneNumberRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.IPoolRef")
class IPoolRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Pool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="poolRef")
    def pool_ref(self) -> "PoolReference":
        '''(experimental) A reference to a Pool resource.

        :stability: experimental
        '''
        ...


class _IPoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Pool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_smsvoice.IPoolRef"

    @builtins.property
    @jsii.member(jsii_name="poolRef")
    def pool_ref(self) -> "PoolReference":
        '''(experimental) A reference to a Pool resource.

        :stability: experimental
        '''
        return typing.cast("PoolReference", jsii.get(self, "poolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPoolRef).__jsii_proxy_class__ = lambda : _IPoolRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.IProtectConfigurationRef"
)
class IProtectConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProtectConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="protectConfigurationRef")
    def protect_configuration_ref(self) -> "ProtectConfigurationReference":
        '''(experimental) A reference to a ProtectConfiguration resource.

        :stability: experimental
        '''
        ...


class _IProtectConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProtectConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_smsvoice.IProtectConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="protectConfigurationRef")
    def protect_configuration_ref(self) -> "ProtectConfigurationReference":
        '''(experimental) A reference to a ProtectConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("ProtectConfigurationReference", jsii.get(self, "protectConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProtectConfigurationRef).__jsii_proxy_class__ = lambda : _IProtectConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.IResourcePolicyRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_smsvoice.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.ISenderIdRef")
class ISenderIdRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SenderId.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="senderIdRef")
    def sender_id_ref(self) -> "SenderIdReference":
        '''(experimental) A reference to a SenderId resource.

        :stability: experimental
        '''
        ...


class _ISenderIdRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SenderId.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_smsvoice.ISenderIdRef"

    @builtins.property
    @jsii.member(jsii_name="senderIdRef")
    def sender_id_ref(self) -> "SenderIdReference":
        '''(experimental) A reference to a SenderId resource.

        :stability: experimental
        '''
        return typing.cast("SenderIdReference", jsii.get(self, "senderIdRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISenderIdRef).__jsii_proxy_class__ = lambda : _ISenderIdRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.OptOutListReference",
    jsii_struct_bases=[],
    name_mapping={
        "opt_out_list_arn": "optOutListArn",
        "opt_out_list_name": "optOutListName",
    },
)
class OptOutListReference:
    def __init__(
        self,
        *,
        opt_out_list_arn: builtins.str,
        opt_out_list_name: builtins.str,
    ) -> None:
        '''A reference to a OptOutList resource.

        :param opt_out_list_arn: The ARN of the OptOutList resource.
        :param opt_out_list_name: The OptOutListName of the OptOutList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_smsvoice as interfaces_smsvoice
            
            opt_out_list_reference = interfaces_smsvoice.OptOutListReference(
                opt_out_list_arn="optOutListArn",
                opt_out_list_name="optOutListName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43cbbd6644494d6e6917995b076d6eff7e0a8fae16fd1c29e2cb4a0769850cf9)
            check_type(argname="argument opt_out_list_arn", value=opt_out_list_arn, expected_type=type_hints["opt_out_list_arn"])
            check_type(argname="argument opt_out_list_name", value=opt_out_list_name, expected_type=type_hints["opt_out_list_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "opt_out_list_arn": opt_out_list_arn,
            "opt_out_list_name": opt_out_list_name,
        }

    @builtins.property
    def opt_out_list_arn(self) -> builtins.str:
        '''The ARN of the OptOutList resource.'''
        result = self._values.get("opt_out_list_arn")
        assert result is not None, "Required property 'opt_out_list_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def opt_out_list_name(self) -> builtins.str:
        '''The OptOutListName of the OptOutList resource.'''
        result = self._values.get("opt_out_list_name")
        assert result is not None, "Required property 'opt_out_list_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OptOutListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.PhoneNumberReference",
    jsii_struct_bases=[],
    name_mapping={
        "phone_number_arn": "phoneNumberArn",
        "phone_number_id": "phoneNumberId",
    },
)
class PhoneNumberReference:
    def __init__(
        self,
        *,
        phone_number_arn: builtins.str,
        phone_number_id: builtins.str,
    ) -> None:
        '''A reference to a PhoneNumber resource.

        :param phone_number_arn: The ARN of the PhoneNumber resource.
        :param phone_number_id: The PhoneNumberId of the PhoneNumber resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_smsvoice as interfaces_smsvoice
            
            phone_number_reference = interfaces_smsvoice.PhoneNumberReference(
                phone_number_arn="phoneNumberArn",
                phone_number_id="phoneNumberId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__453bd7ec7d509a3524a273a39756f965d62e5f124510d71db14e4c0eca91888b)
            check_type(argname="argument phone_number_arn", value=phone_number_arn, expected_type=type_hints["phone_number_arn"])
            check_type(argname="argument phone_number_id", value=phone_number_id, expected_type=type_hints["phone_number_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_number_arn": phone_number_arn,
            "phone_number_id": phone_number_id,
        }

    @builtins.property
    def phone_number_arn(self) -> builtins.str:
        '''The ARN of the PhoneNumber resource.'''
        result = self._values.get("phone_number_arn")
        assert result is not None, "Required property 'phone_number_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def phone_number_id(self) -> builtins.str:
        '''The PhoneNumberId of the PhoneNumber resource.'''
        result = self._values.get("phone_number_id")
        assert result is not None, "Required property 'phone_number_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PhoneNumberReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.PoolReference",
    jsii_struct_bases=[],
    name_mapping={"pool_arn": "poolArn", "pool_id": "poolId"},
)
class PoolReference:
    def __init__(self, *, pool_arn: builtins.str, pool_id: builtins.str) -> None:
        '''A reference to a Pool resource.

        :param pool_arn: The ARN of the Pool resource.
        :param pool_id: The PoolId of the Pool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_smsvoice as interfaces_smsvoice
            
            pool_reference = interfaces_smsvoice.PoolReference(
                pool_arn="poolArn",
                pool_id="poolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a18e0245425fe1d0408a83f73186ebf7f8da155158cc1a6fa8ad9d52335023e)
            check_type(argname="argument pool_arn", value=pool_arn, expected_type=type_hints["pool_arn"])
            check_type(argname="argument pool_id", value=pool_id, expected_type=type_hints["pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pool_arn": pool_arn,
            "pool_id": pool_id,
        }

    @builtins.property
    def pool_arn(self) -> builtins.str:
        '''The ARN of the Pool resource.'''
        result = self._values.get("pool_arn")
        assert result is not None, "Required property 'pool_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pool_id(self) -> builtins.str:
        '''The PoolId of the Pool resource.'''
        result = self._values.get("pool_id")
        assert result is not None, "Required property 'pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.ProtectConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "protect_configuration_arn": "protectConfigurationArn",
        "protect_configuration_id": "protectConfigurationId",
    },
)
class ProtectConfigurationReference:
    def __init__(
        self,
        *,
        protect_configuration_arn: builtins.str,
        protect_configuration_id: builtins.str,
    ) -> None:
        '''A reference to a ProtectConfiguration resource.

        :param protect_configuration_arn: The ARN of the ProtectConfiguration resource.
        :param protect_configuration_id: The ProtectConfigurationId of the ProtectConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_smsvoice as interfaces_smsvoice
            
            protect_configuration_reference = interfaces_smsvoice.ProtectConfigurationReference(
                protect_configuration_arn="protectConfigurationArn",
                protect_configuration_id="protectConfigurationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7a573c31ffa2a3dbcab67f8fc27bcefd307f49af5d533c3d96ed3f9e17288f5)
            check_type(argname="argument protect_configuration_arn", value=protect_configuration_arn, expected_type=type_hints["protect_configuration_arn"])
            check_type(argname="argument protect_configuration_id", value=protect_configuration_id, expected_type=type_hints["protect_configuration_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protect_configuration_arn": protect_configuration_arn,
            "protect_configuration_id": protect_configuration_id,
        }

    @builtins.property
    def protect_configuration_arn(self) -> builtins.str:
        '''The ARN of the ProtectConfiguration resource.'''
        result = self._values.get("protect_configuration_arn")
        assert result is not None, "Required property 'protect_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protect_configuration_id(self) -> builtins.str:
        '''The ProtectConfigurationId of the ProtectConfiguration resource.'''
        result = self._values.get("protect_configuration_id")
        assert result is not None, "Required property 'protect_configuration_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProtectConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class ResourcePolicyReference:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param resource_arn: The ResourceArn of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_smsvoice as interfaces_smsvoice
            
            resource_policy_reference = interfaces_smsvoice.ResourcePolicyReference(
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4e3f8cc42e17b187443815800b2d641d17f0860df1f5ec19e3aeb16b4072509)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the ResourcePolicy resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_smsvoice.SenderIdReference",
    jsii_struct_bases=[],
    name_mapping={
        "iso_country_code": "isoCountryCode",
        "sender_id": "senderId",
        "sender_id_arn": "senderIdArn",
    },
)
class SenderIdReference:
    def __init__(
        self,
        *,
        iso_country_code: builtins.str,
        sender_id: builtins.str,
        sender_id_arn: builtins.str,
    ) -> None:
        '''A reference to a SenderId resource.

        :param iso_country_code: The IsoCountryCode of the SenderId resource.
        :param sender_id: The SenderId of the SenderId resource.
        :param sender_id_arn: The ARN of the SenderId resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_smsvoice as interfaces_smsvoice
            
            sender_id_reference = interfaces_smsvoice.SenderIdReference(
                iso_country_code="isoCountryCode",
                sender_id="senderId",
                sender_id_arn="senderIdArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ba8d95c82cd8ae22b8aa29f3c0b6b9b02e4d8ffd2e2cf690bd27ab2e3d024f4)
            check_type(argname="argument iso_country_code", value=iso_country_code, expected_type=type_hints["iso_country_code"])
            check_type(argname="argument sender_id", value=sender_id, expected_type=type_hints["sender_id"])
            check_type(argname="argument sender_id_arn", value=sender_id_arn, expected_type=type_hints["sender_id_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "iso_country_code": iso_country_code,
            "sender_id": sender_id,
            "sender_id_arn": sender_id_arn,
        }

    @builtins.property
    def iso_country_code(self) -> builtins.str:
        '''The IsoCountryCode of the SenderId resource.'''
        result = self._values.get("iso_country_code")
        assert result is not None, "Required property 'iso_country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sender_id(self) -> builtins.str:
        '''The SenderId of the SenderId resource.'''
        result = self._values.get("sender_id")
        assert result is not None, "Required property 'sender_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sender_id_arn(self) -> builtins.str:
        '''The ARN of the SenderId resource.'''
        result = self._values.get("sender_id_arn")
        assert result is not None, "Required property 'sender_id_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SenderIdReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConfigurationSetReference",
    "IConfigurationSetRef",
    "IOptOutListRef",
    "IPhoneNumberRef",
    "IPoolRef",
    "IProtectConfigurationRef",
    "IResourcePolicyRef",
    "ISenderIdRef",
    "OptOutListReference",
    "PhoneNumberReference",
    "PoolReference",
    "ProtectConfigurationReference",
    "ResourcePolicyReference",
    "SenderIdReference",
]

publication.publish()

def _typecheckingstub__bfb39e554f6e12d2e0f782656ac6a33ba83d6aeeaeb2487ee28801dbe15f558d(
    *,
    configuration_set_arn: builtins.str,
    configuration_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43cbbd6644494d6e6917995b076d6eff7e0a8fae16fd1c29e2cb4a0769850cf9(
    *,
    opt_out_list_arn: builtins.str,
    opt_out_list_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__453bd7ec7d509a3524a273a39756f965d62e5f124510d71db14e4c0eca91888b(
    *,
    phone_number_arn: builtins.str,
    phone_number_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a18e0245425fe1d0408a83f73186ebf7f8da155158cc1a6fa8ad9d52335023e(
    *,
    pool_arn: builtins.str,
    pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a573c31ffa2a3dbcab67f8fc27bcefd307f49af5d533c3d96ed3f9e17288f5(
    *,
    protect_configuration_arn: builtins.str,
    protect_configuration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4e3f8cc42e17b187443815800b2d641d17f0860df1f5ec19e3aeb16b4072509(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ba8d95c82cd8ae22b8aa29f3c0b6b9b02e4d8ffd2e2cf690bd27ab2e3d024f4(
    *,
    iso_country_code: builtins.str,
    sender_id: builtins.str,
    sender_id_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConfigurationSetRef, IOptOutListRef, IPhoneNumberRef, IPoolRef, IProtectConfigurationRef, IResourcePolicyRef, ISenderIdRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
