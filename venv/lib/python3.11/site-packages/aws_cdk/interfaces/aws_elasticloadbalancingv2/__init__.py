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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.IListenerCertificateRef"
)
class IListenerCertificateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ListenerCertificate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="listenerCertificateRef")
    def listener_certificate_ref(self) -> "ListenerCertificateReference":
        '''(experimental) A reference to a ListenerCertificate resource.

        :stability: experimental
        '''
        ...


class _IListenerCertificateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ListenerCertificate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.IListenerCertificateRef"

    @builtins.property
    @jsii.member(jsii_name="listenerCertificateRef")
    def listener_certificate_ref(self) -> "ListenerCertificateReference":
        '''(experimental) A reference to a ListenerCertificate resource.

        :stability: experimental
        '''
        return typing.cast("ListenerCertificateReference", jsii.get(self, "listenerCertificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IListenerCertificateRef).__jsii_proxy_class__ = lambda : _IListenerCertificateRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.IListenerRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.IListenerRef"

    @builtins.property
    @jsii.member(jsii_name="listenerRef")
    def listener_ref(self) -> "ListenerReference":
        '''(experimental) A reference to a Listener resource.

        :stability: experimental
        '''
        return typing.cast("ListenerReference", jsii.get(self, "listenerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IListenerRef).__jsii_proxy_class__ = lambda : _IListenerRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.IListenerRuleRef"
)
class IListenerRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ListenerRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="listenerRuleRef")
    def listener_rule_ref(self) -> "ListenerRuleReference":
        '''(experimental) A reference to a ListenerRule resource.

        :stability: experimental
        '''
        ...


class _IListenerRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ListenerRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.IListenerRuleRef"

    @builtins.property
    @jsii.member(jsii_name="listenerRuleRef")
    def listener_rule_ref(self) -> "ListenerRuleReference":
        '''(experimental) A reference to a ListenerRule resource.

        :stability: experimental
        '''
        return typing.cast("ListenerRuleReference", jsii.get(self, "listenerRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IListenerRuleRef).__jsii_proxy_class__ = lambda : _IListenerRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ILoadBalancerRef"
)
class ILoadBalancerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LoadBalancer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="loadBalancerRef")
    def load_balancer_ref(self) -> "LoadBalancerReference":
        '''(experimental) A reference to a LoadBalancer resource.

        :stability: experimental
        '''
        ...


class _ILoadBalancerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LoadBalancer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ILoadBalancerRef"

    @builtins.property
    @jsii.member(jsii_name="loadBalancerRef")
    def load_balancer_ref(self) -> "LoadBalancerReference":
        '''(experimental) A reference to a LoadBalancer resource.

        :stability: experimental
        '''
        return typing.cast("LoadBalancerReference", jsii.get(self, "loadBalancerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoadBalancerRef).__jsii_proxy_class__ = lambda : _ILoadBalancerRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ITargetGroupRef"
)
class ITargetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TargetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="targetGroupRef")
    def target_group_ref(self) -> "TargetGroupReference":
        '''(experimental) A reference to a TargetGroup resource.

        :stability: experimental
        '''
        ...


class _ITargetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TargetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ITargetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="targetGroupRef")
    def target_group_ref(self) -> "TargetGroupReference":
        '''(experimental) A reference to a TargetGroup resource.

        :stability: experimental
        '''
        return typing.cast("TargetGroupReference", jsii.get(self, "targetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITargetGroupRef).__jsii_proxy_class__ = lambda : _ITargetGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ITrustStoreRef"
)
class ITrustStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrustStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trustStoreRef")
    def trust_store_ref(self) -> "TrustStoreReference":
        '''(experimental) A reference to a TrustStore resource.

        :stability: experimental
        '''
        ...


class _ITrustStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrustStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ITrustStoreRef"

    @builtins.property
    @jsii.member(jsii_name="trustStoreRef")
    def trust_store_ref(self) -> "TrustStoreReference":
        '''(experimental) A reference to a TrustStore resource.

        :stability: experimental
        '''
        return typing.cast("TrustStoreReference", jsii.get(self, "trustStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrustStoreRef).__jsii_proxy_class__ = lambda : _ITrustStoreRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ITrustStoreRevocationRef"
)
class ITrustStoreRevocationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrustStoreRevocation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trustStoreRevocationRef")
    def trust_store_revocation_ref(self) -> "TrustStoreRevocationReference":
        '''(experimental) A reference to a TrustStoreRevocation resource.

        :stability: experimental
        '''
        ...


class _ITrustStoreRevocationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrustStoreRevocation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ITrustStoreRevocationRef"

    @builtins.property
    @jsii.member(jsii_name="trustStoreRevocationRef")
    def trust_store_revocation_ref(self) -> "TrustStoreRevocationReference":
        '''(experimental) A reference to a TrustStoreRevocation resource.

        :stability: experimental
        '''
        return typing.cast("TrustStoreRevocationReference", jsii.get(self, "trustStoreRevocationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrustStoreRevocationRef).__jsii_proxy_class__ = lambda : _ITrustStoreRevocationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ListenerCertificateReference",
    jsii_struct_bases=[],
    name_mapping={"listener_certificate_id": "listenerCertificateId"},
)
class ListenerCertificateReference:
    def __init__(self, *, listener_certificate_id: builtins.str) -> None:
        '''A reference to a ListenerCertificate resource.

        :param listener_certificate_id: The Id of the ListenerCertificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticloadbalancingv2 as interfaces_elasticloadbalancingv2
            
            listener_certificate_reference = interfaces_elasticloadbalancingv2.ListenerCertificateReference(
                listener_certificate_id="listenerCertificateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a0f627c45f1fa15ce4cb3b6894884ccc089f00898e6692396fc44a02e1a9c14)
            check_type(argname="argument listener_certificate_id", value=listener_certificate_id, expected_type=type_hints["listener_certificate_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "listener_certificate_id": listener_certificate_id,
        }

    @builtins.property
    def listener_certificate_id(self) -> builtins.str:
        '''The Id of the ListenerCertificate resource.'''
        result = self._values.get("listener_certificate_id")
        assert result is not None, "Required property 'listener_certificate_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListenerCertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ListenerReference",
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
            from aws_cdk.interfaces import aws_elasticloadbalancingv2 as interfaces_elasticloadbalancingv2
            
            listener_reference = interfaces_elasticloadbalancingv2.ListenerReference(
                listener_arn="listenerArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e889518a9cc05c1abb37d37b4483209c502a1998953978b22d19a24491c24737)
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.ListenerRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class ListenerRuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a ListenerRule resource.

        :param rule_arn: The RuleArn of the ListenerRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticloadbalancingv2 as interfaces_elasticloadbalancingv2
            
            listener_rule_reference = interfaces_elasticloadbalancingv2.ListenerRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0523e483c2f76fde768fac1b0203887b9c24dcf1df4ebbcc5a29810a297de64f)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the ListenerRule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListenerRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.LoadBalancerReference",
    jsii_struct_bases=[],
    name_mapping={"load_balancer_arn": "loadBalancerArn"},
)
class LoadBalancerReference:
    def __init__(self, *, load_balancer_arn: builtins.str) -> None:
        '''A reference to a LoadBalancer resource.

        :param load_balancer_arn: The LoadBalancerArn of the LoadBalancer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticloadbalancingv2 as interfaces_elasticloadbalancingv2
            
            load_balancer_reference = interfaces_elasticloadbalancingv2.LoadBalancerReference(
                load_balancer_arn="loadBalancerArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3931ac7eed267577311b953cecd37052afad6ec0844b0a5f6c22be554d498d4)
            check_type(argname="argument load_balancer_arn", value=load_balancer_arn, expected_type=type_hints["load_balancer_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "load_balancer_arn": load_balancer_arn,
        }

    @builtins.property
    def load_balancer_arn(self) -> builtins.str:
        '''The LoadBalancerArn of the LoadBalancer resource.'''
        result = self._values.get("load_balancer_arn")
        assert result is not None, "Required property 'load_balancer_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.TargetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"target_group_arn": "targetGroupArn"},
)
class TargetGroupReference:
    def __init__(self, *, target_group_arn: builtins.str) -> None:
        '''A reference to a TargetGroup resource.

        :param target_group_arn: The TargetGroupArn of the TargetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticloadbalancingv2 as interfaces_elasticloadbalancingv2
            
            target_group_reference = interfaces_elasticloadbalancingv2.TargetGroupReference(
                target_group_arn="targetGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b59eb018be916de3873b108f25ffb8ec4b49de6d705244946b7c65db73b3a33)
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_group_arn": target_group_arn,
        }

    @builtins.property
    def target_group_arn(self) -> builtins.str:
        '''The TargetGroupArn of the TargetGroup resource.'''
        result = self._values.get("target_group_arn")
        assert result is not None, "Required property 'target_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.TrustStoreReference",
    jsii_struct_bases=[],
    name_mapping={"trust_store_arn": "trustStoreArn"},
)
class TrustStoreReference:
    def __init__(self, *, trust_store_arn: builtins.str) -> None:
        '''A reference to a TrustStore resource.

        :param trust_store_arn: The TrustStoreArn of the TrustStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticloadbalancingv2 as interfaces_elasticloadbalancingv2
            
            trust_store_reference = interfaces_elasticloadbalancingv2.TrustStoreReference(
                trust_store_arn="trustStoreArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fb209663a87cc12a95e9fd21f7df8458757069f54c96874bd177dc6c053a3e3)
            check_type(argname="argument trust_store_arn", value=trust_store_arn, expected_type=type_hints["trust_store_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trust_store_arn": trust_store_arn,
        }

    @builtins.property
    def trust_store_arn(self) -> builtins.str:
        '''The TrustStoreArn of the TrustStore resource.'''
        result = self._values.get("trust_store_arn")
        assert result is not None, "Required property 'trust_store_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrustStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancingv2.TrustStoreRevocationReference",
    jsii_struct_bases=[],
    name_mapping={"revocation_id": "revocationId", "trust_store_arn": "trustStoreArn"},
)
class TrustStoreRevocationReference:
    def __init__(
        self,
        *,
        revocation_id: builtins.str,
        trust_store_arn: builtins.str,
    ) -> None:
        '''A reference to a TrustStoreRevocation resource.

        :param revocation_id: The RevocationId of the TrustStoreRevocation resource.
        :param trust_store_arn: The TrustStoreArn of the TrustStoreRevocation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticloadbalancingv2 as interfaces_elasticloadbalancingv2
            
            trust_store_revocation_reference = interfaces_elasticloadbalancingv2.TrustStoreRevocationReference(
                revocation_id="revocationId",
                trust_store_arn="trustStoreArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__559a77bf18b3fb0747c04ffb929025983437a66322509a5fa856cdcbebce044a)
            check_type(argname="argument revocation_id", value=revocation_id, expected_type=type_hints["revocation_id"])
            check_type(argname="argument trust_store_arn", value=trust_store_arn, expected_type=type_hints["trust_store_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "revocation_id": revocation_id,
            "trust_store_arn": trust_store_arn,
        }

    @builtins.property
    def revocation_id(self) -> builtins.str:
        '''The RevocationId of the TrustStoreRevocation resource.'''
        result = self._values.get("revocation_id")
        assert result is not None, "Required property 'revocation_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trust_store_arn(self) -> builtins.str:
        '''The TrustStoreArn of the TrustStoreRevocation resource.'''
        result = self._values.get("trust_store_arn")
        assert result is not None, "Required property 'trust_store_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrustStoreRevocationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IListenerCertificateRef",
    "IListenerRef",
    "IListenerRuleRef",
    "ILoadBalancerRef",
    "ITargetGroupRef",
    "ITrustStoreRef",
    "ITrustStoreRevocationRef",
    "ListenerCertificateReference",
    "ListenerReference",
    "ListenerRuleReference",
    "LoadBalancerReference",
    "TargetGroupReference",
    "TrustStoreReference",
    "TrustStoreRevocationReference",
]

publication.publish()

def _typecheckingstub__5a0f627c45f1fa15ce4cb3b6894884ccc089f00898e6692396fc44a02e1a9c14(
    *,
    listener_certificate_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e889518a9cc05c1abb37d37b4483209c502a1998953978b22d19a24491c24737(
    *,
    listener_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0523e483c2f76fde768fac1b0203887b9c24dcf1df4ebbcc5a29810a297de64f(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3931ac7eed267577311b953cecd37052afad6ec0844b0a5f6c22be554d498d4(
    *,
    load_balancer_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b59eb018be916de3873b108f25ffb8ec4b49de6d705244946b7c65db73b3a33(
    *,
    target_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fb209663a87cc12a95e9fd21f7df8458757069f54c96874bd177dc6c053a3e3(
    *,
    trust_store_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__559a77bf18b3fb0747c04ffb929025983437a66322509a5fa856cdcbebce044a(
    *,
    revocation_id: builtins.str,
    trust_store_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IListenerCertificateRef, IListenerRef, IListenerRuleRef, ILoadBalancerRef, ITargetGroupRef, ITrustStoreRef, ITrustStoreRevocationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
