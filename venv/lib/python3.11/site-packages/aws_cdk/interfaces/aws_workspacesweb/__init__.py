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
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.BrowserSettingsReference",
    jsii_struct_bases=[],
    name_mapping={"browser_settings_arn": "browserSettingsArn"},
)
class BrowserSettingsReference:
    def __init__(self, *, browser_settings_arn: builtins.str) -> None:
        '''A reference to a BrowserSettings resource.

        :param browser_settings_arn: The BrowserSettingsArn of the BrowserSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            browser_settings_reference = interfaces_workspacesweb.BrowserSettingsReference(
                browser_settings_arn="browserSettingsArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a86f83cb991212444d3914144c22ba1dc691d5dee8f106349739cab5ff64b4a)
            check_type(argname="argument browser_settings_arn", value=browser_settings_arn, expected_type=type_hints["browser_settings_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "browser_settings_arn": browser_settings_arn,
        }

    @builtins.property
    def browser_settings_arn(self) -> builtins.str:
        '''The BrowserSettingsArn of the BrowserSettings resource.'''
        result = self._values.get("browser_settings_arn")
        assert result is not None, "Required property 'browser_settings_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BrowserSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.DataProtectionSettingsReference",
    jsii_struct_bases=[],
    name_mapping={"data_protection_settings_arn": "dataProtectionSettingsArn"},
)
class DataProtectionSettingsReference:
    def __init__(self, *, data_protection_settings_arn: builtins.str) -> None:
        '''A reference to a DataProtectionSettings resource.

        :param data_protection_settings_arn: The DataProtectionSettingsArn of the DataProtectionSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            data_protection_settings_reference = interfaces_workspacesweb.DataProtectionSettingsReference(
                data_protection_settings_arn="dataProtectionSettingsArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1f3632e4487bac999312f4a7bf06ce08cb7b3d71d0411d0bb8a1b296dd3c57b)
            check_type(argname="argument data_protection_settings_arn", value=data_protection_settings_arn, expected_type=type_hints["data_protection_settings_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_protection_settings_arn": data_protection_settings_arn,
        }

    @builtins.property
    def data_protection_settings_arn(self) -> builtins.str:
        '''The DataProtectionSettingsArn of the DataProtectionSettings resource.'''
        result = self._values.get("data_protection_settings_arn")
        assert result is not None, "Required property 'data_protection_settings_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProtectionSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.IBrowserSettingsRef"
)
class IBrowserSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BrowserSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="browserSettingsRef")
    def browser_settings_ref(self) -> "BrowserSettingsReference":
        '''(experimental) A reference to a BrowserSettings resource.

        :stability: experimental
        '''
        ...


class _IBrowserSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BrowserSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.IBrowserSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="browserSettingsRef")
    def browser_settings_ref(self) -> "BrowserSettingsReference":
        '''(experimental) A reference to a BrowserSettings resource.

        :stability: experimental
        '''
        return typing.cast("BrowserSettingsReference", jsii.get(self, "browserSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBrowserSettingsRef).__jsii_proxy_class__ = lambda : _IBrowserSettingsRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.IDataProtectionSettingsRef"
)
class IDataProtectionSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataProtectionSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataProtectionSettingsRef")
    def data_protection_settings_ref(self) -> "DataProtectionSettingsReference":
        '''(experimental) A reference to a DataProtectionSettings resource.

        :stability: experimental
        '''
        ...


class _IDataProtectionSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataProtectionSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.IDataProtectionSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="dataProtectionSettingsRef")
    def data_protection_settings_ref(self) -> "DataProtectionSettingsReference":
        '''(experimental) A reference to a DataProtectionSettings resource.

        :stability: experimental
        '''
        return typing.cast("DataProtectionSettingsReference", jsii.get(self, "dataProtectionSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataProtectionSettingsRef).__jsii_proxy_class__ = lambda : _IDataProtectionSettingsRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.IIdentityProviderRef"
)
class IIdentityProviderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityProvider.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="identityProviderRef")
    def identity_provider_ref(self) -> "IdentityProviderReference":
        '''(experimental) A reference to a IdentityProvider resource.

        :stability: experimental
        '''
        ...


