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
    jsii_type="aws-cdk-lib.interfaces.aws_databrew.DatasetReference",
    jsii_struct_bases=[],
    name_mapping={"dataset_name": "datasetName"},
)
class DatasetReference:
    def __init__(self, *, dataset_name: builtins.str) -> None:
        '''A reference to a Dataset resource.

        :param dataset_name: The Name of the Dataset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_databrew as interfaces_databrew
            
            dataset_reference = interfaces_databrew.DatasetReference(
                dataset_name="datasetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0239bca793c0eabd283a630a5da2409581b1c6fda4d61a82aa36a5197fa003a1)
            check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataset_name": dataset_name,
        }

    @builtins.property
    def dataset_name(self) -> builtins.str:
        '''The Name of the Dataset resource.'''
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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_databrew.IDatasetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_databrew.IDatasetRef"

    @builtins.property
    @jsii.member(jsii_name="datasetRef")
    def dataset_ref(self) -> "DatasetReference":
        '''(experimental) A reference to a Dataset resource.

        :stability: experimental
        '''
        return typing.cast("DatasetReference", jsii.get(self, "datasetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatasetRef).__jsii_proxy_class__ = lambda : _IDatasetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_databrew.IJobRef")
class IJobRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Job.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="jobRef")
    def job_ref(self) -> "JobReference":
        '''(experimental) A reference to a Job resource.

        :stability: experimental
        '''
        ...


class _IJobRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Job.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_databrew.IJobRef"

    @builtins.property
    @jsii.member(jsii_name="jobRef")
    def job_ref(self) -> "JobReference":
        '''(experimental) A reference to a Job resource.

        :stability: experimental
        '''
        return typing.cast("JobReference", jsii.get(self, "jobRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJobRef).__jsii_proxy_class__ = lambda : _IJobRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_databrew.IProjectRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_databrew.IProjectRef"

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        return typing.cast("ProjectReference", jsii.get(self, "projectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectRef).__jsii_proxy_class__ = lambda : _IProjectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_databrew.IRecipeRef")
class IRecipeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Recipe.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="recipeRef")
    def recipe_ref(self) -> "RecipeReference":
        '''(experimental) A reference to a Recipe resource.

        :stability: experimental
        '''
        ...


class _IRecipeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Recipe.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_databrew.IRecipeRef"

    @builtins.property
    @jsii.member(jsii_name="recipeRef")
    def recipe_ref(self) -> "RecipeReference":
        '''(experimental) A reference to a Recipe resource.

        :stability: experimental
        '''
        return typing.cast("RecipeReference", jsii.get(self, "recipeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRecipeRef).__jsii_proxy_class__ = lambda : _IRecipeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_databrew.IRulesetRef")
class IRulesetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Ruleset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="rulesetRef")
    def ruleset_ref(self) -> "RulesetReference":
        '''(experimental) A reference to a Ruleset resource.

        :stability: experimental
        '''
        ...


class _IRulesetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Ruleset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_databrew.IRulesetRef"

    @builtins.property
    @jsii.member(jsii_name="rulesetRef")
    def ruleset_ref(self) -> "RulesetReference":
        '''(experimental) A reference to a Ruleset resource.

        :stability: experimental
        '''
        return typing.cast("RulesetReference", jsii.get(self, "rulesetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRulesetRef).__jsii_proxy_class__ = lambda : _IRulesetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_databrew.IScheduleRef")
class IScheduleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Schedule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scheduleRef")
    def schedule_ref(self) -> "ScheduleReference":
        '''(experimental) A reference to a Schedule resource.

        :stability: experimental
        '''
        ...


class _IScheduleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Schedule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_databrew.IScheduleRef"

    @builtins.property
    @jsii.member(jsii_name="scheduleRef")
    def schedule_ref(self) -> "ScheduleReference":
        '''(experimental) A reference to a Schedule resource.

        :stability: experimental
        '''
        return typing.cast("ScheduleReference", jsii.get(self, "scheduleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduleRef).__jsii_proxy_class__ = lambda : _IScheduleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_databrew.JobReference",
    jsii_struct_bases=[],
    name_mapping={"job_name": "jobName"},
)
class JobReference:
    def __init__(self, *, job_name: builtins.str) -> None:
        '''A reference to a Job resource.

        :param job_name: The Name of the Job resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_databrew as interfaces_databrew
            
            job_reference = interfaces_databrew.JobReference(
                job_name="jobName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42380f439dc32a43a8fc0af1552d8ab791245328b89fe5ffc5c2e9d56eecb595)
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_name": job_name,
        }

    @builtins.property
    def job_name(self) -> builtins.str:
        '''The Name of the Job resource.'''
        result = self._values.get("job_name")
        assert result is not None, "Required property 'job_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_databrew.ProjectReference",
    jsii_struct_bases=[],
    name_mapping={"project_name": "projectName"},
)
class ProjectReference:
    def __init__(self, *, project_name: builtins.str) -> None:
        '''A reference to a Project resource.

        :param project_name: The Name of the Project resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_databrew as interfaces_databrew
            
            project_reference = interfaces_databrew.ProjectReference(
                project_name="projectName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59c8103ac9401128da2a77ebf6a0d111eb77a2abc59bd266e0d1f16e6fd1692c)
            check_type(argname="argument project_name", value=project_name, expected_type=type_hints["project_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_name": project_name,
        }

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
    jsii_type="aws-cdk-lib.interfaces.aws_databrew.RecipeReference",
    jsii_struct_bases=[],
    name_mapping={"recipe_name": "recipeName"},
)
class RecipeReference:
    def __init__(self, *, recipe_name: builtins.str) -> None:
        '''A reference to a Recipe resource.

        :param recipe_name: The Name of the Recipe resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_databrew as interfaces_databrew
            
            recipe_reference = interfaces_databrew.RecipeReference(
                recipe_name="recipeName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8baa6acc267e59b164091037ba9c11ef292fdf3e2d6dd5de6a4dd3bf77fde3ff)
            check_type(argname="argument recipe_name", value=recipe_name, expected_type=type_hints["recipe_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "recipe_name": recipe_name,
        }

    @builtins.property
    def recipe_name(self) -> builtins.str:
        '''The Name of the Recipe resource.'''
        result = self._values.get("recipe_name")
        assert result is not None, "Required property 'recipe_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecipeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_databrew.RulesetReference",
    jsii_struct_bases=[],
    name_mapping={"ruleset_name": "rulesetName"},
)
class RulesetReference:
    def __init__(self, *, ruleset_name: builtins.str) -> None:
        '''A reference to a Ruleset resource.

        :param ruleset_name: The Name of the Ruleset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_databrew as interfaces_databrew
            
            ruleset_reference = interfaces_databrew.RulesetReference(
                ruleset_name="rulesetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62bdf2ec578a001083ee81c43682fcb8e156829011ab968def5d66a0c9224e71)
            check_type(argname="argument ruleset_name", value=ruleset_name, expected_type=type_hints["ruleset_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ruleset_name": ruleset_name,
        }

    @builtins.property
    def ruleset_name(self) -> builtins.str:
        '''The Name of the Ruleset resource.'''
        result = self._values.get("ruleset_name")
        assert result is not None, "Required property 'ruleset_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RulesetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_databrew.ScheduleReference",
    jsii_struct_bases=[],
    name_mapping={"schedule_name": "scheduleName"},
)
class ScheduleReference:
    def __init__(self, *, schedule_name: builtins.str) -> None:
        '''A reference to a Schedule resource.

        :param schedule_name: The Name of the Schedule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_databrew as interfaces_databrew
            
            schedule_reference = interfaces_databrew.ScheduleReference(
                schedule_name="scheduleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5fd760f68af1ceb3fbdd2b6f4635aa344c4930368cb0ba27a066745f51a1fa)
            check_type(argname="argument schedule_name", value=schedule_name, expected_type=type_hints["schedule_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schedule_name": schedule_name,
        }

    @builtins.property
    def schedule_name(self) -> builtins.str:
        '''The Name of the Schedule resource.'''
        result = self._values.get("schedule_name")
        assert result is not None, "Required property 'schedule_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatasetReference",
    "IDatasetRef",
    "IJobRef",
    "IProjectRef",
    "IRecipeRef",
    "IRulesetRef",
    "IScheduleRef",
    "JobReference",
    "ProjectReference",
    "RecipeReference",
    "RulesetReference",
    "ScheduleReference",
]

publication.publish()

def _typecheckingstub__0239bca793c0eabd283a630a5da2409581b1c6fda4d61a82aa36a5197fa003a1(
    *,
    dataset_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42380f439dc32a43a8fc0af1552d8ab791245328b89fe5ffc5c2e9d56eecb595(
    *,
    job_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59c8103ac9401128da2a77ebf6a0d111eb77a2abc59bd266e0d1f16e6fd1692c(
    *,
    project_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8baa6acc267e59b164091037ba9c11ef292fdf3e2d6dd5de6a4dd3bf77fde3ff(
    *,
    recipe_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62bdf2ec578a001083ee81c43682fcb8e156829011ab968def5d66a0c9224e71(
    *,
    ruleset_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5fd760f68af1ceb3fbdd2b6f4635aa344c4930368cb0ba27a066745f51a1fa(
    *,
    schedule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDatasetRef, IJobRef, IProjectRef, IRecipeRef, IRulesetRef, IScheduleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
