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
    jsii_type="aws-cdk-lib.interfaces.aws_rekognition.CollectionReference",
    jsii_struct_bases=[],
    name_mapping={"collection_arn": "collectionArn", "collection_id": "collectionId"},
)
class CollectionReference:
    def __init__(
        self,
        *,
        collection_arn: builtins.str,
        collection_id: builtins.str,
    ) -> None:
        '''A reference to a Collection resource.

        :param collection_arn: The ARN of the Collection resource.
        :param collection_id: The CollectionId of the Collection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rekognition as interfaces_rekognition
            
            collection_reference = interfaces_rekognition.CollectionReference(
                collection_arn="collectionArn",
                collection_id="collectionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbcd5db6de44cf4b5c022bbf4d330997d6c70cad5b7002d4703f1306e5899de7)
            check_type(argname="argument collection_arn", value=collection_arn, expected_type=type_hints["collection_arn"])
            check_type(argname="argument collection_id", value=collection_id, expected_type=type_hints["collection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collection_arn": collection_arn,
            "collection_id": collection_id,
        }

    @builtins.property
    def collection_arn(self) -> builtins.str:
        '''The ARN of the Collection resource.'''
        result = self._values.get("collection_arn")
        assert result is not None, "Required property 'collection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collection_id(self) -> builtins.str:
        '''The CollectionId of the Collection resource.'''
        result = self._values.get("collection_id")
        assert result is not None, "Required property 'collection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CollectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rekognition.ICollectionRef")
class ICollectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Collection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="collectionRef")
    def collection_ref(self) -> "CollectionReference":
        '''(experimental) A reference to a Collection resource.

        :stability: experimental
        '''
        ...


class _ICollectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Collection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rekognition.ICollectionRef"

    @builtins.property
    @jsii.member(jsii_name="collectionRef")
    def collection_ref(self) -> "CollectionReference":
        '''(experimental) A reference to a Collection resource.

        :stability: experimental
        '''
        return typing.cast("CollectionReference", jsii.get(self, "collectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICollectionRef).__jsii_proxy_class__ = lambda : _ICollectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rekognition.IProjectRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rekognition.IProjectRef"

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        return typing.cast("ProjectReference", jsii.get(self, "projectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectRef).__jsii_proxy_class__ = lambda : _IProjectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rekognition.IStreamProcessorRef")
class IStreamProcessorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StreamProcessor.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="streamProcessorRef")
    def stream_processor_ref(self) -> "StreamProcessorReference":
        '''(experimental) A reference to a StreamProcessor resource.

        :stability: experimental
        '''
        ...


class _IStreamProcessorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StreamProcessor.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rekognition.IStreamProcessorRef"

    @builtins.property
    @jsii.member(jsii_name="streamProcessorRef")
    def stream_processor_ref(self) -> "StreamProcessorReference":
        '''(experimental) A reference to a StreamProcessor resource.

        :stability: experimental
        '''
        return typing.cast("StreamProcessorReference", jsii.get(self, "streamProcessorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStreamProcessorRef).__jsii_proxy_class__ = lambda : _IStreamProcessorRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rekognition.ProjectReference",
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
        :param project_name: The ProjectName of the Project resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rekognition as interfaces_rekognition
            
            project_reference = interfaces_rekognition.ProjectReference(
                project_arn="projectArn",
                project_name="projectName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76c0a27c564c4db555e13da7e4f3f64e8e1d4a811c22e0bd322cb7258d2fafd)
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
        '''The ProjectName of the Project resource.'''
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
    jsii_type="aws-cdk-lib.interfaces.aws_rekognition.StreamProcessorReference",
    jsii_struct_bases=[],
    name_mapping={
        "stream_processor_arn": "streamProcessorArn",
        "stream_processor_name": "streamProcessorName",
    },
)
class StreamProcessorReference:
    def __init__(
        self,
        *,
        stream_processor_arn: builtins.str,
        stream_processor_name: builtins.str,
    ) -> None:
        '''A reference to a StreamProcessor resource.

        :param stream_processor_arn: The ARN of the StreamProcessor resource.
        :param stream_processor_name: The Name of the StreamProcessor resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rekognition as interfaces_rekognition
            
            stream_processor_reference = interfaces_rekognition.StreamProcessorReference(
                stream_processor_arn="streamProcessorArn",
                stream_processor_name="streamProcessorName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa1498d942cfe0cf62d8a710e17ad876f3968c50ba6a7b86399706e4a3115f11)
            check_type(argname="argument stream_processor_arn", value=stream_processor_arn, expected_type=type_hints["stream_processor_arn"])
            check_type(argname="argument stream_processor_name", value=stream_processor_name, expected_type=type_hints["stream_processor_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stream_processor_arn": stream_processor_arn,
            "stream_processor_name": stream_processor_name,
        }

    @builtins.property
    def stream_processor_arn(self) -> builtins.str:
        '''The ARN of the StreamProcessor resource.'''
        result = self._values.get("stream_processor_arn")
        assert result is not None, "Required property 'stream_processor_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_processor_name(self) -> builtins.str:
        '''The Name of the StreamProcessor resource.'''
        result = self._values.get("stream_processor_name")
        assert result is not None, "Required property 'stream_processor_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamProcessorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CollectionReference",
    "ICollectionRef",
    "IProjectRef",
    "IStreamProcessorRef",
    "ProjectReference",
    "StreamProcessorReference",
]

publication.publish()

def _typecheckingstub__dbcd5db6de44cf4b5c022bbf4d330997d6c70cad5b7002d4703f1306e5899de7(
    *,
    collection_arn: builtins.str,
    collection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76c0a27c564c4db555e13da7e4f3f64e8e1d4a811c22e0bd322cb7258d2fafd(
    *,
    project_arn: builtins.str,
    project_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa1498d942cfe0cf62d8a710e17ad876f3968c50ba6a7b86399706e4a3115f11(
    *,
    stream_processor_arn: builtins.str,
    stream_processor_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICollectionRef, IProjectRef, IStreamProcessorRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
