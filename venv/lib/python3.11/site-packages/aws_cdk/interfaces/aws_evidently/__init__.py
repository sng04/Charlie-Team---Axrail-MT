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
    jsii_type="aws-cdk-lib.interfaces.aws_evidently.ExperimentReference",
    jsii_struct_bases=[],
    name_mapping={"experiment_arn": "experimentArn"},
)
class ExperimentReference:
    def __init__(self, *, experiment_arn: builtins.str) -> None:
        '''A reference to a Experiment resource.

        :param experiment_arn: The Arn of the Experiment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_evidently as interfaces_evidently
            
            experiment_reference = interfaces_evidently.ExperimentReference(
                experiment_arn="experimentArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__273c4bc4d0d70940cbdab6b36e5b93c7f24f9c57e204c269796b7aa7921ede94)
            check_type(argname="argument experiment_arn", value=experiment_arn, expected_type=type_hints["experiment_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "experiment_arn": experiment_arn,
        }

    @builtins.property
    def experiment_arn(self) -> builtins.str:
        '''The Arn of the Experiment resource.'''
        result = self._values.get("experiment_arn")
        assert result is not None, "Required property 'experiment_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExperimentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_evidently.FeatureReference",
    jsii_struct_bases=[],
    name_mapping={"feature_arn": "featureArn"},
)
class FeatureReference:
    def __init__(self, *, feature_arn: builtins.str) -> None:
        '''A reference to a Feature resource.

        :param feature_arn: The Arn of the Feature resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_evidently as interfaces_evidently
            
            feature_reference = interfaces_evidently.FeatureReference(
                feature_arn="featureArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__831b96d67d54f4b1e981cb5f35e608263e20010bc39182b493c862218f099dec)
            check_type(argname="argument feature_arn", value=feature_arn, expected_type=type_hints["feature_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "feature_arn": feature_arn,
        }

    @builtins.property
    def feature_arn(self) -> builtins.str:
        '''The Arn of the Feature resource.'''
        result = self._values.get("feature_arn")
        assert result is not None, "Required property 'feature_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FeatureReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_evidently.IExperimentRef")
class IExperimentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Experiment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="experimentRef")
    def experiment_ref(self) -> "ExperimentReference":
        '''(experimental) A reference to a Experiment resource.

        :stability: experimental
        '''
        ...


class _IExperimentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Experiment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_evidently.IExperimentRef"

    @builtins.property
    @jsii.member(jsii_name="experimentRef")
    def experiment_ref(self) -> "ExperimentReference":
        '''(experimental) A reference to a Experiment resource.

        :stability: experimental
        '''
        return typing.cast("ExperimentReference", jsii.get(self, "experimentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExperimentRef).__jsii_proxy_class__ = lambda : _IExperimentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_evidently.IFeatureRef")
class IFeatureRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Feature.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="featureRef")
    def feature_ref(self) -> "FeatureReference":
        '''(experimental) A reference to a Feature resource.

        :stability: experimental
        '''
        ...


class _IFeatureRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Feature.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_evidently.IFeatureRef"

    @builtins.property
    @jsii.member(jsii_name="featureRef")
    def feature_ref(self) -> "FeatureReference":
        '''(experimental) A reference to a Feature resource.

        :stability: experimental
        '''
        return typing.cast("FeatureReference", jsii.get(self, "featureRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFeatureRef).__jsii_proxy_class__ = lambda : _IFeatureRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_evidently.ILaunchRef")
class ILaunchRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Launch.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="launchRef")
    def launch_ref(self) -> "LaunchReference":
        '''(experimental) A reference to a Launch resource.

        :stability: experimental
        '''
        ...


