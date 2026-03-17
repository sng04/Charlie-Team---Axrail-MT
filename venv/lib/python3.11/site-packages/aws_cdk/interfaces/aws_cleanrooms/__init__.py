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
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.AnalysisTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "analysis_template_arn": "analysisTemplateArn",
        "analysis_template_identifier": "analysisTemplateIdentifier",
        "membership_identifier": "membershipIdentifier",
    },
)
class AnalysisTemplateReference:
    def __init__(
        self,
        *,
        analysis_template_arn: builtins.str,
        analysis_template_identifier: builtins.str,
        membership_identifier: builtins.str,
    ) -> None:
        '''A reference to a AnalysisTemplate resource.

        :param analysis_template_arn: The ARN of the AnalysisTemplate resource.
        :param analysis_template_identifier: The AnalysisTemplateIdentifier of the AnalysisTemplate resource.
        :param membership_identifier: The MembershipIdentifier of the AnalysisTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cleanrooms as interfaces_cleanrooms
            
            analysis_template_reference = interfaces_cleanrooms.AnalysisTemplateReference(
                analysis_template_arn="analysisTemplateArn",
                analysis_template_identifier="analysisTemplateIdentifier",
                membership_identifier="membershipIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82262301cdf0bbec4ee6c64d3d1c4636580c3f4855c65bb4aa4549915937fa46)
            check_type(argname="argument analysis_template_arn", value=analysis_template_arn, expected_type=type_hints["analysis_template_arn"])
            check_type(argname="argument analysis_template_identifier", value=analysis_template_identifier, expected_type=type_hints["analysis_template_identifier"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "analysis_template_arn": analysis_template_arn,
            "analysis_template_identifier": analysis_template_identifier,
            "membership_identifier": membership_identifier,
        }

    @builtins.property
    def analysis_template_arn(self) -> builtins.str:
        '''The ARN of the AnalysisTemplate resource.'''
        result = self._values.get("analysis_template_arn")
        assert result is not None, "Required property 'analysis_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def analysis_template_identifier(self) -> builtins.str:
        '''The AnalysisTemplateIdentifier of the AnalysisTemplate resource.'''
        result = self._values.get("analysis_template_identifier")
        assert result is not None, "Required property 'analysis_template_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The MembershipIdentifier of the AnalysisTemplate resource.'''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnalysisTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.CollaborationReference",
    jsii_struct_bases=[],
    name_mapping={
        "collaboration_arn": "collaborationArn",
        "collaboration_identifier": "collaborationIdentifier",
    },
)
class CollaborationReference:
    def __init__(
        self,
        *,
        collaboration_arn: builtins.str,
        collaboration_identifier: builtins.str,
    ) -> None:
        '''A reference to a Collaboration resource.

        :param collaboration_arn: The ARN of the Collaboration resource.
        :param collaboration_identifier: The CollaborationIdentifier of the Collaboration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cleanrooms as interfaces_cleanrooms
            
            collaboration_reference = interfaces_cleanrooms.CollaborationReference(
                collaboration_arn="collaborationArn",
                collaboration_identifier="collaborationIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c1e204d44c90efcfa75ee975debd1fc2527ded04aae94fe16212aed2b830156)
            check_type(argname="argument collaboration_arn", value=collaboration_arn, expected_type=type_hints["collaboration_arn"])
            check_type(argname="argument collaboration_identifier", value=collaboration_identifier, expected_type=type_hints["collaboration_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collaboration_arn": collaboration_arn,
            "collaboration_identifier": collaboration_identifier,
        }

    @builtins.property
    def collaboration_arn(self) -> builtins.str:
        '''The ARN of the Collaboration resource.'''
        result = self._values.get("collaboration_arn")
        assert result is not None, "Required property 'collaboration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def collaboration_identifier(self) -> builtins.str:
        '''The CollaborationIdentifier of the Collaboration resource.'''
        result = self._values.get("collaboration_identifier")
        assert result is not None, "Required property 'collaboration_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CollaborationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.ConfiguredTableAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "configured_table_association_arn": "configuredTableAssociationArn",
        "configured_table_association_identifier": "configuredTableAssociationIdentifier",
        "membership_identifier": "membershipIdentifier",
    },
)
class ConfiguredTableAssociationReference:
    def __init__(
        self,
        *,
        configured_table_association_arn: builtins.str,
        configured_table_association_identifier: builtins.str,
        membership_identifier: builtins.str,
    ) -> None:
        '''A reference to a ConfiguredTableAssociation resource.

        :param configured_table_association_arn: The ARN of the ConfiguredTableAssociation resource.
        :param configured_table_association_identifier: The ConfiguredTableAssociationIdentifier of the ConfiguredTableAssociation resource.
        :param membership_identifier: The MembershipIdentifier of the ConfiguredTableAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cleanrooms as interfaces_cleanrooms
            
            configured_table_association_reference = interfaces_cleanrooms.ConfiguredTableAssociationReference(
                configured_table_association_arn="configuredTableAssociationArn",
                configured_table_association_identifier="configuredTableAssociationIdentifier",
                membership_identifier="membershipIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb6b5f3976ac912f7e0044ebf055c0bf7fc4280c37182d2f2e107ea44653b3b)
            check_type(argname="argument configured_table_association_arn", value=configured_table_association_arn, expected_type=type_hints["configured_table_association_arn"])
            check_type(argname="argument configured_table_association_identifier", value=configured_table_association_identifier, expected_type=type_hints["configured_table_association_identifier"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configured_table_association_arn": configured_table_association_arn,
            "configured_table_association_identifier": configured_table_association_identifier,
            "membership_identifier": membership_identifier,
        }

    @builtins.property
    def configured_table_association_arn(self) -> builtins.str:
        '''The ARN of the ConfiguredTableAssociation resource.'''
        result = self._values.get("configured_table_association_arn")
        assert result is not None, "Required property 'configured_table_association_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configured_table_association_identifier(self) -> builtins.str:
        '''The ConfiguredTableAssociationIdentifier of the ConfiguredTableAssociation resource.'''
        result = self._values.get("configured_table_association_identifier")
        assert result is not None, "Required property 'configured_table_association_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The MembershipIdentifier of the ConfiguredTableAssociation resource.'''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfiguredTableAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.ConfiguredTableReference",
    jsii_struct_bases=[],
    name_mapping={
        "configured_table_arn": "configuredTableArn",
        "configured_table_identifier": "configuredTableIdentifier",
    },
)
class ConfiguredTableReference:
    def __init__(
        self,
        *,
        configured_table_arn: builtins.str,
        configured_table_identifier: builtins.str,
    ) -> None:
        '''A reference to a ConfiguredTable resource.

        :param configured_table_arn: The ARN of the ConfiguredTable resource.
        :param configured_table_identifier: The ConfiguredTableIdentifier of the ConfiguredTable resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cleanrooms as interfaces_cleanrooms
            
            configured_table_reference = interfaces_cleanrooms.ConfiguredTableReference(
                configured_table_arn="configuredTableArn",
                configured_table_identifier="configuredTableIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2eb940a6e391d655e24371337fb5f835fac23d7409de80e5ada08fbca1ae31f2)
            check_type(argname="argument configured_table_arn", value=configured_table_arn, expected_type=type_hints["configured_table_arn"])
            check_type(argname="argument configured_table_identifier", value=configured_table_identifier, expected_type=type_hints["configured_table_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configured_table_arn": configured_table_arn,
            "configured_table_identifier": configured_table_identifier,
        }

    @builtins.property
    def configured_table_arn(self) -> builtins.str:
        '''The ARN of the ConfiguredTable resource.'''
        result = self._values.get("configured_table_arn")
        assert result is not None, "Required property 'configured_table_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configured_table_identifier(self) -> builtins.str:
        '''The ConfiguredTableIdentifier of the ConfiguredTable resource.'''
        result = self._values.get("configured_table_identifier")
        assert result is not None, "Required property 'configured_table_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfiguredTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.IAnalysisTemplateRef")
class IAnalysisTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AnalysisTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="analysisTemplateRef")
    def analysis_template_ref(self) -> "AnalysisTemplateReference":
        '''(experimental) A reference to a AnalysisTemplate resource.

        :stability: experimental
        '''
        ...


class _IAnalysisTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AnalysisTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cleanrooms.IAnalysisTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="analysisTemplateRef")
    def analysis_template_ref(self) -> "AnalysisTemplateReference":
        '''(experimental) A reference to a AnalysisTemplate resource.

        :stability: experimental
        '''
        return typing.cast("AnalysisTemplateReference", jsii.get(self, "analysisTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnalysisTemplateRef).__jsii_proxy_class__ = lambda : _IAnalysisTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.ICollaborationRef")
class ICollaborationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Collaboration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="collaborationRef")
    def collaboration_ref(self) -> "CollaborationReference":
        '''(experimental) A reference to a Collaboration resource.

        :stability: experimental
        '''
        ...


class _ICollaborationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Collaboration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cleanrooms.ICollaborationRef"

    @builtins.property
    @jsii.member(jsii_name="collaborationRef")
    def collaboration_ref(self) -> "CollaborationReference":
        '''(experimental) A reference to a Collaboration resource.

        :stability: experimental
        '''
        return typing.cast("CollaborationReference", jsii.get(self, "collaborationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICollaborationRef).__jsii_proxy_class__ = lambda : _ICollaborationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.IConfiguredTableAssociationRef"
)
class IConfiguredTableAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfiguredTableAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configuredTableAssociationRef")
    def configured_table_association_ref(self) -> "ConfiguredTableAssociationReference":
        '''(experimental) A reference to a ConfiguredTableAssociation resource.

        :stability: experimental
        '''
        ...


class _IConfiguredTableAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfiguredTableAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cleanrooms.IConfiguredTableAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="configuredTableAssociationRef")
    def configured_table_association_ref(self) -> "ConfiguredTableAssociationReference":
        '''(experimental) A reference to a ConfiguredTableAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ConfiguredTableAssociationReference", jsii.get(self, "configuredTableAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfiguredTableAssociationRef).__jsii_proxy_class__ = lambda : _IConfiguredTableAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.IConfiguredTableRef")
class IConfiguredTableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfiguredTable.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configuredTableRef")
    def configured_table_ref(self) -> "ConfiguredTableReference":
        '''(experimental) A reference to a ConfiguredTable resource.

        :stability: experimental
        '''
        ...


class _IConfiguredTableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfiguredTable.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cleanrooms.IConfiguredTableRef"

    @builtins.property
    @jsii.member(jsii_name="configuredTableRef")
    def configured_table_ref(self) -> "ConfiguredTableReference":
        '''(experimental) A reference to a ConfiguredTable resource.

        :stability: experimental
        '''
        return typing.cast("ConfiguredTableReference", jsii.get(self, "configuredTableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfiguredTableRef).__jsii_proxy_class__ = lambda : _IConfiguredTableRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.IIdMappingTableRef")
class IIdMappingTableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdMappingTable.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="idMappingTableRef")
    def id_mapping_table_ref(self) -> "IdMappingTableReference":
        '''(experimental) A reference to a IdMappingTable resource.

        :stability: experimental
        '''
        ...


class _IIdMappingTableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdMappingTable.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cleanrooms.IIdMappingTableRef"

    @builtins.property
    @jsii.member(jsii_name="idMappingTableRef")
    def id_mapping_table_ref(self) -> "IdMappingTableReference":
        '''(experimental) A reference to a IdMappingTable resource.

        :stability: experimental
        '''
        return typing.cast("IdMappingTableReference", jsii.get(self, "idMappingTableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdMappingTableRef).__jsii_proxy_class__ = lambda : _IIdMappingTableRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.IIdNamespaceAssociationRef"
)
class IIdNamespaceAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdNamespaceAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="idNamespaceAssociationRef")
    def id_namespace_association_ref(self) -> "IdNamespaceAssociationReference":
        '''(experimental) A reference to a IdNamespaceAssociation resource.

        :stability: experimental
        '''
        ...


