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
    jsii_type="aws-cdk-lib.interfaces.aws_rds.CustomDBEngineVersionReference",
    jsii_struct_bases=[],
    name_mapping={"engine": "engine", "engine_version": "engineVersion"},
)
class CustomDBEngineVersionReference:
    def __init__(self, *, engine: builtins.str, engine_version: builtins.str) -> None:
        '''A reference to a CustomDBEngineVersion resource.

        :param engine: The Engine of the CustomDBEngineVersion resource.
        :param engine_version: The EngineVersion of the CustomDBEngineVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            custom_dBEngine_version_reference = interfaces_rds.CustomDBEngineVersionReference(
                engine="engine",
                engine_version="engineVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7bfade17c85355120dd78174c103b342d9dc394e0d82f07c3b0783661051259)
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "engine": engine,
            "engine_version": engine_version,
        }

    @builtins.property
    def engine(self) -> builtins.str:
        '''The Engine of the CustomDBEngineVersion resource.'''
        result = self._values.get("engine")
        assert result is not None, "Required property 'engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_version(self) -> builtins.str:
        '''The EngineVersion of the CustomDBEngineVersion resource.'''
        result = self._values.get("engine_version")
        assert result is not None, "Required property 'engine_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomDBEngineVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBClusterParameterGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_cluster_parameter_group_name": "dbClusterParameterGroupName"},
)
class DBClusterParameterGroupReference:
    def __init__(self, *, db_cluster_parameter_group_name: builtins.str) -> None:
        '''A reference to a DBClusterParameterGroup resource.

        :param db_cluster_parameter_group_name: The DBClusterParameterGroupName of the DBClusterParameterGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bCluster_parameter_group_reference = interfaces_rds.DBClusterParameterGroupReference(
                db_cluster_parameter_group_name="dbClusterParameterGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9896b5cafd7ae848283661a59e887ee67fc6c6ea0350d5c62400deca461d09e0)
            check_type(argname="argument db_cluster_parameter_group_name", value=db_cluster_parameter_group_name, expected_type=type_hints["db_cluster_parameter_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_cluster_parameter_group_name": db_cluster_parameter_group_name,
        }

    @builtins.property
    def db_cluster_parameter_group_name(self) -> builtins.str:
        '''The DBClusterParameterGroupName of the DBClusterParameterGroup resource.'''
        result = self._values.get("db_cluster_parameter_group_name")
        assert result is not None, "Required property 'db_cluster_parameter_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBClusterParameterGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBClusterReference",
    jsii_struct_bases=[],
    name_mapping={
        "db_cluster_arn": "dbClusterArn",
        "db_cluster_identifier": "dbClusterIdentifier",
    },
)
class DBClusterReference:
    def __init__(
        self,
        *,
        db_cluster_arn: builtins.str,
        db_cluster_identifier: builtins.str,
    ) -> None:
        '''A reference to a DBCluster resource.

        :param db_cluster_arn: The ARN of the DBCluster resource.
        :param db_cluster_identifier: The DBClusterIdentifier of the DBCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bCluster_reference = interfaces_rds.DBClusterReference(
                db_cluster_arn="dbClusterArn",
                db_cluster_identifier="dbClusterIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0d9199af4b014e2da6fc0770b3d7346a7b33c21d6af9d6fba787a7d1e8903d1)
            check_type(argname="argument db_cluster_arn", value=db_cluster_arn, expected_type=type_hints["db_cluster_arn"])
            check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_cluster_arn": db_cluster_arn,
            "db_cluster_identifier": db_cluster_identifier,
        }

    @builtins.property
    def db_cluster_arn(self) -> builtins.str:
        '''The ARN of the DBCluster resource.'''
        result = self._values.get("db_cluster_arn")
        assert result is not None, "Required property 'db_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_cluster_identifier(self) -> builtins.str:
        '''The DBClusterIdentifier of the DBCluster resource.'''
        result = self._values.get("db_cluster_identifier")
        assert result is not None, "Required property 'db_cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBInstanceReference",
    jsii_struct_bases=[],
    name_mapping={
        "db_instance_arn": "dbInstanceArn",
        "db_instance_identifier": "dbInstanceIdentifier",
    },
)
class DBInstanceReference:
    def __init__(
        self,
        *,
        db_instance_arn: builtins.str,
        db_instance_identifier: builtins.str,
    ) -> None:
        '''A reference to a DBInstance resource.

        :param db_instance_arn: The ARN of the DBInstance resource.
        :param db_instance_identifier: The DBInstanceIdentifier of the DBInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bInstance_reference = interfaces_rds.DBInstanceReference(
                db_instance_arn="dbInstanceArn",
                db_instance_identifier="dbInstanceIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a016ffb60db252672a7b690c1ff8bdd0440fbe200a30b69f6386fd985462485)
            check_type(argname="argument db_instance_arn", value=db_instance_arn, expected_type=type_hints["db_instance_arn"])
            check_type(argname="argument db_instance_identifier", value=db_instance_identifier, expected_type=type_hints["db_instance_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_instance_arn": db_instance_arn,
            "db_instance_identifier": db_instance_identifier,
        }

    @builtins.property
    def db_instance_arn(self) -> builtins.str:
        '''The ARN of the DBInstance resource.'''
        result = self._values.get("db_instance_arn")
        assert result is not None, "Required property 'db_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_instance_identifier(self) -> builtins.str:
        '''The DBInstanceIdentifier of the DBInstance resource.'''
        result = self._values.get("db_instance_identifier")
        assert result is not None, "Required property 'db_instance_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBParameterGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_parameter_group_name": "dbParameterGroupName"},
)
class DBParameterGroupReference:
    def __init__(self, *, db_parameter_group_name: builtins.str) -> None:
        '''A reference to a DBParameterGroup resource.

        :param db_parameter_group_name: The DBParameterGroupName of the DBParameterGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bParameter_group_reference = interfaces_rds.DBParameterGroupReference(
                db_parameter_group_name="dbParameterGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a554bb088b971739df533e28d085e09e9eabc0cc0432e620aec60795527d2bb0)
            check_type(argname="argument db_parameter_group_name", value=db_parameter_group_name, expected_type=type_hints["db_parameter_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_parameter_group_name": db_parameter_group_name,
        }

    @builtins.property
    def db_parameter_group_name(self) -> builtins.str:
        '''The DBParameterGroupName of the DBParameterGroup resource.'''
        result = self._values.get("db_parameter_group_name")
        assert result is not None, "Required property 'db_parameter_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBParameterGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBProxyEndpointReference",
    jsii_struct_bases=[],
    name_mapping={
        "db_proxy_endpoint_arn": "dbProxyEndpointArn",
        "db_proxy_endpoint_name": "dbProxyEndpointName",
    },
)
class DBProxyEndpointReference:
    def __init__(
        self,
        *,
        db_proxy_endpoint_arn: builtins.str,
        db_proxy_endpoint_name: builtins.str,
    ) -> None:
        '''A reference to a DBProxyEndpoint resource.

        :param db_proxy_endpoint_arn: The ARN of the DBProxyEndpoint resource.
        :param db_proxy_endpoint_name: The DBProxyEndpointName of the DBProxyEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bProxy_endpoint_reference = interfaces_rds.DBProxyEndpointReference(
                db_proxy_endpoint_arn="dbProxyEndpointArn",
                db_proxy_endpoint_name="dbProxyEndpointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0970c9814399466a0a3b023028801f89b1ad83035bdfe7c1e8153cbd0786eb3)
            check_type(argname="argument db_proxy_endpoint_arn", value=db_proxy_endpoint_arn, expected_type=type_hints["db_proxy_endpoint_arn"])
            check_type(argname="argument db_proxy_endpoint_name", value=db_proxy_endpoint_name, expected_type=type_hints["db_proxy_endpoint_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_proxy_endpoint_arn": db_proxy_endpoint_arn,
            "db_proxy_endpoint_name": db_proxy_endpoint_name,
        }

    @builtins.property
    def db_proxy_endpoint_arn(self) -> builtins.str:
        '''The ARN of the DBProxyEndpoint resource.'''
        result = self._values.get("db_proxy_endpoint_arn")
        assert result is not None, "Required property 'db_proxy_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_proxy_endpoint_name(self) -> builtins.str:
        '''The DBProxyEndpointName of the DBProxyEndpoint resource.'''
        result = self._values.get("db_proxy_endpoint_name")
        assert result is not None, "Required property 'db_proxy_endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBProxyEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBProxyReference",
    jsii_struct_bases=[],
    name_mapping={"db_proxy_arn": "dbProxyArn", "db_proxy_name": "dbProxyName"},
)
class DBProxyReference:
    def __init__(
        self,
        *,
        db_proxy_arn: builtins.str,
        db_proxy_name: builtins.str,
    ) -> None:
        '''A reference to a DBProxy resource.

        :param db_proxy_arn: The ARN of the DBProxy resource.
        :param db_proxy_name: The DBProxyName of the DBProxy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bProxy_reference = interfaces_rds.DBProxyReference(
                db_proxy_arn="dbProxyArn",
                db_proxy_name="dbProxyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1536737d678c1472624c70912c54a2e84854770ef6f56fe46f9a769f34f6c8f)
            check_type(argname="argument db_proxy_arn", value=db_proxy_arn, expected_type=type_hints["db_proxy_arn"])
            check_type(argname="argument db_proxy_name", value=db_proxy_name, expected_type=type_hints["db_proxy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_proxy_arn": db_proxy_arn,
            "db_proxy_name": db_proxy_name,
        }

    @builtins.property
    def db_proxy_arn(self) -> builtins.str:
        '''The ARN of the DBProxy resource.'''
        result = self._values.get("db_proxy_arn")
        assert result is not None, "Required property 'db_proxy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def db_proxy_name(self) -> builtins.str:
        '''The DBProxyName of the DBProxy resource.'''
        result = self._values.get("db_proxy_name")
        assert result is not None, "Required property 'db_proxy_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBProxyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBProxyTargetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"target_group_arn": "targetGroupArn"},
)
class DBProxyTargetGroupReference:
    def __init__(self, *, target_group_arn: builtins.str) -> None:
        '''A reference to a DBProxyTargetGroup resource.

        :param target_group_arn: The TargetGroupArn of the DBProxyTargetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bProxy_target_group_reference = interfaces_rds.DBProxyTargetGroupReference(
                target_group_arn="targetGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fce08547ba1e9bc3b124d1d56e9a7c1805d414d7a0495fc7edce362719c77f7)
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_group_arn": target_group_arn,
        }

    @builtins.property
    def target_group_arn(self) -> builtins.str:
        '''The TargetGroupArn of the DBProxyTargetGroup resource.'''
        result = self._values.get("target_group_arn")
        assert result is not None, "Required property 'target_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBProxyTargetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBSecurityGroupIngressReference",
    jsii_struct_bases=[],
    name_mapping={"db_security_group_ingress_id": "dbSecurityGroupIngressId"},
)
class DBSecurityGroupIngressReference:
    def __init__(self, *, db_security_group_ingress_id: builtins.str) -> None:
        '''A reference to a DBSecurityGroupIngress resource.

        :param db_security_group_ingress_id: The Id of the DBSecurityGroupIngress resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bSecurity_group_ingress_reference = interfaces_rds.DBSecurityGroupIngressReference(
                db_security_group_ingress_id="dbSecurityGroupIngressId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a6231f0886cc0950955a31296404688cbe41e675f2dd02b2da7d2455e00d1f)
            check_type(argname="argument db_security_group_ingress_id", value=db_security_group_ingress_id, expected_type=type_hints["db_security_group_ingress_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_security_group_ingress_id": db_security_group_ingress_id,
        }

    @builtins.property
    def db_security_group_ingress_id(self) -> builtins.str:
        '''The Id of the DBSecurityGroupIngress resource.'''
        result = self._values.get("db_security_group_ingress_id")
        assert result is not None, "Required property 'db_security_group_ingress_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBSecurityGroupIngressReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBSecurityGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_security_group_id": "dbSecurityGroupId"},
)
class DBSecurityGroupReference:
    def __init__(self, *, db_security_group_id: builtins.str) -> None:
        '''A reference to a DBSecurityGroup resource.

        :param db_security_group_id: The Id of the DBSecurityGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bSecurity_group_reference = interfaces_rds.DBSecurityGroupReference(
                db_security_group_id="dbSecurityGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84e372ab9cd502e82c79b5e4f2517c533a120568fbc6ed5a5221ee80adf364d0)
            check_type(argname="argument db_security_group_id", value=db_security_group_id, expected_type=type_hints["db_security_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_security_group_id": db_security_group_id,
        }

    @builtins.property
    def db_security_group_id(self) -> builtins.str:
        '''The Id of the DBSecurityGroup resource.'''
        result = self._values.get("db_security_group_id")
        assert result is not None, "Required property 'db_security_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBSecurityGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBShardGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_shard_group_identifier": "dbShardGroupIdentifier"},
)
class DBShardGroupReference:
    def __init__(self, *, db_shard_group_identifier: builtins.str) -> None:
        '''A reference to a DBShardGroup resource.

        :param db_shard_group_identifier: The DBShardGroupIdentifier of the DBShardGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bShard_group_reference = interfaces_rds.DBShardGroupReference(
                db_shard_group_identifier="dbShardGroupIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91d929c8e4d92f83b9c6cc71e3e5564785a42844226119589dcd306e909027f8)
            check_type(argname="argument db_shard_group_identifier", value=db_shard_group_identifier, expected_type=type_hints["db_shard_group_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_shard_group_identifier": db_shard_group_identifier,
        }

    @builtins.property
    def db_shard_group_identifier(self) -> builtins.str:
        '''The DBShardGroupIdentifier of the DBShardGroup resource.'''
        result = self._values.get("db_shard_group_identifier")
        assert result is not None, "Required property 'db_shard_group_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBShardGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.DBSubnetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_subnet_group_name": "dbSubnetGroupName"},
)
class DBSubnetGroupReference:
    def __init__(self, *, db_subnet_group_name: builtins.str) -> None:
        '''A reference to a DBSubnetGroup resource.

        :param db_subnet_group_name: The DBSubnetGroupName of the DBSubnetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            d_bSubnet_group_reference = interfaces_rds.DBSubnetGroupReference(
                db_subnet_group_name="dbSubnetGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c64adbab12e5b7d86608b91a80802222b0c76775becee65732d46fa582990ae)
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_subnet_group_name": db_subnet_group_name,
        }

    @builtins.property
    def db_subnet_group_name(self) -> builtins.str:
        '''The DBSubnetGroupName of the DBSubnetGroup resource.'''
        result = self._values.get("db_subnet_group_name")
        assert result is not None, "Required property 'db_subnet_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBSubnetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.EventSubscriptionReference",
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
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            event_subscription_reference = interfaces_rds.EventSubscriptionReference(
                subscription_name="subscriptionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfcbf7f37b191411aee1a15d6306bec8f5f7b9d9ad01efe8dea75d4605802bfe)
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.GlobalClusterReference",
    jsii_struct_bases=[],
    name_mapping={"global_cluster_identifier": "globalClusterIdentifier"},
)
class GlobalClusterReference:
    def __init__(self, *, global_cluster_identifier: builtins.str) -> None:
        '''A reference to a GlobalCluster resource.

        :param global_cluster_identifier: The GlobalClusterIdentifier of the GlobalCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            global_cluster_reference = interfaces_rds.GlobalClusterReference(
                global_cluster_identifier="globalClusterIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a7b8ba8eebee3f5972e82bb96352ae7aeb7db50bb9230b6fd3dc77e25631907)
            check_type(argname="argument global_cluster_identifier", value=global_cluster_identifier, expected_type=type_hints["global_cluster_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_cluster_identifier": global_cluster_identifier,
        }

    @builtins.property
    def global_cluster_identifier(self) -> builtins.str:
        '''The GlobalClusterIdentifier of the GlobalCluster resource.'''
        result = self._values.get("global_cluster_identifier")
        assert result is not None, "Required property 'global_cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlobalClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.ICustomDBEngineVersionRef")
class ICustomDBEngineVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomDBEngineVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customDbEngineVersionRef")
    def custom_db_engine_version_ref(self) -> "CustomDBEngineVersionReference":
        '''(experimental) A reference to a CustomDBEngineVersion resource.

        :stability: experimental
        '''
        ...


class _ICustomDBEngineVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomDBEngineVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.ICustomDBEngineVersionRef"

    @builtins.property
    @jsii.member(jsii_name="customDbEngineVersionRef")
    def custom_db_engine_version_ref(self) -> "CustomDBEngineVersionReference":
        '''(experimental) A reference to a CustomDBEngineVersion resource.

        :stability: experimental
        '''
        return typing.cast("CustomDBEngineVersionReference", jsii.get(self, "customDbEngineVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomDBEngineVersionRef).__jsii_proxy_class__ = lambda : _ICustomDBEngineVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBClusterParameterGroupRef")
class IDBClusterParameterGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBClusterParameterGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupRef")
    def db_cluster_parameter_group_ref(self) -> "DBClusterParameterGroupReference":
        '''(experimental) A reference to a DBClusterParameterGroup resource.

        :stability: experimental
        '''
        ...


class _IDBClusterParameterGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBClusterParameterGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBClusterParameterGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupRef")
    def db_cluster_parameter_group_ref(self) -> "DBClusterParameterGroupReference":
        '''(experimental) A reference to a DBClusterParameterGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBClusterParameterGroupReference", jsii.get(self, "dbClusterParameterGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBClusterParameterGroupRef).__jsii_proxy_class__ = lambda : _IDBClusterParameterGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBClusterRef")
class IDBClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbClusterRef")
    def db_cluster_ref(self) -> "DBClusterReference":
        '''(experimental) A reference to a DBCluster resource.

        :stability: experimental
        '''
        ...


class _IDBClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBClusterRef"

    @builtins.property
    @jsii.member(jsii_name="dbClusterRef")
    def db_cluster_ref(self) -> "DBClusterReference":
        '''(experimental) A reference to a DBCluster resource.

        :stability: experimental
        '''
        return typing.cast("DBClusterReference", jsii.get(self, "dbClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBClusterRef).__jsii_proxy_class__ = lambda : _IDBClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBInstanceRef")
class IDBInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbInstanceRef")
    def db_instance_ref(self) -> "DBInstanceReference":
        '''(experimental) A reference to a DBInstance resource.

        :stability: experimental
        '''
        ...


class _IDBInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="dbInstanceRef")
    def db_instance_ref(self) -> "DBInstanceReference":
        '''(experimental) A reference to a DBInstance resource.

        :stability: experimental
        '''
        return typing.cast("DBInstanceReference", jsii.get(self, "dbInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBInstanceRef).__jsii_proxy_class__ = lambda : _IDBInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBParameterGroupRef")
class IDBParameterGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBParameterGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbParameterGroupRef")
    def db_parameter_group_ref(self) -> "DBParameterGroupReference":
        '''(experimental) A reference to a DBParameterGroup resource.

        :stability: experimental
        '''
        ...


class _IDBParameterGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBParameterGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBParameterGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbParameterGroupRef")
    def db_parameter_group_ref(self) -> "DBParameterGroupReference":
        '''(experimental) A reference to a DBParameterGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBParameterGroupReference", jsii.get(self, "dbParameterGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBParameterGroupRef).__jsii_proxy_class__ = lambda : _IDBParameterGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBProxyEndpointRef")
class IDBProxyEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBProxyEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbProxyEndpointRef")
    def db_proxy_endpoint_ref(self) -> "DBProxyEndpointReference":
        '''(experimental) A reference to a DBProxyEndpoint resource.

        :stability: experimental
        '''
        ...


class _IDBProxyEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBProxyEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBProxyEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="dbProxyEndpointRef")
    def db_proxy_endpoint_ref(self) -> "DBProxyEndpointReference":
        '''(experimental) A reference to a DBProxyEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("DBProxyEndpointReference", jsii.get(self, "dbProxyEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBProxyEndpointRef).__jsii_proxy_class__ = lambda : _IDBProxyEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBProxyRef")
class IDBProxyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBProxy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbProxyRef")
    def db_proxy_ref(self) -> "DBProxyReference":
        '''(experimental) A reference to a DBProxy resource.

        :stability: experimental
        '''
        ...


class _IDBProxyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBProxy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBProxyRef"

    @builtins.property
    @jsii.member(jsii_name="dbProxyRef")
    def db_proxy_ref(self) -> "DBProxyReference":
        '''(experimental) A reference to a DBProxy resource.

        :stability: experimental
        '''
        return typing.cast("DBProxyReference", jsii.get(self, "dbProxyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBProxyRef).__jsii_proxy_class__ = lambda : _IDBProxyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBProxyTargetGroupRef")
class IDBProxyTargetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBProxyTargetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbProxyTargetGroupRef")
    def db_proxy_target_group_ref(self) -> "DBProxyTargetGroupReference":
        '''(experimental) A reference to a DBProxyTargetGroup resource.

        :stability: experimental
        '''
        ...


class _IDBProxyTargetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBProxyTargetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBProxyTargetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbProxyTargetGroupRef")
    def db_proxy_target_group_ref(self) -> "DBProxyTargetGroupReference":
        '''(experimental) A reference to a DBProxyTargetGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBProxyTargetGroupReference", jsii.get(self, "dbProxyTargetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBProxyTargetGroupRef).__jsii_proxy_class__ = lambda : _IDBProxyTargetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBSecurityGroupIngressRef")
class IDBSecurityGroupIngressRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBSecurityGroupIngress.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbSecurityGroupIngressRef")
    def db_security_group_ingress_ref(self) -> "DBSecurityGroupIngressReference":
        '''(experimental) A reference to a DBSecurityGroupIngress resource.

        :stability: experimental
        '''
        ...


class _IDBSecurityGroupIngressRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBSecurityGroupIngress.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBSecurityGroupIngressRef"

    @builtins.property
    @jsii.member(jsii_name="dbSecurityGroupIngressRef")
    def db_security_group_ingress_ref(self) -> "DBSecurityGroupIngressReference":
        '''(experimental) A reference to a DBSecurityGroupIngress resource.

        :stability: experimental
        '''
        return typing.cast("DBSecurityGroupIngressReference", jsii.get(self, "dbSecurityGroupIngressRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBSecurityGroupIngressRef).__jsii_proxy_class__ = lambda : _IDBSecurityGroupIngressRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBSecurityGroupRef")
class IDBSecurityGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBSecurityGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbSecurityGroupRef")
    def db_security_group_ref(self) -> "DBSecurityGroupReference":
        '''(experimental) A reference to a DBSecurityGroup resource.

        :stability: experimental
        '''
        ...


class _IDBSecurityGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBSecurityGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBSecurityGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbSecurityGroupRef")
    def db_security_group_ref(self) -> "DBSecurityGroupReference":
        '''(experimental) A reference to a DBSecurityGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBSecurityGroupReference", jsii.get(self, "dbSecurityGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBSecurityGroupRef).__jsii_proxy_class__ = lambda : _IDBSecurityGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBShardGroupRef")
class IDBShardGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBShardGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbShardGroupRef")
    def db_shard_group_ref(self) -> "DBShardGroupReference":
        '''(experimental) A reference to a DBShardGroup resource.

        :stability: experimental
        '''
        ...


class _IDBShardGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBShardGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBShardGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbShardGroupRef")
    def db_shard_group_ref(self) -> "DBShardGroupReference":
        '''(experimental) A reference to a DBShardGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBShardGroupReference", jsii.get(self, "dbShardGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBShardGroupRef).__jsii_proxy_class__ = lambda : _IDBShardGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IDBSubnetGroupRef")
class IDBSubnetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBSubnetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupRef")
    def db_subnet_group_ref(self) -> "DBSubnetGroupReference":
        '''(experimental) A reference to a DBSubnetGroup resource.

        :stability: experimental
        '''
        ...


class _IDBSubnetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBSubnetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IDBSubnetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupRef")
    def db_subnet_group_ref(self) -> "DBSubnetGroupReference":
        '''(experimental) A reference to a DBSubnetGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBSubnetGroupReference", jsii.get(self, "dbSubnetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBSubnetGroupRef).__jsii_proxy_class__ = lambda : _IDBSubnetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IEventSubscriptionRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IEventSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="eventSubscriptionRef")
    def event_subscription_ref(self) -> "EventSubscriptionReference":
        '''(experimental) A reference to a EventSubscription resource.

        :stability: experimental
        '''
        return typing.cast("EventSubscriptionReference", jsii.get(self, "eventSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventSubscriptionRef).__jsii_proxy_class__ = lambda : _IEventSubscriptionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IGlobalClusterRef")
class IGlobalClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="globalClusterRef")
    def global_cluster_ref(self) -> "GlobalClusterReference":
        '''(experimental) A reference to a GlobalCluster resource.

        :stability: experimental
        '''
        ...


