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
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.AlarmReference",
    jsii_struct_bases=[],
    name_mapping={"alarm_arn": "alarmArn", "alarm_name": "alarmName"},
)
class AlarmReference:
    def __init__(self, *, alarm_arn: builtins.str, alarm_name: builtins.str) -> None:
        '''A reference to a Alarm resource.

        :param alarm_arn: The ARN of the Alarm resource.
        :param alarm_name: The AlarmName of the Alarm resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            alarm_reference = interfaces_lightsail.AlarmReference(
                alarm_arn="alarmArn",
                alarm_name="alarmName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__337db78caea804686655f59ca18d9b791d909166130cf6acd0d12c194333f0c2)
            check_type(argname="argument alarm_arn", value=alarm_arn, expected_type=type_hints["alarm_arn"])
            check_type(argname="argument alarm_name", value=alarm_name, expected_type=type_hints["alarm_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_arn": alarm_arn,
            "alarm_name": alarm_name,
        }

    @builtins.property
    def alarm_arn(self) -> builtins.str:
        '''The ARN of the Alarm resource.'''
        result = self._values.get("alarm_arn")
        assert result is not None, "Required property 'alarm_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarm_name(self) -> builtins.str:
        '''The AlarmName of the Alarm resource.'''
        result = self._values.get("alarm_name")
        assert result is not None, "Required property 'alarm_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.BucketReference",
    jsii_struct_bases=[],
    name_mapping={"bucket_arn": "bucketArn", "bucket_name": "bucketName"},
)
class BucketReference:
    def __init__(self, *, bucket_arn: builtins.str, bucket_name: builtins.str) -> None:
        '''A reference to a Bucket resource.

        :param bucket_arn: The ARN of the Bucket resource.
        :param bucket_name: The BucketName of the Bucket resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            bucket_reference = interfaces_lightsail.BucketReference(
                bucket_arn="bucketArn",
                bucket_name="bucketName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dfc3535ced0257498de71d28519b6135ff8f0011c01d7ca3dbb35006683b40d)
            check_type(argname="argument bucket_arn", value=bucket_arn, expected_type=type_hints["bucket_arn"])
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_arn": bucket_arn,
            "bucket_name": bucket_name,
        }

    @builtins.property
    def bucket_arn(self) -> builtins.str:
        '''The ARN of the Bucket resource.'''
        result = self._values.get("bucket_arn")
        assert result is not None, "Required property 'bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The BucketName of the Bucket resource.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BucketReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.CertificateReference",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_arn": "certificateArn",
        "certificate_name": "certificateName",
    },
)
class CertificateReference:
    def __init__(
        self,
        *,
        certificate_arn: builtins.str,
        certificate_name: builtins.str,
    ) -> None:
        '''A reference to a Certificate resource.

        :param certificate_arn: The ARN of the Certificate resource.
        :param certificate_name: The CertificateName of the Certificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            certificate_reference = interfaces_lightsail.CertificateReference(
                certificate_arn="certificateArn",
                certificate_name="certificateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85079d2811b5a242a5ac3874f382d167649d814db74404924e6c368a4279aa68)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
            "certificate_name": certificate_name,
        }

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''The ARN of the Certificate resource.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_name(self) -> builtins.str:
        '''The CertificateName of the Certificate resource.'''
        result = self._values.get("certificate_name")
        assert result is not None, "Required property 'certificate_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.ContainerReference",
    jsii_struct_bases=[],
    name_mapping={"container_arn": "containerArn", "service_name": "serviceName"},
)
class ContainerReference:
    def __init__(
        self,
        *,
        container_arn: builtins.str,
        service_name: builtins.str,
    ) -> None:
        '''A reference to a Container resource.

        :param container_arn: The ARN of the Container resource.
        :param service_name: The ServiceName of the Container resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            container_reference = interfaces_lightsail.ContainerReference(
                container_arn="containerArn",
                service_name="serviceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2efffe0c15cd40bc6850a2bea53cdf7dfbb4d18160dd7603e200d869ac45fc4a)
            check_type(argname="argument container_arn", value=container_arn, expected_type=type_hints["container_arn"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_arn": container_arn,
            "service_name": service_name,
        }

    @builtins.property
    def container_arn(self) -> builtins.str:
        '''The ARN of the Container resource.'''
        result = self._values.get("container_arn")
        assert result is not None, "Required property 'container_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_name(self) -> builtins.str:
        '''The ServiceName of the Container resource.'''
        result = self._values.get("service_name")
        assert result is not None, "Required property 'service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.DatabaseReference",
    jsii_struct_bases=[],
    name_mapping={
        "database_arn": "databaseArn",
        "relational_database_name": "relationalDatabaseName",
    },
)
class DatabaseReference:
    def __init__(
        self,
        *,
        database_arn: builtins.str,
        relational_database_name: builtins.str,
    ) -> None:
        '''A reference to a Database resource.

        :param database_arn: The ARN of the Database resource.
        :param relational_database_name: The RelationalDatabaseName of the Database resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            database_reference = interfaces_lightsail.DatabaseReference(
                database_arn="databaseArn",
                relational_database_name="relationalDatabaseName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70ccc827d1fd7d7e85890ebbac083c9ca9e853e21bdda3342eea1846876a1fbb)
            check_type(argname="argument database_arn", value=database_arn, expected_type=type_hints["database_arn"])
            check_type(argname="argument relational_database_name", value=relational_database_name, expected_type=type_hints["relational_database_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_arn": database_arn,
            "relational_database_name": relational_database_name,
        }

    @builtins.property
    def database_arn(self) -> builtins.str:
        '''The ARN of the Database resource.'''
        result = self._values.get("database_arn")
        assert result is not None, "Required property 'database_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_name(self) -> builtins.str:
        '''The RelationalDatabaseName of the Database resource.'''
        result = self._values.get("relational_database_name")
        assert result is not None, "Required property 'relational_database_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.DatabaseSnapshotReference",
    jsii_struct_bases=[],
    name_mapping={
        "database_snapshot_arn": "databaseSnapshotArn",
        "relational_database_snapshot_name": "relationalDatabaseSnapshotName",
    },
)
class DatabaseSnapshotReference:
    def __init__(
        self,
        *,
        database_snapshot_arn: builtins.str,
        relational_database_snapshot_name: builtins.str,
    ) -> None:
        '''A reference to a DatabaseSnapshot resource.

        :param database_snapshot_arn: The ARN of the DatabaseSnapshot resource.
        :param relational_database_snapshot_name: The RelationalDatabaseSnapshotName of the DatabaseSnapshot resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            database_snapshot_reference = interfaces_lightsail.DatabaseSnapshotReference(
                database_snapshot_arn="databaseSnapshotArn",
                relational_database_snapshot_name="relationalDatabaseSnapshotName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__502d7f0d341a4f9923c01b4d2389b077e255ea4beef655b8efc3498fa2ded806)
            check_type(argname="argument database_snapshot_arn", value=database_snapshot_arn, expected_type=type_hints["database_snapshot_arn"])
            check_type(argname="argument relational_database_snapshot_name", value=relational_database_snapshot_name, expected_type=type_hints["relational_database_snapshot_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_snapshot_arn": database_snapshot_arn,
            "relational_database_snapshot_name": relational_database_snapshot_name,
        }

    @builtins.property
    def database_snapshot_arn(self) -> builtins.str:
        '''The ARN of the DatabaseSnapshot resource.'''
        result = self._values.get("database_snapshot_arn")
        assert result is not None, "Required property 'database_snapshot_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relational_database_snapshot_name(self) -> builtins.str:
        '''The RelationalDatabaseSnapshotName of the DatabaseSnapshot resource.'''
        result = self._values.get("relational_database_snapshot_name")
        assert result is not None, "Required property 'relational_database_snapshot_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseSnapshotReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.DiskReference",
    jsii_struct_bases=[],
    name_mapping={"disk_arn": "diskArn", "disk_name": "diskName"},
)
class DiskReference:
    def __init__(self, *, disk_arn: builtins.str, disk_name: builtins.str) -> None:
        '''A reference to a Disk resource.

        :param disk_arn: The ARN of the Disk resource.
        :param disk_name: The DiskName of the Disk resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            disk_reference = interfaces_lightsail.DiskReference(
                disk_arn="diskArn",
                disk_name="diskName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d411b3610244e9363a0cc69ad0c7a7390c87c80f57f88aefac603d40e1f6523)
            check_type(argname="argument disk_arn", value=disk_arn, expected_type=type_hints["disk_arn"])
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "disk_arn": disk_arn,
            "disk_name": disk_name,
        }

    @builtins.property
    def disk_arn(self) -> builtins.str:
        '''The ARN of the Disk resource.'''
        result = self._values.get("disk_arn")
        assert result is not None, "Required property 'disk_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''The DiskName of the Disk resource.'''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiskReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.DiskSnapshotReference",
    jsii_struct_bases=[],
    name_mapping={
        "disk_snapshot_arn": "diskSnapshotArn",
        "disk_snapshot_name": "diskSnapshotName",
    },
)
class DiskSnapshotReference:
    def __init__(
        self,
        *,
        disk_snapshot_arn: builtins.str,
        disk_snapshot_name: builtins.str,
    ) -> None:
        '''A reference to a DiskSnapshot resource.

        :param disk_snapshot_arn: The ARN of the DiskSnapshot resource.
        :param disk_snapshot_name: The DiskSnapshotName of the DiskSnapshot resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            disk_snapshot_reference = interfaces_lightsail.DiskSnapshotReference(
                disk_snapshot_arn="diskSnapshotArn",
                disk_snapshot_name="diskSnapshotName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__972211f0d06a11bf7c410ddec0712399cab822fca0b46f74a95ab48068278f65)
            check_type(argname="argument disk_snapshot_arn", value=disk_snapshot_arn, expected_type=type_hints["disk_snapshot_arn"])
            check_type(argname="argument disk_snapshot_name", value=disk_snapshot_name, expected_type=type_hints["disk_snapshot_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "disk_snapshot_arn": disk_snapshot_arn,
            "disk_snapshot_name": disk_snapshot_name,
        }

    @builtins.property
    def disk_snapshot_arn(self) -> builtins.str:
        '''The ARN of the DiskSnapshot resource.'''
        result = self._values.get("disk_snapshot_arn")
        assert result is not None, "Required property 'disk_snapshot_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_snapshot_name(self) -> builtins.str:
        '''The DiskSnapshotName of the DiskSnapshot resource.'''
        result = self._values.get("disk_snapshot_name")
        assert result is not None, "Required property 'disk_snapshot_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiskSnapshotReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.DistributionReference",
    jsii_struct_bases=[],
    name_mapping={
        "distribution_arn": "distributionArn",
        "distribution_name": "distributionName",
    },
)
class DistributionReference:
    def __init__(
        self,
        *,
        distribution_arn: builtins.str,
        distribution_name: builtins.str,
    ) -> None:
        '''A reference to a Distribution resource.

        :param distribution_arn: The ARN of the Distribution resource.
        :param distribution_name: The DistributionName of the Distribution resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            distribution_reference = interfaces_lightsail.DistributionReference(
                distribution_arn="distributionArn",
                distribution_name="distributionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b247d312271c3bfbb9c42e90def612cd292f008d73422668b44ace152e12d4c2)
            check_type(argname="argument distribution_arn", value=distribution_arn, expected_type=type_hints["distribution_arn"])
            check_type(argname="argument distribution_name", value=distribution_name, expected_type=type_hints["distribution_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "distribution_arn": distribution_arn,
            "distribution_name": distribution_name,
        }

    @builtins.property
    def distribution_arn(self) -> builtins.str:
        '''The ARN of the Distribution resource.'''
        result = self._values.get("distribution_arn")
        assert result is not None, "Required property 'distribution_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def distribution_name(self) -> builtins.str:
        '''The DistributionName of the Distribution resource.'''
        result = self._values.get("distribution_name")
        assert result is not None, "Required property 'distribution_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DistributionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.DomainReference",
    jsii_struct_bases=[],
    name_mapping={"domain_arn": "domainArn", "domain_name": "domainName"},
)
class DomainReference:
    def __init__(self, *, domain_arn: builtins.str, domain_name: builtins.str) -> None:
        '''A reference to a Domain resource.

        :param domain_arn: The ARN of the Domain resource.
        :param domain_name: The DomainName of the Domain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            domain_reference = interfaces_lightsail.DomainReference(
                domain_arn="domainArn",
                domain_name="domainName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1937efb4450a1e8a57eda9cc5f774d90626a974013ce20020bc4d13173e99968)
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_arn": domain_arn,
            "domain_name": domain_name,
        }

    @builtins.property
    def domain_arn(self) -> builtins.str:
        '''The ARN of the Domain resource.'''
        result = self._values.get("domain_arn")
        assert result is not None, "Required property 'domain_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the Domain resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IAlarmRef")
class IAlarmRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Alarm.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="alarmRef")
    def alarm_ref(self) -> "AlarmReference":
        '''(experimental) A reference to a Alarm resource.

        :stability: experimental
        '''
        ...


class _IAlarmRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Alarm.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IAlarmRef"

    @builtins.property
    @jsii.member(jsii_name="alarmRef")
    def alarm_ref(self) -> "AlarmReference":
        '''(experimental) A reference to a Alarm resource.

        :stability: experimental
        '''
        return typing.cast("AlarmReference", jsii.get(self, "alarmRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarmRef).__jsii_proxy_class__ = lambda : _IAlarmRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IBucketRef")
class IBucketRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Bucket.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="bucketRef")
    def bucket_ref(self) -> "BucketReference":
        '''(experimental) A reference to a Bucket resource.

        :stability: experimental
        '''
        ...


class _IBucketRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Bucket.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IBucketRef"

    @builtins.property
    @jsii.member(jsii_name="bucketRef")
    def bucket_ref(self) -> "BucketReference":
        '''(experimental) A reference to a Bucket resource.

        :stability: experimental
        '''
        return typing.cast("BucketReference", jsii.get(self, "bucketRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBucketRef).__jsii_proxy_class__ = lambda : _IBucketRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.ICertificateRef")
class ICertificateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Certificate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        ...


class _ICertificateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Certificate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.ICertificateRef"

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        return typing.cast("CertificateReference", jsii.get(self, "certificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateRef).__jsii_proxy_class__ = lambda : _ICertificateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IContainerRef")
class IContainerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Container.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="containerRef")
    def container_ref(self) -> "ContainerReference":
        '''(experimental) A reference to a Container resource.

        :stability: experimental
        '''
        ...


class _IContainerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Container.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IContainerRef"

    @builtins.property
    @jsii.member(jsii_name="containerRef")
    def container_ref(self) -> "ContainerReference":
        '''(experimental) A reference to a Container resource.

        :stability: experimental
        '''
        return typing.cast("ContainerReference", jsii.get(self, "containerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContainerRef).__jsii_proxy_class__ = lambda : _IContainerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IDatabaseRef")
class IDatabaseRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Database.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="databaseRef")
    def database_ref(self) -> "DatabaseReference":
        '''(experimental) A reference to a Database resource.

        :stability: experimental
        '''
        ...


class _IDatabaseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Database.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IDatabaseRef"

    @builtins.property
    @jsii.member(jsii_name="databaseRef")
    def database_ref(self) -> "DatabaseReference":
        '''(experimental) A reference to a Database resource.

        :stability: experimental
        '''
        return typing.cast("DatabaseReference", jsii.get(self, "databaseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseRef).__jsii_proxy_class__ = lambda : _IDatabaseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IDatabaseSnapshotRef")
class IDatabaseSnapshotRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DatabaseSnapshot.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="databaseSnapshotRef")
    def database_snapshot_ref(self) -> "DatabaseSnapshotReference":
        '''(experimental) A reference to a DatabaseSnapshot resource.

        :stability: experimental
        '''
        ...


class _IDatabaseSnapshotRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DatabaseSnapshot.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IDatabaseSnapshotRef"

    @builtins.property
    @jsii.member(jsii_name="databaseSnapshotRef")
    def database_snapshot_ref(self) -> "DatabaseSnapshotReference":
        '''(experimental) A reference to a DatabaseSnapshot resource.

        :stability: experimental
        '''
        return typing.cast("DatabaseSnapshotReference", jsii.get(self, "databaseSnapshotRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseSnapshotRef).__jsii_proxy_class__ = lambda : _IDatabaseSnapshotRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IDiskRef")
class IDiskRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Disk.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="diskRef")
    def disk_ref(self) -> "DiskReference":
        '''(experimental) A reference to a Disk resource.

        :stability: experimental
        '''
        ...


class _IDiskRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Disk.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IDiskRef"

    @builtins.property
    @jsii.member(jsii_name="diskRef")
    def disk_ref(self) -> "DiskReference":
        '''(experimental) A reference to a Disk resource.

        :stability: experimental
        '''
        return typing.cast("DiskReference", jsii.get(self, "diskRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDiskRef).__jsii_proxy_class__ = lambda : _IDiskRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IDiskSnapshotRef")
class IDiskSnapshotRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DiskSnapshot.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="diskSnapshotRef")
    def disk_snapshot_ref(self) -> "DiskSnapshotReference":
        '''(experimental) A reference to a DiskSnapshot resource.

        :stability: experimental
        '''
        ...


class _IDiskSnapshotRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DiskSnapshot.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IDiskSnapshotRef"

    @builtins.property
    @jsii.member(jsii_name="diskSnapshotRef")
    def disk_snapshot_ref(self) -> "DiskSnapshotReference":
        '''(experimental) A reference to a DiskSnapshot resource.

        :stability: experimental
        '''
        return typing.cast("DiskSnapshotReference", jsii.get(self, "diskSnapshotRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDiskSnapshotRef).__jsii_proxy_class__ = lambda : _IDiskSnapshotRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IDistributionRef")
class IDistributionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Distribution.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="distributionRef")
    def distribution_ref(self) -> "DistributionReference":
        '''(experimental) A reference to a Distribution resource.

        :stability: experimental
        '''
        ...


class _IDistributionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Distribution.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IDistributionRef"

    @builtins.property
    @jsii.member(jsii_name="distributionRef")
    def distribution_ref(self) -> "DistributionReference":
        '''(experimental) A reference to a Distribution resource.

        :stability: experimental
        '''
        return typing.cast("DistributionReference", jsii.get(self, "distributionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDistributionRef).__jsii_proxy_class__ = lambda : _IDistributionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IDomainRef")
class IDomainRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        ...


class _IDomainRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IDomainRef"

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        return typing.cast("DomainReference", jsii.get(self, "domainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainRef).__jsii_proxy_class__ = lambda : _IDomainRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IInstanceRef")
class IInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Instance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        ...


class _IInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Instance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        return typing.cast("InstanceReference", jsii.get(self, "instanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceRef).__jsii_proxy_class__ = lambda : _IInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IInstanceSnapshotRef")
class IInstanceSnapshotRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceSnapshot.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceSnapshotRef")
    def instance_snapshot_ref(self) -> "InstanceSnapshotReference":
        '''(experimental) A reference to a InstanceSnapshot resource.

        :stability: experimental
        '''
        ...


class _IInstanceSnapshotRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceSnapshot.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IInstanceSnapshotRef"

    @builtins.property
    @jsii.member(jsii_name="instanceSnapshotRef")
    def instance_snapshot_ref(self) -> "InstanceSnapshotReference":
        '''(experimental) A reference to a InstanceSnapshot resource.

        :stability: experimental
        '''
        return typing.cast("InstanceSnapshotReference", jsii.get(self, "instanceSnapshotRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceSnapshotRef).__jsii_proxy_class__ = lambda : _IInstanceSnapshotRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.ILoadBalancerRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.ILoadBalancerRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.ILoadBalancerTlsCertificateRef"
)
class ILoadBalancerTlsCertificateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LoadBalancerTlsCertificate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="loadBalancerTlsCertificateRef")
    def load_balancer_tls_certificate_ref(
        self,
    ) -> "LoadBalancerTlsCertificateReference":
        '''(experimental) A reference to a LoadBalancerTlsCertificate resource.

        :stability: experimental
        '''
        ...


class _ILoadBalancerTlsCertificateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LoadBalancerTlsCertificate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.ILoadBalancerTlsCertificateRef"

    @builtins.property
    @jsii.member(jsii_name="loadBalancerTlsCertificateRef")
    def load_balancer_tls_certificate_ref(
        self,
    ) -> "LoadBalancerTlsCertificateReference":
        '''(experimental) A reference to a LoadBalancerTlsCertificate resource.

        :stability: experimental
        '''
        return typing.cast("LoadBalancerTlsCertificateReference", jsii.get(self, "loadBalancerTlsCertificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoadBalancerTlsCertificateRef).__jsii_proxy_class__ = lambda : _ILoadBalancerTlsCertificateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lightsail.IStaticIpRef")
class IStaticIpRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StaticIp.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="staticIpRef")
    def static_ip_ref(self) -> "StaticIpReference":
        '''(experimental) A reference to a StaticIp resource.

        :stability: experimental
        '''
        ...


class _IStaticIpRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StaticIp.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lightsail.IStaticIpRef"

    @builtins.property
    @jsii.member(jsii_name="staticIpRef")
    def static_ip_ref(self) -> "StaticIpReference":
        '''(experimental) A reference to a StaticIp resource.

        :stability: experimental
        '''
        return typing.cast("StaticIpReference", jsii.get(self, "staticIpRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStaticIpRef).__jsii_proxy_class__ = lambda : _IStaticIpRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.InstanceReference",
    jsii_struct_bases=[],
    name_mapping={"instance_arn": "instanceArn", "instance_name": "instanceName"},
)
class InstanceReference:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        instance_name: builtins.str,
    ) -> None:
        '''A reference to a Instance resource.

        :param instance_arn: The ARN of the Instance resource.
        :param instance_name: The InstanceName of the Instance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            instance_reference = interfaces_lightsail.InstanceReference(
                instance_arn="instanceArn",
                instance_name="instanceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85b90667ac9cbddb49fe221e03e2cd6ec629eee94042c2be1c21668e43461563)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument instance_name", value=instance_name, expected_type=type_hints["instance_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "instance_name": instance_name,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The ARN of the Instance resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_name(self) -> builtins.str:
        '''The InstanceName of the Instance resource.'''
        result = self._values.get("instance_name")
        assert result is not None, "Required property 'instance_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.InstanceSnapshotReference",
    jsii_struct_bases=[],
    name_mapping={
        "instance_snapshot_arn": "instanceSnapshotArn",
        "instance_snapshot_name": "instanceSnapshotName",
    },
)
class InstanceSnapshotReference:
    def __init__(
        self,
        *,
        instance_snapshot_arn: builtins.str,
        instance_snapshot_name: builtins.str,
    ) -> None:
        '''A reference to a InstanceSnapshot resource.

        :param instance_snapshot_arn: The ARN of the InstanceSnapshot resource.
        :param instance_snapshot_name: The InstanceSnapshotName of the InstanceSnapshot resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            instance_snapshot_reference = interfaces_lightsail.InstanceSnapshotReference(
                instance_snapshot_arn="instanceSnapshotArn",
                instance_snapshot_name="instanceSnapshotName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b3213679b67a22b6852e10c45c601db59e53a196b542106afb013892505e18c)
            check_type(argname="argument instance_snapshot_arn", value=instance_snapshot_arn, expected_type=type_hints["instance_snapshot_arn"])
            check_type(argname="argument instance_snapshot_name", value=instance_snapshot_name, expected_type=type_hints["instance_snapshot_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_snapshot_arn": instance_snapshot_arn,
            "instance_snapshot_name": instance_snapshot_name,
        }

    @builtins.property
    def instance_snapshot_arn(self) -> builtins.str:
        '''The ARN of the InstanceSnapshot resource.'''
        result = self._values.get("instance_snapshot_arn")
        assert result is not None, "Required property 'instance_snapshot_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_snapshot_name(self) -> builtins.str:
        '''The InstanceSnapshotName of the InstanceSnapshot resource.'''
        result = self._values.get("instance_snapshot_name")
        assert result is not None, "Required property 'instance_snapshot_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceSnapshotReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.LoadBalancerReference",
    jsii_struct_bases=[],
    name_mapping={
        "load_balancer_arn": "loadBalancerArn",
        "load_balancer_name": "loadBalancerName",
    },
)
class LoadBalancerReference:
    def __init__(
        self,
        *,
        load_balancer_arn: builtins.str,
        load_balancer_name: builtins.str,
    ) -> None:
        '''A reference to a LoadBalancer resource.

        :param load_balancer_arn: The ARN of the LoadBalancer resource.
        :param load_balancer_name: The LoadBalancerName of the LoadBalancer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            load_balancer_reference = interfaces_lightsail.LoadBalancerReference(
                load_balancer_arn="loadBalancerArn",
                load_balancer_name="loadBalancerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab177296e991727275ec145c41e52a9bd1687398bb1b24d2e227a1cf24330a0a)
            check_type(argname="argument load_balancer_arn", value=load_balancer_arn, expected_type=type_hints["load_balancer_arn"])
            check_type(argname="argument load_balancer_name", value=load_balancer_name, expected_type=type_hints["load_balancer_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "load_balancer_arn": load_balancer_arn,
            "load_balancer_name": load_balancer_name,
        }

    @builtins.property
    def load_balancer_arn(self) -> builtins.str:
        '''The ARN of the LoadBalancer resource.'''
        result = self._values.get("load_balancer_arn")
        assert result is not None, "Required property 'load_balancer_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer_name(self) -> builtins.str:
        '''The LoadBalancerName of the LoadBalancer resource.'''
        result = self._values.get("load_balancer_name")
        assert result is not None, "Required property 'load_balancer_name' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.LoadBalancerTlsCertificateReference",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_name": "certificateName",
        "load_balancer_name": "loadBalancerName",
        "load_balancer_tls_certificate_arn": "loadBalancerTlsCertificateArn",
    },
)
class LoadBalancerTlsCertificateReference:
    def __init__(
        self,
        *,
        certificate_name: builtins.str,
        load_balancer_name: builtins.str,
        load_balancer_tls_certificate_arn: builtins.str,
    ) -> None:
        '''A reference to a LoadBalancerTlsCertificate resource.

        :param certificate_name: The CertificateName of the LoadBalancerTlsCertificate resource.
        :param load_balancer_name: The LoadBalancerName of the LoadBalancerTlsCertificate resource.
        :param load_balancer_tls_certificate_arn: The ARN of the LoadBalancerTlsCertificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            load_balancer_tls_certificate_reference = interfaces_lightsail.LoadBalancerTlsCertificateReference(
                certificate_name="certificateName",
                load_balancer_name="loadBalancerName",
                load_balancer_tls_certificate_arn="loadBalancerTlsCertificateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bd56863ab18f7122120f527f43fdf9cc700fadf3ce8ecc453a6312ba11621fa)
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument load_balancer_name", value=load_balancer_name, expected_type=type_hints["load_balancer_name"])
            check_type(argname="argument load_balancer_tls_certificate_arn", value=load_balancer_tls_certificate_arn, expected_type=type_hints["load_balancer_tls_certificate_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_name": certificate_name,
            "load_balancer_name": load_balancer_name,
            "load_balancer_tls_certificate_arn": load_balancer_tls_certificate_arn,
        }

    @builtins.property
    def certificate_name(self) -> builtins.str:
        '''The CertificateName of the LoadBalancerTlsCertificate resource.'''
        result = self._values.get("certificate_name")
        assert result is not None, "Required property 'certificate_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer_name(self) -> builtins.str:
        '''The LoadBalancerName of the LoadBalancerTlsCertificate resource.'''
        result = self._values.get("load_balancer_name")
        assert result is not None, "Required property 'load_balancer_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def load_balancer_tls_certificate_arn(self) -> builtins.str:
        '''The ARN of the LoadBalancerTlsCertificate resource.'''
        result = self._values.get("load_balancer_tls_certificate_arn")
        assert result is not None, "Required property 'load_balancer_tls_certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerTlsCertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lightsail.StaticIpReference",
    jsii_struct_bases=[],
    name_mapping={"static_ip_arn": "staticIpArn", "static_ip_name": "staticIpName"},
)
class StaticIpReference:
    def __init__(
        self,
        *,
        static_ip_arn: builtins.str,
        static_ip_name: builtins.str,
    ) -> None:
        '''A reference to a StaticIp resource.

        :param static_ip_arn: The ARN of the StaticIp resource.
        :param static_ip_name: The StaticIpName of the StaticIp resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lightsail as interfaces_lightsail
            
            static_ip_reference = interfaces_lightsail.StaticIpReference(
                static_ip_arn="staticIpArn",
                static_ip_name="staticIpName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f2476e04990a2a193f7c9e6433f145827b121d8f492aee4e2e21896a06c8a59)
            check_type(argname="argument static_ip_arn", value=static_ip_arn, expected_type=type_hints["static_ip_arn"])
            check_type(argname="argument static_ip_name", value=static_ip_name, expected_type=type_hints["static_ip_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "static_ip_arn": static_ip_arn,
            "static_ip_name": static_ip_name,
        }

    @builtins.property
    def static_ip_arn(self) -> builtins.str:
        '''The ARN of the StaticIp resource.'''
        result = self._values.get("static_ip_arn")
        assert result is not None, "Required property 'static_ip_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def static_ip_name(self) -> builtins.str:
        '''The StaticIpName of the StaticIp resource.'''
        result = self._values.get("static_ip_name")
        assert result is not None, "Required property 'static_ip_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StaticIpReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AlarmReference",
    "BucketReference",
    "CertificateReference",
    "ContainerReference",
    "DatabaseReference",
    "DatabaseSnapshotReference",
    "DiskReference",
    "DiskSnapshotReference",
    "DistributionReference",
    "DomainReference",
    "IAlarmRef",
    "IBucketRef",
    "ICertificateRef",
    "IContainerRef",
    "IDatabaseRef",
    "IDatabaseSnapshotRef",
    "IDiskRef",
    "IDiskSnapshotRef",
    "IDistributionRef",
    "IDomainRef",
    "IInstanceRef",
    "IInstanceSnapshotRef",
    "ILoadBalancerRef",
    "ILoadBalancerTlsCertificateRef",
    "IStaticIpRef",
    "InstanceReference",
    "InstanceSnapshotReference",
    "LoadBalancerReference",
    "LoadBalancerTlsCertificateReference",
    "StaticIpReference",
]

publication.publish()

def _typecheckingstub__337db78caea804686655f59ca18d9b791d909166130cf6acd0d12c194333f0c2(
    *,
    alarm_arn: builtins.str,
    alarm_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dfc3535ced0257498de71d28519b6135ff8f0011c01d7ca3dbb35006683b40d(
    *,
    bucket_arn: builtins.str,
    bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85079d2811b5a242a5ac3874f382d167649d814db74404924e6c368a4279aa68(
    *,
    certificate_arn: builtins.str,
    certificate_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2efffe0c15cd40bc6850a2bea53cdf7dfbb4d18160dd7603e200d869ac45fc4a(
    *,
    container_arn: builtins.str,
    service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ccc827d1fd7d7e85890ebbac083c9ca9e853e21bdda3342eea1846876a1fbb(
    *,
    database_arn: builtins.str,
    relational_database_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__502d7f0d341a4f9923c01b4d2389b077e255ea4beef655b8efc3498fa2ded806(
    *,
    database_snapshot_arn: builtins.str,
    relational_database_snapshot_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d411b3610244e9363a0cc69ad0c7a7390c87c80f57f88aefac603d40e1f6523(
    *,
    disk_arn: builtins.str,
    disk_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__972211f0d06a11bf7c410ddec0712399cab822fca0b46f74a95ab48068278f65(
    *,
    disk_snapshot_arn: builtins.str,
    disk_snapshot_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b247d312271c3bfbb9c42e90def612cd292f008d73422668b44ace152e12d4c2(
    *,
    distribution_arn: builtins.str,
    distribution_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1937efb4450a1e8a57eda9cc5f774d90626a974013ce20020bc4d13173e99968(
    *,
    domain_arn: builtins.str,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85b90667ac9cbddb49fe221e03e2cd6ec629eee94042c2be1c21668e43461563(
    *,
    instance_arn: builtins.str,
    instance_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b3213679b67a22b6852e10c45c601db59e53a196b542106afb013892505e18c(
    *,
    instance_snapshot_arn: builtins.str,
    instance_snapshot_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab177296e991727275ec145c41e52a9bd1687398bb1b24d2e227a1cf24330a0a(
    *,
    load_balancer_arn: builtins.str,
    load_balancer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bd56863ab18f7122120f527f43fdf9cc700fadf3ce8ecc453a6312ba11621fa(
    *,
    certificate_name: builtins.str,
    load_balancer_name: builtins.str,
    load_balancer_tls_certificate_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f2476e04990a2a193f7c9e6433f145827b121d8f492aee4e2e21896a06c8a59(
    *,
    static_ip_arn: builtins.str,
    static_ip_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAlarmRef, IBucketRef, ICertificateRef, IContainerRef, IDatabaseRef, IDatabaseSnapshotRef, IDiskRef, IDiskSnapshotRef, IDistributionRef, IDomainRef, IInstanceRef, IInstanceSnapshotRef, ILoadBalancerRef, ILoadBalancerTlsCertificateRef, IStaticIpRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
