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
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.ClusterParameterGroupReference",
    jsii_struct_bases=[],
    name_mapping={"parameter_group_name": "parameterGroupName"},
)
class ClusterParameterGroupReference:
    def __init__(self, *, parameter_group_name: builtins.str) -> None:
        '''A reference to a ClusterParameterGroup resource.

        :param parameter_group_name: The ParameterGroupName of the ClusterParameterGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            cluster_parameter_group_reference = interfaces_redshift.ClusterParameterGroupReference(
                parameter_group_name="parameterGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8207d9739fddf9bee99f46badc5817541c863d35187199e3c41f06b36d513c50)
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_group_name": parameter_group_name,
        }

    @builtins.property
    def parameter_group_name(self) -> builtins.str:
        '''The ParameterGroupName of the ClusterParameterGroup resource.'''
        result = self._values.get("parameter_group_name")
        assert result is not None, "Required property 'parameter_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterParameterGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.ClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_identifier": "clusterIdentifier"},
)
class ClusterReference:
    def __init__(self, *, cluster_identifier: builtins.str) -> None:
        '''A reference to a Cluster resource.

        :param cluster_identifier: The ClusterIdentifier of the Cluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            cluster_reference = interfaces_redshift.ClusterReference(
                cluster_identifier="clusterIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4abec531fe93c1d3d14551c34ebfab9758412e37d9e635dc02aa6d0a1a974f8c)
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_identifier": cluster_identifier,
        }

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''The ClusterIdentifier of the Cluster resource.'''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.ClusterSecurityGroupIngressReference",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_security_group_ingress_id": "clusterSecurityGroupIngressId",
    },
)
class ClusterSecurityGroupIngressReference:
    def __init__(self, *, cluster_security_group_ingress_id: builtins.str) -> None:
        '''A reference to a ClusterSecurityGroupIngress resource.

        :param cluster_security_group_ingress_id: The Id of the ClusterSecurityGroupIngress resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            cluster_security_group_ingress_reference = interfaces_redshift.ClusterSecurityGroupIngressReference(
                cluster_security_group_ingress_id="clusterSecurityGroupIngressId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bf9a11dd59303950537cf82b8bbb4df53e3fb37abb63a9bf7e727b7850f2d68)
            check_type(argname="argument cluster_security_group_ingress_id", value=cluster_security_group_ingress_id, expected_type=type_hints["cluster_security_group_ingress_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_security_group_ingress_id": cluster_security_group_ingress_id,
        }

    @builtins.property
    def cluster_security_group_ingress_id(self) -> builtins.str:
        '''The Id of the ClusterSecurityGroupIngress resource.'''
        result = self._values.get("cluster_security_group_ingress_id")
        assert result is not None, "Required property 'cluster_security_group_ingress_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterSecurityGroupIngressReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.ClusterSecurityGroupReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_security_group_id": "clusterSecurityGroupId"},
)
class ClusterSecurityGroupReference:
    def __init__(self, *, cluster_security_group_id: builtins.str) -> None:
        '''A reference to a ClusterSecurityGroup resource.

        :param cluster_security_group_id: The Id of the ClusterSecurityGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            cluster_security_group_reference = interfaces_redshift.ClusterSecurityGroupReference(
                cluster_security_group_id="clusterSecurityGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e53c92e67edf20766ca87d9586ec5234ca030e908ae52dfdfd245695e403078)
            check_type(argname="argument cluster_security_group_id", value=cluster_security_group_id, expected_type=type_hints["cluster_security_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_security_group_id": cluster_security_group_id,
        }

    @builtins.property
    def cluster_security_group_id(self) -> builtins.str:
        '''The Id of the ClusterSecurityGroup resource.'''
        result = self._values.get("cluster_security_group_id")
        assert result is not None, "Required property 'cluster_security_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterSecurityGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.ClusterSubnetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_subnet_group_name": "clusterSubnetGroupName"},
)
class ClusterSubnetGroupReference:
    def __init__(self, *, cluster_subnet_group_name: builtins.str) -> None:
        '''A reference to a ClusterSubnetGroup resource.

        :param cluster_subnet_group_name: The ClusterSubnetGroupName of the ClusterSubnetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            cluster_subnet_group_reference = interfaces_redshift.ClusterSubnetGroupReference(
                cluster_subnet_group_name="clusterSubnetGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11e00959438c9959adef3f2c6e93f32e22432ff65e25589e85db08fa857637c9)
            check_type(argname="argument cluster_subnet_group_name", value=cluster_subnet_group_name, expected_type=type_hints["cluster_subnet_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_subnet_group_name": cluster_subnet_group_name,
        }

    @builtins.property
    def cluster_subnet_group_name(self) -> builtins.str:
        '''The ClusterSubnetGroupName of the ClusterSubnetGroup resource.'''
        result = self._values.get("cluster_subnet_group_name")
        assert result is not None, "Required property 'cluster_subnet_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterSubnetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.EndpointAccessReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_name": "endpointName"},
)
class EndpointAccessReference:
    def __init__(self, *, endpoint_name: builtins.str) -> None:
        '''A reference to a EndpointAccess resource.

        :param endpoint_name: The EndpointName of the EndpointAccess resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            endpoint_access_reference = interfaces_redshift.EndpointAccessReference(
                endpoint_name="endpointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c61a1ff9c367fde46732b504ac0347d48edbd568f27884b69c96be0e1d65294d)
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_name": endpoint_name,
        }

    @builtins.property
    def endpoint_name(self) -> builtins.str:
        '''The EndpointName of the EndpointAccess resource.'''
        result = self._values.get("endpoint_name")
        assert result is not None, "Required property 'endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointAccessReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.EndpointAuthorizationReference",
    jsii_struct_bases=[],
    name_mapping={"account": "account", "cluster_identifier": "clusterIdentifier"},
)
class EndpointAuthorizationReference:
    def __init__(
        self,
        *,
        account: builtins.str,
        cluster_identifier: builtins.str,
    ) -> None:
        '''A reference to a EndpointAuthorization resource.

        :param account: The Account of the EndpointAuthorization resource.
        :param cluster_identifier: The ClusterIdentifier of the EndpointAuthorization resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            endpoint_authorization_reference = interfaces_redshift.EndpointAuthorizationReference(
                account="account",
                cluster_identifier="clusterIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5086efb4cbf53f01fb1b32c6f932eeab03e8752fcd9ab3e063cbd2de584a32e1)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "cluster_identifier": cluster_identifier,
        }

    @builtins.property
    def account(self) -> builtins.str:
        '''The Account of the EndpointAuthorization resource.'''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_identifier(self) -> builtins.str:
        '''The ClusterIdentifier of the EndpointAuthorization resource.'''
        result = self._values.get("cluster_identifier")
        assert result is not None, "Required property 'cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointAuthorizationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.EventSubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={"subscription_name": "subscriptionName"},
)
class EventSubscriptionReference:
    def __init__(self, *, subscription_name: builtins.str) -> None:
        '''A reference to a EventSubscription resource.

        :param subscription_name: The SubscriptionName of the EventSubscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            event_subscription_reference = interfaces_redshift.EventSubscriptionReference(
                subscription_name="subscriptionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0a4b02a8b85126ef6c2ccf6fa9dc42b082f9c895466223431f5a80642b88925)
            check_type(argname="argument subscription_name", value=subscription_name, expected_type=type_hints["subscription_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscription_name": subscription_name,
        }

    @builtins.property
    def subscription_name(self) -> builtins.str:
        '''The SubscriptionName of the EventSubscription resource.'''
        result = self._values.get("subscription_name")
        assert result is not None, "Required property 'subscription_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventSubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.IClusterParameterGroupRef"
)
class IClusterParameterGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterParameterGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupRef")
    def cluster_parameter_group_ref(self) -> "ClusterParameterGroupReference":
        '''(experimental) A reference to a ClusterParameterGroup resource.

        :stability: experimental
        '''
        ...


class _IClusterParameterGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterParameterGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IClusterParameterGroupRef"

    @builtins.property
    @jsii.member(jsii_name="clusterParameterGroupRef")
    def cluster_parameter_group_ref(self) -> "ClusterParameterGroupReference":
        '''(experimental) A reference to a ClusterParameterGroup resource.

        :stability: experimental
        '''
        return typing.cast("ClusterParameterGroupReference", jsii.get(self, "clusterParameterGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterParameterGroupRef).__jsii_proxy_class__ = lambda : _IClusterParameterGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_redshift.IClusterRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.IClusterSecurityGroupIngressRef"
)
class IClusterSecurityGroupIngressRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterSecurityGroupIngress.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroupIngressRef")
    def cluster_security_group_ingress_ref(
        self,
    ) -> "ClusterSecurityGroupIngressReference":
        '''(experimental) A reference to a ClusterSecurityGroupIngress resource.

        :stability: experimental
        '''
        ...


class _IClusterSecurityGroupIngressRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterSecurityGroupIngress.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IClusterSecurityGroupIngressRef"

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroupIngressRef")
    def cluster_security_group_ingress_ref(
        self,
    ) -> "ClusterSecurityGroupIngressReference":
        '''(experimental) A reference to a ClusterSecurityGroupIngress resource.

        :stability: experimental
        '''
        return typing.cast("ClusterSecurityGroupIngressReference", jsii.get(self, "clusterSecurityGroupIngressRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterSecurityGroupIngressRef).__jsii_proxy_class__ = lambda : _IClusterSecurityGroupIngressRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.IClusterSecurityGroupRef"
)
class IClusterSecurityGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterSecurityGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroupRef")
    def cluster_security_group_ref(self) -> "ClusterSecurityGroupReference":
        '''(experimental) A reference to a ClusterSecurityGroup resource.

        :stability: experimental
        '''
        ...


class _IClusterSecurityGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterSecurityGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IClusterSecurityGroupRef"

    @builtins.property
    @jsii.member(jsii_name="clusterSecurityGroupRef")
    def cluster_security_group_ref(self) -> "ClusterSecurityGroupReference":
        '''(experimental) A reference to a ClusterSecurityGroup resource.

        :stability: experimental
        '''
        return typing.cast("ClusterSecurityGroupReference", jsii.get(self, "clusterSecurityGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterSecurityGroupRef).__jsii_proxy_class__ = lambda : _IClusterSecurityGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_redshift.IClusterSubnetGroupRef")
class IClusterSubnetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterSubnetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterSubnetGroupRef")
    def cluster_subnet_group_ref(self) -> "ClusterSubnetGroupReference":
        '''(experimental) A reference to a ClusterSubnetGroup resource.

        :stability: experimental
        '''
        ...


class _IClusterSubnetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterSubnetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IClusterSubnetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="clusterSubnetGroupRef")
    def cluster_subnet_group_ref(self) -> "ClusterSubnetGroupReference":
        '''(experimental) A reference to a ClusterSubnetGroup resource.

        :stability: experimental
        '''
        return typing.cast("ClusterSubnetGroupReference", jsii.get(self, "clusterSubnetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterSubnetGroupRef).__jsii_proxy_class__ = lambda : _IClusterSubnetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_redshift.IEndpointAccessRef")
class IEndpointAccessRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EndpointAccess.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointAccessRef")
    def endpoint_access_ref(self) -> "EndpointAccessReference":
        '''(experimental) A reference to a EndpointAccess resource.

        :stability: experimental
        '''
        ...


class _IEndpointAccessRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EndpointAccess.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IEndpointAccessRef"

    @builtins.property
    @jsii.member(jsii_name="endpointAccessRef")
    def endpoint_access_ref(self) -> "EndpointAccessReference":
        '''(experimental) A reference to a EndpointAccess resource.

        :stability: experimental
        '''
        return typing.cast("EndpointAccessReference", jsii.get(self, "endpointAccessRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointAccessRef).__jsii_proxy_class__ = lambda : _IEndpointAccessRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.IEndpointAuthorizationRef"
)
class IEndpointAuthorizationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EndpointAuthorization.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointAuthorizationRef")
    def endpoint_authorization_ref(self) -> "EndpointAuthorizationReference":
        '''(experimental) A reference to a EndpointAuthorization resource.

        :stability: experimental
        '''
        ...


class _IEndpointAuthorizationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EndpointAuthorization.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IEndpointAuthorizationRef"

    @builtins.property
    @jsii.member(jsii_name="endpointAuthorizationRef")
    def endpoint_authorization_ref(self) -> "EndpointAuthorizationReference":
        '''(experimental) A reference to a EndpointAuthorization resource.

        :stability: experimental
        '''
        return typing.cast("EndpointAuthorizationReference", jsii.get(self, "endpointAuthorizationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointAuthorizationRef).__jsii_proxy_class__ = lambda : _IEndpointAuthorizationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_redshift.IEventSubscriptionRef")
class IEventSubscriptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventSubscription.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventSubscriptionRef")
    def event_subscription_ref(self) -> "EventSubscriptionReference":
        '''(experimental) A reference to a EventSubscription resource.

        :stability: experimental
        '''
        ...


class _IEventSubscriptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventSubscription.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IEventSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="eventSubscriptionRef")
    def event_subscription_ref(self) -> "EventSubscriptionReference":
        '''(experimental) A reference to a EventSubscription resource.

        :stability: experimental
        '''
        return typing.cast("EventSubscriptionReference", jsii.get(self, "eventSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventSubscriptionRef).__jsii_proxy_class__ = lambda : _IEventSubscriptionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_redshift.IIntegrationRef")
class IIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        ...


class _IIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationReference", jsii.get(self, "integrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationRef).__jsii_proxy_class__ = lambda : _IIntegrationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_redshift.IScheduledActionRef")
class IScheduledActionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledAction.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scheduledActionRef")
    def scheduled_action_ref(self) -> "ScheduledActionReference":
        '''(experimental) A reference to a ScheduledAction resource.

        :stability: experimental
        '''
        ...


class _IScheduledActionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledAction.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshift.IScheduledActionRef"

    @builtins.property
    @jsii.member(jsii_name="scheduledActionRef")
    def scheduled_action_ref(self) -> "ScheduledActionReference":
        '''(experimental) A reference to a ScheduledAction resource.

        :stability: experimental
        '''
        return typing.cast("ScheduledActionReference", jsii.get(self, "scheduledActionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduledActionRef).__jsii_proxy_class__ = lambda : _IScheduledActionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.IntegrationReference",
    jsii_struct_bases=[],
    name_mapping={"integration_arn": "integrationArn"},
)
class IntegrationReference:
    def __init__(self, *, integration_arn: builtins.str) -> None:
        '''A reference to a Integration resource.

        :param integration_arn: The IntegrationArn of the Integration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            integration_reference = interfaces_redshift.IntegrationReference(
                integration_arn="integrationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__728632c7aa139882a2948f73866352d960014a68b5bbba0fa13131ecabe2b548)
            check_type(argname="argument integration_arn", value=integration_arn, expected_type=type_hints["integration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "integration_arn": integration_arn,
        }

    @builtins.property
    def integration_arn(self) -> builtins.str:
        '''The IntegrationArn of the Integration resource.'''
        result = self._values.get("integration_arn")
        assert result is not None, "Required property 'integration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshift.ScheduledActionReference",
    jsii_struct_bases=[],
    name_mapping={"scheduled_action_name": "scheduledActionName"},
)
class ScheduledActionReference:
    def __init__(self, *, scheduled_action_name: builtins.str) -> None:
        '''A reference to a ScheduledAction resource.

        :param scheduled_action_name: The ScheduledActionName of the ScheduledAction resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshift as interfaces_redshift
            
            scheduled_action_reference = interfaces_redshift.ScheduledActionReference(
                scheduled_action_name="scheduledActionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70d902e960d555dbfb1b278976b8cd3991371d19399bfcea38c0af9308c1ce6f)
            check_type(argname="argument scheduled_action_name", value=scheduled_action_name, expected_type=type_hints["scheduled_action_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scheduled_action_name": scheduled_action_name,
        }

    @builtins.property
    def scheduled_action_name(self) -> builtins.str:
        '''The ScheduledActionName of the ScheduledAction resource.'''
        result = self._values.get("scheduled_action_name")
        assert result is not None, "Required property 'scheduled_action_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduledActionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ClusterParameterGroupReference",
    "ClusterReference",
    "ClusterSecurityGroupIngressReference",
    "ClusterSecurityGroupReference",
    "ClusterSubnetGroupReference",
    "EndpointAccessReference",
    "EndpointAuthorizationReference",
    "EventSubscriptionReference",
    "IClusterParameterGroupRef",
    "IClusterRef",
    "IClusterSecurityGroupIngressRef",
    "IClusterSecurityGroupRef",
    "IClusterSubnetGroupRef",
    "IEndpointAccessRef",
    "IEndpointAuthorizationRef",
    "IEventSubscriptionRef",
    "IIntegrationRef",
    "IScheduledActionRef",
    "IntegrationReference",
    "ScheduledActionReference",
]

publication.publish()

def _typecheckingstub__8207d9739fddf9bee99f46badc5817541c863d35187199e3c41f06b36d513c50(
    *,
    parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4abec531fe93c1d3d14551c34ebfab9758412e37d9e635dc02aa6d0a1a974f8c(
    *,
    cluster_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bf9a11dd59303950537cf82b8bbb4df53e3fb37abb63a9bf7e727b7850f2d68(
    *,
    cluster_security_group_ingress_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e53c92e67edf20766ca87d9586ec5234ca030e908ae52dfdfd245695e403078(
    *,
    cluster_security_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e00959438c9959adef3f2c6e93f32e22432ff65e25589e85db08fa857637c9(
    *,
    cluster_subnet_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c61a1ff9c367fde46732b504ac0347d48edbd568f27884b69c96be0e1d65294d(
    *,
    endpoint_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5086efb4cbf53f01fb1b32c6f932eeab03e8752fcd9ab3e063cbd2de584a32e1(
    *,
    account: builtins.str,
    cluster_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0a4b02a8b85126ef6c2ccf6fa9dc42b082f9c895466223431f5a80642b88925(
    *,
    subscription_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__728632c7aa139882a2948f73866352d960014a68b5bbba0fa13131ecabe2b548(
    *,
    integration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70d902e960d555dbfb1b278976b8cd3991371d19399bfcea38c0af9308c1ce6f(
    *,
    scheduled_action_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IClusterParameterGroupRef, IClusterRef, IClusterSecurityGroupIngressRef, IClusterSecurityGroupRef, IClusterSubnetGroupRef, IEndpointAccessRef, IEndpointAuthorizationRef, IEventSubscriptionRef, IIntegrationRef, IScheduledActionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
