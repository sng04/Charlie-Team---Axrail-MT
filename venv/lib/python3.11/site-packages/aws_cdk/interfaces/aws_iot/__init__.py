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
    jsii_type="aws-cdk-lib.interfaces.aws_iot.AccountAuditConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class AccountAuditConfigurationReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a AccountAuditConfiguration resource.

        :param account_id: The AccountId of the AccountAuditConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            account_audit_configuration_reference = interfaces_iot.AccountAuditConfigurationReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__146e26f046c491c18c156078309a07ab43070e0aa679f424eabb2687e3ad85d0)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the AccountAuditConfiguration resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountAuditConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.AuthorizerReference",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_arn": "authorizerArn",
        "authorizer_name": "authorizerName",
    },
)
class AuthorizerReference:
    def __init__(
        self,
        *,
        authorizer_arn: builtins.str,
        authorizer_name: builtins.str,
    ) -> None:
        '''A reference to a Authorizer resource.

        :param authorizer_arn: The ARN of the Authorizer resource.
        :param authorizer_name: The AuthorizerName of the Authorizer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            authorizer_reference = interfaces_iot.AuthorizerReference(
                authorizer_arn="authorizerArn",
                authorizer_name="authorizerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a589da36a530a5f515e3fd2fa870b4aa7cab41b13bb204655a59aed307070a1)
            check_type(argname="argument authorizer_arn", value=authorizer_arn, expected_type=type_hints["authorizer_arn"])
            check_type(argname="argument authorizer_name", value=authorizer_name, expected_type=type_hints["authorizer_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorizer_arn": authorizer_arn,
            "authorizer_name": authorizer_name,
        }

    @builtins.property
    def authorizer_arn(self) -> builtins.str:
        '''The ARN of the Authorizer resource.'''
        result = self._values.get("authorizer_arn")
        assert result is not None, "Required property 'authorizer_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_name(self) -> builtins.str:
        '''The AuthorizerName of the Authorizer resource.'''
        result = self._values.get("authorizer_name")
        assert result is not None, "Required property 'authorizer_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.BillingGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "billing_group_arn": "billingGroupArn",
        "billing_group_name": "billingGroupName",
    },
)
class BillingGroupReference:
    def __init__(
        self,
        *,
        billing_group_arn: builtins.str,
        billing_group_name: builtins.str,
    ) -> None:
        '''A reference to a BillingGroup resource.

        :param billing_group_arn: The ARN of the BillingGroup resource.
        :param billing_group_name: The BillingGroupName of the BillingGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            billing_group_reference = interfaces_iot.BillingGroupReference(
                billing_group_arn="billingGroupArn",
                billing_group_name="billingGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9703280c049fd51220a0f708d3432e0c796ca6ec022914d413a76a17b8f3a4f0)
            check_type(argname="argument billing_group_arn", value=billing_group_arn, expected_type=type_hints["billing_group_arn"])
            check_type(argname="argument billing_group_name", value=billing_group_name, expected_type=type_hints["billing_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "billing_group_arn": billing_group_arn,
            "billing_group_name": billing_group_name,
        }

    @builtins.property
    def billing_group_arn(self) -> builtins.str:
        '''The ARN of the BillingGroup resource.'''
        result = self._values.get("billing_group_arn")
        assert result is not None, "Required property 'billing_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def billing_group_name(self) -> builtins.str:
        '''The BillingGroupName of the BillingGroup resource.'''
        result = self._values.get("billing_group_name")
        assert result is not None, "Required property 'billing_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.CACertificateReference",
    jsii_struct_bases=[],
    name_mapping={
        "ca_certificate_arn": "caCertificateArn",
        "ca_certificate_id": "caCertificateId",
    },
)
class CACertificateReference:
    def __init__(
        self,
        *,
        ca_certificate_arn: builtins.str,
        ca_certificate_id: builtins.str,
    ) -> None:
        '''A reference to a CACertificate resource.

        :param ca_certificate_arn: The ARN of the CACertificate resource.
        :param ca_certificate_id: The Id of the CACertificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            c_aCertificate_reference = interfaces_iot.CACertificateReference(
                ca_certificate_arn="caCertificateArn",
                ca_certificate_id="caCertificateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85bd9181b7bb427b113fea2b8232f3f1f865da0f77891a59319ebd98727b69e2)
            check_type(argname="argument ca_certificate_arn", value=ca_certificate_arn, expected_type=type_hints["ca_certificate_arn"])
            check_type(argname="argument ca_certificate_id", value=ca_certificate_id, expected_type=type_hints["ca_certificate_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ca_certificate_arn": ca_certificate_arn,
            "ca_certificate_id": ca_certificate_id,
        }

    @builtins.property
    def ca_certificate_arn(self) -> builtins.str:
        '''The ARN of the CACertificate resource.'''
        result = self._values.get("ca_certificate_arn")
        assert result is not None, "Required property 'ca_certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ca_certificate_id(self) -> builtins.str:
        '''The Id of the CACertificate resource.'''
        result = self._values.get("ca_certificate_id")
        assert result is not None, "Required property 'ca_certificate_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CACertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.CertificateProviderReference",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_provider_arn": "certificateProviderArn",
        "certificate_provider_name": "certificateProviderName",
    },
)
class CertificateProviderReference:
    def __init__(
        self,
        *,
        certificate_provider_arn: builtins.str,
        certificate_provider_name: builtins.str,
    ) -> None:
        '''A reference to a CertificateProvider resource.

        :param certificate_provider_arn: The ARN of the CertificateProvider resource.
        :param certificate_provider_name: The CertificateProviderName of the CertificateProvider resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            certificate_provider_reference = interfaces_iot.CertificateProviderReference(
                certificate_provider_arn="certificateProviderArn",
                certificate_provider_name="certificateProviderName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c7ece71d0f471a8be87b66e2a7c9c527cee538e2a3927e0c9a8d36386fc71d0)
            check_type(argname="argument certificate_provider_arn", value=certificate_provider_arn, expected_type=type_hints["certificate_provider_arn"])
            check_type(argname="argument certificate_provider_name", value=certificate_provider_name, expected_type=type_hints["certificate_provider_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_provider_arn": certificate_provider_arn,
            "certificate_provider_name": certificate_provider_name,
        }

    @builtins.property
    def certificate_provider_arn(self) -> builtins.str:
        '''The ARN of the CertificateProvider resource.'''
        result = self._values.get("certificate_provider_arn")
        assert result is not None, "Required property 'certificate_provider_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_provider_name(self) -> builtins.str:
        '''The CertificateProviderName of the CertificateProvider resource.'''
        result = self._values.get("certificate_provider_name")
        assert result is not None, "Required property 'certificate_provider_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateProviderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.CertificateReference",
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
        :param certificate_id: The Id of the Certificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            certificate_reference = interfaces_iot.CertificateReference(
                certificate_arn="certificateArn",
                certificate_id="certificateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd41822bb856d2c4cd7bfd1b33e1f7ae9aa20fabf6771532f867575bce52ca14)
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
        '''The Id of the Certificate resource.'''
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
    jsii_type="aws-cdk-lib.interfaces.aws_iot.CommandReference",
    jsii_struct_bases=[],
    name_mapping={"command_arn": "commandArn", "command_id": "commandId"},
)
class CommandReference:
    def __init__(self, *, command_arn: builtins.str, command_id: builtins.str) -> None:
        '''A reference to a Command resource.

        :param command_arn: The ARN of the Command resource.
        :param command_id: The CommandId of the Command resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            command_reference = interfaces_iot.CommandReference(
                command_arn="commandArn",
                command_id="commandId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af71183d16426d8accbf974b433d009aa255f59da4af7ca7356d9ebd5c8b333)
            check_type(argname="argument command_arn", value=command_arn, expected_type=type_hints["command_arn"])
            check_type(argname="argument command_id", value=command_id, expected_type=type_hints["command_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "command_arn": command_arn,
            "command_id": command_id,
        }

    @builtins.property
    def command_arn(self) -> builtins.str:
        '''The ARN of the Command resource.'''
        result = self._values.get("command_arn")
        assert result is not None, "Required property 'command_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def command_id(self) -> builtins.str:
        '''The CommandId of the Command resource.'''
        result = self._values.get("command_id")
        assert result is not None, "Required property 'command_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommandReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.CustomMetricReference",
    jsii_struct_bases=[],
    name_mapping={"metric_name": "metricName"},
)
class CustomMetricReference:
    def __init__(self, *, metric_name: builtins.str) -> None:
        '''A reference to a CustomMetric resource.

        :param metric_name: The MetricName of the CustomMetric resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            custom_metric_reference = interfaces_iot.CustomMetricReference(
                metric_name="metricName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fc6d149631e90be2dff15aa19b30410d2c3183ced2ee13cdcb1d0ba90a3bbc8)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
        }

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The MetricName of the CustomMetric resource.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomMetricReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.DimensionReference",
    jsii_struct_bases=[],
    name_mapping={"dimension_arn": "dimensionArn", "dimension_name": "dimensionName"},
)
class DimensionReference:
    def __init__(
        self,
        *,
        dimension_arn: builtins.str,
        dimension_name: builtins.str,
    ) -> None:
        '''A reference to a Dimension resource.

        :param dimension_arn: The ARN of the Dimension resource.
        :param dimension_name: The Name of the Dimension resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            dimension_reference = interfaces_iot.DimensionReference(
                dimension_arn="dimensionArn",
                dimension_name="dimensionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536bc66020b6f87b8fa03df1825e2fdd22350c7cab5f996602e34be7f5af3874)
            check_type(argname="argument dimension_arn", value=dimension_arn, expected_type=type_hints["dimension_arn"])
            check_type(argname="argument dimension_name", value=dimension_name, expected_type=type_hints["dimension_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dimension_arn": dimension_arn,
            "dimension_name": dimension_name,
        }

    @builtins.property
    def dimension_arn(self) -> builtins.str:
        '''The ARN of the Dimension resource.'''
        result = self._values.get("dimension_arn")
        assert result is not None, "Required property 'dimension_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimension_name(self) -> builtins.str:
        '''The Name of the Dimension resource.'''
        result = self._values.get("dimension_name")
        assert result is not None, "Required property 'dimension_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DimensionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.DomainConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_configuration_arn": "domainConfigurationArn",
        "domain_configuration_name": "domainConfigurationName",
    },
)
class DomainConfigurationReference:
    def __init__(
        self,
        *,
        domain_configuration_arn: builtins.str,
        domain_configuration_name: builtins.str,
    ) -> None:
        '''A reference to a DomainConfiguration resource.

        :param domain_configuration_arn: The ARN of the DomainConfiguration resource.
        :param domain_configuration_name: The DomainConfigurationName of the DomainConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            domain_configuration_reference = interfaces_iot.DomainConfigurationReference(
                domain_configuration_arn="domainConfigurationArn",
                domain_configuration_name="domainConfigurationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__072a2a0f202205af6e3de264c0d6baafb0bd344109806fb009fb406885e493b8)
            check_type(argname="argument domain_configuration_arn", value=domain_configuration_arn, expected_type=type_hints["domain_configuration_arn"])
            check_type(argname="argument domain_configuration_name", value=domain_configuration_name, expected_type=type_hints["domain_configuration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_configuration_arn": domain_configuration_arn,
            "domain_configuration_name": domain_configuration_name,
        }

    @builtins.property
    def domain_configuration_arn(self) -> builtins.str:
        '''The ARN of the DomainConfiguration resource.'''
        result = self._values.get("domain_configuration_arn")
        assert result is not None, "Required property 'domain_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_configuration_name(self) -> builtins.str:
        '''The DomainConfigurationName of the DomainConfiguration resource.'''
        result = self._values.get("domain_configuration_name")
        assert result is not None, "Required property 'domain_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.EncryptionConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class EncryptionConfigurationReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a EncryptionConfiguration resource.

        :param account_id: The AccountId of the EncryptionConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            encryption_configuration_reference = interfaces_iot.EncryptionConfigurationReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4243e6eeb1178b52ca431a8df25777c644a24a26ede98fac89e27a981c283fdb)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the EncryptionConfiguration resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncryptionConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.FleetMetricReference",
    jsii_struct_bases=[],
    name_mapping={"metric_name": "metricName"},
)
class FleetMetricReference:
    def __init__(self, *, metric_name: builtins.str) -> None:
        '''A reference to a FleetMetric resource.

        :param metric_name: The MetricName of the FleetMetric resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            fleet_metric_reference = interfaces_iot.FleetMetricReference(
                metric_name="metricName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87bcc885b51342fc4a7fd186621f27ba55cc31a51b3cd22d20675d422894e639)
            check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metric_name": metric_name,
        }

    @builtins.property
    def metric_name(self) -> builtins.str:
        '''The MetricName of the FleetMetric resource.'''
        result = self._values.get("metric_name")
        assert result is not None, "Required property 'metric_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FleetMetricReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.IAccountAuditConfigurationRef"
)
class IAccountAuditConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccountAuditConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accountAuditConfigurationRef")
    def account_audit_configuration_ref(self) -> "AccountAuditConfigurationReference":
        '''(experimental) A reference to a AccountAuditConfiguration resource.

        :stability: experimental
        '''
        ...


class _IAccountAuditConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccountAuditConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IAccountAuditConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="accountAuditConfigurationRef")
    def account_audit_configuration_ref(self) -> "AccountAuditConfigurationReference":
        '''(experimental) A reference to a AccountAuditConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("AccountAuditConfigurationReference", jsii.get(self, "accountAuditConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccountAuditConfigurationRef).__jsii_proxy_class__ = lambda : _IAccountAuditConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IAuthorizerRef")
class IAuthorizerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Authorizer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="authorizerRef")
    def authorizer_ref(self) -> "AuthorizerReference":
        '''(experimental) A reference to a Authorizer resource.

        :stability: experimental
        '''
        ...


class _IAuthorizerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Authorizer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IAuthorizerRef"

    @builtins.property
    @jsii.member(jsii_name="authorizerRef")
    def authorizer_ref(self) -> "AuthorizerReference":
        '''(experimental) A reference to a Authorizer resource.

        :stability: experimental
        '''
        return typing.cast("AuthorizerReference", jsii.get(self, "authorizerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAuthorizerRef).__jsii_proxy_class__ = lambda : _IAuthorizerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IBillingGroupRef")
class IBillingGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BillingGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="billingGroupRef")
    def billing_group_ref(self) -> "BillingGroupReference":
        '''(experimental) A reference to a BillingGroup resource.

        :stability: experimental
        '''
        ...


class _IBillingGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BillingGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IBillingGroupRef"

    @builtins.property
    @jsii.member(jsii_name="billingGroupRef")
    def billing_group_ref(self) -> "BillingGroupReference":
        '''(experimental) A reference to a BillingGroup resource.

        :stability: experimental
        '''
        return typing.cast("BillingGroupReference", jsii.get(self, "billingGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBillingGroupRef).__jsii_proxy_class__ = lambda : _IBillingGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ICACertificateRef")
class ICACertificateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CACertificate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="caCertificateRef")
    def ca_certificate_ref(self) -> "CACertificateReference":
        '''(experimental) A reference to a CACertificate resource.

        :stability: experimental
        '''
        ...


class _ICACertificateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CACertificate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ICACertificateRef"

    @builtins.property
    @jsii.member(jsii_name="caCertificateRef")
    def ca_certificate_ref(self) -> "CACertificateReference":
        '''(experimental) A reference to a CACertificate resource.

        :stability: experimental
        '''
        return typing.cast("CACertificateReference", jsii.get(self, "caCertificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICACertificateRef).__jsii_proxy_class__ = lambda : _ICACertificateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ICertificateProviderRef")
class ICertificateProviderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CertificateProvider.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="certificateProviderRef")
    def certificate_provider_ref(self) -> "CertificateProviderReference":
        '''(experimental) A reference to a CertificateProvider resource.

        :stability: experimental
        '''
        ...


class _ICertificateProviderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CertificateProvider.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ICertificateProviderRef"

    @builtins.property
    @jsii.member(jsii_name="certificateProviderRef")
    def certificate_provider_ref(self) -> "CertificateProviderReference":
        '''(experimental) A reference to a CertificateProvider resource.

        :stability: experimental
        '''
        return typing.cast("CertificateProviderReference", jsii.get(self, "certificateProviderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateProviderRef).__jsii_proxy_class__ = lambda : _ICertificateProviderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ICertificateRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ICertificateRef"

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        return typing.cast("CertificateReference", jsii.get(self, "certificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateRef).__jsii_proxy_class__ = lambda : _ICertificateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ICommandRef")
class ICommandRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Command.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="commandRef")
    def command_ref(self) -> "CommandReference":
        '''(experimental) A reference to a Command resource.

        :stability: experimental
        '''
        ...


class _ICommandRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Command.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ICommandRef"

    @builtins.property
    @jsii.member(jsii_name="commandRef")
    def command_ref(self) -> "CommandReference":
        '''(experimental) A reference to a Command resource.

        :stability: experimental
        '''
        return typing.cast("CommandReference", jsii.get(self, "commandRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICommandRef).__jsii_proxy_class__ = lambda : _ICommandRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ICustomMetricRef")
class ICustomMetricRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomMetric.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customMetricRef")
    def custom_metric_ref(self) -> "CustomMetricReference":
        '''(experimental) A reference to a CustomMetric resource.

        :stability: experimental
        '''
        ...


class _ICustomMetricRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomMetric.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ICustomMetricRef"

    @builtins.property
    @jsii.member(jsii_name="customMetricRef")
    def custom_metric_ref(self) -> "CustomMetricReference":
        '''(experimental) A reference to a CustomMetric resource.

        :stability: experimental
        '''
        return typing.cast("CustomMetricReference", jsii.get(self, "customMetricRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomMetricRef).__jsii_proxy_class__ = lambda : _ICustomMetricRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IDimensionRef")
class IDimensionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Dimension.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dimensionRef")
    def dimension_ref(self) -> "DimensionReference":
        '''(experimental) A reference to a Dimension resource.

        :stability: experimental
        '''
        ...


class _IDimensionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Dimension.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IDimensionRef"

    @builtins.property
    @jsii.member(jsii_name="dimensionRef")
    def dimension_ref(self) -> "DimensionReference":
        '''(experimental) A reference to a Dimension resource.

        :stability: experimental
        '''
        return typing.cast("DimensionReference", jsii.get(self, "dimensionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDimensionRef).__jsii_proxy_class__ = lambda : _IDimensionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IDomainConfigurationRef")
class IDomainConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DomainConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainConfigurationRef")
    def domain_configuration_ref(self) -> "DomainConfigurationReference":
        '''(experimental) A reference to a DomainConfiguration resource.

        :stability: experimental
        '''
        ...


class _IDomainConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DomainConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IDomainConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="domainConfigurationRef")
    def domain_configuration_ref(self) -> "DomainConfigurationReference":
        '''(experimental) A reference to a DomainConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("DomainConfigurationReference", jsii.get(self, "domainConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainConfigurationRef).__jsii_proxy_class__ = lambda : _IDomainConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IEncryptionConfigurationRef")
class IEncryptionConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EncryptionConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigurationRef")
    def encryption_configuration_ref(self) -> "EncryptionConfigurationReference":
        '''(experimental) A reference to a EncryptionConfiguration resource.

        :stability: experimental
        '''
        ...


class _IEncryptionConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EncryptionConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IEncryptionConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigurationRef")
    def encryption_configuration_ref(self) -> "EncryptionConfigurationReference":
        '''(experimental) A reference to a EncryptionConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("EncryptionConfigurationReference", jsii.get(self, "encryptionConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEncryptionConfigurationRef).__jsii_proxy_class__ = lambda : _IEncryptionConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IFleetMetricRef")
class IFleetMetricRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FleetMetric.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fleetMetricRef")
    def fleet_metric_ref(self) -> "FleetMetricReference":
        '''(experimental) A reference to a FleetMetric resource.

        :stability: experimental
        '''
        ...


class _IFleetMetricRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FleetMetric.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IFleetMetricRef"

    @builtins.property
    @jsii.member(jsii_name="fleetMetricRef")
    def fleet_metric_ref(self) -> "FleetMetricReference":
        '''(experimental) A reference to a FleetMetric resource.

        :stability: experimental
        '''
        return typing.cast("FleetMetricReference", jsii.get(self, "fleetMetricRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFleetMetricRef).__jsii_proxy_class__ = lambda : _IFleetMetricRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IJobTemplateRef")
class IJobTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a JobTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="jobTemplateRef")
    def job_template_ref(self) -> "JobTemplateReference":
        '''(experimental) A reference to a JobTemplate resource.

        :stability: experimental
        '''
        ...


class _IJobTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a JobTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IJobTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="jobTemplateRef")
    def job_template_ref(self) -> "JobTemplateReference":
        '''(experimental) A reference to a JobTemplate resource.

        :stability: experimental
        '''
        return typing.cast("JobTemplateReference", jsii.get(self, "jobTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJobTemplateRef).__jsii_proxy_class__ = lambda : _IJobTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ILoggingRef")
class ILoggingRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Logging.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="loggingRef")
    def logging_ref(self) -> "LoggingReference":
        '''(experimental) A reference to a Logging resource.

        :stability: experimental
        '''
        ...


class _ILoggingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Logging.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ILoggingRef"

    @builtins.property
    @jsii.member(jsii_name="loggingRef")
    def logging_ref(self) -> "LoggingReference":
        '''(experimental) A reference to a Logging resource.

        :stability: experimental
        '''
        return typing.cast("LoggingReference", jsii.get(self, "loggingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoggingRef).__jsii_proxy_class__ = lambda : _ILoggingRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IMitigationActionRef")
class IMitigationActionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MitigationAction.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mitigationActionRef")
    def mitigation_action_ref(self) -> "MitigationActionReference":
        '''(experimental) A reference to a MitigationAction resource.

        :stability: experimental
        '''
        ...


class _IMitigationActionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MitigationAction.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IMitigationActionRef"

    @builtins.property
    @jsii.member(jsii_name="mitigationActionRef")
    def mitigation_action_ref(self) -> "MitigationActionReference":
        '''(experimental) A reference to a MitigationAction resource.

        :stability: experimental
        '''
        return typing.cast("MitigationActionReference", jsii.get(self, "mitigationActionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMitigationActionRef).__jsii_proxy_class__ = lambda : _IMitigationActionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.IPolicyPrincipalAttachmentRef"
)
class IPolicyPrincipalAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyPrincipalAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="policyPrincipalAttachmentRef")
    def policy_principal_attachment_ref(self) -> "PolicyPrincipalAttachmentReference":
        '''(experimental) A reference to a PolicyPrincipalAttachment resource.

        :stability: experimental
        '''
        ...


class _IPolicyPrincipalAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyPrincipalAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IPolicyPrincipalAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="policyPrincipalAttachmentRef")
    def policy_principal_attachment_ref(self) -> "PolicyPrincipalAttachmentReference":
        '''(experimental) A reference to a PolicyPrincipalAttachment resource.

        :stability: experimental
        '''
        return typing.cast("PolicyPrincipalAttachmentReference", jsii.get(self, "policyPrincipalAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyPrincipalAttachmentRef).__jsii_proxy_class__ = lambda : _IPolicyPrincipalAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IPolicyRef")
class IPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Policy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="policyRef")
    def policy_ref(self) -> "PolicyReference":
        '''(experimental) A reference to a Policy resource.

        :stability: experimental
        '''
        ...


class _IPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Policy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="policyRef")
    def policy_ref(self) -> "PolicyReference":
        '''(experimental) A reference to a Policy resource.

        :stability: experimental
        '''
        return typing.cast("PolicyReference", jsii.get(self, "policyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyRef).__jsii_proxy_class__ = lambda : _IPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IProvisioningTemplateRef")
class IProvisioningTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProvisioningTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="provisioningTemplateRef")
    def provisioning_template_ref(self) -> "ProvisioningTemplateReference":
        '''(experimental) A reference to a ProvisioningTemplate resource.

        :stability: experimental
        '''
        ...


class _IProvisioningTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProvisioningTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IProvisioningTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="provisioningTemplateRef")
    def provisioning_template_ref(self) -> "ProvisioningTemplateReference":
        '''(experimental) A reference to a ProvisioningTemplate resource.

        :stability: experimental
        '''
        return typing.cast("ProvisioningTemplateReference", jsii.get(self, "provisioningTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProvisioningTemplateRef).__jsii_proxy_class__ = lambda : _IProvisioningTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IResourceSpecificLoggingRef")
class IResourceSpecificLoggingRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceSpecificLogging.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceSpecificLoggingRef")
    def resource_specific_logging_ref(self) -> "ResourceSpecificLoggingReference":
        '''(experimental) A reference to a ResourceSpecificLogging resource.

        :stability: experimental
        '''
        ...


class _IResourceSpecificLoggingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceSpecificLogging.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IResourceSpecificLoggingRef"

    @builtins.property
    @jsii.member(jsii_name="resourceSpecificLoggingRef")
    def resource_specific_logging_ref(self) -> "ResourceSpecificLoggingReference":
        '''(experimental) A reference to a ResourceSpecificLogging resource.

        :stability: experimental
        '''
        return typing.cast("ResourceSpecificLoggingReference", jsii.get(self, "resourceSpecificLoggingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceSpecificLoggingRef).__jsii_proxy_class__ = lambda : _IResourceSpecificLoggingRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IRoleAliasRef")
class IRoleAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RoleAlias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="roleAliasRef")
    def role_alias_ref(self) -> "RoleAliasReference":
        '''(experimental) A reference to a RoleAlias resource.

        :stability: experimental
        '''
        ...


class _IRoleAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RoleAlias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IRoleAliasRef"

    @builtins.property
    @jsii.member(jsii_name="roleAliasRef")
    def role_alias_ref(self) -> "RoleAliasReference":
        '''(experimental) A reference to a RoleAlias resource.

        :stability: experimental
        '''
        return typing.cast("RoleAliasReference", jsii.get(self, "roleAliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRoleAliasRef).__jsii_proxy_class__ = lambda : _IRoleAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IScheduledAuditRef")
class IScheduledAuditRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledAudit.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scheduledAuditRef")
    def scheduled_audit_ref(self) -> "ScheduledAuditReference":
        '''(experimental) A reference to a ScheduledAudit resource.

        :stability: experimental
        '''
        ...


class _IScheduledAuditRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledAudit.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IScheduledAuditRef"

    @builtins.property
    @jsii.member(jsii_name="scheduledAuditRef")
    def scheduled_audit_ref(self) -> "ScheduledAuditReference":
        '''(experimental) A reference to a ScheduledAudit resource.

        :stability: experimental
        '''
        return typing.cast("ScheduledAuditReference", jsii.get(self, "scheduledAuditRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduledAuditRef).__jsii_proxy_class__ = lambda : _IScheduledAuditRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ISecurityProfileRef")
class ISecurityProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityProfileRef")
    def security_profile_ref(self) -> "SecurityProfileReference":
        '''(experimental) A reference to a SecurityProfile resource.

        :stability: experimental
        '''
        ...


class _ISecurityProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ISecurityProfileRef"

    @builtins.property
    @jsii.member(jsii_name="securityProfileRef")
    def security_profile_ref(self) -> "SecurityProfileReference":
        '''(experimental) A reference to a SecurityProfile resource.

        :stability: experimental
        '''
        return typing.cast("SecurityProfileReference", jsii.get(self, "securityProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityProfileRef).__jsii_proxy_class__ = lambda : _ISecurityProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ISoftwarePackageRef")
class ISoftwarePackageRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SoftwarePackage.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="softwarePackageRef")
    def software_package_ref(self) -> "SoftwarePackageReference":
        '''(experimental) A reference to a SoftwarePackage resource.

        :stability: experimental
        '''
        ...


class _ISoftwarePackageRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SoftwarePackage.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ISoftwarePackageRef"

    @builtins.property
    @jsii.member(jsii_name="softwarePackageRef")
    def software_package_ref(self) -> "SoftwarePackageReference":
        '''(experimental) A reference to a SoftwarePackage resource.

        :stability: experimental
        '''
        return typing.cast("SoftwarePackageReference", jsii.get(self, "softwarePackageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISoftwarePackageRef).__jsii_proxy_class__ = lambda : _ISoftwarePackageRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ISoftwarePackageVersionRef")
class ISoftwarePackageVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SoftwarePackageVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="softwarePackageVersionRef")
    def software_package_version_ref(self) -> "SoftwarePackageVersionReference":
        '''(experimental) A reference to a SoftwarePackageVersion resource.

        :stability: experimental
        '''
        ...


class _ISoftwarePackageVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SoftwarePackageVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ISoftwarePackageVersionRef"

    @builtins.property
    @jsii.member(jsii_name="softwarePackageVersionRef")
    def software_package_version_ref(self) -> "SoftwarePackageVersionReference":
        '''(experimental) A reference to a SoftwarePackageVersion resource.

        :stability: experimental
        '''
        return typing.cast("SoftwarePackageVersionReference", jsii.get(self, "softwarePackageVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISoftwarePackageVersionRef).__jsii_proxy_class__ = lambda : _ISoftwarePackageVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IThingGroupRef")
class IThingGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ThingGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="thingGroupRef")
    def thing_group_ref(self) -> "ThingGroupReference":
        '''(experimental) A reference to a ThingGroup resource.

        :stability: experimental
        '''
        ...


class _IThingGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ThingGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IThingGroupRef"

    @builtins.property
    @jsii.member(jsii_name="thingGroupRef")
    def thing_group_ref(self) -> "ThingGroupReference":
        '''(experimental) A reference to a ThingGroup resource.

        :stability: experimental
        '''
        return typing.cast("ThingGroupReference", jsii.get(self, "thingGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThingGroupRef).__jsii_proxy_class__ = lambda : _IThingGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.IThingPrincipalAttachmentRef"
)
class IThingPrincipalAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ThingPrincipalAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="thingPrincipalAttachmentRef")
    def thing_principal_attachment_ref(self) -> "ThingPrincipalAttachmentReference":
        '''(experimental) A reference to a ThingPrincipalAttachment resource.

        :stability: experimental
        '''
        ...


class _IThingPrincipalAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ThingPrincipalAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IThingPrincipalAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="thingPrincipalAttachmentRef")
    def thing_principal_attachment_ref(self) -> "ThingPrincipalAttachmentReference":
        '''(experimental) A reference to a ThingPrincipalAttachment resource.

        :stability: experimental
        '''
        return typing.cast("ThingPrincipalAttachmentReference", jsii.get(self, "thingPrincipalAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThingPrincipalAttachmentRef).__jsii_proxy_class__ = lambda : _IThingPrincipalAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IThingRef")
class IThingRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Thing.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="thingRef")
    def thing_ref(self) -> "ThingReference":
        '''(experimental) A reference to a Thing resource.

        :stability: experimental
        '''
        ...


class _IThingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Thing.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IThingRef"

    @builtins.property
    @jsii.member(jsii_name="thingRef")
    def thing_ref(self) -> "ThingReference":
        '''(experimental) A reference to a Thing resource.

        :stability: experimental
        '''
        return typing.cast("ThingReference", jsii.get(self, "thingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThingRef).__jsii_proxy_class__ = lambda : _IThingRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.IThingTypeRef")
class IThingTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ThingType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="thingTypeRef")
    def thing_type_ref(self) -> "ThingTypeReference":
        '''(experimental) A reference to a ThingType resource.

        :stability: experimental
        '''
        ...


class _IThingTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ThingType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.IThingTypeRef"

    @builtins.property
    @jsii.member(jsii_name="thingTypeRef")
    def thing_type_ref(self) -> "ThingTypeReference":
        '''(experimental) A reference to a ThingType resource.

        :stability: experimental
        '''
        return typing.cast("ThingTypeReference", jsii.get(self, "thingTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThingTypeRef).__jsii_proxy_class__ = lambda : _IThingTypeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ITopicRuleDestinationRef")
class ITopicRuleDestinationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TopicRuleDestination.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicRuleDestinationRef")
    def topic_rule_destination_ref(self) -> "TopicRuleDestinationReference":
        '''(experimental) A reference to a TopicRuleDestination resource.

        :stability: experimental
        '''
        ...


class _ITopicRuleDestinationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TopicRuleDestination.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ITopicRuleDestinationRef"

    @builtins.property
    @jsii.member(jsii_name="topicRuleDestinationRef")
    def topic_rule_destination_ref(self) -> "TopicRuleDestinationReference":
        '''(experimental) A reference to a TopicRuleDestination resource.

        :stability: experimental
        '''
        return typing.cast("TopicRuleDestinationReference", jsii.get(self, "topicRuleDestinationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicRuleDestinationRef).__jsii_proxy_class__ = lambda : _ITopicRuleDestinationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iot.ITopicRuleRef")
class ITopicRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TopicRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicRuleRef")
    def topic_rule_ref(self) -> "TopicRuleReference":
        '''(experimental) A reference to a TopicRule resource.

        :stability: experimental
        '''
        ...


class _ITopicRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TopicRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iot.ITopicRuleRef"

    @builtins.property
    @jsii.member(jsii_name="topicRuleRef")
    def topic_rule_ref(self) -> "TopicRuleReference":
        '''(experimental) A reference to a TopicRule resource.

        :stability: experimental
        '''
        return typing.cast("TopicRuleReference", jsii.get(self, "topicRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicRuleRef).__jsii_proxy_class__ = lambda : _ITopicRuleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.JobTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "job_template_arn": "jobTemplateArn",
        "job_template_id": "jobTemplateId",
    },
)
class JobTemplateReference:
    def __init__(
        self,
        *,
        job_template_arn: builtins.str,
        job_template_id: builtins.str,
    ) -> None:
        '''A reference to a JobTemplate resource.

        :param job_template_arn: The ARN of the JobTemplate resource.
        :param job_template_id: The JobTemplateId of the JobTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            job_template_reference = interfaces_iot.JobTemplateReference(
                job_template_arn="jobTemplateArn",
                job_template_id="jobTemplateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cffd41be04fe17710e1be7db9d085434eb15f2abdfafdc430d120ed83c4ec4aa)
            check_type(argname="argument job_template_arn", value=job_template_arn, expected_type=type_hints["job_template_arn"])
            check_type(argname="argument job_template_id", value=job_template_id, expected_type=type_hints["job_template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_template_arn": job_template_arn,
            "job_template_id": job_template_id,
        }

    @builtins.property
    def job_template_arn(self) -> builtins.str:
        '''The ARN of the JobTemplate resource.'''
        result = self._values.get("job_template_arn")
        assert result is not None, "Required property 'job_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_template_id(self) -> builtins.str:
        '''The JobTemplateId of the JobTemplate resource.'''
        result = self._values.get("job_template_id")
        assert result is not None, "Required property 'job_template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.LoggingReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class LoggingReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a Logging resource.

        :param account_id: The AccountId of the Logging resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            logging_reference = interfaces_iot.LoggingReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77f6f67c551d1d6d5b9be87e433d3ac8b37687437ee923fe545bbabcfdaadd98)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the Logging resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.MitigationActionReference",
    jsii_struct_bases=[],
    name_mapping={
        "action_name": "actionName",
        "mitigation_action_arn": "mitigationActionArn",
    },
)
class MitigationActionReference:
    def __init__(
        self,
        *,
        action_name: builtins.str,
        mitigation_action_arn: builtins.str,
    ) -> None:
        '''A reference to a MitigationAction resource.

        :param action_name: The ActionName of the MitigationAction resource.
        :param mitigation_action_arn: The ARN of the MitigationAction resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            mitigation_action_reference = interfaces_iot.MitigationActionReference(
                action_name="actionName",
                mitigation_action_arn="mitigationActionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ab56eb3d521febcf038be8ef1e03908bd95582acb3cf3b9cac5d7c92db5e09f)
            check_type(argname="argument action_name", value=action_name, expected_type=type_hints["action_name"])
            check_type(argname="argument mitigation_action_arn", value=mitigation_action_arn, expected_type=type_hints["mitigation_action_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_name": action_name,
            "mitigation_action_arn": mitigation_action_arn,
        }

    @builtins.property
    def action_name(self) -> builtins.str:
        '''The ActionName of the MitigationAction resource.'''
        result = self._values.get("action_name")
        assert result is not None, "Required property 'action_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mitigation_action_arn(self) -> builtins.str:
        '''The ARN of the MitigationAction resource.'''
        result = self._values.get("mitigation_action_arn")
        assert result is not None, "Required property 'mitigation_action_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MitigationActionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.PolicyPrincipalAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"policy_principal_attachment_id": "policyPrincipalAttachmentId"},
)
class PolicyPrincipalAttachmentReference:
    def __init__(self, *, policy_principal_attachment_id: builtins.str) -> None:
        '''A reference to a PolicyPrincipalAttachment resource.

        :param policy_principal_attachment_id: The Id of the PolicyPrincipalAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            policy_principal_attachment_reference = interfaces_iot.PolicyPrincipalAttachmentReference(
                policy_principal_attachment_id="policyPrincipalAttachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c433b17a937fb1b126780e6e4b459921a745c39de25b681aa6e87feb4111932)
            check_type(argname="argument policy_principal_attachment_id", value=policy_principal_attachment_id, expected_type=type_hints["policy_principal_attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_principal_attachment_id": policy_principal_attachment_id,
        }

    @builtins.property
    def policy_principal_attachment_id(self) -> builtins.str:
        '''The Id of the PolicyPrincipalAttachment resource.'''
        result = self._values.get("policy_principal_attachment_id")
        assert result is not None, "Required property 'policy_principal_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyPrincipalAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.PolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_arn": "policyArn", "policy_name": "policyName"},
)
class PolicyReference:
    def __init__(self, *, policy_arn: builtins.str, policy_name: builtins.str) -> None:
        '''A reference to a Policy resource.

        :param policy_arn: The ARN of the Policy resource.
        :param policy_name: The PolicyName of the Policy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            policy_reference = interfaces_iot.PolicyReference(
                policy_arn="policyArn",
                policy_name="policyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b627d7889748208bffcd4d74e49d11968847654f52f8d4d0b508b1333b01f6aa)
            check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_arn": policy_arn,
            "policy_name": policy_name,
        }

    @builtins.property
    def policy_arn(self) -> builtins.str:
        '''The ARN of the Policy resource.'''
        result = self._values.get("policy_arn")
        assert result is not None, "Required property 'policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The PolicyName of the Policy resource.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.ProvisioningTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"template_name": "templateName"},
)
class ProvisioningTemplateReference:
    def __init__(self, *, template_name: builtins.str) -> None:
        '''A reference to a ProvisioningTemplate resource.

        :param template_name: The TemplateName of the ProvisioningTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            provisioning_template_reference = interfaces_iot.ProvisioningTemplateReference(
                template_name="templateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9039c63005bab6ff59546e15433165533243c424a4b0053c5aef2e6ff1affb7)
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_name": template_name,
        }

    @builtins.property
    def template_name(self) -> builtins.str:
        '''The TemplateName of the ProvisioningTemplate resource.'''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProvisioningTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.ResourceSpecificLoggingReference",
    jsii_struct_bases=[],
    name_mapping={"target_id": "targetId"},
)
class ResourceSpecificLoggingReference:
    def __init__(self, *, target_id: builtins.str) -> None:
        '''A reference to a ResourceSpecificLogging resource.

        :param target_id: The TargetId of the ResourceSpecificLogging resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            resource_specific_logging_reference = interfaces_iot.ResourceSpecificLoggingReference(
                target_id="targetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ebce77dbfe0456eff9639b6385561d6943a5d17fba95d1f552eed0e95bbf6b0)
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_id": target_id,
        }

    @builtins.property
    def target_id(self) -> builtins.str:
        '''The TargetId of the ResourceSpecificLogging resource.'''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceSpecificLoggingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.RoleAliasReference",
    jsii_struct_bases=[],
    name_mapping={"role_alias": "roleAlias", "role_alias_arn": "roleAliasArn"},
)
class RoleAliasReference:
    def __init__(
        self,
        *,
        role_alias: builtins.str,
        role_alias_arn: builtins.str,
    ) -> None:
        '''A reference to a RoleAlias resource.

        :param role_alias: The RoleAlias of the RoleAlias resource.
        :param role_alias_arn: The ARN of the RoleAlias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            role_alias_reference = interfaces_iot.RoleAliasReference(
                role_alias="roleAlias",
                role_alias_arn="roleAliasArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a120b8f8d83a7dded11d9f9de72d69d5ca598d6ec190c3d6340acb452f28b5)
            check_type(argname="argument role_alias", value=role_alias, expected_type=type_hints["role_alias"])
            check_type(argname="argument role_alias_arn", value=role_alias_arn, expected_type=type_hints["role_alias_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_alias": role_alias,
            "role_alias_arn": role_alias_arn,
        }

    @builtins.property
    def role_alias(self) -> builtins.str:
        '''The RoleAlias of the RoleAlias resource.'''
        result = self._values.get("role_alias")
        assert result is not None, "Required property 'role_alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_alias_arn(self) -> builtins.str:
        '''The ARN of the RoleAlias resource.'''
        result = self._values.get("role_alias_arn")
        assert result is not None, "Required property 'role_alias_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleAliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.ScheduledAuditReference",
    jsii_struct_bases=[],
    name_mapping={
        "scheduled_audit_arn": "scheduledAuditArn",
        "scheduled_audit_name": "scheduledAuditName",
    },
)
class ScheduledAuditReference:
    def __init__(
        self,
        *,
        scheduled_audit_arn: builtins.str,
        scheduled_audit_name: builtins.str,
    ) -> None:
        '''A reference to a ScheduledAudit resource.

        :param scheduled_audit_arn: The ARN of the ScheduledAudit resource.
        :param scheduled_audit_name: The ScheduledAuditName of the ScheduledAudit resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            scheduled_audit_reference = interfaces_iot.ScheduledAuditReference(
                scheduled_audit_arn="scheduledAuditArn",
                scheduled_audit_name="scheduledAuditName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60d8201b72f88cdd64cd19128a2c60aeded5bd7dc74179f5252602f226054061)
            check_type(argname="argument scheduled_audit_arn", value=scheduled_audit_arn, expected_type=type_hints["scheduled_audit_arn"])
            check_type(argname="argument scheduled_audit_name", value=scheduled_audit_name, expected_type=type_hints["scheduled_audit_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scheduled_audit_arn": scheduled_audit_arn,
            "scheduled_audit_name": scheduled_audit_name,
        }

    @builtins.property
    def scheduled_audit_arn(self) -> builtins.str:
        '''The ARN of the ScheduledAudit resource.'''
        result = self._values.get("scheduled_audit_arn")
        assert result is not None, "Required property 'scheduled_audit_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scheduled_audit_name(self) -> builtins.str:
        '''The ScheduledAuditName of the ScheduledAudit resource.'''
        result = self._values.get("scheduled_audit_name")
        assert result is not None, "Required property 'scheduled_audit_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduledAuditReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.SecurityProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "security_profile_arn": "securityProfileArn",
        "security_profile_name": "securityProfileName",
    },
)
class SecurityProfileReference:
    def __init__(
        self,
        *,
        security_profile_arn: builtins.str,
        security_profile_name: builtins.str,
    ) -> None:
        '''A reference to a SecurityProfile resource.

        :param security_profile_arn: The ARN of the SecurityProfile resource.
        :param security_profile_name: The SecurityProfileName of the SecurityProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            security_profile_reference = interfaces_iot.SecurityProfileReference(
                security_profile_arn="securityProfileArn",
                security_profile_name="securityProfileName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abf43e9f4ab30ee59ab380489311b985cbddf07f1dc8cdccc91ca1cf38ce9637)
            check_type(argname="argument security_profile_arn", value=security_profile_arn, expected_type=type_hints["security_profile_arn"])
            check_type(argname="argument security_profile_name", value=security_profile_name, expected_type=type_hints["security_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_profile_arn": security_profile_arn,
            "security_profile_name": security_profile_name,
        }

    @builtins.property
    def security_profile_arn(self) -> builtins.str:
        '''The ARN of the SecurityProfile resource.'''
        result = self._values.get("security_profile_arn")
        assert result is not None, "Required property 'security_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_profile_name(self) -> builtins.str:
        '''The SecurityProfileName of the SecurityProfile resource.'''
        result = self._values.get("security_profile_name")
        assert result is not None, "Required property 'security_profile_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.SoftwarePackageReference",
    jsii_struct_bases=[],
    name_mapping={"package_name": "packageName"},
)
class SoftwarePackageReference:
    def __init__(self, *, package_name: builtins.str) -> None:
        '''A reference to a SoftwarePackage resource.

        :param package_name: The PackageName of the SoftwarePackage resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            software_package_reference = interfaces_iot.SoftwarePackageReference(
                package_name="packageName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb6ad3330b82f009179276f80acdee16561cdc42f31b2d0af96bfb331b6421f9)
            check_type(argname="argument package_name", value=package_name, expected_type=type_hints["package_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package_name": package_name,
        }

    @builtins.property
    def package_name(self) -> builtins.str:
        '''The PackageName of the SoftwarePackage resource.'''
        result = self._values.get("package_name")
        assert result is not None, "Required property 'package_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SoftwarePackageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.SoftwarePackageVersionReference",
    jsii_struct_bases=[],
    name_mapping={"package_name": "packageName", "version_name": "versionName"},
)
class SoftwarePackageVersionReference:
    def __init__(
        self,
        *,
        package_name: builtins.str,
        version_name: builtins.str,
    ) -> None:
        '''A reference to a SoftwarePackageVersion resource.

        :param package_name: The PackageName of the SoftwarePackageVersion resource.
        :param version_name: The VersionName of the SoftwarePackageVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            software_package_version_reference = interfaces_iot.SoftwarePackageVersionReference(
                package_name="packageName",
                version_name="versionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8549067511c3dd9b2931691a58ae4f172a4d90a25349fe4ef5b45920e28a073e)
            check_type(argname="argument package_name", value=package_name, expected_type=type_hints["package_name"])
            check_type(argname="argument version_name", value=version_name, expected_type=type_hints["version_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "package_name": package_name,
            "version_name": version_name,
        }

    @builtins.property
    def package_name(self) -> builtins.str:
        '''The PackageName of the SoftwarePackageVersion resource.'''
        result = self._values.get("package_name")
        assert result is not None, "Required property 'package_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_name(self) -> builtins.str:
        '''The VersionName of the SoftwarePackageVersion resource.'''
        result = self._values.get("version_name")
        assert result is not None, "Required property 'version_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SoftwarePackageVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.ThingGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "thing_group_arn": "thingGroupArn",
        "thing_group_name": "thingGroupName",
    },
)
class ThingGroupReference:
    def __init__(
        self,
        *,
        thing_group_arn: builtins.str,
        thing_group_name: builtins.str,
    ) -> None:
        '''A reference to a ThingGroup resource.

        :param thing_group_arn: The ARN of the ThingGroup resource.
        :param thing_group_name: The ThingGroupName of the ThingGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            thing_group_reference = interfaces_iot.ThingGroupReference(
                thing_group_arn="thingGroupArn",
                thing_group_name="thingGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf577bbf82c8129b7cff9884cac80e23395d69657fd40c3d65bef791576507a6)
            check_type(argname="argument thing_group_arn", value=thing_group_arn, expected_type=type_hints["thing_group_arn"])
            check_type(argname="argument thing_group_name", value=thing_group_name, expected_type=type_hints["thing_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "thing_group_arn": thing_group_arn,
            "thing_group_name": thing_group_name,
        }

    @builtins.property
    def thing_group_arn(self) -> builtins.str:
        '''The ARN of the ThingGroup resource.'''
        result = self._values.get("thing_group_arn")
        assert result is not None, "Required property 'thing_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thing_group_name(self) -> builtins.str:
        '''The ThingGroupName of the ThingGroup resource.'''
        result = self._values.get("thing_group_name")
        assert result is not None, "Required property 'thing_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThingGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.ThingPrincipalAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"thing_principal_attachment_id": "thingPrincipalAttachmentId"},
)
class ThingPrincipalAttachmentReference:
    def __init__(self, *, thing_principal_attachment_id: builtins.str) -> None:
        '''A reference to a ThingPrincipalAttachment resource.

        :param thing_principal_attachment_id: The Id of the ThingPrincipalAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            thing_principal_attachment_reference = interfaces_iot.ThingPrincipalAttachmentReference(
                thing_principal_attachment_id="thingPrincipalAttachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43efd3fd743ae12945fd439b22b4a32cf10787e7ffe3bb66b57eb430a483d631)
            check_type(argname="argument thing_principal_attachment_id", value=thing_principal_attachment_id, expected_type=type_hints["thing_principal_attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "thing_principal_attachment_id": thing_principal_attachment_id,
        }

    @builtins.property
    def thing_principal_attachment_id(self) -> builtins.str:
        '''The Id of the ThingPrincipalAttachment resource.'''
        result = self._values.get("thing_principal_attachment_id")
        assert result is not None, "Required property 'thing_principal_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThingPrincipalAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.ThingReference",
    jsii_struct_bases=[],
    name_mapping={"thing_arn": "thingArn", "thing_name": "thingName"},
)
class ThingReference:
    def __init__(self, *, thing_arn: builtins.str, thing_name: builtins.str) -> None:
        '''A reference to a Thing resource.

        :param thing_arn: The ARN of the Thing resource.
        :param thing_name: The ThingName of the Thing resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            thing_reference = interfaces_iot.ThingReference(
                thing_arn="thingArn",
                thing_name="thingName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94282163e56abff7455704452ffdb9ea32a695f0a0a1add365fa6d4b15af02ab)
            check_type(argname="argument thing_arn", value=thing_arn, expected_type=type_hints["thing_arn"])
            check_type(argname="argument thing_name", value=thing_name, expected_type=type_hints["thing_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "thing_arn": thing_arn,
            "thing_name": thing_name,
        }

    @builtins.property
    def thing_arn(self) -> builtins.str:
        '''The ARN of the Thing resource.'''
        result = self._values.get("thing_arn")
        assert result is not None, "Required property 'thing_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thing_name(self) -> builtins.str:
        '''The ThingName of the Thing resource.'''
        result = self._values.get("thing_name")
        assert result is not None, "Required property 'thing_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.ThingTypeReference",
    jsii_struct_bases=[],
    name_mapping={
        "thing_type_arn": "thingTypeArn",
        "thing_type_name": "thingTypeName",
    },
)
class ThingTypeReference:
    def __init__(
        self,
        *,
        thing_type_arn: builtins.str,
        thing_type_name: builtins.str,
    ) -> None:
        '''A reference to a ThingType resource.

        :param thing_type_arn: The ARN of the ThingType resource.
        :param thing_type_name: The ThingTypeName of the ThingType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            thing_type_reference = interfaces_iot.ThingTypeReference(
                thing_type_arn="thingTypeArn",
                thing_type_name="thingTypeName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__292b49d0fadd16c5715ae5ae5da4c61db1f6938820c0abd38301fc02146dc02e)
            check_type(argname="argument thing_type_arn", value=thing_type_arn, expected_type=type_hints["thing_type_arn"])
            check_type(argname="argument thing_type_name", value=thing_type_name, expected_type=type_hints["thing_type_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "thing_type_arn": thing_type_arn,
            "thing_type_name": thing_type_name,
        }

    @builtins.property
    def thing_type_arn(self) -> builtins.str:
        '''The ARN of the ThingType resource.'''
        result = self._values.get("thing_type_arn")
        assert result is not None, "Required property 'thing_type_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def thing_type_name(self) -> builtins.str:
        '''The ThingTypeName of the ThingType resource.'''
        result = self._values.get("thing_type_name")
        assert result is not None, "Required property 'thing_type_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThingTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.TopicRuleDestinationReference",
    jsii_struct_bases=[],
    name_mapping={"topic_rule_destination_arn": "topicRuleDestinationArn"},
)
class TopicRuleDestinationReference:
    def __init__(self, *, topic_rule_destination_arn: builtins.str) -> None:
        '''A reference to a TopicRuleDestination resource.

        :param topic_rule_destination_arn: The Arn of the TopicRuleDestination resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            topic_rule_destination_reference = interfaces_iot.TopicRuleDestinationReference(
                topic_rule_destination_arn="topicRuleDestinationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e74d82455f870901ea2e2fbfbe2edb86ed538ee10667e8514ee1fa6b73ddfc43)
            check_type(argname="argument topic_rule_destination_arn", value=topic_rule_destination_arn, expected_type=type_hints["topic_rule_destination_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topic_rule_destination_arn": topic_rule_destination_arn,
        }

    @builtins.property
    def topic_rule_destination_arn(self) -> builtins.str:
        '''The Arn of the TopicRuleDestination resource.'''
        result = self._values.get("topic_rule_destination_arn")
        assert result is not None, "Required property 'topic_rule_destination_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicRuleDestinationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iot.TopicRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_name": "ruleName", "topic_rule_arn": "topicRuleArn"},
)
class TopicRuleReference:
    def __init__(
        self,
        *,
        rule_name: builtins.str,
        topic_rule_arn: builtins.str,
    ) -> None:
        '''A reference to a TopicRule resource.

        :param rule_name: The RuleName of the TopicRule resource.
        :param topic_rule_arn: The ARN of the TopicRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iot as interfaces_iot
            
            topic_rule_reference = interfaces_iot.TopicRuleReference(
                rule_name="ruleName",
                topic_rule_arn="topicRuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eedeb429f63d21682b03ce0a579ac335118e4919a1318e377d4376db9481ee96)
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument topic_rule_arn", value=topic_rule_arn, expected_type=type_hints["topic_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_name": rule_name,
            "topic_rule_arn": topic_rule_arn,
        }

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The RuleName of the TopicRule resource.'''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_rule_arn(self) -> builtins.str:
        '''The ARN of the TopicRule resource.'''
        result = self._values.get("topic_rule_arn")
        assert result is not None, "Required property 'topic_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccountAuditConfigurationReference",
    "AuthorizerReference",
    "BillingGroupReference",
    "CACertificateReference",
    "CertificateProviderReference",
    "CertificateReference",
    "CommandReference",
    "CustomMetricReference",
    "DimensionReference",
    "DomainConfigurationReference",
    "EncryptionConfigurationReference",
    "FleetMetricReference",
    "IAccountAuditConfigurationRef",
    "IAuthorizerRef",
    "IBillingGroupRef",
    "ICACertificateRef",
    "ICertificateProviderRef",
    "ICertificateRef",
    "ICommandRef",
    "ICustomMetricRef",
    "IDimensionRef",
    "IDomainConfigurationRef",
    "IEncryptionConfigurationRef",
    "IFleetMetricRef",
    "IJobTemplateRef",
    "ILoggingRef",
    "IMitigationActionRef",
    "IPolicyPrincipalAttachmentRef",
    "IPolicyRef",
    "IProvisioningTemplateRef",
    "IResourceSpecificLoggingRef",
    "IRoleAliasRef",
    "IScheduledAuditRef",
    "ISecurityProfileRef",
    "ISoftwarePackageRef",
    "ISoftwarePackageVersionRef",
    "IThingGroupRef",
    "IThingPrincipalAttachmentRef",
    "IThingRef",
    "IThingTypeRef",
    "ITopicRuleDestinationRef",
    "ITopicRuleRef",
    "JobTemplateReference",
    "LoggingReference",
    "MitigationActionReference",
    "PolicyPrincipalAttachmentReference",
    "PolicyReference",
    "ProvisioningTemplateReference",
    "ResourceSpecificLoggingReference",
    "RoleAliasReference",
    "ScheduledAuditReference",
    "SecurityProfileReference",
    "SoftwarePackageReference",
    "SoftwarePackageVersionReference",
    "ThingGroupReference",
    "ThingPrincipalAttachmentReference",
    "ThingReference",
    "ThingTypeReference",
    "TopicRuleDestinationReference",
    "TopicRuleReference",
]

publication.publish()

def _typecheckingstub__146e26f046c491c18c156078309a07ab43070e0aa679f424eabb2687e3ad85d0(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a589da36a530a5f515e3fd2fa870b4aa7cab41b13bb204655a59aed307070a1(
    *,
    authorizer_arn: builtins.str,
    authorizer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9703280c049fd51220a0f708d3432e0c796ca6ec022914d413a76a17b8f3a4f0(
    *,
    billing_group_arn: builtins.str,
    billing_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85bd9181b7bb427b113fea2b8232f3f1f865da0f77891a59319ebd98727b69e2(
    *,
    ca_certificate_arn: builtins.str,
    ca_certificate_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c7ece71d0f471a8be87b66e2a7c9c527cee538e2a3927e0c9a8d36386fc71d0(
    *,
    certificate_provider_arn: builtins.str,
    certificate_provider_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd41822bb856d2c4cd7bfd1b33e1f7ae9aa20fabf6771532f867575bce52ca14(
    *,
    certificate_arn: builtins.str,
    certificate_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af71183d16426d8accbf974b433d009aa255f59da4af7ca7356d9ebd5c8b333(
    *,
    command_arn: builtins.str,
    command_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fc6d149631e90be2dff15aa19b30410d2c3183ced2ee13cdcb1d0ba90a3bbc8(
    *,
    metric_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536bc66020b6f87b8fa03df1825e2fdd22350c7cab5f996602e34be7f5af3874(
    *,
    dimension_arn: builtins.str,
    dimension_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__072a2a0f202205af6e3de264c0d6baafb0bd344109806fb009fb406885e493b8(
    *,
    domain_configuration_arn: builtins.str,
    domain_configuration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4243e6eeb1178b52ca431a8df25777c644a24a26ede98fac89e27a981c283fdb(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87bcc885b51342fc4a7fd186621f27ba55cc31a51b3cd22d20675d422894e639(
    *,
    metric_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffd41be04fe17710e1be7db9d085434eb15f2abdfafdc430d120ed83c4ec4aa(
    *,
    job_template_arn: builtins.str,
    job_template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f6f67c551d1d6d5b9be87e433d3ac8b37687437ee923fe545bbabcfdaadd98(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab56eb3d521febcf038be8ef1e03908bd95582acb3cf3b9cac5d7c92db5e09f(
    *,
    action_name: builtins.str,
    mitigation_action_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c433b17a937fb1b126780e6e4b459921a745c39de25b681aa6e87feb4111932(
    *,
    policy_principal_attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b627d7889748208bffcd4d74e49d11968847654f52f8d4d0b508b1333b01f6aa(
    *,
    policy_arn: builtins.str,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9039c63005bab6ff59546e15433165533243c424a4b0053c5aef2e6ff1affb7(
    *,
    template_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ebce77dbfe0456eff9639b6385561d6943a5d17fba95d1f552eed0e95bbf6b0(
    *,
    target_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a120b8f8d83a7dded11d9f9de72d69d5ca598d6ec190c3d6340acb452f28b5(
    *,
    role_alias: builtins.str,
    role_alias_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d8201b72f88cdd64cd19128a2c60aeded5bd7dc74179f5252602f226054061(
    *,
    scheduled_audit_arn: builtins.str,
    scheduled_audit_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf43e9f4ab30ee59ab380489311b985cbddf07f1dc8cdccc91ca1cf38ce9637(
    *,
    security_profile_arn: builtins.str,
    security_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb6ad3330b82f009179276f80acdee16561cdc42f31b2d0af96bfb331b6421f9(
    *,
    package_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8549067511c3dd9b2931691a58ae4f172a4d90a25349fe4ef5b45920e28a073e(
    *,
    package_name: builtins.str,
    version_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf577bbf82c8129b7cff9884cac80e23395d69657fd40c3d65bef791576507a6(
    *,
    thing_group_arn: builtins.str,
    thing_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43efd3fd743ae12945fd439b22b4a32cf10787e7ffe3bb66b57eb430a483d631(
    *,
    thing_principal_attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94282163e56abff7455704452ffdb9ea32a695f0a0a1add365fa6d4b15af02ab(
    *,
    thing_arn: builtins.str,
    thing_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__292b49d0fadd16c5715ae5ae5da4c61db1f6938820c0abd38301fc02146dc02e(
    *,
    thing_type_arn: builtins.str,
    thing_type_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e74d82455f870901ea2e2fbfbe2edb86ed538ee10667e8514ee1fa6b73ddfc43(
    *,
    topic_rule_destination_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eedeb429f63d21682b03ce0a579ac335118e4919a1318e377d4376db9481ee96(
    *,
    rule_name: builtins.str,
    topic_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccountAuditConfigurationRef, IAuthorizerRef, IBillingGroupRef, ICACertificateRef, ICertificateProviderRef, ICertificateRef, ICommandRef, ICustomMetricRef, IDimensionRef, IDomainConfigurationRef, IEncryptionConfigurationRef, IFleetMetricRef, IJobTemplateRef, ILoggingRef, IMitigationActionRef, IPolicyPrincipalAttachmentRef, IPolicyRef, IProvisioningTemplateRef, IResourceSpecificLoggingRef, IRoleAliasRef, IScheduledAuditRef, ISecurityProfileRef, ISoftwarePackageRef, ISoftwarePackageVersionRef, IThingGroupRef, IThingPrincipalAttachmentRef, IThingRef, IThingTypeRef, ITopicRuleDestinationRef, ITopicRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
