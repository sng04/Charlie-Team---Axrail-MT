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
    jsii_type="aws-cdk-lib.interfaces.aws_globalaccelerator.AcceleratorReference",
    jsii_struct_bases=[],
    name_mapping={"accelerator_arn": "acceleratorArn"},
)
class AcceleratorReference:
    def __init__(self, *, accelerator_arn: builtins.str) -> None:
        '''A reference to a Accelerator resource.

        :param accelerator_arn: The AcceleratorArn of the Accelerator resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_globalaccelerator as interfaces_globalaccelerator
            
            accelerator_reference = interfaces_globalaccelerator.AcceleratorReference(
                accelerator_arn="acceleratorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4096400e288158796964a5ecfa0983a78b9501f6cd517f689063671b58923ce1)
            check_type(argname="argument accelerator_arn", value=accelerator_arn, expected_type=type_hints["accelerator_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "accelerator_arn": accelerator_arn,
        }

    @builtins.property
    def accelerator_arn(self) -> builtins.str:
        '''The AcceleratorArn of the Accelerator resource.'''
        result = self._values.get("accelerator_arn")
        assert result is not None, "Required property 'accelerator_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcceleratorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_globalaccelerator.CrossAccountAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"attachment_arn": "attachmentArn"},
)
class CrossAccountAttachmentReference:
    def __init__(self, *, attachment_arn: builtins.str) -> None:
        '''A reference to a CrossAccountAttachment resource.

        :param attachment_arn: The AttachmentArn of the CrossAccountAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_globalaccelerator as interfaces_globalaccelerator
            
            cross_account_attachment_reference = interfaces_globalaccelerator.CrossAccountAttachmentReference(
                attachment_arn="attachmentArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c41cc2cf3358d10c153b57747f11ab541c4be86d7c7dab98cb63d5e1379ff137)
            check_type(argname="argument attachment_arn", value=attachment_arn, expected_type=type_hints["attachment_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attachment_arn": attachment_arn,
        }

    @builtins.property
    def attachment_arn(self) -> builtins.str:
        '''The AttachmentArn of the CrossAccountAttachment resource.'''
        result = self._values.get("attachment_arn")
        assert result is not None, "Required property 'attachment_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CrossAccountAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_globalaccelerator.EndpointGroupReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_group_arn": "endpointGroupArn"},
)
class EndpointGroupReference:
    def __init__(self, *, endpoint_group_arn: builtins.str) -> None:
        '''A reference to a EndpointGroup resource.

        :param endpoint_group_arn: The EndpointGroupArn of the EndpointGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_globalaccelerator as interfaces_globalaccelerator
            
            endpoint_group_reference = interfaces_globalaccelerator.EndpointGroupReference(
                endpoint_group_arn="endpointGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b5b979b0b8410acbd43365f95043526af7b577eebd4f5201d643350b88abe9f)
            check_type(argname="argument endpoint_group_arn", value=endpoint_group_arn, expected_type=type_hints["endpoint_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_group_arn": endpoint_group_arn,
        }

    @builtins.property
    def endpoint_group_arn(self) -> builtins.str:
        '''The EndpointGroupArn of the EndpointGroup resource.'''
        result = self._values.get("endpoint_group_arn")
        assert result is not None, "Required property 'endpoint_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_globalaccelerator.IAcceleratorRef"
)
class IAcceleratorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Accelerator.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="acceleratorRef")
    def accelerator_ref(self) -> "AcceleratorReference":
        '''(experimental) A reference to a Accelerator resource.

        :stability: experimental
        '''
        ...


class _IAcceleratorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Accelerator.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_globalaccelerator.IAcceleratorRef"

    @builtins.property
    @jsii.member(jsii_name="acceleratorRef")
    def accelerator_ref(self) -> "AcceleratorReference":
        '''(experimental) A reference to a Accelerator resource.

        :stability: experimental
        '''
        return typing.cast("AcceleratorReference", jsii.get(self, "acceleratorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAcceleratorRef).__jsii_proxy_class__ = lambda : _IAcceleratorRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_globalaccelerator.ICrossAccountAttachmentRef"
)
class ICrossAccountAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CrossAccountAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="crossAccountAttachmentRef")
    def cross_account_attachment_ref(self) -> "CrossAccountAttachmentReference":
        '''(experimental) A reference to a CrossAccountAttachment resource.

        :stability: experimental
        '''
        ...


class _ICrossAccountAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CrossAccountAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_globalaccelerator.ICrossAccountAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="crossAccountAttachmentRef")
    def cross_account_attachment_ref(self) -> "CrossAccountAttachmentReference":
        '''(experimental) A reference to a CrossAccountAttachment resource.

        :stability: experimental
        '''
        return typing.cast("CrossAccountAttachmentReference", jsii.get(self, "crossAccountAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICrossAccountAttachmentRef).__jsii_proxy_class__ = lambda : _ICrossAccountAttachmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_globalaccelerator.IEndpointGroupRef"
)
class IEndpointGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EndpointGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointGroupRef")
    def endpoint_group_ref(self) -> "EndpointGroupReference":
        '''(experimental) A reference to a EndpointGroup resource.

        :stability: experimental
        '''
        ...


class _IEndpointGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EndpointGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_globalaccelerator.IEndpointGroupRef"

    @builtins.property
    @jsii.member(jsii_name="endpointGroupRef")
    def endpoint_group_ref(self) -> "EndpointGroupReference":
        '''(experimental) A reference to a EndpointGroup resource.

        :stability: experimental
        '''
        return typing.cast("EndpointGroupReference", jsii.get(self, "endpointGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointGroupRef).__jsii_proxy_class__ = lambda : _IEndpointGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_globalaccelerator.IListenerRef")
class IListenerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Listener.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="listenerRef")
    def listener_ref(self) -> "ListenerReference":
        '''(experimental) A reference to a Listener resource.

        :stability: experimental
        '''
        ...


class _IListenerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Listener.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_globalaccelerator.IListenerRef"

    @builtins.property
    @jsii.member(jsii_name="listenerRef")
    def listener_ref(self) -> "ListenerReference":
        '''(experimental) A reference to a Listener resource.

        :stability: experimental
        '''
        return typing.cast("ListenerReference", jsii.get(self, "listenerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IListenerRef).__jsii_proxy_class__ = lambda : _IListenerRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_globalaccelerator.ListenerReference",
    jsii_struct_bases=[],
    name_mapping={"listener_arn": "listenerArn"},
)
class ListenerReference:
    def __init__(self, *, listener_arn: builtins.str) -> None:
        '''A reference to a Listener resource.

        :param listener_arn: The ListenerArn of the Listener resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_globalaccelerator as interfaces_globalaccelerator
            
            listener_reference = interfaces_globalaccelerator.ListenerReference(
                listener_arn="listenerArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54494481df766234db9c29fb3f9de05ab9855fdbf1eef700fe27b6bd881ab606)
            check_type(argname="argument listener_arn", value=listener_arn, expected_type=type_hints["listener_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "listener_arn": listener_arn,
        }

    @builtins.property
    def listener_arn(self) -> builtins.str:
        '''The ListenerArn of the Listener resource.'''
        result = self._values.get("listener_arn")
        assert result is not None, "Required property 'listener_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListenerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AcceleratorReference",
    "CrossAccountAttachmentReference",
    "EndpointGroupReference",
    "IAcceleratorRef",
    "ICrossAccountAttachmentRef",
    "IEndpointGroupRef",
    "IListenerRef",
    "ListenerReference",
]

publication.publish()

def _typecheckingstub__4096400e288158796964a5ecfa0983a78b9501f6cd517f689063671b58923ce1(
    *,
    accelerator_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41cc2cf3358d10c153b57747f11ab541c4be86d7c7dab98cb63d5e1379ff137(
    *,
    attachment_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b5b979b0b8410acbd43365f95043526af7b577eebd4f5201d643350b88abe9f(
    *,
    endpoint_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54494481df766234db9c29fb3f9de05ab9855fdbf1eef700fe27b6bd881ab606(
    *,
    listener_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAcceleratorRef, ICrossAccountAttachmentRef, IEndpointGroupRef, IListenerRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
