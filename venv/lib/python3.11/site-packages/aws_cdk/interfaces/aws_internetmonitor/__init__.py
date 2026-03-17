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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_internetmonitor.IMonitorRef")
class IMonitorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Monitor.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="monitorRef")
    def monitor_ref(self) -> "MonitorReference":
        '''(experimental) A reference to a Monitor resource.

        :stability: experimental
        '''
        ...


class _IMonitorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Monitor.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_internetmonitor.IMonitorRef"

    @builtins.property
    @jsii.member(jsii_name="monitorRef")
    def monitor_ref(self) -> "MonitorReference":
        '''(experimental) A reference to a Monitor resource.

        :stability: experimental
        '''
        return typing.cast("MonitorReference", jsii.get(self, "monitorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMonitorRef).__jsii_proxy_class__ = lambda : _IMonitorRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_internetmonitor.MonitorReference",
    jsii_struct_bases=[],
    name_mapping={"monitor_arn": "monitorArn", "monitor_name": "monitorName"},
)
class MonitorReference:
    def __init__(
        self,
        *,
        monitor_arn: builtins.str,
        monitor_name: builtins.str,
    ) -> None:
        '''A reference to a Monitor resource.

        :param monitor_arn: The ARN of the Monitor resource.
        :param monitor_name: The MonitorName of the Monitor resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_internetmonitor as interfaces_internetmonitor
            
            monitor_reference = interfaces_internetmonitor.MonitorReference(
                monitor_arn="monitorArn",
                monitor_name="monitorName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbdaa71e5fd9cce7a1afa634e13de5c8d5dc17aa3c35f56537a68c1e4f6c7315)
            check_type(argname="argument monitor_arn", value=monitor_arn, expected_type=type_hints["monitor_arn"])
            check_type(argname="argument monitor_name", value=monitor_name, expected_type=type_hints["monitor_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitor_arn": monitor_arn,
            "monitor_name": monitor_name,
        }

    @builtins.property
    def monitor_arn(self) -> builtins.str:
        '''The ARN of the Monitor resource.'''
        result = self._values.get("monitor_arn")
        assert result is not None, "Required property 'monitor_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def monitor_name(self) -> builtins.str:
        '''The MonitorName of the Monitor resource.'''
        result = self._values.get("monitor_name")
        assert result is not None, "Required property 'monitor_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IMonitorRef",
    "MonitorReference",
]

publication.publish()

def _typecheckingstub__dbdaa71e5fd9cce7a1afa634e13de5c8d5dc17aa3c35f56537a68c1e4f6c7315(
    *,
    monitor_arn: builtins.str,
    monitor_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IMonitorRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