class _IGlobalClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IGlobalClusterRef"

    @builtins.property
    @jsii.member(jsii_name="globalClusterRef")
    def global_cluster_ref(self) -> "GlobalClusterReference":
        '''(experimental) A reference to a GlobalCluster resource.

        :stability: experimental
        '''
        return typing.cast("GlobalClusterReference", jsii.get(self, "globalClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGlobalClusterRef).__jsii_proxy_class__ = lambda : _IGlobalClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IIntegrationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationReference", jsii.get(self, "integrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationRef).__jsii_proxy_class__ = lambda : _IIntegrationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rds.IOptionGroupRef")
class IOptionGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OptionGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="optionGroupRef")
    def option_group_ref(self) -> "OptionGroupReference":
        '''(experimental) A reference to a OptionGroup resource.

        :stability: experimental
        '''
        ...


class _IOptionGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OptionGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rds.IOptionGroupRef"

    @builtins.property
    @jsii.member(jsii_name="optionGroupRef")
    def option_group_ref(self) -> "OptionGroupReference":
        '''(experimental) A reference to a OptionGroup resource.

        :stability: experimental
        '''
        return typing.cast("OptionGroupReference", jsii.get(self, "optionGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOptionGroupRef).__jsii_proxy_class__ = lambda : _IOptionGroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rds.IntegrationReference",
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
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            integration_reference = interfaces_rds.IntegrationReference(
                integration_arn="integrationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d68b7393f509016e8899afca1c60081b2cdc679df5786cb78db816ce2fb54bdb)
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
    jsii_type="aws-cdk-lib.interfaces.aws_rds.OptionGroupReference",
    jsii_struct_bases=[],
    name_mapping={"option_group_name": "optionGroupName"},
)
class OptionGroupReference:
    def __init__(self, *, option_group_name: builtins.str) -> None:
        '''A reference to a OptionGroup resource.

        :param option_group_name: The OptionGroupName of the OptionGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rds as interfaces_rds
            
            option_group_reference = interfaces_rds.OptionGroupReference(
                option_group_name="optionGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e07097ee5cec4d621b125e688e72d708a650095ae041c832d8307f3a22ee46b6)
            check_type(argname="argument option_group_name", value=option_group_name, expected_type=type_hints["option_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "option_group_name": option_group_name,
        }

    @builtins.property
    def option_group_name(self) -> builtins.str:
        '''The OptionGroupName of the OptionGroup resource.'''
        result = self._values.get("option_group_name")
        assert result is not None, "Required property 'option_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OptionGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CustomDBEngineVersionReference",
    "DBClusterParameterGroupReference",
    "DBClusterReference",
    "DBInstanceReference",
    "DBParameterGroupReference",
    "DBProxyEndpointReference",
    "DBProxyReference",
    "DBProxyTargetGroupReference",
    "DBSecurityGroupIngressReference",
    "DBSecurityGroupReference",
    "DBShardGroupReference",
    "DBSubnetGroupReference",
    "EventSubscriptionReference",
    "GlobalClusterReference",
    "ICustomDBEngineVersionRef",
    "IDBClusterParameterGroupRef",
    "IDBClusterRef",
    "IDBInstanceRef",
    "IDBParameterGroupRef",
    "IDBProxyEndpointRef",
    "IDBProxyRef",
    "IDBProxyTargetGroupRef",
    "IDBSecurityGroupIngressRef",
    "IDBSecurityGroupRef",
    "IDBShardGroupRef",
    "IDBSubnetGroupRef",
    "IEventSubscriptionRef",
    "IGlobalClusterRef",
    "IIntegrationRef",
    "IOptionGroupRef",
    "IntegrationReference",
    "OptionGroupReference",
]

publication.publish()

def _typecheckingstub__d7bfade17c85355120dd78174c103b342d9dc394e0d82f07c3b0783661051259(
    *,
    engine: builtins.str,
    engine_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9896b5cafd7ae848283661a59e887ee67fc6c6ea0350d5c62400deca461d09e0(
    *,
    db_cluster_parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0d9199af4b014e2da6fc0770b3d7346a7b33c21d6af9d6fba787a7d1e8903d1(
    *,
    db_cluster_arn: builtins.str,
    db_cluster_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a016ffb60db252672a7b690c1ff8bdd0440fbe200a30b69f6386fd985462485(
    *,
    db_instance_arn: builtins.str,
    db_instance_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a554bb088b971739df533e28d085e09e9eabc0cc0432e620aec60795527d2bb0(
    *,
    db_parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0970c9814399466a0a3b023028801f89b1ad83035bdfe7c1e8153cbd0786eb3(
    *,
    db_proxy_endpoint_arn: builtins.str,
    db_proxy_endpoint_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1536737d678c1472624c70912c54a2e84854770ef6f56fe46f9a769f34f6c8f(
    *,
    db_proxy_arn: builtins.str,
    db_proxy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fce08547ba1e9bc3b124d1d56e9a7c1805d414d7a0495fc7edce362719c77f7(
    *,
    target_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a6231f0886cc0950955a31296404688cbe41e675f2dd02b2da7d2455e00d1f(
    *,
    db_security_group_ingress_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84e372ab9cd502e82c79b5e4f2517c533a120568fbc6ed5a5221ee80adf364d0(
    *,
    db_security_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d929c8e4d92f83b9c6cc71e3e5564785a42844226119589dcd306e909027f8(
    *,
    db_shard_group_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c64adbab12e5b7d86608b91a80802222b0c76775becee65732d46fa582990ae(
    *,
    db_subnet_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfcbf7f37b191411aee1a15d6306bec8f5f7b9d9ad01efe8dea75d4605802bfe(
    *,
    subscription_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a7b8ba8eebee3f5972e82bb96352ae7aeb7db50bb9230b6fd3dc77e25631907(
    *,
    global_cluster_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d68b7393f509016e8899afca1c60081b2cdc679df5786cb78db816ce2fb54bdb(
    *,
    integration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e07097ee5cec4d621b125e688e72d708a650095ae041c832d8307f3a22ee46b6(
    *,
    option_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICustomDBEngineVersionRef, IDBClusterParameterGroupRef, IDBClusterRef, IDBInstanceRef, IDBParameterGroupRef, IDBProxyEndpointRef, IDBProxyRef, IDBProxyTargetGroupRef, IDBSecurityGroupIngressRef, IDBSecurityGroupRef, IDBShardGroupRef, IDBSubnetGroupRef, IEventSubscriptionRef, IGlobalClusterRef, IIntegrationRef, IOptionGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
