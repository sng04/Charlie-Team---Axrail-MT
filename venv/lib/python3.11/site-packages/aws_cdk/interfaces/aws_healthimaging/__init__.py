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
    jsii_type="aws-cdk-lib.interfaces.aws_healthimaging.DatastoreReference",
    jsii_struct_bases=[],
    name_mapping={"datastore_arn": "datastoreArn", "datastore_id": "datastoreId"},
)
class DatastoreReference:
    def __init__(
        self,
        *,
        datastore_arn: builtins.str,
        datastore_id: builtins.str,
    ) -> None:
        '''A reference to a Datastore resource.

        :param datastore_arn: The ARN of the Datastore resource.
        :param datastore_id: The DatastoreId of the Datastore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_healthimaging as interfaces_healthimaging
            
            datastore_reference = interfaces_healthimaging.DatastoreReference(
                datastore_arn="datastoreArn",
                datastore_id="datastoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfda41d9ee176f23cccd12bd1d3be1ff1670433008bc6d47528cf86507fcc346)
            check_type(argname="argument datastore_arn", value=datastore_arn, expected_type=type_hints["datastore_arn"])
            check_type(argname="argument datastore_id", value=datastore_id, expected_type=type_hints["datastore_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datastore_arn": datastore_arn,
            "datastore_id": datastore_id,
        }

    @builtins.property
    def datastore_arn(self) -> builtins.str:
        '''The ARN of the Datastore resource.'''
        result = self._values.get("datastore_arn")
        assert result is not None, "Required property 'datastore_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datastore_id(self) -> builtins.str:
        '''The DatastoreId of the Datastore resource.'''
        result = self._values.get("datastore_id")
        assert result is not None, "Required property 'datastore_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatastoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_healthimaging.IDatastoreRef")
class IDatastoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Datastore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="datastoreRef")
    def datastore_ref(self) -> "DatastoreReference":
        '''(experimental) A reference to a Datastore resource.

        :stability: experimental
        '''
        ...


class _IDatastoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Datastore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_healthimaging.IDatastoreRef"

    @builtins.property
    @jsii.member(jsii_name="datastoreRef")
    def datastore_ref(self) -> "DatastoreReference":
        '''(experimental) A reference to a Datastore resource.

        :stability: experimental
        '''
        return typing.cast("DatastoreReference", jsii.get(self, "datastoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatastoreRef).__jsii_proxy_class__ = lambda : _IDatastoreRefProxy


__all__ = [
    "DatastoreReference",
    "IDatastoreRef",
]

publication.publish()

def _typecheckingstub__dfda41d9ee176f23cccd12bd1d3be1ff1670433008bc6d47528cf86507fcc346(
    *,
    datastore_arn: builtins.str,
    datastore_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDatastoreRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
