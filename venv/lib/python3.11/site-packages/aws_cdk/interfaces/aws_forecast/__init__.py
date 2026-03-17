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
    jsii_type="aws-cdk-lib.interfaces.aws_forecast.DatasetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"dataset_group_arn": "datasetGroupArn"},
)
class DatasetGroupReference:
    def __init__(self, *, dataset_group_arn: builtins.str) -> None:
        '''A reference to a DatasetGroup resource.

        :param dataset_group_arn: The DatasetGroupArn of the DatasetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_forecast as interfaces_forecast
            
            dataset_group_reference = interfaces_forecast.DatasetGroupReference(
                dataset_group_arn="datasetGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b984ec5a8d73ef700abe69c94dc2dbff2aed892fcee98cc9286580e9fbbb9cb)
            check_type(argname="argument dataset_group_arn", value=dataset_group_arn, expected_type=type_hints["dataset_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_group_arn": dataset_group_arn,
        }

    @builtins.property
    def dataset_group_arn(self) -> builtins.str:
        '''The DatasetGroupArn of the DatasetGroup resource.'''
        result = self._values.get("dataset_group_arn")
        assert result is not None, "Required property 'dataset_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_forecast.DatasetReference",
    jsii_struct_bases=[],
    name_mapping={"dataset_arn": "datasetArn"},
)
class DatasetReference:
    def __init__(self, *, dataset_arn: builtins.str) -> None:
        '''A reference to a Dataset resource.

        :param dataset_arn: The Arn of the Dataset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_forecast as interfaces_forecast
            
            dataset_reference = interfaces_forecast.DatasetReference(
                dataset_arn="datasetArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ace9269e485ffb450bdbeedef7bc85a48428ffaef69bf0b62611b2ec8f53808f)
            check_type(argname="argument dataset_arn", value=dataset_arn, expected_type=type_hints["dataset_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_arn": dataset_arn,
        }

    @builtins.property
    def dataset_arn(self) -> builtins.str:
        '''The Arn of the Dataset resource.'''
        result = self._values.get("dataset_arn")
        assert result is not None, "Required property 'dataset_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatasetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_forecast.IDatasetGroupRef")
class IDatasetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DatasetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="datasetGroupRef")
    def dataset_group_ref(self) -> "DatasetGroupReference":
        '''(experimental) A reference to a DatasetGroup resource.

        :stability: experimental
        '''
        ...


class _IDatasetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DatasetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_forecast.IDatasetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="datasetGroupRef")
    def dataset_group_ref(self) -> "DatasetGroupReference":
        '''(experimental) A reference to a DatasetGroup resource.

        :stability: experimental
        '''
        return typing.cast("DatasetGroupReference", jsii.get(self, "datasetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetGroupRef).__jsii_proxy_class__ = lambda : _IDatasetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_forecast.IDatasetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_forecast.IDatasetRef"

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        return typing.cast("DatasetReference", jsii.get(self, "datasetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetRef).__jsii_proxy_class__ = lambda : _IDatasetRefProxy


__all__ = [
    "DatasetGroupReference",
    "DatasetReference",
    "IDatasetGroupRef",
    "IDatasetRef",
]

publication.publish()

def _typecheckingstub__0b984ec5a8d73ef700abe69c94dc2dbff2aed892fcee98cc9286580e9fbbb9cb(
    *,
    dataset_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace9269e485ffb450bdbeedef7bc85a48428ffaef69bf0b62611b2ec8f53808f(
    *,
    dataset_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDatasetGroupRef, IDatasetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
