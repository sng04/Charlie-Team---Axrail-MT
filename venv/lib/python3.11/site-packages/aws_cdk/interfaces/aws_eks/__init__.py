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
    jsii_type="aws-cdk-lib.interfaces.aws_eks.AccessEntryReference",
    jsii_struct_bases=[],
    name_mapping={
        "access_entry_arn": "accessEntryArn",
        "cluster_name": "clusterName",
        "principal_arn": "principalArn",
    },
)
class AccessEntryReference:
    def __init__(
        self,
        *,
        access_entry_arn: builtins.str,
        cluster_name: builtins.str,
        principal_arn: builtins.str,
    ) -> None:
        '''A reference to a AccessEntry resource.

        :param access_entry_arn: The ARN of the AccessEntry resource.
        :param cluster_name: The ClusterName of the AccessEntry resource.
        :param principal_arn: The PrincipalArn of the AccessEntry resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eks as interfaces_eks
            
            access_entry_reference = interfaces_eks.AccessEntryReference(
                access_entry_arn="accessEntryArn",
                cluster_name="clusterName",
                principal_arn="principalArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70a5e484db113b4d5529dd453bcc42197c4a3a2f2574700dceec0ec68d28ea53)
            check_type(argname="argument access_entry_arn", value=access_entry_arn, expected_type=type_hints["access_entry_arn"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument principal_arn", value=principal_arn, expected_type=type_hints["principal_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_entry_arn": access_entry_arn,
            "cluster_name": cluster_name,
            "principal_arn": principal_arn,
        }

    @builtins.property
    def access_entry_arn(self) -> builtins.str:
        '''The ARN of the AccessEntry resource.'''
        result = self._values.get("access_entry_arn")
        assert result is not None, "Required property 'access_entry_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The ClusterName of the AccessEntry resource.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_arn(self) -> builtins.str:
        '''The PrincipalArn of the AccessEntry resource.'''
        result = self._values.get("principal_arn")
        assert result is not None, "Required property 'principal_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessEntryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eks.AddonReference",
    jsii_struct_bases=[],
    name_mapping={
        "addon_arn": "addonArn",
        "addon_name": "addonName",
        "cluster_name": "clusterName",
    },
)
class AddonReference:
    def __init__(
        self,
        *,
        addon_arn: builtins.str,
        addon_name: builtins.str,
        cluster_name: builtins.str,
    ) -> None:
        '''A reference to a Addon resource.

        :param addon_arn: The ARN of the Addon resource.
        :param addon_name: The AddonName of the Addon resource.
        :param cluster_name: The ClusterName of the Addon resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eks as interfaces_eks
            
            addon_reference = interfaces_eks.AddonReference(
                addon_arn="addonArn",
                addon_name="addonName",
                cluster_name="clusterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8380b0e2d2286804f49005cd1b95a852ea64c317bb9048747945aafc0d036cf6)
            check_type(argname="argument addon_arn", value=addon_arn, expected_type=type_hints["addon_arn"])
            check_type(argname="argument addon_name", value=addon_name, expected_type=type_hints["addon_name"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "addon_arn": addon_arn,
            "addon_name": addon_name,
            "cluster_name": cluster_name,
        }

    @builtins.property
    def addon_arn(self) -> builtins.str:
        '''The ARN of the Addon resource.'''
        result = self._values.get("addon_arn")
        assert result is not None, "Required property 'addon_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addon_name(self) -> builtins.str:
        '''The AddonName of the Addon resource.'''
        result = self._values.get("addon_name")
        assert result is not None, "Required property 'addon_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The ClusterName of the Addon resource.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddonReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eks.CapabilityReference",
    jsii_struct_bases=[],
    name_mapping={"capability_arn": "capabilityArn"},
)
class CapabilityReference:
    def __init__(self, *, capability_arn: builtins.str) -> None:
        '''A reference to a Capability resource.

        :param capability_arn: The Arn of the Capability resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eks as interfaces_eks
            
            capability_reference = interfaces_eks.CapabilityReference(
                capability_arn="capabilityArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc801b63380c6ce04f8c7266654f326fcd069c8bbc7b78140d8b612445f8e92c)
            check_type(argname="argument capability_arn", value=capability_arn, expected_type=type_hints["capability_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capability_arn": capability_arn,
        }

    @builtins.property
    def capability_arn(self) -> builtins.str:
        '''The Arn of the Capability resource.'''
        result = self._values.get("capability_arn")
        assert result is not None, "Required property 'capability_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapabilityReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eks.ClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn", "cluster_name": "clusterName"},
)
class ClusterReference:
    def __init__(
        self,
        *,
        cluster_arn: builtins.str,
        cluster_name: builtins.str,
    ) -> None:
        '''A reference to a Cluster resource.

        :param cluster_arn: The ARN of the Cluster resource.
        :param cluster_name: The Name of the Cluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eks as interfaces_eks
            
            cluster_reference = interfaces_eks.ClusterReference(
                cluster_arn="clusterArn",
                cluster_name="clusterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__109fa15f1d27371bb677c33727e10865a978f7a73cae0377fbee4c3b9b55a366)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
            "cluster_name": cluster_name,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The ARN of the Cluster resource.'''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The Name of the Cluster resource.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eks.FargateProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "fargate_profile_arn": "fargateProfileArn",
        "fargate_profile_name": "fargateProfileName",
    },
)
class FargateProfileReference:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        fargate_profile_arn: builtins.str,
        fargate_profile_name: builtins.str,
    ) -> None:
        '''A reference to a FargateProfile resource.

        :param cluster_name: The ClusterName of the FargateProfile resource.
        :param fargate_profile_arn: The ARN of the FargateProfile resource.
        :param fargate_profile_name: The FargateProfileName of the FargateProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eks as interfaces_eks
            
            fargate_profile_reference = interfaces_eks.FargateProfileReference(
                cluster_name="clusterName",
                fargate_profile_arn="fargateProfileArn",
                fargate_profile_name="fargateProfileName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e5b29978a76afad9c5fd180fa3163bf155032420d2718449094254c332eeec2)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument fargate_profile_arn", value=fargate_profile_arn, expected_type=type_hints["fargate_profile_arn"])
            check_type(argname="argument fargate_profile_name", value=fargate_profile_name, expected_type=type_hints["fargate_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "fargate_profile_arn": fargate_profile_arn,
            "fargate_profile_name": fargate_profile_name,
        }

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The ClusterName of the FargateProfile resource.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fargate_profile_arn(self) -> builtins.str:
        '''The ARN of the FargateProfile resource.'''
        result = self._values.get("fargate_profile_arn")
        assert result is not None, "Required property 'fargate_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fargate_profile_name(self) -> builtins.str:
        '''The FargateProfileName of the FargateProfile resource.'''
        result = self._values.get("fargate_profile_name")
        assert result is not None, "Required property 'fargate_profile_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FargateProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eks.IAccessEntryRef")
class IAccessEntryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessEntry.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessEntryRef")
    def access_entry_ref(self) -> "AccessEntryReference":
        '''(experimental) A reference to a AccessEntry resource.

        :stability: experimental
        '''
        ...


class _IAccessEntryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessEntry.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eks.IAccessEntryRef"

    @builtins.property
    @jsii.member(jsii_name="accessEntryRef")
    def access_entry_ref(self) -> "AccessEntryReference":
        '''(experimental) A reference to a AccessEntry resource.

        :stability: experimental
        '''
        return typing.cast("AccessEntryReference", jsii.get(self, "accessEntryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessEntryRef).__jsii_proxy_class__ = lambda : _IAccessEntryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eks.IAddonRef")
class IAddonRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Addon.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="addonRef")
    def addon_ref(self) -> "AddonReference":
        '''(experimental) A reference to a Addon resource.

        :stability: experimental
        '''
        ...


class _IAddonRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Addon.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eks.IAddonRef"

    @builtins.property
    @jsii.member(jsii_name="addonRef")
    def addon_ref(self) -> "AddonReference":
        '''(experimental) A reference to a Addon resource.

        :stability: experimental
        '''
        return typing.cast("AddonReference", jsii.get(self, "addonRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAddonRef).__jsii_proxy_class__ = lambda : _IAddonRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eks.ICapabilityRef")
class ICapabilityRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Capability.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="capabilityRef")
    def capability_ref(self) -> "CapabilityReference":
        '''(experimental) A reference to a Capability resource.

        :stability: experimental
        '''
        ...


class _ICapabilityRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Capability.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eks.ICapabilityRef"

    @builtins.property
    @jsii.member(jsii_name="capabilityRef")
    def capability_ref(self) -> "CapabilityReference":
        '''(experimental) A reference to a Capability resource.

        :stability: experimental
        '''
        return typing.cast("CapabilityReference", jsii.get(self, "capabilityRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICapabilityRef).__jsii_proxy_class__ = lambda : _ICapabilityRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eks.IClusterRef")
class IClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        ...


class _IClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eks.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eks.IFargateProfileRef")
class IFargateProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FargateProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fargateProfileRef")
    def fargate_profile_ref(self) -> "FargateProfileReference":
        '''(experimental) A reference to a FargateProfile resource.

        :stability: experimental
        '''
        ...


class _IFargateProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FargateProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eks.IFargateProfileRef"

    @builtins.property
    @jsii.member(jsii_name="fargateProfileRef")
    def fargate_profile_ref(self) -> "FargateProfileReference":
        '''(experimental) A reference to a FargateProfile resource.

        :stability: experimental
        '''
        return typing.cast("FargateProfileReference", jsii.get(self, "fargateProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFargateProfileRef).__jsii_proxy_class__ = lambda : _IFargateProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eks.IIdentityProviderConfigRef")
class IIdentityProviderConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityProviderConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="identityProviderConfigRef")
    def identity_provider_config_ref(self) -> "IdentityProviderConfigReference":
        '''(experimental) A reference to a IdentityProviderConfig resource.

        :stability: experimental
        '''
        ...


class _IIdentityProviderConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityProviderConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eks.IIdentityProviderConfigRef"

    @builtins.property
    @jsii.member(jsii_name="identityProviderConfigRef")
    def identity_provider_config_ref(self) -> "IdentityProviderConfigReference":
        '''(experimental) A reference to a IdentityProviderConfig resource.

        :stability: experimental
        '''
        return typing.cast("IdentityProviderConfigReference", jsii.get(self, "identityProviderConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentityProviderConfigRef).__jsii_proxy_class__ = lambda : _IIdentityProviderConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eks.INodegroupRef")
class INodegroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Nodegroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="nodegroupRef")
    def nodegroup_ref(self) -> "NodegroupReference":
        '''(experimental) A reference to a Nodegroup resource.

        :stability: experimental
        '''
        ...


class _INodegroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Nodegroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eks.INodegroupRef"

    @builtins.property
    @jsii.member(jsii_name="nodegroupRef")
    def nodegroup_ref(self) -> "NodegroupReference":
        '''(experimental) A reference to a Nodegroup resource.

        :stability: experimental
        '''
        return typing.cast("NodegroupReference", jsii.get(self, "nodegroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INodegroupRef).__jsii_proxy_class__ = lambda : _INodegroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eks.IPodIdentityAssociationRef")
class IPodIdentityAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PodIdentityAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="podIdentityAssociationRef")
    def pod_identity_association_ref(self) -> "PodIdentityAssociationReference":
        '''(experimental) A reference to a PodIdentityAssociation resource.

        :stability: experimental
        '''
        ...


class _IPodIdentityAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PodIdentityAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eks.IPodIdentityAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="podIdentityAssociationRef")
    def pod_identity_association_ref(self) -> "PodIdentityAssociationReference":
        '''(experimental) A reference to a PodIdentityAssociation resource.

        :stability: experimental
        '''
        return typing.cast("PodIdentityAssociationReference", jsii.get(self, "podIdentityAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPodIdentityAssociationRef).__jsii_proxy_class__ = lambda : _IPodIdentityAssociationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eks.IdentityProviderConfigReference",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "identity_provider_config_arn": "identityProviderConfigArn",
        "identity_provider_config_name": "identityProviderConfigName",
        "type": "type",
    },
)
class IdentityProviderConfigReference:
    def __init__(
        self,
        *,
        cluster_name: builtins.str,
        identity_provider_config_arn: builtins.str,
        identity_provider_config_name: builtins.str,
        type: builtins.str,
    ) -> None:
        '''A reference to a IdentityProviderConfig resource.

        :param cluster_name: The ClusterName of the IdentityProviderConfig resource.
        :param identity_provider_config_arn: The ARN of the IdentityProviderConfig resource.
        :param identity_provider_config_name: The IdentityProviderConfigName of the IdentityProviderConfig resource.
        :param type: The Type of the IdentityProviderConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eks as interfaces_eks
            
            identity_provider_config_reference = interfaces_eks.IdentityProviderConfigReference(
                cluster_name="clusterName",
                identity_provider_config_arn="identityProviderConfigArn",
                identity_provider_config_name="identityProviderConfigName",
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7f2b95faafabd5a5ac589edc611ad9e0ba9316371e087b5c86757363f9c056e)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument identity_provider_config_arn", value=identity_provider_config_arn, expected_type=type_hints["identity_provider_config_arn"])
            check_type(argname="argument identity_provider_config_name", value=identity_provider_config_name, expected_type=type_hints["identity_provider_config_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
            "identity_provider_config_arn": identity_provider_config_arn,
            "identity_provider_config_name": identity_provider_config_name,
            "type": type,
        }

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The ClusterName of the IdentityProviderConfig resource.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_provider_config_arn(self) -> builtins.str:
        '''The ARN of the IdentityProviderConfig resource.'''
        result = self._values.get("identity_provider_config_arn")
        assert result is not None, "Required property 'identity_provider_config_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_provider_config_name(self) -> builtins.str:
        '''The IdentityProviderConfigName of the IdentityProviderConfig resource.'''
        result = self._values.get("identity_provider_config_name")
        assert result is not None, "Required property 'identity_provider_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The Type of the IdentityProviderConfig resource.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityProviderConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eks.NodegroupReference",
    jsii_struct_bases=[],
    name_mapping={"nodegroup_arn": "nodegroupArn", "nodegroup_id": "nodegroupId"},
)
class NodegroupReference:
    def __init__(
        self,
        *,
        nodegroup_arn: builtins.str,
        nodegroup_id: builtins.str,
    ) -> None:
        '''A reference to a Nodegroup resource.

        :param nodegroup_arn: The ARN of the Nodegroup resource.
        :param nodegroup_id: The Id of the Nodegroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eks as interfaces_eks
            
            nodegroup_reference = interfaces_eks.NodegroupReference(
                nodegroup_arn="nodegroupArn",
                nodegroup_id="nodegroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__975a2ffb7c240c21e751d5713f57ab08728fcfcda506863593becc085d7234c7)
            check_type(argname="argument nodegroup_arn", value=nodegroup_arn, expected_type=type_hints["nodegroup_arn"])
            check_type(argname="argument nodegroup_id", value=nodegroup_id, expected_type=type_hints["nodegroup_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nodegroup_arn": nodegroup_arn,
            "nodegroup_id": nodegroup_id,
        }

    @builtins.property
    def nodegroup_arn(self) -> builtins.str:
        '''The ARN of the Nodegroup resource.'''
        result = self._values.get("nodegroup_arn")
        assert result is not None, "Required property 'nodegroup_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def nodegroup_id(self) -> builtins.str:
        '''The Id of the Nodegroup resource.'''
        result = self._values.get("nodegroup_id")
        assert result is not None, "Required property 'nodegroup_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NodegroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eks.PodIdentityAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"association_arn": "associationArn"},
)
class PodIdentityAssociationReference:
    def __init__(self, *, association_arn: builtins.str) -> None:
        '''A reference to a PodIdentityAssociation resource.

        :param association_arn: The AssociationArn of the PodIdentityAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eks as interfaces_eks
            
            pod_identity_association_reference = interfaces_eks.PodIdentityAssociationReference(
                association_arn="associationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7465fc9c2ed3ddbe51e8bf5142f1243a8335f32f088977ac177d64c248cde46)
            check_type(argname="argument association_arn", value=association_arn, expected_type=type_hints["association_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_arn": association_arn,
        }

    @builtins.property
    def association_arn(self) -> builtins.str:
        '''The AssociationArn of the PodIdentityAssociation resource.'''
        result = self._values.get("association_arn")
        assert result is not None, "Required property 'association_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodIdentityAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessEntryReference",
    "AddonReference",
    "CapabilityReference",
    "ClusterReference",
    "FargateProfileReference",
    "IAccessEntryRef",
    "IAddonRef",
    "ICapabilityRef",
    "IClusterRef",
    "IFargateProfileRef",
    "IIdentityProviderConfigRef",
    "INodegroupRef",
    "IPodIdentityAssociationRef",
    "IdentityProviderConfigReference",
    "NodegroupReference",
    "PodIdentityAssociationReference",
]

publication.publish()

def _typecheckingstub__70a5e484db113b4d5529dd453bcc42197c4a3a2f2574700dceec0ec68d28ea53(
    *,
    access_entry_arn: builtins.str,
    cluster_name: builtins.str,
    principal_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8380b0e2d2286804f49005cd1b95a852ea64c317bb9048747945aafc0d036cf6(
    *,
    addon_arn: builtins.str,
    addon_name: builtins.str,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc801b63380c6ce04f8c7266654f326fcd069c8bbc7b78140d8b612445f8e92c(
    *,
    capability_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__109fa15f1d27371bb677c33727e10865a978f7a73cae0377fbee4c3b9b55a366(
    *,
    cluster_arn: builtins.str,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5b29978a76afad9c5fd180fa3163bf155032420d2718449094254c332eeec2(
    *,
    cluster_name: builtins.str,
    fargate_profile_arn: builtins.str,
    fargate_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7f2b95faafabd5a5ac589edc611ad9e0ba9316371e087b5c86757363f9c056e(
    *,
    cluster_name: builtins.str,
    identity_provider_config_arn: builtins.str,
    identity_provider_config_name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__975a2ffb7c240c21e751d5713f57ab08728fcfcda506863593becc085d7234c7(
    *,
    nodegroup_arn: builtins.str,
    nodegroup_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7465fc9c2ed3ddbe51e8bf5142f1243a8335f32f088977ac177d64c248cde46(
    *,
    association_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessEntryRef, IAddonRef, ICapabilityRef, IClusterRef, IFargateProfileRef, IIdentityProviderConfigRef, INodegroupRef, IPodIdentityAssociationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
