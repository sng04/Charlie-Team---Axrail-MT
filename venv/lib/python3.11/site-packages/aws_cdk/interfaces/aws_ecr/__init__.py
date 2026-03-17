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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecr.IPublicRepositoryRef")
class IPublicRepositoryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PublicRepository.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="publicRepositoryRef")
    def public_repository_ref(self) -> "PublicRepositoryReference":
        '''(experimental) A reference to a PublicRepository resource.

        :stability: experimental
        '''
        ...


class _IPublicRepositoryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PublicRepository.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecr.IPublicRepositoryRef"

    @builtins.property
    @jsii.member(jsii_name="publicRepositoryRef")
    def public_repository_ref(self) -> "PublicRepositoryReference":
        '''(experimental) A reference to a PublicRepository resource.

        :stability: experimental
        '''
        return typing.cast("PublicRepositoryReference", jsii.get(self, "publicRepositoryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicRepositoryRef).__jsii_proxy_class__ = lambda : _IPublicRepositoryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecr.IPullThroughCacheRuleRef")
class IPullThroughCacheRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PullThroughCacheRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pullThroughCacheRuleRef")
    def pull_through_cache_rule_ref(self) -> "PullThroughCacheRuleReference":
        '''(experimental) A reference to a PullThroughCacheRule resource.

        :stability: experimental
        '''
        ...


class _IPullThroughCacheRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PullThroughCacheRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecr.IPullThroughCacheRuleRef"

    @builtins.property
    @jsii.member(jsii_name="pullThroughCacheRuleRef")
    def pull_through_cache_rule_ref(self) -> "PullThroughCacheRuleReference":
        '''(experimental) A reference to a PullThroughCacheRule resource.

        :stability: experimental
        '''
        return typing.cast("PullThroughCacheRuleReference", jsii.get(self, "pullThroughCacheRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPullThroughCacheRuleRef).__jsii_proxy_class__ = lambda : _IPullThroughCacheRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecr.IPullTimeUpdateExclusionRef")
class IPullTimeUpdateExclusionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PullTimeUpdateExclusion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pullTimeUpdateExclusionRef")
    def pull_time_update_exclusion_ref(self) -> "PullTimeUpdateExclusionReference":
        '''(experimental) A reference to a PullTimeUpdateExclusion resource.

        :stability: experimental
        '''
        ...


class _IPullTimeUpdateExclusionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PullTimeUpdateExclusion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecr.IPullTimeUpdateExclusionRef"

    @builtins.property
    @jsii.member(jsii_name="pullTimeUpdateExclusionRef")
    def pull_time_update_exclusion_ref(self) -> "PullTimeUpdateExclusionReference":
        '''(experimental) A reference to a PullTimeUpdateExclusion resource.

        :stability: experimental
        '''
        return typing.cast("PullTimeUpdateExclusionReference", jsii.get(self, "pullTimeUpdateExclusionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPullTimeUpdateExclusionRef).__jsii_proxy_class__ = lambda : _IPullTimeUpdateExclusionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecr.IRegistryPolicyRef")
class IRegistryPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RegistryPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="registryPolicyRef")
    def registry_policy_ref(self) -> "RegistryPolicyReference":
        '''(experimental) A reference to a RegistryPolicy resource.

        :stability: experimental
        '''
        ...


class _IRegistryPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RegistryPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecr.IRegistryPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="registryPolicyRef")
    def registry_policy_ref(self) -> "RegistryPolicyReference":
        '''(experimental) A reference to a RegistryPolicy resource.

        :stability: experimental
        '''
        return typing.cast("RegistryPolicyReference", jsii.get(self, "registryPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegistryPolicyRef).__jsii_proxy_class__ = lambda : _IRegistryPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.IRegistryScanningConfigurationRef"
)
class IRegistryScanningConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RegistryScanningConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="registryScanningConfigurationRef")
    def registry_scanning_configuration_ref(
        self,
    ) -> "RegistryScanningConfigurationReference":
        '''(experimental) A reference to a RegistryScanningConfiguration resource.

        :stability: experimental
        '''
        ...


class _IRegistryScanningConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RegistryScanningConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecr.IRegistryScanningConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="registryScanningConfigurationRef")
    def registry_scanning_configuration_ref(
        self,
    ) -> "RegistryScanningConfigurationReference":
        '''(experimental) A reference to a RegistryScanningConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("RegistryScanningConfigurationReference", jsii.get(self, "registryScanningConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegistryScanningConfigurationRef).__jsii_proxy_class__ = lambda : _IRegistryScanningConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.IReplicationConfigurationRef"
)
class IReplicationConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="replicationConfigurationRef")
    def replication_configuration_ref(self) -> "ReplicationConfigurationReference":
        '''(experimental) A reference to a ReplicationConfiguration resource.

        :stability: experimental
        '''
        ...


class _IReplicationConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecr.IReplicationConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="replicationConfigurationRef")
    def replication_configuration_ref(self) -> "ReplicationConfigurationReference":
        '''(experimental) A reference to a ReplicationConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("ReplicationConfigurationReference", jsii.get(self, "replicationConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReplicationConfigurationRef).__jsii_proxy_class__ = lambda : _IReplicationConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.IRepositoryCreationTemplateRef"
)
class IRepositoryCreationTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RepositoryCreationTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="repositoryCreationTemplateRef")
    def repository_creation_template_ref(self) -> "RepositoryCreationTemplateReference":
        '''(experimental) A reference to a RepositoryCreationTemplate resource.

        :stability: experimental
        '''
        ...


