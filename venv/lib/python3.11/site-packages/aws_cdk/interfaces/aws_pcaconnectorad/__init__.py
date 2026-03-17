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
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.ConnectorReference",
    jsii_struct_bases=[],
    name_mapping={"connector_arn": "connectorArn"},
)
class ConnectorReference:
    def __init__(self, *, connector_arn: builtins.str) -> None:
        '''A reference to a Connector resource.

        :param connector_arn: The ConnectorArn of the Connector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcaconnectorad as interfaces_pcaconnectorad
            
            connector_reference = interfaces_pcaconnectorad.ConnectorReference(
                connector_arn="connectorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d1a32b1d6d1ca3be3682baaef3a32efd9fc453025e9878f238308110af1f133)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
        }

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The ConnectorArn of the Connector resource.'''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.DirectoryRegistrationReference",
    jsii_struct_bases=[],
    name_mapping={"directory_registration_arn": "directoryRegistrationArn"},
)
class DirectoryRegistrationReference:
    def __init__(self, *, directory_registration_arn: builtins.str) -> None:
        '''A reference to a DirectoryRegistration resource.

        :param directory_registration_arn: The DirectoryRegistrationArn of the DirectoryRegistration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcaconnectorad as interfaces_pcaconnectorad
            
            directory_registration_reference = interfaces_pcaconnectorad.DirectoryRegistrationReference(
                directory_registration_arn="directoryRegistrationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c7b6b44d401574eab989f0757e03f54c33723634d2ac1605a8205baf9b6e223)
            check_type(argname="argument directory_registration_arn", value=directory_registration_arn, expected_type=type_hints["directory_registration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory_registration_arn": directory_registration_arn,
        }

    @builtins.property
    def directory_registration_arn(self) -> builtins.str:
        '''The DirectoryRegistrationArn of the DirectoryRegistration resource.'''
        result = self._values.get("directory_registration_arn")
        assert result is not None, "Required property 'directory_registration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectoryRegistrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.IConnectorRef")
class IConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        ...


class _IConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcaconnectorad.IConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorReference", jsii.get(self, "connectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorRef).__jsii_proxy_class__ = lambda : _IConnectorRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.IDirectoryRegistrationRef"
)
class IDirectoryRegistrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DirectoryRegistration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="directoryRegistrationRef")
    def directory_registration_ref(self) -> "DirectoryRegistrationReference":
        '''(experimental) A reference to a DirectoryRegistration resource.

        :stability: experimental
        '''
        ...


class _IDirectoryRegistrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DirectoryRegistration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcaconnectorad.IDirectoryRegistrationRef"

    @builtins.property
    @jsii.member(jsii_name="directoryRegistrationRef")
    def directory_registration_ref(self) -> "DirectoryRegistrationReference":
        '''(experimental) A reference to a DirectoryRegistration resource.

        :stability: experimental
        '''
        return typing.cast("DirectoryRegistrationReference", jsii.get(self, "directoryRegistrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDirectoryRegistrationRef).__jsii_proxy_class__ = lambda : _IDirectoryRegistrationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.IServicePrincipalNameRef"
)
class IServicePrincipalNameRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServicePrincipalName.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalNameRef")
    def service_principal_name_ref(self) -> "ServicePrincipalNameReference":
        '''(experimental) A reference to a ServicePrincipalName resource.

        :stability: experimental
        '''
        ...


class _IServicePrincipalNameRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServicePrincipalName.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcaconnectorad.IServicePrincipalNameRef"

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalNameRef")
    def service_principal_name_ref(self) -> "ServicePrincipalNameReference":
        '''(experimental) A reference to a ServicePrincipalName resource.

        :stability: experimental
        '''
        return typing.cast("ServicePrincipalNameReference", jsii.get(self, "servicePrincipalNameRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServicePrincipalNameRef).__jsii_proxy_class__ = lambda : _IServicePrincipalNameRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.ITemplateGroupAccessControlEntryRef"
)
class ITemplateGroupAccessControlEntryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TemplateGroupAccessControlEntry.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="templateGroupAccessControlEntryRef")
    def template_group_access_control_entry_ref(
        self,
    ) -> "TemplateGroupAccessControlEntryReference":
        '''(experimental) A reference to a TemplateGroupAccessControlEntry resource.

        :stability: experimental
        '''
        ...


class _ITemplateGroupAccessControlEntryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TemplateGroupAccessControlEntry.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcaconnectorad.ITemplateGroupAccessControlEntryRef"

    @builtins.property
    @jsii.member(jsii_name="templateGroupAccessControlEntryRef")
    def template_group_access_control_entry_ref(
        self,
    ) -> "TemplateGroupAccessControlEntryReference":
        '''(experimental) A reference to a TemplateGroupAccessControlEntry resource.

        :stability: experimental
        '''
        return typing.cast("TemplateGroupAccessControlEntryReference", jsii.get(self, "templateGroupAccessControlEntryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITemplateGroupAccessControlEntryRef).__jsii_proxy_class__ = lambda : _ITemplateGroupAccessControlEntryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.ITemplateRef")
class ITemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Template.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="templateRef")
    def template_ref(self) -> "TemplateReference":
        '''(experimental) A reference to a Template resource.

        :stability: experimental
        '''
        ...


class _ITemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Template.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcaconnectorad.ITemplateRef"

    @builtins.property
    @jsii.member(jsii_name="templateRef")
    def template_ref(self) -> "TemplateReference":
        '''(experimental) A reference to a Template resource.

        :stability: experimental
        '''
        return typing.cast("TemplateReference", jsii.get(self, "templateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITemplateRef).__jsii_proxy_class__ = lambda : _ITemplateRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.ServicePrincipalNameReference",
    jsii_struct_bases=[],
    name_mapping={
        "connector_arn": "connectorArn",
        "directory_registration_arn": "directoryRegistrationArn",
    },
)
class ServicePrincipalNameReference:
    def __init__(
        self,
        *,
        connector_arn: builtins.str,
        directory_registration_arn: builtins.str,
    ) -> None:
        '''A reference to a ServicePrincipalName resource.

        :param connector_arn: The ConnectorArn of the ServicePrincipalName resource.
        :param directory_registration_arn: The DirectoryRegistrationArn of the ServicePrincipalName resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcaconnectorad as interfaces_pcaconnectorad
            
            service_principal_name_reference = interfaces_pcaconnectorad.ServicePrincipalNameReference(
                connector_arn="connectorArn",
                directory_registration_arn="directoryRegistrationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b75796014a5cba8be51c59129fbfd1def406f346b9f1c49e9376788ecea9dfd)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
            check_type(argname="argument directory_registration_arn", value=directory_registration_arn, expected_type=type_hints["directory_registration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
            "directory_registration_arn": directory_registration_arn,
        }

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The ConnectorArn of the ServicePrincipalName resource.'''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_registration_arn(self) -> builtins.str:
        '''The DirectoryRegistrationArn of the ServicePrincipalName resource.'''
        result = self._values.get("directory_registration_arn")
        assert result is not None, "Required property 'directory_registration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServicePrincipalNameReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.TemplateGroupAccessControlEntryReference",
    jsii_struct_bases=[],
    name_mapping={
        "group_security_identifier": "groupSecurityIdentifier",
        "template_arn": "templateArn",
    },
)
class TemplateGroupAccessControlEntryReference:
    def __init__(
        self,
        *,
        group_security_identifier: builtins.str,
        template_arn: builtins.str,
    ) -> None:
        '''A reference to a TemplateGroupAccessControlEntry resource.

        :param group_security_identifier: The GroupSecurityIdentifier of the TemplateGroupAccessControlEntry resource.
        :param template_arn: The TemplateArn of the TemplateGroupAccessControlEntry resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcaconnectorad as interfaces_pcaconnectorad
            
            template_group_access_control_entry_reference = interfaces_pcaconnectorad.TemplateGroupAccessControlEntryReference(
                group_security_identifier="groupSecurityIdentifier",
                template_arn="templateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ead2c8d1dea7b8b359918535d23163e7659b4869b50adcb24b1650b4604ee69)
            check_type(argname="argument group_security_identifier", value=group_security_identifier, expected_type=type_hints["group_security_identifier"])
            check_type(argname="argument template_arn", value=template_arn, expected_type=type_hints["template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_security_identifier": group_security_identifier,
            "template_arn": template_arn,
        }

    @builtins.property
    def group_security_identifier(self) -> builtins.str:
        '''The GroupSecurityIdentifier of the TemplateGroupAccessControlEntry resource.'''
        result = self._values.get("group_security_identifier")
        assert result is not None, "Required property 'group_security_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_arn(self) -> builtins.str:
        '''The TemplateArn of the TemplateGroupAccessControlEntry resource.'''
        result = self._values.get("template_arn")
        assert result is not None, "Required property 'template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateGroupAccessControlEntryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorad.TemplateReference",
    jsii_struct_bases=[],
    name_mapping={"template_arn": "templateArn"},
)
class TemplateReference:
    def __init__(self, *, template_arn: builtins.str) -> None:
        '''A reference to a Template resource.

        :param template_arn: The TemplateArn of the Template resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcaconnectorad as interfaces_pcaconnectorad
            
            template_reference = interfaces_pcaconnectorad.TemplateReference(
                template_arn="templateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6e1f7be54389e3096835c0181c73c4e969a1a521a907c6689ea0427c0971c67)
            check_type(argname="argument template_arn", value=template_arn, expected_type=type_hints["template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_arn": template_arn,
        }

    @builtins.property
    def template_arn(self) -> builtins.str:
        '''The TemplateArn of the Template resource.'''
        result = self._values.get("template_arn")
        assert result is not None, "Required property 'template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConnectorReference",
    "DirectoryRegistrationReference",
    "IConnectorRef",
    "IDirectoryRegistrationRef",
    "IServicePrincipalNameRef",
    "ITemplateGroupAccessControlEntryRef",
    "ITemplateRef",
    "ServicePrincipalNameReference",
    "TemplateGroupAccessControlEntryReference",
    "TemplateReference",
]

publication.publish()

def _typecheckingstub__5d1a32b1d6d1ca3be3682baaef3a32efd9fc453025e9878f238308110af1f133(
    *,
    connector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c7b6b44d401574eab989f0757e03f54c33723634d2ac1605a8205baf9b6e223(
    *,
    directory_registration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b75796014a5cba8be51c59129fbfd1def406f346b9f1c49e9376788ecea9dfd(
    *,
    connector_arn: builtins.str,
    directory_registration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ead2c8d1dea7b8b359918535d23163e7659b4869b50adcb24b1650b4604ee69(
    *,
    group_security_identifier: builtins.str,
    template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e1f7be54389e3096835c0181c73c4e969a1a521a907c6689ea0427c0971c67(
    *,
    template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectorRef, IDirectoryRegistrationRef, IServicePrincipalNameRef, ITemplateGroupAccessControlEntryRef, ITemplateRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
