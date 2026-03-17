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
    jsii_type="aws-cdk-lib.interfaces.aws_logs.AccountPolicyReference",
    jsii_struct_bases=[],
    name_mapping={
        "account_id": "accountId",
        "policy_name": "policyName",
        "policy_type": "policyType",
    },
)
class AccountPolicyReference:
    def __init__(
        self,
        *,
        account_id: builtins.str,
        policy_name: builtins.str,
        policy_type: builtins.str,
    ) -> None:
        '''A reference to a AccountPolicy resource.

        :param account_id: The AccountId of the AccountPolicy resource.
        :param policy_name: The PolicyName of the AccountPolicy resource.
        :param policy_type: The PolicyType of the AccountPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            account_policy_reference = interfaces_logs.AccountPolicyReference(
                account_id="accountId",
                policy_name="policyName",
                policy_type="policyType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e5d30d368dae32e7214dde7327399c249fc454b70c0d414b73a731d6b3b975a)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "policy_name": policy_name,
            "policy_type": policy_type,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the AccountPolicy resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The PolicyName of the AccountPolicy resource.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_type(self) -> builtins.str:
        '''The PolicyType of the AccountPolicy resource.'''
        result = self._values.get("policy_type")
        assert result is not None, "Required property 'policy_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.DeliveryDestinationReference",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_destination_arn": "deliveryDestinationArn",
        "delivery_destination_name": "deliveryDestinationName",
    },
)
class DeliveryDestinationReference:
    def __init__(
        self,
        *,
        delivery_destination_arn: builtins.str,
        delivery_destination_name: builtins.str,
    ) -> None:
        '''A reference to a DeliveryDestination resource.

        :param delivery_destination_arn: The ARN of the DeliveryDestination resource.
        :param delivery_destination_name: The Name of the DeliveryDestination resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            delivery_destination_reference = interfaces_logs.DeliveryDestinationReference(
                delivery_destination_arn="deliveryDestinationArn",
                delivery_destination_name="deliveryDestinationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d77a1fb4ac2647cdfa788a3962d5ff897d9ba488f410dcac7efc4ea322da89c9)
            check_type(argname="argument delivery_destination_arn", value=delivery_destination_arn, expected_type=type_hints["delivery_destination_arn"])
            check_type(argname="argument delivery_destination_name", value=delivery_destination_name, expected_type=type_hints["delivery_destination_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_destination_arn": delivery_destination_arn,
            "delivery_destination_name": delivery_destination_name,
        }

    @builtins.property
    def delivery_destination_arn(self) -> builtins.str:
        '''The ARN of the DeliveryDestination resource.'''
        result = self._values.get("delivery_destination_arn")
        assert result is not None, "Required property 'delivery_destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_destination_name(self) -> builtins.str:
        '''The Name of the DeliveryDestination resource.'''
        result = self._values.get("delivery_destination_name")
        assert result is not None, "Required property 'delivery_destination_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeliveryDestinationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.DeliveryReference",
    jsii_struct_bases=[],
    name_mapping={"delivery_arn": "deliveryArn", "delivery_id": "deliveryId"},
)
class DeliveryReference:
    def __init__(
        self,
        *,
        delivery_arn: builtins.str,
        delivery_id: builtins.str,
    ) -> None:
        '''A reference to a Delivery resource.

        :param delivery_arn: The ARN of the Delivery resource.
        :param delivery_id: The DeliveryId of the Delivery resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            delivery_reference = interfaces_logs.DeliveryReference(
                delivery_arn="deliveryArn",
                delivery_id="deliveryId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__120822921746f4d35e3b0433d834a26219946042aca3813bab6a68930277875e)
            check_type(argname="argument delivery_arn", value=delivery_arn, expected_type=type_hints["delivery_arn"])
            check_type(argname="argument delivery_id", value=delivery_id, expected_type=type_hints["delivery_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_arn": delivery_arn,
            "delivery_id": delivery_id,
        }

    @builtins.property
    def delivery_arn(self) -> builtins.str:
        '''The ARN of the Delivery resource.'''
        result = self._values.get("delivery_arn")
        assert result is not None, "Required property 'delivery_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_id(self) -> builtins.str:
        '''The DeliveryId of the Delivery resource.'''
        result = self._values.get("delivery_id")
        assert result is not None, "Required property 'delivery_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeliveryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.DeliverySourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_source_arn": "deliverySourceArn",
        "delivery_source_name": "deliverySourceName",
    },
)
class DeliverySourceReference:
    def __init__(
        self,
        *,
        delivery_source_arn: builtins.str,
        delivery_source_name: builtins.str,
    ) -> None:
        '''A reference to a DeliverySource resource.

        :param delivery_source_arn: The ARN of the DeliverySource resource.
        :param delivery_source_name: The Name of the DeliverySource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            delivery_source_reference = interfaces_logs.DeliverySourceReference(
                delivery_source_arn="deliverySourceArn",
                delivery_source_name="deliverySourceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84496c584c12fa0a7abce78ecb2626aebff2ea2da1b8692bd28a3ea5be19b90)
            check_type(argname="argument delivery_source_arn", value=delivery_source_arn, expected_type=type_hints["delivery_source_arn"])
            check_type(argname="argument delivery_source_name", value=delivery_source_name, expected_type=type_hints["delivery_source_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_source_arn": delivery_source_arn,
            "delivery_source_name": delivery_source_name,
        }

    @builtins.property
    def delivery_source_arn(self) -> builtins.str:
        '''The ARN of the DeliverySource resource.'''
        result = self._values.get("delivery_source_arn")
        assert result is not None, "Required property 'delivery_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_source_name(self) -> builtins.str:
        '''The Name of the DeliverySource resource.'''
        result = self._values.get("delivery_source_name")
        assert result is not None, "Required property 'delivery_source_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeliverySourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.DestinationReference",
    jsii_struct_bases=[],
    name_mapping={
        "destination_arn": "destinationArn",
        "destination_name": "destinationName",
    },
)
class DestinationReference:
    def __init__(
        self,
        *,
        destination_arn: builtins.str,
        destination_name: builtins.str,
    ) -> None:
        '''A reference to a Destination resource.

        :param destination_arn: The ARN of the Destination resource.
        :param destination_name: The DestinationName of the Destination resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            destination_reference = interfaces_logs.DestinationReference(
                destination_arn="destinationArn",
                destination_name="destinationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8bc552d9e2cd9371b7b566d808d316d9592f3ce00dab981d5ff39de473ff8e1)
            check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            check_type(argname="argument destination_name", value=destination_name, expected_type=type_hints["destination_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_arn": destination_arn,
            "destination_name": destination_name,
        }

    @builtins.property
    def destination_arn(self) -> builtins.str:
        '''The ARN of the Destination resource.'''
        result = self._values.get("destination_arn")
        assert result is not None, "Required property 'destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_name(self) -> builtins.str:
        '''The DestinationName of the Destination resource.'''
        result = self._values.get("destination_name")
        assert result is not None, "Required property 'destination_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IAccountPolicyRef")
class IAccountPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccountPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accountPolicyRef")
    def account_policy_ref(self) -> "AccountPolicyReference":
        '''(experimental) A reference to a AccountPolicy resource.

        :stability: experimental
        '''
        ...


class _IAccountPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccountPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IAccountPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="accountPolicyRef")
    def account_policy_ref(self) -> "AccountPolicyReference":
        '''(experimental) A reference to a AccountPolicy resource.

        :stability: experimental
        '''
        return typing.cast("AccountPolicyReference", jsii.get(self, "accountPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccountPolicyRef).__jsii_proxy_class__ = lambda : _IAccountPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IDeliveryDestinationRef")
class IDeliveryDestinationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeliveryDestination.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deliveryDestinationRef")
    def delivery_destination_ref(self) -> "DeliveryDestinationReference":
        '''(experimental) A reference to a DeliveryDestination resource.

        :stability: experimental
        '''
        ...


class _IDeliveryDestinationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeliveryDestination.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IDeliveryDestinationRef"

    @builtins.property
    @jsii.member(jsii_name="deliveryDestinationRef")
    def delivery_destination_ref(self) -> "DeliveryDestinationReference":
        '''(experimental) A reference to a DeliveryDestination resource.

        :stability: experimental
        '''
        return typing.cast("DeliveryDestinationReference", jsii.get(self, "deliveryDestinationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeliveryDestinationRef).__jsii_proxy_class__ = lambda : _IDeliveryDestinationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IDeliveryRef")
class IDeliveryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Delivery.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deliveryRef")
    def delivery_ref(self) -> "DeliveryReference":
        '''(experimental) A reference to a Delivery resource.

        :stability: experimental
        '''
        ...


class _IDeliveryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Delivery.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IDeliveryRef"

    @builtins.property
    @jsii.member(jsii_name="deliveryRef")
    def delivery_ref(self) -> "DeliveryReference":
        '''(experimental) A reference to a Delivery resource.

        :stability: experimental
        '''
        return typing.cast("DeliveryReference", jsii.get(self, "deliveryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeliveryRef).__jsii_proxy_class__ = lambda : _IDeliveryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IDeliverySourceRef")
class IDeliverySourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeliverySource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deliverySourceRef")
    def delivery_source_ref(self) -> "DeliverySourceReference":
        '''(experimental) A reference to a DeliverySource resource.

        :stability: experimental
        '''
        ...


class _IDeliverySourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeliverySource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IDeliverySourceRef"

    @builtins.property
    @jsii.member(jsii_name="deliverySourceRef")
    def delivery_source_ref(self) -> "DeliverySourceReference":
        '''(experimental) A reference to a DeliverySource resource.

        :stability: experimental
        '''
        return typing.cast("DeliverySourceReference", jsii.get(self, "deliverySourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeliverySourceRef).__jsii_proxy_class__ = lambda : _IDeliverySourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IDestinationRef")
class IDestinationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Destination.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="destinationRef")
    def destination_ref(self) -> "DestinationReference":
        '''(experimental) A reference to a Destination resource.

        :stability: experimental
        '''
        ...


class _IDestinationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Destination.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IDestinationRef"

    @builtins.property
    @jsii.member(jsii_name="destinationRef")
    def destination_ref(self) -> "DestinationReference":
        '''(experimental) A reference to a Destination resource.

        :stability: experimental
        '''
        return typing.cast("DestinationReference", jsii.get(self, "destinationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDestinationRef).__jsii_proxy_class__ = lambda : _IDestinationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IIntegrationRef")
class IIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        ...


class _IIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationReference", jsii.get(self, "integrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationRef).__jsii_proxy_class__ = lambda : _IIntegrationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.ILogAnomalyDetectorRef")
class ILogAnomalyDetectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LogAnomalyDetector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="logAnomalyDetectorRef")
    def log_anomaly_detector_ref(self) -> "LogAnomalyDetectorReference":
        '''(experimental) A reference to a LogAnomalyDetector resource.

        :stability: experimental
        '''
        ...


class _ILogAnomalyDetectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LogAnomalyDetector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.ILogAnomalyDetectorRef"

    @builtins.property
    @jsii.member(jsii_name="logAnomalyDetectorRef")
    def log_anomaly_detector_ref(self) -> "LogAnomalyDetectorReference":
        '''(experimental) A reference to a LogAnomalyDetector resource.

        :stability: experimental
        '''
        return typing.cast("LogAnomalyDetectorReference", jsii.get(self, "logAnomalyDetectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogAnomalyDetectorRef).__jsii_proxy_class__ = lambda : _ILogAnomalyDetectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.ILogGroupRef")
class ILogGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LogGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="logGroupRef")
    def log_group_ref(self) -> "LogGroupReference":
        '''(experimental) A reference to a LogGroup resource.

        :stability: experimental
        '''
        ...


class _ILogGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LogGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.ILogGroupRef"

    @builtins.property
    @jsii.member(jsii_name="logGroupRef")
    def log_group_ref(self) -> "LogGroupReference":
        '''(experimental) A reference to a LogGroup resource.

        :stability: experimental
        '''
        return typing.cast("LogGroupReference", jsii.get(self, "logGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogGroupRef).__jsii_proxy_class__ = lambda : _ILogGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.ILogStreamRef")
class ILogStreamRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LogStream.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="logStreamRef")
    def log_stream_ref(self) -> "LogStreamReference":
        '''(experimental) A reference to a LogStream resource.

        :stability: experimental
        '''
        ...


class _ILogStreamRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LogStream.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.ILogStreamRef"

    @builtins.property
    @jsii.member(jsii_name="logStreamRef")
    def log_stream_ref(self) -> "LogStreamReference":
        '''(experimental) A reference to a LogStream resource.

        :stability: experimental
        '''
        return typing.cast("LogStreamReference", jsii.get(self, "logStreamRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogStreamRef).__jsii_proxy_class__ = lambda : _ILogStreamRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IMetricFilterRef")
class IMetricFilterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MetricFilter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="metricFilterRef")
    def metric_filter_ref(self) -> "MetricFilterReference":
        '''(experimental) A reference to a MetricFilter resource.

        :stability: experimental
        '''
        ...


class _IMetricFilterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MetricFilter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IMetricFilterRef"

    @builtins.property
    @jsii.member(jsii_name="metricFilterRef")
    def metric_filter_ref(self) -> "MetricFilterReference":
        '''(experimental) A reference to a MetricFilter resource.

        :stability: experimental
        '''
        return typing.cast("MetricFilterReference", jsii.get(self, "metricFilterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMetricFilterRef).__jsii_proxy_class__ = lambda : _IMetricFilterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IQueryDefinitionRef")
class IQueryDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QueryDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queryDefinitionRef")
    def query_definition_ref(self) -> "QueryDefinitionReference":
        '''(experimental) A reference to a QueryDefinition resource.

        :stability: experimental
        '''
        ...


class _IQueryDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QueryDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IQueryDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="queryDefinitionRef")
    def query_definition_ref(self) -> "QueryDefinitionReference":
        '''(experimental) A reference to a QueryDefinition resource.

        :stability: experimental
        '''
        return typing.cast("QueryDefinitionReference", jsii.get(self, "queryDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueryDefinitionRef).__jsii_proxy_class__ = lambda : _IQueryDefinitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IResourcePolicyRef")
class IResourcePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        ...


class _IResourcePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.IScheduledQueryRef")
class IScheduledQueryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledQuery.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scheduledQueryRef")
    def scheduled_query_ref(self) -> "ScheduledQueryReference":
        '''(experimental) A reference to a ScheduledQuery resource.

        :stability: experimental
        '''
        ...


class _IScheduledQueryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledQuery.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.IScheduledQueryRef"

    @builtins.property
    @jsii.member(jsii_name="scheduledQueryRef")
    def scheduled_query_ref(self) -> "ScheduledQueryReference":
        '''(experimental) A reference to a ScheduledQuery resource.

        :stability: experimental
        '''
        return typing.cast("ScheduledQueryReference", jsii.get(self, "scheduledQueryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduledQueryRef).__jsii_proxy_class__ = lambda : _IScheduledQueryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.ISubscriptionFilterRef")
class ISubscriptionFilterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriptionFilter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subscriptionFilterRef")
    def subscription_filter_ref(self) -> "SubscriptionFilterReference":
        '''(experimental) A reference to a SubscriptionFilter resource.

        :stability: experimental
        '''
        ...


class _ISubscriptionFilterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriptionFilter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.ISubscriptionFilterRef"

    @builtins.property
    @jsii.member(jsii_name="subscriptionFilterRef")
    def subscription_filter_ref(self) -> "SubscriptionFilterReference":
        '''(experimental) A reference to a SubscriptionFilter resource.

        :stability: experimental
        '''
        return typing.cast("SubscriptionFilterReference", jsii.get(self, "subscriptionFilterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubscriptionFilterRef).__jsii_proxy_class__ = lambda : _ISubscriptionFilterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_logs.ITransformerRef")
class ITransformerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Transformer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transformerRef")
    def transformer_ref(self) -> "TransformerReference":
        '''(experimental) A reference to a Transformer resource.

        :stability: experimental
        '''
        ...


class _ITransformerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Transformer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_logs.ITransformerRef"

    @builtins.property
    @jsii.member(jsii_name="transformerRef")
    def transformer_ref(self) -> "TransformerReference":
        '''(experimental) A reference to a Transformer resource.

        :stability: experimental
        '''
        return typing.cast("TransformerReference", jsii.get(self, "transformerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransformerRef).__jsii_proxy_class__ = lambda : _ITransformerRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.IntegrationReference",
    jsii_struct_bases=[],
    name_mapping={"integration_name": "integrationName"},
)
class IntegrationReference:
    def __init__(self, *, integration_name: builtins.str) -> None:
        '''A reference to a Integration resource.

        :param integration_name: The IntegrationName of the Integration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            integration_reference = interfaces_logs.IntegrationReference(
                integration_name="integrationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1703873f2c4ccbee88bbf0c7ca2ddfc3f1234e6825106fd7e40f138a6a2b2c12)
            check_type(argname="argument integration_name", value=integration_name, expected_type=type_hints["integration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "integration_name": integration_name,
        }

    @builtins.property
    def integration_name(self) -> builtins.str:
        '''The IntegrationName of the Integration resource.'''
        result = self._values.get("integration_name")
        assert result is not None, "Required property 'integration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.LogAnomalyDetectorReference",
    jsii_struct_bases=[],
    name_mapping={"anomaly_detector_arn": "anomalyDetectorArn"},
)
class LogAnomalyDetectorReference:
    def __init__(self, *, anomaly_detector_arn: builtins.str) -> None:
        '''A reference to a LogAnomalyDetector resource.

        :param anomaly_detector_arn: The AnomalyDetectorArn of the LogAnomalyDetector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            log_anomaly_detector_reference = interfaces_logs.LogAnomalyDetectorReference(
                anomaly_detector_arn="anomalyDetectorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__152b39908445fadfbc79d871241b90c661b02270875df9f6e2dad130314205d3)
            check_type(argname="argument anomaly_detector_arn", value=anomaly_detector_arn, expected_type=type_hints["anomaly_detector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "anomaly_detector_arn": anomaly_detector_arn,
        }

    @builtins.property
    def anomaly_detector_arn(self) -> builtins.str:
        '''The AnomalyDetectorArn of the LogAnomalyDetector resource.'''
        result = self._values.get("anomaly_detector_arn")
        assert result is not None, "Required property 'anomaly_detector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogAnomalyDetectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.LogGroupReference",
    jsii_struct_bases=[],
    name_mapping={"log_group_arn": "logGroupArn", "log_group_name": "logGroupName"},
)
class LogGroupReference:
    def __init__(
        self,
        *,
        log_group_arn: builtins.str,
        log_group_name: builtins.str,
    ) -> None:
        '''A reference to a LogGroup resource.

        :param log_group_arn: The ARN of the LogGroup resource.
        :param log_group_name: The LogGroupName of the LogGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            log_group_reference = interfaces_logs.LogGroupReference(
                log_group_arn="logGroupArn",
                log_group_name="logGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fe89828e7a154c5f7552641e63ee94599a41b1e437ef573c9f5e6db186190eb)
            check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_arn": log_group_arn,
            "log_group_name": log_group_name,
        }

    @builtins.property
    def log_group_arn(self) -> builtins.str:
        '''The ARN of the LogGroup resource.'''
        result = self._values.get("log_group_arn")
        assert result is not None, "Required property 'log_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The LogGroupName of the LogGroup resource.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.LogStreamReference",
    jsii_struct_bases=[],
    name_mapping={
        "log_group_name": "logGroupName",
        "log_stream_name": "logStreamName",
    },
)
class LogStreamReference:
    def __init__(
        self,
        *,
        log_group_name: builtins.str,
        log_stream_name: builtins.str,
    ) -> None:
        '''A reference to a LogStream resource.

        :param log_group_name: The LogGroupName of the LogStream resource.
        :param log_stream_name: The LogStreamName of the LogStream resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            log_stream_reference = interfaces_logs.LogStreamReference(
                log_group_name="logGroupName",
                log_stream_name="logStreamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85d915d59921c4aa886cbb4de386337e2c238f0d53665de4072f8408e2b88eed)
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            check_type(argname="argument log_stream_name", value=log_stream_name, expected_type=type_hints["log_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_name": log_group_name,
            "log_stream_name": log_stream_name,
        }

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The LogGroupName of the LogStream resource.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_stream_name(self) -> builtins.str:
        '''The LogStreamName of the LogStream resource.'''
        result = self._values.get("log_stream_name")
        assert result is not None, "Required property 'log_stream_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogStreamReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.MetricFilterReference",
    jsii_struct_bases=[],
    name_mapping={"filter_name": "filterName", "log_group_name": "logGroupName"},
)
class MetricFilterReference:
    def __init__(
        self,
        *,
        filter_name: builtins.str,
        log_group_name: builtins.str,
    ) -> None:
        '''A reference to a MetricFilter resource.

        :param filter_name: The FilterName of the MetricFilter resource.
        :param log_group_name: The LogGroupName of the MetricFilter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            metric_filter_reference = interfaces_logs.MetricFilterReference(
                filter_name="filterName",
                log_group_name="logGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dd155a7485ffe46c95eee44276dec1d256a0f0efaa393c9cf9bca74377784a0)
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_name": filter_name,
            "log_group_name": log_group_name,
        }

    @builtins.property
    def filter_name(self) -> builtins.str:
        '''The FilterName of the MetricFilter resource.'''
        result = self._values.get("filter_name")
        assert result is not None, "Required property 'filter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The LogGroupName of the MetricFilter resource.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetricFilterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.QueryDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"query_definition_id": "queryDefinitionId"},
)
class QueryDefinitionReference:
    def __init__(self, *, query_definition_id: builtins.str) -> None:
        '''A reference to a QueryDefinition resource.

        :param query_definition_id: The QueryDefinitionId of the QueryDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            query_definition_reference = interfaces_logs.QueryDefinitionReference(
                query_definition_id="queryDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6f0fd6904adbb837b22190ab99423e0e018696b8ad4a24948c5f16de048ef3b)
            check_type(argname="argument query_definition_id", value=query_definition_id, expected_type=type_hints["query_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_definition_id": query_definition_id,
        }

    @builtins.property
    def query_definition_id(self) -> builtins.str:
        '''The QueryDefinitionId of the QueryDefinition resource.'''
        result = self._values.get("query_definition_id")
        assert result is not None, "Required property 'query_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueryDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_name": "policyName"},
)
class ResourcePolicyReference:
    def __init__(self, *, policy_name: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param policy_name: The PolicyName of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            resource_policy_reference = interfaces_logs.ResourcePolicyReference(
                policy_name="policyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dd0a9d7208bca48cbe9ee31cf0855b2cfe4bf47b854d644fb162df8becf60a5)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_name": policy_name,
        }

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The PolicyName of the ResourcePolicy resource.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.ScheduledQueryReference",
    jsii_struct_bases=[],
    name_mapping={"scheduled_query_arn": "scheduledQueryArn"},
)
class ScheduledQueryReference:
    def __init__(self, *, scheduled_query_arn: builtins.str) -> None:
        '''A reference to a ScheduledQuery resource.

        :param scheduled_query_arn: The ScheduledQueryArn of the ScheduledQuery resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            scheduled_query_reference = interfaces_logs.ScheduledQueryReference(
                scheduled_query_arn="scheduledQueryArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__090fd04987a985f7f1ab057e746857042cf4b0d5ad8e6b821b8000c6ab14b7ec)
            check_type(argname="argument scheduled_query_arn", value=scheduled_query_arn, expected_type=type_hints["scheduled_query_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scheduled_query_arn": scheduled_query_arn,
        }

    @builtins.property
    def scheduled_query_arn(self) -> builtins.str:
        '''The ScheduledQueryArn of the ScheduledQuery resource.'''
        result = self._values.get("scheduled_query_arn")
        assert result is not None, "Required property 'scheduled_query_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduledQueryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.SubscriptionFilterReference",
    jsii_struct_bases=[],
    name_mapping={"filter_name": "filterName", "log_group_name": "logGroupName"},
)
class SubscriptionFilterReference:
    def __init__(
        self,
        *,
        filter_name: builtins.str,
        log_group_name: builtins.str,
    ) -> None:
        '''A reference to a SubscriptionFilter resource.

        :param filter_name: The FilterName of the SubscriptionFilter resource.
        :param log_group_name: The LogGroupName of the SubscriptionFilter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            subscription_filter_reference = interfaces_logs.SubscriptionFilterReference(
                filter_name="filterName",
                log_group_name="logGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e03b9321b3853e172ea485b7f87ee05500da31635f70cfb3931308cf53d5b7c9)
            check_type(argname="argument filter_name", value=filter_name, expected_type=type_hints["filter_name"])
            check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_name": filter_name,
            "log_group_name": log_group_name,
        }

    @builtins.property
    def filter_name(self) -> builtins.str:
        '''The FilterName of the SubscriptionFilter resource.'''
        result = self._values.get("filter_name")
        assert result is not None, "Required property 'filter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_group_name(self) -> builtins.str:
        '''The LogGroupName of the SubscriptionFilter resource.'''
        result = self._values.get("log_group_name")
        assert result is not None, "Required property 'log_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionFilterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_logs.TransformerReference",
    jsii_struct_bases=[],
    name_mapping={"log_group_identifier": "logGroupIdentifier"},
)
class TransformerReference:
    def __init__(self, *, log_group_identifier: builtins.str) -> None:
        '''A reference to a Transformer resource.

        :param log_group_identifier: The LogGroupIdentifier of the Transformer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_logs as interfaces_logs
            
            transformer_reference = interfaces_logs.TransformerReference(
                log_group_identifier="logGroupIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15e0e35db8a493355cc50017a7dbec5573a8aaa6167649b1ea54abc2a13252d0)
            check_type(argname="argument log_group_identifier", value=log_group_identifier, expected_type=type_hints["log_group_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_group_identifier": log_group_identifier,
        }

    @builtins.property
    def log_group_identifier(self) -> builtins.str:
        '''The LogGroupIdentifier of the Transformer resource.'''
        result = self._values.get("log_group_identifier")
        assert result is not None, "Required property 'log_group_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransformerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccountPolicyReference",
    "DeliveryDestinationReference",
    "DeliveryReference",
    "DeliverySourceReference",
    "DestinationReference",
    "IAccountPolicyRef",
    "IDeliveryDestinationRef",
    "IDeliveryRef",
    "IDeliverySourceRef",
    "IDestinationRef",
    "IIntegrationRef",
    "ILogAnomalyDetectorRef",
    "ILogGroupRef",
    "ILogStreamRef",
    "IMetricFilterRef",
    "IQueryDefinitionRef",
    "IResourcePolicyRef",
    "IScheduledQueryRef",
    "ISubscriptionFilterRef",
    "ITransformerRef",
    "IntegrationReference",
    "LogAnomalyDetectorReference",
    "LogGroupReference",
    "LogStreamReference",
    "MetricFilterReference",
    "QueryDefinitionReference",
    "ResourcePolicyReference",
    "ScheduledQueryReference",
    "SubscriptionFilterReference",
    "TransformerReference",
]

publication.publish()

def _typecheckingstub__6e5d30d368dae32e7214dde7327399c249fc454b70c0d414b73a731d6b3b975a(
    *,
    account_id: builtins.str,
    policy_name: builtins.str,
    policy_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d77a1fb4ac2647cdfa788a3962d5ff897d9ba488f410dcac7efc4ea322da89c9(
    *,
    delivery_destination_arn: builtins.str,
    delivery_destination_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__120822921746f4d35e3b0433d834a26219946042aca3813bab6a68930277875e(
    *,
    delivery_arn: builtins.str,
    delivery_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84496c584c12fa0a7abce78ecb2626aebff2ea2da1b8692bd28a3ea5be19b90(
    *,
    delivery_source_arn: builtins.str,
    delivery_source_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8bc552d9e2cd9371b7b566d808d316d9592f3ce00dab981d5ff39de473ff8e1(
    *,
    destination_arn: builtins.str,
    destination_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1703873f2c4ccbee88bbf0c7ca2ddfc3f1234e6825106fd7e40f138a6a2b2c12(
    *,
    integration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__152b39908445fadfbc79d871241b90c661b02270875df9f6e2dad130314205d3(
    *,
    anomaly_detector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fe89828e7a154c5f7552641e63ee94599a41b1e437ef573c9f5e6db186190eb(
    *,
    log_group_arn: builtins.str,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85d915d59921c4aa886cbb4de386337e2c238f0d53665de4072f8408e2b88eed(
    *,
    log_group_name: builtins.str,
    log_stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dd155a7485ffe46c95eee44276dec1d256a0f0efaa393c9cf9bca74377784a0(
    *,
    filter_name: builtins.str,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f0fd6904adbb837b22190ab99423e0e018696b8ad4a24948c5f16de048ef3b(
    *,
    query_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dd0a9d7208bca48cbe9ee31cf0855b2cfe4bf47b854d644fb162df8becf60a5(
    *,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__090fd04987a985f7f1ab057e746857042cf4b0d5ad8e6b821b8000c6ab14b7ec(
    *,
    scheduled_query_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e03b9321b3853e172ea485b7f87ee05500da31635f70cfb3931308cf53d5b7c9(
    *,
    filter_name: builtins.str,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15e0e35db8a493355cc50017a7dbec5573a8aaa6167649b1ea54abc2a13252d0(
    *,
    log_group_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccountPolicyRef, IDeliveryDestinationRef, IDeliveryRef, IDeliverySourceRef, IDestinationRef, IIntegrationRef, ILogAnomalyDetectorRef, ILogGroupRef, ILogStreamRef, IMetricFilterRef, IQueryDefinitionRef, IResourcePolicyRef, IScheduledQueryRef, ISubscriptionFilterRef, ITransformerRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
