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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_nimblestudio.ILaunchProfileRef")
class ILaunchProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="launchProfileRef")
    def launch_profile_ref(self) -> "LaunchProfileReference":
        '''(experimental) A reference to a LaunchProfile resource.

        :stability: experimental
        '''
        ...


class _ILaunchProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_nimblestudio.ILaunchProfileRef"

    @builtins.property
    @jsii.member(jsii_name="launchProfileRef")
    def launch_profile_ref(self) -> "LaunchProfileReference":
        '''(experimental) A reference to a LaunchProfile resource.

        :stability: experimental
        '''
        return typing.cast("LaunchProfileReference", jsii.get(self, "launchProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILaunchProfileRef).__jsii_proxy_class__ = lambda : _ILaunchProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_nimblestudio.IStreamingImageRef")
class IStreamingImageRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StreamingImage.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="streamingImageRef")
    def streaming_image_ref(self) -> "StreamingImageReference":
        '''(experimental) A reference to a StreamingImage resource.

        :stability: experimental
        '''
        ...


class _IStreamingImageRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StreamingImage.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_nimblestudio.IStreamingImageRef"

    @builtins.property
    @jsii.member(jsii_name="streamingImageRef")
    def streaming_image_ref(self) -> "StreamingImageReference":
        '''(experimental) A reference to a StreamingImage resource.

        :stability: experimental
        '''
        return typing.cast("StreamingImageReference", jsii.get(self, "streamingImageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStreamingImageRef).__jsii_proxy_class__ = lambda : _IStreamingImageRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_nimblestudio.IStudioComponentRef"
)
class IStudioComponentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StudioComponent.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="studioComponentRef")
    def studio_component_ref(self) -> "StudioComponentReference":
        '''(experimental) A reference to a StudioComponent resource.

        :stability: experimental
        '''
        ...


class _IStudioComponentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StudioComponent.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_nimblestudio.IStudioComponentRef"

    @builtins.property
    @jsii.member(jsii_name="studioComponentRef")
    def studio_component_ref(self) -> "StudioComponentReference":
        '''(experimental) A reference to a StudioComponent resource.

        :stability: experimental
        '''
        return typing.cast("StudioComponentReference", jsii.get(self, "studioComponentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStudioComponentRef).__jsii_proxy_class__ = lambda : _IStudioComponentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_nimblestudio.IStudioRef")
class IStudioRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Studio.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="studioRef")
    def studio_ref(self) -> "StudioReference":
        '''(experimental) A reference to a Studio resource.

        :stability: experimental
        '''
        ...


class _IStudioRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Studio.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_nimblestudio.IStudioRef"

    @builtins.property
    @jsii.member(jsii_name="studioRef")
    def studio_ref(self) -> "StudioReference":
        '''(experimental) A reference to a Studio resource.

        :stability: experimental
        '''
        return typing.cast("StudioReference", jsii.get(self, "studioRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStudioRef).__jsii_proxy_class__ = lambda : _IStudioRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_nimblestudio.LaunchProfileReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class LaunchProfileReference:
    def __init__(self) -> None:
        '''A reference to a LaunchProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_nimblestudio as interfaces_nimblestudio
            
            launch_profile_reference = interfaces_nimblestudio.LaunchProfileReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_nimblestudio.StreamingImageReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class StreamingImageReference:
    def __init__(self) -> None:
        '''A reference to a StreamingImage resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_nimblestudio as interfaces_nimblestudio
            
            streaming_image_reference = interfaces_nimblestudio.StreamingImageReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamingImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_nimblestudio.StudioComponentReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class StudioComponentReference:
    def __init__(self) -> None:
        '''A reference to a StudioComponent resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_nimblestudio as interfaces_nimblestudio
            
            studio_component_reference = interfaces_nimblestudio.StudioComponentReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StudioComponentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_nimblestudio.StudioReference",
    jsii_struct_bases=[],
    name_mapping={"studio_id": "studioId"},
)
class StudioReference:
    def __init__(self, *, studio_id: builtins.str) -> None:
        '''A reference to a Studio resource.

        :param studio_id: The StudioId of the Studio resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_nimblestudio as interfaces_nimblestudio
            
            studio_reference = interfaces_nimblestudio.StudioReference(
                studio_id="studioId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d285466776fd973c46082868d6ee958382cde8f6b2cba14ef3c98e5148e42e49)
            check_type(argname="argument studio_id", value=studio_id, expected_type=type_hints["studio_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "studio_id": studio_id,
        }

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''The StudioId of the Studio resource.'''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StudioReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ILaunchProfileRef",
    "IStreamingImageRef",
    "IStudioComponentRef",
    "IStudioRef",
    "LaunchProfileReference",
    "StreamingImageReference",
    "StudioComponentReference",
    "StudioReference",
]

publication.publish()

def _typecheckingstub__d285466776fd973c46082868d6ee958382cde8f6b2cba14ef3c98e5148e42e49(
    *,
    studio_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ILaunchProfileRef, IStreamingImageRef, IStudioComponentRef, IStudioRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
