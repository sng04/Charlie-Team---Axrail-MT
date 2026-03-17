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
    jsii_type="aws-cdk-lib.interfaces.aws_sso.ApplicationAssignmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_arn": "applicationArn",
        "principal_id": "principalId",
        "principal_type": "principalType",
    },
)
class ApplicationAssignmentReference:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
    ) -> None:
        '''A reference to a ApplicationAssignment resource.

        :param application_arn: The ApplicationArn of the ApplicationAssignment resource.
        :param principal_id: The PrincipalId of the ApplicationAssignment resource.
        :param principal_type: The PrincipalType of the ApplicationAssignment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sso as interfaces_sso
            
            application_assignment_reference = interfaces_sso.ApplicationAssignmentReference(
                application_arn="applicationArn",
                principal_id="principalId",
                principal_type="principalType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b7073aa1727024938c13e56fb36c80a014de0a50acda93c269840c3360e87c)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument principal_id", value=principal_id, expected_type=type_hints["principal_id"])
            check_type(argname="argument principal_type", value=principal_type, expected_type=type_hints["principal_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "principal_id": principal_id,
            "principal_type": principal_type,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ApplicationArn of the ApplicationAssignment resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_id(self) -> builtins.str:
        '''The PrincipalId of the ApplicationAssignment resource.'''
        result = self._values.get("principal_id")
        assert result is not None, "Required property 'principal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_type(self) -> builtins.str:
        '''The PrincipalType of the ApplicationAssignment resource.'''
        result = self._values.get("principal_type")
        assert result is not None, "Required property 'principal_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationAssignmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sso.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_arn": "applicationArn"},
)
class ApplicationReference:
    def __init__(self, *, application_arn: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_arn: The ApplicationArn of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sso as interfaces_sso
            
            application_reference = interfaces_sso.ApplicationReference(
                application_arn="applicationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa77687bcbd6afb697dce243636932845b725aa99f21a8a1b8f51b9999449dfb)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ApplicationArn of the Application resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sso.AssignmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "permission_set_arn": "permissionSetArn",
        "principal_id": "principalId",
        "principal_type": "principalType",
        "target_id": "targetId",
        "target_type": "targetType",
    },
)
class AssignmentReference:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
        principal_id: builtins.str,
        principal_type: builtins.str,
        target_id: builtins.str,
        target_type: builtins.str,
    ) -> None:
        '''A reference to a Assignment resource.

        :param instance_arn: The InstanceArn of the Assignment resource.
        :param permission_set_arn: The PermissionSetArn of the Assignment resource.
        :param principal_id: The PrincipalId of the Assignment resource.
        :param principal_type: The PrincipalType of the Assignment resource.
        :param target_id: The TargetId of the Assignment resource.
        :param target_type: The TargetType of the Assignment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sso as interfaces_sso
            
            assignment_reference = interfaces_sso.AssignmentReference(
                instance_arn="instanceArn",
                permission_set_arn="permissionSetArn",
                principal_id="principalId",
                principal_type="principalType",
                target_id="targetId",
                target_type="targetType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b28a75e042845fa476f01bebde42545ce8c82757c5882f6aaebeb3e9ec38fb3)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument permission_set_arn", value=permission_set_arn, expected_type=type_hints["permission_set_arn"])
            check_type(argname="argument principal_id", value=principal_id, expected_type=type_hints["principal_id"])
            check_type(argname="argument principal_type", value=principal_type, expected_type=type_hints["principal_type"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
            check_type(argname="argument target_type", value=target_type, expected_type=type_hints["target_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "permission_set_arn": permission_set_arn,
            "principal_id": principal_id,
            "principal_type": principal_type,
            "target_id": target_id,
            "target_type": target_type,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The InstanceArn of the Assignment resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permission_set_arn(self) -> builtins.str:
        '''The PermissionSetArn of the Assignment resource.'''
        result = self._values.get("permission_set_arn")
        assert result is not None, "Required property 'permission_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_id(self) -> builtins.str:
        '''The PrincipalId of the Assignment resource.'''
        result = self._values.get("principal_id")
        assert result is not None, "Required property 'principal_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_type(self) -> builtins.str:
        '''The PrincipalType of the Assignment resource.'''
        result = self._values.get("principal_type")
        assert result is not None, "Required property 'principal_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''The TargetId of the Assignment resource.'''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_type(self) -> builtins.str:
        '''The TargetType of the Assignment resource.'''
        result = self._values.get("target_type")
        assert result is not None, "Required property 'target_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssignmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sso.IApplicationAssignmentRef")
class IApplicationAssignmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationAssignment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationAssignmentRef")
    def application_assignment_ref(self) -> "ApplicationAssignmentReference":
        '''(experimental) A reference to a ApplicationAssignment resource.

        :stability: experimental
        '''
        ...


class _IApplicationAssignmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationAssignment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sso.IApplicationAssignmentRef"

    @builtins.property
    @jsii.member(jsii_name="applicationAssignmentRef")
    def application_assignment_ref(self) -> "ApplicationAssignmentReference":
        '''(experimental) A reference to a ApplicationAssignment resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationAssignmentReference", jsii.get(self, "applicationAssignmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationAssignmentRef).__jsii_proxy_class__ = lambda : _IApplicationAssignmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sso.IApplicationRef")
class IApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        ...


class _IApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sso.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sso.IAssignmentRef")
class IAssignmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Assignment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="assignmentRef")
    def assignment_ref(self) -> "AssignmentReference":
        '''(experimental) A reference to a Assignment resource.

        :stability: experimental
        '''
        ...


class _IAssignmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Assignment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sso.IAssignmentRef"

    @builtins.property
    @jsii.member(jsii_name="assignmentRef")
    def assignment_ref(self) -> "AssignmentReference":
        '''(experimental) A reference to a Assignment resource.

        :stability: experimental
        '''
        return typing.cast("AssignmentReference", jsii.get(self, "assignmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssignmentRef).__jsii_proxy_class__ = lambda : _IAssignmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_sso.IInstanceAccessControlAttributeConfigurationRef"
)
class IInstanceAccessControlAttributeConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceAccessControlAttributeConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceAccessControlAttributeConfigurationRef")
    def instance_access_control_attribute_configuration_ref(
        self,
    ) -> "InstanceAccessControlAttributeConfigurationReference":
        '''(experimental) A reference to a InstanceAccessControlAttributeConfiguration resource.

        :stability: experimental
        '''
        ...


class _IInstanceAccessControlAttributeConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceAccessControlAttributeConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sso.IInstanceAccessControlAttributeConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="instanceAccessControlAttributeConfigurationRef")
    def instance_access_control_attribute_configuration_ref(
        self,
    ) -> "InstanceAccessControlAttributeConfigurationReference":
        '''(experimental) A reference to a InstanceAccessControlAttributeConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("InstanceAccessControlAttributeConfigurationReference", jsii.get(self, "instanceAccessControlAttributeConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceAccessControlAttributeConfigurationRef).__jsii_proxy_class__ = lambda : _IInstanceAccessControlAttributeConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sso.IInstanceRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sso.IInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        return typing.cast("InstanceReference", jsii.get(self, "instanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceRef).__jsii_proxy_class__ = lambda : _IInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sso.IPermissionSetRef")
class IPermissionSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PermissionSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="permissionSetRef")
    def permission_set_ref(self) -> "PermissionSetReference":
        '''(experimental) A reference to a PermissionSet resource.

        :stability: experimental
        '''
        ...


class _IPermissionSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PermissionSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sso.IPermissionSetRef"

    @builtins.property
    @jsii.member(jsii_name="permissionSetRef")
    def permission_set_ref(self) -> "PermissionSetReference":
        '''(experimental) A reference to a PermissionSet resource.

        :stability: experimental
        '''
        return typing.cast("PermissionSetReference", jsii.get(self, "permissionSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPermissionSetRef).__jsii_proxy_class__ = lambda : _IPermissionSetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sso.InstanceAccessControlAttributeConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"instance_arn": "instanceArn"},
)
class InstanceAccessControlAttributeConfigurationReference:
    def __init__(self, *, instance_arn: builtins.str) -> None:
        '''A reference to a InstanceAccessControlAttributeConfiguration resource.

        :param instance_arn: The InstanceArn of the InstanceAccessControlAttributeConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sso as interfaces_sso
            
            instance_access_control_attribute_configuration_reference = interfaces_sso.InstanceAccessControlAttributeConfigurationReference(
                instance_arn="instanceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6276a1e0604c92b2ff083e91265b3dd5bec3d37ddcdbba0cf410a1cf862862c9)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The InstanceArn of the InstanceAccessControlAttributeConfiguration resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceAccessControlAttributeConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sso.InstanceReference",
    jsii_struct_bases=[],
    name_mapping={"instance_arn": "instanceArn"},
)
class InstanceReference:
    def __init__(self, *, instance_arn: builtins.str) -> None:
        '''A reference to a Instance resource.

        :param instance_arn: The InstanceArn of the Instance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sso as interfaces_sso
            
            instance_reference = interfaces_sso.InstanceReference(
                instance_arn="instanceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e69c6f97dc3f6d758ffd2c375dd8069b113cfdb4694ded2a38f95ae317f7a280)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The InstanceArn of the Instance resource.'''
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
    jsii_type="aws-cdk-lib.interfaces.aws_sso.PermissionSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "instance_arn": "instanceArn",
        "permission_set_arn": "permissionSetArn",
    },
)
class PermissionSetReference:
    def __init__(
        self,
        *,
        instance_arn: builtins.str,
        permission_set_arn: builtins.str,
    ) -> None:
        '''A reference to a PermissionSet resource.

        :param instance_arn: The InstanceArn of the PermissionSet resource.
        :param permission_set_arn: The PermissionSetArn of the PermissionSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sso as interfaces_sso
            
            permission_set_reference = interfaces_sso.PermissionSetReference(
                instance_arn="instanceArn",
                permission_set_arn="permissionSetArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca11e913da510f673bdbcee699e7a609b1b2640eaa35681158c848adc52274ff)
            check_type(argname="argument instance_arn", value=instance_arn, expected_type=type_hints["instance_arn"])
            check_type(argname="argument permission_set_arn", value=permission_set_arn, expected_type=type_hints["permission_set_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_arn": instance_arn,
            "permission_set_arn": permission_set_arn,
        }

    @builtins.property
    def instance_arn(self) -> builtins.str:
        '''The InstanceArn of the PermissionSet resource.'''
        result = self._values.get("instance_arn")
        assert result is not None, "Required property 'instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permission_set_arn(self) -> builtins.str:
        '''The PermissionSetArn of the PermissionSet resource.'''
        result = self._values.get("permission_set_arn")
        assert result is not None, "Required property 'permission_set_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PermissionSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApplicationAssignmentReference",
    "ApplicationReference",
    "AssignmentReference",
    "IApplicationAssignmentRef",
    "IApplicationRef",
    "IAssignmentRef",
    "IInstanceAccessControlAttributeConfigurationRef",
    "IInstanceRef",
    "IPermissionSetRef",
    "InstanceAccessControlAttributeConfigurationReference",
    "InstanceReference",
    "PermissionSetReference",
]

publication.publish()

def _typecheckingstub__44b7073aa1727024938c13e56fb36c80a014de0a50acda93c269840c3360e87c(
    *,
    application_arn: builtins.str,
    principal_id: builtins.str,
    principal_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa77687bcbd6afb697dce243636932845b725aa99f21a8a1b8f51b9999449dfb(
    *,
    application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b28a75e042845fa476f01bebde42545ce8c82757c5882f6aaebeb3e9ec38fb3(
    *,
    instance_arn: builtins.str,
    permission_set_arn: builtins.str,
    principal_id: builtins.str,
    principal_type: builtins.str,
    target_id: builtins.str,
    target_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6276a1e0604c92b2ff083e91265b3dd5bec3d37ddcdbba0cf410a1cf862862c9(
    *,
    instance_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e69c6f97dc3f6d758ffd2c375dd8069b113cfdb4694ded2a38f95ae317f7a280(
    *,
    instance_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca11e913da510f673bdbcee699e7a609b1b2640eaa35681158c848adc52274ff(
    *,
    instance_arn: builtins.str,
    permission_set_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationAssignmentRef, IApplicationRef, IAssignmentRef, IInstanceAccessControlAttributeConfigurationRef, IInstanceRef, IPermissionSetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
