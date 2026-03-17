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
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.IIdMappingWorkflowRef"
)
class IIdMappingWorkflowRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdMappingWorkflow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="idMappingWorkflowRef")
    def id_mapping_workflow_ref(self) -> "IdMappingWorkflowReference":
        '''(experimental) A reference to a IdMappingWorkflow resource.

        :stability: experimental
        '''
        ...


class _IIdMappingWorkflowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdMappingWorkflow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_entityresolution.IIdMappingWorkflowRef"

    @builtins.property
    @jsii.member(jsii_name="idMappingWorkflowRef")
    def id_mapping_workflow_ref(self) -> "IdMappingWorkflowReference":
        '''(experimental) A reference to a IdMappingWorkflow resource.

        :stability: experimental
        '''
        return typing.cast("IdMappingWorkflowReference", jsii.get(self, "idMappingWorkflowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdMappingWorkflowRef).__jsii_proxy_class__ = lambda : _IIdMappingWorkflowRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.IIdNamespaceRef"
)
class IIdNamespaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdNamespace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="idNamespaceRef")
    def id_namespace_ref(self) -> "IdNamespaceReference":
        '''(experimental) A reference to a IdNamespace resource.

        :stability: experimental
        '''
        ...


class _IIdNamespaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdNamespace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_entityresolution.IIdNamespaceRef"

    @builtins.property
    @jsii.member(jsii_name="idNamespaceRef")
    def id_namespace_ref(self) -> "IdNamespaceReference":
        '''(experimental) A reference to a IdNamespace resource.

        :stability: experimental
        '''
        return typing.cast("IdNamespaceReference", jsii.get(self, "idNamespaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdNamespaceRef).__jsii_proxy_class__ = lambda : _IIdNamespaceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.IMatchingWorkflowRef"
)
class IMatchingWorkflowRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MatchingWorkflow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="matchingWorkflowRef")
    def matching_workflow_ref(self) -> "MatchingWorkflowReference":
        '''(experimental) A reference to a MatchingWorkflow resource.

        :stability: experimental
        '''
        ...


class _IMatchingWorkflowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MatchingWorkflow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_entityresolution.IMatchingWorkflowRef"

    @builtins.property
    @jsii.member(jsii_name="matchingWorkflowRef")
    def matching_workflow_ref(self) -> "MatchingWorkflowReference":
        '''(experimental) A reference to a MatchingWorkflow resource.

        :stability: experimental
        '''
        return typing.cast("MatchingWorkflowReference", jsii.get(self, "matchingWorkflowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMatchingWorkflowRef).__jsii_proxy_class__ = lambda : _IMatchingWorkflowRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.IPolicyStatementRef"
)
class IPolicyStatementRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyStatement.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="policyStatementRef")
    def policy_statement_ref(self) -> "PolicyStatementReference":
        '''(experimental) A reference to a PolicyStatement resource.

        :stability: experimental
        '''
        ...


