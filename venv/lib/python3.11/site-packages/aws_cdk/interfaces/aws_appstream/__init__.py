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
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.AppBlockBuilderReference",
    jsii_struct_bases=[],
    name_mapping={
        "app_block_builder_arn": "appBlockBuilderArn",
        "app_block_builder_name": "appBlockBuilderName",
    },
)
class AppBlockBuilderReference:
    def __init__(
        self,
        *,
        app_block_builder_arn: builtins.str,
        app_block_builder_name: builtins.str,
    ) -> None:
        '''A reference to a AppBlockBuilder resource.

        :param app_block_builder_arn: The ARN of the AppBlockBuilder resource.
        :param app_block_builder_name: The Name of the AppBlockBuilder resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            app_block_builder_reference = interfaces_appstream.AppBlockBuilderReference(
                app_block_builder_arn="appBlockBuilderArn",
                app_block_builder_name="appBlockBuilderName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ccf44c8df86ddb2aaa3dd1c1344df0034b12c7bbaed1ab37b6250d970e02b0f)
            check_type(argname="argument app_block_builder_arn", value=app_block_builder_arn, expected_type=type_hints["app_block_builder_arn"])
            check_type(argname="argument app_block_builder_name", value=app_block_builder_name, expected_type=type_hints["app_block_builder_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_block_builder_arn": app_block_builder_arn,
            "app_block_builder_name": app_block_builder_name,
        }

    @builtins.property
    def app_block_builder_arn(self) -> builtins.str:
        '''The ARN of the AppBlockBuilder resource.'''
        result = self._values.get("app_block_builder_arn")
        assert result is not None, "Required property 'app_block_builder_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_block_builder_name(self) -> builtins.str:
        '''The Name of the AppBlockBuilder resource.'''
        result = self._values.get("app_block_builder_name")
        assert result is not None, "Required property 'app_block_builder_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppBlockBuilderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.AppBlockReference",
    jsii_struct_bases=[],
    name_mapping={"app_block_arn": "appBlockArn"},
)
class AppBlockReference:
    def __init__(self, *, app_block_arn: builtins.str) -> None:
        '''A reference to a AppBlock resource.

        :param app_block_arn: The Arn of the AppBlock resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            app_block_reference = interfaces_appstream.AppBlockReference(
                app_block_arn="appBlockArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__999361d2192091ecfd78bba01c6482ad6b51ef4092d3d6e058fcf3faa9dbd0e2)
            check_type(argname="argument app_block_arn", value=app_block_arn, expected_type=type_hints["app_block_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_block_arn": app_block_arn,
        }

    @builtins.property
    def app_block_arn(self) -> builtins.str:
        '''The Arn of the AppBlock resource.'''
        result = self._values.get("app_block_arn")
        assert result is not None, "Required property 'app_block_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppBlockReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.ApplicationEntitlementAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_identifier": "applicationIdentifier",
        "entitlement_name": "entitlementName",
        "stack_name": "stackName",
    },
)
class ApplicationEntitlementAssociationReference:
    def __init__(
        self,
        *,
        application_identifier: builtins.str,
        entitlement_name: builtins.str,
        stack_name: builtins.str,
    ) -> None:
        '''A reference to a ApplicationEntitlementAssociation resource.

        :param application_identifier: The ApplicationIdentifier of the ApplicationEntitlementAssociation resource.
        :param entitlement_name: The EntitlementName of the ApplicationEntitlementAssociation resource.
        :param stack_name: The StackName of the ApplicationEntitlementAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            application_entitlement_association_reference = interfaces_appstream.ApplicationEntitlementAssociationReference(
                application_identifier="applicationIdentifier",
                entitlement_name="entitlementName",
                stack_name="stackName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed86ac6d622d5886a019c6a70ccba7b459759e3530109ee3fcb194657d268885)
            check_type(argname="argument application_identifier", value=application_identifier, expected_type=type_hints["application_identifier"])
            check_type(argname="argument entitlement_name", value=entitlement_name, expected_type=type_hints["entitlement_name"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_identifier": application_identifier,
            "entitlement_name": entitlement_name,
            "stack_name": stack_name,
        }

    @builtins.property
    def application_identifier(self) -> builtins.str:
        '''The ApplicationIdentifier of the ApplicationEntitlementAssociation resource.'''
        result = self._values.get("application_identifier")
        assert result is not None, "Required property 'application_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entitlement_name(self) -> builtins.str:
        '''The EntitlementName of the ApplicationEntitlementAssociation resource.'''
        result = self._values.get("entitlement_name")
        assert result is not None, "Required property 'entitlement_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The StackName of the ApplicationEntitlementAssociation resource.'''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationEntitlementAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.ApplicationFleetAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"application_arn": "applicationArn", "fleet_name": "fleetName"},
)
class ApplicationFleetAssociationReference:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        fleet_name: builtins.str,
    ) -> None:
        '''A reference to a ApplicationFleetAssociation resource.

        :param application_arn: The ApplicationArn of the ApplicationFleetAssociation resource.
        :param fleet_name: The FleetName of the ApplicationFleetAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            application_fleet_association_reference = interfaces_appstream.ApplicationFleetAssociationReference(
                application_arn="applicationArn",
                fleet_name="fleetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__769a3917223ace7abfe471cf26313b453db8d1524a1dbbc471df0cb4285f6e51)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument fleet_name", value=fleet_name, expected_type=type_hints["fleet_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "fleet_name": fleet_name,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ApplicationArn of the ApplicationFleetAssociation resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fleet_name(self) -> builtins.str:
        '''The FleetName of the ApplicationFleetAssociation resource.'''
        result = self._values.get("fleet_name")
        assert result is not None, "Required property 'fleet_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationFleetAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_arn": "applicationArn"},
)
class ApplicationReference:
    def __init__(self, *, application_arn: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_arn: The Arn of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            application_reference = interfaces_appstream.ApplicationReference(
                application_arn="applicationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20e27f24e60cc84ecd4863218985a438ab83cddfd32614837a12eaccaef5b26d)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The Arn of the Application resource.'''
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
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.DirectoryConfigReference",
    jsii_struct_bases=[],
    name_mapping={"directory_name": "directoryName"},
)
class DirectoryConfigReference:
    def __init__(self, *, directory_name: builtins.str) -> None:
        '''A reference to a DirectoryConfig resource.

        :param directory_name: The DirectoryName of the DirectoryConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            directory_config_reference = interfaces_appstream.DirectoryConfigReference(
                directory_name="directoryName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0769cbea8784800cc76f29c4da14a24e3f6a31b7b69f3317cd404dd3dc7e2c51)
            check_type(argname="argument directory_name", value=directory_name, expected_type=type_hints["directory_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "directory_name": directory_name,
        }

    @builtins.property
    def directory_name(self) -> builtins.str:
        '''The DirectoryName of the DirectoryConfig resource.'''
        result = self._values.get("directory_name")
        assert result is not None, "Required property 'directory_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectoryConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.EntitlementReference",
    jsii_struct_bases=[],
    name_mapping={"entitlement_name": "entitlementName", "stack_name": "stackName"},
)
class EntitlementReference:
    def __init__(
        self,
        *,
        entitlement_name: builtins.str,
        stack_name: builtins.str,
    ) -> None:
        '''A reference to a Entitlement resource.

        :param entitlement_name: The Name of the Entitlement resource.
        :param stack_name: The StackName of the Entitlement resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            entitlement_reference = interfaces_appstream.EntitlementReference(
                entitlement_name="entitlementName",
                stack_name="stackName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5da2f4531a553fc09946f90e2f23bdd0a0a94f048a8afd6773a3cee741fdb4db)
            check_type(argname="argument entitlement_name", value=entitlement_name, expected_type=type_hints["entitlement_name"])
            check_type(argname="argument stack_name", value=stack_name, expected_type=type_hints["stack_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entitlement_name": entitlement_name,
            "stack_name": stack_name,
        }

    @builtins.property
    def entitlement_name(self) -> builtins.str:
        '''The Name of the Entitlement resource.'''
        result = self._values.get("entitlement_name")
        assert result is not None, "Required property 'entitlement_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stack_name(self) -> builtins.str:
        '''The StackName of the Entitlement resource.'''
        result = self._values.get("stack_name")
        assert result is not None, "Required property 'stack_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EntitlementReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.FleetReference",
    jsii_struct_bases=[],
    name_mapping={"fleet_id": "fleetId"},
)
class FleetReference:
    def __init__(self, *, fleet_id: builtins.str) -> None:
        '''A reference to a Fleet resource.

        :param fleet_id: The Id of the Fleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            fleet_reference = interfaces_appstream.FleetReference(
                fleet_id="fleetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ff6eedaec7cca9f61d584878f912a02aa3f25654ba401a7b5a184b2cbc6dd3e)
            check_type(argname="argument fleet_id", value=fleet_id, expected_type=type_hints["fleet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_id": fleet_id,
        }

    @builtins.property
    def fleet_id(self) -> builtins.str:
        '''The Id of the Fleet resource.'''
        result = self._values.get("fleet_id")
        assert result is not None, "Required property 'fleet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appstream.IAppBlockBuilderRef")
class IAppBlockBuilderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AppBlockBuilder.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appBlockBuilderRef")
    def app_block_builder_ref(self) -> "AppBlockBuilderReference":
        '''(experimental) A reference to a AppBlockBuilder resource.

        :stability: experimental
        '''
        ...


class _IAppBlockBuilderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AppBlockBuilder.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IAppBlockBuilderRef"

    @builtins.property
    @jsii.member(jsii_name="appBlockBuilderRef")
    def app_block_builder_ref(self) -> "AppBlockBuilderReference":
        '''(experimental) A reference to a AppBlockBuilder resource.

        :stability: experimental
        '''
        return typing.cast("AppBlockBuilderReference", jsii.get(self, "appBlockBuilderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppBlockBuilderRef).__jsii_proxy_class__ = lambda : _IAppBlockBuilderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appstream.IAppBlockRef")
class IAppBlockRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AppBlock.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appBlockRef")
    def app_block_ref(self) -> "AppBlockReference":
        '''(experimental) A reference to a AppBlock resource.

        :stability: experimental
        '''
        ...


class _IAppBlockRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AppBlock.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IAppBlockRef"

    @builtins.property
    @jsii.member(jsii_name="appBlockRef")
    def app_block_ref(self) -> "AppBlockReference":
        '''(experimental) A reference to a AppBlock resource.

        :stability: experimental
        '''
        return typing.cast("AppBlockReference", jsii.get(self, "appBlockRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppBlockRef).__jsii_proxy_class__ = lambda : _IAppBlockRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.IApplicationEntitlementAssociationRef"
)
class IApplicationEntitlementAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationEntitlementAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationEntitlementAssociationRef")
    def application_entitlement_association_ref(
        self,
    ) -> "ApplicationEntitlementAssociationReference":
        '''(experimental) A reference to a ApplicationEntitlementAssociation resource.

        :stability: experimental
        '''
        ...


class _IApplicationEntitlementAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationEntitlementAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IApplicationEntitlementAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationEntitlementAssociationRef")
    def application_entitlement_association_ref(
        self,
    ) -> "ApplicationEntitlementAssociationReference":
        '''(experimental) A reference to a ApplicationEntitlementAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationEntitlementAssociationReference", jsii.get(self, "applicationEntitlementAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationEntitlementAssociationRef).__jsii_proxy_class__ = lambda : _IApplicationEntitlementAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.IApplicationFleetAssociationRef"
)
class IApplicationFleetAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationFleetAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationFleetAssociationRef")
    def application_fleet_association_ref(
        self,
    ) -> "ApplicationFleetAssociationReference":
        '''(experimental) A reference to a ApplicationFleetAssociation resource.

        :stability: experimental
        '''
        ...


