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
    jsii_type="aws-cdk-lib.interfaces.aws_inspector.AssessmentTargetReference",
    jsii_struct_bases=[],
    name_mapping={"assessment_target_arn": "assessmentTargetArn"},
)
class AssessmentTargetReference:
    def __init__(self, *, assessment_target_arn: builtins.str) -> None:
        '''A reference to a AssessmentTarget resource.

        :param assessment_target_arn: The Arn of the AssessmentTarget resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_inspector as interfaces_inspector
            
            assessment_target_reference = interfaces_inspector.AssessmentTargetReference(
                assessment_target_arn="assessmentTargetArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8b8f599bceaadd0d2c2ab9dcd0ade6505ea4009df50526fa0c122e128ba8896)
            check_type(argname="argument assessment_target_arn", value=assessment_target_arn, expected_type=type_hints["assessment_target_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assessment_target_arn": assessment_target_arn,
        }

    @builtins.property
    def assessment_target_arn(self) -> builtins.str:
        '''The Arn of the AssessmentTarget resource.'''
        result = self._values.get("assessment_target_arn")
        assert result is not None, "Required property 'assessment_target_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssessmentTargetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_inspector.AssessmentTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"assessment_template_arn": "assessmentTemplateArn"},
)
class AssessmentTemplateReference:
    def __init__(self, *, assessment_template_arn: builtins.str) -> None:
        '''A reference to a AssessmentTemplate resource.

        :param assessment_template_arn: The Arn of the AssessmentTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_inspector as interfaces_inspector
            
            assessment_template_reference = interfaces_inspector.AssessmentTemplateReference(
                assessment_template_arn="assessmentTemplateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e907696c4f08f302eb003a0307c44624fcc3bcbf21e5da09caefef1b2d5ac630)
            check_type(argname="argument assessment_template_arn", value=assessment_template_arn, expected_type=type_hints["assessment_template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assessment_template_arn": assessment_template_arn,
        }

    @builtins.property
    def assessment_template_arn(self) -> builtins.str:
        '''The Arn of the AssessmentTemplate resource.'''
        result = self._values.get("assessment_template_arn")
        assert result is not None, "Required property 'assessment_template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssessmentTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_inspector.IAssessmentTargetRef")
class IAssessmentTargetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AssessmentTarget.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="assessmentTargetRef")
    def assessment_target_ref(self) -> "AssessmentTargetReference":
        '''(experimental) A reference to a AssessmentTarget resource.

        :stability: experimental
        '''
        ...


class _IAssessmentTargetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AssessmentTarget.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_inspector.IAssessmentTargetRef"

    @builtins.property
    @jsii.member(jsii_name="assessmentTargetRef")
    def assessment_target_ref(self) -> "AssessmentTargetReference":
        '''(experimental) A reference to a AssessmentTarget resource.

        :stability: experimental
        '''
        return typing.cast("AssessmentTargetReference", jsii.get(self, "assessmentTargetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssessmentTargetRef).__jsii_proxy_class__ = lambda : _IAssessmentTargetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_inspector.IAssessmentTemplateRef"
)
class IAssessmentTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AssessmentTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="assessmentTemplateRef")
    def assessment_template_ref(self) -> "AssessmentTemplateReference":
        '''(experimental) A reference to a AssessmentTemplate resource.

        :stability: experimental
        '''
        ...


class _IAssessmentTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AssessmentTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_inspector.IAssessmentTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="assessmentTemplateRef")
    def assessment_template_ref(self) -> "AssessmentTemplateReference":
        '''(experimental) A reference to a AssessmentTemplate resource.

        :stability: experimental
        '''
        return typing.cast("AssessmentTemplateReference", jsii.get(self, "assessmentTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssessmentTemplateRef).__jsii_proxy_class__ = lambda : _IAssessmentTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_inspector.IResourceGroupRef")
class IResourceGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceGroupRef")
    def resource_group_ref(self) -> "ResourceGroupReference":
        '''(experimental) A reference to a ResourceGroup resource.

        :stability: experimental
        '''
        ...


class _IResourceGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_inspector.IResourceGroupRef"

    @builtins.property
    @jsii.member(jsii_name="resourceGroupRef")
    def resource_group_ref(self) -> "ResourceGroupReference":
        '''(experimental) A reference to a ResourceGroup resource.

        :stability: experimental
        '''
        return typing.cast("ResourceGroupReference", jsii.get(self, "resourceGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceGroupRef).__jsii_proxy_class__ = lambda : _IResourceGroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_inspector.ResourceGroupReference",
    jsii_struct_bases=[],
    name_mapping={"resource_group_arn": "resourceGroupArn"},
)
class ResourceGroupReference:
    def __init__(self, *, resource_group_arn: builtins.str) -> None:
        '''A reference to a ResourceGroup resource.

        :param resource_group_arn: The Arn of the ResourceGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_inspector as interfaces_inspector
            
            resource_group_reference = interfaces_inspector.ResourceGroupReference(
                resource_group_arn="resourceGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__660c353b6816ac5684115ed98eadd56d22276ac8139cce9abc79d6b46cb922bc)
            check_type(argname="argument resource_group_arn", value=resource_group_arn, expected_type=type_hints["resource_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_group_arn": resource_group_arn,
        }

    @builtins.property
    def resource_group_arn(self) -> builtins.str:
        '''The Arn of the ResourceGroup resource.'''
        result = self._values.get("resource_group_arn")
        assert result is not None, "Required property 'resource_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AssessmentTargetReference",
    "AssessmentTemplateReference",
    "IAssessmentTargetRef",
    "IAssessmentTemplateRef",
    "IResourceGroupRef",
    "ResourceGroupReference",
]

publication.publish()

def _typecheckingstub__c8b8f599bceaadd0d2c2ab9dcd0ade6505ea4009df50526fa0c122e128ba8896(
    *,
    assessment_target_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e907696c4f08f302eb003a0307c44624fcc3bcbf21e5da09caefef1b2d5ac630(
    *,
    assessment_template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660c353b6816ac5684115ed98eadd56d22276ac8139cce9abc79d6b46cb922bc(
    *,
    resource_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAssessmentTargetRef, IAssessmentTemplateRef, IResourceGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
