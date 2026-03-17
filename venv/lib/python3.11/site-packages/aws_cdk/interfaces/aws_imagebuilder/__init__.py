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
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.ComponentReference",
    jsii_struct_bases=[],
    name_mapping={"component_arn": "componentArn"},
)
class ComponentReference:
    def __init__(self, *, component_arn: builtins.str) -> None:
        '''A reference to a Component resource.

        :param component_arn: The Arn of the Component resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_imagebuilder as interfaces_imagebuilder
            
            component_reference = interfaces_imagebuilder.ComponentReference(
                component_arn="componentArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ca56b2395a8f846764be2a4a24e940c2ff5663afee7eaf27811f8696b037a37)
            check_type(argname="argument component_arn", value=component_arn, expected_type=type_hints["component_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "component_arn": component_arn,
        }

    @builtins.property
    def component_arn(self) -> builtins.str:
        '''The Arn of the Component resource.'''
        result = self._values.get("component_arn")
        assert result is not None, "Required property 'component_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComponentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.ContainerRecipeReference",
    jsii_struct_bases=[],
    name_mapping={"container_recipe_arn": "containerRecipeArn"},
)
class ContainerRecipeReference:
    def __init__(self, *, container_recipe_arn: builtins.str) -> None:
        '''A reference to a ContainerRecipe resource.

        :param container_recipe_arn: The Arn of the ContainerRecipe resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_imagebuilder as interfaces_imagebuilder
            
            container_recipe_reference = interfaces_imagebuilder.ContainerRecipeReference(
                container_recipe_arn="containerRecipeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32c30ac19c73ff0a6f39648af615b28260ba93d0aa1f57c685ecb51a53e01993)
            check_type(argname="argument container_recipe_arn", value=container_recipe_arn, expected_type=type_hints["container_recipe_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_recipe_arn": container_recipe_arn,
        }

    @builtins.property
    def container_recipe_arn(self) -> builtins.str:
        '''The Arn of the ContainerRecipe resource.'''
        result = self._values.get("container_recipe_arn")
        assert result is not None, "Required property 'container_recipe_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerRecipeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.DistributionConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"distribution_configuration_arn": "distributionConfigurationArn"},
)
class DistributionConfigurationReference:
    def __init__(self, *, distribution_configuration_arn: builtins.str) -> None:
        '''A reference to a DistributionConfiguration resource.

        :param distribution_configuration_arn: The Arn of the DistributionConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_imagebuilder as interfaces_imagebuilder
            
            distribution_configuration_reference = interfaces_imagebuilder.DistributionConfigurationReference(
                distribution_configuration_arn="distributionConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70eff7db95a3efc4f77e797d9acec5418d9e4b767751975b90ff345e2a3844e2)
            check_type(argname="argument distribution_configuration_arn", value=distribution_configuration_arn, expected_type=type_hints["distribution_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "distribution_configuration_arn": distribution_configuration_arn,
        }

    @builtins.property
    def distribution_configuration_arn(self) -> builtins.str:
        '''The Arn of the DistributionConfiguration resource.'''
        result = self._values.get("distribution_configuration_arn")
        assert result is not None, "Required property 'distribution_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributionConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.IComponentRef")
class IComponentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Component.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="componentRef")
    def component_ref(self) -> "ComponentReference":
        '''(experimental) A reference to a Component resource.

        :stability: experimental
        '''
        ...


class _IComponentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Component.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_imagebuilder.IComponentRef"

    @builtins.property
    @jsii.member(jsii_name="componentRef")
    def component_ref(self) -> "ComponentReference":
        '''(experimental) A reference to a Component resource.

        :stability: experimental
        '''
        return typing.cast("ComponentReference", jsii.get(self, "componentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IComponentRef).__jsii_proxy_class__ = lambda : _IComponentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.IContainerRecipeRef"
)
class IContainerRecipeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContainerRecipe.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="containerRecipeRef")
    def container_recipe_ref(self) -> "ContainerRecipeReference":
        '''(experimental) A reference to a ContainerRecipe resource.

        :stability: experimental
        '''
        ...


class _IContainerRecipeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContainerRecipe.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_imagebuilder.IContainerRecipeRef"

    @builtins.property
    @jsii.member(jsii_name="containerRecipeRef")
    def container_recipe_ref(self) -> "ContainerRecipeReference":
        '''(experimental) A reference to a ContainerRecipe resource.

        :stability: experimental
        '''
        return typing.cast("ContainerRecipeReference", jsii.get(self, "containerRecipeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContainerRecipeRef).__jsii_proxy_class__ = lambda : _IContainerRecipeRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.IDistributionConfigurationRef"
)
class IDistributionConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DistributionConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="distributionConfigurationRef")
    def distribution_configuration_ref(self) -> "DistributionConfigurationReference":
        '''(experimental) A reference to a DistributionConfiguration resource.

        :stability: experimental
        '''
        ...


class _IDistributionConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DistributionConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_imagebuilder.IDistributionConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="distributionConfigurationRef")
    def distribution_configuration_ref(self) -> "DistributionConfigurationReference":
        '''(experimental) A reference to a DistributionConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("DistributionConfigurationReference", jsii.get(self, "distributionConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDistributionConfigurationRef).__jsii_proxy_class__ = lambda : _IDistributionConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.IImagePipelineRef")
class IImagePipelineRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ImagePipeline.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="imagePipelineRef")
    def image_pipeline_ref(self) -> "ImagePipelineReference":
        '''(experimental) A reference to a ImagePipeline resource.

        :stability: experimental
        '''
        ...


class _IImagePipelineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ImagePipeline.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_imagebuilder.IImagePipelineRef"

    @builtins.property
    @jsii.member(jsii_name="imagePipelineRef")
    def image_pipeline_ref(self) -> "ImagePipelineReference":
        '''(experimental) A reference to a ImagePipeline resource.

        :stability: experimental
        '''
        return typing.cast("ImagePipelineReference", jsii.get(self, "imagePipelineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IImagePipelineRef).__jsii_proxy_class__ = lambda : _IImagePipelineRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.IImageRecipeRef")
class IImageRecipeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ImageRecipe.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="imageRecipeRef")
    def image_recipe_ref(self) -> "ImageRecipeReference":
        '''(experimental) A reference to a ImageRecipe resource.

        :stability: experimental
        '''
        ...


class _IImageRecipeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ImageRecipe.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_imagebuilder.IImageRecipeRef"

    @builtins.property
    @jsii.member(jsii_name="imageRecipeRef")
    def image_recipe_ref(self) -> "ImageRecipeReference":
        '''(experimental) A reference to a ImageRecipe resource.

        :stability: experimental
        '''
        return typing.cast("ImageRecipeReference", jsii.get(self, "imageRecipeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IImageRecipeRef).__jsii_proxy_class__ = lambda : _IImageRecipeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.IImageRef")
class IImageRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Image.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="imageRef")
    def image_ref(self) -> "ImageReference":
        '''(experimental) A reference to a Image resource.

        :stability: experimental
        '''
        ...


class _IImageRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Image.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_imagebuilder.IImageRef"

    @builtins.property
    @jsii.member(jsii_name="imageRef")
    def image_ref(self) -> "ImageReference":
        '''(experimental) A reference to a Image resource.

        :stability: experimental
        '''
        return typing.cast("ImageReference", jsii.get(self, "imageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IImageRef).__jsii_proxy_class__ = lambda : _IImageRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.IInfrastructureConfigurationRef"
)
class IInfrastructureConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InfrastructureConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="infrastructureConfigurationRef")
    def infrastructure_configuration_ref(
        self,
    ) -> "InfrastructureConfigurationReference":
        '''(experimental) A reference to a InfrastructureConfiguration resource.

        :stability: experimental
        '''
        ...


class _IInfrastructureConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InfrastructureConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_imagebuilder.IInfrastructureConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="infrastructureConfigurationRef")
    def infrastructure_configuration_ref(
        self,
    ) -> "InfrastructureConfigurationReference":
        '''(experimental) A reference to a InfrastructureConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("InfrastructureConfigurationReference", jsii.get(self, "infrastructureConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInfrastructureConfigurationRef).__jsii_proxy_class__ = lambda : _IInfrastructureConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.ILifecyclePolicyRef"
)
class ILifecyclePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LifecyclePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicyRef")
    def lifecycle_policy_ref(self) -> "LifecyclePolicyReference":
        '''(experimental) A reference to a LifecyclePolicy resource.

        :stability: experimental
        '''
        ...


class _ILifecyclePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LifecyclePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_imagebuilder.ILifecyclePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicyRef")
    def lifecycle_policy_ref(self) -> "LifecyclePolicyReference":
        '''(experimental) A reference to a LifecyclePolicy resource.

        :stability: experimental
        '''
        return typing.cast("LifecyclePolicyReference", jsii.get(self, "lifecyclePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILifecyclePolicyRef).__jsii_proxy_class__ = lambda : _ILifecyclePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.IWorkflowRef")
class IWorkflowRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        ...


class _IWorkflowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_imagebuilder.IWorkflowRef"

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        return typing.cast("WorkflowReference", jsii.get(self, "workflowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkflowRef).__jsii_proxy_class__ = lambda : _IWorkflowRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.ImagePipelineReference",
    jsii_struct_bases=[],
    name_mapping={"image_pipeline_arn": "imagePipelineArn"},
)
class ImagePipelineReference:
    def __init__(self, *, image_pipeline_arn: builtins.str) -> None:
        '''A reference to a ImagePipeline resource.

        :param image_pipeline_arn: The Arn of the ImagePipeline resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_imagebuilder as interfaces_imagebuilder
            
            image_pipeline_reference = interfaces_imagebuilder.ImagePipelineReference(
                image_pipeline_arn="imagePipelineArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2edfea91c44d2f5551b3f39b1283265dd4c4ba4a69e39f8470b0ee280a5f584b)
            check_type(argname="argument image_pipeline_arn", value=image_pipeline_arn, expected_type=type_hints["image_pipeline_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_pipeline_arn": image_pipeline_arn,
        }

    @builtins.property
    def image_pipeline_arn(self) -> builtins.str:
        '''The Arn of the ImagePipeline resource.'''
        result = self._values.get("image_pipeline_arn")
        assert result is not None, "Required property 'image_pipeline_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImagePipelineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.ImageRecipeReference",
    jsii_struct_bases=[],
    name_mapping={"image_recipe_arn": "imageRecipeArn"},
)
class ImageRecipeReference:
    def __init__(self, *, image_recipe_arn: builtins.str) -> None:
        '''A reference to a ImageRecipe resource.

        :param image_recipe_arn: The Arn of the ImageRecipe resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_imagebuilder as interfaces_imagebuilder
            
            image_recipe_reference = interfaces_imagebuilder.ImageRecipeReference(
                image_recipe_arn="imageRecipeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__822a60b009e7a8fb8c6138b46d26bf862351f4cdd38d9300a4e14ca1672119c5)
            check_type(argname="argument image_recipe_arn", value=image_recipe_arn, expected_type=type_hints["image_recipe_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_recipe_arn": image_recipe_arn,
        }

    @builtins.property
    def image_recipe_arn(self) -> builtins.str:
        '''The Arn of the ImageRecipe resource.'''
        result = self._values.get("image_recipe_arn")
        assert result is not None, "Required property 'image_recipe_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageRecipeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.ImageReference",
    jsii_struct_bases=[],
    name_mapping={"image_arn": "imageArn"},
)
class ImageReference:
    def __init__(self, *, image_arn: builtins.str) -> None:
        '''A reference to a Image resource.

        :param image_arn: The Arn of the Image resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_imagebuilder as interfaces_imagebuilder
            
            image_reference = interfaces_imagebuilder.ImageReference(
                image_arn="imageArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c2e068912f6d5b798b23176aa40959a1849e60e2b42920c7f82c6ebe6c05e20)
            check_type(argname="argument image_arn", value=image_arn, expected_type=type_hints["image_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_arn": image_arn,
        }

    @builtins.property
    def image_arn(self) -> builtins.str:
        '''The Arn of the Image resource.'''
        result = self._values.get("image_arn")
        assert result is not None, "Required property 'image_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.InfrastructureConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "infrastructure_configuration_arn": "infrastructureConfigurationArn",
    },
)
class InfrastructureConfigurationReference:
    def __init__(self, *, infrastructure_configuration_arn: builtins.str) -> None:
        '''A reference to a InfrastructureConfiguration resource.

        :param infrastructure_configuration_arn: The Arn of the InfrastructureConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_imagebuilder as interfaces_imagebuilder
            
            infrastructure_configuration_reference = interfaces_imagebuilder.InfrastructureConfigurationReference(
                infrastructure_configuration_arn="infrastructureConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c26eaf1e4681c4f419e405ba90cc4bd6133a1009f5afbd003651f78fd48ef87)
            check_type(argname="argument infrastructure_configuration_arn", value=infrastructure_configuration_arn, expected_type=type_hints["infrastructure_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "infrastructure_configuration_arn": infrastructure_configuration_arn,
        }

    @builtins.property
    def infrastructure_configuration_arn(self) -> builtins.str:
        '''The Arn of the InfrastructureConfiguration resource.'''
        result = self._values.get("infrastructure_configuration_arn")
        assert result is not None, "Required property 'infrastructure_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InfrastructureConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.LifecyclePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"lifecycle_policy_arn": "lifecyclePolicyArn"},
)
class LifecyclePolicyReference:
    def __init__(self, *, lifecycle_policy_arn: builtins.str) -> None:
        '''A reference to a LifecyclePolicy resource.

        :param lifecycle_policy_arn: The Arn of the LifecyclePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_imagebuilder as interfaces_imagebuilder
            
            lifecycle_policy_reference = interfaces_imagebuilder.LifecyclePolicyReference(
                lifecycle_policy_arn="lifecyclePolicyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0e33e0615fd6db354b50325a083d7a4ba4c4fd4b885437c35be0e5f9149ca3a)
            check_type(argname="argument lifecycle_policy_arn", value=lifecycle_policy_arn, expected_type=type_hints["lifecycle_policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lifecycle_policy_arn": lifecycle_policy_arn,
        }

    @builtins.property
    def lifecycle_policy_arn(self) -> builtins.str:
        '''The Arn of the LifecyclePolicy resource.'''
        result = self._values.get("lifecycle_policy_arn")
        assert result is not None, "Required property 'lifecycle_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LifecyclePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_imagebuilder.WorkflowReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_arn": "workflowArn"},
)
class WorkflowReference:
    def __init__(self, *, workflow_arn: builtins.str) -> None:
        '''A reference to a Workflow resource.

        :param workflow_arn: The Arn of the Workflow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_imagebuilder as interfaces_imagebuilder
            
            workflow_reference = interfaces_imagebuilder.WorkflowReference(
                workflow_arn="workflowArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c546261c2556897bd85b6ea4c73c8e1757dc626717aab7bab599cf97ba458923)
            check_type(argname="argument workflow_arn", value=workflow_arn, expected_type=type_hints["workflow_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_arn": workflow_arn,
        }

    @builtins.property
    def workflow_arn(self) -> builtins.str:
        '''The Arn of the Workflow resource.'''
        result = self._values.get("workflow_arn")
        assert result is not None, "Required property 'workflow_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ComponentReference",
    "ContainerRecipeReference",
    "DistributionConfigurationReference",
    "IComponentRef",
    "IContainerRecipeRef",
    "IDistributionConfigurationRef",
    "IImagePipelineRef",
    "IImageRecipeRef",
    "IImageRef",
    "IInfrastructureConfigurationRef",
    "ILifecyclePolicyRef",
    "IWorkflowRef",
    "ImagePipelineReference",
    "ImageRecipeReference",
    "ImageReference",
    "InfrastructureConfigurationReference",
    "LifecyclePolicyReference",
    "WorkflowReference",
]

publication.publish()

def _typecheckingstub__1ca56b2395a8f846764be2a4a24e940c2ff5663afee7eaf27811f8696b037a37(
    *,
    component_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32c30ac19c73ff0a6f39648af615b28260ba93d0aa1f57c685ecb51a53e01993(
    *,
    container_recipe_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70eff7db95a3efc4f77e797d9acec5418d9e4b767751975b90ff345e2a3844e2(
    *,
    distribution_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2edfea91c44d2f5551b3f39b1283265dd4c4ba4a69e39f8470b0ee280a5f584b(
    *,
    image_pipeline_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__822a60b009e7a8fb8c6138b46d26bf862351f4cdd38d9300a4e14ca1672119c5(
    *,
    image_recipe_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c2e068912f6d5b798b23176aa40959a1849e60e2b42920c7f82c6ebe6c05e20(
    *,
    image_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c26eaf1e4681c4f419e405ba90cc4bd6133a1009f5afbd003651f78fd48ef87(
    *,
    infrastructure_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e33e0615fd6db354b50325a083d7a4ba4c4fd4b885437c35be0e5f9149ca3a(
    *,
    lifecycle_policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c546261c2556897bd85b6ea4c73c8e1757dc626717aab7bab599cf97ba458923(
    *,
    workflow_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IComponentRef, IContainerRecipeRef, IDistributionConfigurationRef, IImagePipelineRef, IImageRecipeRef, IImageRef, IInfrastructureConfigurationRef, ILifecyclePolicyRef, IWorkflowRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
