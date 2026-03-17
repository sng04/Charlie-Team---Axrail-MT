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
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ActionConnectorReference",
    jsii_struct_bases=[],
    name_mapping={
        "action_connector_arn": "actionConnectorArn",
        "action_connector_id": "actionConnectorId",
        "aws_account_id": "awsAccountId",
    },
)
class ActionConnectorReference:
    def __init__(
        self,
        *,
        action_connector_arn: builtins.str,
        action_connector_id: builtins.str,
        aws_account_id: builtins.str,
    ) -> None:
        '''A reference to a ActionConnector resource.

        :param action_connector_arn: The ARN of the ActionConnector resource.
        :param action_connector_id: The ActionConnectorId of the ActionConnector resource.
        :param aws_account_id: The AwsAccountId of the ActionConnector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            action_connector_reference = interfaces_quicksight.ActionConnectorReference(
                action_connector_arn="actionConnectorArn",
                action_connector_id="actionConnectorId",
                aws_account_id="awsAccountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31055bc274e952c4fc3166d11f0fbbc107ed08b00575ccf7d73fa07a9e5f9f9f)
            check_type(argname="argument action_connector_arn", value=action_connector_arn, expected_type=type_hints["action_connector_arn"])
            check_type(argname="argument action_connector_id", value=action_connector_id, expected_type=type_hints["action_connector_id"])
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_connector_arn": action_connector_arn,
            "action_connector_id": action_connector_id,
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def action_connector_arn(self) -> builtins.str:
        '''The ARN of the ActionConnector resource.'''
        result = self._values.get("action_connector_arn")
        assert result is not None, "Required property 'action_connector_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def action_connector_id(self) -> builtins.str:
        '''The ActionConnectorId of the ActionConnector resource.'''
        result = self._values.get("action_connector_id")
        assert result is not None, "Required property 'action_connector_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the ActionConnector resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActionConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.AnalysisReference",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_arn": "analysisArn",
        "analysis_id": "analysisId",
        "aws_account_id": "awsAccountId",
    },
)
class AnalysisReference:
    def __init__(
        self,
        *,
        analysis_arn: builtins.str,
        analysis_id: builtins.str,
        aws_account_id: builtins.str,
    ) -> None:
        '''A reference to a Analysis resource.

        :param analysis_arn: The ARN of the Analysis resource.
        :param analysis_id: The AnalysisId of the Analysis resource.
        :param aws_account_id: The AwsAccountId of the Analysis resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            analysis_reference = interfaces_quicksight.AnalysisReference(
                analysis_arn="analysisArn",
                analysis_id="analysisId",
                aws_account_id="awsAccountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79dd570d6da6d3fe7b5ab82dcad552abbb17b11f076a26256bed0f162c545988)
            check_type(argname="argument analysis_arn", value=analysis_arn, expected_type=type_hints["analysis_arn"])
            check_type(argname="argument analysis_id", value=analysis_id, expected_type=type_hints["analysis_id"])
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "analysis_arn": analysis_arn,
            "analysis_id": analysis_id,
            "aws_account_id": aws_account_id,
        }

    @builtins.property
    def analysis_arn(self) -> builtins.str:
        '''The ARN of the Analysis resource.'''
        result = self._values.get("analysis_arn")
        assert result is not None, "Required property 'analysis_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def analysis_id(self) -> builtins.str:
        '''The AnalysisId of the Analysis resource.'''
        result = self._values.get("analysis_id")
        assert result is not None, "Required property 'analysis_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Analysis resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalysisReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.CustomPermissionsReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "custom_permissions_arn": "customPermissionsArn",
        "custom_permissions_name": "customPermissionsName",
    },
)
class CustomPermissionsReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        custom_permissions_arn: builtins.str,
        custom_permissions_name: builtins.str,
    ) -> None:
        '''A reference to a CustomPermissions resource.

        :param aws_account_id: The AwsAccountId of the CustomPermissions resource.
        :param custom_permissions_arn: The ARN of the CustomPermissions resource.
        :param custom_permissions_name: The CustomPermissionsName of the CustomPermissions resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            custom_permissions_reference = interfaces_quicksight.CustomPermissionsReference(
                aws_account_id="awsAccountId",
                custom_permissions_arn="customPermissionsArn",
                custom_permissions_name="customPermissionsName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcbb01a6ae4003c466f2c9facde86b4a9228b2947e8db14b07e90c8828b892fc)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument custom_permissions_arn", value=custom_permissions_arn, expected_type=type_hints["custom_permissions_arn"])
            check_type(argname="argument custom_permissions_name", value=custom_permissions_name, expected_type=type_hints["custom_permissions_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "custom_permissions_arn": custom_permissions_arn,
            "custom_permissions_name": custom_permissions_name,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the CustomPermissions resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_permissions_arn(self) -> builtins.str:
        '''The ARN of the CustomPermissions resource.'''
        result = self._values.get("custom_permissions_arn")
        assert result is not None, "Required property 'custom_permissions_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_permissions_name(self) -> builtins.str:
        '''The CustomPermissionsName of the CustomPermissions resource.'''
        result = self._values.get("custom_permissions_name")
        assert result is not None, "Required property 'custom_permissions_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomPermissionsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.DashboardReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "dashboard_arn": "dashboardArn",
        "dashboard_id": "dashboardId",
    },
)
class DashboardReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        dashboard_arn: builtins.str,
        dashboard_id: builtins.str,
    ) -> None:
        '''A reference to a Dashboard resource.

        :param aws_account_id: The AwsAccountId of the Dashboard resource.
        :param dashboard_arn: The ARN of the Dashboard resource.
        :param dashboard_id: The DashboardId of the Dashboard resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            dashboard_reference = interfaces_quicksight.DashboardReference(
                aws_account_id="awsAccountId",
                dashboard_arn="dashboardArn",
                dashboard_id="dashboardId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e1998cd35473accee4a1dd066f5d4e4af29b9cdfdf78293c732f43e8ae1071f)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument dashboard_arn", value=dashboard_arn, expected_type=type_hints["dashboard_arn"])
            check_type(argname="argument dashboard_id", value=dashboard_id, expected_type=type_hints["dashboard_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "dashboard_arn": dashboard_arn,
            "dashboard_id": dashboard_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Dashboard resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_arn(self) -> builtins.str:
        '''The ARN of the Dashboard resource.'''
        result = self._values.get("dashboard_arn")
        assert result is not None, "Required property 'dashboard_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dashboard_id(self) -> builtins.str:
        '''The DashboardId of the Dashboard resource.'''
        result = self._values.get("dashboard_id")
        assert result is not None, "Required property 'dashboard_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.DataSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_arn": "dataSetArn",
        "data_set_id": "dataSetId",
    },
)
class DataSetReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_arn: builtins.str,
        data_set_id: builtins.str,
    ) -> None:
        '''A reference to a DataSet resource.

        :param aws_account_id: The AwsAccountId of the DataSet resource.
        :param data_set_arn: The ARN of the DataSet resource.
        :param data_set_id: The DataSetId of the DataSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            data_set_reference = interfaces_quicksight.DataSetReference(
                aws_account_id="awsAccountId",
                data_set_arn="dataSetArn",
                data_set_id="dataSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39696e8afe9ffe21ed7b01deb7349ba2563b8d2cdae5e74d20ee2a0e637d3f7f)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument data_set_arn", value=data_set_arn, expected_type=type_hints["data_set_arn"])
            check_type(argname="argument data_set_id", value=data_set_id, expected_type=type_hints["data_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_arn": data_set_arn,
            "data_set_id": data_set_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the DataSet resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_arn(self) -> builtins.str:
        '''The ARN of the DataSet resource.'''
        result = self._values.get("data_set_arn")
        assert result is not None, "Required property 'data_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The DataSetId of the DataSet resource.'''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.DataSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_source_arn": "dataSourceArn",
        "data_source_id": "dataSourceId",
    },
)
class DataSourceReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_source_arn: builtins.str,
        data_source_id: builtins.str,
    ) -> None:
        '''A reference to a DataSource resource.

        :param aws_account_id: The AwsAccountId of the DataSource resource.
        :param data_source_arn: The ARN of the DataSource resource.
        :param data_source_id: The DataSourceId of the DataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            data_source_reference = interfaces_quicksight.DataSourceReference(
                aws_account_id="awsAccountId",
                data_source_arn="dataSourceArn",
                data_source_id="dataSourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70b8fb657688960b4dae12c4a8f205b2a58737c1dd982d8e201b45cf5cb10c90)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument data_source_arn", value=data_source_arn, expected_type=type_hints["data_source_arn"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_source_arn": data_source_arn,
            "data_source_id": data_source_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the DataSource resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The ARN of the DataSource resource.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The DataSourceId of the DataSource resource.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.FolderReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "folder_arn": "folderArn",
        "folder_id": "folderId",
    },
)
class FolderReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        folder_arn: builtins.str,
        folder_id: builtins.str,
    ) -> None:
        '''A reference to a Folder resource.

        :param aws_account_id: The AwsAccountId of the Folder resource.
        :param folder_arn: The ARN of the Folder resource.
        :param folder_id: The FolderId of the Folder resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            folder_reference = interfaces_quicksight.FolderReference(
                aws_account_id="awsAccountId",
                folder_arn="folderArn",
                folder_id="folderId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d11833d18be618b7ec87af3be2a77728a162bc466dd4aaa5584c1b4c7d4012)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument folder_arn", value=folder_arn, expected_type=type_hints["folder_arn"])
            check_type(argname="argument folder_id", value=folder_id, expected_type=type_hints["folder_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "folder_arn": folder_arn,
            "folder_id": folder_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Folder resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def folder_arn(self) -> builtins.str:
        '''The ARN of the Folder resource.'''
        result = self._values.get("folder_arn")
        assert result is not None, "Required property 'folder_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def folder_id(self) -> builtins.str:
        '''The FolderId of the Folder resource.'''
        result = self._values.get("folder_id")
        assert result is not None, "Required property 'folder_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FolderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IActionConnectorRef")
class IActionConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ActionConnector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="actionConnectorRef")
    def action_connector_ref(self) -> "ActionConnectorReference":
        '''(experimental) A reference to a ActionConnector resource.

        :stability: experimental
        '''
        ...