class _IRepositoryCreationTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RepositoryCreationTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecr.IRepositoryCreationTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="repositoryCreationTemplateRef")
    def repository_creation_template_ref(self) -> "RepositoryCreationTemplateReference":
        '''(experimental) A reference to a RepositoryCreationTemplate resource.

        :stability: experimental
        '''
        return typing.cast("RepositoryCreationTemplateReference", jsii.get(self, "repositoryCreationTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRepositoryCreationTemplateRef).__jsii_proxy_class__ = lambda : _IRepositoryCreationTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecr.IRepositoryRef")
class IRepositoryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Repository.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="repositoryRef")
    def repository_ref(self) -> "RepositoryReference":
        '''(experimental) A reference to a Repository resource.

        :stability: experimental
        '''
        ...


class _IRepositoryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Repository.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecr.IRepositoryRef"

    @builtins.property
    @jsii.member(jsii_name="repositoryRef")
    def repository_ref(self) -> "RepositoryReference":
        '''(experimental) A reference to a Repository resource.

        :stability: experimental
        '''
        return typing.cast("RepositoryReference", jsii.get(self, "repositoryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRepositoryRef).__jsii_proxy_class__ = lambda : _IRepositoryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecr.ISigningConfigurationRef")
class ISigningConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SigningConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="signingConfigurationRef")
    def signing_configuration_ref(self) -> "SigningConfigurationReference":
        '''(experimental) A reference to a SigningConfiguration resource.

        :stability: experimental
        '''
        ...


