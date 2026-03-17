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
    jsii_type="aws-cdk-lib.interfaces.aws_codebuild.FleetReference",
    jsii_struct_bases=[],
    name_mapping={"fleet_arn": "fleetArn"},
)
class FleetReference:
    def __init__(self, *, fleet_arn: builtins.str) -> None:
        '''A reference to a Fleet resource.

        :param fleet_arn: The Arn of the Fleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codebuild as interfaces_codebuild
            
            fleet_reference = interfaces_codebuild.FleetReference(
                fleet_arn="fleetArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b252b09ea2d7a037ef7eb8c132fdc4bf9af5d216a313e3c3b3a3847f4e0d380c)
            check_type(argname="argument fleet_arn", value=fleet_arn, expected_type=type_hints["fleet_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_arn": fleet_arn,
        }

    @builtins.property
    def fleet_arn(self) -> builtins.str:
        '''The Arn of the Fleet resource.'''
        result = self._values.get("fleet_arn")
        assert result is not None, "Required property 'fleet_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codebuild.IFleetRef")
class IFleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        ...


class _IFleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codebuild.IFleetRef"

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        return typing.cast("FleetReference", jsii.get(self, "fleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFleetRef).__jsii_proxy_class__ = lambda : _IFleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codebuild.IProjectRef")
class IProjectRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Project.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        ...


class _IProjectRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Project.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codebuild.IProjectRef"

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        return typing.cast("ProjectReference", jsii.get(self, "projectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectRef).__jsii_proxy_class__ = lambda : _IProjectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codebuild.IReportGroupRef")
class IReportGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReportGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="reportGroupRef")
    def report_group_ref(self) -> "ReportGroupReference":
        '''(experimental) A reference to a ReportGroup resource.

        :stability: experimental
        '''
        ...


class _IReportGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReportGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codebuild.IReportGroupRef"

    @builtins.property
    @jsii.member(jsii_name="reportGroupRef")
    def report_group_ref(self) -> "ReportGroupReference":
        '''(experimental) A reference to a ReportGroup resource.

        :stability: experimental
        '''
        return typing.cast("ReportGroupReference", jsii.get(self, "reportGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReportGroupRef).__jsii_proxy_class__ = lambda : _IReportGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codebuild.ISourceCredentialRef")
class ISourceCredentialRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SourceCredential.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sourceCredentialRef")
    def source_credential_ref(self) -> "SourceCredentialReference":
        '''(experimental) A reference to a SourceCredential resource.

        :stability: experimental
        '''
        ...


class _ISourceCredentialRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SourceCredential.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codebuild.ISourceCredentialRef"

    @builtins.property
    @jsii.member(jsii_name="sourceCredentialRef")
    def source_credential_ref(self) -> "SourceCredentialReference":
        '''(experimental) A reference to a SourceCredential resource.

        :stability: experimental
        '''
        return typing.cast("SourceCredentialReference", jsii.get(self, "sourceCredentialRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISourceCredentialRef).__jsii_proxy_class__ = lambda : _ISourceCredentialRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codebuild.ProjectReference",
    jsii_struct_bases=[],
    name_mapping={"project_arn": "projectArn", "project_name": "projectName"},
)
class ProjectReference:
    def __init__(
        self,
        *,
        project_arn: builtins.str,
        project_name: builtins.str,
    ) -> None:
        '''A reference to a Project resource.

        :param project_arn: The ARN of the Project resource.
        :param project_name: The Name of the Project resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codebuild as interfaces_codebuild
            
            project_reference = interfaces_codebuild.ProjectReference(
                project_arn="projectArn",
                project_name="projectName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__938517d640cf480acbfa73e5d436dfdb8249909865744af5fcd6ced48675a435)
            check_type(argname="argument project_arn", value=project_arn, expected_type=type_hints["project_arn"])
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_arn": project_arn,
            "project_name": project_name,
        }

    @builtins.property
    def project_arn(self) -> builtins.str:
        '''The ARN of the Project resource.'''
        result = self._values.get("project_arn")
        assert result is not None, "Required property 'project_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_name(self) -> builtins.str:
        '''The Name of the Project resource.'''
        result = self._values.get("project_name")
        assert result is not None, "Required property 'project_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codebuild.ReportGroupReference",
    jsii_struct_bases=[],
    name_mapping={"report_group_arn": "reportGroupArn"},
)
class ReportGroupReference:
    def __init__(self, *, report_group_arn: builtins.str) -> None:
        '''A reference to a ReportGroup resource.

        :param report_group_arn: The Arn of the ReportGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codebuild as interfaces_codebuild
            
            report_group_reference = interfaces_codebuild.ReportGroupReference(
                report_group_arn="reportGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cd46ecb1a45984facc4fba5861d8c76e61cb467c28f418886f84499d8ece72c)
            check_type(argname="argument report_group_arn", value=report_group_arn, expected_type=type_hints["report_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "report_group_arn": report_group_arn,
        }

    @builtins.property
    def report_group_arn(self) -> builtins.str:
        '''The Arn of the ReportGroup resource.'''
        result = self._values.get("report_group_arn")
        assert result is not None, "Required property 'report_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReportGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codebuild.SourceCredentialReference",
    jsii_struct_bases=[],
    name_mapping={"source_credential_id": "sourceCredentialId"},
)
class SourceCredentialReference:
    def __init__(self, *, source_credential_id: builtins.str) -> None:
        '''A reference to a SourceCredential resource.

        :param source_credential_id: The Id of the SourceCredential resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codebuild as interfaces_codebuild
            
            source_credential_reference = interfaces_codebuild.SourceCredentialReference(
                source_credential_id="sourceCredentialId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1401c6ca94e02a490ee8ba6e38db6ee0841aa4f2e47c6995257d49aa5711a95c)
            check_type(argname="argument source_credential_id", value=source_credential_id, expected_type=type_hints["source_credential_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_credential_id": source_credential_id,
        }

    @builtins.property
    def source_credential_id(self) -> builtins.str:
        '''The Id of the SourceCredential resource.'''
        result = self._values.get("source_credential_id")
        assert result is not None, "Required property 'source_credential_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceCredentialReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "FleetReference",
    "IFleetRef",
    "IProjectRef",
    "IReportGroupRef",
    "ISourceCredentialRef",
    "ProjectReference",
    "ReportGroupReference",
    "SourceCredentialReference",
]

publication.publish()

def _typecheckingstub__b252b09ea2d7a037ef7eb8c132fdc4bf9af5d216a313e3c3b3a3847f4e0d380c(
    *,
    fleet_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__938517d640cf480acbfa73e5d436dfdb8249909865744af5fcd6ced48675a435(
    *,
    project_arn: builtins.str,
    project_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cd46ecb1a45984facc4fba5861d8c76e61cb467c28f418886f84499d8ece72c(
    *,
    report_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1401c6ca94e02a490ee8ba6e38db6ee0841aa4f2e47c6995257d49aa5711a95c(
    *,
    source_credential_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IFleetRef, IProjectRef, IReportGroupRef, ISourceCredentialRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