class _IIdentityProviderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityProvider.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.IIdentityProviderRef"

    @builtins.property
    @jsii.member(jsii_name="identityProviderRef")
    def identity_provider_ref(self) -> "IdentityProviderReference":
        '''(experimental) A reference to a IdentityProvider resource.

        :stability: experimental
        '''
        return typing.cast("IdentityProviderReference", jsii.get(self, "identityProviderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentityProviderRef).__jsii_proxy_class__ = lambda : _IIdentityProviderRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.IIpAccessSettingsRef"
)
class IIpAccessSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IpAccessSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipAccessSettingsRef")
    def ip_access_settings_ref(self) -> "IpAccessSettingsReference":
        '''(experimental) A reference to a IpAccessSettings resource.

        :stability: experimental
        '''
        ...


class _IIpAccessSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IpAccessSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.IIpAccessSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="ipAccessSettingsRef")
    def ip_access_settings_ref(self) -> "IpAccessSettingsReference":
        '''(experimental) A reference to a IpAccessSettings resource.

        :stability: experimental
        '''
        return typing.cast("IpAccessSettingsReference", jsii.get(self, "ipAccessSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIpAccessSettingsRef).__jsii_proxy_class__ = lambda : _IIpAccessSettingsRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.INetworkSettingsRef"
)
class INetworkSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkSettingsRef")
    def network_settings_ref(self) -> "NetworkSettingsReference":
        '''(experimental) A reference to a NetworkSettings resource.

        :stability: experimental
        '''
        ...


class _INetworkSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.INetworkSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="networkSettingsRef")
    def network_settings_ref(self) -> "NetworkSettingsReference":
        '''(experimental) A reference to a NetworkSettings resource.

        :stability: experimental
        '''
        return typing.cast("NetworkSettingsReference", jsii.get(self, "networkSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkSettingsRef).__jsii_proxy_class__ = lambda : _INetworkSettingsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.IPortalRef")
class IPortalRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Portal.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="portalRef")
    def portal_ref(self) -> "PortalReference":
        '''(experimental) A reference to a Portal resource.

        :stability: experimental
        '''
        ...


