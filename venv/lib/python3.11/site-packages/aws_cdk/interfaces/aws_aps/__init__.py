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
    jsii_type="aws-cdk-lib.interfaces.aws_aps.AnomalyDetectorReference",
    jsii_struct_bases=[],
    name_mapping={"anomaly_detector_arn": "anomalyDetectorArn"},
)
class AnomalyDetectorReference:
    def __init__(self, *, anomaly_detector_arn: builtins.str) -> None:
        '''A reference to a AnomalyDetector resource.

        :param anomaly_detector_arn: The Arn of the AnomalyDetector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_aps as interfaces_aps
            
            anomaly_detector_reference = interfaces_aps.AnomalyDetectorReference(
                anomaly_detector_arn="anomalyDetectorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8713accc66b6c1a4a61b78d26bd833761032f548f0c6d01a445c484902f3b26b)
            check_type(argname="argument anomaly_detector_arn", value=anomaly_detector_arn, expected_type=type_hints["anomaly_detector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "anomaly_detector_arn": anomaly_detector_arn,
        }

    @builtins.property
    def anomaly_detector_arn(self) -> builtins.str:
        '''The Arn of the AnomalyDetector resource.'''
        result = self._values.get("anomaly_detector_arn")
        assert result is not None, "Required property 'anomaly_detector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnomalyDetectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_aps.IAnomalyDetectorRef")
class IAnomalyDetectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AnomalyDetector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorRef")
    def anomaly_detector_ref(self) -> "AnomalyDetectorReference":
        '''(experimental) A reference to a AnomalyDetector resource.

        :stability: experimental
        '''
        ...


class _IAnomalyDetectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AnomalyDetector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_aps.IAnomalyDetectorRef"

    @builtins.property
    @jsii.member(jsii_name="anomalyDetectorRef")
    def anomaly_detector_ref(self) -> "AnomalyDetectorReference":
        '''(experimental) A reference to a AnomalyDetector resource.

        :stability: experimental
        '''
        return typing.cast("AnomalyDetectorReference", jsii.get(self, "anomalyDetectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnomalyDetectorRef).__jsii_proxy_class__ = lambda : _IAnomalyDetectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_aps.IResourcePolicyRef")
class IResourcePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        ...


class _IResourcePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_aps.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_aps.IRuleGroupsNamespaceRef")
class IRuleGroupsNamespaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RuleGroupsNamespace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ruleGroupsNamespaceRef")
    def rule_groups_namespace_ref(self) -> "RuleGroupsNamespaceReference":
        '''(experimental) A reference to a RuleGroupsNamespace resource.

        :stability: experimental
        '''
        ...


class _IRuleGroupsNamespaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RuleGroupsNamespace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_aps.IRuleGroupsNamespaceRef"

    @builtins.property
    @jsii.member(jsii_name="ruleGroupsNamespaceRef")
    def rule_groups_namespace_ref(self) -> "RuleGroupsNamespaceReference":
        '''(experimental) A reference to a RuleGroupsNamespace resource.

        :stability: experimental
        '''
        return typing.cast("RuleGroupsNamespaceReference", jsii.get(self, "ruleGroupsNamespaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuleGroupsNamespaceRef).__jsii_proxy_class__ = lambda : _IRuleGroupsNamespaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_aps.IScraperRef")
class IScraperRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Scraper.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scraperRef")
    def scraper_ref(self) -> "ScraperReference":
        '''(experimental) A reference to a Scraper resource.

        :stability: experimental
        '''
        ...


class _IScraperRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Scraper.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_aps.IScraperRef"

    @builtins.property
    @jsii.member(jsii_name="scraperRef")
    def scraper_ref(self) -> "ScraperReference":
        '''(experimental) A reference to a Scraper resource.

        :stability: experimental
        '''
        return typing.cast("ScraperReference", jsii.get(self, "scraperRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScraperRef).__jsii_proxy_class__ = lambda : _IScraperRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_aps.IWorkspaceRef")
class IWorkspaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workspace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workspaceRef")
    def workspace_ref(self) -> "WorkspaceReference":
        '''(experimental) A reference to a Workspace resource.

        :stability: experimental
        '''
        ...


class _IWorkspaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workspace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_aps.IWorkspaceRef"

    @builtins.property
    @jsii.member(jsii_name="workspaceRef")
    def workspace_ref(self) -> "WorkspaceReference":
        '''(experimental) A reference to a Workspace resource.

        :stability: experimental
        '''
        return typing.cast("WorkspaceReference", jsii.get(self, "workspaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkspaceRef).__jsii_proxy_class__ = lambda : _IWorkspaceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_aps.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"workspace_arn": "workspaceArn"},
)
class ResourcePolicyReference:
    def __init__(self, *, workspace_arn: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param workspace_arn: The WorkspaceArn of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_aps as interfaces_aps
            
            resource_policy_reference = interfaces_aps.ResourcePolicyReference(
                workspace_arn="workspaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0f24d8ab317c40a83230f293fadb89964bbc2927faa60441cac5180eb7b4008)
            check_type(argname="argument workspace_arn", value=workspace_arn, expected_type=type_hints["workspace_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workspace_arn": workspace_arn,
        }

    @builtins.property
    def workspace_arn(self) -> builtins.str:
        '''The WorkspaceArn of the ResourcePolicy resource.'''
        result = self._values.get("workspace_arn")
        assert result is not None, "Required property 'workspace_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_aps.RuleGroupsNamespaceReference",
    jsii_struct_bases=[],
    name_mapping={"rule_groups_namespace_arn": "ruleGroupsNamespaceArn"},
)
class RuleGroupsNamespaceReference:
    def __init__(self, *, rule_groups_namespace_arn: builtins.str) -> None:
        '''A reference to a RuleGroupsNamespace resource.

        :param rule_groups_namespace_arn: The Arn of the RuleGroupsNamespace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_aps as interfaces_aps
            
            rule_groups_namespace_reference = interfaces_aps.RuleGroupsNamespaceReference(
                rule_groups_namespace_arn="ruleGroupsNamespaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7babc091249b2b8f07528284ae1ae6c847c2d6a98e06c8e8811e4425107ed0a9)
            check_type(argname="argument rule_groups_namespace_arn", value=rule_groups_namespace_arn, expected_type=type_hints["rule_groups_namespace_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_groups_namespace_arn": rule_groups_namespace_arn,
        }

    @builtins.property
    def rule_groups_namespace_arn(self) -> builtins.str:
        '''The Arn of the RuleGroupsNamespace resource.'''
        result = self._values.get("rule_groups_namespace_arn")
        assert result is not None, "Required property 'rule_groups_namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleGroupsNamespaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_aps.ScraperReference",
    jsii_struct_bases=[],
    name_mapping={"scraper_arn": "scraperArn"},
)
class ScraperReference:
    def __init__(self, *, scraper_arn: builtins.str) -> None:
        '''A reference to a Scraper resource.

        :param scraper_arn: The Arn of the Scraper resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_aps as interfaces_aps
            
            scraper_reference = interfaces_aps.ScraperReference(
                scraper_arn="scraperArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b691c6ec24da852c7fa2138c93c6c122fe42f78d55b29bd6a4dab6f23fbb2a21)
            check_type(argname="argument scraper_arn", value=scraper_arn, expected_type=type_hints["scraper_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scraper_arn": scraper_arn,
        }

    @builtins.property
    def scraper_arn(self) -> builtins.str:
        '''The Arn of the Scraper resource.'''
        result = self._values.get("scraper_arn")
        assert result is not None, "Required property 'scraper_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScraperReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_aps.WorkspaceReference",
    jsii_struct_bases=[],
    name_mapping={"workspace_arn": "workspaceArn"},
)
class WorkspaceReference:
    def __init__(self, *, workspace_arn: builtins.str) -> None:
        '''A reference to a Workspace resource.

        :param workspace_arn: The Arn of the Workspace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_aps as interfaces_aps
            
            workspace_reference = interfaces_aps.WorkspaceReference(
                workspace_arn="workspaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e288d1d5d6e00c7cdc3a91d4e4e579a062e4c6d0cf48b6f3cbc3dd8acf598b7)
            check_type(argname="argument workspace_arn", value=workspace_arn, expected_type=type_hints["workspace_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workspace_arn": workspace_arn,
        }

    @builtins.property
    def workspace_arn(self) -> builtins.str:
        '''The Arn of the Workspace resource.'''
        result = self._values.get("workspace_arn")
        assert result is not None, "Required property 'workspace_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AnomalyDetectorReference",
    "IAnomalyDetectorRef",
    "IResourcePolicyRef",
    "IRuleGroupsNamespaceRef",
    "IScraperRef",
    "IWorkspaceRef",
    "ResourcePolicyReference",
    "RuleGroupsNamespaceReference",
    "ScraperReference",
    "WorkspaceReference",
]

publication.publish()

def _typecheckingstub__8713accc66b6c1a4a61b78d26bd833761032f548f0c6d01a445c484902f3b26b(
    *,
    anomaly_detector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0f24d8ab317c40a83230f293fadb89964bbc2927faa60441cac5180eb7b4008(
    *,
    workspace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7babc091249b2b8f07528284ae1ae6c847c2d6a98e06c8e8811e4425107ed0a9(
    *,
    rule_groups_namespace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b691c6ec24da852c7fa2138c93c6c122fe42f78d55b29bd6a4dab6f23fbb2a21(
    *,
    scraper_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e288d1d5d6e00c7cdc3a91d4e4e579a062e4c6d0cf48b6f3cbc3dd8acf598b7(
    *,
    workspace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAnomalyDetectorRef, IResourcePolicyRef, IRuleGroupsNamespaceRef, IScraperRef, IWorkspaceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
