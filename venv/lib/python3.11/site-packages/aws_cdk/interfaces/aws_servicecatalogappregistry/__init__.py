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
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalogappregistry.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_arn": "applicationArn",
        "application_id": "applicationId",
    },
)
class ApplicationReference:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        application_id: builtins.str,
    ) -> None:
        '''A reference to a Application resource.

        :param application_arn: The ARN of the Application resource.
        :param application_id: The Id of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalogappregistry as interfaces_servicecatalogappregistry
            
            application_reference = interfaces_servicecatalogappregistry.ApplicationReference(
                application_arn="applicationArn",
                application_id="applicationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9833364a975dcb14d2d5af11f8e89141c5dc8331ad7ffd6a87b41482eeca4824)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "application_id": application_id,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ARN of the Application resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The Id of the Application resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalogappregistry.AttributeGroupAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_arn": "applicationArn",
        "attribute_group_arn": "attributeGroupArn",
    },
)
class AttributeGroupAssociationReference:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        attribute_group_arn: builtins.str,
    ) -> None:
        '''A reference to a AttributeGroupAssociation resource.

        :param application_arn: The ApplicationArn of the AttributeGroupAssociation resource.
        :param attribute_group_arn: The AttributeGroupArn of the AttributeGroupAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalogappregistry as interfaces_servicecatalogappregistry
            
            attribute_group_association_reference = interfaces_servicecatalogappregistry.AttributeGroupAssociationReference(
                application_arn="applicationArn",
                attribute_group_arn="attributeGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2863fa3269af7342cd65d5ac0c219cba80d985946bd7cdcd449b74848eb3d5f3)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument attribute_group_arn", value=attribute_group_arn, expected_type=type_hints["attribute_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "attribute_group_arn": attribute_group_arn,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ApplicationArn of the AttributeGroupAssociation resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute_group_arn(self) -> builtins.str:
        '''The AttributeGroupArn of the AttributeGroupAssociation resource.'''
        result = self._values.get("attribute_group_arn")
        assert result is not None, "Required property 'attribute_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AttributeGroupAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalogappregistry.AttributeGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_group_arn": "attributeGroupArn",
        "attribute_group_id": "attributeGroupId",
    },
)
class AttributeGroupReference:
    def __init__(
        self,
        *,
        attribute_group_arn: builtins.str,
        attribute_group_id: builtins.str,
    ) -> None:
        '''A reference to a AttributeGroup resource.

        :param attribute_group_arn: The ARN of the AttributeGroup resource.
        :param attribute_group_id: The Id of the AttributeGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalogappregistry as interfaces_servicecatalogappregistry
            
            attribute_group_reference = interfaces_servicecatalogappregistry.AttributeGroupReference(
                attribute_group_arn="attributeGroupArn",
                attribute_group_id="attributeGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd783e1278bd474dda8fc054df65d1662f8b175eadcd05e0b4dd161f2ba8ee13)
            check_type(argname="argument attribute_group_arn", value=attribute_group_arn, expected_type=type_hints["attribute_group_arn"])
            check_type(argname="argument attribute_group_id", value=attribute_group_id, expected_type=type_hints["attribute_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attribute_group_arn": attribute_group_arn,
            "attribute_group_id": attribute_group_id,
        }

    @builtins.property
    def attribute_group_arn(self) -> builtins.str:
        '''The ARN of the AttributeGroup resource.'''
        result = self._values.get("attribute_group_arn")
        assert result is not None, "Required property 'attribute_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attribute_group_id(self) -> builtins.str:
        '''The Id of the AttributeGroup resource.'''
        result = self._values.get("attribute_group_id")
        assert result is not None, "Required property 'attribute_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AttributeGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalogappregistry.IApplicationRef"
)
class IApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        ...


class _IApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalogappregistry.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalogappregistry.IAttributeGroupAssociationRef"
)
class IAttributeGroupAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AttributeGroupAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="attributeGroupAssociationRef")
    def attribute_group_association_ref(self) -> "AttributeGroupAssociationReference":
        '''(experimental) A reference to a AttributeGroupAssociation resource.

        :stability: experimental
        '''
        ...


class _IAttributeGroupAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AttributeGroupAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalogappregistry.IAttributeGroupAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="attributeGroupAssociationRef")
    def attribute_group_association_ref(self) -> "AttributeGroupAssociationReference":
        '''(experimental) A reference to a AttributeGroupAssociation resource.

        :stability: experimental
        '''
        return typing.cast("AttributeGroupAssociationReference", jsii.get(self, "attributeGroupAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAttributeGroupAssociationRef).__jsii_proxy_class__ = lambda : _IAttributeGroupAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalogappregistry.IAttributeGroupRef"
)
class IAttributeGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AttributeGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="attributeGroupRef")
    def attribute_group_ref(self) -> "AttributeGroupReference":
        '''(experimental) A reference to a AttributeGroup resource.

        :stability: experimental
        '''
        ...


class _IAttributeGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AttributeGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalogappregistry.IAttributeGroupRef"

    @builtins.property
    @jsii.member(jsii_name="attributeGroupRef")
    def attribute_group_ref(self) -> "AttributeGroupReference":
        '''(experimental) A reference to a AttributeGroup resource.

        :stability: experimental
        '''
        return typing.cast("AttributeGroupReference", jsii.get(self, "attributeGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAttributeGroupRef).__jsii_proxy_class__ = lambda : _IAttributeGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalogappregistry.IResourceAssociationRef"
)
class IResourceAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceAssociationRef")
    def resource_association_ref(self) -> "ResourceAssociationReference":
        '''(experimental) A reference to a ResourceAssociation resource.

        :stability: experimental
        '''
        ...


class _IResourceAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalogappregistry.IResourceAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="resourceAssociationRef")
    def resource_association_ref(self) -> "ResourceAssociationReference":
        '''(experimental) A reference to a ResourceAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ResourceAssociationReference", jsii.get(self, "resourceAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceAssociationRef).__jsii_proxy_class__ = lambda : _IResourceAssociationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalogappregistry.ResourceAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_arn": "applicationArn",
        "resource_arn": "resourceArn",
        "resource_type": "resourceType",
    },
)
class ResourceAssociationReference:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        resource_arn: builtins.str,
        resource_type: builtins.str,
    ) -> None:
        '''A reference to a ResourceAssociation resource.

        :param application_arn: The ApplicationArn of the ResourceAssociation resource.
        :param resource_arn: The ResourceArn of the ResourceAssociation resource.
        :param resource_type: The ResourceType of the ResourceAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalogappregistry as interfaces_servicecatalogappregistry
            
            resource_association_reference = interfaces_servicecatalogappregistry.ResourceAssociationReference(
                application_arn="applicationArn",
                resource_arn="resourceArn",
                resource_type="resourceType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__968cb785b25d864fc0f5b494088e92b6ff37bf6801c5e0512c12e9dc24bf5010)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "resource_arn": resource_arn,
            "resource_type": resource_type,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ApplicationArn of the ResourceAssociation resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the ResourceAssociation resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''The ResourceType of the ResourceAssociation resource.'''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApplicationReference",
    "AttributeGroupAssociationReference",
    "AttributeGroupReference",
    "IApplicationRef",
    "IAttributeGroupAssociationRef",
    "IAttributeGroupRef",
    "IResourceAssociationRef",
    "ResourceAssociationReference",
]

publication.publish()

def _typecheckingstub__9833364a975dcb14d2d5af11f8e89141c5dc8331ad7ffd6a87b41482eeca4824(
    *,
    application_arn: builtins.str,
    application_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2863fa3269af7342cd65d5ac0c219cba80d985946bd7cdcd449b74848eb3d5f3(
    *,
    application_arn: builtins.str,
    attribute_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd783e1278bd474dda8fc054df65d1662f8b175eadcd05e0b4dd161f2ba8ee13(
    *,
    attribute_group_arn: builtins.str,
    attribute_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__968cb785b25d864fc0f5b494088e92b6ff37bf6801c5e0512c12e9dc24bf5010(
    *,
    application_arn: builtins.str,
    resource_arn: builtins.str,
    resource_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IAttributeGroupAssociationRef, IAttributeGroupRef, IResourceAssociationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
