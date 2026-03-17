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
    jsii_type="aws-cdk-lib.interfaces.aws_transfer.AgreementReference",
    jsii_struct_bases=[],
    name_mapping={
        "agreement_arn": "agreementArn",
        "agreement_id": "agreementId",
        "server_id": "serverId",
    },
)
class AgreementReference:
    def __init__(
        self,
        *,
        agreement_arn: builtins.str,
        agreement_id: builtins.str,
        server_id: builtins.str,
    ) -> None:
        '''A reference to a Agreement resource.

        :param agreement_arn: The ARN of the Agreement resource.
        :param agreement_id: The AgreementId of the Agreement resource.
        :param server_id: The ServerId of the Agreement resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transfer as interfaces_transfer
            
            agreement_reference = interfaces_transfer.AgreementReference(
                agreement_arn="agreementArn",
                agreement_id="agreementId",
                server_id="serverId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0030237a7d5a23fbc6eeb6e8de52083d7dad7bca8c74b1ce8274ef7bc716f87b)
            check_type(argname="argument agreement_arn", value=agreement_arn, expected_type=type_hints["agreement_arn"])
            check_type(argname="argument agreement_id", value=agreement_id, expected_type=type_hints["agreement_id"])
            check_type(argname="argument server_id", value=server_id, expected_type=type_hints["server_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agreement_arn": agreement_arn,
            "agreement_id": agreement_id,
            "server_id": server_id,
        }

    @builtins.property
    def agreement_arn(self) -> builtins.str:
        '''The ARN of the Agreement resource.'''
        result = self._values.get("agreement_arn")
        assert result is not None, "Required property 'agreement_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agreement_id(self) -> builtins.str:
        '''The AgreementId of the Agreement resource.'''
        result = self._values.get("agreement_id")
        assert result is not None, "Required property 'agreement_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_id(self) -> builtins.str:
        '''The ServerId of the Agreement resource.'''
        result = self._values.get("server_id")
        assert result is not None, "Required property 'server_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgreementReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transfer.CertificateReference",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_arn": "certificateArn",
        "certificate_id": "certificateId",
    },
)
class CertificateReference:
    def __init__(
        self,
        *,
        certificate_arn: builtins.str,
        certificate_id: builtins.str,
    ) -> None:
        '''A reference to a Certificate resource.

        :param certificate_arn: The ARN of the Certificate resource.
        :param certificate_id: The CertificateId of the Certificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transfer as interfaces_transfer
            
            certificate_reference = interfaces_transfer.CertificateReference(
                certificate_arn="certificateArn",
                certificate_id="certificateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__caf271284d683188649cf64ad00dc777fdd06d3fda99e93a85cf306ad81582b1)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument certificate_id", value=certificate_id, expected_type=type_hints["certificate_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
            "certificate_id": certificate_id,
        }

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''The ARN of the Certificate resource.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_id(self) -> builtins.str:
        '''The CertificateId of the Certificate resource.'''
        result = self._values.get("certificate_id")
        assert result is not None, "Required property 'certificate_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transfer.ConnectorReference",
    jsii_struct_bases=[],
    name_mapping={"connector_arn": "connectorArn", "connector_id": "connectorId"},
)
class ConnectorReference:
    def __init__(
        self,
        *,
        connector_arn: builtins.str,
        connector_id: builtins.str,
    ) -> None:
        '''A reference to a Connector resource.

        :param connector_arn: The ARN of the Connector resource.
        :param connector_id: The ConnectorId of the Connector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transfer as interfaces_transfer
            
            connector_reference = interfaces_transfer.ConnectorReference(
                connector_arn="connectorArn",
                connector_id="connectorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974da67127b3da5e370496e33bb89b2173fc2dbbd88f7e8a3b9eb2c7cfe2e07c)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
            check_type(argname="argument connector_id", value=connector_id, expected_type=type_hints["connector_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
            "connector_id": connector_id,
        }

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The ARN of the Connector resource.'''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_id(self) -> builtins.str:
        '''The ConnectorId of the Connector resource.'''
        result = self._values.get("connector_id")
        assert result is not None, "Required property 'connector_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transfer.IAgreementRef")
class IAgreementRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Agreement.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agreementRef")
    def agreement_ref(self) -> "AgreementReference":
        '''(experimental) A reference to a Agreement resource.

        :stability: experimental
        '''
        ...


