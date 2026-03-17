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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.IOrganizationCentralizationRuleRef"
)
class IOrganizationCentralizationRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationCentralizationRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationCentralizationRuleRef")
    def organization_centralization_rule_ref(
        self,
    ) -> "OrganizationCentralizationRuleReference":
        '''(experimental) A reference to a OrganizationCentralizationRule resource.

        :stability: experimental
        '''
        ...


class _IOrganizationCentralizationRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationCentralizationRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_observabilityadmin.IOrganizationCentralizationRuleRef"

    @builtins.property
    @jsii.member(jsii_name="organizationCentralizationRuleRef")
    def organization_centralization_rule_ref(
        self,
    ) -> "OrganizationCentralizationRuleReference":
        '''(experimental) A reference to a OrganizationCentralizationRule resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationCentralizationRuleReference", jsii.get(self, "organizationCentralizationRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationCentralizationRuleRef).__jsii_proxy_class__ = lambda : _IOrganizationCentralizationRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.IOrganizationTelemetryRuleRef"
)
class IOrganizationTelemetryRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationTelemetryRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationTelemetryRuleRef")
    def organization_telemetry_rule_ref(self) -> "OrganizationTelemetryRuleReference":
        '''(experimental) A reference to a OrganizationTelemetryRule resource.

        :stability: experimental
        '''
        ...


class _IOrganizationTelemetryRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationTelemetryRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_observabilityadmin.IOrganizationTelemetryRuleRef"

    @builtins.property
    @jsii.member(jsii_name="organizationTelemetryRuleRef")
    def organization_telemetry_rule_ref(self) -> "OrganizationTelemetryRuleReference":
        '''(experimental) A reference to a OrganizationTelemetryRule resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationTelemetryRuleReference", jsii.get(self, "organizationTelemetryRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationTelemetryRuleRef).__jsii_proxy_class__ = lambda : _IOrganizationTelemetryRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.IS3TableIntegrationRef"
)
class IS3TableIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a S3TableIntegration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="s3TableIntegrationRef")
    def s3_table_integration_ref(self) -> "S3TableIntegrationReference":
        '''(experimental) A reference to a S3TableIntegration resource.

        :stability: experimental
        '''
        ...


class _IS3TableIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a S3TableIntegration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_observabilityadmin.IS3TableIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="s3TableIntegrationRef")
    def s3_table_integration_ref(self) -> "S3TableIntegrationReference":
        '''(experimental) A reference to a S3TableIntegration resource.

        :stability: experimental
        '''
        return typing.cast("S3TableIntegrationReference", jsii.get(self, "s3TableIntegrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IS3TableIntegrationRef).__jsii_proxy_class__ = lambda : _IS3TableIntegrationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.ITelemetryPipelinesRef"
)
class ITelemetryPipelinesRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TelemetryPipelines.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="telemetryPipelinesRef")
    def telemetry_pipelines_ref(self) -> "TelemetryPipelinesReference":
        '''(experimental) A reference to a TelemetryPipelines resource.

        :stability: experimental
        '''
        ...


class _ITelemetryPipelinesRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TelemetryPipelines.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_observabilityadmin.ITelemetryPipelinesRef"

    @builtins.property
    @jsii.member(jsii_name="telemetryPipelinesRef")
    def telemetry_pipelines_ref(self) -> "TelemetryPipelinesReference":
        '''(experimental) A reference to a TelemetryPipelines resource.

        :stability: experimental
        '''
        return typing.cast("TelemetryPipelinesReference", jsii.get(self, "telemetryPipelinesRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITelemetryPipelinesRef).__jsii_proxy_class__ = lambda : _ITelemetryPipelinesRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.ITelemetryRuleRef"
)
class ITelemetryRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TelemetryRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="telemetryRuleRef")
    def telemetry_rule_ref(self) -> "TelemetryRuleReference":
        '''(experimental) A reference to a TelemetryRule resource.

        :stability: experimental
        '''
        ...