class _IIdNamespaceAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdNamespaceAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cleanrooms.IIdNamespaceAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="idNamespaceAssociationRef")
    def id_namespace_association_ref(self) -> "IdNamespaceAssociationReference":
        '''(experimental) A reference to a IdNamespaceAssociation resource.

        :stability: experimental
        '''
        return typing.cast("IdNamespaceAssociationReference", jsii.get(self, "idNamespaceAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdNamespaceAssociationRef).__jsii_proxy_class__ = lambda : _IIdNamespaceAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.IMembershipRef")
class IMembershipRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Membership.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="membershipRef")
    def membership_ref(self) -> "MembershipReference":
        '''(experimental) A reference to a Membership resource.

        :stability: experimental
        '''
        ...


class _IMembershipRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Membership.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cleanrooms.IMembershipRef"

    @builtins.property
    @jsii.member(jsii_name="membershipRef")
    def membership_ref(self) -> "MembershipReference":
        '''(experimental) A reference to a Membership resource.

        :stability: experimental
        '''
        return typing.cast("MembershipReference", jsii.get(self, "membershipRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMembershipRef).__jsii_proxy_class__ = lambda : _IMembershipRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.IPrivacyBudgetTemplateRef"
)
class IPrivacyBudgetTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PrivacyBudgetTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="privacyBudgetTemplateRef")
    def privacy_budget_template_ref(self) -> "PrivacyBudgetTemplateReference":
        '''(experimental) A reference to a PrivacyBudgetTemplate resource.

        :stability: experimental
        '''
        ...


