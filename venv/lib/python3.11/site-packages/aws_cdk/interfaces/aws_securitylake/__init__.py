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
    jsii_type="aws-cdk-lib.interfaces.aws_securitylake.AwsLogSourceReference",
    jsii_struct_bases=[],
    name_mapping={"source_name": "sourceName", "source_version": "sourceVersion"},
)
class AwsLogSourceReference:
    def __init__(
        self,
        *,
        source_name: builtins.str,
        source_version: builtins.str,
    ) -> None:
        '''A reference to a AwsLogSource resource.

        :param source_name: The SourceName of the AwsLogSource resource.
        :param source_version: The SourceVersion of the AwsLogSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securitylake as interfaces_securitylake
            
            aws_log_source_reference = interfaces_securitylake.AwsLogSourceReference(
                source_name="sourceName",
                source_version="sourceVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1400264d7b65d0f09b4e71ee0568106ff533e33049fdc7a3e8f5609544b16fee)
            check_type(argname="argument source_name", value=source_name, expected_type=type_hints["source_name"])
            check_type(argname="argument source_version", value=source_version, expected_type=type_hints["source_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_name": source_name,
            "source_version": source_version,
        }

    @builtins.property
    def source_name(self) -> builtins.str:
        '''The SourceName of the AwsLogSource resource.'''
        result = self._values.get("source_name")
        assert result is not None, "Required property 'source_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_version(self) -> builtins.str:
        '''The SourceVersion of the AwsLogSource resource.'''
        result = self._values.get("source_version")
        assert result is not None, "Required property 'source_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsLogSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securitylake.DataLakeReference",
    jsii_struct_bases=[],
    name_mapping={"data_lake_arn": "dataLakeArn"},
)
class DataLakeReference:
    def __init__(self, *, data_lake_arn: builtins.str) -> None:
        '''A reference to a DataLake resource.

        :param data_lake_arn: The Arn of the DataLake resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securitylake as interfaces_securitylake
            
            data_lake_reference = interfaces_securitylake.DataLakeReference(
                data_lake_arn="dataLakeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05506121f92ba81a85ad1a4f98ae21ba572c13637d74188809bfd6b68a8879fc)
            check_type(argname="argument data_lake_arn", value=data_lake_arn, expected_type=type_hints["data_lake_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_lake_arn": data_lake_arn,
        }

    @builtins.property
    def data_lake_arn(self) -> builtins.str:
        '''The Arn of the DataLake resource.'''
        result = self._values.get("data_lake_arn")
        assert result is not None, "Required property 'data_lake_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securitylake.IAwsLogSourceRef")
class IAwsLogSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AwsLogSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="awsLogSourceRef")
    def aws_log_source_ref(self) -> "AwsLogSourceReference":
        '''(experimental) A reference to a AwsLogSource resource.

        :stability: experimental
        '''
        ...


