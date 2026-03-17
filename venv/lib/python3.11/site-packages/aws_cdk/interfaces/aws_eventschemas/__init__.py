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
    jsii_type="aws-cdk-lib.interfaces.aws_eventschemas.DiscovererReference",
    jsii_struct_bases=[],
    name_mapping={"discoverer_arn": "discovererArn"},
)
class DiscovererReference:
    def __init__(self, *, discoverer_arn: builtins.str) -> None:
        '''A reference to a Discoverer resource.

        :param discoverer_arn: The DiscovererArn of the Discoverer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eventschemas as interfaces_eventschemas
            
            discoverer_reference = interfaces_eventschemas.DiscovererReference(
                discoverer_arn="discovererArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef5f0f98b996f76f680660442586169116e286a17380f815a5a3a375677f9663)
            check_type(argname="argument discoverer_arn", value=discoverer_arn, expected_type=type_hints["discoverer_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "discoverer_arn": discoverer_arn,
        }

    @builtins.property
    def discoverer_arn(self) -> builtins.str:
        '''The DiscovererArn of the Discoverer resource.'''
        result = self._values.get("discoverer_arn")
        assert result is not None, "Required property 'discoverer_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiscovererReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eventschemas.IDiscovererRef")
class IDiscovererRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Discoverer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="discovererRef")
    def discoverer_ref(self) -> "DiscovererReference":
        '''(experimental) A reference to a Discoverer resource.

        :stability: experimental
        '''
        ...


class _IDiscovererRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Discoverer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eventschemas.IDiscovererRef"

    @builtins.property
    @jsii.member(jsii_name="discovererRef")
    def discoverer_ref(self) -> "DiscovererReference":
        '''(experimental) A reference to a Discoverer resource.

        :stability: experimental
        '''
        return typing.cast("DiscovererReference", jsii.get(self, "discovererRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDiscovererRef).__jsii_proxy_class__ = lambda : _IDiscovererRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eventschemas.IRegistryPolicyRef")
class IRegistryPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RegistryPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="registryPolicyRef")
    def registry_policy_ref(self) -> "RegistryPolicyReference":
        '''(experimental) A reference to a RegistryPolicy resource.

        :stability: experimental
        '''
        ...


class _IRegistryPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RegistryPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eventschemas.IRegistryPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="registryPolicyRef")
    def registry_policy_ref(self) -> "RegistryPolicyReference":
        '''(experimental) A reference to a RegistryPolicy resource.

        :stability: experimental
        '''
        return typing.cast("RegistryPolicyReference", jsii.get(self, "registryPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegistryPolicyRef).__jsii_proxy_class__ = lambda : _IRegistryPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eventschemas.IRegistryRef")
class IRegistryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Registry.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="registryRef")
    def registry_ref(self) -> "RegistryReference":
        '''(experimental) A reference to a Registry resource.

        :stability: experimental
        '''
        ...


class _IRegistryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Registry.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eventschemas.IRegistryRef"

    @builtins.property
    @jsii.member(jsii_name="registryRef")
    def registry_ref(self) -> "RegistryReference":
        '''(experimental) A reference to a Registry resource.

        :stability: experimental
        '''
        return typing.cast("RegistryReference", jsii.get(self, "registryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegistryRef).__jsii_proxy_class__ = lambda : _IRegistryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_eventschemas.ISchemaRef")
class ISchemaRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        ...


class _ISchemaRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_eventschemas.ISchemaRef"

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        return typing.cast("SchemaReference", jsii.get(self, "schemaRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaRef).__jsii_proxy_class__ = lambda : _ISchemaRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eventschemas.RegistryPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"registry_name": "registryName"},
)
class RegistryPolicyReference:
    def __init__(self, *, registry_name: builtins.str) -> None:
        '''A reference to a RegistryPolicy resource.

        :param registry_name: The RegistryName of the RegistryPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eventschemas as interfaces_eventschemas
            
            registry_policy_reference = interfaces_eventschemas.RegistryPolicyReference(
                registry_name="registryName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01fcbf08dbbccfe46b4a7e85e067411892483d560177fa9bf861e4ebad973d4f)
            check_type(argname="argument registry_name", value=registry_name, expected_type=type_hints["registry_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_name": registry_name,
        }

    @builtins.property
    def registry_name(self) -> builtins.str:
        '''The RegistryName of the RegistryPolicy resource.'''
        result = self._values.get("registry_name")
        assert result is not None, "Required property 'registry_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eventschemas.RegistryReference",
    jsii_struct_bases=[],
    name_mapping={"registry_arn": "registryArn"},
)
class RegistryReference:
    def __init__(self, *, registry_arn: builtins.str) -> None:
        '''A reference to a Registry resource.

        :param registry_arn: The RegistryArn of the Registry resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eventschemas as interfaces_eventschemas
            
            registry_reference = interfaces_eventschemas.RegistryReference(
                registry_arn="registryArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01e880fdfd7d0c7f26d51f4a7dc0cd40ff62bb642c691cf2445e7aac801a61d8)
            check_type(argname="argument registry_arn", value=registry_arn, expected_type=type_hints["registry_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_arn": registry_arn,
        }

    @builtins.property
    def registry_arn(self) -> builtins.str:
        '''The RegistryArn of the Registry resource.'''
        result = self._values.get("registry_arn")
        assert result is not None, "Required property 'registry_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_eventschemas.SchemaReference",
    jsii_struct_bases=[],
    name_mapping={"schema_arn": "schemaArn"},
)
class SchemaReference:
    def __init__(self, *, schema_arn: builtins.str) -> None:
        '''A reference to a Schema resource.

        :param schema_arn: The SchemaArn of the Schema resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_eventschemas as interfaces_eventschemas
            
            schema_reference = interfaces_eventschemas.SchemaReference(
                schema_arn="schemaArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfe16a515e744eec76e1c363fb01a802b2701313bee77a5afbaa550836fb82f3)
            check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_arn": schema_arn,
        }

    @builtins.property
    def schema_arn(self) -> builtins.str:
        '''The SchemaArn of the Schema resource.'''
        result = self._values.get("schema_arn")
        assert result is not None, "Required property 'schema_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DiscovererReference",
    "IDiscovererRef",
    "IRegistryPolicyRef",
    "IRegistryRef",
    "ISchemaRef",
    "RegistryPolicyReference",
    "RegistryReference",
    "SchemaReference",
]

publication.publish()

def _typecheckingstub__ef5f0f98b996f76f680660442586169116e286a17380f815a5a3a375677f9663(
    *,
    discoverer_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01fcbf08dbbccfe46b4a7e85e067411892483d560177fa9bf861e4ebad973d4f(
    *,
    registry_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01e880fdfd7d0c7f26d51f4a7dc0cd40ff62bb642c691cf2445e7aac801a61d8(
    *,
    registry_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfe16a515e744eec76e1c363fb01a802b2701313bee77a5afbaa550836fb82f3(
    *,
    schema_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDiscovererRef, IRegistryPolicyRef, IRegistryRef, ISchemaRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
