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
    jsii_type="aws-cdk-lib.interfaces.aws_cleanroomsml.ITrainingDatasetRef"
)
class ITrainingDatasetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrainingDataset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trainingDatasetRef")
    def training_dataset_ref(self) -> "TrainingDatasetReference":
        '''(experimental) A reference to a TrainingDataset resource.

        :stability: experimental
        '''
        ...


class _ITrainingDatasetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrainingDataset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cleanroomsml.ITrainingDatasetRef"

    @builtins.property
    @jsii.member(jsii_name="trainingDatasetRef")
    def training_dataset_ref(self) -> "TrainingDatasetReference":
        '''(experimental) A reference to a TrainingDataset resource.

        :stability: experimental
        '''
        return typing.cast("TrainingDatasetReference", jsii.get(self, "trainingDatasetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrainingDatasetRef).__jsii_proxy_class__ = lambda : _ITrainingDatasetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanroomsml.TrainingDatasetReference",
    jsii_struct_bases=[],
    name_mapping={"training_dataset_arn": "trainingDatasetArn"},
)
class TrainingDatasetReference:
    def __init__(self, *, training_dataset_arn: builtins.str) -> None:
        '''A reference to a TrainingDataset resource.

        :param training_dataset_arn: The TrainingDatasetArn of the TrainingDataset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cleanroomsml as interfaces_cleanroomsml
            
            training_dataset_reference = interfaces_cleanroomsml.TrainingDatasetReference(
                training_dataset_arn="trainingDatasetArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a27e18c1c530f885505e65eaef8080f9233bf44070ce8f18315805c24e608d9)
            check_type(argname="argument training_dataset_arn", value=training_dataset_arn, expected_type=type_hints["training_dataset_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "training_dataset_arn": training_dataset_arn,
        }

    @builtins.property
    def training_dataset_arn(self) -> builtins.str:
        '''The TrainingDatasetArn of the TrainingDataset resource.'''
        result = self._values.get("training_dataset_arn")
        assert result is not None, "Required property 'training_dataset_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrainingDatasetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ITrainingDatasetRef",
    "TrainingDatasetReference",
]

publication.publish()

def _typecheckingstub__0a27e18c1c530f885505e65eaef8080f9233bf44070ce8f18315805c24e608d9(
    *,
    training_dataset_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ITrainingDatasetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
