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
    jsii_type="aws-cdk-lib.interfaces.aws_iotanalytics.ChannelReference",
    jsii_struct_bases=[],
    name_mapping={"channel_name": "channelName"},
)
class ChannelReference:
    def __init__(self, *, channel_name: builtins.str) -> None:
        '''A reference to a Channel resource.

        :param channel_name: The ChannelName of the Channel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotanalytics as interfaces_iotanalytics
            
            channel_reference = interfaces_iotanalytics.ChannelReference(
                channel_name="channelName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5cd4b5ea64eb67b3f113dc7dc338dde95fd3e19b91e349588b31c490719ef71)
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_name": channel_name,
        }

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The ChannelName of the Channel resource.'''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotanalytics.DatasetReference",
    jsii_struct_bases=[],
    name_mapping={"dataset_name": "datasetName"},
)
class DatasetReference:
    def __init__(self, *, dataset_name: builtins.str) -> None:
        '''A reference to a Dataset resource.

        :param dataset_name: The DatasetName of the Dataset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotanalytics as interfaces_iotanalytics
            
            dataset_reference = interfaces_iotanalytics.DatasetReference(
                dataset_name="datasetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__016408ec4f7e9e507bdf4b868525967b6c1f5d82cf433acbaee46cbda0088fb4)
            check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_name": dataset_name,
        }

    @builtins.property
    def dataset_name(self) -> builtins.str:
        '''The DatasetName of the Dataset resource.'''
        result = self._values.get("dataset_name")
        assert result is not None, "Required property 'dataset_name' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_iotanalytics.DatastoreReference",
    jsii_struct_bases=[],
    name_mapping={"datastore_name": "datastoreName"},
)
class DatastoreReference:
    def __init__(self, *, datastore_name: builtins.str) -> None:
        '''A reference to a Datastore resource.

        :param datastore_name: The DatastoreName of the Datastore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotanalytics as interfaces_iotanalytics
            
            datastore_reference = interfaces_iotanalytics.DatastoreReference(
                datastore_name="datastoreName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7032bc5b8dbe64970fac281cb91b607194410e31888c1c8329a4d7ed5d349cf)
            check_type(argname="argument datastore_name", value=datastore_name, expected_type=type_hints["datastore_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datastore_name": datastore_name,
        }

    @builtins.property
    def datastore_name(self) -> builtins.str:
        '''The DatastoreName of the Datastore resource.'''
        result = self._values.get("datastore_name")
        assert result is not None, "Required property 'datastore_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotanalytics.IChannelRef")
class IChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Channel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        ...


class _IChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Channel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotanalytics.IChannelRef"

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        return typing.cast("ChannelReference", jsii.get(self, "channelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelRef).__jsii_proxy_class__ = lambda : _IChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotanalytics.IDatasetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotanalytics.IDatasetRef"

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        return typing.cast("DatasetReference", jsii.get(self, "datasetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetRef).__jsii_proxy_class__ = lambda : _IDatasetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotanalytics.IDatastoreRef")
class IDatastoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Datastore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="datastoreRef")
    def datastore_ref(self) -> "DatastoreReference":
        '''(experimental) A reference to a Datastore resource.

        :stability: experimental
        '''
        ...


class _IDatastoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Datastore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotanalytics.IDatastoreRef"

    @builtins.property
    @jsii.member(jsii_name="datastoreRef")
    def datastore_ref(self) -> "DatastoreReference":
        '''(experimental) A reference to a Datastore resource.

        :stability: experimental
        '''
        return typing.cast("DatastoreReference", jsii.get(self, "datastoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatastoreRef).__jsii_proxy_class__ = lambda : _IDatastoreRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotanalytics.IPipelineRef")
class IPipelineRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Pipeline.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pipelineRef")
    def pipeline_ref(self) -> "PipelineReference":
        '''(experimental) A reference to a Pipeline resource.

        :stability: experimental
        '''
        ...


class _IPipelineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Pipeline.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotanalytics.IPipelineRef"

    @builtins.property
    @jsii.member(jsii_name="pipelineRef")
    def pipeline_ref(self) -> "PipelineReference":
        '''(experimental) A reference to a Pipeline resource.

        :stability: experimental
        '''
        return typing.cast("PipelineReference", jsii.get(self, "pipelineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPipelineRef).__jsii_proxy_class__ = lambda : _IPipelineRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotanalytics.PipelineReference",
    jsii_struct_bases=[],
    name_mapping={"pipeline_name": "pipelineName"},
)
class PipelineReference:
    def __init__(self, *, pipeline_name: builtins.str) -> None:
        '''A reference to a Pipeline resource.

        :param pipeline_name: The PipelineName of the Pipeline resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotanalytics as interfaces_iotanalytics
            
            pipeline_reference = interfaces_iotanalytics.PipelineReference(
                pipeline_name="pipelineName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8247a3d7d88d85e4cfa9d5394f245c4854ce7787a2232fa0c42cba1c3df27d49)
            check_type(argname="argument pipeline_name", value=pipeline_name, expected_type=type_hints["pipeline_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pipeline_name": pipeline_name,
        }

    @builtins.property
    def pipeline_name(self) -> builtins.str:
        '''The PipelineName of the Pipeline resource.'''
        result = self._values.get("pipeline_name")
        assert result is not None, "Required property 'pipeline_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ChannelReference",
    "DatasetReference",
    "DatastoreReference",
    "IChannelRef",
    "IDatasetRef",
    "IDatastoreRef",
    "IPipelineRef",
    "PipelineReference",
]

publication.publish()

def _typecheckingstub__f5cd4b5ea64eb67b3f113dc7dc338dde95fd3e19b91e349588b31c490719ef71(
    *,
    channel_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__016408ec4f7e9e507bdf4b868525967b6c1f5d82cf433acbaee46cbda0088fb4(
    *,
    dataset_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7032bc5b8dbe64970fac281cb91b607194410e31888c1c8329a4d7ed5d349cf(
    *,
    datastore_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8247a3d7d88d85e4cfa9d5394f245c4854ce7787a2232fa0c42cba1c3df27d49(
    *,
    pipeline_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IChannelRef, IDatasetRef, IDatastoreRef, IPipelineRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