class _IPolicyStatementRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyStatement.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_entityresolution.IPolicyStatementRef"

    @builtins.property
    @jsii.member(jsii_name="policyStatementRef")
    def policy_statement_ref(self) -> "PolicyStatementReference":
        '''(experimental) A reference to a PolicyStatement resource.

        :stability: experimental
        '''
        return typing.cast("PolicyStatementReference", jsii.get(self, "policyStatementRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyStatementRef).__jsii_proxy_class__ = lambda : _IPolicyStatementRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.ISchemaMappingRef"
)
class ISchemaMappingRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaMapping.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaMappingRef")
    def schema_mapping_ref(self) -> "SchemaMappingReference":
        '''(experimental) A reference to a SchemaMapping resource.

        :stability: experimental
        '''
        ...


class _ISchemaMappingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaMapping.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_entityresolution.ISchemaMappingRef"

    @builtins.property
    @jsii.member(jsii_name="schemaMappingRef")
    def schema_mapping_ref(self) -> "SchemaMappingReference":
        '''(experimental) A reference to a SchemaMapping resource.

        :stability: experimental
        '''
        return typing.cast("SchemaMappingReference", jsii.get(self, "schemaMappingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaMappingRef).__jsii_proxy_class__ = lambda : _ISchemaMappingRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.IdMappingWorkflowReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_name": "workflowName"},
)
class IdMappingWorkflowReference:
    def __init__(self, *, workflow_name: builtins.str) -> None:
        '''A reference to a IdMappingWorkflow resource.

        :param workflow_name: The WorkflowName of the IdMappingWorkflow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_entityresolution as interfaces_entityresolution
            
            id_mapping_workflow_reference = interfaces_entityresolution.IdMappingWorkflowReference(
                workflow_name="workflowName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37caac4f4b69db6d5f1130f5dc1b860f7214f7b71ef8c26965be0267e3b4a3ca)
            check_type(argname="argument workflow_name", value=workflow_name, expected_type=type_hints["workflow_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_name": workflow_name,
        }

    @builtins.property
    def workflow_name(self) -> builtins.str:
        '''The WorkflowName of the IdMappingWorkflow resource.'''
        result = self._values.get("workflow_name")
        assert result is not None, "Required property 'workflow_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdMappingWorkflowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.IdNamespaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "id_namespace_arn": "idNamespaceArn",
        "id_namespace_name": "idNamespaceName",
    },
)
class IdNamespaceReference:
    def __init__(
        self,
        *,
        id_namespace_arn: builtins.str,
        id_namespace_name: builtins.str,
    ) -> None:
        '''A reference to a IdNamespace resource.

        :param id_namespace_arn: The ARN of the IdNamespace resource.
        :param id_namespace_name: The IdNamespaceName of the IdNamespace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_entityresolution as interfaces_entityresolution
            
            id_namespace_reference = interfaces_entityresolution.IdNamespaceReference(
                id_namespace_arn="idNamespaceArn",
                id_namespace_name="idNamespaceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84946b161214154ee5fbee7ff1dfd58709fc4c388198fdae9f58349ce8f7de36)
            check_type(argname="argument id_namespace_arn", value=id_namespace_arn, expected_type=type_hints["id_namespace_arn"])
            check_type(argname="argument id_namespace_name", value=id_namespace_name, expected_type=type_hints["id_namespace_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "id_namespace_arn": id_namespace_arn,
            "id_namespace_name": id_namespace_name,
        }

    @builtins.property
    def id_namespace_arn(self) -> builtins.str:
        '''The ARN of the IdNamespace resource.'''
        result = self._values.get("id_namespace_arn")
        assert result is not None, "Required property 'id_namespace_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id_namespace_name(self) -> builtins.str:
        '''The IdNamespaceName of the IdNamespace resource.'''
        result = self._values.get("id_namespace_name")
        assert result is not None, "Required property 'id_namespace_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdNamespaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.MatchingWorkflowReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_name": "workflowName"},
)
class MatchingWorkflowReference:
    def __init__(self, *, workflow_name: builtins.str) -> None:
        '''A reference to a MatchingWorkflow resource.

        :param workflow_name: The WorkflowName of the MatchingWorkflow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_entityresolution as interfaces_entityresolution
            
            matching_workflow_reference = interfaces_entityresolution.MatchingWorkflowReference(
                workflow_name="workflowName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e14699b90393c25e0943578c10660c5d654fd6e1eba00d305dd38017a8cde25)
            check_type(argname="argument workflow_name", value=workflow_name, expected_type=type_hints["workflow_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_name": workflow_name,
        }

    @builtins.property
    def workflow_name(self) -> builtins.str:
        '''The WorkflowName of the MatchingWorkflow resource.'''
        result = self._values.get("workflow_name")
        assert result is not None, "Required property 'workflow_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MatchingWorkflowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.PolicyStatementReference",
    jsii_struct_bases=[],
    name_mapping={
        "policy_statement_arn": "policyStatementArn",
        "statement_id": "statementId",
    },
)
class PolicyStatementReference:
    def __init__(
        self,
        *,
        policy_statement_arn: builtins.str,
        statement_id: builtins.str,
    ) -> None:
        '''A reference to a PolicyStatement resource.

        :param policy_statement_arn: The Arn of the PolicyStatement resource.
        :param statement_id: The StatementId of the PolicyStatement resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_entityresolution as interfaces_entityresolution
            
            policy_statement_reference = interfaces_entityresolution.PolicyStatementReference(
                policy_statement_arn="policyStatementArn",
                statement_id="statementId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bfd6a0aa4cd92acd08d9aeddac23127972b6b8985b144c45122a8f1d1d962d0)
            check_type(argname="argument policy_statement_arn", value=policy_statement_arn, expected_type=type_hints["policy_statement_arn"])
            check_type(argname="argument statement_id", value=statement_id, expected_type=type_hints["statement_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_statement_arn": policy_statement_arn,
            "statement_id": statement_id,
        }

    @builtins.property
    def policy_statement_arn(self) -> builtins.str:
        '''The Arn of the PolicyStatement resource.'''
        result = self._values.get("policy_statement_arn")
        assert result is not None, "Required property 'policy_statement_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement_id(self) -> builtins.str:
        '''The StatementId of the PolicyStatement resource.'''
        result = self._values.get("statement_id")
        assert result is not None, "Required property 'statement_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyStatementReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_entityresolution.SchemaMappingReference",
    jsii_struct_bases=[],
    name_mapping={"schema_name": "schemaName"},
)
class SchemaMappingReference:
    def __init__(self, *, schema_name: builtins.str) -> None:
        '''A reference to a SchemaMapping resource.

        :param schema_name: The SchemaName of the SchemaMapping resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_entityresolution as interfaces_entityresolution
            
            schema_mapping_reference = interfaces_entityresolution.SchemaMappingReference(
                schema_name="schemaName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a833940eaa015fb2ddf4f62f8edf18d654bad5c95b977d78202bf6b5bd0929c)
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_name": schema_name,
        }

    @builtins.property
    def schema_name(self) -> builtins.str:
        '''The SchemaName of the SchemaMapping resource.'''
        result = self._values.get("schema_name")
        assert result is not None, "Required property 'schema_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaMappingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IIdMappingWorkflowRef",
    "IIdNamespaceRef",
    "IMatchingWorkflowRef",
    "IPolicyStatementRef",
    "ISchemaMappingRef",
    "IdMappingWorkflowReference",
    "IdNamespaceReference",
    "MatchingWorkflowReference",
    "PolicyStatementReference",
    "SchemaMappingReference",
]

publication.publish()

def _typecheckingstub__37caac4f4b69db6d5f1130f5dc1b860f7214f7b71ef8c26965be0267e3b4a3ca(
    *,
    workflow_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84946b161214154ee5fbee7ff1dfd58709fc4c388198fdae9f58349ce8f7de36(
    *,
    id_namespace_arn: builtins.str,
    id_namespace_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e14699b90393c25e0943578c10660c5d654fd6e1eba00d305dd38017a8cde25(
    *,
    workflow_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bfd6a0aa4cd92acd08d9aeddac23127972b6b8985b144c45122a8f1d1d962d0(
    *,
    policy_statement_arn: builtins.str,
    statement_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a833940eaa015fb2ddf4f62f8edf18d654bad5c95b977d78202bf6b5bd0929c(
    *,
    schema_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IIdMappingWorkflowRef, IIdNamespaceRef, IMatchingWorkflowRef, IPolicyStatementRef, ISchemaMappingRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