class _IPortalRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Portal.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.IPortalRef"

    @builtins.property
    @jsii.member(jsii_name="portalRef")
    def portal_ref(self) -> "PortalReference":
        '''(experimental) A reference to a Portal resource.

        :stability: experimental
        '''
        return typing.cast("PortalReference", jsii.get(self, "portalRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPortalRef).__jsii_proxy_class__ = lambda : _IPortalRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.ISessionLoggerRef")
class ISessionLoggerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SessionLogger.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sessionLoggerRef")
    def session_logger_ref(self) -> "SessionLoggerReference":
        '''(experimental) A reference to a SessionLogger resource.

        :stability: experimental
        '''
        ...


class _ISessionLoggerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SessionLogger.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.ISessionLoggerRef"

    @builtins.property
    @jsii.member(jsii_name="sessionLoggerRef")
    def session_logger_ref(self) -> "SessionLoggerReference":
        '''(experimental) A reference to a SessionLogger resource.

        :stability: experimental
        '''
        return typing.cast("SessionLoggerReference", jsii.get(self, "sessionLoggerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISessionLoggerRef).__jsii_proxy_class__ = lambda : _ISessionLoggerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.ITrustStoreRef")
class ITrustStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrustStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trustStoreRef")
    def trust_store_ref(self) -> "TrustStoreReference":
        '''(experimental) A reference to a TrustStore resource.

        :stability: experimental
        '''
        ...


class _ITrustStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrustStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.ITrustStoreRef"

    @builtins.property
    @jsii.member(jsii_name="trustStoreRef")
    def trust_store_ref(self) -> "TrustStoreReference":
        '''(experimental) A reference to a TrustStore resource.

        :stability: experimental
        '''
        return typing.cast("TrustStoreReference", jsii.get(self, "trustStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrustStoreRef).__jsii_proxy_class__ = lambda : _ITrustStoreRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.IUserAccessLoggingSettingsRef"
)
class IUserAccessLoggingSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserAccessLoggingSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userAccessLoggingSettingsRef")
    def user_access_logging_settings_ref(self) -> "UserAccessLoggingSettingsReference":
        '''(experimental) A reference to a UserAccessLoggingSettings resource.

        :stability: experimental
        '''
        ...


class _IUserAccessLoggingSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserAccessLoggingSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.IUserAccessLoggingSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="userAccessLoggingSettingsRef")
    def user_access_logging_settings_ref(self) -> "UserAccessLoggingSettingsReference":
        '''(experimental) A reference to a UserAccessLoggingSettings resource.

        :stability: experimental
        '''
        return typing.cast("UserAccessLoggingSettingsReference", jsii.get(self, "userAccessLoggingSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserAccessLoggingSettingsRef).__jsii_proxy_class__ = lambda : _IUserAccessLoggingSettingsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.IUserSettingsRef")
class IUserSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userSettingsRef")
    def user_settings_ref(self) -> "UserSettingsReference":
        '''(experimental) A reference to a UserSettings resource.

        :stability: experimental
        '''
        ...


class _IUserSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesweb.IUserSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="userSettingsRef")
    def user_settings_ref(self) -> "UserSettingsReference":
        '''(experimental) A reference to a UserSettings resource.

        :stability: experimental
        '''
        return typing.cast("UserSettingsReference", jsii.get(self, "userSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserSettingsRef).__jsii_proxy_class__ = lambda : _IUserSettingsRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.IdentityProviderReference",
    jsii_struct_bases=[],
    name_mapping={"identity_provider_arn": "identityProviderArn"},
)
class IdentityProviderReference:
    def __init__(self, *, identity_provider_arn: builtins.str) -> None:
        '''A reference to a IdentityProvider resource.

        :param identity_provider_arn: The IdentityProviderArn of the IdentityProvider resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            identity_provider_reference = interfaces_workspacesweb.IdentityProviderReference(
                identity_provider_arn="identityProviderArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d06a54ff8ceeaae4c4158181d934d8e147b1c9743c60c74bdf6fd682edcf3636)
            check_type(argname="argument identity_provider_arn", value=identity_provider_arn, expected_type=type_hints["identity_provider_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_provider_arn": identity_provider_arn,
        }

    @builtins.property
    def identity_provider_arn(self) -> builtins.str:
        '''The IdentityProviderArn of the IdentityProvider resource.'''
        result = self._values.get("identity_provider_arn")
        assert result is not None, "Required property 'identity_provider_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityProviderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.IpAccessSettingsReference",
    jsii_struct_bases=[],
    name_mapping={"ip_access_settings_arn": "ipAccessSettingsArn"},
)
class IpAccessSettingsReference:
    def __init__(self, *, ip_access_settings_arn: builtins.str) -> None:
        '''A reference to a IpAccessSettings resource.

        :param ip_access_settings_arn: The IpAccessSettingsArn of the IpAccessSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            ip_access_settings_reference = interfaces_workspacesweb.IpAccessSettingsReference(
                ip_access_settings_arn="ipAccessSettingsArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83929b7ec7392cc5bbd9b90982729d0fd7528f39bc08e8d857f58293db8c397b)
            check_type(argname="argument ip_access_settings_arn", value=ip_access_settings_arn, expected_type=type_hints["ip_access_settings_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_access_settings_arn": ip_access_settings_arn,
        }

    @builtins.property
    def ip_access_settings_arn(self) -> builtins.str:
        '''The IpAccessSettingsArn of the IpAccessSettings resource.'''
        result = self._values.get("ip_access_settings_arn")
        assert result is not None, "Required property 'ip_access_settings_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IpAccessSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.NetworkSettingsReference",
    jsii_struct_bases=[],
    name_mapping={"network_settings_arn": "networkSettingsArn"},
)
class NetworkSettingsReference:
    def __init__(self, *, network_settings_arn: builtins.str) -> None:
        '''A reference to a NetworkSettings resource.

        :param network_settings_arn: The NetworkSettingsArn of the NetworkSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            network_settings_reference = interfaces_workspacesweb.NetworkSettingsReference(
                network_settings_arn="networkSettingsArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b481c867b1f52384ef579bc94fecc53088b5d9b42cbf8fd48ae69a4f3eba7614)
            check_type(argname="argument network_settings_arn", value=network_settings_arn, expected_type=type_hints["network_settings_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_settings_arn": network_settings_arn,
        }

    @builtins.property
    def network_settings_arn(self) -> builtins.str:
        '''The NetworkSettingsArn of the NetworkSettings resource.'''
        result = self._values.get("network_settings_arn")
        assert result is not None, "Required property 'network_settings_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.PortalReference",
    jsii_struct_bases=[],
    name_mapping={"portal_arn": "portalArn"},
)
class PortalReference:
    def __init__(self, *, portal_arn: builtins.str) -> None:
        '''A reference to a Portal resource.

        :param portal_arn: The PortalArn of the Portal resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            portal_reference = interfaces_workspacesweb.PortalReference(
                portal_arn="portalArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e663ea314aede92b25306c3859d2d29050477dc0a13e30bad8966d0295d92ddc)
            check_type(argname="argument portal_arn", value=portal_arn, expected_type=type_hints["portal_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "portal_arn": portal_arn,
        }

    @builtins.property
    def portal_arn(self) -> builtins.str:
        '''The PortalArn of the Portal resource.'''
        result = self._values.get("portal_arn")
        assert result is not None, "Required property 'portal_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortalReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.SessionLoggerReference",
    jsii_struct_bases=[],
    name_mapping={"session_logger_arn": "sessionLoggerArn"},
)
class SessionLoggerReference:
    def __init__(self, *, session_logger_arn: builtins.str) -> None:
        '''A reference to a SessionLogger resource.

        :param session_logger_arn: The SessionLoggerArn of the SessionLogger resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            session_logger_reference = interfaces_workspacesweb.SessionLoggerReference(
                session_logger_arn="sessionLoggerArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__093e66dd03530c70c2cad4c0f448985c476bc2060565e5166b6df4c62767aa17)
            check_type(argname="argument session_logger_arn", value=session_logger_arn, expected_type=type_hints["session_logger_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "session_logger_arn": session_logger_arn,
        }

    @builtins.property
    def session_logger_arn(self) -> builtins.str:
        '''The SessionLoggerArn of the SessionLogger resource.'''
        result = self._values.get("session_logger_arn")
        assert result is not None, "Required property 'session_logger_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SessionLoggerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.TrustStoreReference",
    jsii_struct_bases=[],
    name_mapping={"trust_store_arn": "trustStoreArn"},
)
class TrustStoreReference:
    def __init__(self, *, trust_store_arn: builtins.str) -> None:
        '''A reference to a TrustStore resource.

        :param trust_store_arn: The TrustStoreArn of the TrustStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            trust_store_reference = interfaces_workspacesweb.TrustStoreReference(
                trust_store_arn="trustStoreArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f89506317979fe315a43fa5d8074f96c94b1d554fda4754a3be13cf61c32164)
            check_type(argname="argument trust_store_arn", value=trust_store_arn, expected_type=type_hints["trust_store_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trust_store_arn": trust_store_arn,
        }

    @builtins.property
    def trust_store_arn(self) -> builtins.str:
        '''The TrustStoreArn of the TrustStore resource.'''
        result = self._values.get("trust_store_arn")
        assert result is not None, "Required property 'trust_store_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrustStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.UserAccessLoggingSettingsReference",
    jsii_struct_bases=[],
    name_mapping={"user_access_logging_settings_arn": "userAccessLoggingSettingsArn"},
)
class UserAccessLoggingSettingsReference:
    def __init__(self, *, user_access_logging_settings_arn: builtins.str) -> None:
        '''A reference to a UserAccessLoggingSettings resource.

        :param user_access_logging_settings_arn: The UserAccessLoggingSettingsArn of the UserAccessLoggingSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            user_access_logging_settings_reference = interfaces_workspacesweb.UserAccessLoggingSettingsReference(
                user_access_logging_settings_arn="userAccessLoggingSettingsArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d5e1a279ef19952e911a4b1d07cccfd213091ece112e6e4d62b76fd9fc991aa)
            check_type(argname="argument user_access_logging_settings_arn", value=user_access_logging_settings_arn, expected_type=type_hints["user_access_logging_settings_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_access_logging_settings_arn": user_access_logging_settings_arn,
        }

    @builtins.property
    def user_access_logging_settings_arn(self) -> builtins.str:
        '''The UserAccessLoggingSettingsArn of the UserAccessLoggingSettings resource.'''
        result = self._values.get("user_access_logging_settings_arn")
        assert result is not None, "Required property 'user_access_logging_settings_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserAccessLoggingSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesweb.UserSettingsReference",
    jsii_struct_bases=[],
    name_mapping={"user_settings_arn": "userSettingsArn"},
)
class UserSettingsReference:
    def __init__(self, *, user_settings_arn: builtins.str) -> None:
        '''A reference to a UserSettings resource.

        :param user_settings_arn: The UserSettingsArn of the UserSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesweb as interfaces_workspacesweb
            
            user_settings_reference = interfaces_workspacesweb.UserSettingsReference(
                user_settings_arn="userSettingsArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81697bb362c73df236f633996ec44c352ab35bdb7ad0f499d04e1d627cd2c7f3)
            check_type(argname="argument user_settings_arn", value=user_settings_arn, expected_type=type_hints["user_settings_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_settings_arn": user_settings_arn,
        }

    @builtins.property
    def user_settings_arn(self) -> builtins.str:
        '''The UserSettingsArn of the UserSettings resource.'''
        result = self._values.get("user_settings_arn")
        assert result is not None, "Required property 'user_settings_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BrowserSettingsReference",
    "DataProtectionSettingsReference",
    "IBrowserSettingsRef",
    "IDataProtectionSettingsRef",
    "IIdentityProviderRef",
    "IIpAccessSettingsRef",
    "INetworkSettingsRef",
    "IPortalRef",
    "ISessionLoggerRef",
    "ITrustStoreRef",
    "IUserAccessLoggingSettingsRef",
    "IUserSettingsRef",
    "IdentityProviderReference",
    "IpAccessSettingsReference",
    "NetworkSettingsReference",
    "PortalReference",
    "SessionLoggerReference",
    "TrustStoreReference",
    "UserAccessLoggingSettingsReference",
    "UserSettingsReference",
]

publication.publish()

def _typecheckingstub__0a86f83cb991212444d3914144c22ba1dc691d5dee8f106349739cab5ff64b4a(
    *,
    browser_settings_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1f3632e4487bac999312f4a7bf06ce08cb7b3d71d0411d0bb8a1b296dd3c57b(
    *,
    data_protection_settings_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d06a54ff8ceeaae4c4158181d934d8e147b1c9743c60c74bdf6fd682edcf3636(
    *,
    identity_provider_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83929b7ec7392cc5bbd9b90982729d0fd7528f39bc08e8d857f58293db8c397b(
    *,
    ip_access_settings_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b481c867b1f52384ef579bc94fecc53088b5d9b42cbf8fd48ae69a4f3eba7614(
    *,
    network_settings_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e663ea314aede92b25306c3859d2d29050477dc0a13e30bad8966d0295d92ddc(
    *,
    portal_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093e66dd03530c70c2cad4c0f448985c476bc2060565e5166b6df4c62767aa17(
    *,
    session_logger_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f89506317979fe315a43fa5d8074f96c94b1d554fda4754a3be13cf61c32164(
    *,
    trust_store_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d5e1a279ef19952e911a4b1d07cccfd213091ece112e6e4d62b76fd9fc991aa(
    *,
    user_access_logging_settings_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81697bb362c73df236f633996ec44c352ab35bdb7ad0f499d04e1d627cd2c7f3(
    *,
    user_settings_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBrowserSettingsRef, IDataProtectionSettingsRef, IIdentityProviderRef, IIpAccessSettingsRef, INetworkSettingsRef, IPortalRef, ISessionLoggerRef, ITrustStoreRef, IUserAccessLoggingSettingsRef, IUserSettingsRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