class _IApplicationFleetAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationFleetAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IApplicationFleetAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationFleetAssociationRef")
    def application_fleet_association_ref(
        self,
    ) -> "ApplicationFleetAssociationReference":
        '''(experimental) A reference to a ApplicationFleetAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationFleetAssociationReference", jsii.get(self, "applicationFleetAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationFleetAssociationRef).__jsii_proxy_class__ = lambda : _IApplicationFleetAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appstream.IApplicationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appstream.IDirectoryConfigRef")
class IDirectoryConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DirectoryConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="directoryConfigRef")
    def directory_config_ref(self) -> "DirectoryConfigReference":
        '''(experimental) A reference to a DirectoryConfig resource.

        :stability: experimental
        '''
        ...


class _IDirectoryConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DirectoryConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IDirectoryConfigRef"

    @builtins.property
    @jsii.member(jsii_name="directoryConfigRef")
    def directory_config_ref(self) -> "DirectoryConfigReference":
        '''(experimental) A reference to a DirectoryConfig resource.

        :stability: experimental
        '''
        return typing.cast("DirectoryConfigReference", jsii.get(self, "directoryConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDirectoryConfigRef).__jsii_proxy_class__ = lambda : _IDirectoryConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appstream.IEntitlementRef")
class IEntitlementRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Entitlement.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="entitlementRef")
    def entitlement_ref(self) -> "EntitlementReference":
        '''(experimental) A reference to a Entitlement resource.

        :stability: experimental
        '''
        ...


class _IEntitlementRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Entitlement.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IEntitlementRef"

    @builtins.property
    @jsii.member(jsii_name="entitlementRef")
    def entitlement_ref(self) -> "EntitlementReference":
        '''(experimental) A reference to a Entitlement resource.

        :stability: experimental
        '''
        return typing.cast("EntitlementReference", jsii.get(self, "entitlementRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEntitlementRef).__jsii_proxy_class__ = lambda : _IEntitlementRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appstream.IFleetRef")
class IFleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        ...


class _IFleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IFleetRef"

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        return typing.cast("FleetReference", jsii.get(self, "fleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFleetRef).__jsii_proxy_class__ = lambda : _IFleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appstream.IImageBuilderRef")
class IImageBuilderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ImageBuilder.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="imageBuilderRef")
    def image_builder_ref(self) -> "ImageBuilderReference":
        '''(experimental) A reference to a ImageBuilder resource.

        :stability: experimental
        '''
        ...


class _IImageBuilderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ImageBuilder.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IImageBuilderRef"

    @builtins.property
    @jsii.member(jsii_name="imageBuilderRef")
    def image_builder_ref(self) -> "ImageBuilderReference":
        '''(experimental) A reference to a ImageBuilder resource.

        :stability: experimental
        '''
        return typing.cast("ImageBuilderReference", jsii.get(self, "imageBuilderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IImageBuilderRef).__jsii_proxy_class__ = lambda : _IImageBuilderRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.IStackFleetAssociationRef"
)
class IStackFleetAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StackFleetAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stackFleetAssociationRef")
    def stack_fleet_association_ref(self) -> "StackFleetAssociationReference":
        '''(experimental) A reference to a StackFleetAssociation resource.

        :stability: experimental
        '''
        ...


class _IStackFleetAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StackFleetAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IStackFleetAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="stackFleetAssociationRef")
    def stack_fleet_association_ref(self) -> "StackFleetAssociationReference":
        '''(experimental) A reference to a StackFleetAssociation resource.

        :stability: experimental
        '''
        return typing.cast("StackFleetAssociationReference", jsii.get(self, "stackFleetAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackFleetAssociationRef).__jsii_proxy_class__ = lambda : _IStackFleetAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appstream.IStackRef")
class IStackRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Stack.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stackRef")
    def stack_ref(self) -> "StackReference":
        '''(experimental) A reference to a Stack resource.

        :stability: experimental
        '''
        ...


class _IStackRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Stack.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IStackRef"

    @builtins.property
    @jsii.member(jsii_name="stackRef")
    def stack_ref(self) -> "StackReference":
        '''(experimental) A reference to a Stack resource.

        :stability: experimental
        '''
        return typing.cast("StackReference", jsii.get(self, "stackRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackRef).__jsii_proxy_class__ = lambda : _IStackRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.IStackUserAssociationRef"
)
class IStackUserAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StackUserAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stackUserAssociationRef")
    def stack_user_association_ref(self) -> "StackUserAssociationReference":
        '''(experimental) A reference to a StackUserAssociation resource.

        :stability: experimental
        '''
        ...


class _IStackUserAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StackUserAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IStackUserAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="stackUserAssociationRef")
    def stack_user_association_ref(self) -> "StackUserAssociationReference":
        '''(experimental) A reference to a StackUserAssociation resource.

        :stability: experimental
        '''
        return typing.cast("StackUserAssociationReference", jsii.get(self, "stackUserAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackUserAssociationRef).__jsii_proxy_class__ = lambda : _IStackUserAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appstream.IUserRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appstream.IUserRef"

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "UserReference":
        '''(experimental) A reference to a User resource.

        :stability: experimental
        '''
        return typing.cast("UserReference", jsii.get(self, "userRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserRef).__jsii_proxy_class__ = lambda : _IUserRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.ImageBuilderReference",
    jsii_struct_bases=[],
    name_mapping={"image_builder_name": "imageBuilderName"},
)
class ImageBuilderReference:
    def __init__(self, *, image_builder_name: builtins.str) -> None:
        '''A reference to a ImageBuilder resource.

        :param image_builder_name: The Name of the ImageBuilder resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            image_builder_reference = interfaces_appstream.ImageBuilderReference(
                image_builder_name="imageBuilderName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd8c28dc257befffc80371dd057b43178b4a6070998fd325b2917af4c7b13dd)
            check_type(argname="argument image_builder_name", value=image_builder_name, expected_type=type_hints["image_builder_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "image_builder_name": image_builder_name,
        }

    @builtins.property
    def image_builder_name(self) -> builtins.str:
        '''The Name of the ImageBuilder resource.'''
        result = self._values.get("image_builder_name")
        assert result is not None, "Required property 'image_builder_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ImageBuilderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.StackFleetAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"stack_fleet_association_id": "stackFleetAssociationId"},
)
class StackFleetAssociationReference:
    def __init__(self, *, stack_fleet_association_id: builtins.str) -> None:
        '''A reference to a StackFleetAssociation resource.

        :param stack_fleet_association_id: The Id of the StackFleetAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            stack_fleet_association_reference = interfaces_appstream.StackFleetAssociationReference(
                stack_fleet_association_id="stackFleetAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75af852a1fd8c23c7edb9bd59224cb6cbb18155271a51d4cad9dbd81f024f528)
            check_type(argname="argument stack_fleet_association_id", value=stack_fleet_association_id, expected_type=type_hints["stack_fleet_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stack_fleet_association_id": stack_fleet_association_id,
        }

    @builtins.property
    def stack_fleet_association_id(self) -> builtins.str:
        '''The Id of the StackFleetAssociation resource.'''
        result = self._values.get("stack_fleet_association_id")
        assert result is not None, "Required property 'stack_fleet_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackFleetAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.StackReference",
    jsii_struct_bases=[],
    name_mapping={"stack_id": "stackId"},
)
class StackReference:
    def __init__(self, *, stack_id: builtins.str) -> None:
        '''A reference to a Stack resource.

        :param stack_id: The Id of the Stack resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            stack_reference = interfaces_appstream.StackReference(
                stack_id="stackId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18e2db2f88ee8958e1ce93ecd8dee4f9694f7bd4fd83892ea90f8bae81bdabfb)
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stack_id": stack_id,
        }

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''The Id of the Stack resource.'''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.StackUserAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"stack_user_association_id": "stackUserAssociationId"},
)
class StackUserAssociationReference:
    def __init__(self, *, stack_user_association_id: builtins.str) -> None:
        '''A reference to a StackUserAssociation resource.

        :param stack_user_association_id: The Id of the StackUserAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            stack_user_association_reference = interfaces_appstream.StackUserAssociationReference(
                stack_user_association_id="stackUserAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2130170f8c1e17f1e893b413b87fa336531a5bfd65795c1f55dd180b4c23cb2)
            check_type(argname="argument stack_user_association_id", value=stack_user_association_id, expected_type=type_hints["stack_user_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stack_user_association_id": stack_user_association_id,
        }

    @builtins.property
    def stack_user_association_id(self) -> builtins.str:
        '''The Id of the StackUserAssociation resource.'''
        result = self._values.get("stack_user_association_id")
        assert result is not None, "Required property 'stack_user_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackUserAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appstream.UserReference",
    jsii_struct_bases=[],
    name_mapping={"user_id": "userId"},
)
class UserReference:
    def __init__(self, *, user_id: builtins.str) -> None:
        '''A reference to a User resource.

        :param user_id: The Id of the User resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appstream as interfaces_appstream
            
            user_reference = interfaces_appstream.UserReference(
                user_id="userId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ebf6320aef40f4a25ef1a995b2ab69386c3f385461a0216574eee343afd525e)
            check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_id": user_id,
        }

    @builtins.property
    def user_id(self) -> builtins.str:
        '''The Id of the User resource.'''
        result = self._values.get("user_id")
        assert result is not None, "Required property 'user_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AppBlockBuilderReference",
    "AppBlockReference",
    "ApplicationEntitlementAssociationReference",
    "ApplicationFleetAssociationReference",
    "ApplicationReference",
    "DirectoryConfigReference",
    "EntitlementReference",
    "FleetReference",
    "IAppBlockBuilderRef",
    "IAppBlockRef",
    "IApplicationEntitlementAssociationRef",
    "IApplicationFleetAssociationRef",
    "IApplicationRef",
    "IDirectoryConfigRef",
    "IEntitlementRef",
    "IFleetRef",
    "IImageBuilderRef",
    "IStackFleetAssociationRef",
    "IStackRef",
    "IStackUserAssociationRef",
    "IUserRef",
    "ImageBuilderReference",
    "StackFleetAssociationReference",
    "StackReference",
    "StackUserAssociationReference",
    "UserReference",
]

publication.publish()

def _typecheckingstub__3ccf44c8df86ddb2aaa3dd1c1344df0034b12c7bbaed1ab37b6250d970e02b0f(
    *,
    app_block_builder_arn: builtins.str,
    app_block_builder_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__999361d2192091ecfd78bba01c6482ad6b51ef4092d3d6e058fcf3faa9dbd0e2(
    *,
    app_block_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed86ac6d622d5886a019c6a70ccba7b459759e3530109ee3fcb194657d268885(
    *,
    application_identifier: builtins.str,
    entitlement_name: builtins.str,
    stack_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__769a3917223ace7abfe471cf26313b453db8d1524a1dbbc471df0cb4285f6e51(
    *,
    application_arn: builtins.str,
    fleet_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e27f24e60cc84ecd4863218985a438ab83cddfd32614837a12eaccaef5b26d(
    *,
    application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0769cbea8784800cc76f29c4da14a24e3f6a31b7b69f3317cd404dd3dc7e2c51(
    *,
    directory_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5da2f4531a553fc09946f90e2f23bdd0a0a94f048a8afd6773a3cee741fdb4db(
    *,
    entitlement_name: builtins.str,
    stack_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ff6eedaec7cca9f61d584878f912a02aa3f25654ba401a7b5a184b2cbc6dd3e(
    *,
    fleet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd8c28dc257befffc80371dd057b43178b4a6070998fd325b2917af4c7b13dd(
    *,
    image_builder_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75af852a1fd8c23c7edb9bd59224cb6cbb18155271a51d4cad9dbd81f024f528(
    *,
    stack_fleet_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18e2db2f88ee8958e1ce93ecd8dee4f9694f7bd4fd83892ea90f8bae81bdabfb(
    *,
    stack_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2130170f8c1e17f1e893b413b87fa336531a5bfd65795c1f55dd180b4c23cb2(
    *,
    stack_user_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ebf6320aef40f4a25ef1a995b2ab69386c3f385461a0216574eee343afd525e(
    *,
    user_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAppBlockBuilderRef, IAppBlockRef, IApplicationEntitlementAssociationRef, IApplicationFleetAssociationRef, IApplicationRef, IDirectoryConfigRef, IEntitlementRef, IFleetRef, IImageBuilderRef, IStackFleetAssociationRef, IStackRef, IStackUserAssociationRef, IUserRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