class _IAwsLogSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AwsLogSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securitylake.IAwsLogSourceRef"

    @builtins.property
    @jsii.member(jsii_name="awsLogSourceRef")
    def aws_log_source_ref(self) -> "AwsLogSourceReference":
        '''(experimental) A reference to a AwsLogSource resource.

        :stability: experimental
        '''
        return typing.cast("AwsLogSourceReference", jsii.get(self, "awsLogSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAwsLogSourceRef).__jsii_proxy_class__ = lambda : _IAwsLogSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securitylake.IDataLakeRef")
class IDataLakeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataLake.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataLakeRef")
    def data_lake_ref(self) -> "DataLakeReference":
        '''(experimental) A reference to a DataLake resource.

        :stability: experimental
        '''
        ...


class _IDataLakeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataLake.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securitylake.IDataLakeRef"

    @builtins.property
    @jsii.member(jsii_name="dataLakeRef")
    def data_lake_ref(self) -> "DataLakeReference":
        '''(experimental) A reference to a DataLake resource.

        :stability: experimental
        '''
        return typing.cast("DataLakeReference", jsii.get(self, "dataLakeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataLakeRef).__jsii_proxy_class__ = lambda : _IDataLakeRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_securitylake.ISubscriberNotificationRef"
)
class ISubscriberNotificationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriberNotification.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subscriberNotificationRef")
    def subscriber_notification_ref(self) -> "SubscriberNotificationReference":
        '''(experimental) A reference to a SubscriberNotification resource.

        :stability: experimental
        '''
        ...


class _ISubscriberNotificationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriberNotification.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securitylake.ISubscriberNotificationRef"

    @builtins.property
    @jsii.member(jsii_name="subscriberNotificationRef")
    def subscriber_notification_ref(self) -> "SubscriberNotificationReference":
        '''(experimental) A reference to a SubscriberNotification resource.

        :stability: experimental
        '''
        return typing.cast("SubscriberNotificationReference", jsii.get(self, "subscriberNotificationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubscriberNotificationRef).__jsii_proxy_class__ = lambda : _ISubscriberNotificationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securitylake.ISubscriberRef")
class ISubscriberRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Subscriber.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subscriberRef")
    def subscriber_ref(self) -> "SubscriberReference":
        '''(experimental) A reference to a Subscriber resource.

        :stability: experimental
        '''
        ...


class _ISubscriberRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Subscriber.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securitylake.ISubscriberRef"

    @builtins.property
    @jsii.member(jsii_name="subscriberRef")
    def subscriber_ref(self) -> "SubscriberReference":
        '''(experimental) A reference to a Subscriber resource.

        :stability: experimental
        '''
        return typing.cast("SubscriberReference", jsii.get(self, "subscriberRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubscriberRef).__jsii_proxy_class__ = lambda : _ISubscriberRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securitylake.SubscriberNotificationReference",
    jsii_struct_bases=[],
    name_mapping={"subscriber_arn": "subscriberArn"},
)
class SubscriberNotificationReference:
    def __init__(self, *, subscriber_arn: builtins.str) -> None:
        '''A reference to a SubscriberNotification resource.

        :param subscriber_arn: The SubscriberArn of the SubscriberNotification resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securitylake as interfaces_securitylake
            
            subscriber_notification_reference = interfaces_securitylake.SubscriberNotificationReference(
                subscriber_arn="subscriberArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31232187ee4c0f248cbe10f5a9af57504b391973bd54bed246386f75669c3c4e)
            check_type(argname="argument subscriber_arn", value=subscriber_arn, expected_type=type_hints["subscriber_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscriber_arn": subscriber_arn,
        }

    @builtins.property
    def subscriber_arn(self) -> builtins.str:
        '''The SubscriberArn of the SubscriberNotification resource.'''
        result = self._values.get("subscriber_arn")
        assert result is not None, "Required property 'subscriber_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriberNotificationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securitylake.SubscriberReference",
    jsii_struct_bases=[],
    name_mapping={"subscriber_arn": "subscriberArn"},
)
class SubscriberReference:
    def __init__(self, *, subscriber_arn: builtins.str) -> None:
        '''A reference to a Subscriber resource.

        :param subscriber_arn: The SubscriberArn of the Subscriber resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securitylake as interfaces_securitylake
            
            subscriber_reference = interfaces_securitylake.SubscriberReference(
                subscriber_arn="subscriberArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fafcdb804bbd83bec7d9b6f23eb86184c7e57df80dc96235abceadd473640c23)
            check_type(argname="argument subscriber_arn", value=subscriber_arn, expected_type=type_hints["subscriber_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscriber_arn": subscriber_arn,
        }

    @builtins.property
    def subscriber_arn(self) -> builtins.str:
        '''The SubscriberArn of the Subscriber resource.'''
        result = self._values.get("subscriber_arn")
        assert result is not None, "Required property 'subscriber_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriberReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsLogSourceReference",
    "DataLakeReference",
    "IAwsLogSourceRef",
    "IDataLakeRef",
    "ISubscriberNotificationRef",
    "ISubscriberRef",
    "SubscriberNotificationReference",
    "SubscriberReference",
]

publication.publish()

def _typecheckingstub__1400264d7b65d0f09b4e71ee0568106ff533e33049fdc7a3e8f5609544b16fee(
    *,
    source_name: builtins.str,
    source_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05506121f92ba81a85ad1a4f98ae21ba572c13637d74188809bfd6b68a8879fc(
    *,
    data_lake_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31232187ee4c0f248cbe10f5a9af57504b391973bd54bed246386f75669c3c4e(
    *,
    subscriber_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fafcdb804bbd83bec7d9b6f23eb86184c7e57df80dc96235abceadd473640c23(
    *,
    subscriber_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAwsLogSourceRef, IDataLakeRef, ISubscriberNotificationRef, ISubscriberRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