class _ILaunchRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Launch.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_evidently.ILaunchRef"

    @builtins.property
    @jsii.member(jsii_name="launchRef")
    def launch_ref(self) -> "LaunchReference":
        '''(experimental) A reference to a Launch resource.

        :stability: experimental
        '''
        return typing.cast("LaunchReference", jsii.get(self, "launchRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILaunchRef).__jsii_proxy_class__ = lambda : _ILaunchRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_evidently.IProjectRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_evidently.IProjectRef"

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        return typing.cast("ProjectReference", jsii.get(self, "projectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectRef).__jsii_proxy_class__ = lambda : _IProjectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_evidently.ISegmentRef")
class ISegmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Segment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="segmentRef")
    def segment_ref(self) -> "SegmentReference":
        '''(experimental) A reference to a Segment resource.

        :stability: experimental
        '''
        ...


class _ISegmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Segment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_evidently.ISegmentRef"

    @builtins.property
    @jsii.member(jsii_name="segmentRef")
    def segment_ref(self) -> "SegmentReference":
        '''(experimental) A reference to a Segment resource.

        :stability: experimental
        '''
        return typing.cast("SegmentReference", jsii.get(self, "segmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISegmentRef).__jsii_proxy_class__ = lambda : _ISegmentRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_evidently.LaunchReference",
    jsii_struct_bases=[],
    name_mapping={"launch_arn": "launchArn"},
)
class LaunchReference:
    def __init__(self, *, launch_arn: builtins.str) -> None:
        '''A reference to a Launch resource.

        :param launch_arn: The Arn of the Launch resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_evidently as interfaces_evidently
            
            launch_reference = interfaces_evidently.LaunchReference(
                launch_arn="launchArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f08fc370928445d3ab5aeef206978f42ea5a361de0c1103dcb07d75fccf1585)
            check_type(argname="argument launch_arn", value=launch_arn, expected_type=type_hints["launch_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_arn": launch_arn,
        }

    @builtins.property
    def launch_arn(self) -> builtins.str:
        '''The Arn of the Launch resource.'''
        result = self._values.get("launch_arn")
        assert result is not None, "Required property 'launch_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_evidently.ProjectReference",
    jsii_struct_bases=[],
    name_mapping={"project_arn": "projectArn"},
)
class ProjectReference:
    def __init__(self, *, project_arn: builtins.str) -> None:
        '''A reference to a Project resource.

        :param project_arn: The Arn of the Project resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_evidently as interfaces_evidently
            
            project_reference = interfaces_evidently.ProjectReference(
                project_arn="projectArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a70a94b2940f4b0b37bcd06afa645bc43376effd49a6e6ac58020e7e136e5d9)
            check_type(argname="argument project_arn", value=project_arn, expected_type=type_hints["project_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_arn": project_arn,
        }

    @builtins.property
    def project_arn(self) -> builtins.str:
        '''The Arn of the Project resource.'''
        result = self._values.get("project_arn")
        assert result is not None, "Required property 'project_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_evidently.SegmentReference",
    jsii_struct_bases=[],
    name_mapping={"segment_arn": "segmentArn"},
)
class SegmentReference:
    def __init__(self, *, segment_arn: builtins.str) -> None:
        '''A reference to a Segment resource.

        :param segment_arn: The Arn of the Segment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_evidently as interfaces_evidently
            
            segment_reference = interfaces_evidently.SegmentReference(
                segment_arn="segmentArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d494b13284010e96daa2c9f36f99557c7bd984967c16f4868e5aaafdf3a1e539)
            check_type(argname="argument segment_arn", value=segment_arn, expected_type=type_hints["segment_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "segment_arn": segment_arn,
        }

    @builtins.property
    def segment_arn(self) -> builtins.str:
        '''The Arn of the Segment resource.'''
        result = self._values.get("segment_arn")
        assert result is not None, "Required property 'segment_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SegmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ExperimentReference",
    "FeatureReference",
    "IExperimentRef",
    "IFeatureRef",
    "ILaunchRef",
    "IProjectRef",
    "ISegmentRef",
    "LaunchReference",
    "ProjectReference",
    "SegmentReference",
]

publication.publish()

def _typecheckingstub__273c4bc4d0d70940cbdab6b36e5b93c7f24f9c57e204c269796b7aa7921ede94(
    *,
    experiment_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__831b96d67d54f4b1e981cb5f35e608263e20010bc39182b493c862218f099dec(
    *,
    feature_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f08fc370928445d3ab5aeef206978f42ea5a361de0c1103dcb07d75fccf1585(
    *,
    launch_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a70a94b2940f4b0b37bcd06afa645bc43376effd49a6e6ac58020e7e136e5d9(
    *,
    project_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d494b13284010e96daa2c9f36f99557c7bd984967c16f4868e5aaafdf3a1e539(
    *,
    segment_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IExperimentRef, IFeatureRef, ILaunchRef, IProjectRef, ISegmentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
