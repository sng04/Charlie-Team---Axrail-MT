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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconvert.IJobTemplateRef")
class IJobTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a JobTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="jobTemplateRef")
    def job_template_ref(self) -> "JobTemplateReference":
        '''(experimental) A reference to a JobTemplate resource.

        :stability: experimental
        '''
        ...


class _IJobTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a JobTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconvert.IJobTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="jobTemplateRef")
    def job_template_ref(self) -> "JobTemplateReference":
        '''(experimental) A reference to a JobTemplate resource.

        :stability: experimental
        '''
        return typing.cast("JobTemplateReference", jsii.get(self, "jobTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJobTemplateRef).__jsii_proxy_class__ = lambda : _IJobTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconvert.IPresetRef")
class IPresetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Preset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="presetRef")
    def preset_ref(self) -> "PresetReference":
        '''(experimental) A reference to a Preset resource.

        :stability: experimental
        '''
        ...


class _IPresetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Preset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconvert.IPresetRef"

    @builtins.property
    @jsii.member(jsii_name="presetRef")
    def preset_ref(self) -> "PresetReference":
        '''(experimental) A reference to a Preset resource.

        :stability: experimental
        '''
        return typing.cast("PresetReference", jsii.get(self, "presetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPresetRef).__jsii_proxy_class__ = lambda : _IPresetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconvert.IQueueRef")
class IQueueRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        ...


class _IQueueRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconvert.IQueueRef"

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        return typing.cast("QueueReference", jsii.get(self, "queueRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueueRef).__jsii_proxy_class__ = lambda : _IQueueRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconvert.JobTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "job_template_arn": "jobTemplateArn",
        "job_template_name": "jobTemplateName",
    },
)
class JobTemplateReference:
    def __init__(
        self,
        *,
        job_template_arn: builtins.str,
        job_template_name: builtins.str,
    ) -> None:
        '''A reference to a JobTemplate resource.

        :param job_template_arn: The ARN of the JobTemplate resource.
        :param job_template_name: The Name of the JobTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconvert as interfaces_mediaconvert
            
            job_template_reference = interfaces_mediaconvert.JobTemplateReference(
                job_template_arn="jobTemplateArn",
                job_template_name="jobTemplateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7057bf140c0efe97b502c8c81350b25690b2d11402f6434cea5a83600a341d37)
            check_type(argname="argument job_template_arn", value=job_template_arn, expected_type=type_hints["job_template_arn"])
            check_type(argname="argument job_template_name", value=job_template_name, expected_type=type_hints["job_template_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_template_arn": job_template_arn,
            "job_template_name": job_template_name,
        }

    @builtins.property
    def job_template_arn(self) -> builtins.str:
        '''The ARN of the JobTemplate resource.'''
        result = self._values.get("job_template_arn")
        assert result is not None, "Required property 'job_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def job_template_name(self) -> builtins.str:
        '''The Name of the JobTemplate resource.'''
        result = self._values.get("job_template_name")
        assert result is not None, "Required property 'job_template_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconvert.PresetReference",
    jsii_struct_bases=[],
    name_mapping={"preset_arn": "presetArn", "preset_name": "presetName"},
)
class PresetReference:
    def __init__(self, *, preset_arn: builtins.str, preset_name: builtins.str) -> None:
        '''A reference to a Preset resource.

        :param preset_arn: The ARN of the Preset resource.
        :param preset_name: The Name of the Preset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconvert as interfaces_mediaconvert
            
            preset_reference = interfaces_mediaconvert.PresetReference(
                preset_arn="presetArn",
                preset_name="presetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a094c7e15534639180349b8892b52804fbafd16fecc7b750df6e04ef1dd33c2)
            check_type(argname="argument preset_arn", value=preset_arn, expected_type=type_hints["preset_arn"])
            check_type(argname="argument preset_name", value=preset_name, expected_type=type_hints["preset_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "preset_arn": preset_arn,
            "preset_name": preset_name,
        }

    @builtins.property
    def preset_arn(self) -> builtins.str:
        '''The ARN of the Preset resource.'''
        result = self._values.get("preset_arn")
        assert result is not None, "Required property 'preset_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preset_name(self) -> builtins.str:
        '''The Name of the Preset resource.'''
        result = self._values.get("preset_name")
        assert result is not None, "Required property 'preset_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PresetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconvert.QueueReference",
    jsii_struct_bases=[],
    name_mapping={"queue_arn": "queueArn", "queue_name": "queueName"},
)
class QueueReference:
    def __init__(self, *, queue_arn: builtins.str, queue_name: builtins.str) -> None:
        '''A reference to a Queue resource.

        :param queue_arn: The ARN of the Queue resource.
        :param queue_name: The Name of the Queue resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconvert as interfaces_mediaconvert
            
            queue_reference = interfaces_mediaconvert.QueueReference(
                queue_arn="queueArn",
                queue_name="queueName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8d20bb72aaa75880deb41e80cf087e8733dde75baef670e7f1346b59f19e481)
            check_type(argname="argument queue_arn", value=queue_arn, expected_type=type_hints["queue_arn"])
            check_type(argname="argument queue_name", value=queue_name, expected_type=type_hints["queue_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "queue_arn": queue_arn,
            "queue_name": queue_name,
        }

    @builtins.property
    def queue_arn(self) -> builtins.str:
        '''The ARN of the Queue resource.'''
        result = self._values.get("queue_arn")
        assert result is not None, "Required property 'queue_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_name(self) -> builtins.str:
        '''The Name of the Queue resource.'''
        result = self._values.get("queue_name")
        assert result is not None, "Required property 'queue_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IJobTemplateRef",
    "IPresetRef",
    "IQueueRef",
    "JobTemplateReference",
    "PresetReference",
    "QueueReference",
]

publication.publish()

def _typecheckingstub__7057bf140c0efe97b502c8c81350b25690b2d11402f6434cea5a83600a341d37(
    *,
    job_template_arn: builtins.str,
    job_template_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a094c7e15534639180349b8892b52804fbafd16fecc7b750df6e04ef1dd33c2(
    *,
    preset_arn: builtins.str,
    preset_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8d20bb72aaa75880deb41e80cf087e8733dde75baef670e7f1346b59f19e481(
    *,
    queue_arn: builtins.str,
    queue_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IJobTemplateRef, IPresetRef, IQueueRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
