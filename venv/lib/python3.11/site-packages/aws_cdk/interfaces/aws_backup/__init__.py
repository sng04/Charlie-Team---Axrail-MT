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
    jsii_type="aws-cdk-lib.interfaces.aws_backup.BackupPlanReference",
    jsii_struct_bases=[],
    name_mapping={
        "backup_plan_arn": "backupPlanArn",
        "backup_plan_id": "backupPlanId",
    },
)
class BackupPlanReference:
    def __init__(
        self,
        *,
        backup_plan_arn: builtins.str,
        backup_plan_id: builtins.str,
    ) -> None:
        '''A reference to a BackupPlan resource.

        :param backup_plan_arn: The ARN of the BackupPlan resource.
        :param backup_plan_id: The BackupPlanId of the BackupPlan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_backup as interfaces_backup
            
            backup_plan_reference = interfaces_backup.BackupPlanReference(
                backup_plan_arn="backupPlanArn",
                backup_plan_id="backupPlanId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a77079e1b20aa3ac92fe146c61c7fbe6e5dbf5c8e182f93cd84530d8527a86c)
            check_type(argname="argument backup_plan_arn", value=backup_plan_arn, expected_type=type_hints["backup_plan_arn"])
            check_type(argname="argument backup_plan_id", value=backup_plan_id, expected_type=type_hints["backup_plan_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_plan_arn": backup_plan_arn,
            "backup_plan_id": backup_plan_id,
        }

    @builtins.property
    def backup_plan_arn(self) -> builtins.str:
        '''The ARN of the BackupPlan resource.'''
        result = self._values.get("backup_plan_arn")
        assert result is not None, "Required property 'backup_plan_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backup_plan_id(self) -> builtins.str:
        '''The BackupPlanId of the BackupPlan resource.'''
        result = self._values.get("backup_plan_id")
        assert result is not None, "Required property 'backup_plan_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupPlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.BackupSelectionReference",
    jsii_struct_bases=[],
    name_mapping={"backup_selection_id": "backupSelectionId"},
)
class BackupSelectionReference:
    def __init__(self, *, backup_selection_id: builtins.str) -> None:
        '''A reference to a BackupSelection resource.

        :param backup_selection_id: The Id of the BackupSelection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_backup as interfaces_backup
            
            backup_selection_reference = interfaces_backup.BackupSelectionReference(
                backup_selection_id="backupSelectionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa6e9d1cc32cb328e42920a9a5ef76b40c2def12f8c14e2dbd345a29c78eff8d)
            check_type(argname="argument backup_selection_id", value=backup_selection_id, expected_type=type_hints["backup_selection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_selection_id": backup_selection_id,
        }

    @builtins.property
    def backup_selection_id(self) -> builtins.str:
        '''The Id of the BackupSelection resource.'''
        result = self._values.get("backup_selection_id")
        assert result is not None, "Required property 'backup_selection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupSelectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.BackupVaultReference",
    jsii_struct_bases=[],
    name_mapping={
        "backup_vault_arn": "backupVaultArn",
        "backup_vault_name": "backupVaultName",
    },
)
class BackupVaultReference:
    def __init__(
        self,
        *,
        backup_vault_arn: builtins.str,
        backup_vault_name: builtins.str,
    ) -> None:
        '''A reference to a BackupVault resource.

        :param backup_vault_arn: The ARN of the BackupVault resource.
        :param backup_vault_name: The BackupVaultName of the BackupVault resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_backup as interfaces_backup
            
            backup_vault_reference = interfaces_backup.BackupVaultReference(
                backup_vault_arn="backupVaultArn",
                backup_vault_name="backupVaultName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5af0184161160d25bde07c18f7ff0302737896654b6080404dee97165575ee6a)
            check_type(argname="argument backup_vault_arn", value=backup_vault_arn, expected_type=type_hints["backup_vault_arn"])
            check_type(argname="argument backup_vault_name", value=backup_vault_name, expected_type=type_hints["backup_vault_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_vault_arn": backup_vault_arn,
            "backup_vault_name": backup_vault_name,
        }

    @builtins.property
    def backup_vault_arn(self) -> builtins.str:
        '''The ARN of the BackupVault resource.'''
        result = self._values.get("backup_vault_arn")
        assert result is not None, "Required property 'backup_vault_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backup_vault_name(self) -> builtins.str:
        '''The BackupVaultName of the BackupVault resource.'''
        result = self._values.get("backup_vault_name")
        assert result is not None, "Required property 'backup_vault_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackupVaultReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.FrameworkReference",
    jsii_struct_bases=[],
    name_mapping={"framework_arn": "frameworkArn"},
)
class FrameworkReference:
    def __init__(self, *, framework_arn: builtins.str) -> None:
        '''A reference to a Framework resource.

        :param framework_arn: The FrameworkArn of the Framework resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_backup as interfaces_backup
            
            framework_reference = interfaces_backup.FrameworkReference(
                framework_arn="frameworkArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9208e01f3f2fa93dada1794b4e883d88008205648db75087779eae32c2fd686)
            check_type(argname="argument framework_arn", value=framework_arn, expected_type=type_hints["framework_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "framework_arn": framework_arn,
        }

    @builtins.property
    def framework_arn(self) -> builtins.str:
        '''The FrameworkArn of the Framework resource.'''
        result = self._values.get("framework_arn")
        assert result is not None, "Required property 'framework_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FrameworkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_backup.IBackupPlanRef")
class IBackupPlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BackupPlan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="backupPlanRef")
    def backup_plan_ref(self) -> "BackupPlanReference":
        '''(experimental) A reference to a BackupPlan resource.

        :stability: experimental
        '''
        ...


class _IBackupPlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BackupPlan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_backup.IBackupPlanRef"

    @builtins.property
    @jsii.member(jsii_name="backupPlanRef")
    def backup_plan_ref(self) -> "BackupPlanReference":
        '''(experimental) A reference to a BackupPlan resource.

        :stability: experimental
        '''
        return typing.cast("BackupPlanReference", jsii.get(self, "backupPlanRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBackupPlanRef).__jsii_proxy_class__ = lambda : _IBackupPlanRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_backup.IBackupSelectionRef")
class IBackupSelectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BackupSelection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="backupSelectionRef")
    def backup_selection_ref(self) -> "BackupSelectionReference":
        '''(experimental) A reference to a BackupSelection resource.

        :stability: experimental
        '''
        ...


class _IBackupSelectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BackupSelection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_backup.IBackupSelectionRef"

    @builtins.property
    @jsii.member(jsii_name="backupSelectionRef")
    def backup_selection_ref(self) -> "BackupSelectionReference":
        '''(experimental) A reference to a BackupSelection resource.

        :stability: experimental
        '''
        return typing.cast("BackupSelectionReference", jsii.get(self, "backupSelectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBackupSelectionRef).__jsii_proxy_class__ = lambda : _IBackupSelectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_backup.IBackupVaultRef")
class IBackupVaultRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BackupVault.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="backupVaultRef")
    def backup_vault_ref(self) -> "BackupVaultReference":
        '''(experimental) A reference to a BackupVault resource.

        :stability: experimental
        '''
        ...


class _IBackupVaultRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BackupVault.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_backup.IBackupVaultRef"

    @builtins.property
    @jsii.member(jsii_name="backupVaultRef")
    def backup_vault_ref(self) -> "BackupVaultReference":
        '''(experimental) A reference to a BackupVault resource.

        :stability: experimental
        '''
        return typing.cast("BackupVaultReference", jsii.get(self, "backupVaultRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBackupVaultRef).__jsii_proxy_class__ = lambda : _IBackupVaultRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_backup.IFrameworkRef")
class IFrameworkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Framework.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="frameworkRef")
    def framework_ref(self) -> "FrameworkReference":
        '''(experimental) A reference to a Framework resource.

        :stability: experimental
        '''
        ...


class _IFrameworkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Framework.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_backup.IFrameworkRef"

    @builtins.property
    @jsii.member(jsii_name="frameworkRef")
    def framework_ref(self) -> "FrameworkReference":
        '''(experimental) A reference to a Framework resource.

        :stability: experimental
        '''
        return typing.cast("FrameworkReference", jsii.get(self, "frameworkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFrameworkRef).__jsii_proxy_class__ = lambda : _IFrameworkRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.ILogicallyAirGappedBackupVaultRef"
)
class ILogicallyAirGappedBackupVaultRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LogicallyAirGappedBackupVault.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="logicallyAirGappedBackupVaultRef")
    def logically_air_gapped_backup_vault_ref(
        self,
    ) -> "LogicallyAirGappedBackupVaultReference":
        '''(experimental) A reference to a LogicallyAirGappedBackupVault resource.

        :stability: experimental
        '''
        ...


class _ILogicallyAirGappedBackupVaultRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LogicallyAirGappedBackupVault.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_backup.ILogicallyAirGappedBackupVaultRef"

    @builtins.property
    @jsii.member(jsii_name="logicallyAirGappedBackupVaultRef")
    def logically_air_gapped_backup_vault_ref(
        self,
    ) -> "LogicallyAirGappedBackupVaultReference":
        '''(experimental) A reference to a LogicallyAirGappedBackupVault resource.

        :stability: experimental
        '''
        return typing.cast("LogicallyAirGappedBackupVaultReference", jsii.get(self, "logicallyAirGappedBackupVaultRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogicallyAirGappedBackupVaultRef).__jsii_proxy_class__ = lambda : _ILogicallyAirGappedBackupVaultRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_backup.IReportPlanRef")
class IReportPlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReportPlan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="reportPlanRef")
    def report_plan_ref(self) -> "ReportPlanReference":
        '''(experimental) A reference to a ReportPlan resource.

        :stability: experimental
        '''
        ...


class _IReportPlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReportPlan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_backup.IReportPlanRef"

    @builtins.property
    @jsii.member(jsii_name="reportPlanRef")
    def report_plan_ref(self) -> "ReportPlanReference":
        '''(experimental) A reference to a ReportPlan resource.

        :stability: experimental
        '''
        return typing.cast("ReportPlanReference", jsii.get(self, "reportPlanRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReportPlanRef).__jsii_proxy_class__ = lambda : _IReportPlanRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_backup.IRestoreTestingPlanRef")
class IRestoreTestingPlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RestoreTestingPlan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="restoreTestingPlanRef")
    def restore_testing_plan_ref(self) -> "RestoreTestingPlanReference":
        '''(experimental) A reference to a RestoreTestingPlan resource.

        :stability: experimental
        '''
        ...


class _IRestoreTestingPlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RestoreTestingPlan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_backup.IRestoreTestingPlanRef"

    @builtins.property
    @jsii.member(jsii_name="restoreTestingPlanRef")
    def restore_testing_plan_ref(self) -> "RestoreTestingPlanReference":
        '''(experimental) A reference to a RestoreTestingPlan resource.

        :stability: experimental
        '''
        return typing.cast("RestoreTestingPlanReference", jsii.get(self, "restoreTestingPlanRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRestoreTestingPlanRef).__jsii_proxy_class__ = lambda : _IRestoreTestingPlanRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.IRestoreTestingSelectionRef"
)
class IRestoreTestingSelectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RestoreTestingSelection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="restoreTestingSelectionRef")
    def restore_testing_selection_ref(self) -> "RestoreTestingSelectionReference":
        '''(experimental) A reference to a RestoreTestingSelection resource.

        :stability: experimental
        '''
        ...


class _IRestoreTestingSelectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RestoreTestingSelection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_backup.IRestoreTestingSelectionRef"

    @builtins.property
    @jsii.member(jsii_name="restoreTestingSelectionRef")
    def restore_testing_selection_ref(self) -> "RestoreTestingSelectionReference":
        '''(experimental) A reference to a RestoreTestingSelection resource.

        :stability: experimental
        '''
        return typing.cast("RestoreTestingSelectionReference", jsii.get(self, "restoreTestingSelectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRestoreTestingSelectionRef).__jsii_proxy_class__ = lambda : _IRestoreTestingSelectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_backup.ITieringConfigurationRef")
class ITieringConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TieringConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tieringConfigurationRef")
    def tiering_configuration_ref(self) -> "TieringConfigurationReference":
        '''(experimental) A reference to a TieringConfiguration resource.

        :stability: experimental
        '''
        ...


class _ITieringConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TieringConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_backup.ITieringConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="tieringConfigurationRef")
    def tiering_configuration_ref(self) -> "TieringConfigurationReference":
        '''(experimental) A reference to a TieringConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("TieringConfigurationReference", jsii.get(self, "tieringConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITieringConfigurationRef).__jsii_proxy_class__ = lambda : _ITieringConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.LogicallyAirGappedBackupVaultReference",
    jsii_struct_bases=[],
    name_mapping={"backup_vault_name": "backupVaultName"},
)
class LogicallyAirGappedBackupVaultReference:
    def __init__(self, *, backup_vault_name: builtins.str) -> None:
        '''A reference to a LogicallyAirGappedBackupVault resource.

        :param backup_vault_name: The BackupVaultName of the LogicallyAirGappedBackupVault resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_backup as interfaces_backup
            
            logically_air_gapped_backup_vault_reference = interfaces_backup.LogicallyAirGappedBackupVaultReference(
                backup_vault_name="backupVaultName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd6d881ce3a7fcd23239f41692330b56b4e404d0f65dba0ecfb5f1e7e2d66e37)
            check_type(argname="argument backup_vault_name", value=backup_vault_name, expected_type=type_hints["backup_vault_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backup_vault_name": backup_vault_name,
        }

    @builtins.property
    def backup_vault_name(self) -> builtins.str:
        '''The BackupVaultName of the LogicallyAirGappedBackupVault resource.'''
        result = self._values.get("backup_vault_name")
        assert result is not None, "Required property 'backup_vault_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogicallyAirGappedBackupVaultReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.ReportPlanReference",
    jsii_struct_bases=[],
    name_mapping={"report_plan_arn": "reportPlanArn"},
)
class ReportPlanReference:
    def __init__(self, *, report_plan_arn: builtins.str) -> None:
        '''A reference to a ReportPlan resource.

        :param report_plan_arn: The ReportPlanArn of the ReportPlan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_backup as interfaces_backup
            
            report_plan_reference = interfaces_backup.ReportPlanReference(
                report_plan_arn="reportPlanArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e14b1b1589fa26c0b02d2ec6412c42d2edc39d661213cea5340023281023ceb)
            check_type(argname="argument report_plan_arn", value=report_plan_arn, expected_type=type_hints["report_plan_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "report_plan_arn": report_plan_arn,
        }

    @builtins.property
    def report_plan_arn(self) -> builtins.str:
        '''The ReportPlanArn of the ReportPlan resource.'''
        result = self._values.get("report_plan_arn")
        assert result is not None, "Required property 'report_plan_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReportPlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.RestoreTestingPlanReference",
    jsii_struct_bases=[],
    name_mapping={
        "restore_testing_plan_arn": "restoreTestingPlanArn",
        "restore_testing_plan_name": "restoreTestingPlanName",
    },
)
class RestoreTestingPlanReference:
    def __init__(
        self,
        *,
        restore_testing_plan_arn: builtins.str,
        restore_testing_plan_name: builtins.str,
    ) -> None:
        '''A reference to a RestoreTestingPlan resource.

        :param restore_testing_plan_arn: The ARN of the RestoreTestingPlan resource.
        :param restore_testing_plan_name: The RestoreTestingPlanName of the RestoreTestingPlan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_backup as interfaces_backup
            
            restore_testing_plan_reference = interfaces_backup.RestoreTestingPlanReference(
                restore_testing_plan_arn="restoreTestingPlanArn",
                restore_testing_plan_name="restoreTestingPlanName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b57e829b5ee97cfa44e5dee464dcd7972373f8a282a3c8fea7bc76b2ca0726b7)
            check_type(argname="argument restore_testing_plan_arn", value=restore_testing_plan_arn, expected_type=type_hints["restore_testing_plan_arn"])
            check_type(argname="argument restore_testing_plan_name", value=restore_testing_plan_name, expected_type=type_hints["restore_testing_plan_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "restore_testing_plan_arn": restore_testing_plan_arn,
            "restore_testing_plan_name": restore_testing_plan_name,
        }

    @builtins.property
    def restore_testing_plan_arn(self) -> builtins.str:
        '''The ARN of the RestoreTestingPlan resource.'''
        result = self._values.get("restore_testing_plan_arn")
        assert result is not None, "Required property 'restore_testing_plan_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def restore_testing_plan_name(self) -> builtins.str:
        '''The RestoreTestingPlanName of the RestoreTestingPlan resource.'''
        result = self._values.get("restore_testing_plan_name")
        assert result is not None, "Required property 'restore_testing_plan_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RestoreTestingPlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.RestoreTestingSelectionReference",
    jsii_struct_bases=[],
    name_mapping={
        "restore_testing_plan_name": "restoreTestingPlanName",
        "restore_testing_selection_name": "restoreTestingSelectionName",
    },
)
class RestoreTestingSelectionReference:
    def __init__(
        self,
        *,
        restore_testing_plan_name: builtins.str,
        restore_testing_selection_name: builtins.str,
    ) -> None:
        '''A reference to a RestoreTestingSelection resource.

        :param restore_testing_plan_name: The RestoreTestingPlanName of the RestoreTestingSelection resource.
        :param restore_testing_selection_name: The RestoreTestingSelectionName of the RestoreTestingSelection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_backup as interfaces_backup
            
            restore_testing_selection_reference = interfaces_backup.RestoreTestingSelectionReference(
                restore_testing_plan_name="restoreTestingPlanName",
                restore_testing_selection_name="restoreTestingSelectionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6873344f6558099662d6c3ff3f04f56bac4fc761ac9d664357b2e2f936f3a436)
            check_type(argname="argument restore_testing_plan_name", value=restore_testing_plan_name, expected_type=type_hints["restore_testing_plan_name"])
            check_type(argname="argument restore_testing_selection_name", value=restore_testing_selection_name, expected_type=type_hints["restore_testing_selection_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "restore_testing_plan_name": restore_testing_plan_name,
            "restore_testing_selection_name": restore_testing_selection_name,
        }

    @builtins.property
    def restore_testing_plan_name(self) -> builtins.str:
        '''The RestoreTestingPlanName of the RestoreTestingSelection resource.'''
        result = self._values.get("restore_testing_plan_name")
        assert result is not None, "Required property 'restore_testing_plan_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def restore_testing_selection_name(self) -> builtins.str:
        '''The RestoreTestingSelectionName of the RestoreTestingSelection resource.'''
        result = self._values.get("restore_testing_selection_name")
        assert result is not None, "Required property 'restore_testing_selection_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RestoreTestingSelectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_backup.TieringConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "tiering_configuration_arn": "tieringConfigurationArn",
        "tiering_configuration_name": "tieringConfigurationName",
    },
)
class TieringConfigurationReference:
    def __init__(
        self,
        *,
        tiering_configuration_arn: builtins.str,
        tiering_configuration_name: builtins.str,
    ) -> None:
        '''A reference to a TieringConfiguration resource.

        :param tiering_configuration_arn: The ARN of the TieringConfiguration resource.
        :param tiering_configuration_name: The TieringConfigurationName of the TieringConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_backup as interfaces_backup
            
            tiering_configuration_reference = interfaces_backup.TieringConfigurationReference(
                tiering_configuration_arn="tieringConfigurationArn",
                tiering_configuration_name="tieringConfigurationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c4ffd604d0acac2ed3572f6ad959173a1356f2c2bbb020e85ed859deceecf3e)
            check_type(argname="argument tiering_configuration_arn", value=tiering_configuration_arn, expected_type=type_hints["tiering_configuration_arn"])
            check_type(argname="argument tiering_configuration_name", value=tiering_configuration_name, expected_type=type_hints["tiering_configuration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tiering_configuration_arn": tiering_configuration_arn,
            "tiering_configuration_name": tiering_configuration_name,
        }

    @builtins.property
    def tiering_configuration_arn(self) -> builtins.str:
        '''The ARN of the TieringConfiguration resource.'''
        result = self._values.get("tiering_configuration_arn")
        assert result is not None, "Required property 'tiering_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tiering_configuration_name(self) -> builtins.str:
        '''The TieringConfigurationName of the TieringConfiguration resource.'''
        result = self._values.get("tiering_configuration_name")
        assert result is not None, "Required property 'tiering_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TieringConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BackupPlanReference",
    "BackupSelectionReference",
    "BackupVaultReference",
    "FrameworkReference",
    "IBackupPlanRef",
    "IBackupSelectionRef",
    "IBackupVaultRef",
    "IFrameworkRef",
    "ILogicallyAirGappedBackupVaultRef",
    "IReportPlanRef",
    "IRestoreTestingPlanRef",
    "IRestoreTestingSelectionRef",
    "ITieringConfigurationRef",
    "LogicallyAirGappedBackupVaultReference",
    "ReportPlanReference",
    "RestoreTestingPlanReference",
    "RestoreTestingSelectionReference",
    "TieringConfigurationReference",
]

publication.publish()

def _typecheckingstub__6a77079e1b20aa3ac92fe146c61c7fbe6e5dbf5c8e182f93cd84530d8527a86c(
    *,
    backup_plan_arn: builtins.str,
    backup_plan_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa6e9d1cc32cb328e42920a9a5ef76b40c2def12f8c14e2dbd345a29c78eff8d(
    *,
    backup_selection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5af0184161160d25bde07c18f7ff0302737896654b6080404dee97165575ee6a(
    *,
    backup_vault_arn: builtins.str,
    backup_vault_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9208e01f3f2fa93dada1794b4e883d88008205648db75087779eae32c2fd686(
    *,
    framework_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd6d881ce3a7fcd23239f41692330b56b4e404d0f65dba0ecfb5f1e7e2d66e37(
    *,
    backup_vault_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e14b1b1589fa26c0b02d2ec6412c42d2edc39d661213cea5340023281023ceb(
    *,
    report_plan_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b57e829b5ee97cfa44e5dee464dcd7972373f8a282a3c8fea7bc76b2ca0726b7(
    *,
    restore_testing_plan_arn: builtins.str,
    restore_testing_plan_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6873344f6558099662d6c3ff3f04f56bac4fc761ac9d664357b2e2f936f3a436(
    *,
    restore_testing_plan_name: builtins.str,
    restore_testing_selection_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4ffd604d0acac2ed3572f6ad959173a1356f2c2bbb020e85ed859deceecf3e(
    *,
    tiering_configuration_arn: builtins.str,
    tiering_configuration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBackupPlanRef, IBackupSelectionRef, IBackupVaultRef, IFrameworkRef, ILogicallyAirGappedBackupVaultRef, IReportPlanRef, IRestoreTestingPlanRef, IRestoreTestingSelectionRef, ITieringConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
