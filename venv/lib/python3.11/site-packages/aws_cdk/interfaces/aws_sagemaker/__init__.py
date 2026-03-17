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
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.AppImageConfigReference",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_arn": "appImageConfigArn",
        "app_image_config_name": "appImageConfigName",
    },
)
class AppImageConfigReference:
    def __init__(
        self,
        *,
        app_image_config_arn: builtins.str,
        app_image_config_name: builtins.str,
    ) -> None:
        '''A reference to a AppImageConfig resource.

        :param app_image_config_arn: The ARN of the AppImageConfig resource.
        :param app_image_config_name: The AppImageConfigName of the AppImageConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            app_image_config_reference = interfaces_sagemaker.AppImageConfigReference(
                app_image_config_arn="appImageConfigArn",
                app_image_config_name="appImageConfigName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8605a0bbddb7566b87d731e87346f01eed74a7a840b35f21894ff7b04efe109a)
            check_type(argname="argument app_image_config_arn", value=app_image_config_arn, expected_type=type_hints["app_image_config_arn"])
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_image_config_arn": app_image_config_arn,
            "app_image_config_name": app_image_config_name,
        }

    @builtins.property
    def app_image_config_arn(self) -> builtins.str:
        '''The ARN of the AppImageConfig resource.'''
        result = self._values.get("app_image_config_arn")
        assert result is not None, "Required property 'app_image_config_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''The AppImageConfigName of the AppImageConfig resource.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppImageConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.AppReference",
    jsii_struct_bases=[],
    name_mapping={
        "app_arn": "appArn",
        "app_name": "appName",
        "app_type": "appType",
        "domain_id": "domainId",
        "user_profile_name": "userProfileName",
    },
)
class AppReference:
    def __init__(
        self,
        *,
        app_arn: builtins.str,
        app_name: builtins.str,
        app_type: builtins.str,
        domain_id: builtins.str,
        user_profile_name: builtins.str,
    ) -> None:
        '''A reference to a App resource.

        :param app_arn: The ARN of the App resource.
        :param app_name: The AppName of the App resource.
        :param app_type: The AppType of the App resource.
        :param domain_id: The DomainId of the App resource.
        :param user_profile_name: The UserProfileName of the App resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            app_reference = interfaces_sagemaker.AppReference(
                app_arn="appArn",
                app_name="appName",
                app_type="appType",
                domain_id="domainId",
                user_profile_name="userProfileName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acf6b4a544b0ae2c52d54ce3ceff8c75d3dcd96d513a527222edb518b2378b61)
            check_type(argname="argument app_arn", value=app_arn, expected_type=type_hints["app_arn"])
            check_type(argname="argument app_name", value=app_name, expected_type=type_hints["app_name"])
            check_type(argname="argument app_type", value=app_type, expected_type=type_hints["app_type"])
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument user_profile_name", value=user_profile_name, expected_type=type_hints["user_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_arn": app_arn,
            "app_name": app_name,
            "app_type": app_type,
            "domain_id": domain_id,
            "user_profile_name": user_profile_name,
        }

    @builtins.property
    def app_arn(self) -> builtins.str:
        '''The ARN of the App resource.'''
        result = self._values.get("app_arn")
        assert result is not None, "Required property 'app_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_name(self) -> builtins.str:
        '''The AppName of the App resource.'''
        result = self._values.get("app_name")
        assert result is not None, "Required property 'app_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_type(self) -> builtins.str:
        '''The AppType of the App resource.'''
        result = self._values.get("app_type")
        assert result is not None, "Required property 'app_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the App resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_profile_name(self) -> builtins.str:
        '''The UserProfileName of the App resource.'''
        result = self._values.get("user_profile_name")
        assert result is not None, "Required property 'user_profile_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn"},
)
class ClusterReference:
    def __init__(self, *, cluster_arn: builtins.str) -> None:
        '''A reference to a Cluster resource.

        :param cluster_arn: The ClusterArn of the Cluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            cluster_reference = interfaces_sagemaker.ClusterReference(
                cluster_arn="clusterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b41740c83d2043a3c12795517b06ef5392e313ddf64f0baf09ea7a2ce947048c)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The ClusterArn of the Cluster resource.'''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.CodeRepositoryReference",
    jsii_struct_bases=[],
    name_mapping={
        "code_repository_id": "codeRepositoryId",
        "code_repository_name": "codeRepositoryName",
    },
)
class CodeRepositoryReference:
    def __init__(
        self,
        *,
        code_repository_id: builtins.str,
        code_repository_name: builtins.str,
    ) -> None:
        '''A reference to a CodeRepository resource.

        :param code_repository_id: The Id of the CodeRepository resource.
        :param code_repository_name: The CodeRepositoryName of the CodeRepository resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            code_repository_reference = interfaces_sagemaker.CodeRepositoryReference(
                code_repository_id="codeRepositoryId",
                code_repository_name="codeRepositoryName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d50203d0b8619bba87d6272a7d3180c525e4133465ac661135be4365a5902520)
            check_type(argname="argument code_repository_id", value=code_repository_id, expected_type=type_hints["code_repository_id"])
            check_type(argname="argument code_repository_name", value=code_repository_name, expected_type=type_hints["code_repository_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code_repository_id": code_repository_id,
            "code_repository_name": code_repository_name,
        }

    @builtins.property
    def code_repository_id(self) -> builtins.str:
        '''The Id of the CodeRepository resource.'''
        result = self._values.get("code_repository_id")
        assert result is not None, "Required property 'code_repository_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code_repository_name(self) -> builtins.str:
        '''The CodeRepositoryName of the CodeRepository resource.'''
        result = self._values.get("code_repository_name")
        assert result is not None, "Required property 'code_repository_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeRepositoryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.DataQualityJobDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"job_definition_arn": "jobDefinitionArn"},
)
class DataQualityJobDefinitionReference:
    def __init__(self, *, job_definition_arn: builtins.str) -> None:
        '''A reference to a DataQualityJobDefinition resource.

        :param job_definition_arn: The JobDefinitionArn of the DataQualityJobDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            data_quality_job_definition_reference = interfaces_sagemaker.DataQualityJobDefinitionReference(
                job_definition_arn="jobDefinitionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b50ea0229d7c5b363f40e378afed722f72bc9584c588e33961e55a8acd85a7d)
            check_type(argname="argument job_definition_arn", value=job_definition_arn, expected_type=type_hints["job_definition_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_definition_arn": job_definition_arn,
        }

    @builtins.property
    def job_definition_arn(self) -> builtins.str:
        '''The JobDefinitionArn of the DataQualityJobDefinition resource.'''
        result = self._values.get("job_definition_arn")
        assert result is not None, "Required property 'job_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataQualityJobDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.DeviceFleetReference",
    jsii_struct_bases=[],
    name_mapping={"device_fleet_name": "deviceFleetName"},
)
class DeviceFleetReference:
    def __init__(self, *, device_fleet_name: builtins.str) -> None:
        '''A reference to a DeviceFleet resource.

        :param device_fleet_name: The DeviceFleetName of the DeviceFleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            device_fleet_reference = interfaces_sagemaker.DeviceFleetReference(
                device_fleet_name="deviceFleetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b9a733d992a034e2946905dc4f6aea8cb11d66ab8a69578e5ec6f5ac02a78c1)
            check_type(argname="argument device_fleet_name", value=device_fleet_name, expected_type=type_hints["device_fleet_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_fleet_name": device_fleet_name,
        }

    @builtins.property
    def device_fleet_name(self) -> builtins.str:
        '''The DeviceFleetName of the DeviceFleet resource.'''
        result = self._values.get("device_fleet_name")
        assert result is not None, "Required property 'device_fleet_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeviceFleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.DeviceReference",
    jsii_struct_bases=[],
    name_mapping={"device_fleet_name": "deviceFleetName"},
)
class DeviceReference:
    def __init__(self, *, device_fleet_name: builtins.str) -> None:
        '''A reference to a Device resource.

        :param device_fleet_name: The DeviceFleetName of the Device resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            device_reference = interfaces_sagemaker.DeviceReference(
                device_fleet_name="deviceFleetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e91123dc160df144def6083969becc0cfa03100ce49a86dbd47dbc531c40dc4)
            check_type(argname="argument device_fleet_name", value=device_fleet_name, expected_type=type_hints["device_fleet_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_fleet_name": device_fleet_name,
        }

    @builtins.property
    def device_fleet_name(self) -> builtins.str:
        '''The DeviceFleetName of the Device resource.'''
        result = self._values.get("device_fleet_name")
        assert result is not None, "Required property 'device_fleet_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeviceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.DomainReference",
    jsii_struct_bases=[],
    name_mapping={"domain_arn": "domainArn", "domain_id": "domainId"},
)
class DomainReference:
    def __init__(self, *, domain_arn: builtins.str, domain_id: builtins.str) -> None:
        '''A reference to a Domain resource.

        :param domain_arn: The ARN of the Domain resource.
        :param domain_id: The DomainId of the Domain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            domain_reference = interfaces_sagemaker.DomainReference(
                domain_arn="domainArn",
                domain_id="domainId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b051cfa5b56c2c44861ce067c6e3e2b5ff6bc49d74d2a599515c501b0884167)
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_arn": domain_arn,
            "domain_id": domain_id,
        }

    @builtins.property
    def domain_arn(self) -> builtins.str:
        '''The ARN of the Domain resource.'''
        result = self._values.get("domain_arn")
        assert result is not None, "Required property 'domain_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the Domain resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.EndpointConfigReference",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_config_id": "endpointConfigId",
        "endpoint_config_name": "endpointConfigName",
    },
)
class EndpointConfigReference:
    def __init__(
        self,
        *,
        endpoint_config_id: builtins.str,
        endpoint_config_name: builtins.str,
    ) -> None:
        '''A reference to a EndpointConfig resource.

        :param endpoint_config_id: The Id of the EndpointConfig resource.
        :param endpoint_config_name: The EndpointConfigName of the EndpointConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            endpoint_config_reference = interfaces_sagemaker.EndpointConfigReference(
                endpoint_config_id="endpointConfigId",
                endpoint_config_name="endpointConfigName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__671b59e91ff91baea0cef8d7d45d4100318e43b4ba27225394b64570ce952f45)
            check_type(argname="argument endpoint_config_id", value=endpoint_config_id, expected_type=type_hints["endpoint_config_id"])
            check_type(argname="argument endpoint_config_name", value=endpoint_config_name, expected_type=type_hints["endpoint_config_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_config_id": endpoint_config_id,
            "endpoint_config_name": endpoint_config_name,
        }

    @builtins.property
    def endpoint_config_id(self) -> builtins.str:
        '''The Id of the EndpointConfig resource.'''
        result = self._values.get("endpoint_config_id")
        assert result is not None, "Required property 'endpoint_config_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_config_name(self) -> builtins.str:
        '''The EndpointConfigName of the EndpointConfig resource.'''
        result = self._values.get("endpoint_config_name")
        assert result is not None, "Required property 'endpoint_config_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.EndpointReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_arn": "endpointArn"},
)
class EndpointReference:
    def __init__(self, *, endpoint_arn: builtins.str) -> None:
        '''A reference to a Endpoint resource.

        :param endpoint_arn: The EndpointArn of the Endpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            endpoint_reference = interfaces_sagemaker.EndpointReference(
                endpoint_arn="endpointArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba07aa533865a76289f1b8ba76c2ae9b68760c1195553f601d11a7addf968c43)
            check_type(argname="argument endpoint_arn", value=endpoint_arn, expected_type=type_hints["endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_arn": endpoint_arn,
        }

    @builtins.property
    def endpoint_arn(self) -> builtins.str:
        '''The EndpointArn of the Endpoint resource.'''
        result = self._values.get("endpoint_arn")
        assert result is not None, "Required property 'endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.FeatureGroupReference",
    jsii_struct_bases=[],
    name_mapping={"feature_group_name": "featureGroupName"},
)
class FeatureGroupReference:
    def __init__(self, *, feature_group_name: builtins.str) -> None:
        '''A reference to a FeatureGroup resource.

        :param feature_group_name: The FeatureGroupName of the FeatureGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            feature_group_reference = interfaces_sagemaker.FeatureGroupReference(
                feature_group_name="featureGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0043c65a11b7af9fa8bd64a420c0be15fb3226e8c86d9153a34ccb0e0c57f82b)
            check_type(argname="argument feature_group_name", value=feature_group_name, expected_type=type_hints["feature_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "feature_group_name": feature_group_name,
        }

    @builtins.property
    def feature_group_name(self) -> builtins.str:
        '''The FeatureGroupName of the FeatureGroup resource.'''
        result = self._values.get("feature_group_name")
        assert result is not None, "Required property 'feature_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FeatureGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IAppImageConfigRef")
class IAppImageConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AppImageConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appImageConfigRef")
    def app_image_config_ref(self) -> "AppImageConfigReference":
        '''(experimental) A reference to a AppImageConfig resource.

        :stability: experimental
        '''
        ...


class _IAppImageConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AppImageConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IAppImageConfigRef"

    @builtins.property
    @jsii.member(jsii_name="appImageConfigRef")
    def app_image_config_ref(self) -> "AppImageConfigReference":
        '''(experimental) A reference to a AppImageConfig resource.

        :stability: experimental
        '''
        return typing.cast("AppImageConfigReference", jsii.get(self, "appImageConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppImageConfigRef).__jsii_proxy_class__ = lambda : _IAppImageConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IAppRef")
class IAppRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        ...


class _IAppRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IAppRef"

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        return typing.cast("AppReference", jsii.get(self, "appRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppRef).__jsii_proxy_class__ = lambda : _IAppRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IClusterRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ICodeRepositoryRef")
class ICodeRepositoryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CodeRepository.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="codeRepositoryRef")
    def code_repository_ref(self) -> "CodeRepositoryReference":
        '''(experimental) A reference to a CodeRepository resource.

        :stability: experimental
        '''
        ...


class _ICodeRepositoryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CodeRepository.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.ICodeRepositoryRef"

    @builtins.property
    @jsii.member(jsii_name="codeRepositoryRef")
    def code_repository_ref(self) -> "CodeRepositoryReference":
        '''(experimental) A reference to a CodeRepository resource.

        :stability: experimental
        '''
        return typing.cast("CodeRepositoryReference", jsii.get(self, "codeRepositoryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICodeRepositoryRef).__jsii_proxy_class__ = lambda : _ICodeRepositoryRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IDataQualityJobDefinitionRef"
)
class IDataQualityJobDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataQualityJobDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataQualityJobDefinitionRef")
    def data_quality_job_definition_ref(self) -> "DataQualityJobDefinitionReference":
        '''(experimental) A reference to a DataQualityJobDefinition resource.

        :stability: experimental
        '''
        ...


class _IDataQualityJobDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataQualityJobDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IDataQualityJobDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="dataQualityJobDefinitionRef")
    def data_quality_job_definition_ref(self) -> "DataQualityJobDefinitionReference":
        '''(experimental) A reference to a DataQualityJobDefinition resource.

        :stability: experimental
        '''
        return typing.cast("DataQualityJobDefinitionReference", jsii.get(self, "dataQualityJobDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataQualityJobDefinitionRef).__jsii_proxy_class__ = lambda : _IDataQualityJobDefinitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IDeviceFleetRef")
class IDeviceFleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeviceFleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deviceFleetRef")
    def device_fleet_ref(self) -> "DeviceFleetReference":
        '''(experimental) A reference to a DeviceFleet resource.

        :stability: experimental
        '''
        ...


class _IDeviceFleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeviceFleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IDeviceFleetRef"

    @builtins.property
    @jsii.member(jsii_name="deviceFleetRef")
    def device_fleet_ref(self) -> "DeviceFleetReference":
        '''(experimental) A reference to a DeviceFleet resource.

        :stability: experimental
        '''
        return typing.cast("DeviceFleetReference", jsii.get(self, "deviceFleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeviceFleetRef).__jsii_proxy_class__ = lambda : _IDeviceFleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IDeviceRef")
class IDeviceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Device.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deviceRef")
    def device_ref(self) -> "DeviceReference":
        '''(experimental) A reference to a Device resource.

        :stability: experimental
        '''
        ...


class _IDeviceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Device.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IDeviceRef"

    @builtins.property
    @jsii.member(jsii_name="deviceRef")
    def device_ref(self) -> "DeviceReference":
        '''(experimental) A reference to a Device resource.

        :stability: experimental
        '''
        return typing.cast("DeviceReference", jsii.get(self, "deviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeviceRef).__jsii_proxy_class__ = lambda : _IDeviceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IDomainRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IDomainRef"

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        return typing.cast("DomainReference", jsii.get(self, "domainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainRef).__jsii_proxy_class__ = lambda : _IDomainRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IEndpointConfigRef")
class IEndpointConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EndpointConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointConfigRef")
    def endpoint_config_ref(self) -> "EndpointConfigReference":
        '''(experimental) A reference to a EndpointConfig resource.

        :stability: experimental
        '''
        ...


class _IEndpointConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EndpointConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IEndpointConfigRef"

    @builtins.property
    @jsii.member(jsii_name="endpointConfigRef")
    def endpoint_config_ref(self) -> "EndpointConfigReference":
        '''(experimental) A reference to a EndpointConfig resource.

        :stability: experimental
        '''
        return typing.cast("EndpointConfigReference", jsii.get(self, "endpointConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointConfigRef).__jsii_proxy_class__ = lambda : _IEndpointConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IEndpointRef")
class IEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        ...


class _IEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        return typing.cast("EndpointReference", jsii.get(self, "endpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointRef).__jsii_proxy_class__ = lambda : _IEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IFeatureGroupRef")
class IFeatureGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FeatureGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="featureGroupRef")
    def feature_group_ref(self) -> "FeatureGroupReference":
        '''(experimental) A reference to a FeatureGroup resource.

        :stability: experimental
        '''
        ...


class _IFeatureGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FeatureGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IFeatureGroupRef"

    @builtins.property
    @jsii.member(jsii_name="featureGroupRef")
    def feature_group_ref(self) -> "FeatureGroupReference":
        '''(experimental) A reference to a FeatureGroup resource.

        :stability: experimental
        '''
        return typing.cast("FeatureGroupReference", jsii.get(self, "featureGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFeatureGroupRef).__jsii_proxy_class__ = lambda : _IFeatureGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IImageRef")
class IImageRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Image.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="imageRef")
    def image_ref(self) -> "ImageReference":
        '''(experimental) A reference to a Image resource.

        :stability: experimental
        '''
        ...


class _IImageRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Image.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IImageRef"

    @builtins.property
    @jsii.member(jsii_name="imageRef")
    def image_ref(self) -> "ImageReference":
        '''(experimental) A reference to a Image resource.

        :stability: experimental
        '''
        return typing.cast("ImageReference", jsii.get(self, "imageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IImageRef).__jsii_proxy_class__ = lambda : _IImageRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IImageVersionRef")
class IImageVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ImageVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="imageVersionRef")
    def image_version_ref(self) -> "ImageVersionReference":
        '''(experimental) A reference to a ImageVersion resource.

        :stability: experimental
        '''
        ...


class _IImageVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ImageVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IImageVersionRef"

    @builtins.property
    @jsii.member(jsii_name="imageVersionRef")
    def image_version_ref(self) -> "ImageVersionReference":
        '''(experimental) A reference to a ImageVersion resource.

        :stability: experimental
        '''
        return typing.cast("ImageVersionReference", jsii.get(self, "imageVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IImageVersionRef).__jsii_proxy_class__ = lambda : _IImageVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IInferenceComponentRef"
)
class IInferenceComponentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InferenceComponent.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="inferenceComponentRef")
    def inference_component_ref(self) -> "InferenceComponentReference":
        '''(experimental) A reference to a InferenceComponent resource.

        :stability: experimental
        '''
        ...


class _IInferenceComponentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InferenceComponent.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IInferenceComponentRef"

    @builtins.property
    @jsii.member(jsii_name="inferenceComponentRef")
    def inference_component_ref(self) -> "InferenceComponentReference":
        '''(experimental) A reference to a InferenceComponent resource.

        :stability: experimental
        '''
        return typing.cast("InferenceComponentReference", jsii.get(self, "inferenceComponentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInferenceComponentRef).__jsii_proxy_class__ = lambda : _IInferenceComponentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IInferenceExperimentRef"
)
class IInferenceExperimentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InferenceExperiment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="inferenceExperimentRef")
    def inference_experiment_ref(self) -> "InferenceExperimentReference":
        '''(experimental) A reference to a InferenceExperiment resource.

        :stability: experimental
        '''
        ...


class _IInferenceExperimentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InferenceExperiment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IInferenceExperimentRef"

    @builtins.property
    @jsii.member(jsii_name="inferenceExperimentRef")
    def inference_experiment_ref(self) -> "InferenceExperimentReference":
        '''(experimental) A reference to a InferenceExperiment resource.

        :stability: experimental
        '''
        return typing.cast("InferenceExperimentReference", jsii.get(self, "inferenceExperimentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInferenceExperimentRef).__jsii_proxy_class__ = lambda : _IInferenceExperimentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IMlflowTrackingServerRef"
)
class IMlflowTrackingServerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MlflowTrackingServer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mlflowTrackingServerRef")
    def mlflow_tracking_server_ref(self) -> "MlflowTrackingServerReference":
        '''(experimental) A reference to a MlflowTrackingServer resource.

        :stability: experimental
        '''
        ...


class _IMlflowTrackingServerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MlflowTrackingServer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IMlflowTrackingServerRef"

    @builtins.property
    @jsii.member(jsii_name="mlflowTrackingServerRef")
    def mlflow_tracking_server_ref(self) -> "MlflowTrackingServerReference":
        '''(experimental) A reference to a MlflowTrackingServer resource.

        :stability: experimental
        '''
        return typing.cast("MlflowTrackingServerReference", jsii.get(self, "mlflowTrackingServerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMlflowTrackingServerRef).__jsii_proxy_class__ = lambda : _IMlflowTrackingServerRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IModelBiasJobDefinitionRef"
)
class IModelBiasJobDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ModelBiasJobDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelBiasJobDefinitionRef")
    def model_bias_job_definition_ref(self) -> "ModelBiasJobDefinitionReference":
        '''(experimental) A reference to a ModelBiasJobDefinition resource.

        :stability: experimental
        '''
        ...


class _IModelBiasJobDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ModelBiasJobDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IModelBiasJobDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="modelBiasJobDefinitionRef")
    def model_bias_job_definition_ref(self) -> "ModelBiasJobDefinitionReference":
        '''(experimental) A reference to a ModelBiasJobDefinition resource.

        :stability: experimental
        '''
        return typing.cast("ModelBiasJobDefinitionReference", jsii.get(self, "modelBiasJobDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelBiasJobDefinitionRef).__jsii_proxy_class__ = lambda : _IModelBiasJobDefinitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IModelCardRef")
class IModelCardRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ModelCard.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelCardRef")
    def model_card_ref(self) -> "ModelCardReference":
        '''(experimental) A reference to a ModelCard resource.

        :stability: experimental
        '''
        ...


class _IModelCardRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ModelCard.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IModelCardRef"

    @builtins.property
    @jsii.member(jsii_name="modelCardRef")
    def model_card_ref(self) -> "ModelCardReference":
        '''(experimental) A reference to a ModelCard resource.

        :stability: experimental
        '''
        return typing.cast("ModelCardReference", jsii.get(self, "modelCardRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelCardRef).__jsii_proxy_class__ = lambda : _IModelCardRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IModelExplainabilityJobDefinitionRef"
)
class IModelExplainabilityJobDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ModelExplainabilityJobDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelExplainabilityJobDefinitionRef")
    def model_explainability_job_definition_ref(
        self,
    ) -> "ModelExplainabilityJobDefinitionReference":
        '''(experimental) A reference to a ModelExplainabilityJobDefinition resource.

        :stability: experimental
        '''
        ...


class _IModelExplainabilityJobDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ModelExplainabilityJobDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IModelExplainabilityJobDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="modelExplainabilityJobDefinitionRef")
    def model_explainability_job_definition_ref(
        self,
    ) -> "ModelExplainabilityJobDefinitionReference":
        '''(experimental) A reference to a ModelExplainabilityJobDefinition resource.

        :stability: experimental
        '''
        return typing.cast("ModelExplainabilityJobDefinitionReference", jsii.get(self, "modelExplainabilityJobDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelExplainabilityJobDefinitionRef).__jsii_proxy_class__ = lambda : _IModelExplainabilityJobDefinitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IModelPackageGroupRef")
class IModelPackageGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ModelPackageGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelPackageGroupRef")
    def model_package_group_ref(self) -> "ModelPackageGroupReference":
        '''(experimental) A reference to a ModelPackageGroup resource.

        :stability: experimental
        '''
        ...


class _IModelPackageGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ModelPackageGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IModelPackageGroupRef"

    @builtins.property
    @jsii.member(jsii_name="modelPackageGroupRef")
    def model_package_group_ref(self) -> "ModelPackageGroupReference":
        '''(experimental) A reference to a ModelPackageGroup resource.

        :stability: experimental
        '''
        return typing.cast("ModelPackageGroupReference", jsii.get(self, "modelPackageGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelPackageGroupRef).__jsii_proxy_class__ = lambda : _IModelPackageGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IModelPackageRef")
class IModelPackageRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ModelPackage.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelPackageRef")
    def model_package_ref(self) -> "ModelPackageReference":
        '''(experimental) A reference to a ModelPackage resource.

        :stability: experimental
        '''
        ...


class _IModelPackageRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ModelPackage.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IModelPackageRef"

    @builtins.property
    @jsii.member(jsii_name="modelPackageRef")
    def model_package_ref(self) -> "ModelPackageReference":
        '''(experimental) A reference to a ModelPackage resource.

        :stability: experimental
        '''
        return typing.cast("ModelPackageReference", jsii.get(self, "modelPackageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelPackageRef).__jsii_proxy_class__ = lambda : _IModelPackageRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IModelQualityJobDefinitionRef"
)
class IModelQualityJobDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ModelQualityJobDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelQualityJobDefinitionRef")
    def model_quality_job_definition_ref(self) -> "ModelQualityJobDefinitionReference":
        '''(experimental) A reference to a ModelQualityJobDefinition resource.

        :stability: experimental
        '''
        ...


class _IModelQualityJobDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ModelQualityJobDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IModelQualityJobDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="modelQualityJobDefinitionRef")
    def model_quality_job_definition_ref(self) -> "ModelQualityJobDefinitionReference":
        '''(experimental) A reference to a ModelQualityJobDefinition resource.

        :stability: experimental
        '''
        return typing.cast("ModelQualityJobDefinitionReference", jsii.get(self, "modelQualityJobDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelQualityJobDefinitionRef).__jsii_proxy_class__ = lambda : _IModelQualityJobDefinitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IModelRef")
class IModelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Model.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="modelRef")
    def model_ref(self) -> "ModelReference":
        '''(experimental) A reference to a Model resource.

        :stability: experimental
        '''
        ...


class _IModelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Model.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IModelRef"

    @builtins.property
    @jsii.member(jsii_name="modelRef")
    def model_ref(self) -> "ModelReference":
        '''(experimental) A reference to a Model resource.

        :stability: experimental
        '''
        return typing.cast("ModelReference", jsii.get(self, "modelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModelRef).__jsii_proxy_class__ = lambda : _IModelRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IMonitoringScheduleRef"
)
class IMonitoringScheduleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MonitoringSchedule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="monitoringScheduleRef")
    def monitoring_schedule_ref(self) -> "MonitoringScheduleReference":
        '''(experimental) A reference to a MonitoringSchedule resource.

        :stability: experimental
        '''
        ...


class _IMonitoringScheduleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MonitoringSchedule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IMonitoringScheduleRef"

    @builtins.property
    @jsii.member(jsii_name="monitoringScheduleRef")
    def monitoring_schedule_ref(self) -> "MonitoringScheduleReference":
        '''(experimental) A reference to a MonitoringSchedule resource.

        :stability: experimental
        '''
        return typing.cast("MonitoringScheduleReference", jsii.get(self, "monitoringScheduleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMonitoringScheduleRef).__jsii_proxy_class__ = lambda : _IMonitoringScheduleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.INotebookInstanceLifecycleConfigRef"
)
class INotebookInstanceLifecycleConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NotebookInstanceLifecycleConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="notebookInstanceLifecycleConfigRef")
    def notebook_instance_lifecycle_config_ref(
        self,
    ) -> "NotebookInstanceLifecycleConfigReference":
        '''(experimental) A reference to a NotebookInstanceLifecycleConfig resource.

        :stability: experimental
        '''
        ...


class _INotebookInstanceLifecycleConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NotebookInstanceLifecycleConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.INotebookInstanceLifecycleConfigRef"

    @builtins.property
    @jsii.member(jsii_name="notebookInstanceLifecycleConfigRef")
    def notebook_instance_lifecycle_config_ref(
        self,
    ) -> "NotebookInstanceLifecycleConfigReference":
        '''(experimental) A reference to a NotebookInstanceLifecycleConfig resource.

        :stability: experimental
        '''
        return typing.cast("NotebookInstanceLifecycleConfigReference", jsii.get(self, "notebookInstanceLifecycleConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotebookInstanceLifecycleConfigRef).__jsii_proxy_class__ = lambda : _INotebookInstanceLifecycleConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.INotebookInstanceRef")
class INotebookInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NotebookInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="notebookInstanceRef")
    def notebook_instance_ref(self) -> "NotebookInstanceReference":
        '''(experimental) A reference to a NotebookInstance resource.

        :stability: experimental
        '''
        ...


class _INotebookInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NotebookInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.INotebookInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="notebookInstanceRef")
    def notebook_instance_ref(self) -> "NotebookInstanceReference":
        '''(experimental) A reference to a NotebookInstance resource.

        :stability: experimental
        '''
        return typing.cast("NotebookInstanceReference", jsii.get(self, "notebookInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotebookInstanceRef).__jsii_proxy_class__ = lambda : _INotebookInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IPartnerAppRef")
class IPartnerAppRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PartnerApp.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="partnerAppRef")
    def partner_app_ref(self) -> "PartnerAppReference":
        '''(experimental) A reference to a PartnerApp resource.

        :stability: experimental
        '''
        ...


class _IPartnerAppRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PartnerApp.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IPartnerAppRef"

    @builtins.property
    @jsii.member(jsii_name="partnerAppRef")
    def partner_app_ref(self) -> "PartnerAppReference":
        '''(experimental) A reference to a PartnerApp resource.

        :stability: experimental
        '''
        return typing.cast("PartnerAppReference", jsii.get(self, "partnerAppRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPartnerAppRef).__jsii_proxy_class__ = lambda : _IPartnerAppRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IPipelineRef")
class IPipelineRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Pipeline.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pipelineRef")
    def pipeline_ref(self) -> "PipelineReference":
        '''(experimental) A reference to a Pipeline resource.

        :stability: experimental
        '''
        ...


class _IPipelineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Pipeline.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IPipelineRef"

    @builtins.property
    @jsii.member(jsii_name="pipelineRef")
    def pipeline_ref(self) -> "PipelineReference":
        '''(experimental) A reference to a Pipeline resource.

        :stability: experimental
        '''
        return typing.cast("PipelineReference", jsii.get(self, "pipelineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPipelineRef).__jsii_proxy_class__ = lambda : _IPipelineRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IProcessingJobRef")
class IProcessingJobRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProcessingJob.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="processingJobRef")
    def processing_job_ref(self) -> "ProcessingJobReference":
        '''(experimental) A reference to a ProcessingJob resource.

        :stability: experimental
        '''
        ...


class _IProcessingJobRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProcessingJob.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IProcessingJobRef"

    @builtins.property
    @jsii.member(jsii_name="processingJobRef")
    def processing_job_ref(self) -> "ProcessingJobReference":
        '''(experimental) A reference to a ProcessingJob resource.

        :stability: experimental
        '''
        return typing.cast("ProcessingJobReference", jsii.get(self, "processingJobRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProcessingJobRef).__jsii_proxy_class__ = lambda : _IProcessingJobRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IProjectRef")
class IProjectRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Project.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        ...


class _IProjectRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Project.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IProjectRef"

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        return typing.cast("ProjectReference", jsii.get(self, "projectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectRef).__jsii_proxy_class__ = lambda : _IProjectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ISpaceRef")
class ISpaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Space.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="spaceRef")
    def space_ref(self) -> "SpaceReference":
        '''(experimental) A reference to a Space resource.

        :stability: experimental
        '''
        ...


class _ISpaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Space.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.ISpaceRef"

    @builtins.property
    @jsii.member(jsii_name="spaceRef")
    def space_ref(self) -> "SpaceReference":
        '''(experimental) A reference to a Space resource.

        :stability: experimental
        '''
        return typing.cast("SpaceReference", jsii.get(self, "spaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISpaceRef).__jsii_proxy_class__ = lambda : _ISpaceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IStudioLifecycleConfigRef"
)
class IStudioLifecycleConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StudioLifecycleConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="studioLifecycleConfigRef")
    def studio_lifecycle_config_ref(self) -> "StudioLifecycleConfigReference":
        '''(experimental) A reference to a StudioLifecycleConfig resource.

        :stability: experimental
        '''
        ...


class _IStudioLifecycleConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StudioLifecycleConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IStudioLifecycleConfigRef"

    @builtins.property
    @jsii.member(jsii_name="studioLifecycleConfigRef")
    def studio_lifecycle_config_ref(self) -> "StudioLifecycleConfigReference":
        '''(experimental) A reference to a StudioLifecycleConfig resource.

        :stability: experimental
        '''
        return typing.cast("StudioLifecycleConfigReference", jsii.get(self, "studioLifecycleConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStudioLifecycleConfigRef).__jsii_proxy_class__ = lambda : _IStudioLifecycleConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IUserProfileRef")
class IUserProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userProfileRef")
    def user_profile_ref(self) -> "UserProfileReference":
        '''(experimental) A reference to a UserProfile resource.

        :stability: experimental
        '''
        ...


class _IUserProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IUserProfileRef"

    @builtins.property
    @jsii.member(jsii_name="userProfileRef")
    def user_profile_ref(self) -> "UserProfileReference":
        '''(experimental) A reference to a UserProfile resource.

        :stability: experimental
        '''
        return typing.cast("UserProfileReference", jsii.get(self, "userProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserProfileRef).__jsii_proxy_class__ = lambda : _IUserProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.IWorkteamRef")
class IWorkteamRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workteam.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workteamRef")
    def workteam_ref(self) -> "WorkteamReference":
        '''(experimental) A reference to a Workteam resource.

        :stability: experimental
        '''
        ...


class _IWorkteamRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workteam.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sagemaker.IWorkteamRef"

    @builtins.property
    @jsii.member(jsii_name="workteamRef")
    def workteam_ref(self) -> "WorkteamReference":
        '''(experimental) A reference to a Workteam resource.

        :stability: experimental
        '''
        return typing.cast("WorkteamReference", jsii.get(self, "workteamRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkteamRef).__jsii_proxy_class__ = lambda : _IWorkteamRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ImageReference",
    jsii_struct_bases=[],
    name_mapping={"image_arn": "imageArn"},
)
class ImageReference:
    def __init__(self, *, image_arn: builtins.str) -> None:
        '''A reference to a Image resource.

        :param image_arn: The ImageArn of the Image resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            image_reference = interfaces_sagemaker.ImageReference(
                image_arn="imageArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84c8da85f1097ad468daeebaf96185535637ac444b0d540b6b2c7e24ae5f23b6)
            check_type(argname="argument image_arn", value=image_arn, expected_type=type_hints["image_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_arn": image_arn,
        }

    @builtins.property
    def image_arn(self) -> builtins.str:
        '''The ImageArn of the Image resource.'''
        result = self._values.get("image_arn")
        assert result is not None, "Required property 'image_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ImageVersionReference",
    jsii_struct_bases=[],
    name_mapping={"image_version_arn": "imageVersionArn"},
)
class ImageVersionReference:
    def __init__(self, *, image_version_arn: builtins.str) -> None:
        '''A reference to a ImageVersion resource.

        :param image_version_arn: The ImageVersionArn of the ImageVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            image_version_reference = interfaces_sagemaker.ImageVersionReference(
                image_version_arn="imageVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49ddecb7633f51ab5122ae78f78bcdbad2e65eb4e6e17e13971b80a156e849c2)
            check_type(argname="argument image_version_arn", value=image_version_arn, expected_type=type_hints["image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_version_arn": image_version_arn,
        }

    @builtins.property
    def image_version_arn(self) -> builtins.str:
        '''The ImageVersionArn of the ImageVersion resource.'''
        result = self._values.get("image_version_arn")
        assert result is not None, "Required property 'image_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.InferenceComponentReference",
    jsii_struct_bases=[],
    name_mapping={"inference_component_arn": "inferenceComponentArn"},
)
class InferenceComponentReference:
    def __init__(self, *, inference_component_arn: builtins.str) -> None:
        '''A reference to a InferenceComponent resource.

        :param inference_component_arn: The InferenceComponentArn of the InferenceComponent resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            inference_component_reference = interfaces_sagemaker.InferenceComponentReference(
                inference_component_arn="inferenceComponentArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cb0712a1d37391a9ac27801c64ffce4938819ecc0068f44355fc8c66d46f11c)
            check_type(argname="argument inference_component_arn", value=inference_component_arn, expected_type=type_hints["inference_component_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "inference_component_arn": inference_component_arn,
        }

    @builtins.property
    def inference_component_arn(self) -> builtins.str:
        '''The InferenceComponentArn of the InferenceComponent resource.'''
        result = self._values.get("inference_component_arn")
        assert result is not None, "Required property 'inference_component_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InferenceComponentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.InferenceExperimentReference",
    jsii_struct_bases=[],
    name_mapping={
        "inference_experiment_arn": "inferenceExperimentArn",
        "inference_experiment_name": "inferenceExperimentName",
    },
)
class InferenceExperimentReference:
    def __init__(
        self,
        *,
        inference_experiment_arn: builtins.str,
        inference_experiment_name: builtins.str,
    ) -> None:
        '''A reference to a InferenceExperiment resource.

        :param inference_experiment_arn: The ARN of the InferenceExperiment resource.
        :param inference_experiment_name: The Name of the InferenceExperiment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            inference_experiment_reference = interfaces_sagemaker.InferenceExperimentReference(
                inference_experiment_arn="inferenceExperimentArn",
                inference_experiment_name="inferenceExperimentName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b532a236e9f5644ab601b8577c98128bdb2ef5bdf68da9dcf2746fd05154165)
            check_type(argname="argument inference_experiment_arn", value=inference_experiment_arn, expected_type=type_hints["inference_experiment_arn"])
            check_type(argname="argument inference_experiment_name", value=inference_experiment_name, expected_type=type_hints["inference_experiment_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "inference_experiment_arn": inference_experiment_arn,
            "inference_experiment_name": inference_experiment_name,
        }

    @builtins.property
    def inference_experiment_arn(self) -> builtins.str:
        '''The ARN of the InferenceExperiment resource.'''
        result = self._values.get("inference_experiment_arn")
        assert result is not None, "Required property 'inference_experiment_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def inference_experiment_name(self) -> builtins.str:
        '''The Name of the InferenceExperiment resource.'''
        result = self._values.get("inference_experiment_name")
        assert result is not None, "Required property 'inference_experiment_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InferenceExperimentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.MlflowTrackingServerReference",
    jsii_struct_bases=[],
    name_mapping={"tracking_server_name": "trackingServerName"},
)
class MlflowTrackingServerReference:
    def __init__(self, *, tracking_server_name: builtins.str) -> None:
        '''A reference to a MlflowTrackingServer resource.

        :param tracking_server_name: The TrackingServerName of the MlflowTrackingServer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            mlflow_tracking_server_reference = interfaces_sagemaker.MlflowTrackingServerReference(
                tracking_server_name="trackingServerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d99c408522f7349c897e23be4744e959306611b6fd5efc957b063d102ec92522)
            check_type(argname="argument tracking_server_name", value=tracking_server_name, expected_type=type_hints["tracking_server_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tracking_server_name": tracking_server_name,
        }

    @builtins.property
    def tracking_server_name(self) -> builtins.str:
        '''The TrackingServerName of the MlflowTrackingServer resource.'''
        result = self._values.get("tracking_server_name")
        assert result is not None, "Required property 'tracking_server_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MlflowTrackingServerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ModelBiasJobDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"job_definition_arn": "jobDefinitionArn"},
)
class ModelBiasJobDefinitionReference:
    def __init__(self, *, job_definition_arn: builtins.str) -> None:
        '''A reference to a ModelBiasJobDefinition resource.

        :param job_definition_arn: The JobDefinitionArn of the ModelBiasJobDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            model_bias_job_definition_reference = interfaces_sagemaker.ModelBiasJobDefinitionReference(
                job_definition_arn="jobDefinitionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5975e1e9188ce42ebb073ab7c379272fdeac18196793ba4480f21e139536faca)
            check_type(argname="argument job_definition_arn", value=job_definition_arn, expected_type=type_hints["job_definition_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_definition_arn": job_definition_arn,
        }

    @builtins.property
    def job_definition_arn(self) -> builtins.str:
        '''The JobDefinitionArn of the ModelBiasJobDefinition resource.'''
        result = self._values.get("job_definition_arn")
        assert result is not None, "Required property 'job_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelBiasJobDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ModelCardReference",
    jsii_struct_bases=[],
    name_mapping={
        "model_card_arn": "modelCardArn",
        "model_card_name": "modelCardName",
    },
)
class ModelCardReference:
    def __init__(
        self,
        *,
        model_card_arn: builtins.str,
        model_card_name: builtins.str,
    ) -> None:
        '''A reference to a ModelCard resource.

        :param model_card_arn: The ARN of the ModelCard resource.
        :param model_card_name: The ModelCardName of the ModelCard resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            model_card_reference = interfaces_sagemaker.ModelCardReference(
                model_card_arn="modelCardArn",
                model_card_name="modelCardName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__585b4b2caaab4bb217cdcf5e9292379439e22c8a4340180cb0280cd16ec35e45)
            check_type(argname="argument model_card_arn", value=model_card_arn, expected_type=type_hints["model_card_arn"])
            check_type(argname="argument model_card_name", value=model_card_name, expected_type=type_hints["model_card_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_card_arn": model_card_arn,
            "model_card_name": model_card_name,
        }

    @builtins.property
    def model_card_arn(self) -> builtins.str:
        '''The ARN of the ModelCard resource.'''
        result = self._values.get("model_card_arn")
        assert result is not None, "Required property 'model_card_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_card_name(self) -> builtins.str:
        '''The ModelCardName of the ModelCard resource.'''
        result = self._values.get("model_card_name")
        assert result is not None, "Required property 'model_card_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelCardReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ModelExplainabilityJobDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"job_definition_arn": "jobDefinitionArn"},
)
class ModelExplainabilityJobDefinitionReference:
    def __init__(self, *, job_definition_arn: builtins.str) -> None:
        '''A reference to a ModelExplainabilityJobDefinition resource.

        :param job_definition_arn: The JobDefinitionArn of the ModelExplainabilityJobDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            model_explainability_job_definition_reference = interfaces_sagemaker.ModelExplainabilityJobDefinitionReference(
                job_definition_arn="jobDefinitionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__338ff88c81763c3ba75192f41dd1d6104a1093708fa00c66feb46891a0d36642)
            check_type(argname="argument job_definition_arn", value=job_definition_arn, expected_type=type_hints["job_definition_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_definition_arn": job_definition_arn,
        }

    @builtins.property
    def job_definition_arn(self) -> builtins.str:
        '''The JobDefinitionArn of the ModelExplainabilityJobDefinition resource.'''
        result = self._values.get("job_definition_arn")
        assert result is not None, "Required property 'job_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelExplainabilityJobDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ModelPackageGroupReference",
    jsii_struct_bases=[],
    name_mapping={"model_package_group_arn": "modelPackageGroupArn"},
)
class ModelPackageGroupReference:
    def __init__(self, *, model_package_group_arn: builtins.str) -> None:
        '''A reference to a ModelPackageGroup resource.

        :param model_package_group_arn: The ModelPackageGroupArn of the ModelPackageGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            model_package_group_reference = interfaces_sagemaker.ModelPackageGroupReference(
                model_package_group_arn="modelPackageGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__806afa0fdfcf55a7dbed3ace5685eb72f47a2b679cc3441208fa038f86769929)
            check_type(argname="argument model_package_group_arn", value=model_package_group_arn, expected_type=type_hints["model_package_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_package_group_arn": model_package_group_arn,
        }

    @builtins.property
    def model_package_group_arn(self) -> builtins.str:
        '''The ModelPackageGroupArn of the ModelPackageGroup resource.'''
        result = self._values.get("model_package_group_arn")
        assert result is not None, "Required property 'model_package_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelPackageGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ModelPackageReference",
    jsii_struct_bases=[],
    name_mapping={"model_package_arn": "modelPackageArn"},
)
class ModelPackageReference:
    def __init__(self, *, model_package_arn: builtins.str) -> None:
        '''A reference to a ModelPackage resource.

        :param model_package_arn: The ModelPackageArn of the ModelPackage resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            model_package_reference = interfaces_sagemaker.ModelPackageReference(
                model_package_arn="modelPackageArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7ad20bc3e1fff796a212b6e948c57005cfde11a3f0866526379c06aebbab528)
            check_type(argname="argument model_package_arn", value=model_package_arn, expected_type=type_hints["model_package_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_package_arn": model_package_arn,
        }

    @builtins.property
    def model_package_arn(self) -> builtins.str:
        '''The ModelPackageArn of the ModelPackage resource.'''
        result = self._values.get("model_package_arn")
        assert result is not None, "Required property 'model_package_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelPackageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ModelQualityJobDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"job_definition_arn": "jobDefinitionArn"},
)
class ModelQualityJobDefinitionReference:
    def __init__(self, *, job_definition_arn: builtins.str) -> None:
        '''A reference to a ModelQualityJobDefinition resource.

        :param job_definition_arn: The JobDefinitionArn of the ModelQualityJobDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            model_quality_job_definition_reference = interfaces_sagemaker.ModelQualityJobDefinitionReference(
                job_definition_arn="jobDefinitionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bbb410da1ba18623b904a946e29f21cdc36bdf281f4a84f6f779158070559f7)
            check_type(argname="argument job_definition_arn", value=job_definition_arn, expected_type=type_hints["job_definition_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_definition_arn": job_definition_arn,
        }

    @builtins.property
    def job_definition_arn(self) -> builtins.str:
        '''The JobDefinitionArn of the ModelQualityJobDefinition resource.'''
        result = self._values.get("job_definition_arn")
        assert result is not None, "Required property 'job_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelQualityJobDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ModelReference",
    jsii_struct_bases=[],
    name_mapping={"model_id": "modelId", "model_name": "modelName"},
)
class ModelReference:
    def __init__(self, *, model_id: builtins.str, model_name: builtins.str) -> None:
        '''A reference to a Model resource.

        :param model_id: The Id of the Model resource.
        :param model_name: The ModelName of the Model resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            model_reference = interfaces_sagemaker.ModelReference(
                model_id="modelId",
                model_name="modelName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cd61af7df82fd40369c69cb9d02ff44230d37cd682d4ca1b498121f1cc8b4c5)
            check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            check_type(argname="argument model_name", value=model_name, expected_type=type_hints["model_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "model_id": model_id,
            "model_name": model_name,
        }

    @builtins.property
    def model_id(self) -> builtins.str:
        '''The Id of the Model resource.'''
        result = self._values.get("model_id")
        assert result is not None, "Required property 'model_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_name(self) -> builtins.str:
        '''The ModelName of the Model resource.'''
        result = self._values.get("model_name")
        assert result is not None, "Required property 'model_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.MonitoringScheduleReference",
    jsii_struct_bases=[],
    name_mapping={"monitoring_schedule_arn": "monitoringScheduleArn"},
)
class MonitoringScheduleReference:
    def __init__(self, *, monitoring_schedule_arn: builtins.str) -> None:
        '''A reference to a MonitoringSchedule resource.

        :param monitoring_schedule_arn: The MonitoringScheduleArn of the MonitoringSchedule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            monitoring_schedule_reference = interfaces_sagemaker.MonitoringScheduleReference(
                monitoring_schedule_arn="monitoringScheduleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d97efa57770ba22be684610fdc6172b3eb4efd10380b38759c295dd74f7bb31)
            check_type(argname="argument monitoring_schedule_arn", value=monitoring_schedule_arn, expected_type=type_hints["monitoring_schedule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitoring_schedule_arn": monitoring_schedule_arn,
        }

    @builtins.property
    def monitoring_schedule_arn(self) -> builtins.str:
        '''The MonitoringScheduleArn of the MonitoringSchedule resource.'''
        result = self._values.get("monitoring_schedule_arn")
        assert result is not None, "Required property 'monitoring_schedule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitoringScheduleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.NotebookInstanceLifecycleConfigReference",
    jsii_struct_bases=[],
    name_mapping={
        "notebook_instance_lifecycle_config_id": "notebookInstanceLifecycleConfigId",
        "notebook_instance_lifecycle_config_name": "notebookInstanceLifecycleConfigName",
    },
)
class NotebookInstanceLifecycleConfigReference:
    def __init__(
        self,
        *,
        notebook_instance_lifecycle_config_id: builtins.str,
        notebook_instance_lifecycle_config_name: builtins.str,
    ) -> None:
        '''A reference to a NotebookInstanceLifecycleConfig resource.

        :param notebook_instance_lifecycle_config_id: The Id of the NotebookInstanceLifecycleConfig resource.
        :param notebook_instance_lifecycle_config_name: The NotebookInstanceLifecycleConfigName of the NotebookInstanceLifecycleConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            notebook_instance_lifecycle_config_reference = interfaces_sagemaker.NotebookInstanceLifecycleConfigReference(
                notebook_instance_lifecycle_config_id="notebookInstanceLifecycleConfigId",
                notebook_instance_lifecycle_config_name="notebookInstanceLifecycleConfigName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bd4bd8843ef6d70f3dd8ae74880bf978f098b162369119c9940d295166f6c9e)
            check_type(argname="argument notebook_instance_lifecycle_config_id", value=notebook_instance_lifecycle_config_id, expected_type=type_hints["notebook_instance_lifecycle_config_id"])
            check_type(argname="argument notebook_instance_lifecycle_config_name", value=notebook_instance_lifecycle_config_name, expected_type=type_hints["notebook_instance_lifecycle_config_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "notebook_instance_lifecycle_config_id": notebook_instance_lifecycle_config_id,
            "notebook_instance_lifecycle_config_name": notebook_instance_lifecycle_config_name,
        }

    @builtins.property
    def notebook_instance_lifecycle_config_id(self) -> builtins.str:
        '''The Id of the NotebookInstanceLifecycleConfig resource.'''
        result = self._values.get("notebook_instance_lifecycle_config_id")
        assert result is not None, "Required property 'notebook_instance_lifecycle_config_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notebook_instance_lifecycle_config_name(self) -> builtins.str:
        '''The NotebookInstanceLifecycleConfigName of the NotebookInstanceLifecycleConfig resource.'''
        result = self._values.get("notebook_instance_lifecycle_config_name")
        assert result is not None, "Required property 'notebook_instance_lifecycle_config_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotebookInstanceLifecycleConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.NotebookInstanceReference",
    jsii_struct_bases=[],
    name_mapping={
        "notebook_instance_id": "notebookInstanceId",
        "notebook_instance_name": "notebookInstanceName",
    },
)
class NotebookInstanceReference:
    def __init__(
        self,
        *,
        notebook_instance_id: builtins.str,
        notebook_instance_name: builtins.str,
    ) -> None:
        '''A reference to a NotebookInstance resource.

        :param notebook_instance_id: The Id of the NotebookInstance resource.
        :param notebook_instance_name: The NotebookInstanceName of the NotebookInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            notebook_instance_reference = interfaces_sagemaker.NotebookInstanceReference(
                notebook_instance_id="notebookInstanceId",
                notebook_instance_name="notebookInstanceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a755b532c8c9e307e8c797edce2cc8a880caf510ede5ca055a88def8d821580d)
            check_type(argname="argument notebook_instance_id", value=notebook_instance_id, expected_type=type_hints["notebook_instance_id"])
            check_type(argname="argument notebook_instance_name", value=notebook_instance_name, expected_type=type_hints["notebook_instance_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "notebook_instance_id": notebook_instance_id,
            "notebook_instance_name": notebook_instance_name,
        }

    @builtins.property
    def notebook_instance_id(self) -> builtins.str:
        '''The Id of the NotebookInstance resource.'''
        result = self._values.get("notebook_instance_id")
        assert result is not None, "Required property 'notebook_instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notebook_instance_name(self) -> builtins.str:
        '''The NotebookInstanceName of the NotebookInstance resource.'''
        result = self._values.get("notebook_instance_name")
        assert result is not None, "Required property 'notebook_instance_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotebookInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.PartnerAppReference",
    jsii_struct_bases=[],
    name_mapping={"partner_app_arn": "partnerAppArn"},
)
class PartnerAppReference:
    def __init__(self, *, partner_app_arn: builtins.str) -> None:
        '''A reference to a PartnerApp resource.

        :param partner_app_arn: The Arn of the PartnerApp resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            partner_app_reference = interfaces_sagemaker.PartnerAppReference(
                partner_app_arn="partnerAppArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6626228075a70abe3bcda83e61523a68eaf55bd7ba47801143a8489c621642d0)
            check_type(argname="argument partner_app_arn", value=partner_app_arn, expected_type=type_hints["partner_app_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "partner_app_arn": partner_app_arn,
        }

    @builtins.property
    def partner_app_arn(self) -> builtins.str:
        '''The Arn of the PartnerApp resource.'''
        result = self._values.get("partner_app_arn")
        assert result is not None, "Required property 'partner_app_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PartnerAppReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.PipelineReference",
    jsii_struct_bases=[],
    name_mapping={"pipeline_name": "pipelineName"},
)
class PipelineReference:
    def __init__(self, *, pipeline_name: builtins.str) -> None:
        '''A reference to a Pipeline resource.

        :param pipeline_name: The PipelineName of the Pipeline resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            pipeline_reference = interfaces_sagemaker.PipelineReference(
                pipeline_name="pipelineName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad9acc2ace51dbdf01b438f91968bd738f36794a0975b7dffb9facf7d427bb1b)
            check_type(argname="argument pipeline_name", value=pipeline_name, expected_type=type_hints["pipeline_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pipeline_name": pipeline_name,
        }

    @builtins.property
    def pipeline_name(self) -> builtins.str:
        '''The PipelineName of the Pipeline resource.'''
        result = self._values.get("pipeline_name")
        assert result is not None, "Required property 'pipeline_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PipelineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ProcessingJobReference",
    jsii_struct_bases=[],
    name_mapping={"processing_job_arn": "processingJobArn"},
)
class ProcessingJobReference:
    def __init__(self, *, processing_job_arn: builtins.str) -> None:
        '''A reference to a ProcessingJob resource.

        :param processing_job_arn: The ProcessingJobArn of the ProcessingJob resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            processing_job_reference = interfaces_sagemaker.ProcessingJobReference(
                processing_job_arn="processingJobArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28ca4f390d63827e5d80cbe193cd18d766e8487d3a3b2bfa5882ac83e75f29dc)
            check_type(argname="argument processing_job_arn", value=processing_job_arn, expected_type=type_hints["processing_job_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "processing_job_arn": processing_job_arn,
        }

    @builtins.property
    def processing_job_arn(self) -> builtins.str:
        '''The ProcessingJobArn of the ProcessingJob resource.'''
        result = self._values.get("processing_job_arn")
        assert result is not None, "Required property 'processing_job_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProcessingJobReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.ProjectReference",
    jsii_struct_bases=[],
    name_mapping={"project_arn": "projectArn"},
)
class ProjectReference:
    def __init__(self, *, project_arn: builtins.str) -> None:
        '''A reference to a Project resource.

        :param project_arn: The ProjectArn of the Project resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            project_reference = interfaces_sagemaker.ProjectReference(
                project_arn="projectArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dbf30c5cad56a5319c780818fab0e1ecabcd4ca3510888e70ca4e4a4440da7e)
            check_type(argname="argument project_arn", value=project_arn, expected_type=type_hints["project_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_arn": project_arn,
        }

    @builtins.property
    def project_arn(self) -> builtins.str:
        '''The ProjectArn of the Project resource.'''
        result = self._values.get("project_arn")
        assert result is not None, "Required property 'project_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.SpaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_id": "domainId",
        "space_arn": "spaceArn",
        "space_name": "spaceName",
    },
)
class SpaceReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        space_arn: builtins.str,
        space_name: builtins.str,
    ) -> None:
        '''A reference to a Space resource.

        :param domain_id: The DomainId of the Space resource.
        :param space_arn: The ARN of the Space resource.
        :param space_name: The SpaceName of the Space resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            space_reference = interfaces_sagemaker.SpaceReference(
                domain_id="domainId",
                space_arn="spaceArn",
                space_name="spaceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__960b6b3f1e6407778e534a453c19051ff7b4ab7231ac395afdc47214610602eb)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument space_arn", value=space_arn, expected_type=type_hints["space_arn"])
            check_type(argname="argument space_name", value=space_name, expected_type=type_hints["space_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "space_arn": space_arn,
            "space_name": space_name,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the Space resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def space_arn(self) -> builtins.str:
        '''The ARN of the Space resource.'''
        result = self._values.get("space_arn")
        assert result is not None, "Required property 'space_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def space_name(self) -> builtins.str:
        '''The SpaceName of the Space resource.'''
        result = self._values.get("space_name")
        assert result is not None, "Required property 'space_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.StudioLifecycleConfigReference",
    jsii_struct_bases=[],
    name_mapping={
        "studio_lifecycle_config_arn": "studioLifecycleConfigArn",
        "studio_lifecycle_config_name": "studioLifecycleConfigName",
    },
)
class StudioLifecycleConfigReference:
    def __init__(
        self,
        *,
        studio_lifecycle_config_arn: builtins.str,
        studio_lifecycle_config_name: builtins.str,
    ) -> None:
        '''A reference to a StudioLifecycleConfig resource.

        :param studio_lifecycle_config_arn: The ARN of the StudioLifecycleConfig resource.
        :param studio_lifecycle_config_name: The StudioLifecycleConfigName of the StudioLifecycleConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            studio_lifecycle_config_reference = interfaces_sagemaker.StudioLifecycleConfigReference(
                studio_lifecycle_config_arn="studioLifecycleConfigArn",
                studio_lifecycle_config_name="studioLifecycleConfigName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb952dd8843aa4f3071a4649857357f9cf5f6ee34b859ebafd283f7013f0c67d)
            check_type(argname="argument studio_lifecycle_config_arn", value=studio_lifecycle_config_arn, expected_type=type_hints["studio_lifecycle_config_arn"])
            check_type(argname="argument studio_lifecycle_config_name", value=studio_lifecycle_config_name, expected_type=type_hints["studio_lifecycle_config_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "studio_lifecycle_config_arn": studio_lifecycle_config_arn,
            "studio_lifecycle_config_name": studio_lifecycle_config_name,
        }

    @builtins.property
    def studio_lifecycle_config_arn(self) -> builtins.str:
        '''The ARN of the StudioLifecycleConfig resource.'''
        result = self._values.get("studio_lifecycle_config_arn")
        assert result is not None, "Required property 'studio_lifecycle_config_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_lifecycle_config_name(self) -> builtins.str:
        '''The StudioLifecycleConfigName of the StudioLifecycleConfig resource.'''
        result = self._values.get("studio_lifecycle_config_name")
        assert result is not None, "Required property 'studio_lifecycle_config_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StudioLifecycleConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.UserProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_id": "domainId",
        "user_profile_arn": "userProfileArn",
        "user_profile_name": "userProfileName",
    },
)
class UserProfileReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        user_profile_arn: builtins.str,
        user_profile_name: builtins.str,
    ) -> None:
        '''A reference to a UserProfile resource.

        :param domain_id: The DomainId of the UserProfile resource.
        :param user_profile_arn: The ARN of the UserProfile resource.
        :param user_profile_name: The UserProfileName of the UserProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            user_profile_reference = interfaces_sagemaker.UserProfileReference(
                domain_id="domainId",
                user_profile_arn="userProfileArn",
                user_profile_name="userProfileName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c8b4ff7d349ddb3632965b5498543cbf7e6d497d2d7bc15f093cf6cf3f84ace)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument user_profile_arn", value=user_profile_arn, expected_type=type_hints["user_profile_arn"])
            check_type(argname="argument user_profile_name", value=user_profile_name, expected_type=type_hints["user_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "user_profile_arn": user_profile_arn,
            "user_profile_name": user_profile_name,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the UserProfile resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_profile_arn(self) -> builtins.str:
        '''The ARN of the UserProfile resource.'''
        result = self._values.get("user_profile_arn")
        assert result is not None, "Required property 'user_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_profile_name(self) -> builtins.str:
        '''The UserProfileName of the UserProfile resource.'''
        result = self._values.get("user_profile_name")
        assert result is not None, "Required property 'user_profile_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sagemaker.WorkteamReference",
    jsii_struct_bases=[],
    name_mapping={"workteam_id": "workteamId", "workteam_name": "workteamName"},
)
class WorkteamReference:
    def __init__(
        self,
        *,
        workteam_id: builtins.str,
        workteam_name: builtins.str,
    ) -> None:
        '''A reference to a Workteam resource.

        :param workteam_id: The Id of the Workteam resource.
        :param workteam_name: The WorkteamName of the Workteam resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sagemaker as interfaces_sagemaker
            
            workteam_reference = interfaces_sagemaker.WorkteamReference(
                workteam_id="workteamId",
                workteam_name="workteamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57fcc1ca690db91207cd9de5695c57ca45d13772e64730ab43c815d1704cc2b9)
            check_type(argname="argument workteam_id", value=workteam_id, expected_type=type_hints["workteam_id"])
            check_type(argname="argument workteam_name", value=workteam_name, expected_type=type_hints["workteam_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workteam_id": workteam_id,
            "workteam_name": workteam_name,
        }

    @builtins.property
    def workteam_id(self) -> builtins.str:
        '''The Id of the Workteam resource.'''
        result = self._values.get("workteam_id")
        assert result is not None, "Required property 'workteam_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workteam_name(self) -> builtins.str:
        '''The WorkteamName of the Workteam resource.'''
        result = self._values.get("workteam_name")
        assert result is not None, "Required property 'workteam_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkteamReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppImageConfigReference",
    "AppReference",
    "ClusterReference",
    "CodeRepositoryReference",
    "DataQualityJobDefinitionReference",
    "DeviceFleetReference",
    "DeviceReference",
    "DomainReference",
    "EndpointConfigReference",
    "EndpointReference",
    "FeatureGroupReference",
    "IAppImageConfigRef",
    "IAppRef",
    "IClusterRef",
    "ICodeRepositoryRef",
    "IDataQualityJobDefinitionRef",
    "IDeviceFleetRef",
    "IDeviceRef",
    "IDomainRef",
    "IEndpointConfigRef",
    "IEndpointRef",
    "IFeatureGroupRef",
    "IImageRef",
    "IImageVersionRef",
    "IInferenceComponentRef",
    "IInferenceExperimentRef",
    "IMlflowTrackingServerRef",
    "IModelBiasJobDefinitionRef",
    "IModelCardRef",
    "IModelExplainabilityJobDefinitionRef",
    "IModelPackageGroupRef",
    "IModelPackageRef",
    "IModelQualityJobDefinitionRef",
    "IModelRef",
    "IMonitoringScheduleRef",
    "INotebookInstanceLifecycleConfigRef",
    "INotebookInstanceRef",
    "IPartnerAppRef",
    "IPipelineRef",
    "IProcessingJobRef",
    "IProjectRef",
    "ISpaceRef",
    "IStudioLifecycleConfigRef",
    "IUserProfileRef",
    "IWorkteamRef",
    "ImageReference",
    "ImageVersionReference",
    "InferenceComponentReference",
    "InferenceExperimentReference",
    "MlflowTrackingServerReference",
    "ModelBiasJobDefinitionReference",
    "ModelCardReference",
    "ModelExplainabilityJobDefinitionReference",
    "ModelPackageGroupReference",
    "ModelPackageReference",
    "ModelQualityJobDefinitionReference",
    "ModelReference",
    "MonitoringScheduleReference",
    "NotebookInstanceLifecycleConfigReference",
    "NotebookInstanceReference",
    "PartnerAppReference",
    "PipelineReference",
    "ProcessingJobReference",
    "ProjectReference",
    "SpaceReference",
    "StudioLifecycleConfigReference",
    "UserProfileReference",
    "WorkteamReference",
]

publication.publish()

def _typecheckingstub__8605a0bbddb7566b87d731e87346f01eed74a7a840b35f21894ff7b04efe109a(
    *,
    app_image_config_arn: builtins.str,
    app_image_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acf6b4a544b0ae2c52d54ce3ceff8c75d3dcd96d513a527222edb518b2378b61(
    *,
    app_arn: builtins.str,
    app_name: builtins.str,
    app_type: builtins.str,
    domain_id: builtins.str,
    user_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b41740c83d2043a3c12795517b06ef5392e313ddf64f0baf09ea7a2ce947048c(
    *,
    cluster_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d50203d0b8619bba87d6272a7d3180c525e4133465ac661135be4365a5902520(
    *,
    code_repository_id: builtins.str,
    code_repository_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b50ea0229d7c5b363f40e378afed722f72bc9584c588e33961e55a8acd85a7d(
    *,
    job_definition_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b9a733d992a034e2946905dc4f6aea8cb11d66ab8a69578e5ec6f5ac02a78c1(
    *,
    device_fleet_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e91123dc160df144def6083969becc0cfa03100ce49a86dbd47dbc531c40dc4(
    *,
    device_fleet_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b051cfa5b56c2c44861ce067c6e3e2b5ff6bc49d74d2a599515c501b0884167(
    *,
    domain_arn: builtins.str,
    domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__671b59e91ff91baea0cef8d7d45d4100318e43b4ba27225394b64570ce952f45(
    *,
    endpoint_config_id: builtins.str,
    endpoint_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba07aa533865a76289f1b8ba76c2ae9b68760c1195553f601d11a7addf968c43(
    *,
    endpoint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0043c65a11b7af9fa8bd64a420c0be15fb3226e8c86d9153a34ccb0e0c57f82b(
    *,
    feature_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84c8da85f1097ad468daeebaf96185535637ac444b0d540b6b2c7e24ae5f23b6(
    *,
    image_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49ddecb7633f51ab5122ae78f78bcdbad2e65eb4e6e17e13971b80a156e849c2(
    *,
    image_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb0712a1d37391a9ac27801c64ffce4938819ecc0068f44355fc8c66d46f11c(
    *,
    inference_component_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b532a236e9f5644ab601b8577c98128bdb2ef5bdf68da9dcf2746fd05154165(
    *,
    inference_experiment_arn: builtins.str,
    inference_experiment_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d99c408522f7349c897e23be4744e959306611b6fd5efc957b063d102ec92522(
    *,
    tracking_server_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5975e1e9188ce42ebb073ab7c379272fdeac18196793ba4480f21e139536faca(
    *,
    job_definition_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__585b4b2caaab4bb217cdcf5e9292379439e22c8a4340180cb0280cd16ec35e45(
    *,
    model_card_arn: builtins.str,
    model_card_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__338ff88c81763c3ba75192f41dd1d6104a1093708fa00c66feb46891a0d36642(
    *,
    job_definition_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__806afa0fdfcf55a7dbed3ace5685eb72f47a2b679cc3441208fa038f86769929(
    *,
    model_package_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7ad20bc3e1fff796a212b6e948c57005cfde11a3f0866526379c06aebbab528(
    *,
    model_package_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bbb410da1ba18623b904a946e29f21cdc36bdf281f4a84f6f779158070559f7(
    *,
    job_definition_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd61af7df82fd40369c69cb9d02ff44230d37cd682d4ca1b498121f1cc8b4c5(
    *,
    model_id: builtins.str,
    model_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d97efa57770ba22be684610fdc6172b3eb4efd10380b38759c295dd74f7bb31(
    *,
    monitoring_schedule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bd4bd8843ef6d70f3dd8ae74880bf978f098b162369119c9940d295166f6c9e(
    *,
    notebook_instance_lifecycle_config_id: builtins.str,
    notebook_instance_lifecycle_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a755b532c8c9e307e8c797edce2cc8a880caf510ede5ca055a88def8d821580d(
    *,
    notebook_instance_id: builtins.str,
    notebook_instance_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6626228075a70abe3bcda83e61523a68eaf55bd7ba47801143a8489c621642d0(
    *,
    partner_app_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad9acc2ace51dbdf01b438f91968bd738f36794a0975b7dffb9facf7d427bb1b(
    *,
    pipeline_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ca4f390d63827e5d80cbe193cd18d766e8487d3a3b2bfa5882ac83e75f29dc(
    *,
    processing_job_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dbf30c5cad56a5319c780818fab0e1ecabcd4ca3510888e70ca4e4a4440da7e(
    *,
    project_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__960b6b3f1e6407778e534a453c19051ff7b4ab7231ac395afdc47214610602eb(
    *,
    domain_id: builtins.str,
    space_arn: builtins.str,
    space_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb952dd8843aa4f3071a4649857357f9cf5f6ee34b859ebafd283f7013f0c67d(
    *,
    studio_lifecycle_config_arn: builtins.str,
    studio_lifecycle_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8b4ff7d349ddb3632965b5498543cbf7e6d497d2d7bc15f093cf6cf3f84ace(
    *,
    domain_id: builtins.str,
    user_profile_arn: builtins.str,
    user_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57fcc1ca690db91207cd9de5695c57ca45d13772e64730ab43c815d1704cc2b9(
    *,
    workteam_id: builtins.str,
    workteam_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAppImageConfigRef, IAppRef, IClusterRef, ICodeRepositoryRef, IDataQualityJobDefinitionRef, IDeviceFleetRef, IDeviceRef, IDomainRef, IEndpointConfigRef, IEndpointRef, IFeatureGroupRef, IImageRef, IImageVersionRef, IInferenceComponentRef, IInferenceExperimentRef, IMlflowTrackingServerRef, IModelBiasJobDefinitionRef, IModelCardRef, IModelExplainabilityJobDefinitionRef, IModelPackageGroupRef, IModelPackageRef, IModelQualityJobDefinitionRef, IModelRef, IMonitoringScheduleRef, INotebookInstanceLifecycleConfigRef, INotebookInstanceRef, IPartnerAppRef, IPipelineRef, IProcessingJobRef, IProjectRef, ISpaceRef, IStudioLifecycleConfigRef, IUserProfileRef, IWorkteamRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