class _IAgreementRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Agreement.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transfer.IAgreementRef"

    @builtins.property
    @jsii.member(jsii_name="agreementRef")
    def agreement_ref(self) -> "AgreementReference":
        '''(experimental) A reference to a Agreement resource.

        :stability: experimental
        '''
        return typing.cast("AgreementReference", jsii.get(self, "agreementRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgreementRef).__jsii_proxy_class__ = lambda : _IAgreementRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transfer.ICertificateRef")
class ICertificateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Certificate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        ...


class _ICertificateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Certificate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transfer.ICertificateRef"

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        return typing.cast("CertificateReference", jsii.get(self, "certificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateRef).__jsii_proxy_class__ = lambda : _ICertificateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transfer.IConnectorRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transfer.IConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorReference", jsii.get(self, "connectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorRef).__jsii_proxy_class__ = lambda : _IConnectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transfer.IProfileRef")
class IProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Profile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "ProfileReference":
        '''(experimental) A reference to a Profile resource.

        :stability: experimental
        '''
        ...


class _IProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Profile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transfer.IProfileRef"

    @builtins.property
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "ProfileReference":
        '''(experimental) A reference to a Profile resource.

        :stability: experimental
        '''
        return typing.cast("ProfileReference", jsii.get(self, "profileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfileRef).__jsii_proxy_class__ = lambda : _IProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transfer.IServerRef")
class IServerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Server.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serverRef")
    def server_ref(self) -> "ServerReference":
        '''(experimental) A reference to a Server resource.

        :stability: experimental
        '''
        ...


class _IServerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Server.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transfer.IServerRef"

    @builtins.property
    @jsii.member(jsii_name="serverRef")
    def server_ref(self) -> "ServerReference":
        '''(experimental) A reference to a Server resource.

        :stability: experimental
        '''
        return typing.cast("ServerReference", jsii.get(self, "serverRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServerRef).__jsii_proxy_class__ = lambda : _IServerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transfer.IUserRef")
class IUserRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a User.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "UserReference":
        '''(experimental) A reference to a User resource.

        :stability: experimental
        '''
        ...


class _IUserRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a User.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transfer.IUserRef"

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "UserReference":
        '''(experimental) A reference to a User resource.

        :stability: experimental
        '''
        return typing.cast("UserReference", jsii.get(self, "userRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserRef).__jsii_proxy_class__ = lambda : _IUserRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transfer.IWebAppRef")
class IWebAppRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WebApp.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="webAppRef")
    def web_app_ref(self) -> "WebAppReference":
        '''(experimental) A reference to a WebApp resource.

        :stability: experimental
        '''
        ...


class _IWebAppRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WebApp.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transfer.IWebAppRef"

    @builtins.property
    @jsii.member(jsii_name="webAppRef")
    def web_app_ref(self) -> "WebAppReference":
        '''(experimental) A reference to a WebApp resource.

        :stability: experimental
        '''
        return typing.cast("WebAppReference", jsii.get(self, "webAppRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWebAppRef).__jsii_proxy_class__ = lambda : _IWebAppRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_transfer.IWorkflowRef")
class IWorkflowRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        ...


class _IWorkflowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_transfer.IWorkflowRef"

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        return typing.cast("WorkflowReference", jsii.get(self, "workflowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkflowRef).__jsii_proxy_class__ = lambda : _IWorkflowRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transfer.ProfileReference",
    jsii_struct_bases=[],
    name_mapping={"profile_arn": "profileArn", "profile_id": "profileId"},
)
class ProfileReference:
    def __init__(self, *, profile_arn: builtins.str, profile_id: builtins.str) -> None:
        '''A reference to a Profile resource.

        :param profile_arn: The ARN of the Profile resource.
        :param profile_id: The ProfileId of the Profile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transfer as interfaces_transfer
            
            profile_reference = interfaces_transfer.ProfileReference(
                profile_arn="profileArn",
                profile_id="profileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__310c9dc04eebf93efed779abf1d912d9070e65e28308fc060d53c77d9936f275)
            check_type(argname="argument profile_arn", value=profile_arn, expected_type=type_hints["profile_arn"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile_arn": profile_arn,
            "profile_id": profile_id,
        }

    @builtins.property
    def profile_arn(self) -> builtins.str:
        '''The ARN of the Profile resource.'''
        result = self._values.get("profile_arn")
        assert result is not None, "Required property 'profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''The ProfileId of the Profile resource.'''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transfer.ServerReference",
    jsii_struct_bases=[],
    name_mapping={"server_arn": "serverArn"},
)
class ServerReference:
    def __init__(self, *, server_arn: builtins.str) -> None:
        '''A reference to a Server resource.

        :param server_arn: The Arn of the Server resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transfer as interfaces_transfer
            
            server_reference = interfaces_transfer.ServerReference(
                server_arn="serverArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a0c78b5b069ffd6d9dc14cbb47ea17972d3098d9cff0861f81d0355e995e1fd)
            check_type(argname="argument server_arn", value=server_arn, expected_type=type_hints["server_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "server_arn": server_arn,
        }

    @builtins.property
    def server_arn(self) -> builtins.str:
        '''The Arn of the Server resource.'''
        result = self._values.get("server_arn")
        assert result is not None, "Required property 'server_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transfer.UserReference",
    jsii_struct_bases=[],
    name_mapping={"user_arn": "userArn"},
)
class UserReference:
    def __init__(self, *, user_arn: builtins.str) -> None:
        '''A reference to a User resource.

        :param user_arn: The Arn of the User resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transfer as interfaces_transfer
            
            user_reference = interfaces_transfer.UserReference(
                user_arn="userArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b87070aabdbc0663833c9b86c2d1fbf0d8f13ada9783ebfcbe5d4d1f2935c0cd)
            check_type(argname="argument user_arn", value=user_arn, expected_type=type_hints["user_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_arn": user_arn,
        }

    @builtins.property
    def user_arn(self) -> builtins.str:
        '''The Arn of the User resource.'''
        result = self._values.get("user_arn")
        assert result is not None, "Required property 'user_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transfer.WebAppReference",
    jsii_struct_bases=[],
    name_mapping={"web_app_arn": "webAppArn"},
)
class WebAppReference:
    def __init__(self, *, web_app_arn: builtins.str) -> None:
        '''A reference to a WebApp resource.

        :param web_app_arn: The Arn of the WebApp resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transfer as interfaces_transfer
            
            web_app_reference = interfaces_transfer.WebAppReference(
                web_app_arn="webAppArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48f680666c5f554b9d06c749e3a4df45b0e28f45712ae3a502b2d40c23b41201)
            check_type(argname="argument web_app_arn", value=web_app_arn, expected_type=type_hints["web_app_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "web_app_arn": web_app_arn,
        }

    @builtins.property
    def web_app_arn(self) -> builtins.str:
        '''The Arn of the WebApp resource.'''
        result = self._values.get("web_app_arn")
        assert result is not None, "Required property 'web_app_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebAppReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_transfer.WorkflowReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_arn": "workflowArn", "workflow_id": "workflowId"},
)
class WorkflowReference:
    def __init__(
        self,
        *,
        workflow_arn: builtins.str,
        workflow_id: builtins.str,
    ) -> None:
        '''A reference to a Workflow resource.

        :param workflow_arn: The ARN of the Workflow resource.
        :param workflow_id: The WorkflowId of the Workflow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_transfer as interfaces_transfer
            
            workflow_reference = interfaces_transfer.WorkflowReference(
                workflow_arn="workflowArn",
                workflow_id="workflowId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64712cbe947d7c5d260d231d036ee92b38e6c3920bdac81ff3856ad3d6f82d90)
            check_type(argname="argument workflow_arn", value=workflow_arn, expected_type=type_hints["workflow_arn"])
            check_type(argname="argument workflow_id", value=workflow_id, expected_type=type_hints["workflow_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_arn": workflow_arn,
            "workflow_id": workflow_id,
        }

    @builtins.property
    def workflow_arn(self) -> builtins.str:
        '''The ARN of the Workflow resource.'''
        result = self._values.get("workflow_arn")
        assert result is not None, "Required property 'workflow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workflow_id(self) -> builtins.str:
        '''The WorkflowId of the Workflow resource.'''
        result = self._values.get("workflow_id")
        assert result is not None, "Required property 'workflow_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AgreementReference",
    "CertificateReference",
    "ConnectorReference",
    "IAgreementRef",
    "ICertificateRef",
    "IConnectorRef",
    "IProfileRef",
    "IServerRef",
    "IUserRef",
    "IWebAppRef",
    "IWorkflowRef",
    "ProfileReference",
    "ServerReference",
    "UserReference",
    "WebAppReference",
    "WorkflowReference",
]

publication.publish()

def _typecheckingstub__0030237a7d5a23fbc6eeb6e8de52083d7dad7bca8c74b1ce8274ef7bc716f87b(
    *,
    agreement_arn: builtins.str,
    agreement_id: builtins.str,
    server_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caf271284d683188649cf64ad00dc777fdd06d3fda99e93a85cf306ad81582b1(
    *,
    certificate_arn: builtins.str,
    certificate_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974da67127b3da5e370496e33bb89b2173fc2dbbd88f7e8a3b9eb2c7cfe2e07c(
    *,
    connector_arn: builtins.str,
    connector_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__310c9dc04eebf93efed779abf1d912d9070e65e28308fc060d53c77d9936f275(
    *,
    profile_arn: builtins.str,
    profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0c78b5b069ffd6d9dc14cbb47ea17972d3098d9cff0861f81d0355e995e1fd(
    *,
    server_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b87070aabdbc0663833c9b86c2d1fbf0d8f13ada9783ebfcbe5d4d1f2935c0cd(
    *,
    user_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48f680666c5f554b9d06c749e3a4df45b0e28f45712ae3a502b2d40c23b41201(
    *,
    web_app_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64712cbe947d7c5d260d231d036ee92b38e6c3920bdac81ff3856ad3d6f82d90(
    *,
    workflow_arn: builtins.str,
    workflow_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAgreementRef, ICertificateRef, IConnectorRef, IProfileRef, IServerRef, IUserRef, IWebAppRef, IWorkflowRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
