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
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.ConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"connection_id": "connectionId", "domain_id": "domainId"},
)
class ConnectionReference:
    def __init__(self, *, connection_id: builtins.str, domain_id: builtins.str) -> None:
        '''A reference to a Connection resource.

        :param connection_id: The ConnectionId of the Connection resource.
        :param domain_id: The DomainId of the Connection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            connection_reference = interfaces_datazone.ConnectionReference(
                connection_id="connectionId",
                domain_id="domainId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f7850fde9fef51a80e2d06ac28cd4fe81de985a525e994d643ac6d109536637)
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_id": connection_id,
            "domain_id": domain_id,
        }

    @builtins.property
    def connection_id(self) -> builtins.str:
        '''The ConnectionId of the Connection resource.'''
        result = self._values.get("connection_id")
        assert result is not None, "Required property 'connection_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the Connection resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.DataSourceReference",
    jsii_struct_bases=[],
    name_mapping={"data_source_id": "dataSourceId", "domain_id": "domainId"},
)
class DataSourceReference:
    def __init__(
        self,
        *,
        data_source_id: builtins.str,
        domain_id: builtins.str,
    ) -> None:
        '''A reference to a DataSource resource.

        :param data_source_id: The Id of the DataSource resource.
        :param domain_id: The DomainId of the DataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            data_source_reference = interfaces_datazone.DataSourceReference(
                data_source_id="dataSourceId",
                domain_id="domainId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6871dc8841d605ea74965422b16e2a095c2fa3cefc233d56325c05b81d859c3a)
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_id": data_source_id,
            "domain_id": domain_id,
        }

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The Id of the DataSource resource.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the DataSource resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.DomainReference",
    jsii_struct_bases=[],
    name_mapping={"domain_arn": "domainArn", "domain_id": "domainId"},
)
class DomainReference:
    def __init__(self, *, domain_arn: builtins.str, domain_id: builtins.str) -> None:
        '''A reference to a Domain resource.

        :param domain_arn: The ARN of the Domain resource.
        :param domain_id: The Id of the Domain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            domain_reference = interfaces_datazone.DomainReference(
                domain_arn="domainArn",
                domain_id="domainId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb767451ab5e19a7b28b12c6fceb9e1a1d5fd6b93294c9455242952d67797a9e)
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
        '''The Id of the Domain resource.'''
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
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.DomainUnitReference",
    jsii_struct_bases=[],
    name_mapping={"domain_id": "domainId", "domain_unit_id": "domainUnitId"},
)
class DomainUnitReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        domain_unit_id: builtins.str,
    ) -> None:
        '''A reference to a DomainUnit resource.

        :param domain_id: The DomainId of the DomainUnit resource.
        :param domain_unit_id: The Id of the DomainUnit resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            domain_unit_reference = interfaces_datazone.DomainUnitReference(
                domain_id="domainId",
                domain_unit_id="domainUnitId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4c196b765e57c342c351f2229a31f253bc5dfd9e3885706168310286ca0c2c2)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument domain_unit_id", value=domain_unit_id, expected_type=type_hints["domain_unit_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "domain_unit_id": domain_unit_id,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the DomainUnit resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_unit_id(self) -> builtins.str:
        '''The Id of the DomainUnit resource.'''
        result = self._values.get("domain_unit_id")
        assert result is not None, "Required property 'domain_unit_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainUnitReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.EnvironmentActionsReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_id": "domainId",
        "environment_actions_id": "environmentActionsId",
        "environment_id": "environmentId",
    },
)
class EnvironmentActionsReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        environment_actions_id: builtins.str,
        environment_id: builtins.str,
    ) -> None:
        '''A reference to a EnvironmentActions resource.

        :param domain_id: The DomainId of the EnvironmentActions resource.
        :param environment_actions_id: The Id of the EnvironmentActions resource.
        :param environment_id: The EnvironmentId of the EnvironmentActions resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            environment_actions_reference = interfaces_datazone.EnvironmentActionsReference(
                domain_id="domainId",
                environment_actions_id="environmentActionsId",
                environment_id="environmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d0a753cfdc48e1908e540974b3fb1b37607132b5a1c7ba25ad51caaa8689c75)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument environment_actions_id", value=environment_actions_id, expected_type=type_hints["environment_actions_id"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "environment_actions_id": environment_actions_id,
            "environment_id": environment_id,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the EnvironmentActions resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_actions_id(self) -> builtins.str:
        '''The Id of the EnvironmentActions resource.'''
        result = self._values.get("environment_actions_id")
        assert result is not None, "Required property 'environment_actions_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''The EnvironmentId of the EnvironmentActions resource.'''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentActionsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.EnvironmentBlueprintConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_id": "domainId",
        "environment_blueprint_id": "environmentBlueprintId",
    },
)
class EnvironmentBlueprintConfigurationReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        environment_blueprint_id: builtins.str,
    ) -> None:
        '''A reference to a EnvironmentBlueprintConfiguration resource.

        :param domain_id: The DomainId of the EnvironmentBlueprintConfiguration resource.
        :param environment_blueprint_id: The EnvironmentBlueprintId of the EnvironmentBlueprintConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            environment_blueprint_configuration_reference = interfaces_datazone.EnvironmentBlueprintConfigurationReference(
                domain_id="domainId",
                environment_blueprint_id="environmentBlueprintId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3dfe34b538dd9e6fb1f8301a81eeb9b47a3c4d9878ab58c0ea301dbfa5d6053)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument environment_blueprint_id", value=environment_blueprint_id, expected_type=type_hints["environment_blueprint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "environment_blueprint_id": environment_blueprint_id,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the EnvironmentBlueprintConfiguration resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_blueprint_id(self) -> builtins.str:
        '''The EnvironmentBlueprintId of the EnvironmentBlueprintConfiguration resource.'''
        result = self._values.get("environment_blueprint_id")
        assert result is not None, "Required property 'environment_blueprint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentBlueprintConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.EnvironmentProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_id": "domainId",
        "environment_profile_id": "environmentProfileId",
    },
)
class EnvironmentProfileReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        environment_profile_id: builtins.str,
    ) -> None:
        '''A reference to a EnvironmentProfile resource.

        :param domain_id: The DomainId of the EnvironmentProfile resource.
        :param environment_profile_id: The Id of the EnvironmentProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            environment_profile_reference = interfaces_datazone.EnvironmentProfileReference(
                domain_id="domainId",
                environment_profile_id="environmentProfileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e5797ce9ff71fb7ca1f857bfc1ebc8de57d2694bac8c3e1880544b1d5d106ec)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument environment_profile_id", value=environment_profile_id, expected_type=type_hints["environment_profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "environment_profile_id": environment_profile_id,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the EnvironmentProfile resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_profile_id(self) -> builtins.str:
        '''The Id of the EnvironmentProfile resource.'''
        result = self._values.get("environment_profile_id")
        assert result is not None, "Required property 'environment_profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.EnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={"domain_id": "domainId", "environment_id": "environmentId"},
)
class EnvironmentReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        environment_id: builtins.str,
    ) -> None:
        '''A reference to a Environment resource.

        :param domain_id: The DomainId of the Environment resource.
        :param environment_id: The Id of the Environment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            environment_reference = interfaces_datazone.EnvironmentReference(
                domain_id="domainId",
                environment_id="environmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0598aa1fd0986ce9b7c3b0e4fd6a9a5f144a1fd6d959bf12f7dd2e000ba97a25)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "environment_id": environment_id,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the Environment resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''The Id of the Environment resource.'''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.FormTypeReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "form_type_identifier": "formTypeIdentifier",
    },
)
class FormTypeReference:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        form_type_identifier: builtins.str,
    ) -> None:
        '''A reference to a FormType resource.

        :param domain_identifier: The DomainIdentifier of the FormType resource.
        :param form_type_identifier: The FormTypeIdentifier of the FormType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            form_type_reference = interfaces_datazone.FormTypeReference(
                domain_identifier="domainIdentifier",
                form_type_identifier="formTypeIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab76ee3af4baa56b49082234e89d0e064c6abd968ab7a49bbc66020a57c938dc)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument form_type_identifier", value=form_type_identifier, expected_type=type_hints["form_type_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "form_type_identifier": form_type_identifier,
        }

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The DomainIdentifier of the FormType resource.'''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def form_type_identifier(self) -> builtins.str:
        '''The FormTypeIdentifier of the FormType resource.'''
        result = self._values.get("form_type_identifier")
        assert result is not None, "Required property 'form_type_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FormTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.GroupProfileReference",
    jsii_struct_bases=[],
    name_mapping={"domain_id": "domainId", "group_profile_id": "groupProfileId"},
)
class GroupProfileReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        group_profile_id: builtins.str,
    ) -> None:
        '''A reference to a GroupProfile resource.

        :param domain_id: The DomainId of the GroupProfile resource.
        :param group_profile_id: The Id of the GroupProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            group_profile_reference = interfaces_datazone.GroupProfileReference(
                domain_id="domainId",
                group_profile_id="groupProfileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91a1b5d0de041d5e3b32120d7f53ca62f70d31a4e431952ebbc8e9d9c3896096)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument group_profile_id", value=group_profile_id, expected_type=type_hints["group_profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "group_profile_id": group_profile_id,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the GroupProfile resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_profile_id(self) -> builtins.str:
        '''The Id of the GroupProfile resource.'''
        result = self._values.get("group_profile_id")
        assert result is not None, "Required property 'group_profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IConnectionRef")
class IConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        ...


class _IConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionReference", jsii.get(self, "connectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionRef).__jsii_proxy_class__ = lambda : _IConnectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IDataSourceRef")
class IDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        ...


class _IDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        return typing.cast("DataSourceReference", jsii.get(self, "dataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSourceRef).__jsii_proxy_class__ = lambda : _IDataSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IDomainRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IDomainRef"

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        return typing.cast("DomainReference", jsii.get(self, "domainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainRef).__jsii_proxy_class__ = lambda : _IDomainRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IDomainUnitRef")
class IDomainUnitRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DomainUnit.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainUnitRef")
    def domain_unit_ref(self) -> "DomainUnitReference":
        '''(experimental) A reference to a DomainUnit resource.

        :stability: experimental
        '''
        ...


class _IDomainUnitRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DomainUnit.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IDomainUnitRef"

    @builtins.property
    @jsii.member(jsii_name="domainUnitRef")
    def domain_unit_ref(self) -> "DomainUnitReference":
        '''(experimental) A reference to a DomainUnit resource.

        :stability: experimental
        '''
        return typing.cast("DomainUnitReference", jsii.get(self, "domainUnitRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainUnitRef).__jsii_proxy_class__ = lambda : _IDomainUnitRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IEnvironmentActionsRef")
class IEnvironmentActionsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentActions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentActionsRef")
    def environment_actions_ref(self) -> "EnvironmentActionsReference":
        '''(experimental) A reference to a EnvironmentActions resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentActionsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentActions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IEnvironmentActionsRef"

    @builtins.property
    @jsii.member(jsii_name="environmentActionsRef")
    def environment_actions_ref(self) -> "EnvironmentActionsReference":
        '''(experimental) A reference to a EnvironmentActions resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentActionsReference", jsii.get(self, "environmentActionsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentActionsRef).__jsii_proxy_class__ = lambda : _IEnvironmentActionsRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.IEnvironmentBlueprintConfigurationRef"
)
class IEnvironmentBlueprintConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentBlueprintConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentBlueprintConfigurationRef")
    def environment_blueprint_configuration_ref(
        self,
    ) -> "EnvironmentBlueprintConfigurationReference":
        '''(experimental) A reference to a EnvironmentBlueprintConfiguration resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentBlueprintConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentBlueprintConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IEnvironmentBlueprintConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="environmentBlueprintConfigurationRef")
    def environment_blueprint_configuration_ref(
        self,
    ) -> "EnvironmentBlueprintConfigurationReference":
        '''(experimental) A reference to a EnvironmentBlueprintConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentBlueprintConfigurationReference", jsii.get(self, "environmentBlueprintConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentBlueprintConfigurationRef).__jsii_proxy_class__ = lambda : _IEnvironmentBlueprintConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IEnvironmentProfileRef")
class IEnvironmentProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentProfileRef")
    def environment_profile_ref(self) -> "EnvironmentProfileReference":
        '''(experimental) A reference to a EnvironmentProfile resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EnvironmentProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IEnvironmentProfileRef"

    @builtins.property
    @jsii.member(jsii_name="environmentProfileRef")
    def environment_profile_ref(self) -> "EnvironmentProfileReference":
        '''(experimental) A reference to a EnvironmentProfile resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentProfileReference", jsii.get(self, "environmentProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentProfileRef).__jsii_proxy_class__ = lambda : _IEnvironmentProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IEnvironmentRef")
class IEnvironmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IEnvironmentRef"

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentReference", jsii.get(self, "environmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentRef).__jsii_proxy_class__ = lambda : _IEnvironmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IFormTypeRef")
class IFormTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FormType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="formTypeRef")
    def form_type_ref(self) -> "FormTypeReference":
        '''(experimental) A reference to a FormType resource.

        :stability: experimental
        '''
        ...


class _IFormTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FormType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IFormTypeRef"

    @builtins.property
    @jsii.member(jsii_name="formTypeRef")
    def form_type_ref(self) -> "FormTypeReference":
        '''(experimental) A reference to a FormType resource.

        :stability: experimental
        '''
        return typing.cast("FormTypeReference", jsii.get(self, "formTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFormTypeRef).__jsii_proxy_class__ = lambda : _IFormTypeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IGroupProfileRef")
class IGroupProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GroupProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="groupProfileRef")
    def group_profile_ref(self) -> "GroupProfileReference":
        '''(experimental) A reference to a GroupProfile resource.

        :stability: experimental
        '''
        ...


class _IGroupProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GroupProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IGroupProfileRef"

    @builtins.property
    @jsii.member(jsii_name="groupProfileRef")
    def group_profile_ref(self) -> "GroupProfileReference":
        '''(experimental) A reference to a GroupProfile resource.

        :stability: experimental
        '''
        return typing.cast("GroupProfileReference", jsii.get(self, "groupProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupProfileRef).__jsii_proxy_class__ = lambda : _IGroupProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IOwnerRef")
class IOwnerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Owner.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ownerRef")
    def owner_ref(self) -> "OwnerReference":
        '''(experimental) A reference to a Owner resource.

        :stability: experimental
        '''
        ...


class _IOwnerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Owner.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IOwnerRef"

    @builtins.property
    @jsii.member(jsii_name="ownerRef")
    def owner_ref(self) -> "OwnerReference":
        '''(experimental) A reference to a Owner resource.

        :stability: experimental
        '''
        return typing.cast("OwnerReference", jsii.get(self, "ownerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOwnerRef).__jsii_proxy_class__ = lambda : _IOwnerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IPolicyGrantRef")
class IPolicyGrantRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyGrant.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="policyGrantRef")
    def policy_grant_ref(self) -> "PolicyGrantReference":
        '''(experimental) A reference to a PolicyGrant resource.

        :stability: experimental
        '''
        ...


class _IPolicyGrantRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyGrant.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IPolicyGrantRef"

    @builtins.property
    @jsii.member(jsii_name="policyGrantRef")
    def policy_grant_ref(self) -> "PolicyGrantReference":
        '''(experimental) A reference to a PolicyGrant resource.

        :stability: experimental
        '''
        return typing.cast("PolicyGrantReference", jsii.get(self, "policyGrantRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyGrantRef).__jsii_proxy_class__ = lambda : _IPolicyGrantRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IProjectMembershipRef")
class IProjectMembershipRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProjectMembership.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="projectMembershipRef")
    def project_membership_ref(self) -> "ProjectMembershipReference":
        '''(experimental) A reference to a ProjectMembership resource.

        :stability: experimental
        '''
        ...


class _IProjectMembershipRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProjectMembership.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IProjectMembershipRef"

    @builtins.property
    @jsii.member(jsii_name="projectMembershipRef")
    def project_membership_ref(self) -> "ProjectMembershipReference":
        '''(experimental) A reference to a ProjectMembership resource.

        :stability: experimental
        '''
        return typing.cast("ProjectMembershipReference", jsii.get(self, "projectMembershipRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectMembershipRef).__jsii_proxy_class__ = lambda : _IProjectMembershipRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IProjectProfileRef")
class IProjectProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProjectProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="projectProfileRef")
    def project_profile_ref(self) -> "ProjectProfileReference":
        '''(experimental) A reference to a ProjectProfile resource.

        :stability: experimental
        '''
        ...


class _IProjectProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProjectProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IProjectProfileRef"

    @builtins.property
    @jsii.member(jsii_name="projectProfileRef")
    def project_profile_ref(self) -> "ProjectProfileReference":
        '''(experimental) A reference to a ProjectProfile resource.

        :stability: experimental
        '''
        return typing.cast("ProjectProfileReference", jsii.get(self, "projectProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectProfileRef).__jsii_proxy_class__ = lambda : _IProjectProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IProjectRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IProjectRef"

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        return typing.cast("ProjectReference", jsii.get(self, "projectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectRef).__jsii_proxy_class__ = lambda : _IProjectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.ISubscriptionTargetRef")
class ISubscriptionTargetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriptionTarget.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subscriptionTargetRef")
    def subscription_target_ref(self) -> "SubscriptionTargetReference":
        '''(experimental) A reference to a SubscriptionTarget resource.

        :stability: experimental
        '''
        ...


class _ISubscriptionTargetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriptionTarget.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.ISubscriptionTargetRef"

    @builtins.property
    @jsii.member(jsii_name="subscriptionTargetRef")
    def subscription_target_ref(self) -> "SubscriptionTargetReference":
        '''(experimental) A reference to a SubscriptionTarget resource.

        :stability: experimental
        '''
        return typing.cast("SubscriptionTargetReference", jsii.get(self, "subscriptionTargetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubscriptionTargetRef).__jsii_proxy_class__ = lambda : _ISubscriptionTargetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_datazone.IUserProfileRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_datazone.IUserProfileRef"

    @builtins.property
    @jsii.member(jsii_name="userProfileRef")
    def user_profile_ref(self) -> "UserProfileReference":
        '''(experimental) A reference to a UserProfile resource.

        :stability: experimental
        '''
        return typing.cast("UserProfileReference", jsii.get(self, "userProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserProfileRef).__jsii_proxy_class__ = lambda : _IUserProfileRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.OwnerReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "entity_identifier": "entityIdentifier",
        "entity_type": "entityType",
        "owner_identifier": "ownerIdentifier",
        "owner_type": "ownerType",
    },
)
class OwnerReference:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        entity_identifier: builtins.str,
        entity_type: builtins.str,
        owner_identifier: builtins.str,
        owner_type: builtins.str,
    ) -> None:
        '''A reference to a Owner resource.

        :param domain_identifier: The DomainIdentifier of the Owner resource.
        :param entity_identifier: The EntityIdentifier of the Owner resource.
        :param entity_type: The EntityType of the Owner resource.
        :param owner_identifier: The OwnerIdentifier of the Owner resource.
        :param owner_type: The OwnerType of the Owner resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            owner_reference = interfaces_datazone.OwnerReference(
                domain_identifier="domainIdentifier",
                entity_identifier="entityIdentifier",
                entity_type="entityType",
                owner_identifier="ownerIdentifier",
                owner_type="ownerType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24300f06c1e5be24db2bc08d9fc81f2d86bc7593405c538c43faa80a3af368d2)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument entity_identifier", value=entity_identifier, expected_type=type_hints["entity_identifier"])
            check_type(argname="argument entity_type", value=entity_type, expected_type=type_hints["entity_type"])
            check_type(argname="argument owner_identifier", value=owner_identifier, expected_type=type_hints["owner_identifier"])
            check_type(argname="argument owner_type", value=owner_type, expected_type=type_hints["owner_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "owner_identifier": owner_identifier,
            "owner_type": owner_type,
        }

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The DomainIdentifier of the Owner resource.'''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entity_identifier(self) -> builtins.str:
        '''The EntityIdentifier of the Owner resource.'''
        result = self._values.get("entity_identifier")
        assert result is not None, "Required property 'entity_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entity_type(self) -> builtins.str:
        '''The EntityType of the Owner resource.'''
        result = self._values.get("entity_type")
        assert result is not None, "Required property 'entity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def owner_identifier(self) -> builtins.str:
        '''The OwnerIdentifier of the Owner resource.'''
        result = self._values.get("owner_identifier")
        assert result is not None, "Required property 'owner_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def owner_type(self) -> builtins.str:
        '''The OwnerType of the Owner resource.'''
        result = self._values.get("owner_type")
        assert result is not None, "Required property 'owner_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OwnerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.PolicyGrantReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "entity_identifier": "entityIdentifier",
        "entity_type": "entityType",
        "grant_id": "grantId",
        "policy_type": "policyType",
    },
)
class PolicyGrantReference:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        entity_identifier: builtins.str,
        entity_type: builtins.str,
        grant_id: builtins.str,
        policy_type: builtins.str,
    ) -> None:
        '''A reference to a PolicyGrant resource.

        :param domain_identifier: The DomainIdentifier of the PolicyGrant resource.
        :param entity_identifier: The EntityIdentifier of the PolicyGrant resource.
        :param entity_type: The EntityType of the PolicyGrant resource.
        :param grant_id: The GrantId of the PolicyGrant resource.
        :param policy_type: The PolicyType of the PolicyGrant resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            policy_grant_reference = interfaces_datazone.PolicyGrantReference(
                domain_identifier="domainIdentifier",
                entity_identifier="entityIdentifier",
                entity_type="entityType",
                grant_id="grantId",
                policy_type="policyType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88380419cb3fb4633bf9d15c7fe2fab35634016cea533af37fbda633135ed0e6)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument entity_identifier", value=entity_identifier, expected_type=type_hints["entity_identifier"])
            check_type(argname="argument entity_type", value=entity_type, expected_type=type_hints["entity_type"])
            check_type(argname="argument grant_id", value=grant_id, expected_type=type_hints["grant_id"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "entity_identifier": entity_identifier,
            "entity_type": entity_type,
            "grant_id": grant_id,
            "policy_type": policy_type,
        }

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The DomainIdentifier of the PolicyGrant resource.'''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entity_identifier(self) -> builtins.str:
        '''The EntityIdentifier of the PolicyGrant resource.'''
        result = self._values.get("entity_identifier")
        assert result is not None, "Required property 'entity_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entity_type(self) -> builtins.str:
        '''The EntityType of the PolicyGrant resource.'''
        result = self._values.get("entity_type")
        assert result is not None, "Required property 'entity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def grant_id(self) -> builtins.str:
        '''The GrantId of the PolicyGrant resource.'''
        result = self._values.get("grant_id")
        assert result is not None, "Required property 'grant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_type(self) -> builtins.str:
        '''The PolicyType of the PolicyGrant resource.'''
        result = self._values.get("policy_type")
        assert result is not None, "Required property 'policy_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyGrantReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.ProjectMembershipReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_identifier": "domainIdentifier",
        "member_identifier": "memberIdentifier",
        "member_identifier_type": "memberIdentifierType",
        "project_identifier": "projectIdentifier",
    },
)
class ProjectMembershipReference:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        member_identifier: builtins.str,
        member_identifier_type: builtins.str,
        project_identifier: builtins.str,
    ) -> None:
        '''A reference to a ProjectMembership resource.

        :param domain_identifier: The DomainIdentifier of the ProjectMembership resource.
        :param member_identifier: The MemberIdentifier of the ProjectMembership resource.
        :param member_identifier_type: The MemberIdentifierType of the ProjectMembership resource.
        :param project_identifier: The ProjectIdentifier of the ProjectMembership resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            project_membership_reference = interfaces_datazone.ProjectMembershipReference(
                domain_identifier="domainIdentifier",
                member_identifier="memberIdentifier",
                member_identifier_type="memberIdentifierType",
                project_identifier="projectIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d670a2ef882ac4f5231d337c7aaeef990f6d287cf2fe9c68ff74a3969d9b83e)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument member_identifier", value=member_identifier, expected_type=type_hints["member_identifier"])
            check_type(argname="argument member_identifier_type", value=member_identifier_type, expected_type=type_hints["member_identifier_type"])
            check_type(argname="argument project_identifier", value=project_identifier, expected_type=type_hints["project_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "member_identifier": member_identifier,
            "member_identifier_type": member_identifier_type,
            "project_identifier": project_identifier,
        }

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The DomainIdentifier of the ProjectMembership resource.'''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_identifier(self) -> builtins.str:
        '''The MemberIdentifier of the ProjectMembership resource.'''
        result = self._values.get("member_identifier")
        assert result is not None, "Required property 'member_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def member_identifier_type(self) -> builtins.str:
        '''The MemberIdentifierType of the ProjectMembership resource.'''
        result = self._values.get("member_identifier_type")
        assert result is not None, "Required property 'member_identifier_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_identifier(self) -> builtins.str:
        '''The ProjectIdentifier of the ProjectMembership resource.'''
        result = self._values.get("project_identifier")
        assert result is not None, "Required property 'project_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectMembershipReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.ProjectProfileReference",
    jsii_struct_bases=[],
    name_mapping={"domain_identifier": "domainIdentifier", "identifier": "identifier"},
)
class ProjectProfileReference:
    def __init__(
        self,
        *,
        domain_identifier: builtins.str,
        identifier: builtins.str,
    ) -> None:
        '''A reference to a ProjectProfile resource.

        :param domain_identifier: The DomainIdentifier of the ProjectProfile resource.
        :param identifier: The Identifier of the ProjectProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            project_profile_reference = interfaces_datazone.ProjectProfileReference(
                domain_identifier="domainIdentifier",
                identifier="identifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9c551e99acae1b5ff204ecabd19ad43163c93f2366dd8dc844916b1ca7aecaa)
            check_type(argname="argument domain_identifier", value=domain_identifier, expected_type=type_hints["domain_identifier"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_identifier": domain_identifier,
            "identifier": identifier,
        }

    @builtins.property
    def domain_identifier(self) -> builtins.str:
        '''The DomainIdentifier of the ProjectProfile resource.'''
        result = self._values.get("domain_identifier")
        assert result is not None, "Required property 'domain_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The Identifier of the ProjectProfile resource.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.ProjectReference",
    jsii_struct_bases=[],
    name_mapping={"domain_id": "domainId", "project_id": "projectId"},
)
class ProjectReference:
    def __init__(self, *, domain_id: builtins.str, project_id: builtins.str) -> None:
        '''A reference to a Project resource.

        :param domain_id: The DomainId of the Project resource.
        :param project_id: The Id of the Project resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            project_reference = interfaces_datazone.ProjectReference(
                domain_id="domainId",
                project_id="projectId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__600c307bfee60c781ed4c9a88901844bae53ffbfa30c1ad689d9c413f0ff2c82)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "project_id": project_id,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the Project resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The Id of the Project resource.'''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.SubscriptionTargetReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_id": "domainId",
        "environment_id": "environmentId",
        "subscription_target_id": "subscriptionTargetId",
    },
)
class SubscriptionTargetReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        environment_id: builtins.str,
        subscription_target_id: builtins.str,
    ) -> None:
        '''A reference to a SubscriptionTarget resource.

        :param domain_id: The DomainId of the SubscriptionTarget resource.
        :param environment_id: The EnvironmentId of the SubscriptionTarget resource.
        :param subscription_target_id: The Id of the SubscriptionTarget resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            subscription_target_reference = interfaces_datazone.SubscriptionTargetReference(
                domain_id="domainId",
                environment_id="environmentId",
                subscription_target_id="subscriptionTargetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8984b2f7457b8acf05c191203141022be229ece488865d3498eb161dfa7ed384)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
            check_type(argname="argument subscription_target_id", value=subscription_target_id, expected_type=type_hints["subscription_target_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "environment_id": environment_id,
            "subscription_target_id": subscription_target_id,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the SubscriptionTarget resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''The EnvironmentId of the SubscriptionTarget resource.'''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscription_target_id(self) -> builtins.str:
        '''The Id of the SubscriptionTarget resource.'''
        result = self._values.get("subscription_target_id")
        assert result is not None, "Required property 'subscription_target_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionTargetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_datazone.UserProfileReference",
    jsii_struct_bases=[],
    name_mapping={"domain_id": "domainId", "user_profile_id": "userProfileId"},
)
class UserProfileReference:
    def __init__(
        self,
        *,
        domain_id: builtins.str,
        user_profile_id: builtins.str,
    ) -> None:
        '''A reference to a UserProfile resource.

        :param domain_id: The DomainId of the UserProfile resource.
        :param user_profile_id: The Id of the UserProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_datazone as interfaces_datazone
            
            user_profile_reference = interfaces_datazone.UserProfileReference(
                domain_id="domainId",
                user_profile_id="userProfileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c091d792ce24ad06f2d236c51e842cd29ca48787d85819469c7e7764e53a8fd)
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument user_profile_id", value=user_profile_id, expected_type=type_hints["user_profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_id": domain_id,
            "user_profile_id": user_profile_id,
        }

    @builtins.property
    def domain_id(self) -> builtins.str:
        '''The DomainId of the UserProfile resource.'''
        result = self._values.get("domain_id")
        assert result is not None, "Required property 'domain_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_profile_id(self) -> builtins.str:
        '''The Id of the UserProfile resource.'''
        result = self._values.get("user_profile_id")
        assert result is not None, "Required property 'user_profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConnectionReference",
    "DataSourceReference",
    "DomainReference",
    "DomainUnitReference",
    "EnvironmentActionsReference",
    "EnvironmentBlueprintConfigurationReference",
    "EnvironmentProfileReference",
    "EnvironmentReference",
    "FormTypeReference",
    "GroupProfileReference",
    "IConnectionRef",
    "IDataSourceRef",
    "IDomainRef",
    "IDomainUnitRef",
    "IEnvironmentActionsRef",
    "IEnvironmentBlueprintConfigurationRef",
    "IEnvironmentProfileRef",
    "IEnvironmentRef",
    "IFormTypeRef",
    "IGroupProfileRef",
    "IOwnerRef",
    "IPolicyGrantRef",
    "IProjectMembershipRef",
    "IProjectProfileRef",
    "IProjectRef",
    "ISubscriptionTargetRef",
    "IUserProfileRef",
    "OwnerReference",
    "PolicyGrantReference",
    "ProjectMembershipReference",
    "ProjectProfileReference",
    "ProjectReference",
    "SubscriptionTargetReference",
    "UserProfileReference",
]

publication.publish()

def _typecheckingstub__2f7850fde9fef51a80e2d06ac28cd4fe81de985a525e994d643ac6d109536637(
    *,
    connection_id: builtins.str,
    domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6871dc8841d605ea74965422b16e2a095c2fa3cefc233d56325c05b81d859c3a(
    *,
    data_source_id: builtins.str,
    domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb767451ab5e19a7b28b12c6fceb9e1a1d5fd6b93294c9455242952d67797a9e(
    *,
    domain_arn: builtins.str,
    domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c196b765e57c342c351f2229a31f253bc5dfd9e3885706168310286ca0c2c2(
    *,
    domain_id: builtins.str,
    domain_unit_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d0a753cfdc48e1908e540974b3fb1b37607132b5a1c7ba25ad51caaa8689c75(
    *,
    domain_id: builtins.str,
    environment_actions_id: builtins.str,
    environment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3dfe34b538dd9e6fb1f8301a81eeb9b47a3c4d9878ab58c0ea301dbfa5d6053(
    *,
    domain_id: builtins.str,
    environment_blueprint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e5797ce9ff71fb7ca1f857bfc1ebc8de57d2694bac8c3e1880544b1d5d106ec(
    *,
    domain_id: builtins.str,
    environment_profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0598aa1fd0986ce9b7c3b0e4fd6a9a5f144a1fd6d959bf12f7dd2e000ba97a25(
    *,
    domain_id: builtins.str,
    environment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab76ee3af4baa56b49082234e89d0e064c6abd968ab7a49bbc66020a57c938dc(
    *,
    domain_identifier: builtins.str,
    form_type_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a1b5d0de041d5e3b32120d7f53ca62f70d31a4e431952ebbc8e9d9c3896096(
    *,
    domain_id: builtins.str,
    group_profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24300f06c1e5be24db2bc08d9fc81f2d86bc7593405c538c43faa80a3af368d2(
    *,
    domain_identifier: builtins.str,
    entity_identifier: builtins.str,
    entity_type: builtins.str,
    owner_identifier: builtins.str,
    owner_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88380419cb3fb4633bf9d15c7fe2fab35634016cea533af37fbda633135ed0e6(
    *,
    domain_identifier: builtins.str,
    entity_identifier: builtins.str,
    entity_type: builtins.str,
    grant_id: builtins.str,
    policy_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d670a2ef882ac4f5231d337c7aaeef990f6d287cf2fe9c68ff74a3969d9b83e(
    *,
    domain_identifier: builtins.str,
    member_identifier: builtins.str,
    member_identifier_type: builtins.str,
    project_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9c551e99acae1b5ff204ecabd19ad43163c93f2366dd8dc844916b1ca7aecaa(
    *,
    domain_identifier: builtins.str,
    identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__600c307bfee60c781ed4c9a88901844bae53ffbfa30c1ad689d9c413f0ff2c82(
    *,
    domain_id: builtins.str,
    project_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8984b2f7457b8acf05c191203141022be229ece488865d3498eb161dfa7ed384(
    *,
    domain_id: builtins.str,
    environment_id: builtins.str,
    subscription_target_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c091d792ce24ad06f2d236c51e842cd29ca48787d85819469c7e7764e53a8fd(
    *,
    domain_id: builtins.str,
    user_profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectionRef, IDataSourceRef, IDomainRef, IDomainUnitRef, IEnvironmentActionsRef, IEnvironmentBlueprintConfigurationRef, IEnvironmentProfileRef, IEnvironmentRef, IFormTypeRef, IGroupProfileRef, IOwnerRef, IPolicyGrantRef, IProjectMembershipRef, IProjectProfileRef, IProjectRef, ISubscriptionTargetRef, IUserProfileRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
