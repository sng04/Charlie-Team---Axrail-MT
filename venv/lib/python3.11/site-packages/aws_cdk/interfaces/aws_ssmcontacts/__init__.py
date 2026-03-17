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
    jsii_type="aws-cdk-lib.interfaces.aws_ssmcontacts.ContactChannelReference",
    jsii_struct_bases=[],
    name_mapping={"contact_channel_arn": "contactChannelArn"},
)
class ContactChannelReference:
    def __init__(self, *, contact_channel_arn: builtins.str) -> None:
        '''A reference to a ContactChannel resource.

        :param contact_channel_arn: The Arn of the ContactChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssmcontacts as interfaces_ssmcontacts
            
            contact_channel_reference = interfaces_ssmcontacts.ContactChannelReference(
                contact_channel_arn="contactChannelArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa33296c3c3670cc59adac83c271120f59a697b64d7328af8dd7b7a5c9a3672a)
            check_type(argname="argument contact_channel_arn", value=contact_channel_arn, expected_type=type_hints["contact_channel_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_channel_arn": contact_channel_arn,
        }

    @builtins.property
    def contact_channel_arn(self) -> builtins.str:
        '''The Arn of the ContactChannel resource.'''
        result = self._values.get("contact_channel_arn")
        assert result is not None, "Required property 'contact_channel_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssmcontacts.ContactReference",
    jsii_struct_bases=[],
    name_mapping={"contact_arn": "contactArn"},
)
class ContactReference:
    def __init__(self, *, contact_arn: builtins.str) -> None:
        '''A reference to a Contact resource.

        :param contact_arn: The Arn of the Contact resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssmcontacts as interfaces_ssmcontacts
            
            contact_reference = interfaces_ssmcontacts.ContactReference(
                contact_arn="contactArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36216d76d7ce7b1898272e2065e78857ce44e7292b4fa42538900fc1bf4b8348)
            check_type(argname="argument contact_arn", value=contact_arn, expected_type=type_hints["contact_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_arn": contact_arn,
        }

    @builtins.property
    def contact_arn(self) -> builtins.str:
        '''The Arn of the Contact resource.'''
        result = self._values.get("contact_arn")
        assert result is not None, "Required property 'contact_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssmcontacts.IContactChannelRef")
class IContactChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContactChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="contactChannelRef")
    def contact_channel_ref(self) -> "ContactChannelReference":
        '''(experimental) A reference to a ContactChannel resource.

        :stability: experimental
        '''
        ...


class _IContactChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContactChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssmcontacts.IContactChannelRef"

    @builtins.property
    @jsii.member(jsii_name="contactChannelRef")
    def contact_channel_ref(self) -> "ContactChannelReference":
        '''(experimental) A reference to a ContactChannel resource.

        :stability: experimental
        '''
        return typing.cast("ContactChannelReference", jsii.get(self, "contactChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContactChannelRef).__jsii_proxy_class__ = lambda : _IContactChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssmcontacts.IContactRef")
class IContactRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Contact.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="contactRef")
    def contact_ref(self) -> "ContactReference":
        '''(experimental) A reference to a Contact resource.

        :stability: experimental
        '''
        ...


class _IContactRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Contact.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssmcontacts.IContactRef"

    @builtins.property
    @jsii.member(jsii_name="contactRef")
    def contact_ref(self) -> "ContactReference":
        '''(experimental) A reference to a Contact resource.

        :stability: experimental
        '''
        return typing.cast("ContactReference", jsii.get(self, "contactRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContactRef).__jsii_proxy_class__ = lambda : _IContactRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssmcontacts.IPlanRef")
class IPlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Plan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="planRef")
    def plan_ref(self) -> "PlanReference":
        '''(experimental) A reference to a Plan resource.

        :stability: experimental
        '''
        ...


class _IPlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Plan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssmcontacts.IPlanRef"

    @builtins.property
    @jsii.member(jsii_name="planRef")
    def plan_ref(self) -> "PlanReference":
        '''(experimental) A reference to a Plan resource.

        :stability: experimental
        '''
        return typing.cast("PlanReference", jsii.get(self, "planRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPlanRef).__jsii_proxy_class__ = lambda : _IPlanRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssmcontacts.IRotationRef")
class IRotationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Rotation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="rotationRef")
    def rotation_ref(self) -> "RotationReference":
        '''(experimental) A reference to a Rotation resource.

        :stability: experimental
        '''
        ...


class _IRotationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Rotation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssmcontacts.IRotationRef"

    @builtins.property
    @jsii.member(jsii_name="rotationRef")
    def rotation_ref(self) -> "RotationReference":
        '''(experimental) A reference to a Rotation resource.

        :stability: experimental
        '''
        return typing.cast("RotationReference", jsii.get(self, "rotationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRotationRef).__jsii_proxy_class__ = lambda : _IRotationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssmcontacts.PlanReference",
    jsii_struct_bases=[],
    name_mapping={"plan_arn": "planArn"},
)
class PlanReference:
    def __init__(self, *, plan_arn: builtins.str) -> None:
        '''A reference to a Plan resource.

        :param plan_arn: The Arn of the Plan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssmcontacts as interfaces_ssmcontacts
            
            plan_reference = interfaces_ssmcontacts.PlanReference(
                plan_arn="planArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae04ba0d8398024589495ed8155a06f04ac18d21bea51ef2b50e61a68f8d02f2)
            check_type(argname="argument plan_arn", value=plan_arn, expected_type=type_hints["plan_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "plan_arn": plan_arn,
        }

    @builtins.property
    def plan_arn(self) -> builtins.str:
        '''The Arn of the Plan resource.'''
        result = self._values.get("plan_arn")
        assert result is not None, "Required property 'plan_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssmcontacts.RotationReference",
    jsii_struct_bases=[],
    name_mapping={"rotation_arn": "rotationArn"},
)
class RotationReference:
    def __init__(self, *, rotation_arn: builtins.str) -> None:
        '''A reference to a Rotation resource.

        :param rotation_arn: The Arn of the Rotation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssmcontacts as interfaces_ssmcontacts
            
            rotation_reference = interfaces_ssmcontacts.RotationReference(
                rotation_arn="rotationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16e671ce46f69cea0af715fd68a8feeebd2d94dc6541bbe8081404a485dbcc54)
            check_type(argname="argument rotation_arn", value=rotation_arn, expected_type=type_hints["rotation_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rotation_arn": rotation_arn,
        }

    @builtins.property
    def rotation_arn(self) -> builtins.str:
        '''The Arn of the Rotation resource.'''
        result = self._values.get("rotation_arn")
        assert result is not None, "Required property 'rotation_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RotationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ContactChannelReference",
    "ContactReference",
    "IContactChannelRef",
    "IContactRef",
    "IPlanRef",
    "IRotationRef",
    "PlanReference",
    "RotationReference",
]

publication.publish()

def _typecheckingstub__aa33296c3c3670cc59adac83c271120f59a697b64d7328af8dd7b7a5c9a3672a(
    *,
    contact_channel_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36216d76d7ce7b1898272e2065e78857ce44e7292b4fa42538900fc1bf4b8348(
    *,
    contact_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae04ba0d8398024589495ed8155a06f04ac18d21bea51ef2b50e61a68f8d02f2(
    *,
    plan_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e671ce46f69cea0af715fd68a8feeebd2d94dc6541bbe8081404a485dbcc54(
    *,
    rotation_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IContactChannelRef, IContactRef, IPlanRef, IRotationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
