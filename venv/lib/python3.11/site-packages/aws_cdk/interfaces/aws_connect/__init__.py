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
    jsii_type="aws-cdk-lib.interfaces.aws_connect.AgentStatusReference",
    jsii_struct_bases=[],
    name_mapping={"agent_status_arn": "agentStatusArn"},
)
class AgentStatusReference:
    def __init__(self, *, agent_status_arn: builtins.str) -> None:
        '''A reference to a AgentStatus resource.

        :param agent_status_arn: The AgentStatusArn of the AgentStatus resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            agent_status_reference = interfaces_connect.AgentStatusReference(
                agent_status_arn="agentStatusArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80c2ee1f86d017d30c810fdfe35ebe75edb827c0c9b72fce1dfaea275aebbeaa)
            check_type(argname="argument agent_status_arn", value=agent_status_arn, expected_type=type_hints["agent_status_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_status_arn": agent_status_arn,
        }

    @builtins.property
    def agent_status_arn(self) -> builtins.str:
        '''The AgentStatusArn of the AgentStatus resource.'''
        result = self._values.get("agent_status_arn")
        assert result is not None, "Required property 'agent_status_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentStatusReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.ApprovedOriginReference",
    jsii_struct_bases=[],
    name_mapping={"instance_id": "instanceId", "origin": "origin"},
)
class ApprovedOriginReference:
    def __init__(self, *, instance_id: builtins.str, origin: builtins.str) -> None:
        '''A reference to a ApprovedOrigin resource.

        :param instance_id: The InstanceId of the ApprovedOrigin resource.
        :param origin: The Origin of the ApprovedOrigin resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            approved_origin_reference = interfaces_connect.ApprovedOriginReference(
                instance_id="instanceId",
                origin="origin"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__420107c3fcd91bed4de5358f4760ba480949bdc8881c5d0538f7ef3c2b2b5dca)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "origin": origin,
        }

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The InstanceId of the ApprovedOrigin resource.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin(self) -> builtins.str:
        '''The Origin of the ApprovedOrigin resource.'''
        result = self._values.get("origin")
        assert result is not None, "Required property 'origin' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprovedOriginReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.ContactFlowModuleAliasReference",
    jsii_struct_bases=[],
    name_mapping={"contact_flow_module_alias_arn": "contactFlowModuleAliasArn"},
)
class ContactFlowModuleAliasReference:
    def __init__(self, *, contact_flow_module_alias_arn: builtins.str) -> None:
        '''A reference to a ContactFlowModuleAlias resource.

        :param contact_flow_module_alias_arn: The ContactFlowModuleAliasARN of the ContactFlowModuleAlias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            contact_flow_module_alias_reference = interfaces_connect.ContactFlowModuleAliasReference(
                contact_flow_module_alias_arn="contactFlowModuleAliasArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20d4bbaa3402801ecaedf7fd115c6b26c722e3c434fea3b3c5595d76f6875dbf)
            check_type(argname="argument contact_flow_module_alias_arn", value=contact_flow_module_alias_arn, expected_type=type_hints["contact_flow_module_alias_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_flow_module_alias_arn": contact_flow_module_alias_arn,
        }

    @builtins.property
    def contact_flow_module_alias_arn(self) -> builtins.str:
        '''The ContactFlowModuleAliasARN of the ContactFlowModuleAlias resource.'''
        result = self._values.get("contact_flow_module_alias_arn")
        assert result is not None, "Required property 'contact_flow_module_alias_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactFlowModuleAliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.ContactFlowModuleReference",
    jsii_struct_bases=[],
    name_mapping={"contact_flow_module_arn": "contactFlowModuleArn"},
)
class ContactFlowModuleReference:
    def __init__(self, *, contact_flow_module_arn: builtins.str) -> None:
        '''A reference to a ContactFlowModule resource.

        :param contact_flow_module_arn: The ContactFlowModuleArn of the ContactFlowModule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            contact_flow_module_reference = interfaces_connect.ContactFlowModuleReference(
                contact_flow_module_arn="contactFlowModuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ec59a97e450b6e15ebf5f88fe0e6ba5fd33f4df09f3ba1201e6804bf44c54c7)
            check_type(argname="argument contact_flow_module_arn", value=contact_flow_module_arn, expected_type=type_hints["contact_flow_module_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_flow_module_arn": contact_flow_module_arn,
        }

    @builtins.property
    def contact_flow_module_arn(self) -> builtins.str:
        '''The ContactFlowModuleArn of the ContactFlowModule resource.'''
        result = self._values.get("contact_flow_module_arn")
        assert result is not None, "Required property 'contact_flow_module_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactFlowModuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.ContactFlowModuleVersionReference",
    jsii_struct_bases=[],
    name_mapping={"contact_flow_module_version_arn": "contactFlowModuleVersionArn"},
)
class ContactFlowModuleVersionReference:
    def __init__(self, *, contact_flow_module_version_arn: builtins.str) -> None:
        '''A reference to a ContactFlowModuleVersion resource.

        :param contact_flow_module_version_arn: The ContactFlowModuleVersionARN of the ContactFlowModuleVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            contact_flow_module_version_reference = interfaces_connect.ContactFlowModuleVersionReference(
                contact_flow_module_version_arn="contactFlowModuleVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__765dc1aed839fcfb38c331a611567553c325090dc403c41e00e34926961cf6fc)
            check_type(argname="argument contact_flow_module_version_arn", value=contact_flow_module_version_arn, expected_type=type_hints["contact_flow_module_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_flow_module_version_arn": contact_flow_module_version_arn,
        }

    @builtins.property
    def contact_flow_module_version_arn(self) -> builtins.str:
        '''The ContactFlowModuleVersionARN of the ContactFlowModuleVersion resource.'''
        result = self._values.get("contact_flow_module_version_arn")
        assert result is not None, "Required property 'contact_flow_module_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactFlowModuleVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.ContactFlowReference",
    jsii_struct_bases=[],
    name_mapping={"contact_flow_arn": "contactFlowArn"},
)
class ContactFlowReference:
    def __init__(self, *, contact_flow_arn: builtins.str) -> None:
        '''A reference to a ContactFlow resource.

        :param contact_flow_arn: The ContactFlowArn of the ContactFlow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            contact_flow_reference = interfaces_connect.ContactFlowReference(
                contact_flow_arn="contactFlowArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dfa181ff2c0859219dbf48106492ecead1b4da0281898a69b709514db4d8f00)
            check_type(argname="argument contact_flow_arn", value=contact_flow_arn, expected_type=type_hints["contact_flow_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_flow_arn": contact_flow_arn,
        }

    @builtins.property
    def contact_flow_arn(self) -> builtins.str:
        '''The ContactFlowArn of the ContactFlow resource.'''
        result = self._values.get("contact_flow_arn")
        assert result is not None, "Required property 'contact_flow_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactFlowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.ContactFlowVersionReference",
    jsii_struct_bases=[],
    name_mapping={"contact_flow_version_arn": "contactFlowVersionArn"},
)
class ContactFlowVersionReference:
    def __init__(self, *, contact_flow_version_arn: builtins.str) -> None:
        '''A reference to a ContactFlowVersion resource.

        :param contact_flow_version_arn: The ContactFlowVersionARN of the ContactFlowVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            contact_flow_version_reference = interfaces_connect.ContactFlowVersionReference(
                contact_flow_version_arn="contactFlowVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f8ed10dcdc4a77bc2068dd63220cfc0b8add9c5c8c1020fec0826fbf1cecaa1)
            check_type(argname="argument contact_flow_version_arn", value=contact_flow_version_arn, expected_type=type_hints["contact_flow_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_flow_version_arn": contact_flow_version_arn,
        }

    @builtins.property
    def contact_flow_version_arn(self) -> builtins.str:
        '''The ContactFlowVersionARN of the ContactFlowVersion resource.'''
        result = self._values.get("contact_flow_version_arn")
        assert result is not None, "Required property 'contact_flow_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactFlowVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.DataTableAttributeReference",
    jsii_struct_bases=[],
    name_mapping={
        "attribute_id": "attributeId",
        "data_table_arn": "dataTableArn",
        "instance_arn": "instanceArn",
    },
)
class DataTableAttributeReference:
    def __init__(
        self,
        *,
        attribute_id: builtins.str,
        data_table_arn: builtins.str,
        instance_arn: builtins.str,
    ) -> None:
        '''A reference to a DataTableAttribute resource.

        :param attribute_id: The AttributeId of the DataTableAttribute resource.
        :param data_table_arn: The DataTableArn of the DataTableAttribute resource.
        :param instance_arn: The InstanceArn of the DataTableAttribute resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            data_table_attribute_reference = interfaces_connect.DataTableAttributeReference(
                attribute_id="attributeId",
                data_table_arn="dataTableArn",
                instance_arn="instanceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e5c1d586322eb5f50ced0dfce17a7353fcfd770475aabc413e355fcebf55c8)
            check_type(argname="argument attribute_id", value=attribute_id, expected_type=type_hints["attribute_id"])
            check_type(argname="argument data_table_arn", value=data_table_arn, expected_type=type_hints["data_table_arn"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attribute_id": attribute_id,
            "data_table_arn": data_table_arn,
            "instance_arn": instance_arn,
        }

    @builtins.property
    def attribute_id(self) -> builtins.str:
        '''The AttributeId of the DataTableAttribute resource.'''
        result = self._values.get("attribute_id")
        assert result is not None, "Required property 'attribute_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_table_arn(self) -> builtins.str:
        '''The DataTableArn of the DataTableAttribute resource.'''
        result = self._values.get("data_table_arn")
        assert result is not None, "Required property 'data_table_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The InstanceArn of the DataTableAttribute resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTableAttributeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.DataTableRecordReference",
    jsii_struct_bases=[],
    name_mapping={
        "data_table_arn": "dataTableArn",
        "instance_arn": "instanceArn",
        "record_id": "recordId",
    },
)
class DataTableRecordReference:
    def __init__(
        self,
        *,
        data_table_arn: builtins.str,
        instance_arn: builtins.str,
        record_id: builtins.str,
    ) -> None:
        '''A reference to a DataTableRecord resource.

        :param data_table_arn: The DataTableArn of the DataTableRecord resource.
        :param instance_arn: The InstanceArn of the DataTableRecord resource.
        :param record_id: The RecordId of the DataTableRecord resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            data_table_record_reference = interfaces_connect.DataTableRecordReference(
                data_table_arn="dataTableArn",
                instance_arn="instanceArn",
                record_id="recordId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a889d8714c4a728775a98ceba8c53a6fe42518e93b4afe450277d0437e88e7b)
            check_type(argname="argument data_table_arn", value=data_table_arn, expected_type=type_hints["data_table_arn"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument record_id", value=record_id, expected_type=type_hints["record_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_table_arn": data_table_arn,
            "instance_arn": instance_arn,
            "record_id": record_id,
        }

    @builtins.property
    def data_table_arn(self) -> builtins.str:
        '''The DataTableArn of the DataTableRecord resource.'''
        result = self._values.get("data_table_arn")
        assert result is not None, "Required property 'data_table_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The InstanceArn of the DataTableRecord resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def record_id(self) -> builtins.str:
        '''The RecordId of the DataTableRecord resource.'''
        result = self._values.get("record_id")
        assert result is not None, "Required property 'record_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTableRecordReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.DataTableReference",
    jsii_struct_bases=[],
    name_mapping={"data_table_arn": "dataTableArn", "instance_arn": "instanceArn"},
)
class DataTableReference:
    def __init__(
        self,
        *,
        data_table_arn: builtins.str,
        instance_arn: builtins.str,
    ) -> None:
        '''A reference to a DataTable resource.

        :param data_table_arn: The Arn of the DataTable resource.
        :param instance_arn: The InstanceArn of the DataTable resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            data_table_reference = interfaces_connect.DataTableReference(
                data_table_arn="dataTableArn",
                instance_arn="instanceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67ba9770097234b94f825ce5d9299c6c020d31311df11a5f307f8a110b95ce7e)
            check_type(argname="argument data_table_arn", value=data_table_arn, expected_type=type_hints["data_table_arn"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_table_arn": data_table_arn,
            "instance_arn": instance_arn,
        }

    @builtins.property
    def data_table_arn(self) -> builtins.str:
        '''The Arn of the DataTable resource.'''
        result = self._values.get("data_table_arn")
        assert result is not None, "Required property 'data_table_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The InstanceArn of the DataTable resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.EmailAddressReference",
    jsii_struct_bases=[],
    name_mapping={"email_address_arn": "emailAddressArn"},
)
class EmailAddressReference:
    def __init__(self, *, email_address_arn: builtins.str) -> None:
        '''A reference to a EmailAddress resource.

        :param email_address_arn: The EmailAddressArn of the EmailAddress resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            email_address_reference = interfaces_connect.EmailAddressReference(
                email_address_arn="emailAddressArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6089d57da936a584df9a8b70f9f44fb73b442ddc2498e220add2c31f7faba584)
            check_type(argname="argument email_address_arn", value=email_address_arn, expected_type=type_hints["email_address_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email_address_arn": email_address_arn,
        }

    @builtins.property
    def email_address_arn(self) -> builtins.str:
        '''The EmailAddressArn of the EmailAddress resource.'''
        result = self._values.get("email_address_arn")
        assert result is not None, "Required property 'email_address_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailAddressReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.EvaluationFormReference",
    jsii_struct_bases=[],
    name_mapping={"evaluation_form_arn": "evaluationFormArn"},
)
class EvaluationFormReference:
    def __init__(self, *, evaluation_form_arn: builtins.str) -> None:
        '''A reference to a EvaluationForm resource.

        :param evaluation_form_arn: The EvaluationFormArn of the EvaluationForm resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            evaluation_form_reference = interfaces_connect.EvaluationFormReference(
                evaluation_form_arn="evaluationFormArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5264e070ad3ac631aba777dd6c2a9c99c524dafea18344334f59097bfbddbb1)
            check_type(argname="argument evaluation_form_arn", value=evaluation_form_arn, expected_type=type_hints["evaluation_form_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "evaluation_form_arn": evaluation_form_arn,
        }

    @builtins.property
    def evaluation_form_arn(self) -> builtins.str:
        '''The EvaluationFormArn of the EvaluationForm resource.'''
        result = self._values.get("evaluation_form_arn")
        assert result is not None, "Required property 'evaluation_form_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EvaluationFormReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.HoursOfOperationReference",
    jsii_struct_bases=[],
    name_mapping={"hours_of_operation_arn": "hoursOfOperationArn"},
)
class HoursOfOperationReference:
    def __init__(self, *, hours_of_operation_arn: builtins.str) -> None:
        '''A reference to a HoursOfOperation resource.

        :param hours_of_operation_arn: The HoursOfOperationArn of the HoursOfOperation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            hours_of_operation_reference = interfaces_connect.HoursOfOperationReference(
                hours_of_operation_arn="hoursOfOperationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__963a1a8b18b2bbfd6eb3ab2343ba1df7da95bee1b6c17ccec51bc122ecdcd770)
            check_type(argname="argument hours_of_operation_arn", value=hours_of_operation_arn, expected_type=type_hints["hours_of_operation_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hours_of_operation_arn": hours_of_operation_arn,
        }

    @builtins.property
    def hours_of_operation_arn(self) -> builtins.str:
        '''The HoursOfOperationArn of the HoursOfOperation resource.'''
        result = self._values.get("hours_of_operation_arn")
        assert result is not None, "Required property 'hours_of_operation_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HoursOfOperationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IAgentStatusRef")
class IAgentStatusRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AgentStatus.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentStatusRef")
    def agent_status_ref(self) -> "AgentStatusReference":
        '''(experimental) A reference to a AgentStatus resource.

        :stability: experimental
        '''
        ...


class _IAgentStatusRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AgentStatus.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IAgentStatusRef"

    @builtins.property
    @jsii.member(jsii_name="agentStatusRef")
    def agent_status_ref(self) -> "AgentStatusReference":
        '''(experimental) A reference to a AgentStatus resource.

        :stability: experimental
        '''
        return typing.cast("AgentStatusReference", jsii.get(self, "agentStatusRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentStatusRef).__jsii_proxy_class__ = lambda : _IAgentStatusRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IApprovedOriginRef")
class IApprovedOriginRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApprovedOrigin.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="approvedOriginRef")
    def approved_origin_ref(self) -> "ApprovedOriginReference":
        '''(experimental) A reference to a ApprovedOrigin resource.

        :stability: experimental
        '''
        ...


class _IApprovedOriginRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApprovedOrigin.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IApprovedOriginRef"

    @builtins.property
    @jsii.member(jsii_name="approvedOriginRef")
    def approved_origin_ref(self) -> "ApprovedOriginReference":
        '''(experimental) A reference to a ApprovedOrigin resource.

        :stability: experimental
        '''
        return typing.cast("ApprovedOriginReference", jsii.get(self, "approvedOriginRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApprovedOriginRef).__jsii_proxy_class__ = lambda : _IApprovedOriginRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.IContactFlowModuleAliasRef"
)
class IContactFlowModuleAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlowModuleAlias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="contactFlowModuleAliasRef")
    def contact_flow_module_alias_ref(self) -> "ContactFlowModuleAliasReference":
        '''(experimental) A reference to a ContactFlowModuleAlias resource.

        :stability: experimental
        '''
        ...


class _IContactFlowModuleAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlowModuleAlias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IContactFlowModuleAliasRef"

    @builtins.property
    @jsii.member(jsii_name="contactFlowModuleAliasRef")
    def contact_flow_module_alias_ref(self) -> "ContactFlowModuleAliasReference":
        '''(experimental) A reference to a ContactFlowModuleAlias resource.

        :stability: experimental
        '''
        return typing.cast("ContactFlowModuleAliasReference", jsii.get(self, "contactFlowModuleAliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContactFlowModuleAliasRef).__jsii_proxy_class__ = lambda : _IContactFlowModuleAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IContactFlowModuleRef")
class IContactFlowModuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlowModule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="contactFlowModuleRef")
    def contact_flow_module_ref(self) -> "ContactFlowModuleReference":
        '''(experimental) A reference to a ContactFlowModule resource.

        :stability: experimental
        '''
        ...


class _IContactFlowModuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlowModule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IContactFlowModuleRef"

    @builtins.property
    @jsii.member(jsii_name="contactFlowModuleRef")
    def contact_flow_module_ref(self) -> "ContactFlowModuleReference":
        '''(experimental) A reference to a ContactFlowModule resource.

        :stability: experimental
        '''
        return typing.cast("ContactFlowModuleReference", jsii.get(self, "contactFlowModuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContactFlowModuleRef).__jsii_proxy_class__ = lambda : _IContactFlowModuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.IContactFlowModuleVersionRef"
)
class IContactFlowModuleVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlowModuleVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="contactFlowModuleVersionRef")
    def contact_flow_module_version_ref(self) -> "ContactFlowModuleVersionReference":
        '''(experimental) A reference to a ContactFlowModuleVersion resource.

        :stability: experimental
        '''
        ...


class _IContactFlowModuleVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlowModuleVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IContactFlowModuleVersionRef"

    @builtins.property
    @jsii.member(jsii_name="contactFlowModuleVersionRef")
    def contact_flow_module_version_ref(self) -> "ContactFlowModuleVersionReference":
        '''(experimental) A reference to a ContactFlowModuleVersion resource.

        :stability: experimental
        '''
        return typing.cast("ContactFlowModuleVersionReference", jsii.get(self, "contactFlowModuleVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContactFlowModuleVersionRef).__jsii_proxy_class__ = lambda : _IContactFlowModuleVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IContactFlowRef")
class IContactFlowRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="contactFlowRef")
    def contact_flow_ref(self) -> "ContactFlowReference":
        '''(experimental) A reference to a ContactFlow resource.

        :stability: experimental
        '''
        ...


class _IContactFlowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IContactFlowRef"

    @builtins.property
    @jsii.member(jsii_name="contactFlowRef")
    def contact_flow_ref(self) -> "ContactFlowReference":
        '''(experimental) A reference to a ContactFlow resource.

        :stability: experimental
        '''
        return typing.cast("ContactFlowReference", jsii.get(self, "contactFlowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContactFlowRef).__jsii_proxy_class__ = lambda : _IContactFlowRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IContactFlowVersionRef")
class IContactFlowVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlowVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="contactFlowVersionRef")
    def contact_flow_version_ref(self) -> "ContactFlowVersionReference":
        '''(experimental) A reference to a ContactFlowVersion resource.

        :stability: experimental
        '''
        ...


class _IContactFlowVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContactFlowVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IContactFlowVersionRef"

    @builtins.property
    @jsii.member(jsii_name="contactFlowVersionRef")
    def contact_flow_version_ref(self) -> "ContactFlowVersionReference":
        '''(experimental) A reference to a ContactFlowVersion resource.

        :stability: experimental
        '''
        return typing.cast("ContactFlowVersionReference", jsii.get(self, "contactFlowVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContactFlowVersionRef).__jsii_proxy_class__ = lambda : _IContactFlowVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IDataTableAttributeRef")
class IDataTableAttributeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataTableAttribute.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataTableAttributeRef")
    def data_table_attribute_ref(self) -> "DataTableAttributeReference":
        '''(experimental) A reference to a DataTableAttribute resource.

        :stability: experimental
        '''
        ...


class _IDataTableAttributeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataTableAttribute.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IDataTableAttributeRef"

    @builtins.property
    @jsii.member(jsii_name="dataTableAttributeRef")
    def data_table_attribute_ref(self) -> "DataTableAttributeReference":
        '''(experimental) A reference to a DataTableAttribute resource.

        :stability: experimental
        '''
        return typing.cast("DataTableAttributeReference", jsii.get(self, "dataTableAttributeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataTableAttributeRef).__jsii_proxy_class__ = lambda : _IDataTableAttributeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IDataTableRecordRef")
class IDataTableRecordRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataTableRecord.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataTableRecordRef")
    def data_table_record_ref(self) -> "DataTableRecordReference":
        '''(experimental) A reference to a DataTableRecord resource.

        :stability: experimental
        '''
        ...


class _IDataTableRecordRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataTableRecord.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IDataTableRecordRef"

    @builtins.property
    @jsii.member(jsii_name="dataTableRecordRef")
    def data_table_record_ref(self) -> "DataTableRecordReference":
        '''(experimental) A reference to a DataTableRecord resource.

        :stability: experimental
        '''
        return typing.cast("DataTableRecordReference", jsii.get(self, "dataTableRecordRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataTableRecordRef).__jsii_proxy_class__ = lambda : _IDataTableRecordRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IDataTableRef")
class IDataTableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataTable.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataTableRef")
    def data_table_ref(self) -> "DataTableReference":
        '''(experimental) A reference to a DataTable resource.

        :stability: experimental
        '''
        ...


class _IDataTableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataTable.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IDataTableRef"

    @builtins.property
    @jsii.member(jsii_name="dataTableRef")
    def data_table_ref(self) -> "DataTableReference":
        '''(experimental) A reference to a DataTable resource.

        :stability: experimental
        '''
        return typing.cast("DataTableReference", jsii.get(self, "dataTableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataTableRef).__jsii_proxy_class__ = lambda : _IDataTableRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IEmailAddressRef")
class IEmailAddressRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EmailAddress.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="emailAddressRef")
    def email_address_ref(self) -> "EmailAddressReference":
        '''(experimental) A reference to a EmailAddress resource.

        :stability: experimental
        '''
        ...


class _IEmailAddressRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EmailAddress.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IEmailAddressRef"

    @builtins.property
    @jsii.member(jsii_name="emailAddressRef")
    def email_address_ref(self) -> "EmailAddressReference":
        '''(experimental) A reference to a EmailAddress resource.

        :stability: experimental
        '''
        return typing.cast("EmailAddressReference", jsii.get(self, "emailAddressRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEmailAddressRef).__jsii_proxy_class__ = lambda : _IEmailAddressRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IEvaluationFormRef")
class IEvaluationFormRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EvaluationForm.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="evaluationFormRef")
    def evaluation_form_ref(self) -> "EvaluationFormReference":
        '''(experimental) A reference to a EvaluationForm resource.

        :stability: experimental
        '''
        ...


class _IEvaluationFormRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EvaluationForm.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IEvaluationFormRef"

    @builtins.property
    @jsii.member(jsii_name="evaluationFormRef")
    def evaluation_form_ref(self) -> "EvaluationFormReference":
        '''(experimental) A reference to a EvaluationForm resource.

        :stability: experimental
        '''
        return typing.cast("EvaluationFormReference", jsii.get(self, "evaluationFormRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEvaluationFormRef).__jsii_proxy_class__ = lambda : _IEvaluationFormRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IHoursOfOperationRef")
class IHoursOfOperationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HoursOfOperation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hoursOfOperationRef")
    def hours_of_operation_ref(self) -> "HoursOfOperationReference":
        '''(experimental) A reference to a HoursOfOperation resource.

        :stability: experimental
        '''
        ...


class _IHoursOfOperationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HoursOfOperation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IHoursOfOperationRef"

    @builtins.property
    @jsii.member(jsii_name="hoursOfOperationRef")
    def hours_of_operation_ref(self) -> "HoursOfOperationReference":
        '''(experimental) A reference to a HoursOfOperation resource.

        :stability: experimental
        '''
        return typing.cast("HoursOfOperationReference", jsii.get(self, "hoursOfOperationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHoursOfOperationRef).__jsii_proxy_class__ = lambda : _IHoursOfOperationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IInstanceRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        return typing.cast("InstanceReference", jsii.get(self, "instanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceRef).__jsii_proxy_class__ = lambda : _IInstanceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.IInstanceStorageConfigRef"
)
class IInstanceStorageConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceStorageConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceStorageConfigRef")
    def instance_storage_config_ref(self) -> "InstanceStorageConfigReference":
        '''(experimental) A reference to a InstanceStorageConfig resource.

        :stability: experimental
        '''
        ...


class _IInstanceStorageConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceStorageConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IInstanceStorageConfigRef"

    @builtins.property
    @jsii.member(jsii_name="instanceStorageConfigRef")
    def instance_storage_config_ref(self) -> "InstanceStorageConfigReference":
        '''(experimental) A reference to a InstanceStorageConfig resource.

        :stability: experimental
        '''
        return typing.cast("InstanceStorageConfigReference", jsii.get(self, "instanceStorageConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceStorageConfigRef).__jsii_proxy_class__ = lambda : _IInstanceStorageConfigRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.IIntegrationAssociationRef"
)
class IIntegrationAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IntegrationAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="integrationAssociationRef")
    def integration_association_ref(self) -> "IntegrationAssociationReference":
        '''(experimental) A reference to a IntegrationAssociation resource.

        :stability: experimental
        '''
        ...


class _IIntegrationAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IntegrationAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IIntegrationAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="integrationAssociationRef")
    def integration_association_ref(self) -> "IntegrationAssociationReference":
        '''(experimental) A reference to a IntegrationAssociation resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationAssociationReference", jsii.get(self, "integrationAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationAssociationRef).__jsii_proxy_class__ = lambda : _IIntegrationAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.INotificationRef")
class INotificationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Notification.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="notificationRef")
    def notification_ref(self) -> "NotificationReference":
        '''(experimental) A reference to a Notification resource.

        :stability: experimental
        '''
        ...


class _INotificationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Notification.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.INotificationRef"

    @builtins.property
    @jsii.member(jsii_name="notificationRef")
    def notification_ref(self) -> "NotificationReference":
        '''(experimental) A reference to a Notification resource.

        :stability: experimental
        '''
        return typing.cast("NotificationReference", jsii.get(self, "notificationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotificationRef).__jsii_proxy_class__ = lambda : _INotificationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IPhoneNumberRef")
class IPhoneNumberRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PhoneNumber.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="phoneNumberRef")
    def phone_number_ref(self) -> "PhoneNumberReference":
        '''(experimental) A reference to a PhoneNumber resource.

        :stability: experimental
        '''
        ...


class _IPhoneNumberRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PhoneNumber.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IPhoneNumberRef"

    @builtins.property
    @jsii.member(jsii_name="phoneNumberRef")
    def phone_number_ref(self) -> "PhoneNumberReference":
        '''(experimental) A reference to a PhoneNumber resource.

        :stability: experimental
        '''
        return typing.cast("PhoneNumberReference", jsii.get(self, "phoneNumberRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPhoneNumberRef).__jsii_proxy_class__ = lambda : _IPhoneNumberRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IPredefinedAttributeRef")
class IPredefinedAttributeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PredefinedAttribute.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="predefinedAttributeRef")
    def predefined_attribute_ref(self) -> "PredefinedAttributeReference":
        '''(experimental) A reference to a PredefinedAttribute resource.

        :stability: experimental
        '''
        ...


class _IPredefinedAttributeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PredefinedAttribute.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IPredefinedAttributeRef"

    @builtins.property
    @jsii.member(jsii_name="predefinedAttributeRef")
    def predefined_attribute_ref(self) -> "PredefinedAttributeReference":
        '''(experimental) A reference to a PredefinedAttribute resource.

        :stability: experimental
        '''
        return typing.cast("PredefinedAttributeReference", jsii.get(self, "predefinedAttributeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPredefinedAttributeRef).__jsii_proxy_class__ = lambda : _IPredefinedAttributeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IPromptRef")
class IPromptRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Prompt.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="promptRef")
    def prompt_ref(self) -> "PromptReference":
        '''(experimental) A reference to a Prompt resource.

        :stability: experimental
        '''
        ...


class _IPromptRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Prompt.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IPromptRef"

    @builtins.property
    @jsii.member(jsii_name="promptRef")
    def prompt_ref(self) -> "PromptReference":
        '''(experimental) A reference to a Prompt resource.

        :stability: experimental
        '''
        return typing.cast("PromptReference", jsii.get(self, "promptRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPromptRef).__jsii_proxy_class__ = lambda : _IPromptRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IQueueRef")
class IQueueRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        ...


class _IQueueRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IQueueRef"

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        return typing.cast("QueueReference", jsii.get(self, "queueRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueueRef).__jsii_proxy_class__ = lambda : _IQueueRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IQuickConnectRef")
class IQuickConnectRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QuickConnect.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="quickConnectRef")
    def quick_connect_ref(self) -> "QuickConnectReference":
        '''(experimental) A reference to a QuickConnect resource.

        :stability: experimental
        '''
        ...


class _IQuickConnectRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QuickConnect.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IQuickConnectRef"

    @builtins.property
    @jsii.member(jsii_name="quickConnectRef")
    def quick_connect_ref(self) -> "QuickConnectReference":
        '''(experimental) A reference to a QuickConnect resource.

        :stability: experimental
        '''
        return typing.cast("QuickConnectReference", jsii.get(self, "quickConnectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQuickConnectRef).__jsii_proxy_class__ = lambda : _IQuickConnectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IRoutingProfileRef")
class IRoutingProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RoutingProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routingProfileRef")
    def routing_profile_ref(self) -> "RoutingProfileReference":
        '''(experimental) A reference to a RoutingProfile resource.

        :stability: experimental
        '''
        ...


class _IRoutingProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RoutingProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IRoutingProfileRef"

    @builtins.property
    @jsii.member(jsii_name="routingProfileRef")
    def routing_profile_ref(self) -> "RoutingProfileReference":
        '''(experimental) A reference to a RoutingProfile resource.

        :stability: experimental
        '''
        return typing.cast("RoutingProfileReference", jsii.get(self, "routingProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRoutingProfileRef).__jsii_proxy_class__ = lambda : _IRoutingProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IRuleRef")
class IRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Rule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ruleRef")
    def rule_ref(self) -> "RuleReference":
        '''(experimental) A reference to a Rule resource.

        :stability: experimental
        '''
        ...


class _IRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Rule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IRuleRef"

    @builtins.property
    @jsii.member(jsii_name="ruleRef")
    def rule_ref(self) -> "RuleReference":
        '''(experimental) A reference to a Rule resource.

        :stability: experimental
        '''
        return typing.cast("RuleReference", jsii.get(self, "ruleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuleRef).__jsii_proxy_class__ = lambda : _IRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.ISecurityKeyRef")
class ISecurityKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityKeyRef")
    def security_key_ref(self) -> "SecurityKeyReference":
        '''(experimental) A reference to a SecurityKey resource.

        :stability: experimental
        '''
        ...


class _ISecurityKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.ISecurityKeyRef"

    @builtins.property
    @jsii.member(jsii_name="securityKeyRef")
    def security_key_ref(self) -> "SecurityKeyReference":
        '''(experimental) A reference to a SecurityKey resource.

        :stability: experimental
        '''
        return typing.cast("SecurityKeyReference", jsii.get(self, "securityKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityKeyRef).__jsii_proxy_class__ = lambda : _ISecurityKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.ISecurityProfileRef")
class ISecurityProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityProfileRef")
    def security_profile_ref(self) -> "SecurityProfileReference":
        '''(experimental) A reference to a SecurityProfile resource.

        :stability: experimental
        '''
        ...


class _ISecurityProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.ISecurityProfileRef"

    @builtins.property
    @jsii.member(jsii_name="securityProfileRef")
    def security_profile_ref(self) -> "SecurityProfileReference":
        '''(experimental) A reference to a SecurityProfile resource.

        :stability: experimental
        '''
        return typing.cast("SecurityProfileReference", jsii.get(self, "securityProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityProfileRef).__jsii_proxy_class__ = lambda : _ISecurityProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.ITaskTemplateRef")
class ITaskTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TaskTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="taskTemplateRef")
    def task_template_ref(self) -> "TaskTemplateReference":
        '''(experimental) A reference to a TaskTemplate resource.

        :stability: experimental
        '''
        ...


class _ITaskTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TaskTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.ITaskTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="taskTemplateRef")
    def task_template_ref(self) -> "TaskTemplateReference":
        '''(experimental) A reference to a TaskTemplate resource.

        :stability: experimental
        '''
        return typing.cast("TaskTemplateReference", jsii.get(self, "taskTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITaskTemplateRef).__jsii_proxy_class__ = lambda : _ITaskTemplateRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.ITrafficDistributionGroupRef"
)
class ITrafficDistributionGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficDistributionGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trafficDistributionGroupRef")
    def traffic_distribution_group_ref(self) -> "TrafficDistributionGroupReference":
        '''(experimental) A reference to a TrafficDistributionGroup resource.

        :stability: experimental
        '''
        ...


class _ITrafficDistributionGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficDistributionGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.ITrafficDistributionGroupRef"

    @builtins.property
    @jsii.member(jsii_name="trafficDistributionGroupRef")
    def traffic_distribution_group_ref(self) -> "TrafficDistributionGroupReference":
        '''(experimental) A reference to a TrafficDistributionGroup resource.

        :stability: experimental
        '''
        return typing.cast("TrafficDistributionGroupReference", jsii.get(self, "trafficDistributionGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrafficDistributionGroupRef).__jsii_proxy_class__ = lambda : _ITrafficDistributionGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IUserHierarchyGroupRef")
class IUserHierarchyGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserHierarchyGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userHierarchyGroupRef")
    def user_hierarchy_group_ref(self) -> "UserHierarchyGroupReference":
        '''(experimental) A reference to a UserHierarchyGroup resource.

        :stability: experimental
        '''
        ...


class _IUserHierarchyGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserHierarchyGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IUserHierarchyGroupRef"

    @builtins.property
    @jsii.member(jsii_name="userHierarchyGroupRef")
    def user_hierarchy_group_ref(self) -> "UserHierarchyGroupReference":
        '''(experimental) A reference to a UserHierarchyGroup resource.

        :stability: experimental
        '''
        return typing.cast("UserHierarchyGroupReference", jsii.get(self, "userHierarchyGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserHierarchyGroupRef).__jsii_proxy_class__ = lambda : _IUserHierarchyGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.IUserHierarchyStructureRef"
)
class IUserHierarchyStructureRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserHierarchyStructure.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userHierarchyStructureRef")
    def user_hierarchy_structure_ref(self) -> "UserHierarchyStructureReference":
        '''(experimental) A reference to a UserHierarchyStructure resource.

        :stability: experimental
        '''
        ...


class _IUserHierarchyStructureRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserHierarchyStructure.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IUserHierarchyStructureRef"

    @builtins.property
    @jsii.member(jsii_name="userHierarchyStructureRef")
    def user_hierarchy_structure_ref(self) -> "UserHierarchyStructureReference":
        '''(experimental) A reference to a UserHierarchyStructure resource.

        :stability: experimental
        '''
        return typing.cast("UserHierarchyStructureReference", jsii.get(self, "userHierarchyStructureRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserHierarchyStructureRef).__jsii_proxy_class__ = lambda : _IUserHierarchyStructureRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IUserRef")
class IUserRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a User.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "UserReference":
        '''(experimental) A reference to a User resource.

        :stability: experimental
        '''
        ...


class _IUserRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a User.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IUserRef"

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "UserReference":
        '''(experimental) A reference to a User resource.

        :stability: experimental
        '''
        return typing.cast("UserReference", jsii.get(self, "userRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserRef).__jsii_proxy_class__ = lambda : _IUserRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IViewRef")
class IViewRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a View.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="viewRef")
    def view_ref(self) -> "ViewReference":
        '''(experimental) A reference to a View resource.

        :stability: experimental
        '''
        ...


class _IViewRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a View.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IViewRef"

    @builtins.property
    @jsii.member(jsii_name="viewRef")
    def view_ref(self) -> "ViewReference":
        '''(experimental) A reference to a View resource.

        :stability: experimental
        '''
        return typing.cast("ViewReference", jsii.get(self, "viewRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IViewRef).__jsii_proxy_class__ = lambda : _IViewRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IViewVersionRef")
class IViewVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ViewVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="viewVersionRef")
    def view_version_ref(self) -> "ViewVersionReference":
        '''(experimental) A reference to a ViewVersion resource.

        :stability: experimental
        '''
        ...


class _IViewVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ViewVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IViewVersionRef"

    @builtins.property
    @jsii.member(jsii_name="viewVersionRef")
    def view_version_ref(self) -> "ViewVersionReference":
        '''(experimental) A reference to a ViewVersion resource.

        :stability: experimental
        '''
        return typing.cast("ViewVersionReference", jsii.get(self, "viewVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IViewVersionRef).__jsii_proxy_class__ = lambda : _IViewVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connect.IWorkspaceRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connect.IWorkspaceRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_connect.InstanceReference",
    jsii_struct_bases=[],
    name_mapping={"instance_arn": "instanceArn"},
)
class InstanceReference:
    def __init__(self, *, instance_arn: builtins.str) -> None:
        '''A reference to a Instance resource.

        :param instance_arn: The Arn of the Instance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            instance_reference = interfaces_connect.InstanceReference(
                instance_arn="instanceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b76dd1eb3d9005eac5fb96ac7e63df95d3bf741cb41df73de65028580b6b162)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The Arn of the Instance resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_connect.InstanceStorageConfigReference",
    jsii_struct_bases=[],
    name_mapping={
        "association_id": "associationId",
        "instance_arn": "instanceArn",
        "resource_type": "resourceType",
    },
)
class InstanceStorageConfigReference:
    def __init__(
        self,
        *,
        association_id: builtins.str,
        instance_arn: builtins.str,
        resource_type: builtins.str,
    ) -> None:
        '''A reference to a InstanceStorageConfig resource.

        :param association_id: The AssociationId of the InstanceStorageConfig resource.
        :param instance_arn: The InstanceArn of the InstanceStorageConfig resource.
        :param resource_type: The ResourceType of the InstanceStorageConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            instance_storage_config_reference = interfaces_connect.InstanceStorageConfigReference(
                association_id="associationId",
                instance_arn="instanceArn",
                resource_type="resourceType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4fc4417924caad1755e93ec3b6218e62a2b9def90ddb60999a95daf4804980)
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_id": association_id,
            "instance_arn": instance_arn,
            "resource_type": resource_type,
        }

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the InstanceStorageConfig resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The InstanceArn of the InstanceStorageConfig resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_type(self) -> builtins.str:
        '''The ResourceType of the InstanceStorageConfig resource.'''
        result = self._values.get("resource_type")
        assert result is not None, "Required property 'resource_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceStorageConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.IntegrationAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "instance_id": "instanceId",
        "integration_arn": "integrationArn",
        "integration_type": "integrationType",
    },
)
class IntegrationAssociationReference:
    def __init__(
        self,
        *,
        instance_id: builtins.str,
        integration_arn: builtins.str,
        integration_type: builtins.str,
    ) -> None:
        '''A reference to a IntegrationAssociation resource.

        :param instance_id: The InstanceId of the IntegrationAssociation resource.
        :param integration_arn: The IntegrationArn of the IntegrationAssociation resource.
        :param integration_type: The IntegrationType of the IntegrationAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            integration_association_reference = interfaces_connect.IntegrationAssociationReference(
                instance_id="instanceId",
                integration_arn="integrationArn",
                integration_type="integrationType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5999c1ba890f4adfda7054c24861a2310b5ba7a9a28f49ee65ee35f0151b82c)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument integration_arn", value=integration_arn, expected_type=type_hints["integration_arn"])
            check_type(argname="argument integration_type", value=integration_type, expected_type=type_hints["integration_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "integration_arn": integration_arn,
            "integration_type": integration_type,
        }

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The InstanceId of the IntegrationAssociation resource.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_arn(self) -> builtins.str:
        '''The IntegrationArn of the IntegrationAssociation resource.'''
        result = self._values.get("integration_arn")
        assert result is not None, "Required property 'integration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_type(self) -> builtins.str:
        '''The IntegrationType of the IntegrationAssociation resource.'''
        result = self._values.get("integration_type")
        assert result is not None, "Required property 'integration_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.NotificationReference",
    jsii_struct_bases=[],
    name_mapping={"notification_arn": "notificationArn"},
)
class NotificationReference:
    def __init__(self, *, notification_arn: builtins.str) -> None:
        '''A reference to a Notification resource.

        :param notification_arn: The Arn of the Notification resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            notification_reference = interfaces_connect.NotificationReference(
                notification_arn="notificationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f4ece0f255a501d0bd96693eb9db3bee21572a43e2fd821454853291e5c8f9e)
            check_type(argname="argument notification_arn", value=notification_arn, expected_type=type_hints["notification_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "notification_arn": notification_arn,
        }

    @builtins.property
    def notification_arn(self) -> builtins.str:
        '''The Arn of the Notification resource.'''
        result = self._values.get("notification_arn")
        assert result is not None, "Required property 'notification_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.PhoneNumberReference",
    jsii_struct_bases=[],
    name_mapping={"phone_number_arn": "phoneNumberArn"},
)
class PhoneNumberReference:
    def __init__(self, *, phone_number_arn: builtins.str) -> None:
        '''A reference to a PhoneNumber resource.

        :param phone_number_arn: The PhoneNumberArn of the PhoneNumber resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            phone_number_reference = interfaces_connect.PhoneNumberReference(
                phone_number_arn="phoneNumberArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a017fc00d1c7cb21da571675bdda55010f440fa23e8e172f4a3b24f6bdaf5415)
            check_type(argname="argument phone_number_arn", value=phone_number_arn, expected_type=type_hints["phone_number_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "phone_number_arn": phone_number_arn,
        }

    @builtins.property
    def phone_number_arn(self) -> builtins.str:
        '''The PhoneNumberArn of the PhoneNumber resource.'''
        result = self._values.get("phone_number_arn")
        assert result is not None, "Required property 'phone_number_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PhoneNumberReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.PredefinedAttributeReference",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "predefined_attribute_name": "predefinedAttributeName",
    },
)
class PredefinedAttributeReference:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        predefined_attribute_name: builtins.str,
    ) -> None:
        '''A reference to a PredefinedAttribute resource.

        :param instance_arn: The InstanceArn of the PredefinedAttribute resource.
        :param predefined_attribute_name: The Name of the PredefinedAttribute resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            predefined_attribute_reference = interfaces_connect.PredefinedAttributeReference(
                instance_arn="instanceArn",
                predefined_attribute_name="predefinedAttributeName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1241b67955ca029382e8d7366caa0f732171738edf7def115902c0eb75ba1705)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument predefined_attribute_name", value=predefined_attribute_name, expected_type=type_hints["predefined_attribute_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "predefined_attribute_name": predefined_attribute_name,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The InstanceArn of the PredefinedAttribute resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def predefined_attribute_name(self) -> builtins.str:
        '''The Name of the PredefinedAttribute resource.'''
        result = self._values.get("predefined_attribute_name")
        assert result is not None, "Required property 'predefined_attribute_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PredefinedAttributeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.PromptReference",
    jsii_struct_bases=[],
    name_mapping={"prompt_arn": "promptArn"},
)
class PromptReference:
    def __init__(self, *, prompt_arn: builtins.str) -> None:
        '''A reference to a Prompt resource.

        :param prompt_arn: The PromptArn of the Prompt resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            prompt_reference = interfaces_connect.PromptReference(
                prompt_arn="promptArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d55b69f9fecfdd078d9274c7d3c724a275fb3a37dbf1567237993e5c3dad4690)
            check_type(argname="argument prompt_arn", value=prompt_arn, expected_type=type_hints["prompt_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prompt_arn": prompt_arn,
        }

    @builtins.property
    def prompt_arn(self) -> builtins.str:
        '''The PromptArn of the Prompt resource.'''
        result = self._values.get("prompt_arn")
        assert result is not None, "Required property 'prompt_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PromptReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.QueueReference",
    jsii_struct_bases=[],
    name_mapping={"queue_arn": "queueArn"},
)
class QueueReference:
    def __init__(self, *, queue_arn: builtins.str) -> None:
        '''A reference to a Queue resource.

        :param queue_arn: The QueueArn of the Queue resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            queue_reference = interfaces_connect.QueueReference(
                queue_arn="queueArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27ae30bde80531a7290c70df5b8d8deb2082f04620811bc2cb904fb363bfd383)
            check_type(argname="argument queue_arn", value=queue_arn, expected_type=type_hints["queue_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "queue_arn": queue_arn,
        }

    @builtins.property
    def queue_arn(self) -> builtins.str:
        '''The QueueArn of the Queue resource.'''
        result = self._values.get("queue_arn")
        assert result is not None, "Required property 'queue_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.QuickConnectReference",
    jsii_struct_bases=[],
    name_mapping={"quick_connect_arn": "quickConnectArn"},
)
class QuickConnectReference:
    def __init__(self, *, quick_connect_arn: builtins.str) -> None:
        '''A reference to a QuickConnect resource.

        :param quick_connect_arn: The QuickConnectArn of the QuickConnect resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            quick_connect_reference = interfaces_connect.QuickConnectReference(
                quick_connect_arn="quickConnectArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61a9f07b8950a62478d108fcc8b7cc88257ae3ab15a2d5a0a6eeff2a6032a660)
            check_type(argname="argument quick_connect_arn", value=quick_connect_arn, expected_type=type_hints["quick_connect_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "quick_connect_arn": quick_connect_arn,
        }

    @builtins.property
    def quick_connect_arn(self) -> builtins.str:
        '''The QuickConnectArn of the QuickConnect resource.'''
        result = self._values.get("quick_connect_arn")
        assert result is not None, "Required property 'quick_connect_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuickConnectReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.RoutingProfileReference",
    jsii_struct_bases=[],
    name_mapping={"routing_profile_arn": "routingProfileArn"},
)
class RoutingProfileReference:
    def __init__(self, *, routing_profile_arn: builtins.str) -> None:
        '''A reference to a RoutingProfile resource.

        :param routing_profile_arn: The RoutingProfileArn of the RoutingProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            routing_profile_reference = interfaces_connect.RoutingProfileReference(
                routing_profile_arn="routingProfileArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d8e9adc471206e70d32a08e1e9311e9850a74b778329a4f2acfc0bd10fc2de1)
            check_type(argname="argument routing_profile_arn", value=routing_profile_arn, expected_type=type_hints["routing_profile_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "routing_profile_arn": routing_profile_arn,
        }

    @builtins.property
    def routing_profile_arn(self) -> builtins.str:
        '''The RoutingProfileArn of the RoutingProfile resource.'''
        result = self._values.get("routing_profile_arn")
        assert result is not None, "Required property 'routing_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoutingProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.RuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class RuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a Rule resource.

        :param rule_arn: The RuleArn of the Rule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            rule_reference = interfaces_connect.RuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0388549a3a18f273589be2892e2f4e691ef46c30d7457d3d5e09c6c7cd194df7)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the Rule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.SecurityKeyReference",
    jsii_struct_bases=[],
    name_mapping={"association_id": "associationId", "instance_id": "instanceId"},
)
class SecurityKeyReference:
    def __init__(
        self,
        *,
        association_id: builtins.str,
        instance_id: builtins.str,
    ) -> None:
        '''A reference to a SecurityKey resource.

        :param association_id: The AssociationId of the SecurityKey resource.
        :param instance_id: The InstanceId of the SecurityKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            security_key_reference = interfaces_connect.SecurityKeyReference(
                association_id="associationId",
                instance_id="instanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a21b74ea5d61053be00bd200db5a4e5a553cd6904bd5b26181227739a9cb351f)
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_id": association_id,
            "instance_id": instance_id,
        }

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the SecurityKey resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The InstanceId of the SecurityKey resource.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.SecurityProfileReference",
    jsii_struct_bases=[],
    name_mapping={"security_profile_arn": "securityProfileArn"},
)
class SecurityProfileReference:
    def __init__(self, *, security_profile_arn: builtins.str) -> None:
        '''A reference to a SecurityProfile resource.

        :param security_profile_arn: The SecurityProfileArn of the SecurityProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            security_profile_reference = interfaces_connect.SecurityProfileReference(
                security_profile_arn="securityProfileArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da3b85906eb1f9b6f3415843aadaf0d8deb77a8f169449cfa7d84796c0932faa)
            check_type(argname="argument security_profile_arn", value=security_profile_arn, expected_type=type_hints["security_profile_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_profile_arn": security_profile_arn,
        }

    @builtins.property
    def security_profile_arn(self) -> builtins.str:
        '''The SecurityProfileArn of the SecurityProfile resource.'''
        result = self._values.get("security_profile_arn")
        assert result is not None, "Required property 'security_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.TaskTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"task_template_arn": "taskTemplateArn"},
)
class TaskTemplateReference:
    def __init__(self, *, task_template_arn: builtins.str) -> None:
        '''A reference to a TaskTemplate resource.

        :param task_template_arn: The Arn of the TaskTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            task_template_reference = interfaces_connect.TaskTemplateReference(
                task_template_arn="taskTemplateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d2986f44b09563bb2a18f28dc14dc32045ae58bdb7a88833bb825b35ddbc07c)
            check_type(argname="argument task_template_arn", value=task_template_arn, expected_type=type_hints["task_template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_template_arn": task_template_arn,
        }

    @builtins.property
    def task_template_arn(self) -> builtins.str:
        '''The Arn of the TaskTemplate resource.'''
        result = self._values.get("task_template_arn")
        assert result is not None, "Required property 'task_template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.TrafficDistributionGroupReference",
    jsii_struct_bases=[],
    name_mapping={"traffic_distribution_group_arn": "trafficDistributionGroupArn"},
)
class TrafficDistributionGroupReference:
    def __init__(self, *, traffic_distribution_group_arn: builtins.str) -> None:
        '''A reference to a TrafficDistributionGroup resource.

        :param traffic_distribution_group_arn: The TrafficDistributionGroupArn of the TrafficDistributionGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            traffic_distribution_group_reference = interfaces_connect.TrafficDistributionGroupReference(
                traffic_distribution_group_arn="trafficDistributionGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c796f8e45b121ab681d015e3771a509db889301a7e8baac72a2019b83b4601eb)
            check_type(argname="argument traffic_distribution_group_arn", value=traffic_distribution_group_arn, expected_type=type_hints["traffic_distribution_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "traffic_distribution_group_arn": traffic_distribution_group_arn,
        }

    @builtins.property
    def traffic_distribution_group_arn(self) -> builtins.str:
        '''The TrafficDistributionGroupArn of the TrafficDistributionGroup resource.'''
        result = self._values.get("traffic_distribution_group_arn")
        assert result is not None, "Required property 'traffic_distribution_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficDistributionGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.UserHierarchyGroupReference",
    jsii_struct_bases=[],
    name_mapping={"user_hierarchy_group_arn": "userHierarchyGroupArn"},
)
class UserHierarchyGroupReference:
    def __init__(self, *, user_hierarchy_group_arn: builtins.str) -> None:
        '''A reference to a UserHierarchyGroup resource.

        :param user_hierarchy_group_arn: The UserHierarchyGroupArn of the UserHierarchyGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            user_hierarchy_group_reference = interfaces_connect.UserHierarchyGroupReference(
                user_hierarchy_group_arn="userHierarchyGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bf3a8ec9856720f13fb245a1598df9f51892a36db03120b151e698a43a76193)
            check_type(argname="argument user_hierarchy_group_arn", value=user_hierarchy_group_arn, expected_type=type_hints["user_hierarchy_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_hierarchy_group_arn": user_hierarchy_group_arn,
        }

    @builtins.property
    def user_hierarchy_group_arn(self) -> builtins.str:
        '''The UserHierarchyGroupArn of the UserHierarchyGroup resource.'''
        result = self._values.get("user_hierarchy_group_arn")
        assert result is not None, "Required property 'user_hierarchy_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserHierarchyGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.UserHierarchyStructureReference",
    jsii_struct_bases=[],
    name_mapping={"user_hierarchy_structure_arn": "userHierarchyStructureArn"},
)
class UserHierarchyStructureReference:
    def __init__(self, *, user_hierarchy_structure_arn: builtins.str) -> None:
        '''A reference to a UserHierarchyStructure resource.

        :param user_hierarchy_structure_arn: The UserHierarchyStructureArn of the UserHierarchyStructure resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            user_hierarchy_structure_reference = interfaces_connect.UserHierarchyStructureReference(
                user_hierarchy_structure_arn="userHierarchyStructureArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9427e68950421072d2545a0bc15ab942d9f19a69c2f5a7e6a57c0811e2fb51c9)
            check_type(argname="argument user_hierarchy_structure_arn", value=user_hierarchy_structure_arn, expected_type=type_hints["user_hierarchy_structure_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_hierarchy_structure_arn": user_hierarchy_structure_arn,
        }

    @builtins.property
    def user_hierarchy_structure_arn(self) -> builtins.str:
        '''The UserHierarchyStructureArn of the UserHierarchyStructure resource.'''
        result = self._values.get("user_hierarchy_structure_arn")
        assert result is not None, "Required property 'user_hierarchy_structure_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserHierarchyStructureReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.UserReference",
    jsii_struct_bases=[],
    name_mapping={"user_arn": "userArn"},
)
class UserReference:
    def __init__(self, *, user_arn: builtins.str) -> None:
        '''A reference to a User resource.

        :param user_arn: The UserArn of the User resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            user_reference = interfaces_connect.UserReference(
                user_arn="userArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__539758d567c9a4a5ddb2d8ac3ec97c0389bab53bc9c8bf8042f80416ec4759e6)
            check_type(argname="argument user_arn", value=user_arn, expected_type=type_hints["user_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_arn": user_arn,
        }

    @builtins.property
    def user_arn(self) -> builtins.str:
        '''The UserArn of the User resource.'''
        result = self._values.get("user_arn")
        assert result is not None, "Required property 'user_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.ViewReference",
    jsii_struct_bases=[],
    name_mapping={"view_arn": "viewArn"},
)
class ViewReference:
    def __init__(self, *, view_arn: builtins.str) -> None:
        '''A reference to a View resource.

        :param view_arn: The ViewArn of the View resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            view_reference = interfaces_connect.ViewReference(
                view_arn="viewArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00ff6f35080638036af764fa6c3eb9fa880d119d801ce3f9a958f4241dc4d400)
            check_type(argname="argument view_arn", value=view_arn, expected_type=type_hints["view_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "view_arn": view_arn,
        }

    @builtins.property
    def view_arn(self) -> builtins.str:
        '''The ViewArn of the View resource.'''
        result = self._values.get("view_arn")
        assert result is not None, "Required property 'view_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ViewReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.ViewVersionReference",
    jsii_struct_bases=[],
    name_mapping={"view_version_arn": "viewVersionArn"},
)
class ViewVersionReference:
    def __init__(self, *, view_version_arn: builtins.str) -> None:
        '''A reference to a ViewVersion resource.

        :param view_version_arn: The ViewVersionArn of the ViewVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            view_version_reference = interfaces_connect.ViewVersionReference(
                view_version_arn="viewVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deae179674b96a536a16655001cf7da75f0dd842cd313daf145cd60ccff2aec3)
            check_type(argname="argument view_version_arn", value=view_version_arn, expected_type=type_hints["view_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "view_version_arn": view_version_arn,
        }

    @builtins.property
    def view_version_arn(self) -> builtins.str:
        '''The ViewVersionArn of the ViewVersion resource.'''
        result = self._values.get("view_version_arn")
        assert result is not None, "Required property 'view_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ViewVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_connect.WorkspaceReference",
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
            from aws_cdk.interfaces import aws_connect as interfaces_connect
            
            workspace_reference = interfaces_connect.WorkspaceReference(
                workspace_arn="workspaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59549022c53269d7289aa349f0070431eec816e9588f5cf8c4a4c8e463b0325a)
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
    "AgentStatusReference",
    "ApprovedOriginReference",
    "ContactFlowModuleAliasReference",
    "ContactFlowModuleReference",
    "ContactFlowModuleVersionReference",
    "ContactFlowReference",
    "ContactFlowVersionReference",
    "DataTableAttributeReference",
    "DataTableRecordReference",
    "DataTableReference",
    "EmailAddressReference",
    "EvaluationFormReference",
    "HoursOfOperationReference",
    "IAgentStatusRef",
    "IApprovedOriginRef",
    "IContactFlowModuleAliasRef",
    "IContactFlowModuleRef",
    "IContactFlowModuleVersionRef",
    "IContactFlowRef",
    "IContactFlowVersionRef",
    "IDataTableAttributeRef",
    "IDataTableRecordRef",
    "IDataTableRef",
    "IEmailAddressRef",
    "IEvaluationFormRef",
    "IHoursOfOperationRef",
    "IInstanceRef",
    "IInstanceStorageConfigRef",
    "IIntegrationAssociationRef",
    "INotificationRef",
    "IPhoneNumberRef",
    "IPredefinedAttributeRef",
    "IPromptRef",
    "IQueueRef",
    "IQuickConnectRef",
    "IRoutingProfileRef",
    "IRuleRef",
    "ISecurityKeyRef",
    "ISecurityProfileRef",
    "ITaskTemplateRef",
    "ITrafficDistributionGroupRef",
    "IUserHierarchyGroupRef",
    "IUserHierarchyStructureRef",
    "IUserRef",
    "IViewRef",
    "IViewVersionRef",
    "IWorkspaceRef",
    "InstanceReference",
    "InstanceStorageConfigReference",
    "IntegrationAssociationReference",
    "NotificationReference",
    "PhoneNumberReference",
    "PredefinedAttributeReference",
    "PromptReference",
    "QueueReference",
    "QuickConnectReference",
    "RoutingProfileReference",
    "RuleReference",
    "SecurityKeyReference",
    "SecurityProfileReference",
    "TaskTemplateReference",
    "TrafficDistributionGroupReference",
    "UserHierarchyGroupReference",
    "UserHierarchyStructureReference",
    "UserReference",
    "ViewReference",
    "ViewVersionReference",
    "WorkspaceReference",
]

publication.publish()

def _typecheckingstub__80c2ee1f86d017d30c810fdfe35ebe75edb827c0c9b72fce1dfaea275aebbeaa(
    *,
    agent_status_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__420107c3fcd91bed4de5358f4760ba480949bdc8881c5d0538f7ef3c2b2b5dca(
    *,
    instance_id: builtins.str,
    origin: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20d4bbaa3402801ecaedf7fd115c6b26c722e3c434fea3b3c5595d76f6875dbf(
    *,
    contact_flow_module_alias_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ec59a97e450b6e15ebf5f88fe0e6ba5fd33f4df09f3ba1201e6804bf44c54c7(
    *,
    contact_flow_module_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__765dc1aed839fcfb38c331a611567553c325090dc403c41e00e34926961cf6fc(
    *,
    contact_flow_module_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dfa181ff2c0859219dbf48106492ecead1b4da0281898a69b709514db4d8f00(
    *,
    contact_flow_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f8ed10dcdc4a77bc2068dd63220cfc0b8add9c5c8c1020fec0826fbf1cecaa1(
    *,
    contact_flow_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e5c1d586322eb5f50ced0dfce17a7353fcfd770475aabc413e355fcebf55c8(
    *,
    attribute_id: builtins.str,
    data_table_arn: builtins.str,
    instance_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a889d8714c4a728775a98ceba8c53a6fe42518e93b4afe450277d0437e88e7b(
    *,
    data_table_arn: builtins.str,
    instance_arn: builtins.str,
    record_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67ba9770097234b94f825ce5d9299c6c020d31311df11a5f307f8a110b95ce7e(
    *,
    data_table_arn: builtins.str,
    instance_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6089d57da936a584df9a8b70f9f44fb73b442ddc2498e220add2c31f7faba584(
    *,
    email_address_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5264e070ad3ac631aba777dd6c2a9c99c524dafea18344334f59097bfbddbb1(
    *,
    evaluation_form_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__963a1a8b18b2bbfd6eb3ab2343ba1df7da95bee1b6c17ccec51bc122ecdcd770(
    *,
    hours_of_operation_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b76dd1eb3d9005eac5fb96ac7e63df95d3bf741cb41df73de65028580b6b162(
    *,
    instance_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4fc4417924caad1755e93ec3b6218e62a2b9def90ddb60999a95daf4804980(
    *,
    association_id: builtins.str,
    instance_arn: builtins.str,
    resource_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5999c1ba890f4adfda7054c24861a2310b5ba7a9a28f49ee65ee35f0151b82c(
    *,
    instance_id: builtins.str,
    integration_arn: builtins.str,
    integration_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f4ece0f255a501d0bd96693eb9db3bee21572a43e2fd821454853291e5c8f9e(
    *,
    notification_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a017fc00d1c7cb21da571675bdda55010f440fa23e8e172f4a3b24f6bdaf5415(
    *,
    phone_number_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1241b67955ca029382e8d7366caa0f732171738edf7def115902c0eb75ba1705(
    *,
    instance_arn: builtins.str,
    predefined_attribute_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d55b69f9fecfdd078d9274c7d3c724a275fb3a37dbf1567237993e5c3dad4690(
    *,
    prompt_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27ae30bde80531a7290c70df5b8d8deb2082f04620811bc2cb904fb363bfd383(
    *,
    queue_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61a9f07b8950a62478d108fcc8b7cc88257ae3ab15a2d5a0a6eeff2a6032a660(
    *,
    quick_connect_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d8e9adc471206e70d32a08e1e9311e9850a74b778329a4f2acfc0bd10fc2de1(
    *,
    routing_profile_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0388549a3a18f273589be2892e2f4e691ef46c30d7457d3d5e09c6c7cd194df7(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a21b74ea5d61053be00bd200db5a4e5a553cd6904bd5b26181227739a9cb351f(
    *,
    association_id: builtins.str,
    instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da3b85906eb1f9b6f3415843aadaf0d8deb77a8f169449cfa7d84796c0932faa(
    *,
    security_profile_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d2986f44b09563bb2a18f28dc14dc32045ae58bdb7a88833bb825b35ddbc07c(
    *,
    task_template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c796f8e45b121ab681d015e3771a509db889301a7e8baac72a2019b83b4601eb(
    *,
    traffic_distribution_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bf3a8ec9856720f13fb245a1598df9f51892a36db03120b151e698a43a76193(
    *,
    user_hierarchy_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9427e68950421072d2545a0bc15ab942d9f19a69c2f5a7e6a57c0811e2fb51c9(
    *,
    user_hierarchy_structure_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__539758d567c9a4a5ddb2d8ac3ec97c0389bab53bc9c8bf8042f80416ec4759e6(
    *,
    user_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00ff6f35080638036af764fa6c3eb9fa880d119d801ce3f9a958f4241dc4d400(
    *,
    view_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deae179674b96a536a16655001cf7da75f0dd842cd313daf145cd60ccff2aec3(
    *,
    view_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59549022c53269d7289aa349f0070431eec816e9588f5cf8c4a4c8e463b0325a(
    *,
    workspace_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAgentStatusRef, IApprovedOriginRef, IContactFlowModuleAliasRef, IContactFlowModuleRef, IContactFlowModuleVersionRef, IContactFlowRef, IContactFlowVersionRef, IDataTableAttributeRef, IDataTableRecordRef, IDataTableRef, IEmailAddressRef, IEvaluationFormRef, IHoursOfOperationRef, IInstanceRef, IInstanceStorageConfigRef, IIntegrationAssociationRef, INotificationRef, IPhoneNumberRef, IPredefinedAttributeRef, IPromptRef, IQueueRef, IQuickConnectRef, IRoutingProfileRef, IRuleRef, ISecurityKeyRef, ISecurityProfileRef, ITaskTemplateRef, ITrafficDistributionGroupRef, IUserHierarchyGroupRef, IUserHierarchyStructureRef, IUserRef, IViewRef, IViewVersionRef, IWorkspaceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