class _ITelemetryRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TelemetryRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_observabilityadmin.ITelemetryRuleRef"

    @builtins.property
    @jsii.member(jsii_name="telemetryRuleRef")
    def telemetry_rule_ref(self) -> "TelemetryRuleReference":
        '''(experimental) A reference to a TelemetryRule resource.

        :stability: experimental
        '''
        return typing.cast("TelemetryRuleReference", jsii.get(self, "telemetryRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITelemetryRuleRef).__jsii_proxy_class__ = lambda : _ITelemetryRuleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.OrganizationCentralizationRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class OrganizationCentralizationRuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a OrganizationCentralizationRule resource.

        :param rule_arn: The RuleArn of the OrganizationCentralizationRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_observabilityadmin as interfaces_observabilityadmin
            
            organization_centralization_rule_reference = interfaces_observabilityadmin.OrganizationCentralizationRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__954ef56f547b852ec9d4a111054e5601faba2a807f7124bccca33ab6f2a56d71)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the OrganizationCentralizationRule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationCentralizationRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.OrganizationTelemetryRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class OrganizationTelemetryRuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a OrganizationTelemetryRule resource.

        :param rule_arn: The RuleArn of the OrganizationTelemetryRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_observabilityadmin as interfaces_observabilityadmin
            
            organization_telemetry_rule_reference = interfaces_observabilityadmin.OrganizationTelemetryRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbaa448311f6f304eaa3b8b6adb9dd50b4accec2ca25b614d9e0cbd75cd36503)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the OrganizationTelemetryRule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationTelemetryRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.S3TableIntegrationReference",
    jsii_struct_bases=[],
    name_mapping={"s3_table_integration_arn": "s3TableIntegrationArn"},
)
class S3TableIntegrationReference:
    def __init__(self, *, s3_table_integration_arn: builtins.str) -> None:
        '''A reference to a S3TableIntegration resource.

        :param s3_table_integration_arn: The Arn of the S3TableIntegration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_observabilityadmin as interfaces_observabilityadmin
            
            s3_table_integration_reference = interfaces_observabilityadmin.S3TableIntegrationReference(
                s3_table_integration_arn="s3TableIntegrationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a129f29e2d687950d49f2d71dcabb911b4d152b80fc935b47eff900bdb4f7332)
            check_type(argname="argument s3_table_integration_arn", value=s3_table_integration_arn, expected_type=type_hints["s3_table_integration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "s3_table_integration_arn": s3_table_integration_arn,
        }

    @builtins.property
    def s3_table_integration_arn(self) -> builtins.str:
        '''The Arn of the S3TableIntegration resource.'''
        result = self._values.get("s3_table_integration_arn")
        assert result is not None, "Required property 's3_table_integration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3TableIntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.TelemetryPipelinesReference",
    jsii_struct_bases=[],
    name_mapping={
        "pipeline_identifier": "pipelineIdentifier",
        "telemetry_pipelines_arn": "telemetryPipelinesArn",
    },
)
class TelemetryPipelinesReference:
    def __init__(
        self,
        *,
        pipeline_identifier: builtins.str,
        telemetry_pipelines_arn: builtins.str,
    ) -> None:
        '''A reference to a TelemetryPipelines resource.

        :param pipeline_identifier: The PipelineIdentifier of the TelemetryPipelines resource.
        :param telemetry_pipelines_arn: The ARN of the TelemetryPipelines resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_observabilityadmin as interfaces_observabilityadmin
            
            telemetry_pipelines_reference = interfaces_observabilityadmin.TelemetryPipelinesReference(
                pipeline_identifier="pipelineIdentifier",
                telemetry_pipelines_arn="telemetryPipelinesArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24c90824fbeb949eef9156de96b282679aefd592395a4d1dd12f1cd2d46e4624)
            check_type(argname="argument pipeline_identifier", value=pipeline_identifier, expected_type=type_hints["pipeline_identifier"])
            check_type(argname="argument telemetry_pipelines_arn", value=telemetry_pipelines_arn, expected_type=type_hints["telemetry_pipelines_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pipeline_identifier": pipeline_identifier,
            "telemetry_pipelines_arn": telemetry_pipelines_arn,
        }

    @builtins.property
    def pipeline_identifier(self) -> builtins.str:
        '''The PipelineIdentifier of the TelemetryPipelines resource.'''
        result = self._values.get("pipeline_identifier")
        assert result is not None, "Required property 'pipeline_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def telemetry_pipelines_arn(self) -> builtins.str:
        '''The ARN of the TelemetryPipelines resource.'''
        result = self._values.get("telemetry_pipelines_arn")
        assert result is not None, "Required property 'telemetry_pipelines_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetryPipelinesReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_observabilityadmin.TelemetryRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class TelemetryRuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a TelemetryRule resource.

        :param rule_arn: The RuleArn of the TelemetryRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_observabilityadmin as interfaces_observabilityadmin
            
            telemetry_rule_reference = interfaces_observabilityadmin.TelemetryRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f3442b866c7be36ef85439dc80d47ed5cfc8d0a761fa5260939a94726bf2f76)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the TelemetryRule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TelemetryRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IOrganizationCentralizationRuleRef",
    "IOrganizationTelemetryRuleRef",
    "IS3TableIntegrationRef",
    "ITelemetryPipelinesRef",
    "ITelemetryRuleRef",
    "OrganizationCentralizationRuleReference",
    "OrganizationTelemetryRuleReference",
    "S3TableIntegrationReference",
    "TelemetryPipelinesReference",
    "TelemetryRuleReference",
]

publication.publish()

def _typecheckingstub__954ef56f547b852ec9d4a111054e5601faba2a807f7124bccca33ab6f2a56d71(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbaa448311f6f304eaa3b8b6adb9dd50b4accec2ca25b614d9e0cbd75cd36503(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a129f29e2d687950d49f2d71dcabb911b4d152b80fc935b47eff900bdb4f7332(
    *,
    s3_table_integration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24c90824fbeb949eef9156de96b282679aefd592395a4d1dd12f1cd2d46e4624(
    *,
    pipeline_identifier: builtins.str,
    telemetry_pipelines_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f3442b866c7be36ef85439dc80d47ed5cfc8d0a761fa5260939a94726bf2f76(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IOrganizationCentralizationRuleRef, IOrganizationTelemetryRuleRef, IS3TableIntegrationRef, ITelemetryPipelinesRef, ITelemetryRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