class _ISigningConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SigningConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecr.ISigningConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="signingConfigurationRef")
    def signing_configuration_ref(self) -> "SigningConfigurationReference":
        '''(experimental) A reference to a SigningConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("SigningConfigurationReference", jsii.get(self, "signingConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISigningConfigurationRef).__jsii_proxy_class__ = lambda : _ISigningConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.PublicRepositoryReference",
    jsii_struct_bases=[],
    name_mapping={
        "public_repository_arn": "publicRepositoryArn",
        "repository_name": "repositoryName",
    },
)
class PublicRepositoryReference:
    def __init__(
        self,
        *,
        public_repository_arn: builtins.str,
        repository_name: builtins.str,
    ) -> None:
        '''A reference to a PublicRepository resource.

        :param public_repository_arn: The ARN of the PublicRepository resource.
        :param repository_name: The RepositoryName of the PublicRepository resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecr as interfaces_ecr
            
            public_repository_reference = interfaces_ecr.PublicRepositoryReference(
                public_repository_arn="publicRepositoryArn",
                repository_name="repositoryName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebfd2912489ae24385c01d2d04e3310cbb4346432c48a1318317144a875e6a58)
            check_type(argname="argument public_repository_arn", value=public_repository_arn, expected_type=type_hints["public_repository_arn"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_repository_arn": public_repository_arn,
            "repository_name": repository_name,
        }

    @builtins.property
    def public_repository_arn(self) -> builtins.str:
        '''The ARN of the PublicRepository resource.'''
        result = self._values.get("public_repository_arn")
        assert result is not None, "Required property 'public_repository_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''The RepositoryName of the PublicRepository resource.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicRepositoryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.PullThroughCacheRuleReference",
    jsii_struct_bases=[],
    name_mapping={"ecr_repository_prefix": "ecrRepositoryPrefix"},
)
class PullThroughCacheRuleReference:
    def __init__(self, *, ecr_repository_prefix: builtins.str) -> None:
        '''A reference to a PullThroughCacheRule resource.

        :param ecr_repository_prefix: The EcrRepositoryPrefix of the PullThroughCacheRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecr as interfaces_ecr
            
            pull_through_cache_rule_reference = interfaces_ecr.PullThroughCacheRuleReference(
                ecr_repository_prefix="ecrRepositoryPrefix"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145dab6c3bc935d0a97f691c737a910e8ba1300b79792f40d3dfb1008511c177)
            check_type(argname="argument ecr_repository_prefix", value=ecr_repository_prefix, expected_type=type_hints["ecr_repository_prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ecr_repository_prefix": ecr_repository_prefix,
        }

    @builtins.property
    def ecr_repository_prefix(self) -> builtins.str:
        '''The EcrRepositoryPrefix of the PullThroughCacheRule resource.'''
        result = self._values.get("ecr_repository_prefix")
        assert result is not None, "Required property 'ecr_repository_prefix' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PullThroughCacheRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.PullTimeUpdateExclusionReference",
    jsii_struct_bases=[],
    name_mapping={"principal_arn": "principalArn"},
)
class PullTimeUpdateExclusionReference:
    def __init__(self, *, principal_arn: builtins.str) -> None:
        '''A reference to a PullTimeUpdateExclusion resource.

        :param principal_arn: The PrincipalArn of the PullTimeUpdateExclusion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecr as interfaces_ecr
            
            pull_time_update_exclusion_reference = interfaces_ecr.PullTimeUpdateExclusionReference(
                principal_arn="principalArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__330a03e1fa55fb9c9d03472c69de74e957ac563c8d7dc720929d2a24569ea675)
            check_type(argname="argument principal_arn", value=principal_arn, expected_type=type_hints["principal_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "principal_arn": principal_arn,
        }

    @builtins.property
    def principal_arn(self) -> builtins.str:
        '''The PrincipalArn of the PullTimeUpdateExclusion resource.'''
        result = self._values.get("principal_arn")
        assert result is not None, "Required property 'principal_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PullTimeUpdateExclusionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.RegistryPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"registry_id": "registryId"},
)
class RegistryPolicyReference:
    def __init__(self, *, registry_id: builtins.str) -> None:
        '''A reference to a RegistryPolicy resource.

        :param registry_id: The RegistryId of the RegistryPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecr as interfaces_ecr
            
            registry_policy_reference = interfaces_ecr.RegistryPolicyReference(
                registry_id="registryId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adbdf7f0cd6e663344f70be0b5fa348493a990a080943914514a05cfacf2dc95)
            check_type(argname="argument registry_id", value=registry_id, expected_type=type_hints["registry_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_id": registry_id,
        }

    @builtins.property
    def registry_id(self) -> builtins.str:
        '''The RegistryId of the RegistryPolicy resource.'''
        result = self._values.get("registry_id")
        assert result is not None, "Required property 'registry_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.RegistryScanningConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"registry_id": "registryId"},
)
class RegistryScanningConfigurationReference:
    def __init__(self, *, registry_id: builtins.str) -> None:
        '''A reference to a RegistryScanningConfiguration resource.

        :param registry_id: The RegistryId of the RegistryScanningConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecr as interfaces_ecr
            
            registry_scanning_configuration_reference = interfaces_ecr.RegistryScanningConfigurationReference(
                registry_id="registryId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ee207c1cd4e8682993e949b8972b5f14d9e37a776fc2cb20f7fe381aaf8c25d)
            check_type(argname="argument registry_id", value=registry_id, expected_type=type_hints["registry_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_id": registry_id,
        }

    @builtins.property
    def registry_id(self) -> builtins.str:
        '''The RegistryId of the RegistryScanningConfiguration resource.'''
        result = self._values.get("registry_id")
        assert result is not None, "Required property 'registry_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryScanningConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.ReplicationConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"registry_id": "registryId"},
)
class ReplicationConfigurationReference:
    def __init__(self, *, registry_id: builtins.str) -> None:
        '''A reference to a ReplicationConfiguration resource.

        :param registry_id: The RegistryId of the ReplicationConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecr as interfaces_ecr
            
            replication_configuration_reference = interfaces_ecr.ReplicationConfigurationReference(
                registry_id="registryId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c47cd53463c588d1b5b205c09185c16a98bbabe3ab9a58d21c9d9c458bc95220)
            check_type(argname="argument registry_id", value=registry_id, expected_type=type_hints["registry_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_id": registry_id,
        }

    @builtins.property
    def registry_id(self) -> builtins.str:
        '''The RegistryId of the ReplicationConfiguration resource.'''
        result = self._values.get("registry_id")
        assert result is not None, "Required property 'registry_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.RepositoryCreationTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"prefix": "prefix"},
)
class RepositoryCreationTemplateReference:
    def __init__(self, *, prefix: builtins.str) -> None:
        '''A reference to a RepositoryCreationTemplate resource.

        :param prefix: The Prefix of the RepositoryCreationTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecr as interfaces_ecr
            
            repository_creation_template_reference = interfaces_ecr.RepositoryCreationTemplateReference(
                prefix="prefix"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d0639d93d36d2a80d3b390e50a9eb750e26e65b1ac6939a9416a6455008fac)
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prefix": prefix,
        }

    @builtins.property
    def prefix(self) -> builtins.str:
        '''The Prefix of the RepositoryCreationTemplate resource.'''
        result = self._values.get("prefix")
        assert result is not None, "Required property 'prefix' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryCreationTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.RepositoryReference",
    jsii_struct_bases=[],
    name_mapping={
        "repository_arn": "repositoryArn",
        "repository_name": "repositoryName",
    },
)
class RepositoryReference:
    def __init__(
        self,
        *,
        repository_arn: builtins.str,
        repository_name: builtins.str,
    ) -> None:
        '''A reference to a Repository resource.

        :param repository_arn: The ARN of the Repository resource.
        :param repository_name: The RepositoryName of the Repository resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecr as interfaces_ecr
            
            repository_reference = interfaces_ecr.RepositoryReference(
                repository_arn="repositoryArn",
                repository_name="repositoryName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66f32cea5ccda62bfe26a5f38558d87cb2981e17b98568d84bbddab158c09060)
            check_type(argname="argument repository_arn", value=repository_arn, expected_type=type_hints["repository_arn"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_arn": repository_arn,
            "repository_name": repository_name,
        }

    @builtins.property
    def repository_arn(self) -> builtins.str:
        '''The ARN of the Repository resource.'''
        result = self._values.get("repository_arn")
        assert result is not None, "Required property 'repository_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''The RepositoryName of the Repository resource.'''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecr.SigningConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"registry_id": "registryId"},
)
class SigningConfigurationReference:
    def __init__(self, *, registry_id: builtins.str) -> None:
        '''A reference to a SigningConfiguration resource.

        :param registry_id: The RegistryId of the SigningConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecr as interfaces_ecr
            
            signing_configuration_reference = interfaces_ecr.SigningConfigurationReference(
                registry_id="registryId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ca5da87623cd8967a68263b6732601acb2deab8aca8c22890cdd5142d8a3a9d)
            check_type(argname="argument registry_id", value=registry_id, expected_type=type_hints["registry_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_id": registry_id,
        }

    @builtins.property
    def registry_id(self) -> builtins.str:
        '''The RegistryId of the SigningConfiguration resource.'''
        result = self._values.get("registry_id")
        assert result is not None, "Required property 'registry_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SigningConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IPublicRepositoryRef",
    "IPullThroughCacheRuleRef",
    "IPullTimeUpdateExclusionRef",
    "IRegistryPolicyRef",
    "IRegistryScanningConfigurationRef",
    "IReplicationConfigurationRef",
    "IRepositoryCreationTemplateRef",
    "IRepositoryRef",
    "ISigningConfigurationRef",
    "PublicRepositoryReference",
    "PullThroughCacheRuleReference",
    "PullTimeUpdateExclusionReference",
    "RegistryPolicyReference",
    "RegistryScanningConfigurationReference",
    "ReplicationConfigurationReference",
    "RepositoryCreationTemplateReference",
    "RepositoryReference",
    "SigningConfigurationReference",
]

publication.publish()

def _typecheckingstub__ebfd2912489ae24385c01d2d04e3310cbb4346432c48a1318317144a875e6a58(
    *,
    public_repository_arn: builtins.str,
    repository_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145dab6c3bc935d0a97f691c737a910e8ba1300b79792f40d3dfb1008511c177(
    *,
    ecr_repository_prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__330a03e1fa55fb9c9d03472c69de74e957ac563c8d7dc720929d2a24569ea675(
    *,
    principal_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adbdf7f0cd6e663344f70be0b5fa348493a990a080943914514a05cfacf2dc95(
    *,
    registry_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ee207c1cd4e8682993e949b8972b5f14d9e37a776fc2cb20f7fe381aaf8c25d(
    *,
    registry_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c47cd53463c588d1b5b205c09185c16a98bbabe3ab9a58d21c9d9c458bc95220(
    *,
    registry_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d0639d93d36d2a80d3b390e50a9eb750e26e65b1ac6939a9416a6455008fac(
    *,
    prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f32cea5ccda62bfe26a5f38558d87cb2981e17b98568d84bbddab158c09060(
    *,
    repository_arn: builtins.str,
    repository_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ca5da87623cd8967a68263b6732601acb2deab8aca8c22890cdd5142d8a3a9d(
    *,
    registry_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IPublicRepositoryRef, IPullThroughCacheRuleRef, IPullTimeUpdateExclusionRef, IRegistryPolicyRef, IRegistryScanningConfigurationRef, IReplicationConfigurationRef, IRepositoryCreationTemplateRef, IRepositoryRef, ISigningConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
