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
    jsii_type="aws-cdk-lib.interfaces.aws_macie.AllowListReference",
    jsii_struct_bases=[],
    name_mapping={"allow_list_arn": "allowListArn", "allow_list_id": "allowListId"},
)
class AllowListReference:
    def __init__(
        self,
        *,
        allow_list_arn: builtins.str,
        allow_list_id: builtins.str,
    ) -> None:
        '''A reference to a AllowList resource.

        :param allow_list_arn: The ARN of the AllowList resource.
        :param allow_list_id: The Id of the AllowList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_macie as interfaces_macie
            
            allow_list_reference = interfaces_macie.AllowListReference(
                allow_list_arn="allowListArn",
                allow_list_id="allowListId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54e6e5f8846d73a84a985bd3386ca6287c1449afc07d186db83ed617426ef97e)
            check_type(argname="argument allow_list_arn", value=allow_list_arn, expected_type=type_hints["allow_list_arn"])
            check_type(argname="argument allow_list_id", value=allow_list_id, expected_type=type_hints["allow_list_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allow_list_arn": allow_list_arn,
            "allow_list_id": allow_list_id,
        }

    @builtins.property
    def allow_list_arn(self) -> builtins.str:
        '''The ARN of the AllowList resource.'''
        result = self._values.get("allow_list_arn")
        assert result is not None, "Required property 'allow_list_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_list_id(self) -> builtins.str:
        '''The Id of the AllowList resource.'''
        result = self._values.get("allow_list_id")
        assert result is not None, "Required property 'allow_list_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AllowListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_macie.CustomDataIdentifierReference",
    jsii_struct_bases=[],
    name_mapping={
        "custom_data_identifier_arn": "customDataIdentifierArn",
        "custom_data_identifier_id": "customDataIdentifierId",
    },
)
class CustomDataIdentifierReference:
    def __init__(
        self,
        *,
        custom_data_identifier_arn: builtins.str,
        custom_data_identifier_id: builtins.str,
    ) -> None:
        '''A reference to a CustomDataIdentifier resource.

        :param custom_data_identifier_arn: The ARN of the CustomDataIdentifier resource.
        :param custom_data_identifier_id: The Id of the CustomDataIdentifier resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_macie as interfaces_macie
            
            custom_data_identifier_reference = interfaces_macie.CustomDataIdentifierReference(
                custom_data_identifier_arn="customDataIdentifierArn",
                custom_data_identifier_id="customDataIdentifierId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea2943911aabf217701b1b1009bb5bdda42d1386119897350068c76b6707a82d)
            check_type(argname="argument custom_data_identifier_arn", value=custom_data_identifier_arn, expected_type=type_hints["custom_data_identifier_arn"])
            check_type(argname="argument custom_data_identifier_id", value=custom_data_identifier_id, expected_type=type_hints["custom_data_identifier_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_data_identifier_arn": custom_data_identifier_arn,
            "custom_data_identifier_id": custom_data_identifier_id,
        }

    @builtins.property
    def custom_data_identifier_arn(self) -> builtins.str:
        '''The ARN of the CustomDataIdentifier resource.'''
        result = self._values.get("custom_data_identifier_arn")
        assert result is not None, "Required property 'custom_data_identifier_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_data_identifier_id(self) -> builtins.str:
        '''The Id of the CustomDataIdentifier resource.'''
        result = self._values.get("custom_data_identifier_id")
        assert result is not None, "Required property 'custom_data_identifier_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomDataIdentifierReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_macie.FindingsFilterReference",
    jsii_struct_bases=[],
    name_mapping={
        "findings_filter_arn": "findingsFilterArn",
        "findings_filter_id": "findingsFilterId",
    },
)
class FindingsFilterReference:
    def __init__(
        self,
        *,
        findings_filter_arn: builtins.str,
        findings_filter_id: builtins.str,
    ) -> None:
        '''A reference to a FindingsFilter resource.

        :param findings_filter_arn: The ARN of the FindingsFilter resource.
        :param findings_filter_id: The Id of the FindingsFilter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_macie as interfaces_macie
            
            findings_filter_reference = interfaces_macie.FindingsFilterReference(
                findings_filter_arn="findingsFilterArn",
                findings_filter_id="findingsFilterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24174987f734b706b6e1c3dd4f221c1363636e84df59dcd187b49d9555c19aac)
            check_type(argname="argument findings_filter_arn", value=findings_filter_arn, expected_type=type_hints["findings_filter_arn"])
            check_type(argname="argument findings_filter_id", value=findings_filter_id, expected_type=type_hints["findings_filter_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "findings_filter_arn": findings_filter_arn,
            "findings_filter_id": findings_filter_id,
        }

    @builtins.property
    def findings_filter_arn(self) -> builtins.str:
        '''The ARN of the FindingsFilter resource.'''
        result = self._values.get("findings_filter_arn")
        assert result is not None, "Required property 'findings_filter_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def findings_filter_id(self) -> builtins.str:
        '''The Id of the FindingsFilter resource.'''
        result = self._values.get("findings_filter_id")
        assert result is not None, "Required property 'findings_filter_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FindingsFilterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_macie.IAllowListRef")
class IAllowListRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AllowList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="allowListRef")
    def allow_list_ref(self) -> "AllowListReference":
        '''(experimental) A reference to a AllowList resource.

        :stability: experimental
        '''
        ...


class _IAllowListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AllowList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_macie.IAllowListRef"

    @builtins.property
    @jsii.member(jsii_name="allowListRef")
    def allow_list_ref(self) -> "AllowListReference":
        '''(experimental) A reference to a AllowList resource.

        :stability: experimental
        '''
        return typing.cast("AllowListReference", jsii.get(self, "allowListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAllowListRef).__jsii_proxy_class__ = lambda : _IAllowListRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_macie.ICustomDataIdentifierRef")
class ICustomDataIdentifierRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomDataIdentifier.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customDataIdentifierRef")
    def custom_data_identifier_ref(self) -> "CustomDataIdentifierReference":
        '''(experimental) A reference to a CustomDataIdentifier resource.

        :stability: experimental
        '''
        ...


class _ICustomDataIdentifierRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomDataIdentifier.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_macie.ICustomDataIdentifierRef"

    @builtins.property
    @jsii.member(jsii_name="customDataIdentifierRef")
    def custom_data_identifier_ref(self) -> "CustomDataIdentifierReference":
        '''(experimental) A reference to a CustomDataIdentifier resource.

        :stability: experimental
        '''
        return typing.cast("CustomDataIdentifierReference", jsii.get(self, "customDataIdentifierRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomDataIdentifierRef).__jsii_proxy_class__ = lambda : _ICustomDataIdentifierRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_macie.IFindingsFilterRef")
class IFindingsFilterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FindingsFilter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="findingsFilterRef")
    def findings_filter_ref(self) -> "FindingsFilterReference":
        '''(experimental) A reference to a FindingsFilter resource.

        :stability: experimental
        '''
        ...


class _IFindingsFilterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FindingsFilter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_macie.IFindingsFilterRef"

    @builtins.property
    @jsii.member(jsii_name="findingsFilterRef")
    def findings_filter_ref(self) -> "FindingsFilterReference":
        '''(experimental) A reference to a FindingsFilter resource.

        :stability: experimental
        '''
        return typing.cast("FindingsFilterReference", jsii.get(self, "findingsFilterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFindingsFilterRef).__jsii_proxy_class__ = lambda : _IFindingsFilterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_macie.ISessionRef")
class ISessionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Session.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sessionRef")
    def session_ref(self) -> "SessionReference":
        '''(experimental) A reference to a Session resource.

        :stability: experimental
        '''
        ...


class _ISessionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Session.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_macie.ISessionRef"

    @builtins.property
    @jsii.member(jsii_name="sessionRef")
    def session_ref(self) -> "SessionReference":
        '''(experimental) A reference to a Session resource.

        :stability: experimental
        '''
        return typing.cast("SessionReference", jsii.get(self, "sessionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISessionRef).__jsii_proxy_class__ = lambda : _ISessionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_macie.SessionReference",
    jsii_struct_bases=[],
    name_mapping={"aws_account_id": "awsAccountId"},
)
class SessionReference:
    def __init__(self, *, aws_account_id: builtins.str) -> None:
        '''A reference to a Session resource.

        :param aws_account_id: The AwsAccountId of the Session resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_macie as interfaces_macie
            
            session_reference = interfaces_macie.SessionReference(
                aws_account_id="awsAccountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece2bd8504f31fceb52c2611c4b61cc2f5451f6ed5b3791c5282ae7168572620)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Session resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SessionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AllowListReference",
    "CustomDataIdentifierReference",
    "FindingsFilterReference",
    "IAllowListRef",
    "ICustomDataIdentifierRef",
    "IFindingsFilterRef",
    "ISessionRef",
    "SessionReference",
]

publication.publish()

def _typecheckingstub__54e6e5f8846d73a84a985bd3386ca6287c1449afc07d186db83ed617426ef97e(
    *,
    allow_list_arn: builtins.str,
    allow_list_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea2943911aabf217701b1b1009bb5bdda42d1386119897350068c76b6707a82d(
    *,
    custom_data_identifier_arn: builtins.str,
    custom_data_identifier_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24174987f734b706b6e1c3dd4f221c1363636e84df59dcd187b49d9555c19aac(
    *,
    findings_filter_arn: builtins.str,
    findings_filter_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece2bd8504f31fceb52c2611c4b61cc2f5451f6ed5b3791c5282ae7168572620(
    *,
    aws_account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAllowListRef, ICustomDataIdentifierRef, IFindingsFilterRef, ISessionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