class _IActionConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ActionConnector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IActionConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="actionConnectorRef")
    def action_connector_ref(self) -> "ActionConnectorReference":
        '''(experimental) A reference to a ActionConnector resource.

        :stability: experimental
        '''
        return typing.cast("ActionConnectorReference", jsii.get(self, "actionConnectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IActionConnectorRef).__jsii_proxy_class__ = lambda : _IActionConnectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IAnalysisRef")
class IAnalysisRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Analysis.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="analysisRef")
    def analysis_ref(self) -> "AnalysisReference":
        '''(experimental) A reference to a Analysis resource.

        :stability: experimental
        '''
        ...


class _IAnalysisRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Analysis.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IAnalysisRef"

    @builtins.property
    @jsii.member(jsii_name="analysisRef")
    def analysis_ref(self) -> "AnalysisReference":
        '''(experimental) A reference to a Analysis resource.

        :stability: experimental
        '''
        return typing.cast("AnalysisReference", jsii.get(self, "analysisRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnalysisRef).__jsii_proxy_class__ = lambda : _IAnalysisRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ICustomPermissionsRef"
)
class ICustomPermissionsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomPermissions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customPermissionsRef")
    def custom_permissions_ref(self) -> "CustomPermissionsReference":
        '''(experimental) A reference to a CustomPermissions resource.

        :stability: experimental
        '''
        ...


class _ICustomPermissionsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomPermissions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ICustomPermissionsRef"

    @builtins.property
    @jsii.member(jsii_name="customPermissionsRef")
    def custom_permissions_ref(self) -> "CustomPermissionsReference":
        '''(experimental) A reference to a CustomPermissions resource.

        :stability: experimental
        '''
        return typing.cast("CustomPermissionsReference", jsii.get(self, "customPermissionsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomPermissionsRef).__jsii_proxy_class__ = lambda : _ICustomPermissionsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IDashboardRef")
class IDashboardRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Dashboard.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dashboardRef")
    def dashboard_ref(self) -> "DashboardReference":
        '''(experimental) A reference to a Dashboard resource.

        :stability: experimental
        '''
        ...


class _IDashboardRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Dashboard.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IDashboardRef"

    @builtins.property
    @jsii.member(jsii_name="dashboardRef")
    def dashboard_ref(self) -> "DashboardReference":
        '''(experimental) A reference to a Dashboard resource.

        :stability: experimental
        '''
        return typing.cast("DashboardReference", jsii.get(self, "dashboardRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDashboardRef).__jsii_proxy_class__ = lambda : _IDashboardRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IDataSetRef")
class IDataSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSetRef")
    def data_set_ref(self) -> "DataSetReference":
        '''(experimental) A reference to a DataSet resource.

        :stability: experimental
        '''
        ...


class _IDataSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IDataSetRef"

    @builtins.property
    @jsii.member(jsii_name="dataSetRef")
    def data_set_ref(self) -> "DataSetReference":
        '''(experimental) A reference to a DataSet resource.

        :stability: experimental
        '''
        return typing.cast("DataSetReference", jsii.get(self, "dataSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSetRef).__jsii_proxy_class__ = lambda : _IDataSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IDataSourceRef")
class IDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        ...


class _IDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        return typing.cast("DataSourceReference", jsii.get(self, "dataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSourceRef).__jsii_proxy_class__ = lambda : _IDataSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IFolderRef")
class IFolderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Folder.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="folderRef")
    def folder_ref(self) -> "FolderReference":
        '''(experimental) A reference to a Folder resource.

        :stability: experimental
        '''
        ...


class _IFolderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Folder.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IFolderRef"

    @builtins.property
    @jsii.member(jsii_name="folderRef")
    def folder_ref(self) -> "FolderReference":
        '''(experimental) A reference to a Folder resource.

        :stability: experimental
        '''
        return typing.cast("FolderReference", jsii.get(self, "folderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFolderRef).__jsii_proxy_class__ = lambda : _IFolderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IRefreshScheduleRef")
class IRefreshScheduleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RefreshSchedule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="refreshScheduleRef")
    def refresh_schedule_ref(self) -> "RefreshScheduleReference":
        '''(experimental) A reference to a RefreshSchedule resource.

        :stability: experimental
        '''
        ...


class _IRefreshScheduleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RefreshSchedule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IRefreshScheduleRef"

    @builtins.property
    @jsii.member(jsii_name="refreshScheduleRef")
    def refresh_schedule_ref(self) -> "RefreshScheduleReference":
        '''(experimental) A reference to a RefreshSchedule resource.

        :stability: experimental
        '''
        return typing.cast("RefreshScheduleReference", jsii.get(self, "refreshScheduleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRefreshScheduleRef).__jsii_proxy_class__ = lambda : _IRefreshScheduleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ITemplateRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ITemplateRef"

    @builtins.property
    @jsii.member(jsii_name="templateRef")
    def template_ref(self) -> "TemplateReference":
        '''(experimental) A reference to a Template resource.

        :stability: experimental
        '''
        return typing.cast("TemplateReference", jsii.get(self, "templateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITemplateRef).__jsii_proxy_class__ = lambda : _ITemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IThemeRef")
class IThemeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Theme.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="themeRef")
    def theme_ref(self) -> "ThemeReference":
        '''(experimental) A reference to a Theme resource.

        :stability: experimental
        '''
        ...


class _IThemeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Theme.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IThemeRef"

    @builtins.property
    @jsii.member(jsii_name="themeRef")
    def theme_ref(self) -> "ThemeReference":
        '''(experimental) A reference to a Theme resource.

        :stability: experimental
        '''
        return typing.cast("ThemeReference", jsii.get(self, "themeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThemeRef).__jsii_proxy_class__ = lambda : _IThemeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ITopicRef")
class ITopicRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Topic.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicRef")
    def topic_ref(self) -> "TopicReference":
        '''(experimental) A reference to a Topic resource.

        :stability: experimental
        '''
        ...


class _ITopicRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Topic.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.ITopicRef"

    @builtins.property
    @jsii.member(jsii_name="topicRef")
    def topic_ref(self) -> "TopicReference":
        '''(experimental) A reference to a Topic resource.

        :stability: experimental
        '''
        return typing.cast("TopicReference", jsii.get(self, "topicRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicRef).__jsii_proxy_class__ = lambda : _ITopicRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_quicksight.IVPCConnectionRef")
class IVPCConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCConnection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionRef")
    def vpc_connection_ref(self) -> "VPCConnectionReference":
        '''(experimental) A reference to a VPCConnection resource.

        :stability: experimental
        '''
        ...


class _IVPCConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCConnection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_quicksight.IVPCConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionRef")
    def vpc_connection_ref(self) -> "VPCConnectionReference":
        '''(experimental) A reference to a VPCConnection resource.

        :stability: experimental
        '''
        return typing.cast("VPCConnectionReference", jsii.get(self, "vpcConnectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCConnectionRef).__jsii_proxy_class__ = lambda : _IVPCConnectionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.RefreshScheduleReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "data_set_id": "dataSetId",
        "refresh_schedule_arn": "refreshScheduleArn",
        "schedule_id": "scheduleId",
    },
)
class RefreshScheduleReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        data_set_id: builtins.str,
        refresh_schedule_arn: builtins.str,
        schedule_id: builtins.str,
    ) -> None:
        '''A reference to a RefreshSchedule resource.

        :param aws_account_id: The AwsAccountId of the RefreshSchedule resource.
        :param data_set_id: The DataSetId of the RefreshSchedule resource.
        :param refresh_schedule_arn: The ARN of the RefreshSchedule resource.
        :param schedule_id: The Schedule/ScheduleId of the RefreshSchedule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            refresh_schedule_reference = interfaces_quicksight.RefreshScheduleReference(
                aws_account_id="awsAccountId",
                data_set_id="dataSetId",
                refresh_schedule_arn="refreshScheduleArn",
                schedule_id="scheduleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8723d097fe811477bf46d6e8328f08cbc18d550832e45dfd85d0a290a2e9c9ea)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument data_set_id", value=data_set_id, expected_type=type_hints["data_set_id"])
            check_type(argname="argument refresh_schedule_arn", value=refresh_schedule_arn, expected_type=type_hints["refresh_schedule_arn"])
            check_type(argname="argument schedule_id", value=schedule_id, expected_type=type_hints["schedule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "data_set_id": data_set_id,
            "refresh_schedule_arn": refresh_schedule_arn,
            "schedule_id": schedule_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the RefreshSchedule resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_set_id(self) -> builtins.str:
        '''The DataSetId of the RefreshSchedule resource.'''
        result = self._values.get("data_set_id")
        assert result is not None, "Required property 'data_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def refresh_schedule_arn(self) -> builtins.str:
        '''The ARN of the RefreshSchedule resource.'''
        result = self._values.get("refresh_schedule_arn")
        assert result is not None, "Required property 'refresh_schedule_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule_id(self) -> builtins.str:
        '''The Schedule/ScheduleId of the RefreshSchedule resource.'''
        result = self._values.get("schedule_id")
        assert result is not None, "Required property 'schedule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RefreshScheduleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.TemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "template_arn": "templateArn",
        "template_id": "templateId",
    },
)
class TemplateReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        template_arn: builtins.str,
        template_id: builtins.str,
    ) -> None:
        '''A reference to a Template resource.

        :param aws_account_id: The AwsAccountId of the Template resource.
        :param template_arn: The ARN of the Template resource.
        :param template_id: The TemplateId of the Template resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            template_reference = interfaces_quicksight.TemplateReference(
                aws_account_id="awsAccountId",
                template_arn="templateArn",
                template_id="templateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5bef292799a30d68c18b479c9372960c83ce75f740acf6872746b1c68a4f4be)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument template_arn", value=template_arn, expected_type=type_hints["template_arn"])
            check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "template_arn": template_arn,
            "template_id": template_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Template resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_arn(self) -> builtins.str:
        '''The ARN of the Template resource.'''
        result = self._values.get("template_arn")
        assert result is not None, "Required property 'template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The TemplateId of the Template resource.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.ThemeReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "theme_arn": "themeArn",
        "theme_id": "themeId",
    },
)
class ThemeReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        theme_arn: builtins.str,
        theme_id: builtins.str,
    ) -> None:
        '''A reference to a Theme resource.

        :param aws_account_id: The AwsAccountId of the Theme resource.
        :param theme_arn: The ARN of the Theme resource.
        :param theme_id: The ThemeId of the Theme resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            theme_reference = interfaces_quicksight.ThemeReference(
                aws_account_id="awsAccountId",
                theme_arn="themeArn",
                theme_id="themeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145097322a7b346d435b378f4f5398ed66d47436afe9e55c22372eab8a112c87)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument theme_arn", value=theme_arn, expected_type=type_hints["theme_arn"])
            check_type(argname="argument theme_id", value=theme_id, expected_type=type_hints["theme_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "theme_arn": theme_arn,
            "theme_id": theme_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Theme resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_arn(self) -> builtins.str:
        '''The ARN of the Theme resource.'''
        result = self._values.get("theme_arn")
        assert result is not None, "Required property 'theme_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The ThemeId of the Theme resource.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.TopicReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "topic_arn": "topicArn",
        "topic_id": "topicId",
    },
)
class TopicReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        topic_arn: builtins.str,
        topic_id: builtins.str,
    ) -> None:
        '''A reference to a Topic resource.

        :param aws_account_id: The AwsAccountId of the Topic resource.
        :param topic_arn: The ARN of the Topic resource.
        :param topic_id: The TopicId of the Topic resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            topic_reference = interfaces_quicksight.TopicReference(
                aws_account_id="awsAccountId",
                topic_arn="topicArn",
                topic_id="topicId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__644dc61611189aa4ef3678efd6b78c7718549c2efda0dd7842ca761132bca1a7)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            check_type(argname="argument topic_id", value=topic_id, expected_type=type_hints["topic_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "topic_arn": topic_arn,
            "topic_id": topic_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the Topic resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''The ARN of the Topic resource.'''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_id(self) -> builtins.str:
        '''The TopicId of the Topic resource.'''
        result = self._values.get("topic_id")
        assert result is not None, "Required property 'topic_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_quicksight.VPCConnectionReference",
    jsii_struct_bases=[],
    name_mapping={
        "aws_account_id": "awsAccountId",
        "vpc_connection_arn": "vpcConnectionArn",
        "vpc_connection_id": "vpcConnectionId",
    },
)
class VPCConnectionReference:
    def __init__(
        self,
        *,
        aws_account_id: builtins.str,
        vpc_connection_arn: builtins.str,
        vpc_connection_id: builtins.str,
    ) -> None:
        '''A reference to a VPCConnection resource.

        :param aws_account_id: The AwsAccountId of the VPCConnection resource.
        :param vpc_connection_arn: The ARN of the VPCConnection resource.
        :param vpc_connection_id: The VPCConnectionId of the VPCConnection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_quicksight as interfaces_quicksight
            
            v_pCConnection_reference = interfaces_quicksight.VPCConnectionReference(
                aws_account_id="awsAccountId",
                vpc_connection_arn="vpcConnectionArn",
                vpc_connection_id="vpcConnectionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a94c806f9f5d8f329e5fe8025b2cd7112ef5f8d032fce0a9cf2e9f64bafb27b)
            check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
            check_type(argname="argument vpc_connection_arn", value=vpc_connection_arn, expected_type=type_hints["vpc_connection_arn"])
            check_type(argname="argument vpc_connection_id", value=vpc_connection_id, expected_type=type_hints["vpc_connection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aws_account_id": aws_account_id,
            "vpc_connection_arn": vpc_connection_arn,
            "vpc_connection_id": vpc_connection_id,
        }

    @builtins.property
    def aws_account_id(self) -> builtins.str:
        '''The AwsAccountId of the VPCConnection resource.'''
        result = self._values.get("aws_account_id")
        assert result is not None, "Required property 'aws_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_connection_arn(self) -> builtins.str:
        '''The ARN of the VPCConnection resource.'''
        result = self._values.get("vpc_connection_arn")
        assert result is not None, "Required property 'vpc_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_connection_id(self) -> builtins.str:
        '''The VPCConnectionId of the VPCConnection resource.'''
        result = self._values.get("vpc_connection_id")
        assert result is not None, "Required property 'vpc_connection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ActionConnectorReference",
    "AnalysisReference",
    "CustomPermissionsReference",
    "DashboardReference",
    "DataSetReference",
    "DataSourceReference",
    "FolderReference",
    "IActionConnectorRef",
    "IAnalysisRef",
    "ICustomPermissionsRef",
    "IDashboardRef",
    "IDataSetRef",
    "IDataSourceRef",
    "IFolderRef",
    "IRefreshScheduleRef",
    "ITemplateRef",
    "IThemeRef",
    "ITopicRef",
    "IVPCConnectionRef",
    "RefreshScheduleReference",
    "TemplateReference",
    "ThemeReference",
    "TopicReference",
    "VPCConnectionReference",
]

publication.publish()

def _typecheckingstub__31055bc274e952c4fc3166d11f0fbbc107ed08b00575ccf7d73fa07a9e5f9f9f(
    *,
    action_connector_arn: builtins.str,
    action_connector_id: builtins.str,
    aws_account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79dd570d6da6d3fe7b5ab82dcad552abbb17b11f076a26256bed0f162c545988(
    *,
    analysis_arn: builtins.str,
    analysis_id: builtins.str,
    aws_account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcbb01a6ae4003c466f2c9facde86b4a9228b2947e8db14b07e90c8828b892fc(
    *,
    aws_account_id: builtins.str,
    custom_permissions_arn: builtins.str,
    custom_permissions_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e1998cd35473accee4a1dd066f5d4e4af29b9cdfdf78293c732f43e8ae1071f(
    *,
    aws_account_id: builtins.str,
    dashboard_arn: builtins.str,
    dashboard_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39696e8afe9ffe21ed7b01deb7349ba2563b8d2cdae5e74d20ee2a0e637d3f7f(
    *,
    aws_account_id: builtins.str,
    data_set_arn: builtins.str,
    data_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70b8fb657688960b4dae12c4a8f205b2a58737c1dd982d8e201b45cf5cb10c90(
    *,
    aws_account_id: builtins.str,
    data_source_arn: builtins.str,
    data_source_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d11833d18be618b7ec87af3be2a77728a162bc466dd4aaa5584c1b4c7d4012(
    *,
    aws_account_id: builtins.str,
    folder_arn: builtins.str,
    folder_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8723d097fe811477bf46d6e8328f08cbc18d550832e45dfd85d0a290a2e9c9ea(
    *,
    aws_account_id: builtins.str,
    data_set_id: builtins.str,
    refresh_schedule_arn: builtins.str,
    schedule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5bef292799a30d68c18b479c9372960c83ce75f740acf6872746b1c68a4f4be(
    *,
    aws_account_id: builtins.str,
    template_arn: builtins.str,
    template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145097322a7b346d435b378f4f5398ed66d47436afe9e55c22372eab8a112c87(
    *,
    aws_account_id: builtins.str,
    theme_arn: builtins.str,
    theme_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__644dc61611189aa4ef3678efd6b78c7718549c2efda0dd7842ca761132bca1a7(
    *,
    aws_account_id: builtins.str,
    topic_arn: builtins.str,
    topic_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a94c806f9f5d8f329e5fe8025b2cd7112ef5f8d032fce0a9cf2e9f64bafb27b(
    *,
    aws_account_id: builtins.str,
    vpc_connection_arn: builtins.str,
    vpc_connection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IActionConnectorRef, IAnalysisRef, ICustomPermissionsRef, IDashboardRef, IDataSetRef, IDataSourceRef, IFolderRef, IRefreshScheduleRef, ITemplateRef, IThemeRef, ITopicRef, IVPCConnectionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
