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
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.AccessPolicyReference",
    jsii_struct_bases=[],
    name_mapping={
        "access_policy_arn": "accessPolicyArn",
        "access_policy_id": "accessPolicyId",
    },
)
class AccessPolicyReference:
    def __init__(
        self,
        *,
        access_policy_arn: builtins.str,
        access_policy_id: builtins.str,
    ) -> None:
        '''A reference to a AccessPolicy resource.

        :param access_policy_arn: The ARN of the AccessPolicy resource.
        :param access_policy_id: The AccessPolicyId of the AccessPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsitewise as interfaces_iotsitewise
            
            access_policy_reference = interfaces_iotsitewise.AccessPolicyReference(
                access_policy_arn="accessPolicyArn",
                access_policy_id="accessPolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e9b62b3a35e2e33ea2fe71af556eefe7952c4e8fd6c2259e70f4f7929e793a4)
            check_type(argname="argument access_policy_arn", value=access_policy_arn, expected_type=type_hints["access_policy_arn"])
            check_type(argname="argument access_policy_id", value=access_policy_id, expected_type=type_hints["access_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_policy_arn": access_policy_arn,
            "access_policy_id": access_policy_id,
        }

    @builtins.property
    def access_policy_arn(self) -> builtins.str:
        '''The ARN of the AccessPolicy resource.'''
        result = self._values.get("access_policy_arn")
        assert result is not None, "Required property 'access_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_policy_id(self) -> builtins.str:
        '''The AccessPolicyId of the AccessPolicy resource.'''
        result = self._values.get("access_policy_id")
        assert result is not None, "Required property 'access_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.AssetModelReference",
    jsii_struct_bases=[],
    name_mapping={
        "asset_model_arn": "assetModelArn",
        "asset_model_id": "assetModelId",
    },
)
class AssetModelReference:
    def __init__(
        self,
        *,
        asset_model_arn: builtins.str,
        asset_model_id: builtins.str,
    ) -> None:
        '''A reference to a AssetModel resource.

        :param asset_model_arn: The ARN of the AssetModel resource.
        :param asset_model_id: The AssetModelId of the AssetModel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsitewise as interfaces_iotsitewise
            
            asset_model_reference = interfaces_iotsitewise.AssetModelReference(
                asset_model_arn="assetModelArn",
                asset_model_id="assetModelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bab29450acde6214ed20346491b24158baa66cbaed5de6bb3a65d909c0c7d406)
            check_type(argname="argument asset_model_arn", value=asset_model_arn, expected_type=type_hints["asset_model_arn"])
            check_type(argname="argument asset_model_id", value=asset_model_id, expected_type=type_hints["asset_model_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "asset_model_arn": asset_model_arn,
            "asset_model_id": asset_model_id,
        }

    @builtins.property
    def asset_model_arn(self) -> builtins.str:
        '''The ARN of the AssetModel resource.'''
        result = self._values.get("asset_model_arn")
        assert result is not None, "Required property 'asset_model_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_model_id(self) -> builtins.str:
        '''The AssetModelId of the AssetModel resource.'''
        result = self._values.get("asset_model_id")
        assert result is not None, "Required property 'asset_model_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetModelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.AssetReference",
    jsii_struct_bases=[],
    name_mapping={"asset_arn": "assetArn", "asset_id": "assetId"},
)
class AssetReference:
    def __init__(self, *, asset_arn: builtins.str, asset_id: builtins.str) -> None:
        '''A reference to a Asset resource.

        :param asset_arn: The ARN of the Asset resource.
        :param asset_id: The AssetId of the Asset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsitewise as interfaces_iotsitewise
            
            asset_reference = interfaces_iotsitewise.AssetReference(
                asset_arn="assetArn",
                asset_id="assetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c074d028d8c3d8ddde5786d0c5bf418062568dba78879a698a0f7aa209f5f2a8)
            check_type(argname="argument asset_arn", value=asset_arn, expected_type=type_hints["asset_arn"])
            check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "asset_arn": asset_arn,
            "asset_id": asset_id,
        }

    @builtins.property
    def asset_arn(self) -> builtins.str:
        '''The ARN of the Asset resource.'''
        result = self._values.get("asset_arn")
        assert result is not None, "Required property 'asset_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_id(self) -> builtins.str:
        '''The AssetId of the Asset resource.'''
        result = self._values.get("asset_id")
        assert result is not None, "Required property 'asset_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.ComputationModelReference",
    jsii_struct_bases=[],
    name_mapping={
        "computation_model_arn": "computationModelArn",
        "computation_model_id": "computationModelId",
    },
)
class ComputationModelReference:
    def __init__(
        self,
        *,
        computation_model_arn: builtins.str,
        computation_model_id: builtins.str,
    ) -> None:
        '''A reference to a ComputationModel resource.

        :param computation_model_arn: The ARN of the ComputationModel resource.
        :param computation_model_id: The ComputationModelId of the ComputationModel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsitewise as interfaces_iotsitewise
            
            computation_model_reference = interfaces_iotsitewise.ComputationModelReference(
                computation_model_arn="computationModelArn",
                computation_model_id="computationModelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a0a6223986863d3b15a3782a66961c8e28eded5d3045c5b0b733751bbbaf4e)
            check_type(argname="argument computation_model_arn", value=computation_model_arn, expected_type=type_hints["computation_model_arn"])
            check_type(argname="argument computation_model_id", value=computation_model_id, expected_type=type_hints["computation_model_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "computation_model_arn": computation_model_arn,
            "computation_model_id": computation_model_id,
        }

    @builtins.property
    def computation_model_arn(self) -> builtins.str:
        '''The ARN of the ComputationModel resource.'''
        result = self._values.get("computation_model_arn")
        assert result is not None, "Required property 'computation_model_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def computation_model_id(self) -> builtins.str:
        '''The ComputationModelId of the ComputationModel resource.'''
        result = self._values.get("computation_model_id")
        assert result is not None, "Required property 'computation_model_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputationModelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.DashboardReference",
    jsii_struct_bases=[],
    name_mapping={"dashboard_arn": "dashboardArn", "dashboard_id": "dashboardId"},
)
class DashboardReference:
    def __init__(
        self,
        *,
        dashboard_arn: builtins.str,
        dashboard_id: builtins.str,
    ) -> None:
        '''A reference to a Dashboard resource.

        :param dashboard_arn: The ARN of the Dashboard resource.
        :param dashboard_id: The DashboardId of the Dashboard resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsitewise as interfaces_iotsitewise
            
            dashboard_reference = interfaces_iotsitewise.DashboardReference(
                dashboard_arn="dashboardArn",
                dashboard_id="dashboardId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36e06a0e5feb5746f79588f3bb7ea7d2a372e4c9036763e6a9444485c779d511)
            check_type(argname="argument dashboard_arn", value=dashboard_arn, expected_type=type_hints["dashboard_arn"])
            check_type(argname="argument dashboard_id", value=dashboard_id, expected_type=type_hints["dashboard_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dashboard_arn": dashboard_arn,
            "dashboard_id": dashboard_id,
        }

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
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.DatasetReference",
    jsii_struct_bases=[],
    name_mapping={"dataset_arn": "datasetArn", "dataset_id": "datasetId"},
)
class DatasetReference:
    def __init__(self, *, dataset_arn: builtins.str, dataset_id: builtins.str) -> None:
        '''A reference to a Dataset resource.

        :param dataset_arn: The ARN of the Dataset resource.
        :param dataset_id: The DatasetId of the Dataset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsitewise as interfaces_iotsitewise
            
            dataset_reference = interfaces_iotsitewise.DatasetReference(
                dataset_arn="datasetArn",
                dataset_id="datasetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3601882a0c740557c0a8716c914e6b15c3628888a9696f79714fae1d10449fa3)
            check_type(argname="argument dataset_arn", value=dataset_arn, expected_type=type_hints["dataset_arn"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_arn": dataset_arn,
            "dataset_id": dataset_id,
        }

    @builtins.property
    def dataset_arn(self) -> builtins.str:
        '''The ARN of the Dataset resource.'''
        result = self._values.get("dataset_arn")
        assert result is not None, "Required property 'dataset_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The DatasetId of the Dataset resource.'''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.GatewayReference",
    jsii_struct_bases=[],
    name_mapping={"gateway_id": "gatewayId"},
)
class GatewayReference:
    def __init__(self, *, gateway_id: builtins.str) -> None:
        '''A reference to a Gateway resource.

        :param gateway_id: The GatewayId of the Gateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsitewise as interfaces_iotsitewise
            
            gateway_reference = interfaces_iotsitewise.GatewayReference(
                gateway_id="gatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__219fd8e8909bacd09e6fd45c24703df8b0ab052abec0e92596bc385088cc2ec0)
            check_type(argname="argument gateway_id", value=gateway_id, expected_type=type_hints["gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_id": gateway_id,
        }

    @builtins.property
    def gateway_id(self) -> builtins.str:
        '''The GatewayId of the Gateway resource.'''
        result = self._values.get("gateway_id")
        assert result is not None, "Required property 'gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.IAccessPolicyRef")
class IAccessPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessPolicyRef")
    def access_policy_ref(self) -> "AccessPolicyReference":
        '''(experimental) A reference to a AccessPolicy resource.

        :stability: experimental
        '''
        ...


class _IAccessPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsitewise.IAccessPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="accessPolicyRef")
    def access_policy_ref(self) -> "AccessPolicyReference":
        '''(experimental) A reference to a AccessPolicy resource.

        :stability: experimental
        '''
        return typing.cast("AccessPolicyReference", jsii.get(self, "accessPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPolicyRef).__jsii_proxy_class__ = lambda : _IAccessPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.IAssetModelRef")
class IAssetModelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AssetModel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="assetModelRef")
    def asset_model_ref(self) -> "AssetModelReference":
        '''(experimental) A reference to a AssetModel resource.

        :stability: experimental
        '''
        ...


class _IAssetModelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AssetModel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsitewise.IAssetModelRef"

    @builtins.property
    @jsii.member(jsii_name="assetModelRef")
    def asset_model_ref(self) -> "AssetModelReference":
        '''(experimental) A reference to a AssetModel resource.

        :stability: experimental
        '''
        return typing.cast("AssetModelReference", jsii.get(self, "assetModelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssetModelRef).__jsii_proxy_class__ = lambda : _IAssetModelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.IAssetRef")
class IAssetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Asset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="assetRef")
    def asset_ref(self) -> "AssetReference":
        '''(experimental) A reference to a Asset resource.

        :stability: experimental
        '''
        ...


class _IAssetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Asset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsitewise.IAssetRef"

    @builtins.property
    @jsii.member(jsii_name="assetRef")
    def asset_ref(self) -> "AssetReference":
        '''(experimental) A reference to a Asset resource.

        :stability: experimental
        '''
        return typing.cast("AssetReference", jsii.get(self, "assetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssetRef).__jsii_proxy_class__ = lambda : _IAssetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.IComputationModelRef"
)
class IComputationModelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ComputationModel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="computationModelRef")
    def computation_model_ref(self) -> "ComputationModelReference":
        '''(experimental) A reference to a ComputationModel resource.

        :stability: experimental
        '''
        ...


class _IComputationModelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ComputationModel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsitewise.IComputationModelRef"

    @builtins.property
    @jsii.member(jsii_name="computationModelRef")
    def computation_model_ref(self) -> "ComputationModelReference":
        '''(experimental) A reference to a ComputationModel resource.

        :stability: experimental
        '''
        return typing.cast("ComputationModelReference", jsii.get(self, "computationModelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IComputationModelRef).__jsii_proxy_class__ = lambda : _IComputationModelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.IDashboardRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsitewise.IDashboardRef"

    @builtins.property
    @jsii.member(jsii_name="dashboardRef")
    def dashboard_ref(self) -> "DashboardReference":
        '''(experimental) A reference to a Dashboard resource.

        :stability: experimental
        '''
        return typing.cast("DashboardReference", jsii.get(self, "dashboardRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDashboardRef).__jsii_proxy_class__ = lambda : _IDashboardRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.IDatasetRef")
class IDatasetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Dataset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        ...


class _IDatasetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Dataset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsitewise.IDatasetRef"

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        return typing.cast("DatasetReference", jsii.get(self, "datasetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetRef).__jsii_proxy_class__ = lambda : _IDatasetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.IGatewayRef")
class IGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Gateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gatewayRef")
    def gateway_ref(self) -> "GatewayReference":
        '''(experimental) A reference to a Gateway resource.

        :stability: experimental
        '''
        ...


class _IGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Gateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsitewise.IGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="gatewayRef")
    def gateway_ref(self) -> "GatewayReference":
        '''(experimental) A reference to a Gateway resource.

        :stability: experimental
        '''
        return typing.cast("GatewayReference", jsii.get(self, "gatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGatewayRef).__jsii_proxy_class__ = lambda : _IGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.IPortalRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsitewise.IPortalRef"

    @builtins.property
    @jsii.member(jsii_name="portalRef")
    def portal_ref(self) -> "PortalReference":
        '''(experimental) A reference to a Portal resource.

        :stability: experimental
        '''
        return typing.cast("PortalReference", jsii.get(self, "portalRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPortalRef).__jsii_proxy_class__ = lambda : _IPortalRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.IProjectRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotsitewise.IProjectRef"

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        return typing.cast("ProjectReference", jsii.get(self, "projectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectRef).__jsii_proxy_class__ = lambda : _IProjectRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.PortalReference",
    jsii_struct_bases=[],
    name_mapping={"portal_arn": "portalArn", "portal_id": "portalId"},
)
class PortalReference:
    def __init__(self, *, portal_arn: builtins.str, portal_id: builtins.str) -> None:
        '''A reference to a Portal resource.

        :param portal_arn: The ARN of the Portal resource.
        :param portal_id: The PortalId of the Portal resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsitewise as interfaces_iotsitewise
            
            portal_reference = interfaces_iotsitewise.PortalReference(
                portal_arn="portalArn",
                portal_id="portalId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22d209b3458a45c845d0f086b6efe3ca2e75eed78de6397221a3f08157d8ccf)
            check_type(argname="argument portal_arn", value=portal_arn, expected_type=type_hints["portal_arn"])
            check_type(argname="argument portal_id", value=portal_id, expected_type=type_hints["portal_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "portal_arn": portal_arn,
            "portal_id": portal_id,
        }

    @builtins.property
    def portal_arn(self) -> builtins.str:
        '''The ARN of the Portal resource.'''
        result = self._values.get("portal_arn")
        assert result is not None, "Required property 'portal_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def portal_id(self) -> builtins.str:
        '''The PortalId of the Portal resource.'''
        result = self._values.get("portal_id")
        assert result is not None, "Required property 'portal_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_iotsitewise.ProjectReference",
    jsii_struct_bases=[],
    name_mapping={"project_arn": "projectArn", "project_id": "projectId"},
)
class ProjectReference:
    def __init__(self, *, project_arn: builtins.str, project_id: builtins.str) -> None:
        '''A reference to a Project resource.

        :param project_arn: The ARN of the Project resource.
        :param project_id: The ProjectId of the Project resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotsitewise as interfaces_iotsitewise
            
            project_reference = interfaces_iotsitewise.ProjectReference(
                project_arn="projectArn",
                project_id="projectId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a8ae4c6854c75be3a7c7b370de23f31606b008da1f7c14d066fc1a1c17d480b)
            check_type(argname="argument project_arn", value=project_arn, expected_type=type_hints["project_arn"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_arn": project_arn,
            "project_id": project_id,
        }

    @builtins.property
    def project_arn(self) -> builtins.str:
        '''The ARN of the Project resource.'''
        result = self._values.get("project_arn")
        assert result is not None, "Required property 'project_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ProjectId of the Project resource.'''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessPolicyReference",
    "AssetModelReference",
    "AssetReference",
    "ComputationModelReference",
    "DashboardReference",
    "DatasetReference",
    "GatewayReference",
    "IAccessPolicyRef",
    "IAssetModelRef",
    "IAssetRef",
    "IComputationModelRef",
    "IDashboardRef",
    "IDatasetRef",
    "IGatewayRef",
    "IPortalRef",
    "IProjectRef",
    "PortalReference",
    "ProjectReference",
]

publication.publish()

def _typecheckingstub__4e9b62b3a35e2e33ea2fe71af556eefe7952c4e8fd6c2259e70f4f7929e793a4(
    *,
    access_policy_arn: builtins.str,
    access_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bab29450acde6214ed20346491b24158baa66cbaed5de6bb3a65d909c0c7d406(
    *,
    asset_model_arn: builtins.str,
    asset_model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c074d028d8c3d8ddde5786d0c5bf418062568dba78879a698a0f7aa209f5f2a8(
    *,
    asset_arn: builtins.str,
    asset_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a0a6223986863d3b15a3782a66961c8e28eded5d3045c5b0b733751bbbaf4e(
    *,
    computation_model_arn: builtins.str,
    computation_model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36e06a0e5feb5746f79588f3bb7ea7d2a372e4c9036763e6a9444485c779d511(
    *,
    dashboard_arn: builtins.str,
    dashboard_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3601882a0c740557c0a8716c914e6b15c3628888a9696f79714fae1d10449fa3(
    *,
    dataset_arn: builtins.str,
    dataset_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__219fd8e8909bacd09e6fd45c24703df8b0ab052abec0e92596bc385088cc2ec0(
    *,
    gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22d209b3458a45c845d0f086b6efe3ca2e75eed78de6397221a3f08157d8ccf(
    *,
    portal_arn: builtins.str,
    portal_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a8ae4c6854c75be3a7c7b370de23f31606b008da1f7c14d066fc1a1c17d480b(
    *,
    project_arn: builtins.str,
    project_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessPolicyRef, IAssetModelRef, IAssetRef, IComputationModelRef, IDashboardRef, IDatasetRef, IGatewayRef, IPortalRef, IProjectRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
