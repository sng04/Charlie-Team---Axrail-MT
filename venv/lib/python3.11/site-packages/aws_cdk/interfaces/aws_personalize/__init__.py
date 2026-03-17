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
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.DatasetGroupReference",
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
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            dataset_group_reference = interfaces_personalize.DatasetGroupReference(
                dataset_group_arn="datasetGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bd607e866ffb5f894ee4515b429500888071106bbb3684630b35c3f634570cb)
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
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.DatasetReference",
    jsii_struct_bases=[],
    name_mapping={"dataset_arn": "datasetArn"},
)
class DatasetReference:
    def __init__(self, *, dataset_arn: builtins.str) -> None:
        '''A reference to a Dataset resource.

        :param dataset_arn: The DatasetArn of the Dataset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            dataset_reference = interfaces_personalize.DatasetReference(
                dataset_arn="datasetArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8259ee192b97f65bb1bfb7dd2c09770b403cad7400c4318eae4c7d5c897451f3)
            check_type(argname="argument dataset_arn", value=dataset_arn, expected_type=type_hints["dataset_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_arn": dataset_arn,
        }

    @builtins.property
    def dataset_arn(self) -> builtins.str:
        '''The DatasetArn of the Dataset resource.'''
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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.IDatasetGroupRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.IDatasetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="datasetGroupRef")
    def dataset_group_ref(self) -> "DatasetGroupReference":
        '''(experimental) A reference to a DatasetGroup resource.

        :stability: experimental
        '''
        return typing.cast("DatasetGroupReference", jsii.get(self, "datasetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetGroupRef).__jsii_proxy_class__ = lambda : _IDatasetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.IDatasetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.IDatasetRef"

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        return typing.cast("DatasetReference", jsii.get(self, "datasetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetRef).__jsii_proxy_class__ = lambda : _IDatasetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.ISchemaRef")
class ISchemaRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        ...


class _ISchemaRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.ISchemaRef"

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        return typing.cast("SchemaReference", jsii.get(self, "schemaRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaRef).__jsii_proxy_class__ = lambda : _ISchemaRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_personalize.ISolutionRef")
class ISolutionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Solution.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="solutionRef")
    def solution_ref(self) -> "SolutionReference":
        '''(experimental) A reference to a Solution resource.

        :stability: experimental
        '''
        ...


class _ISolutionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Solution.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_personalize.ISolutionRef"

    @builtins.property
    @jsii.member(jsii_name="solutionRef")
    def solution_ref(self) -> "SolutionReference":
        '''(experimental) A reference to a Solution resource.

        :stability: experimental
        '''
        return typing.cast("SolutionReference", jsii.get(self, "solutionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISolutionRef).__jsii_proxy_class__ = lambda : _ISolutionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.SchemaReference",
    jsii_struct_bases=[],
    name_mapping={"schema_arn": "schemaArn"},
)
class SchemaReference:
    def __init__(self, *, schema_arn: builtins.str) -> None:
        '''A reference to a Schema resource.

        :param schema_arn: The SchemaArn of the Schema resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            schema_reference = interfaces_personalize.SchemaReference(
                schema_arn="schemaArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6cd5ef72a7892e6fc2e89c44ce2a2108abd8cb5fa5db53e6d641fbf75e6fd0e)
            check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_arn": schema_arn,
        }

    @builtins.property
    def schema_arn(self) -> builtins.str:
        '''The SchemaArn of the Schema resource.'''
        result = self._values.get("schema_arn")
        assert result is not None, "Required property 'schema_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_personalize.SolutionReference",
    jsii_struct_bases=[],
    name_mapping={"solution_arn": "solutionArn"},
)
class SolutionReference:
    def __init__(self, *, solution_arn: builtins.str) -> None:
        '''A reference to a Solution resource.

        :param solution_arn: The SolutionArn of the Solution resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_personalize as interfaces_personalize
            
            solution_reference = interfaces_personalize.SolutionReference(
                solution_arn="solutionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eb7000ac778c9296a1bcf604536bc2f9b85654eafa6d8acf1a30e8d4a677c4d)
            check_type(argname="argument solution_arn", value=solution_arn, expected_type=type_hints["solution_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "solution_arn": solution_arn,
        }

    @builtins.property
    def solution_arn(self) -> builtins.str:
        '''The SolutionArn of the Solution resource.'''
        result = self._values.get("solution_arn")
        assert result is not None, "Required property 'solution_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SolutionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatasetGroupReference",
    "DatasetReference",
    "IDatasetGroupRef",
    "IDatasetRef",
    "ISchemaRef",
    "ISolutionRef",
    "SchemaReference",
    "SolutionReference",
]

publication.publish()

def _typecheckingstub__9bd607e866ffb5f894ee4515b429500888071106bbb3684630b35c3f634570cb(
    *,
    dataset_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8259ee192b97f65bb1bfb7dd2c09770b403cad7400c4318eae4c7d5c897451f3(
    *,
    dataset_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6cd5ef72a7892e6fc2e89c44ce2a2108abd8cb5fa5db53e6d641fbf75e6fd0e(
    *,
    schema_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eb7000ac778c9296a1bcf604536bc2f9b85654eafa6d8acf1a30e8d4a677c4d(
    *,
    solution_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDatasetGroupRef, IDatasetRef, ISchemaRef, ISolutionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