class _IPrivacyBudgetTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PrivacyBudgetTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cleanrooms.IPrivacyBudgetTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="privacyBudgetTemplateRef")
    def privacy_budget_template_ref(self) -> "PrivacyBudgetTemplateReference":
        '''(experimental) A reference to a PrivacyBudgetTemplate resource.

        :stability: experimental
        '''
        return typing.cast("PrivacyBudgetTemplateReference", jsii.get(self, "privacyBudgetTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrivacyBudgetTemplateRef).__jsii_proxy_class__ = lambda : _IPrivacyBudgetTemplateRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.IdMappingTableReference",
    jsii_struct_bases=[],
    name_mapping={
        "id_mapping_table_arn": "idMappingTableArn",
        "id_mapping_table_identifier": "idMappingTableIdentifier",
        "membership_identifier": "membershipIdentifier",
    },
)
class IdMappingTableReference:
    def __init__(
        self,
        *,
        id_mapping_table_arn: builtins.str,
        id_mapping_table_identifier: builtins.str,
        membership_identifier: builtins.str,
    ) -> None:
        '''A reference to a IdMappingTable resource.

        :param id_mapping_table_arn: The ARN of the IdMappingTable resource.
        :param id_mapping_table_identifier: The IdMappingTableIdentifier of the IdMappingTable resource.
        :param membership_identifier: The MembershipIdentifier of the IdMappingTable resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cleanrooms as interfaces_cleanrooms
            
            id_mapping_table_reference = interfaces_cleanrooms.IdMappingTableReference(
                id_mapping_table_arn="idMappingTableArn",
                id_mapping_table_identifier="idMappingTableIdentifier",
                membership_identifier="membershipIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c1f6ada073baa9d8e9b0d83eb33c662ccac937bc72755fe07773e7c3cfd218)
            check_type(argname="argument id_mapping_table_arn", value=id_mapping_table_arn, expected_type=type_hints["id_mapping_table_arn"])
            check_type(argname="argument id_mapping_table_identifier", value=id_mapping_table_identifier, expected_type=type_hints["id_mapping_table_identifier"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id_mapping_table_arn": id_mapping_table_arn,
            "id_mapping_table_identifier": id_mapping_table_identifier,
            "membership_identifier": membership_identifier,
        }

    @builtins.property
    def id_mapping_table_arn(self) -> builtins.str:
        '''The ARN of the IdMappingTable resource.'''
        result = self._values.get("id_mapping_table_arn")
        assert result is not None, "Required property 'id_mapping_table_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id_mapping_table_identifier(self) -> builtins.str:
        '''The IdMappingTableIdentifier of the IdMappingTable resource.'''
        result = self._values.get("id_mapping_table_identifier")
        assert result is not None, "Required property 'id_mapping_table_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The MembershipIdentifier of the IdMappingTable resource.'''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdMappingTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.IdNamespaceAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "id_namespace_association_arn": "idNamespaceAssociationArn",
        "id_namespace_association_identifier": "idNamespaceAssociationIdentifier",
        "membership_identifier": "membershipIdentifier",
    },
)
class IdNamespaceAssociationReference:
    def __init__(
        self,
        *,
        id_namespace_association_arn: builtins.str,
        id_namespace_association_identifier: builtins.str,
        membership_identifier: builtins.str,
    ) -> None:
        '''A reference to a IdNamespaceAssociation resource.

        :param id_namespace_association_arn: The ARN of the IdNamespaceAssociation resource.
        :param id_namespace_association_identifier: The IdNamespaceAssociationIdentifier of the IdNamespaceAssociation resource.
        :param membership_identifier: The MembershipIdentifier of the IdNamespaceAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cleanrooms as interfaces_cleanrooms
            
            id_namespace_association_reference = interfaces_cleanrooms.IdNamespaceAssociationReference(
                id_namespace_association_arn="idNamespaceAssociationArn",
                id_namespace_association_identifier="idNamespaceAssociationIdentifier",
                membership_identifier="membershipIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e5c51d77a9254a26baaaef48d6f7fef6cb7bb514ba0928032c6f95ebdbc7859)
            check_type(argname="argument id_namespace_association_arn", value=id_namespace_association_arn, expected_type=type_hints["id_namespace_association_arn"])
            check_type(argname="argument id_namespace_association_identifier", value=id_namespace_association_identifier, expected_type=type_hints["id_namespace_association_identifier"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id_namespace_association_arn": id_namespace_association_arn,
            "id_namespace_association_identifier": id_namespace_association_identifier,
            "membership_identifier": membership_identifier,
        }

    @builtins.property
    def id_namespace_association_arn(self) -> builtins.str:
        '''The ARN of the IdNamespaceAssociation resource.'''
        result = self._values.get("id_namespace_association_arn")
        assert result is not None, "Required property 'id_namespace_association_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id_namespace_association_identifier(self) -> builtins.str:
        '''The IdNamespaceAssociationIdentifier of the IdNamespaceAssociation resource.'''
        result = self._values.get("id_namespace_association_identifier")
        assert result is not None, "Required property 'id_namespace_association_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The MembershipIdentifier of the IdNamespaceAssociation resource.'''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdNamespaceAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.MembershipReference",
    jsii_struct_bases=[],
    name_mapping={
        "membership_arn": "membershipArn",
        "membership_identifier": "membershipIdentifier",
    },
)
class MembershipReference:
    def __init__(
        self,
        *,
        membership_arn: builtins.str,
        membership_identifier: builtins.str,
    ) -> None:
        '''A reference to a Membership resource.

        :param membership_arn: The ARN of the Membership resource.
        :param membership_identifier: The MembershipIdentifier of the Membership resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cleanrooms as interfaces_cleanrooms
            
            membership_reference = interfaces_cleanrooms.MembershipReference(
                membership_arn="membershipArn",
                membership_identifier="membershipIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d5a8a067b5206625d9650c35900d7f89d583beb5413a3ec0462e084a2ebdc9b)
            check_type(argname="argument membership_arn", value=membership_arn, expected_type=type_hints["membership_arn"])
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "membership_arn": membership_arn,
            "membership_identifier": membership_identifier,
        }

    @builtins.property
    def membership_arn(self) -> builtins.str:
        '''The ARN of the Membership resource.'''
        result = self._values.get("membership_arn")
        assert result is not None, "Required property 'membership_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The MembershipIdentifier of the Membership resource.'''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MembershipReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cleanrooms.PrivacyBudgetTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "membership_identifier": "membershipIdentifier",
        "privacy_budget_template_arn": "privacyBudgetTemplateArn",
        "privacy_budget_template_identifier": "privacyBudgetTemplateIdentifier",
    },
)
class PrivacyBudgetTemplateReference:
    def __init__(
        self,
        *,
        membership_identifier: builtins.str,
        privacy_budget_template_arn: builtins.str,
        privacy_budget_template_identifier: builtins.str,
    ) -> None:
        '''A reference to a PrivacyBudgetTemplate resource.

        :param membership_identifier: The MembershipIdentifier of the PrivacyBudgetTemplate resource.
        :param privacy_budget_template_arn: The ARN of the PrivacyBudgetTemplate resource.
        :param privacy_budget_template_identifier: The PrivacyBudgetTemplateIdentifier of the PrivacyBudgetTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cleanrooms as interfaces_cleanrooms
            
            privacy_budget_template_reference = interfaces_cleanrooms.PrivacyBudgetTemplateReference(
                membership_identifier="membershipIdentifier",
                privacy_budget_template_arn="privacyBudgetTemplateArn",
                privacy_budget_template_identifier="privacyBudgetTemplateIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75fffac054bd44cf4a1c25f9dbb25317dfa83275ae8e640fdbc8383809bcf89a)
            check_type(argname="argument membership_identifier", value=membership_identifier, expected_type=type_hints["membership_identifier"])
            check_type(argname="argument privacy_budget_template_arn", value=privacy_budget_template_arn, expected_type=type_hints["privacy_budget_template_arn"])
            check_type(argname="argument privacy_budget_template_identifier", value=privacy_budget_template_identifier, expected_type=type_hints["privacy_budget_template_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "membership_identifier": membership_identifier,
            "privacy_budget_template_arn": privacy_budget_template_arn,
            "privacy_budget_template_identifier": privacy_budget_template_identifier,
        }

    @builtins.property
    def membership_identifier(self) -> builtins.str:
        '''The MembershipIdentifier of the PrivacyBudgetTemplate resource.'''
        result = self._values.get("membership_identifier")
        assert result is not None, "Required property 'membership_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def privacy_budget_template_arn(self) -> builtins.str:
        '''The ARN of the PrivacyBudgetTemplate resource.'''
        result = self._values.get("privacy_budget_template_arn")
        assert result is not None, "Required property 'privacy_budget_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def privacy_budget_template_identifier(self) -> builtins.str:
        '''The PrivacyBudgetTemplateIdentifier of the PrivacyBudgetTemplate resource.'''
        result = self._values.get("privacy_budget_template_identifier")
        assert result is not None, "Required property 'privacy_budget_template_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivacyBudgetTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AnalysisTemplateReference",
    "CollaborationReference",
    "ConfiguredTableAssociationReference",
    "ConfiguredTableReference",
    "IAnalysisTemplateRef",
    "ICollaborationRef",
    "IConfiguredTableAssociationRef",
    "IConfiguredTableRef",
    "IIdMappingTableRef",
    "IIdNamespaceAssociationRef",
    "IMembershipRef",
    "IPrivacyBudgetTemplateRef",
    "IdMappingTableReference",
    "IdNamespaceAssociationReference",
    "MembershipReference",
    "PrivacyBudgetTemplateReference",
]

publication.publish()

def _typecheckingstub__82262301cdf0bbec4ee6c64d3d1c4636580c3f4855c65bb4aa4549915937fa46(
    *,
    analysis_template_arn: builtins.str,
    analysis_template_identifier: builtins.str,
    membership_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c1e204d44c90efcfa75ee975debd1fc2527ded04aae94fe16212aed2b830156(
    *,
    collaboration_arn: builtins.str,
    collaboration_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb6b5f3976ac912f7e0044ebf055c0bf7fc4280c37182d2f2e107ea44653b3b(
    *,
    configured_table_association_arn: builtins.str,
    configured_table_association_identifier: builtins.str,
    membership_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2eb940a6e391d655e24371337fb5f835fac23d7409de80e5ada08fbca1ae31f2(
    *,
    configured_table_arn: builtins.str,
    configured_table_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c1f6ada073baa9d8e9b0d83eb33c662ccac937bc72755fe07773e7c3cfd218(
    *,
    id_mapping_table_arn: builtins.str,
    id_mapping_table_identifier: builtins.str,
    membership_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5c51d77a9254a26baaaef48d6f7fef6cb7bb514ba0928032c6f95ebdbc7859(
    *,
    id_namespace_association_arn: builtins.str,
    id_namespace_association_identifier: builtins.str,
    membership_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d5a8a067b5206625d9650c35900d7f89d583beb5413a3ec0462e084a2ebdc9b(
    *,
    membership_arn: builtins.str,
    membership_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75fffac054bd44cf4a1c25f9dbb25317dfa83275ae8e640fdbc8383809bcf89a(
    *,
    membership_identifier: builtins.str,
    privacy_budget_template_arn: builtins.str,
    privacy_budget_template_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAnalysisTemplateRef, ICollaborationRef, IConfiguredTableAssociationRef, IConfiguredTableRef, IIdMappingTableRef, IIdNamespaceAssociationRef, IMembershipRef, IPrivacyBudgetTemplateRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
