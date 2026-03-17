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
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.AppReference",
    jsii_struct_bases=[],
    name_mapping={"app_id": "appId"},
)
class AppReference:
    def __init__(self, *, app_id: builtins.str) -> None:
        '''A reference to a App resource.

        :param app_id: The Id of the App resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            app_reference = interfaces_opsworks.AppReference(
                app_id="appId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0c551713e40277c55a6aa34fecf93fc68a27bf62797d47dc60613cd2a435b38)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
        }

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The Id of the App resource.'''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.ElasticLoadBalancerAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "elastic_load_balancer_attachment_id": "elasticLoadBalancerAttachmentId",
    },
)
class ElasticLoadBalancerAttachmentReference:
    def __init__(self, *, elastic_load_balancer_attachment_id: builtins.str) -> None:
        '''A reference to a ElasticLoadBalancerAttachment resource.

        :param elastic_load_balancer_attachment_id: The Id of the ElasticLoadBalancerAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            elastic_load_balancer_attachment_reference = interfaces_opsworks.ElasticLoadBalancerAttachmentReference(
                elastic_load_balancer_attachment_id="elasticLoadBalancerAttachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d3c8dd924ad4994b9195afd966c18d0950398fb10f8078b91f2679d74e08117)
            check_type(argname="argument elastic_load_balancer_attachment_id", value=elastic_load_balancer_attachment_id, expected_type=type_hints["elastic_load_balancer_attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "elastic_load_balancer_attachment_id": elastic_load_balancer_attachment_id,
        }

    @builtins.property
    def elastic_load_balancer_attachment_id(self) -> builtins.str:
        '''The Id of the ElasticLoadBalancerAttachment resource.'''
        result = self._values.get("elastic_load_balancer_attachment_id")
        assert result is not None, "Required property 'elastic_load_balancer_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticLoadBalancerAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IAppRef")
class IAppRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        ...


class _IAppRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IAppRef"

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        return typing.cast("AppReference", jsii.get(self, "appRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppRef).__jsii_proxy_class__ = lambda : _IAppRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IElasticLoadBalancerAttachmentRef"
)
class IElasticLoadBalancerAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ElasticLoadBalancerAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancerAttachmentRef")
    def elastic_load_balancer_attachment_ref(
        self,
    ) -> "ElasticLoadBalancerAttachmentReference":
        '''(experimental) A reference to a ElasticLoadBalancerAttachment resource.

        :stability: experimental
        '''
        ...


class _IElasticLoadBalancerAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ElasticLoadBalancerAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IElasticLoadBalancerAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="elasticLoadBalancerAttachmentRef")
    def elastic_load_balancer_attachment_ref(
        self,
    ) -> "ElasticLoadBalancerAttachmentReference":
        '''(experimental) A reference to a ElasticLoadBalancerAttachment resource.

        :stability: experimental
        '''
        return typing.cast("ElasticLoadBalancerAttachmentReference", jsii.get(self, "elasticLoadBalancerAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IElasticLoadBalancerAttachmentRef).__jsii_proxy_class__ = lambda : _IElasticLoadBalancerAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IInstanceRef")
class IInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Instance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        ...


class _IInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Instance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        return typing.cast("InstanceReference", jsii.get(self, "instanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceRef).__jsii_proxy_class__ = lambda : _IInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.ILayerRef")
class ILayerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Layer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="layerRef")
    def layer_ref(self) -> "LayerReference":
        '''(experimental) A reference to a Layer resource.

        :stability: experimental
        '''
        ...


class _ILayerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Layer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.ILayerRef"

    @builtins.property
    @jsii.member(jsii_name="layerRef")
    def layer_ref(self) -> "LayerReference":
        '''(experimental) A reference to a Layer resource.

        :stability: experimental
        '''
        return typing.cast("LayerReference", jsii.get(self, "layerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILayerRef).__jsii_proxy_class__ = lambda : _ILayerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IStackRef")
class IStackRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Stack.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stackRef")
    def stack_ref(self) -> "StackReference":
        '''(experimental) A reference to a Stack resource.

        :stability: experimental
        '''
        ...


class _IStackRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Stack.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IStackRef"

    @builtins.property
    @jsii.member(jsii_name="stackRef")
    def stack_ref(self) -> "StackReference":
        '''(experimental) A reference to a Stack resource.

        :stability: experimental
        '''
        return typing.cast("StackReference", jsii.get(self, "stackRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackRef).__jsii_proxy_class__ = lambda : _IStackRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IUserProfileRef")
class IUserProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userProfileRef")
    def user_profile_ref(self) -> "UserProfileReference":
        '''(experimental) A reference to a UserProfile resource.

        :stability: experimental
        '''
        ...


class _IUserProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IUserProfileRef"

    @builtins.property
    @jsii.member(jsii_name="userProfileRef")
    def user_profile_ref(self) -> "UserProfileReference":
        '''(experimental) A reference to a UserProfile resource.

        :stability: experimental
        '''
        return typing.cast("UserProfileReference", jsii.get(self, "userProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserProfileRef).__jsii_proxy_class__ = lambda : _IUserProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_opsworks.IVolumeRef")
class IVolumeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        ...


class _IVolumeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_opsworks.IVolumeRef"

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        return typing.cast("VolumeReference", jsii.get(self, "volumeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVolumeRef).__jsii_proxy_class__ = lambda : _IVolumeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.InstanceReference",
    jsii_struct_bases=[],
    name_mapping={"instance_id": "instanceId"},
)
class InstanceReference:
    def __init__(self, *, instance_id: builtins.str) -> None:
        '''A reference to a Instance resource.

        :param instance_id: The Id of the Instance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            instance_reference = interfaces_opsworks.InstanceReference(
                instance_id="instanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__895cec226c11fff5e2501bf617655014b5c476842d77743c043755d94cf4902a)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
        }

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The Id of the Instance resource.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.LayerReference",
    jsii_struct_bases=[],
    name_mapping={"layer_id": "layerId"},
)
class LayerReference:
    def __init__(self, *, layer_id: builtins.str) -> None:
        '''A reference to a Layer resource.

        :param layer_id: The Id of the Layer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            layer_reference = interfaces_opsworks.LayerReference(
                layer_id="layerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f515be01b79f66817a8720fdb1c48591d298d39dd85b86723b2cfa226000e98)
            check_type(argname="argument layer_id", value=layer_id, expected_type=type_hints["layer_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "layer_id": layer_id,
        }

    @builtins.property
    def layer_id(self) -> builtins.str:
        '''The Id of the Layer resource.'''
        result = self._values.get("layer_id")
        assert result is not None, "Required property 'layer_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.StackReference",
    jsii_struct_bases=[],
    name_mapping={"stack_id": "stackId"},
)
class StackReference:
    def __init__(self, *, stack_id: builtins.str) -> None:
        '''A reference to a Stack resource.

        :param stack_id: The Id of the Stack resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            stack_reference = interfaces_opsworks.StackReference(
                stack_id="stackId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2cc53fe8368ff29f02f3d4cfd0cd430b913740167ad005b9f6aeaf877419c17)
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stack_id": stack_id,
        }

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''The Id of the Stack resource.'''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.UserProfileReference",
    jsii_struct_bases=[],
    name_mapping={"user_profile_id": "userProfileId"},
)
class UserProfileReference:
    def __init__(self, *, user_profile_id: builtins.str) -> None:
        '''A reference to a UserProfile resource.

        :param user_profile_id: The Id of the UserProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            user_profile_reference = interfaces_opsworks.UserProfileReference(
                user_profile_id="userProfileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07032bd286f2c6831af6600508d1b6611c89b34e96e91eb295766dbd00a81ba5)
            check_type(argname="argument user_profile_id", value=user_profile_id, expected_type=type_hints["user_profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_profile_id": user_profile_id,
        }

    @builtins.property
    def user_profile_id(self) -> builtins.str:
        '''The Id of the UserProfile resource.'''
        result = self._values.get("user_profile_id")
        assert result is not None, "Required property 'user_profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_opsworks.VolumeReference",
    jsii_struct_bases=[],
    name_mapping={"volume_id": "volumeId"},
)
class VolumeReference:
    def __init__(self, *, volume_id: builtins.str) -> None:
        '''A reference to a Volume resource.

        :param volume_id: The Id of the Volume resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_opsworks as interfaces_opsworks
            
            volume_reference = interfaces_opsworks.VolumeReference(
                volume_id="volumeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1d2a127f5d0d2cf3cb22749134f0f85e3e64120f84467645be864337323c6bf)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The Id of the Volume resource.'''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppReference",
    "ElasticLoadBalancerAttachmentReference",
    "IAppRef",
    "IElasticLoadBalancerAttachmentRef",
    "IInstanceRef",
    "ILayerRef",
    "IStackRef",
    "IUserProfileRef",
    "IVolumeRef",
    "InstanceReference",
    "LayerReference",
    "StackReference",
    "UserProfileReference",
    "VolumeReference",
]

publication.publish()

def _typecheckingstub__e0c551713e40277c55a6aa34fecf93fc68a27bf62797d47dc60613cd2a435b38(
    *,
    app_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d3c8dd924ad4994b9195afd966c18d0950398fb10f8078b91f2679d74e08117(
    *,
    elastic_load_balancer_attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__895cec226c11fff5e2501bf617655014b5c476842d77743c043755d94cf4902a(
    *,
    instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f515be01b79f66817a8720fdb1c48591d298d39dd85b86723b2cfa226000e98(
    *,
    layer_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2cc53fe8368ff29f02f3d4cfd0cd430b913740167ad005b9f6aeaf877419c17(
    *,
    stack_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07032bd286f2c6831af6600508d1b6611c89b34e96e91eb295766dbd00a81ba5(
    *,
    user_profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1d2a127f5d0d2cf3cb22749134f0f85e3e64120f84467645be864337323c6bf(
    *,
    volume_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAppRef, IElasticLoadBalancerAttachmentRef, IInstanceRef, ILayerRef, IStackRef, IUserProfileRef, IVolumeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
