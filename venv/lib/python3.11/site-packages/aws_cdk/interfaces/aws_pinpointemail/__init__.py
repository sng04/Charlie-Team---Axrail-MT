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
    jsii_type="aws-cdk-lib.interfaces.aws_pinpointemail.ConfigurationSetEventDestinationReference",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_event_destination_id": "configurationSetEventDestinationId",
    },
)
class ConfigurationSetEventDestinationReference:
    def __init__(self, *, configuration_set_event_destination_id: builtins.str) -> None:
        '''A reference to a ConfigurationSetEventDestination resource.

        :param configuration_set_event_destination_id: The Id of the ConfigurationSetEventDestination resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpointemail as interfaces_pinpointemail
            
            configuration_set_event_destination_reference = interfaces_pinpointemail.ConfigurationSetEventDestinationReference(
                configuration_set_event_destination_id="configurationSetEventDestinationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b909465e6f6306bba6e842c397fc01b44eb7471a9fbb9b43cf9caba8cb9ddf3)
            check_type(argname="argument configuration_set_event_destination_id", value=configuration_set_event_destination_id, expected_type=type_hints["configuration_set_event_destination_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_set_event_destination_id": configuration_set_event_destination_id,
        }

    @builtins.property
    def configuration_set_event_destination_id(self) -> builtins.str:
        '''The Id of the ConfigurationSetEventDestination resource.'''
        result = self._values.get("configuration_set_event_destination_id")
        assert result is not None, "Required property 'configuration_set_event_destination_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationSetEventDestinationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpointemail.ConfigurationSetReference",
    jsii_struct_bases=[],
    name_mapping={"configuration_set_id": "configurationSetId"},
)
class ConfigurationSetReference:
    def __init__(self, *, configuration_set_id: builtins.str) -> None:
        '''A reference to a ConfigurationSet resource.

        :param configuration_set_id: The Id of the ConfigurationSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpointemail as interfaces_pinpointemail
            
            configuration_set_reference = interfaces_pinpointemail.ConfigurationSetReference(
                configuration_set_id="configurationSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c65b2a61909640ecc74c0f5c538aa77bdf3497e55637f9c825f2a3bd86cf838)
            check_type(argname="argument configuration_set_id", value=configuration_set_id, expected_type=type_hints["configuration_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_set_id": configuration_set_id,
        }

    @builtins.property
    def configuration_set_id(self) -> builtins.str:
        '''The Id of the ConfigurationSet resource.'''
        result = self._values.get("configuration_set_id")
        assert result is not None, "Required property 'configuration_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpointemail.DedicatedIpPoolReference",
    jsii_struct_bases=[],
    name_mapping={"dedicated_ip_pool_id": "dedicatedIpPoolId"},
)
class DedicatedIpPoolReference:
    def __init__(self, *, dedicated_ip_pool_id: builtins.str) -> None:
        '''A reference to a DedicatedIpPool resource.

        :param dedicated_ip_pool_id: The Id of the DedicatedIpPool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpointemail as interfaces_pinpointemail
            
            dedicated_ip_pool_reference = interfaces_pinpointemail.DedicatedIpPoolReference(
                dedicated_ip_pool_id="dedicatedIpPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fafa93669457d2e7d713b3029005b5a26adb0ce923a0eada0db2a3d9d4b72a95)
            check_type(argname="argument dedicated_ip_pool_id", value=dedicated_ip_pool_id, expected_type=type_hints["dedicated_ip_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dedicated_ip_pool_id": dedicated_ip_pool_id,
        }

    @builtins.property
    def dedicated_ip_pool_id(self) -> builtins.str:
        '''The Id of the DedicatedIpPool resource.'''
        result = self._values.get("dedicated_ip_pool_id")
        assert result is not None, "Required property 'dedicated_ip_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DedicatedIpPoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpointemail.IConfigurationSetEventDestinationRef"
)
class IConfigurationSetEventDestinationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationSetEventDestination.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationSetEventDestinationRef")
    def configuration_set_event_destination_ref(
        self,
    ) -> "ConfigurationSetEventDestinationReference":
        '''(experimental) A reference to a ConfigurationSetEventDestination resource.

        :stability: experimental
        '''
        ...


class _IConfigurationSetEventDestinationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationSetEventDestination.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpointemail.IConfigurationSetEventDestinationRef"

    @builtins.property
    @jsii.member(jsii_name="configurationSetEventDestinationRef")
    def configuration_set_event_destination_ref(
        self,
    ) -> "ConfigurationSetEventDestinationReference":
        '''(experimental) A reference to a ConfigurationSetEventDestination resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationSetEventDestinationReference", jsii.get(self, "configurationSetEventDestinationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationSetEventDestinationRef).__jsii_proxy_class__ = lambda : _IConfigurationSetEventDestinationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpointemail.IConfigurationSetRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpointemail.IConfigurationSetRef"

    @builtins.property
    @jsii.member(jsii_name="configurationSetRef")
    def configuration_set_ref(self) -> "ConfigurationSetReference":
        '''(experimental) A reference to a ConfigurationSet resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationSetReference", jsii.get(self, "configurationSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationSetRef).__jsii_proxy_class__ = lambda : _IConfigurationSetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpointemail.IDedicatedIpPoolRef"
)
class IDedicatedIpPoolRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DedicatedIpPool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dedicatedIpPoolRef")
    def dedicated_ip_pool_ref(self) -> "DedicatedIpPoolReference":
        '''(experimental) A reference to a DedicatedIpPool resource.

        :stability: experimental
        '''
        ...


class _IDedicatedIpPoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DedicatedIpPool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpointemail.IDedicatedIpPoolRef"

    @builtins.property
    @jsii.member(jsii_name="dedicatedIpPoolRef")
    def dedicated_ip_pool_ref(self) -> "DedicatedIpPoolReference":
        '''(experimental) A reference to a DedicatedIpPool resource.

        :stability: experimental
        '''
        return typing.cast("DedicatedIpPoolReference", jsii.get(self, "dedicatedIpPoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDedicatedIpPoolRef).__jsii_proxy_class__ = lambda : _IDedicatedIpPoolRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpointemail.IIdentityRef")
class IIdentityRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Identity.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="identityRef")
    def identity_ref(self) -> "IdentityReference":
        '''(experimental) A reference to a Identity resource.

        :stability: experimental
        '''
        ...


class _IIdentityRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Identity.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpointemail.IIdentityRef"

    @builtins.property
    @jsii.member(jsii_name="identityRef")
    def identity_ref(self) -> "IdentityReference":
        '''(experimental) A reference to a Identity resource.

        :stability: experimental
        '''
        return typing.cast("IdentityReference", jsii.get(self, "identityRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentityRef).__jsii_proxy_class__ = lambda : _IIdentityRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpointemail.IdentityReference",
    jsii_struct_bases=[],
    name_mapping={"identity_id": "identityId"},
)
class IdentityReference:
    def __init__(self, *, identity_id: builtins.str) -> None:
        '''A reference to a Identity resource.

        :param identity_id: The Id of the Identity resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpointemail as interfaces_pinpointemail
            
            identity_reference = interfaces_pinpointemail.IdentityReference(
                identity_id="identityId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6e5c957f470b1c97778fb1d59e10b6b948992635bfdaccfbc1e61d9ffa5e7f2)
            check_type(argname="argument identity_id", value=identity_id, expected_type=type_hints["identity_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_id": identity_id,
        }

    @builtins.property
    def identity_id(self) -> builtins.str:
        '''The Id of the Identity resource.'''
        result = self._values.get("identity_id")
        assert result is not None, "Required property 'identity_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConfigurationSetEventDestinationReference",
    "ConfigurationSetReference",
    "DedicatedIpPoolReference",
    "IConfigurationSetEventDestinationRef",
    "IConfigurationSetRef",
    "IDedicatedIpPoolRef",
    "IIdentityRef",
    "IdentityReference",
]

publication.publish()

def _typecheckingstub__5b909465e6f6306bba6e842c397fc01b44eb7471a9fbb9b43cf9caba8cb9ddf3(
    *,
    configuration_set_event_destination_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c65b2a61909640ecc74c0f5c538aa77bdf3497e55637f9c825f2a3bd86cf838(
    *,
    configuration_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fafa93669457d2e7d713b3029005b5a26adb0ce923a0eada0db2a3d9d4b72a95(
    *,
    dedicated_ip_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e5c957f470b1c97778fb1d59e10b6b948992635bfdaccfbc1e61d9ffa5e7f2(
    *,
    identity_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConfigurationSetEventDestinationRef, IConfigurationSetRef, IDedicatedIpPoolRef, IIdentityRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
