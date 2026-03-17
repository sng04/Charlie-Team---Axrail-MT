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
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.CapacityManagerDataExportReference",
    jsii_struct_bases=[],
    name_mapping={"capacity_manager_data_export_id": "capacityManagerDataExportId"},
)
class CapacityManagerDataExportReference:
    def __init__(self, *, capacity_manager_data_export_id: builtins.str) -> None:
        '''A reference to a CapacityManagerDataExport resource.

        :param capacity_manager_data_export_id: The CapacityManagerDataExportId of the CapacityManagerDataExport resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            capacity_manager_data_export_reference = interfaces_ec2.CapacityManagerDataExportReference(
                capacity_manager_data_export_id="capacityManagerDataExportId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9a5eb41f01361d654103936a1b9162b653c840153b29de7c1a9fd3b59192fb)
            check_type(argname="argument capacity_manager_data_export_id", value=capacity_manager_data_export_id, expected_type=type_hints["capacity_manager_data_export_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity_manager_data_export_id": capacity_manager_data_export_id,
        }

    @builtins.property
    def capacity_manager_data_export_id(self) -> builtins.str:
        '''The CapacityManagerDataExportId of the CapacityManagerDataExport resource.'''
        result = self._values.get("capacity_manager_data_export_id")
        assert result is not None, "Required property 'capacity_manager_data_export_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapacityManagerDataExportReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.CapacityReservationFleetReference",
    jsii_struct_bases=[],
    name_mapping={"capacity_reservation_fleet_id": "capacityReservationFleetId"},
)
class CapacityReservationFleetReference:
    def __init__(self, *, capacity_reservation_fleet_id: builtins.str) -> None:
        '''A reference to a CapacityReservationFleet resource.

        :param capacity_reservation_fleet_id: The CapacityReservationFleetId of the CapacityReservationFleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            capacity_reservation_fleet_reference = interfaces_ec2.CapacityReservationFleetReference(
                capacity_reservation_fleet_id="capacityReservationFleetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a639beaf30f994702c8cce7edf0705ad867304287d6ef4b89b9d26288bcf32dc)
            check_type(argname="argument capacity_reservation_fleet_id", value=capacity_reservation_fleet_id, expected_type=type_hints["capacity_reservation_fleet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity_reservation_fleet_id": capacity_reservation_fleet_id,
        }

    @builtins.property
    def capacity_reservation_fleet_id(self) -> builtins.str:
        '''The CapacityReservationFleetId of the CapacityReservationFleet resource.'''
        result = self._values.get("capacity_reservation_fleet_id")
        assert result is not None, "Required property 'capacity_reservation_fleet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapacityReservationFleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.CapacityReservationReference",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_reservation_arn": "capacityReservationArn",
        "capacity_reservation_id": "capacityReservationId",
    },
)
class CapacityReservationReference:
    def __init__(
        self,
        *,
        capacity_reservation_arn: builtins.str,
        capacity_reservation_id: builtins.str,
    ) -> None:
        '''A reference to a CapacityReservation resource.

        :param capacity_reservation_arn: The ARN of the CapacityReservation resource.
        :param capacity_reservation_id: The Id of the CapacityReservation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            capacity_reservation_reference = interfaces_ec2.CapacityReservationReference(
                capacity_reservation_arn="capacityReservationArn",
                capacity_reservation_id="capacityReservationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c9ad69aaf7d522f4991de0383043ae158e9356f51e89f794bed440c4a0e47da)
            check_type(argname="argument capacity_reservation_arn", value=capacity_reservation_arn, expected_type=type_hints["capacity_reservation_arn"])
            check_type(argname="argument capacity_reservation_id", value=capacity_reservation_id, expected_type=type_hints["capacity_reservation_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity_reservation_arn": capacity_reservation_arn,
            "capacity_reservation_id": capacity_reservation_id,
        }

    @builtins.property
    def capacity_reservation_arn(self) -> builtins.str:
        '''The ARN of the CapacityReservation resource.'''
        result = self._values.get("capacity_reservation_arn")
        assert result is not None, "Required property 'capacity_reservation_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_reservation_id(self) -> builtins.str:
        '''The Id of the CapacityReservation resource.'''
        result = self._values.get("capacity_reservation_id")
        assert result is not None, "Required property 'capacity_reservation_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapacityReservationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.CarrierGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"carrier_gateway_id": "carrierGatewayId"},
)
class CarrierGatewayReference:
    def __init__(self, *, carrier_gateway_id: builtins.str) -> None:
        '''A reference to a CarrierGateway resource.

        :param carrier_gateway_id: The CarrierGatewayId of the CarrierGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            carrier_gateway_reference = interfaces_ec2.CarrierGatewayReference(
                carrier_gateway_id="carrierGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0e46133742af7c64acb96c7643cdd4b68523b466749e2e2f37a9b8fb3c3e311)
            check_type(argname="argument carrier_gateway_id", value=carrier_gateway_id, expected_type=type_hints["carrier_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "carrier_gateway_id": carrier_gateway_id,
        }

    @builtins.property
    def carrier_gateway_id(self) -> builtins.str:
        '''The CarrierGatewayId of the CarrierGateway resource.'''
        result = self._values.get("carrier_gateway_id")
        assert result is not None, "Required property 'carrier_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CarrierGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ClientVpnAuthorizationRuleReference",
    jsii_struct_bases=[],
    name_mapping={"client_vpn_authorization_rule_id": "clientVpnAuthorizationRuleId"},
)
class ClientVpnAuthorizationRuleReference:
    def __init__(self, *, client_vpn_authorization_rule_id: builtins.str) -> None:
        '''A reference to a ClientVpnAuthorizationRule resource.

        :param client_vpn_authorization_rule_id: The Id of the ClientVpnAuthorizationRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            client_vpn_authorization_rule_reference = interfaces_ec2.ClientVpnAuthorizationRuleReference(
                client_vpn_authorization_rule_id="clientVpnAuthorizationRuleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57fa36bad5ea59002afc4e1ffe1f5e727fc3229f1b2cfb394708c3fe01884cd7)
            check_type(argname="argument client_vpn_authorization_rule_id", value=client_vpn_authorization_rule_id, expected_type=type_hints["client_vpn_authorization_rule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_vpn_authorization_rule_id": client_vpn_authorization_rule_id,
        }

    @builtins.property
    def client_vpn_authorization_rule_id(self) -> builtins.str:
        '''The Id of the ClientVpnAuthorizationRule resource.'''
        result = self._values.get("client_vpn_authorization_rule_id")
        assert result is not None, "Required property 'client_vpn_authorization_rule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClientVpnAuthorizationRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ClientVpnEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"client_vpn_endpoint_id": "clientVpnEndpointId"},
)
class ClientVpnEndpointReference:
    def __init__(self, *, client_vpn_endpoint_id: builtins.str) -> None:
        '''A reference to a ClientVpnEndpoint resource.

        :param client_vpn_endpoint_id: The Id of the ClientVpnEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            client_vpn_endpoint_reference = interfaces_ec2.ClientVpnEndpointReference(
                client_vpn_endpoint_id="clientVpnEndpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3483bfe3b3da3b5359fa2a5ef1fcb0071cbabc25dc4825b83c857cc83437b76)
            check_type(argname="argument client_vpn_endpoint_id", value=client_vpn_endpoint_id, expected_type=type_hints["client_vpn_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_vpn_endpoint_id": client_vpn_endpoint_id,
        }

    @builtins.property
    def client_vpn_endpoint_id(self) -> builtins.str:
        '''The Id of the ClientVpnEndpoint resource.'''
        result = self._values.get("client_vpn_endpoint_id")
        assert result is not None, "Required property 'client_vpn_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClientVpnEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ClientVpnRouteReference",
    jsii_struct_bases=[],
    name_mapping={"client_vpn_route_id": "clientVpnRouteId"},
)
class ClientVpnRouteReference:
    def __init__(self, *, client_vpn_route_id: builtins.str) -> None:
        '''A reference to a ClientVpnRoute resource.

        :param client_vpn_route_id: The Id of the ClientVpnRoute resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            client_vpn_route_reference = interfaces_ec2.ClientVpnRouteReference(
                client_vpn_route_id="clientVpnRouteId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955d0e41ede8d58fe3f1e03206fcc6cf2c837c6a701c1cdbfcdb58c18e7fef2f)
            check_type(argname="argument client_vpn_route_id", value=client_vpn_route_id, expected_type=type_hints["client_vpn_route_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_vpn_route_id": client_vpn_route_id,
        }

    @builtins.property
    def client_vpn_route_id(self) -> builtins.str:
        '''The Id of the ClientVpnRoute resource.'''
        result = self._values.get("client_vpn_route_id")
        assert result is not None, "Required property 'client_vpn_route_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClientVpnRouteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ClientVpnTargetNetworkAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "client_vpn_target_network_association_id": "clientVpnTargetNetworkAssociationId",
    },
)
class ClientVpnTargetNetworkAssociationReference:
    def __init__(
        self,
        *,
        client_vpn_target_network_association_id: builtins.str,
    ) -> None:
        '''A reference to a ClientVpnTargetNetworkAssociation resource.

        :param client_vpn_target_network_association_id: The Id of the ClientVpnTargetNetworkAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            client_vpn_target_network_association_reference = interfaces_ec2.ClientVpnTargetNetworkAssociationReference(
                client_vpn_target_network_association_id="clientVpnTargetNetworkAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3c7fcd523c40c46f0da3e82691f5dd7318f305bacc934e54d00ced4247cdc9d)
            check_type(argname="argument client_vpn_target_network_association_id", value=client_vpn_target_network_association_id, expected_type=type_hints["client_vpn_target_network_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_vpn_target_network_association_id": client_vpn_target_network_association_id,
        }

    @builtins.property
    def client_vpn_target_network_association_id(self) -> builtins.str:
        '''The Id of the ClientVpnTargetNetworkAssociation resource.'''
        result = self._values.get("client_vpn_target_network_association_id")
        assert result is not None, "Required property 'client_vpn_target_network_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClientVpnTargetNetworkAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.CustomerGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"customer_gateway_id": "customerGatewayId"},
)
class CustomerGatewayReference:
    def __init__(self, *, customer_gateway_id: builtins.str) -> None:
        '''A reference to a CustomerGateway resource.

        :param customer_gateway_id: The CustomerGatewayId of the CustomerGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            customer_gateway_reference = interfaces_ec2.CustomerGatewayReference(
                customer_gateway_id="customerGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3af586fe619a2c65fed2a5927f842d40e7d8218e2affcc6d9632c1f96c1a5f08)
            check_type(argname="argument customer_gateway_id", value=customer_gateway_id, expected_type=type_hints["customer_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "customer_gateway_id": customer_gateway_id,
        }

    @builtins.property
    def customer_gateway_id(self) -> builtins.str:
        '''The CustomerGatewayId of the CustomerGateway resource.'''
        result = self._values.get("customer_gateway_id")
        assert result is not None, "Required property 'customer_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomerGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.DHCPOptionsReference",
    jsii_struct_bases=[],
    name_mapping={"dhcp_options_id": "dhcpOptionsId"},
)
class DHCPOptionsReference:
    def __init__(self, *, dhcp_options_id: builtins.str) -> None:
        '''A reference to a DHCPOptions resource.

        :param dhcp_options_id: The DhcpOptionsId of the DHCPOptions resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            d_hCPOptions_reference = interfaces_ec2.DHCPOptionsReference(
                dhcp_options_id="dhcpOptionsId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e883f4c5fc03af683cd9793dfbd9657b07f02feb74e5fc9ccaaa558e82d8b1cb)
            check_type(argname="argument dhcp_options_id", value=dhcp_options_id, expected_type=type_hints["dhcp_options_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dhcp_options_id": dhcp_options_id,
        }

    @builtins.property
    def dhcp_options_id(self) -> builtins.str:
        '''The DhcpOptionsId of the DHCPOptions resource.'''
        result = self._values.get("dhcp_options_id")
        assert result is not None, "Required property 'dhcp_options_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DHCPOptionsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.EC2FleetReference",
    jsii_struct_bases=[],
    name_mapping={"fleet_id": "fleetId"},
)
class EC2FleetReference:
    def __init__(self, *, fleet_id: builtins.str) -> None:
        '''A reference to a EC2Fleet resource.

        :param fleet_id: The FleetId of the EC2Fleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            e_c2_fleet_reference = interfaces_ec2.EC2FleetReference(
                fleet_id="fleetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a9a7b73ab5651dd8a52334ffb8d29401dc3fa34c2fe49e7a22e3dfcd471697)
            check_type(argname="argument fleet_id", value=fleet_id, expected_type=type_hints["fleet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_id": fleet_id,
        }

    @builtins.property
    def fleet_id(self) -> builtins.str:
        '''The FleetId of the EC2Fleet resource.'''
        result = self._values.get("fleet_id")
        assert result is not None, "Required property 'fleet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EC2FleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.EIPAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"eip_association_id": "eipAssociationId"},
)
class EIPAssociationReference:
    def __init__(self, *, eip_association_id: builtins.str) -> None:
        '''A reference to a EIPAssociation resource.

        :param eip_association_id: The Id of the EIPAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            e_iPAssociation_reference = interfaces_ec2.EIPAssociationReference(
                eip_association_id="eipAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa3055e31c0189eeb8900337e9a55041990b609176240fdfb650e8d6ea71ce4f)
            check_type(argname="argument eip_association_id", value=eip_association_id, expected_type=type_hints["eip_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "eip_association_id": eip_association_id,
        }

    @builtins.property
    def eip_association_id(self) -> builtins.str:
        '''The Id of the EIPAssociation resource.'''
        result = self._values.get("eip_association_id")
        assert result is not None, "Required property 'eip_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EIPAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.EIPReference",
    jsii_struct_bases=[],
    name_mapping={"allocation_id": "allocationId", "public_ip": "publicIp"},
)
class EIPReference:
    def __init__(self, *, allocation_id: builtins.str, public_ip: builtins.str) -> None:
        '''A reference to a EIP resource.

        :param allocation_id: The AllocationId of the EIP resource.
        :param public_ip: The PublicIp of the EIP resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            e_iPReference = interfaces_ec2.EIPReference(
                allocation_id="allocationId",
                public_ip="publicIp"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a670552386e3bc70dcecf664a8471c2e1ae1e3d6daecb073bb63f3a449edf2e)
            check_type(argname="argument allocation_id", value=allocation_id, expected_type=type_hints["allocation_id"])
            check_type(argname="argument public_ip", value=public_ip, expected_type=type_hints["public_ip"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "allocation_id": allocation_id,
            "public_ip": public_ip,
        }

    @builtins.property
    def allocation_id(self) -> builtins.str:
        '''The AllocationId of the EIP resource.'''
        result = self._values.get("allocation_id")
        assert result is not None, "Required property 'allocation_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_ip(self) -> builtins.str:
        '''The PublicIp of the EIP resource.'''
        result = self._values.get("public_ip")
        assert result is not None, "Required property 'public_ip' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EIPReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.EgressOnlyInternetGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"egress_only_internet_gateway_id": "egressOnlyInternetGatewayId"},
)
class EgressOnlyInternetGatewayReference:
    def __init__(self, *, egress_only_internet_gateway_id: builtins.str) -> None:
        '''A reference to a EgressOnlyInternetGateway resource.

        :param egress_only_internet_gateway_id: The Id of the EgressOnlyInternetGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            egress_only_internet_gateway_reference = interfaces_ec2.EgressOnlyInternetGatewayReference(
                egress_only_internet_gateway_id="egressOnlyInternetGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d13b682c8162d3e06226c015673682f4ca0b635bf82debdfa16df85ebff4c9c4)
            check_type(argname="argument egress_only_internet_gateway_id", value=egress_only_internet_gateway_id, expected_type=type_hints["egress_only_internet_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "egress_only_internet_gateway_id": egress_only_internet_gateway_id,
        }

    @builtins.property
    def egress_only_internet_gateway_id(self) -> builtins.str:
        '''The Id of the EgressOnlyInternetGateway resource.'''
        result = self._values.get("egress_only_internet_gateway_id")
        assert result is not None, "Required property 'egress_only_internet_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EgressOnlyInternetGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.EnclaveCertificateIamRoleAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"certificate_arn": "certificateArn", "role_arn": "roleArn"},
)
class EnclaveCertificateIamRoleAssociationReference:
    def __init__(
        self,
        *,
        certificate_arn: builtins.str,
        role_arn: builtins.str,
    ) -> None:
        '''A reference to a EnclaveCertificateIamRoleAssociation resource.

        :param certificate_arn: The CertificateArn of the EnclaveCertificateIamRoleAssociation resource.
        :param role_arn: The RoleArn of the EnclaveCertificateIamRoleAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            enclave_certificate_iam_role_association_reference = interfaces_ec2.EnclaveCertificateIamRoleAssociationReference(
                certificate_arn="certificateArn",
                role_arn="roleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52a31f01eec480fc55294e086132d2231213830dc4e9ffe9768bac28e14e514b)
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_arn": certificate_arn,
            "role_arn": role_arn,
        }

    @builtins.property
    def certificate_arn(self) -> builtins.str:
        '''The CertificateArn of the EnclaveCertificateIamRoleAssociation resource.'''
        result = self._values.get("certificate_arn")
        assert result is not None, "Required property 'certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The RoleArn of the EnclaveCertificateIamRoleAssociation resource.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnclaveCertificateIamRoleAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.FlowLogReference",
    jsii_struct_bases=[],
    name_mapping={"flow_log_id": "flowLogId"},
)
class FlowLogReference:
    def __init__(self, *, flow_log_id: builtins.str) -> None:
        '''A reference to a FlowLog resource.

        :param flow_log_id: The Id of the FlowLog resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            flow_log_reference = interfaces_ec2.FlowLogReference(
                flow_log_id="flowLogId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c7f7816dd23c5966fe0b62e931bf88b8f149b9f474737f0550657e967cf640f)
            check_type(argname="argument flow_log_id", value=flow_log_id, expected_type=type_hints["flow_log_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_log_id": flow_log_id,
        }

    @builtins.property
    def flow_log_id(self) -> builtins.str:
        '''The Id of the FlowLog resource.'''
        result = self._values.get("flow_log_id")
        assert result is not None, "Required property 'flow_log_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowLogReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.GatewayRouteTableAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"gateway_id": "gatewayId"},
)
class GatewayRouteTableAssociationReference:
    def __init__(self, *, gateway_id: builtins.str) -> None:
        '''A reference to a GatewayRouteTableAssociation resource.

        :param gateway_id: The GatewayId of the GatewayRouteTableAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            gateway_route_table_association_reference = interfaces_ec2.GatewayRouteTableAssociationReference(
                gateway_id="gatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73d71f159bc2caf82458bd401787c04be0e393554b0767a258a4c1f03a7254ee)
            check_type(argname="argument gateway_id", value=gateway_id, expected_type=type_hints["gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_id": gateway_id,
        }

    @builtins.property
    def gateway_id(self) -> builtins.str:
        '''The GatewayId of the GatewayRouteTableAssociation resource.'''
        result = self._values.get("gateway_id")
        assert result is not None, "Required property 'gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayRouteTableAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.HostReference",
    jsii_struct_bases=[],
    name_mapping={"host_id": "hostId"},
)
class HostReference:
    def __init__(self, *, host_id: builtins.str) -> None:
        '''A reference to a Host resource.

        :param host_id: The HostId of the Host resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            host_reference = interfaces_ec2.HostReference(
                host_id="hostId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d7ca0868625d89fec5ae55e8e630cc64fa2b42416142c1e2df8e9388dc41c50)
            check_type(argname="argument host_id", value=host_id, expected_type=type_hints["host_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host_id": host_id,
        }

    @builtins.property
    def host_id(self) -> builtins.str:
        '''The HostId of the Host resource.'''
        result = self._values.get("host_id")
        assert result is not None, "Required property 'host_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ICapacityManagerDataExportRef"
)
class ICapacityManagerDataExportRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityManagerDataExport.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="capacityManagerDataExportRef")
    def capacity_manager_data_export_ref(self) -> "CapacityManagerDataExportReference":
        '''(experimental) A reference to a CapacityManagerDataExport resource.

        :stability: experimental
        '''
        ...


class _ICapacityManagerDataExportRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityManagerDataExport.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ICapacityManagerDataExportRef"

    @builtins.property
    @jsii.member(jsii_name="capacityManagerDataExportRef")
    def capacity_manager_data_export_ref(self) -> "CapacityManagerDataExportReference":
        '''(experimental) A reference to a CapacityManagerDataExport resource.

        :stability: experimental
        '''
        return typing.cast("CapacityManagerDataExportReference", jsii.get(self, "capacityManagerDataExportRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICapacityManagerDataExportRef).__jsii_proxy_class__ = lambda : _ICapacityManagerDataExportRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ICapacityReservationFleetRef"
)
class ICapacityReservationFleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityReservationFleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="capacityReservationFleetRef")
    def capacity_reservation_fleet_ref(self) -> "CapacityReservationFleetReference":
        '''(experimental) A reference to a CapacityReservationFleet resource.

        :stability: experimental
        '''
        ...


class _ICapacityReservationFleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityReservationFleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ICapacityReservationFleetRef"

    @builtins.property
    @jsii.member(jsii_name="capacityReservationFleetRef")
    def capacity_reservation_fleet_ref(self) -> "CapacityReservationFleetReference":
        '''(experimental) A reference to a CapacityReservationFleet resource.

        :stability: experimental
        '''
        return typing.cast("CapacityReservationFleetReference", jsii.get(self, "capacityReservationFleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICapacityReservationFleetRef).__jsii_proxy_class__ = lambda : _ICapacityReservationFleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ICapacityReservationRef")
class ICapacityReservationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityReservation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="capacityReservationRef")
    def capacity_reservation_ref(self) -> "CapacityReservationReference":
        '''(experimental) A reference to a CapacityReservation resource.

        :stability: experimental
        '''
        ...


class _ICapacityReservationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityReservation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ICapacityReservationRef"

    @builtins.property
    @jsii.member(jsii_name="capacityReservationRef")
    def capacity_reservation_ref(self) -> "CapacityReservationReference":
        '''(experimental) A reference to a CapacityReservation resource.

        :stability: experimental
        '''
        return typing.cast("CapacityReservationReference", jsii.get(self, "capacityReservationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICapacityReservationRef).__jsii_proxy_class__ = lambda : _ICapacityReservationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ICarrierGatewayRef")
class ICarrierGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CarrierGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="carrierGatewayRef")
    def carrier_gateway_ref(self) -> "CarrierGatewayReference":
        '''(experimental) A reference to a CarrierGateway resource.

        :stability: experimental
        '''
        ...


class _ICarrierGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CarrierGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ICarrierGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="carrierGatewayRef")
    def carrier_gateway_ref(self) -> "CarrierGatewayReference":
        '''(experimental) A reference to a CarrierGateway resource.

        :stability: experimental
        '''
        return typing.cast("CarrierGatewayReference", jsii.get(self, "carrierGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICarrierGatewayRef).__jsii_proxy_class__ = lambda : _ICarrierGatewayRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IClientVpnAuthorizationRuleRef"
)
class IClientVpnAuthorizationRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClientVpnAuthorizationRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clientVpnAuthorizationRuleRef")
    def client_vpn_authorization_rule_ref(
        self,
    ) -> "ClientVpnAuthorizationRuleReference":
        '''(experimental) A reference to a ClientVpnAuthorizationRule resource.

        :stability: experimental
        '''
        ...


class _IClientVpnAuthorizationRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClientVpnAuthorizationRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IClientVpnAuthorizationRuleRef"

    @builtins.property
    @jsii.member(jsii_name="clientVpnAuthorizationRuleRef")
    def client_vpn_authorization_rule_ref(
        self,
    ) -> "ClientVpnAuthorizationRuleReference":
        '''(experimental) A reference to a ClientVpnAuthorizationRule resource.

        :stability: experimental
        '''
        return typing.cast("ClientVpnAuthorizationRuleReference", jsii.get(self, "clientVpnAuthorizationRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClientVpnAuthorizationRuleRef).__jsii_proxy_class__ = lambda : _IClientVpnAuthorizationRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IClientVpnEndpointRef")
class IClientVpnEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClientVpnEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clientVpnEndpointRef")
    def client_vpn_endpoint_ref(self) -> "ClientVpnEndpointReference":
        '''(experimental) A reference to a ClientVpnEndpoint resource.

        :stability: experimental
        '''
        ...


class _IClientVpnEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClientVpnEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IClientVpnEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="clientVpnEndpointRef")
    def client_vpn_endpoint_ref(self) -> "ClientVpnEndpointReference":
        '''(experimental) A reference to a ClientVpnEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("ClientVpnEndpointReference", jsii.get(self, "clientVpnEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClientVpnEndpointRef).__jsii_proxy_class__ = lambda : _IClientVpnEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IClientVpnRouteRef")
class IClientVpnRouteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClientVpnRoute.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clientVpnRouteRef")
    def client_vpn_route_ref(self) -> "ClientVpnRouteReference":
        '''(experimental) A reference to a ClientVpnRoute resource.

        :stability: experimental
        '''
        ...


class _IClientVpnRouteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClientVpnRoute.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IClientVpnRouteRef"

    @builtins.property
    @jsii.member(jsii_name="clientVpnRouteRef")
    def client_vpn_route_ref(self) -> "ClientVpnRouteReference":
        '''(experimental) A reference to a ClientVpnRoute resource.

        :stability: experimental
        '''
        return typing.cast("ClientVpnRouteReference", jsii.get(self, "clientVpnRouteRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClientVpnRouteRef).__jsii_proxy_class__ = lambda : _IClientVpnRouteRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IClientVpnTargetNetworkAssociationRef"
)
class IClientVpnTargetNetworkAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClientVpnTargetNetworkAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clientVpnTargetNetworkAssociationRef")
    def client_vpn_target_network_association_ref(
        self,
    ) -> "ClientVpnTargetNetworkAssociationReference":
        '''(experimental) A reference to a ClientVpnTargetNetworkAssociation resource.

        :stability: experimental
        '''
        ...


class _IClientVpnTargetNetworkAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClientVpnTargetNetworkAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IClientVpnTargetNetworkAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="clientVpnTargetNetworkAssociationRef")
    def client_vpn_target_network_association_ref(
        self,
    ) -> "ClientVpnTargetNetworkAssociationReference":
        '''(experimental) A reference to a ClientVpnTargetNetworkAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ClientVpnTargetNetworkAssociationReference", jsii.get(self, "clientVpnTargetNetworkAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClientVpnTargetNetworkAssociationRef).__jsii_proxy_class__ = lambda : _IClientVpnTargetNetworkAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ICustomerGatewayRef")
class ICustomerGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomerGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customerGatewayRef")
    def customer_gateway_ref(self) -> "CustomerGatewayReference":
        '''(experimental) A reference to a CustomerGateway resource.

        :stability: experimental
        '''
        ...


class _ICustomerGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomerGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ICustomerGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="customerGatewayRef")
    def customer_gateway_ref(self) -> "CustomerGatewayReference":
        '''(experimental) A reference to a CustomerGateway resource.

        :stability: experimental
        '''
        return typing.cast("CustomerGatewayReference", jsii.get(self, "customerGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomerGatewayRef).__jsii_proxy_class__ = lambda : _ICustomerGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IDHCPOptionsRef")
class IDHCPOptionsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DHCPOptions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsRef")
    def dhcp_options_ref(self) -> "DHCPOptionsReference":
        '''(experimental) A reference to a DHCPOptions resource.

        :stability: experimental
        '''
        ...


class _IDHCPOptionsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DHCPOptions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IDHCPOptionsRef"

    @builtins.property
    @jsii.member(jsii_name="dhcpOptionsRef")
    def dhcp_options_ref(self) -> "DHCPOptionsReference":
        '''(experimental) A reference to a DHCPOptions resource.

        :stability: experimental
        '''
        return typing.cast("DHCPOptionsReference", jsii.get(self, "dhcpOptionsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDHCPOptionsRef).__jsii_proxy_class__ = lambda : _IDHCPOptionsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IEC2FleetRef")
class IEC2FleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EC2Fleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ec2FleetRef")
    def ec2_fleet_ref(self) -> "EC2FleetReference":
        '''(experimental) A reference to a EC2Fleet resource.

        :stability: experimental
        '''
        ...


class _IEC2FleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EC2Fleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IEC2FleetRef"

    @builtins.property
    @jsii.member(jsii_name="ec2FleetRef")
    def ec2_fleet_ref(self) -> "EC2FleetReference":
        '''(experimental) A reference to a EC2Fleet resource.

        :stability: experimental
        '''
        return typing.cast("EC2FleetReference", jsii.get(self, "ec2FleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEC2FleetRef).__jsii_proxy_class__ = lambda : _IEC2FleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IEIPAssociationRef")
class IEIPAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EIPAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eipAssociationRef")
    def eip_association_ref(self) -> "EIPAssociationReference":
        '''(experimental) A reference to a EIPAssociation resource.

        :stability: experimental
        '''
        ...


class _IEIPAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EIPAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IEIPAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="eipAssociationRef")
    def eip_association_ref(self) -> "EIPAssociationReference":
        '''(experimental) A reference to a EIPAssociation resource.

        :stability: experimental
        '''
        return typing.cast("EIPAssociationReference", jsii.get(self, "eipAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEIPAssociationRef).__jsii_proxy_class__ = lambda : _IEIPAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IEIPRef")
class IEIPRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EIP.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eipRef")
    def eip_ref(self) -> "EIPReference":
        '''(experimental) A reference to a EIP resource.

        :stability: experimental
        '''
        ...


class _IEIPRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EIP.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IEIPRef"

    @builtins.property
    @jsii.member(jsii_name="eipRef")
    def eip_ref(self) -> "EIPReference":
        '''(experimental) A reference to a EIP resource.

        :stability: experimental
        '''
        return typing.cast("EIPReference", jsii.get(self, "eipRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEIPRef).__jsii_proxy_class__ = lambda : _IEIPRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IEgressOnlyInternetGatewayRef"
)
class IEgressOnlyInternetGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EgressOnlyInternetGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="egressOnlyInternetGatewayRef")
    def egress_only_internet_gateway_ref(self) -> "EgressOnlyInternetGatewayReference":
        '''(experimental) A reference to a EgressOnlyInternetGateway resource.

        :stability: experimental
        '''
        ...


class _IEgressOnlyInternetGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EgressOnlyInternetGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IEgressOnlyInternetGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="egressOnlyInternetGatewayRef")
    def egress_only_internet_gateway_ref(self) -> "EgressOnlyInternetGatewayReference":
        '''(experimental) A reference to a EgressOnlyInternetGateway resource.

        :stability: experimental
        '''
        return typing.cast("EgressOnlyInternetGatewayReference", jsii.get(self, "egressOnlyInternetGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEgressOnlyInternetGatewayRef).__jsii_proxy_class__ = lambda : _IEgressOnlyInternetGatewayRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IEnclaveCertificateIamRoleAssociationRef"
)
class IEnclaveCertificateIamRoleAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EnclaveCertificateIamRoleAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="enclaveCertificateIamRoleAssociationRef")
    def enclave_certificate_iam_role_association_ref(
        self,
    ) -> "EnclaveCertificateIamRoleAssociationReference":
        '''(experimental) A reference to a EnclaveCertificateIamRoleAssociation resource.

        :stability: experimental
        '''
        ...


class _IEnclaveCertificateIamRoleAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EnclaveCertificateIamRoleAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IEnclaveCertificateIamRoleAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="enclaveCertificateIamRoleAssociationRef")
    def enclave_certificate_iam_role_association_ref(
        self,
    ) -> "EnclaveCertificateIamRoleAssociationReference":
        '''(experimental) A reference to a EnclaveCertificateIamRoleAssociation resource.

        :stability: experimental
        '''
        return typing.cast("EnclaveCertificateIamRoleAssociationReference", jsii.get(self, "enclaveCertificateIamRoleAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnclaveCertificateIamRoleAssociationRef).__jsii_proxy_class__ = lambda : _IEnclaveCertificateIamRoleAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IFlowLogRef")
class IFlowLogRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FlowLog.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowLogRef")
    def flow_log_ref(self) -> "FlowLogReference":
        '''(experimental) A reference to a FlowLog resource.

        :stability: experimental
        '''
        ...


class _IFlowLogRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FlowLog.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IFlowLogRef"

    @builtins.property
    @jsii.member(jsii_name="flowLogRef")
    def flow_log_ref(self) -> "FlowLogReference":
        '''(experimental) A reference to a FlowLog resource.

        :stability: experimental
        '''
        return typing.cast("FlowLogReference", jsii.get(self, "flowLogRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowLogRef).__jsii_proxy_class__ = lambda : _IFlowLogRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IGatewayRouteTableAssociationRef"
)
class IGatewayRouteTableAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GatewayRouteTableAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gatewayRouteTableAssociationRef")
    def gateway_route_table_association_ref(
        self,
    ) -> "GatewayRouteTableAssociationReference":
        '''(experimental) A reference to a GatewayRouteTableAssociation resource.

        :stability: experimental
        '''
        ...


class _IGatewayRouteTableAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GatewayRouteTableAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IGatewayRouteTableAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="gatewayRouteTableAssociationRef")
    def gateway_route_table_association_ref(
        self,
    ) -> "GatewayRouteTableAssociationReference":
        '''(experimental) A reference to a GatewayRouteTableAssociation resource.

        :stability: experimental
        '''
        return typing.cast("GatewayRouteTableAssociationReference", jsii.get(self, "gatewayRouteTableAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGatewayRouteTableAssociationRef).__jsii_proxy_class__ = lambda : _IGatewayRouteTableAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IHostRef")
class IHostRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Host.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hostRef")
    def host_ref(self) -> "HostReference":
        '''(experimental) A reference to a Host resource.

        :stability: experimental
        '''
        ...


class _IHostRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Host.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IHostRef"

    @builtins.property
    @jsii.member(jsii_name="hostRef")
    def host_ref(self) -> "HostReference":
        '''(experimental) A reference to a Host resource.

        :stability: experimental
        '''
        return typing.cast("HostReference", jsii.get(self, "hostRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHostRef).__jsii_proxy_class__ = lambda : _IHostRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IIPAMAllocationRef")
class IIPAMAllocationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMAllocation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipamAllocationRef")
    def ipam_allocation_ref(self) -> "IPAMAllocationReference":
        '''(experimental) A reference to a IPAMAllocation resource.

        :stability: experimental
        '''
        ...


class _IIPAMAllocationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMAllocation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IIPAMAllocationRef"

    @builtins.property
    @jsii.member(jsii_name="ipamAllocationRef")
    def ipam_allocation_ref(self) -> "IPAMAllocationReference":
        '''(experimental) A reference to a IPAMAllocation resource.

        :stability: experimental
        '''
        return typing.cast("IPAMAllocationReference", jsii.get(self, "ipamAllocationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPAMAllocationRef).__jsii_proxy_class__ = lambda : _IIPAMAllocationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IIPAMPoolCidrRef")
class IIPAMPoolCidrRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMPoolCidr.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipamPoolCidrRef")
    def ipam_pool_cidr_ref(self) -> "IPAMPoolCidrReference":
        '''(experimental) A reference to a IPAMPoolCidr resource.

        :stability: experimental
        '''
        ...


class _IIPAMPoolCidrRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMPoolCidr.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IIPAMPoolCidrRef"

    @builtins.property
    @jsii.member(jsii_name="ipamPoolCidrRef")
    def ipam_pool_cidr_ref(self) -> "IPAMPoolCidrReference":
        '''(experimental) A reference to a IPAMPoolCidr resource.

        :stability: experimental
        '''
        return typing.cast("IPAMPoolCidrReference", jsii.get(self, "ipamPoolCidrRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPAMPoolCidrRef).__jsii_proxy_class__ = lambda : _IIPAMPoolCidrRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IIPAMPoolRef")
class IIPAMPoolRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMPool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipamPoolRef")
    def ipam_pool_ref(self) -> "IPAMPoolReference":
        '''(experimental) A reference to a IPAMPool resource.

        :stability: experimental
        '''
        ...


class _IIPAMPoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMPool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IIPAMPoolRef"

    @builtins.property
    @jsii.member(jsii_name="ipamPoolRef")
    def ipam_pool_ref(self) -> "IPAMPoolReference":
        '''(experimental) A reference to a IPAMPool resource.

        :stability: experimental
        '''
        return typing.cast("IPAMPoolReference", jsii.get(self, "ipamPoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPAMPoolRef).__jsii_proxy_class__ = lambda : _IIPAMPoolRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IIPAMPrefixListResolverRef")
class IIPAMPrefixListResolverRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMPrefixListResolver.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipamPrefixListResolverRef")
    def ipam_prefix_list_resolver_ref(self) -> "IPAMPrefixListResolverReference":
        '''(experimental) A reference to a IPAMPrefixListResolver resource.

        :stability: experimental
        '''
        ...


class _IIPAMPrefixListResolverRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMPrefixListResolver.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IIPAMPrefixListResolverRef"

    @builtins.property
    @jsii.member(jsii_name="ipamPrefixListResolverRef")
    def ipam_prefix_list_resolver_ref(self) -> "IPAMPrefixListResolverReference":
        '''(experimental) A reference to a IPAMPrefixListResolver resource.

        :stability: experimental
        '''
        return typing.cast("IPAMPrefixListResolverReference", jsii.get(self, "ipamPrefixListResolverRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPAMPrefixListResolverRef).__jsii_proxy_class__ = lambda : _IIPAMPrefixListResolverRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IIPAMRef")
class IIPAMRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPAM.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipamRef")
    def ipam_ref(self) -> "IPAMReference":
        '''(experimental) A reference to a IPAM resource.

        :stability: experimental
        '''
        ...


class _IIPAMRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPAM.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IIPAMRef"

    @builtins.property
    @jsii.member(jsii_name="ipamRef")
    def ipam_ref(self) -> "IPAMReference":
        '''(experimental) A reference to a IPAM resource.

        :stability: experimental
        '''
        return typing.cast("IPAMReference", jsii.get(self, "ipamRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPAMRef).__jsii_proxy_class__ = lambda : _IIPAMRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IIPAMResourceDiscoveryAssociationRef"
)
class IIPAMResourceDiscoveryAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMResourceDiscoveryAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipamResourceDiscoveryAssociationRef")
    def ipam_resource_discovery_association_ref(
        self,
    ) -> "IPAMResourceDiscoveryAssociationReference":
        '''(experimental) A reference to a IPAMResourceDiscoveryAssociation resource.

        :stability: experimental
        '''
        ...


class _IIPAMResourceDiscoveryAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMResourceDiscoveryAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IIPAMResourceDiscoveryAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="ipamResourceDiscoveryAssociationRef")
    def ipam_resource_discovery_association_ref(
        self,
    ) -> "IPAMResourceDiscoveryAssociationReference":
        '''(experimental) A reference to a IPAMResourceDiscoveryAssociation resource.

        :stability: experimental
        '''
        return typing.cast("IPAMResourceDiscoveryAssociationReference", jsii.get(self, "ipamResourceDiscoveryAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPAMResourceDiscoveryAssociationRef).__jsii_proxy_class__ = lambda : _IIPAMResourceDiscoveryAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IIPAMResourceDiscoveryRef")
class IIPAMResourceDiscoveryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMResourceDiscovery.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipamResourceDiscoveryRef")
    def ipam_resource_discovery_ref(self) -> "IPAMResourceDiscoveryReference":
        '''(experimental) A reference to a IPAMResourceDiscovery resource.

        :stability: experimental
        '''
        ...


class _IIPAMResourceDiscoveryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMResourceDiscovery.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IIPAMResourceDiscoveryRef"

    @builtins.property
    @jsii.member(jsii_name="ipamResourceDiscoveryRef")
    def ipam_resource_discovery_ref(self) -> "IPAMResourceDiscoveryReference":
        '''(experimental) A reference to a IPAMResourceDiscovery resource.

        :stability: experimental
        '''
        return typing.cast("IPAMResourceDiscoveryReference", jsii.get(self, "ipamResourceDiscoveryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPAMResourceDiscoveryRef).__jsii_proxy_class__ = lambda : _IIPAMResourceDiscoveryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IIPAMScopeRef")
class IIPAMScopeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMScope.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipamScopeRef")
    def ipam_scope_ref(self) -> "IPAMScopeReference":
        '''(experimental) A reference to a IPAMScope resource.

        :stability: experimental
        '''
        ...


class _IIPAMScopeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPAMScope.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IIPAMScopeRef"

    @builtins.property
    @jsii.member(jsii_name="ipamScopeRef")
    def ipam_scope_ref(self) -> "IPAMScopeReference":
        '''(experimental) A reference to a IPAMScope resource.

        :stability: experimental
        '''
        return typing.cast("IPAMScopeReference", jsii.get(self, "ipamScopeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPAMScopeRef).__jsii_proxy_class__ = lambda : _IIPAMScopeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IInstanceConnectEndpointRef")
class IInstanceConnectEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceConnectEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceConnectEndpointRef")
    def instance_connect_endpoint_ref(self) -> "InstanceConnectEndpointReference":
        '''(experimental) A reference to a InstanceConnectEndpoint resource.

        :stability: experimental
        '''
        ...


class _IInstanceConnectEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceConnectEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IInstanceConnectEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="instanceConnectEndpointRef")
    def instance_connect_endpoint_ref(self) -> "InstanceConnectEndpointReference":
        '''(experimental) A reference to a InstanceConnectEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("InstanceConnectEndpointReference", jsii.get(self, "instanceConnectEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceConnectEndpointRef).__jsii_proxy_class__ = lambda : _IInstanceConnectEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IInstanceRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="instanceRef")
    def instance_ref(self) -> "InstanceReference":
        '''(experimental) A reference to a Instance resource.

        :stability: experimental
        '''
        return typing.cast("InstanceReference", jsii.get(self, "instanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceRef).__jsii_proxy_class__ = lambda : _IInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IInternetGatewayRef")
class IInternetGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InternetGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="internetGatewayRef")
    def internet_gateway_ref(self) -> "InternetGatewayReference":
        '''(experimental) A reference to a InternetGateway resource.

        :stability: experimental
        '''
        ...


class _IInternetGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InternetGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IInternetGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="internetGatewayRef")
    def internet_gateway_ref(self) -> "InternetGatewayReference":
        '''(experimental) A reference to a InternetGateway resource.

        :stability: experimental
        '''
        return typing.cast("InternetGatewayReference", jsii.get(self, "internetGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInternetGatewayRef).__jsii_proxy_class__ = lambda : _IInternetGatewayRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IIpPoolRouteTableAssociationRef"
)
class IIpPoolRouteTableAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IpPoolRouteTableAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipPoolRouteTableAssociationRef")
    def ip_pool_route_table_association_ref(
        self,
    ) -> "IpPoolRouteTableAssociationReference":
        '''(experimental) A reference to a IpPoolRouteTableAssociation resource.

        :stability: experimental
        '''
        ...


class _IIpPoolRouteTableAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IpPoolRouteTableAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IIpPoolRouteTableAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="ipPoolRouteTableAssociationRef")
    def ip_pool_route_table_association_ref(
        self,
    ) -> "IpPoolRouteTableAssociationReference":
        '''(experimental) A reference to a IpPoolRouteTableAssociation resource.

        :stability: experimental
        '''
        return typing.cast("IpPoolRouteTableAssociationReference", jsii.get(self, "ipPoolRouteTableAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIpPoolRouteTableAssociationRef).__jsii_proxy_class__ = lambda : _IIpPoolRouteTableAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IKeyPairRef")
class IKeyPairRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a KeyPair.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="keyPairRef")
    def key_pair_ref(self) -> "KeyPairReference":
        '''(experimental) A reference to a KeyPair resource.

        :stability: experimental
        '''
        ...


class _IKeyPairRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a KeyPair.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IKeyPairRef"

    @builtins.property
    @jsii.member(jsii_name="keyPairRef")
    def key_pair_ref(self) -> "KeyPairReference":
        '''(experimental) A reference to a KeyPair resource.

        :stability: experimental
        '''
        return typing.cast("KeyPairReference", jsii.get(self, "keyPairRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKeyPairRef).__jsii_proxy_class__ = lambda : _IKeyPairRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ILaunchTemplateRef")
class ILaunchTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="launchTemplateRef")
    def launch_template_ref(self) -> "LaunchTemplateReference":
        '''(experimental) A reference to a LaunchTemplate resource.

        :stability: experimental
        '''
        ...


class _ILaunchTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ILaunchTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="launchTemplateRef")
    def launch_template_ref(self) -> "LaunchTemplateReference":
        '''(experimental) A reference to a LaunchTemplate resource.

        :stability: experimental
        '''
        return typing.cast("LaunchTemplateReference", jsii.get(self, "launchTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILaunchTemplateRef).__jsii_proxy_class__ = lambda : _ILaunchTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayRouteRef")
class ILocalGatewayRouteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayRoute.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="localGatewayRouteRef")
    def local_gateway_route_ref(self) -> "LocalGatewayRouteReference":
        '''(experimental) A reference to a LocalGatewayRoute resource.

        :stability: experimental
        '''
        ...


class _ILocalGatewayRouteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayRoute.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayRouteRef"

    @builtins.property
    @jsii.member(jsii_name="localGatewayRouteRef")
    def local_gateway_route_ref(self) -> "LocalGatewayRouteReference":
        '''(experimental) A reference to a LocalGatewayRoute resource.

        :stability: experimental
        '''
        return typing.cast("LocalGatewayRouteReference", jsii.get(self, "localGatewayRouteRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocalGatewayRouteRef).__jsii_proxy_class__ = lambda : _ILocalGatewayRouteRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayRouteTableRef")
class ILocalGatewayRouteTableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayRouteTable.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="localGatewayRouteTableRef")
    def local_gateway_route_table_ref(self) -> "LocalGatewayRouteTableReference":
        '''(experimental) A reference to a LocalGatewayRouteTable resource.

        :stability: experimental
        '''
        ...


class _ILocalGatewayRouteTableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayRouteTable.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayRouteTableRef"

    @builtins.property
    @jsii.member(jsii_name="localGatewayRouteTableRef")
    def local_gateway_route_table_ref(self) -> "LocalGatewayRouteTableReference":
        '''(experimental) A reference to a LocalGatewayRouteTable resource.

        :stability: experimental
        '''
        return typing.cast("LocalGatewayRouteTableReference", jsii.get(self, "localGatewayRouteTableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocalGatewayRouteTableRef).__jsii_proxy_class__ = lambda : _ILocalGatewayRouteTableRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayRouteTableVPCAssociationRef"
)
class ILocalGatewayRouteTableVPCAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayRouteTableVPCAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="localGatewayRouteTableVpcAssociationRef")
    def local_gateway_route_table_vpc_association_ref(
        self,
    ) -> "LocalGatewayRouteTableVPCAssociationReference":
        '''(experimental) A reference to a LocalGatewayRouteTableVPCAssociation resource.

        :stability: experimental
        '''
        ...


class _ILocalGatewayRouteTableVPCAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayRouteTableVPCAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayRouteTableVPCAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="localGatewayRouteTableVpcAssociationRef")
    def local_gateway_route_table_vpc_association_ref(
        self,
    ) -> "LocalGatewayRouteTableVPCAssociationReference":
        '''(experimental) A reference to a LocalGatewayRouteTableVPCAssociation resource.

        :stability: experimental
        '''
        return typing.cast("LocalGatewayRouteTableVPCAssociationReference", jsii.get(self, "localGatewayRouteTableVpcAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocalGatewayRouteTableVPCAssociationRef).__jsii_proxy_class__ = lambda : _ILocalGatewayRouteTableVPCAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayRouteTableVirtualInterfaceGroupAssociationRef"
)
class ILocalGatewayRouteTableVirtualInterfaceGroupAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayRouteTableVirtualInterfaceGroupAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="localGatewayRouteTableVirtualInterfaceGroupAssociationRef")
    def local_gateway_route_table_virtual_interface_group_association_ref(
        self,
    ) -> "LocalGatewayRouteTableVirtualInterfaceGroupAssociationReference":
        '''(experimental) A reference to a LocalGatewayRouteTableVirtualInterfaceGroupAssociation resource.

        :stability: experimental
        '''
        ...


class _ILocalGatewayRouteTableVirtualInterfaceGroupAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayRouteTableVirtualInterfaceGroupAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayRouteTableVirtualInterfaceGroupAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="localGatewayRouteTableVirtualInterfaceGroupAssociationRef")
    def local_gateway_route_table_virtual_interface_group_association_ref(
        self,
    ) -> "LocalGatewayRouteTableVirtualInterfaceGroupAssociationReference":
        '''(experimental) A reference to a LocalGatewayRouteTableVirtualInterfaceGroupAssociation resource.

        :stability: experimental
        '''
        return typing.cast("LocalGatewayRouteTableVirtualInterfaceGroupAssociationReference", jsii.get(self, "localGatewayRouteTableVirtualInterfaceGroupAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocalGatewayRouteTableVirtualInterfaceGroupAssociationRef).__jsii_proxy_class__ = lambda : _ILocalGatewayRouteTableVirtualInterfaceGroupAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayVirtualInterfaceGroupRef"
)
class ILocalGatewayVirtualInterfaceGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayVirtualInterfaceGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="localGatewayVirtualInterfaceGroupRef")
    def local_gateway_virtual_interface_group_ref(
        self,
    ) -> "LocalGatewayVirtualInterfaceGroupReference":
        '''(experimental) A reference to a LocalGatewayVirtualInterfaceGroup resource.

        :stability: experimental
        '''
        ...


class _ILocalGatewayVirtualInterfaceGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayVirtualInterfaceGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayVirtualInterfaceGroupRef"

    @builtins.property
    @jsii.member(jsii_name="localGatewayVirtualInterfaceGroupRef")
    def local_gateway_virtual_interface_group_ref(
        self,
    ) -> "LocalGatewayVirtualInterfaceGroupReference":
        '''(experimental) A reference to a LocalGatewayVirtualInterfaceGroup resource.

        :stability: experimental
        '''
        return typing.cast("LocalGatewayVirtualInterfaceGroupReference", jsii.get(self, "localGatewayVirtualInterfaceGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocalGatewayVirtualInterfaceGroupRef).__jsii_proxy_class__ = lambda : _ILocalGatewayVirtualInterfaceGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayVirtualInterfaceRef"
)
class ILocalGatewayVirtualInterfaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayVirtualInterface.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="localGatewayVirtualInterfaceRef")
    def local_gateway_virtual_interface_ref(
        self,
    ) -> "LocalGatewayVirtualInterfaceReference":
        '''(experimental) A reference to a LocalGatewayVirtualInterface resource.

        :stability: experimental
        '''
        ...


class _ILocalGatewayVirtualInterfaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LocalGatewayVirtualInterface.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ILocalGatewayVirtualInterfaceRef"

    @builtins.property
    @jsii.member(jsii_name="localGatewayVirtualInterfaceRef")
    def local_gateway_virtual_interface_ref(
        self,
    ) -> "LocalGatewayVirtualInterfaceReference":
        '''(experimental) A reference to a LocalGatewayVirtualInterface resource.

        :stability: experimental
        '''
        return typing.cast("LocalGatewayVirtualInterfaceReference", jsii.get(self, "localGatewayVirtualInterfaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocalGatewayVirtualInterfaceRef).__jsii_proxy_class__ = lambda : _ILocalGatewayVirtualInterfaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.INatGatewayRef")
class INatGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NatGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="natGatewayRef")
    def nat_gateway_ref(self) -> "NatGatewayReference":
        '''(experimental) A reference to a NatGateway resource.

        :stability: experimental
        '''
        ...


class _INatGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NatGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INatGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="natGatewayRef")
    def nat_gateway_ref(self) -> "NatGatewayReference":
        '''(experimental) A reference to a NatGateway resource.

        :stability: experimental
        '''
        return typing.cast("NatGatewayReference", jsii.get(self, "natGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INatGatewayRef).__jsii_proxy_class__ = lambda : _INatGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkAclEntryRef")
class INetworkAclEntryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkAclEntry.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkAclEntryRef")
    def network_acl_entry_ref(self) -> "NetworkAclEntryReference":
        '''(experimental) A reference to a NetworkAclEntry resource.

        :stability: experimental
        '''
        ...


class _INetworkAclEntryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkAclEntry.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkAclEntryRef"

    @builtins.property
    @jsii.member(jsii_name="networkAclEntryRef")
    def network_acl_entry_ref(self) -> "NetworkAclEntryReference":
        '''(experimental) A reference to a NetworkAclEntry resource.

        :stability: experimental
        '''
        return typing.cast("NetworkAclEntryReference", jsii.get(self, "networkAclEntryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkAclEntryRef).__jsii_proxy_class__ = lambda : _INetworkAclEntryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkAclRef")
class INetworkAclRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkAcl.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkAclRef")
    def network_acl_ref(self) -> "NetworkAclReference":
        '''(experimental) A reference to a NetworkAcl resource.

        :stability: experimental
        '''
        ...


class _INetworkAclRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkAcl.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkAclRef"

    @builtins.property
    @jsii.member(jsii_name="networkAclRef")
    def network_acl_ref(self) -> "NetworkAclReference":
        '''(experimental) A reference to a NetworkAcl resource.

        :stability: experimental
        '''
        return typing.cast("NetworkAclReference", jsii.get(self, "networkAclRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkAclRef).__jsii_proxy_class__ = lambda : _INetworkAclRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkInsightsAccessScopeAnalysisRef"
)
class INetworkInsightsAccessScopeAnalysisRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInsightsAccessScopeAnalysis.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkInsightsAccessScopeAnalysisRef")
    def network_insights_access_scope_analysis_ref(
        self,
    ) -> "NetworkInsightsAccessScopeAnalysisReference":
        '''(experimental) A reference to a NetworkInsightsAccessScopeAnalysis resource.

        :stability: experimental
        '''
        ...


class _INetworkInsightsAccessScopeAnalysisRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInsightsAccessScopeAnalysis.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkInsightsAccessScopeAnalysisRef"

    @builtins.property
    @jsii.member(jsii_name="networkInsightsAccessScopeAnalysisRef")
    def network_insights_access_scope_analysis_ref(
        self,
    ) -> "NetworkInsightsAccessScopeAnalysisReference":
        '''(experimental) A reference to a NetworkInsightsAccessScopeAnalysis resource.

        :stability: experimental
        '''
        return typing.cast("NetworkInsightsAccessScopeAnalysisReference", jsii.get(self, "networkInsightsAccessScopeAnalysisRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkInsightsAccessScopeAnalysisRef).__jsii_proxy_class__ = lambda : _INetworkInsightsAccessScopeAnalysisRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkInsightsAccessScopeRef"
)
class INetworkInsightsAccessScopeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInsightsAccessScope.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkInsightsAccessScopeRef")
    def network_insights_access_scope_ref(
        self,
    ) -> "NetworkInsightsAccessScopeReference":
        '''(experimental) A reference to a NetworkInsightsAccessScope resource.

        :stability: experimental
        '''
        ...


class _INetworkInsightsAccessScopeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInsightsAccessScope.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkInsightsAccessScopeRef"

    @builtins.property
    @jsii.member(jsii_name="networkInsightsAccessScopeRef")
    def network_insights_access_scope_ref(
        self,
    ) -> "NetworkInsightsAccessScopeReference":
        '''(experimental) A reference to a NetworkInsightsAccessScope resource.

        :stability: experimental
        '''
        return typing.cast("NetworkInsightsAccessScopeReference", jsii.get(self, "networkInsightsAccessScopeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkInsightsAccessScopeRef).__jsii_proxy_class__ = lambda : _INetworkInsightsAccessScopeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkInsightsAnalysisRef")
class INetworkInsightsAnalysisRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInsightsAnalysis.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkInsightsAnalysisRef")
    def network_insights_analysis_ref(self) -> "NetworkInsightsAnalysisReference":
        '''(experimental) A reference to a NetworkInsightsAnalysis resource.

        :stability: experimental
        '''
        ...


class _INetworkInsightsAnalysisRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInsightsAnalysis.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkInsightsAnalysisRef"

    @builtins.property
    @jsii.member(jsii_name="networkInsightsAnalysisRef")
    def network_insights_analysis_ref(self) -> "NetworkInsightsAnalysisReference":
        '''(experimental) A reference to a NetworkInsightsAnalysis resource.

        :stability: experimental
        '''
        return typing.cast("NetworkInsightsAnalysisReference", jsii.get(self, "networkInsightsAnalysisRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkInsightsAnalysisRef).__jsii_proxy_class__ = lambda : _INetworkInsightsAnalysisRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkInsightsPathRef")
class INetworkInsightsPathRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInsightsPath.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkInsightsPathRef")
    def network_insights_path_ref(self) -> "NetworkInsightsPathReference":
        '''(experimental) A reference to a NetworkInsightsPath resource.

        :stability: experimental
        '''
        ...


class _INetworkInsightsPathRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInsightsPath.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkInsightsPathRef"

    @builtins.property
    @jsii.member(jsii_name="networkInsightsPathRef")
    def network_insights_path_ref(self) -> "NetworkInsightsPathReference":
        '''(experimental) A reference to a NetworkInsightsPath resource.

        :stability: experimental
        '''
        return typing.cast("NetworkInsightsPathReference", jsii.get(self, "networkInsightsPathRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkInsightsPathRef).__jsii_proxy_class__ = lambda : _INetworkInsightsPathRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkInterfaceAttachmentRef"
)
class INetworkInterfaceAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInterfaceAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceAttachmentRef")
    def network_interface_attachment_ref(self) -> "NetworkInterfaceAttachmentReference":
        '''(experimental) A reference to a NetworkInterfaceAttachment resource.

        :stability: experimental
        '''
        ...


class _INetworkInterfaceAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInterfaceAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkInterfaceAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceAttachmentRef")
    def network_interface_attachment_ref(self) -> "NetworkInterfaceAttachmentReference":
        '''(experimental) A reference to a NetworkInterfaceAttachment resource.

        :stability: experimental
        '''
        return typing.cast("NetworkInterfaceAttachmentReference", jsii.get(self, "networkInterfaceAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkInterfaceAttachmentRef).__jsii_proxy_class__ = lambda : _INetworkInterfaceAttachmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkInterfacePermissionRef"
)
class INetworkInterfacePermissionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInterfacePermission.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkInterfacePermissionRef")
    def network_interface_permission_ref(self) -> "NetworkInterfacePermissionReference":
        '''(experimental) A reference to a NetworkInterfacePermission resource.

        :stability: experimental
        '''
        ...


class _INetworkInterfacePermissionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInterfacePermission.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkInterfacePermissionRef"

    @builtins.property
    @jsii.member(jsii_name="networkInterfacePermissionRef")
    def network_interface_permission_ref(self) -> "NetworkInterfacePermissionReference":
        '''(experimental) A reference to a NetworkInterfacePermission resource.

        :stability: experimental
        '''
        return typing.cast("NetworkInterfacePermissionReference", jsii.get(self, "networkInterfacePermissionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkInterfacePermissionRef).__jsii_proxy_class__ = lambda : _INetworkInterfacePermissionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkInterfaceRef")
class INetworkInterfaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInterface.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceRef")
    def network_interface_ref(self) -> "NetworkInterfaceReference":
        '''(experimental) A reference to a NetworkInterface resource.

        :stability: experimental
        '''
        ...


class _INetworkInterfaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkInterface.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkInterfaceRef"

    @builtins.property
    @jsii.member(jsii_name="networkInterfaceRef")
    def network_interface_ref(self) -> "NetworkInterfaceReference":
        '''(experimental) A reference to a NetworkInterface resource.

        :stability: experimental
        '''
        return typing.cast("NetworkInterfaceReference", jsii.get(self, "networkInterfaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkInterfaceRef).__jsii_proxy_class__ = lambda : _INetworkInterfaceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.INetworkPerformanceMetricSubscriptionRef"
)
class INetworkPerformanceMetricSubscriptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkPerformanceMetricSubscription.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkPerformanceMetricSubscriptionRef")
    def network_performance_metric_subscription_ref(
        self,
    ) -> "NetworkPerformanceMetricSubscriptionReference":
        '''(experimental) A reference to a NetworkPerformanceMetricSubscription resource.

        :stability: experimental
        '''
        ...


class _INetworkPerformanceMetricSubscriptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkPerformanceMetricSubscription.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.INetworkPerformanceMetricSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="networkPerformanceMetricSubscriptionRef")
    def network_performance_metric_subscription_ref(
        self,
    ) -> "NetworkPerformanceMetricSubscriptionReference":
        '''(experimental) A reference to a NetworkPerformanceMetricSubscription resource.

        :stability: experimental
        '''
        return typing.cast("NetworkPerformanceMetricSubscriptionReference", jsii.get(self, "networkPerformanceMetricSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkPerformanceMetricSubscriptionRef).__jsii_proxy_class__ = lambda : _INetworkPerformanceMetricSubscriptionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPAMAllocationReference",
    jsii_struct_bases=[],
    name_mapping={
        "cidr": "cidr",
        "ipam_pool_allocation_id": "ipamPoolAllocationId",
        "ipam_pool_id": "ipamPoolId",
    },
)
class IPAMAllocationReference:
    def __init__(
        self,
        *,
        cidr: builtins.str,
        ipam_pool_allocation_id: builtins.str,
        ipam_pool_id: builtins.str,
    ) -> None:
        '''A reference to a IPAMAllocation resource.

        :param cidr: The Cidr of the IPAMAllocation resource.
        :param ipam_pool_allocation_id: The IpamPoolAllocationId of the IPAMAllocation resource.
        :param ipam_pool_id: The IpamPoolId of the IPAMAllocation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            i_pAMAllocation_reference = {
                "cidr": "cidr",
                "ipam_pool_allocation_id": "ipamPoolAllocationId",
                "ipam_pool_id": "ipamPoolId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7feb4439f565248f1d51f179a7e018bb0fb9c2a8a48ea0d41c27aed11307ea75)
            check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            check_type(argname="argument ipam_pool_allocation_id", value=ipam_pool_allocation_id, expected_type=type_hints["ipam_pool_allocation_id"])
            check_type(argname="argument ipam_pool_id", value=ipam_pool_id, expected_type=type_hints["ipam_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidr": cidr,
            "ipam_pool_allocation_id": ipam_pool_allocation_id,
            "ipam_pool_id": ipam_pool_id,
        }

    @builtins.property
    def cidr(self) -> builtins.str:
        '''The Cidr of the IPAMAllocation resource.'''
        result = self._values.get("cidr")
        assert result is not None, "Required property 'cidr' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_pool_allocation_id(self) -> builtins.str:
        '''The IpamPoolAllocationId of the IPAMAllocation resource.'''
        result = self._values.get("ipam_pool_allocation_id")
        assert result is not None, "Required property 'ipam_pool_allocation_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_pool_id(self) -> builtins.str:
        '''The IpamPoolId of the IPAMAllocation resource.'''
        result = self._values.get("ipam_pool_id")
        assert result is not None, "Required property 'ipam_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPAMAllocationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPAMPoolCidrReference",
    jsii_struct_bases=[],
    name_mapping={"ipam_pool_cidr_id": "ipamPoolCidrId", "ipam_pool_id": "ipamPoolId"},
)
class IPAMPoolCidrReference:
    def __init__(
        self,
        *,
        ipam_pool_cidr_id: builtins.str,
        ipam_pool_id: builtins.str,
    ) -> None:
        '''A reference to a IPAMPoolCidr resource.

        :param ipam_pool_cidr_id: The IpamPoolCidrId of the IPAMPoolCidr resource.
        :param ipam_pool_id: The IpamPoolId of the IPAMPoolCidr resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            i_pAMPool_cidr_reference = {
                "ipam_pool_cidr_id": "ipamPoolCidrId",
                "ipam_pool_id": "ipamPoolId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3683b95716ecb232814e443e685b635edbf9643420649ae07689e14b51dfcc17)
            check_type(argname="argument ipam_pool_cidr_id", value=ipam_pool_cidr_id, expected_type=type_hints["ipam_pool_cidr_id"])
            check_type(argname="argument ipam_pool_id", value=ipam_pool_id, expected_type=type_hints["ipam_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ipam_pool_cidr_id": ipam_pool_cidr_id,
            "ipam_pool_id": ipam_pool_id,
        }

    @builtins.property
    def ipam_pool_cidr_id(self) -> builtins.str:
        '''The IpamPoolCidrId of the IPAMPoolCidr resource.'''
        result = self._values.get("ipam_pool_cidr_id")
        assert result is not None, "Required property 'ipam_pool_cidr_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_pool_id(self) -> builtins.str:
        '''The IpamPoolId of the IPAMPoolCidr resource.'''
        result = self._values.get("ipam_pool_id")
        assert result is not None, "Required property 'ipam_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPAMPoolCidrReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPAMPoolReference",
    jsii_struct_bases=[],
    name_mapping={"ipam_pool_arn": "ipamPoolArn", "ipam_pool_id": "ipamPoolId"},
)
class IPAMPoolReference:
    def __init__(
        self,
        *,
        ipam_pool_arn: builtins.str,
        ipam_pool_id: builtins.str,
    ) -> None:
        '''A reference to a IPAMPool resource.

        :param ipam_pool_arn: The ARN of the IPAMPool resource.
        :param ipam_pool_id: The IpamPoolId of the IPAMPool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            i_pAMPool_reference = {
                "ipam_pool_arn": "ipamPoolArn",
                "ipam_pool_id": "ipamPoolId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54638f34ae06307f1bc4313c2916619169655bbba473fe8a9c1bc2378c38dbc8)
            check_type(argname="argument ipam_pool_arn", value=ipam_pool_arn, expected_type=type_hints["ipam_pool_arn"])
            check_type(argname="argument ipam_pool_id", value=ipam_pool_id, expected_type=type_hints["ipam_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ipam_pool_arn": ipam_pool_arn,
            "ipam_pool_id": ipam_pool_id,
        }

    @builtins.property
    def ipam_pool_arn(self) -> builtins.str:
        '''The ARN of the IPAMPool resource.'''
        result = self._values.get("ipam_pool_arn")
        assert result is not None, "Required property 'ipam_pool_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_pool_id(self) -> builtins.str:
        '''The IpamPoolId of the IPAMPool resource.'''
        result = self._values.get("ipam_pool_id")
        assert result is not None, "Required property 'ipam_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPAMPoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPAMPrefixListResolverReference",
    jsii_struct_bases=[],
    name_mapping={
        "ipam_prefix_list_resolver_arn": "ipamPrefixListResolverArn",
        "ipam_prefix_list_resolver_id": "ipamPrefixListResolverId",
    },
)
class IPAMPrefixListResolverReference:
    def __init__(
        self,
        *,
        ipam_prefix_list_resolver_arn: builtins.str,
        ipam_prefix_list_resolver_id: builtins.str,
    ) -> None:
        '''A reference to a IPAMPrefixListResolver resource.

        :param ipam_prefix_list_resolver_arn: The ARN of the IPAMPrefixListResolver resource.
        :param ipam_prefix_list_resolver_id: The IpamPrefixListResolverId of the IPAMPrefixListResolver resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            i_pAMPrefix_list_resolver_reference = {
                "ipam_prefix_list_resolver_arn": "ipamPrefixListResolverArn",
                "ipam_prefix_list_resolver_id": "ipamPrefixListResolverId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ac17af28aa1061e001efd103ab675ccb82fc60c97079265f5fdddbcde5fdd3)
            check_type(argname="argument ipam_prefix_list_resolver_arn", value=ipam_prefix_list_resolver_arn, expected_type=type_hints["ipam_prefix_list_resolver_arn"])
            check_type(argname="argument ipam_prefix_list_resolver_id", value=ipam_prefix_list_resolver_id, expected_type=type_hints["ipam_prefix_list_resolver_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ipam_prefix_list_resolver_arn": ipam_prefix_list_resolver_arn,
            "ipam_prefix_list_resolver_id": ipam_prefix_list_resolver_id,
        }

    @builtins.property
    def ipam_prefix_list_resolver_arn(self) -> builtins.str:
        '''The ARN of the IPAMPrefixListResolver resource.'''
        result = self._values.get("ipam_prefix_list_resolver_arn")
        assert result is not None, "Required property 'ipam_prefix_list_resolver_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_prefix_list_resolver_id(self) -> builtins.str:
        '''The IpamPrefixListResolverId of the IPAMPrefixListResolver resource.'''
        result = self._values.get("ipam_prefix_list_resolver_id")
        assert result is not None, "Required property 'ipam_prefix_list_resolver_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPAMPrefixListResolverReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPAMReference",
    jsii_struct_bases=[],
    name_mapping={"ipam_arn": "ipamArn", "ipam_id": "ipamId"},
)
class IPAMReference:
    def __init__(self, *, ipam_arn: builtins.str, ipam_id: builtins.str) -> None:
        '''A reference to a IPAM resource.

        :param ipam_arn: The ARN of the IPAM resource.
        :param ipam_id: The IpamId of the IPAM resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            i_pAMReference = {
                "ipam_arn": "ipamArn",
                "ipam_id": "ipamId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4b18eb7f984a38a0d1b97de048402fd4bff3a9c791619a68aa7bba3b69b606c)
            check_type(argname="argument ipam_arn", value=ipam_arn, expected_type=type_hints["ipam_arn"])
            check_type(argname="argument ipam_id", value=ipam_id, expected_type=type_hints["ipam_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ipam_arn": ipam_arn,
            "ipam_id": ipam_id,
        }

    @builtins.property
    def ipam_arn(self) -> builtins.str:
        '''The ARN of the IPAM resource.'''
        result = self._values.get("ipam_arn")
        assert result is not None, "Required property 'ipam_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_id(self) -> builtins.str:
        '''The IpamId of the IPAM resource.'''
        result = self._values.get("ipam_id")
        assert result is not None, "Required property 'ipam_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPAMReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPAMResourceDiscoveryAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "ipam_resource_discovery_association_arn": "ipamResourceDiscoveryAssociationArn",
        "ipam_resource_discovery_association_id": "ipamResourceDiscoveryAssociationId",
    },
)
class IPAMResourceDiscoveryAssociationReference:
    def __init__(
        self,
        *,
        ipam_resource_discovery_association_arn: builtins.str,
        ipam_resource_discovery_association_id: builtins.str,
    ) -> None:
        '''A reference to a IPAMResourceDiscoveryAssociation resource.

        :param ipam_resource_discovery_association_arn: The ARN of the IPAMResourceDiscoveryAssociation resource.
        :param ipam_resource_discovery_association_id: The IpamResourceDiscoveryAssociationId of the IPAMResourceDiscoveryAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            i_pAMResource_discovery_association_reference = {
                "ipam_resource_discovery_association_arn": "ipamResourceDiscoveryAssociationArn",
                "ipam_resource_discovery_association_id": "ipamResourceDiscoveryAssociationId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adc737e46a3649729021f88f43561d31e8fdcefc112469a6222d8a7681574227)
            check_type(argname="argument ipam_resource_discovery_association_arn", value=ipam_resource_discovery_association_arn, expected_type=type_hints["ipam_resource_discovery_association_arn"])
            check_type(argname="argument ipam_resource_discovery_association_id", value=ipam_resource_discovery_association_id, expected_type=type_hints["ipam_resource_discovery_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ipam_resource_discovery_association_arn": ipam_resource_discovery_association_arn,
            "ipam_resource_discovery_association_id": ipam_resource_discovery_association_id,
        }

    @builtins.property
    def ipam_resource_discovery_association_arn(self) -> builtins.str:
        '''The ARN of the IPAMResourceDiscoveryAssociation resource.'''
        result = self._values.get("ipam_resource_discovery_association_arn")
        assert result is not None, "Required property 'ipam_resource_discovery_association_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_resource_discovery_association_id(self) -> builtins.str:
        '''The IpamResourceDiscoveryAssociationId of the IPAMResourceDiscoveryAssociation resource.'''
        result = self._values.get("ipam_resource_discovery_association_id")
        assert result is not None, "Required property 'ipam_resource_discovery_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPAMResourceDiscoveryAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPAMResourceDiscoveryReference",
    jsii_struct_bases=[],
    name_mapping={
        "ipam_resource_discovery_arn": "ipamResourceDiscoveryArn",
        "ipam_resource_discovery_id": "ipamResourceDiscoveryId",
    },
)
class IPAMResourceDiscoveryReference:
    def __init__(
        self,
        *,
        ipam_resource_discovery_arn: builtins.str,
        ipam_resource_discovery_id: builtins.str,
    ) -> None:
        '''A reference to a IPAMResourceDiscovery resource.

        :param ipam_resource_discovery_arn: The ARN of the IPAMResourceDiscovery resource.
        :param ipam_resource_discovery_id: The IpamResourceDiscoveryId of the IPAMResourceDiscovery resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            i_pAMResource_discovery_reference = {
                "ipam_resource_discovery_arn": "ipamResourceDiscoveryArn",
                "ipam_resource_discovery_id": "ipamResourceDiscoveryId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2ea9e66efdddfa8669cc157e45981e03ce182eab234c9a9ea016baa95bd4659)
            check_type(argname="argument ipam_resource_discovery_arn", value=ipam_resource_discovery_arn, expected_type=type_hints["ipam_resource_discovery_arn"])
            check_type(argname="argument ipam_resource_discovery_id", value=ipam_resource_discovery_id, expected_type=type_hints["ipam_resource_discovery_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ipam_resource_discovery_arn": ipam_resource_discovery_arn,
            "ipam_resource_discovery_id": ipam_resource_discovery_id,
        }

    @builtins.property
    def ipam_resource_discovery_arn(self) -> builtins.str:
        '''The ARN of the IPAMResourceDiscovery resource.'''
        result = self._values.get("ipam_resource_discovery_arn")
        assert result is not None, "Required property 'ipam_resource_discovery_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_resource_discovery_id(self) -> builtins.str:
        '''The IpamResourceDiscoveryId of the IPAMResourceDiscovery resource.'''
        result = self._values.get("ipam_resource_discovery_id")
        assert result is not None, "Required property 'ipam_resource_discovery_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPAMResourceDiscoveryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPAMScopeReference",
    jsii_struct_bases=[],
    name_mapping={"ipam_scope_arn": "ipamScopeArn", "ipam_scope_id": "ipamScopeId"},
)
class IPAMScopeReference:
    def __init__(
        self,
        *,
        ipam_scope_arn: builtins.str,
        ipam_scope_id: builtins.str,
    ) -> None:
        '''A reference to a IPAMScope resource.

        :param ipam_scope_arn: The ARN of the IPAMScope resource.
        :param ipam_scope_id: The IpamScopeId of the IPAMScope resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            i_pAMScope_reference = {
                "ipam_scope_arn": "ipamScopeArn",
                "ipam_scope_id": "ipamScopeId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da183a6f045185e65fe67a7bb0f4e74662c652173a7c3c2d9103452e54ccbbbf)
            check_type(argname="argument ipam_scope_arn", value=ipam_scope_arn, expected_type=type_hints["ipam_scope_arn"])
            check_type(argname="argument ipam_scope_id", value=ipam_scope_id, expected_type=type_hints["ipam_scope_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ipam_scope_arn": ipam_scope_arn,
            "ipam_scope_id": ipam_scope_id,
        }

    @builtins.property
    def ipam_scope_arn(self) -> builtins.str:
        '''The ARN of the IPAMScope resource.'''
        result = self._values.get("ipam_scope_arn")
        assert result is not None, "Required property 'ipam_scope_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ipam_scope_id(self) -> builtins.str:
        '''The IpamScopeId of the IPAMScope resource.'''
        result = self._values.get("ipam_scope_id")
        assert result is not None, "Required property 'ipam_scope_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPAMScopeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPlacementGroupRef")
class IPlacementGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PlacementGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="placementGroupRef")
    def placement_group_ref(self) -> "PlacementGroupReference":
        '''(experimental) A reference to a PlacementGroup resource.

        :stability: experimental
        '''
        ...


class _IPlacementGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PlacementGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IPlacementGroupRef"

    @builtins.property
    @jsii.member(jsii_name="placementGroupRef")
    def placement_group_ref(self) -> "PlacementGroupReference":
        '''(experimental) A reference to a PlacementGroup resource.

        :stability: experimental
        '''
        return typing.cast("PlacementGroupReference", jsii.get(self, "placementGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPlacementGroupRef).__jsii_proxy_class__ = lambda : _IPlacementGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IPrefixListRef")
class IPrefixListRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PrefixList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="prefixListRef")
    def prefix_list_ref(self) -> "PrefixListReference":
        '''(experimental) A reference to a PrefixList resource.

        :stability: experimental
        '''
        ...


class _IPrefixListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PrefixList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IPrefixListRef"

    @builtins.property
    @jsii.member(jsii_name="prefixListRef")
    def prefix_list_ref(self) -> "PrefixListReference":
        '''(experimental) A reference to a PrefixList resource.

        :stability: experimental
        '''
        return typing.cast("PrefixListReference", jsii.get(self, "prefixListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrefixListRef).__jsii_proxy_class__ = lambda : _IPrefixListRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IRouteRef")
class IRouteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Route.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeRef")
    def route_ref(self) -> "RouteReference":
        '''(experimental) A reference to a Route resource.

        :stability: experimental
        '''
        ...


class _IRouteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Route.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IRouteRef"

    @builtins.property
    @jsii.member(jsii_name="routeRef")
    def route_ref(self) -> "RouteReference":
        '''(experimental) A reference to a Route resource.

        :stability: experimental
        '''
        return typing.cast("RouteReference", jsii.get(self, "routeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteRef).__jsii_proxy_class__ = lambda : _IRouteRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IRouteServerAssociationRef")
class IRouteServerAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServerAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeServerAssociationRef")
    def route_server_association_ref(self) -> "RouteServerAssociationReference":
        '''(experimental) A reference to a RouteServerAssociation resource.

        :stability: experimental
        '''
        ...


class _IRouteServerAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServerAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IRouteServerAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="routeServerAssociationRef")
    def route_server_association_ref(self) -> "RouteServerAssociationReference":
        '''(experimental) A reference to a RouteServerAssociation resource.

        :stability: experimental
        '''
        return typing.cast("RouteServerAssociationReference", jsii.get(self, "routeServerAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteServerAssociationRef).__jsii_proxy_class__ = lambda : _IRouteServerAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IRouteServerEndpointRef")
class IRouteServerEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServerEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeServerEndpointRef")
    def route_server_endpoint_ref(self) -> "RouteServerEndpointReference":
        '''(experimental) A reference to a RouteServerEndpoint resource.

        :stability: experimental
        '''
        ...


class _IRouteServerEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServerEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IRouteServerEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="routeServerEndpointRef")
    def route_server_endpoint_ref(self) -> "RouteServerEndpointReference":
        '''(experimental) A reference to a RouteServerEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("RouteServerEndpointReference", jsii.get(self, "routeServerEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteServerEndpointRef).__jsii_proxy_class__ = lambda : _IRouteServerEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IRouteServerPeerRef")
class IRouteServerPeerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServerPeer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeServerPeerRef")
    def route_server_peer_ref(self) -> "RouteServerPeerReference":
        '''(experimental) A reference to a RouteServerPeer resource.

        :stability: experimental
        '''
        ...


class _IRouteServerPeerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServerPeer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IRouteServerPeerRef"

    @builtins.property
    @jsii.member(jsii_name="routeServerPeerRef")
    def route_server_peer_ref(self) -> "RouteServerPeerReference":
        '''(experimental) A reference to a RouteServerPeer resource.

        :stability: experimental
        '''
        return typing.cast("RouteServerPeerReference", jsii.get(self, "routeServerPeerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteServerPeerRef).__jsii_proxy_class__ = lambda : _IRouteServerPeerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IRouteServerPropagationRef")
class IRouteServerPropagationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServerPropagation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeServerPropagationRef")
    def route_server_propagation_ref(self) -> "RouteServerPropagationReference":
        '''(experimental) A reference to a RouteServerPropagation resource.

        :stability: experimental
        '''
        ...


class _IRouteServerPropagationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServerPropagation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IRouteServerPropagationRef"

    @builtins.property
    @jsii.member(jsii_name="routeServerPropagationRef")
    def route_server_propagation_ref(self) -> "RouteServerPropagationReference":
        '''(experimental) A reference to a RouteServerPropagation resource.

        :stability: experimental
        '''
        return typing.cast("RouteServerPropagationReference", jsii.get(self, "routeServerPropagationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteServerPropagationRef).__jsii_proxy_class__ = lambda : _IRouteServerPropagationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IRouteServerRef")
class IRouteServerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeServerRef")
    def route_server_ref(self) -> "RouteServerReference":
        '''(experimental) A reference to a RouteServer resource.

        :stability: experimental
        '''
        ...


class _IRouteServerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouteServer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IRouteServerRef"

    @builtins.property
    @jsii.member(jsii_name="routeServerRef")
    def route_server_ref(self) -> "RouteServerReference":
        '''(experimental) A reference to a RouteServer resource.

        :stability: experimental
        '''
        return typing.cast("RouteServerReference", jsii.get(self, "routeServerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteServerRef).__jsii_proxy_class__ = lambda : _IRouteServerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IRouteTableRef")
class IRouteTableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouteTable.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeTableRef")
    def route_table_ref(self) -> "RouteTableReference":
        '''(experimental) A reference to a RouteTable resource.

        :stability: experimental
        '''
        ...


class _IRouteTableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouteTable.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IRouteTableRef"

    @builtins.property
    @jsii.member(jsii_name="routeTableRef")
    def route_table_ref(self) -> "RouteTableReference":
        '''(experimental) A reference to a RouteTable resource.

        :stability: experimental
        '''
        return typing.cast("RouteTableReference", jsii.get(self, "routeTableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteTableRef).__jsii_proxy_class__ = lambda : _IRouteTableRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISecurityGroupEgressRef")
class ISecurityGroupEgressRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroupEgress.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityGroupEgressRef")
    def security_group_egress_ref(self) -> "SecurityGroupEgressReference":
        '''(experimental) A reference to a SecurityGroupEgress resource.

        :stability: experimental
        '''
        ...


class _ISecurityGroupEgressRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroupEgress.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISecurityGroupEgressRef"

    @builtins.property
    @jsii.member(jsii_name="securityGroupEgressRef")
    def security_group_egress_ref(self) -> "SecurityGroupEgressReference":
        '''(experimental) A reference to a SecurityGroupEgress resource.

        :stability: experimental
        '''
        return typing.cast("SecurityGroupEgressReference", jsii.get(self, "securityGroupEgressRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityGroupEgressRef).__jsii_proxy_class__ = lambda : _ISecurityGroupEgressRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISecurityGroupIngressRef")
class ISecurityGroupIngressRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroupIngress.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityGroupIngressRef")
    def security_group_ingress_ref(self) -> "SecurityGroupIngressReference":
        '''(experimental) A reference to a SecurityGroupIngress resource.

        :stability: experimental
        '''
        ...


class _ISecurityGroupIngressRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroupIngress.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISecurityGroupIngressRef"

    @builtins.property
    @jsii.member(jsii_name="securityGroupIngressRef")
    def security_group_ingress_ref(self) -> "SecurityGroupIngressReference":
        '''(experimental) A reference to a SecurityGroupIngress resource.

        :stability: experimental
        '''
        return typing.cast("SecurityGroupIngressReference", jsii.get(self, "securityGroupIngressRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityGroupIngressRef).__jsii_proxy_class__ = lambda : _ISecurityGroupIngressRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISecurityGroupRef")
class ISecurityGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityGroupRef")
    def security_group_ref(self) -> "SecurityGroupReference":
        '''(experimental) A reference to a SecurityGroup resource.

        :stability: experimental
        '''
        ...


class _ISecurityGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISecurityGroupRef"

    @builtins.property
    @jsii.member(jsii_name="securityGroupRef")
    def security_group_ref(self) -> "SecurityGroupReference":
        '''(experimental) A reference to a SecurityGroup resource.

        :stability: experimental
        '''
        return typing.cast("SecurityGroupReference", jsii.get(self, "securityGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityGroupRef).__jsii_proxy_class__ = lambda : _ISecurityGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISecurityGroupVpcAssociationRef"
)
class ISecurityGroupVpcAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroupVpcAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityGroupVpcAssociationRef")
    def security_group_vpc_association_ref(
        self,
    ) -> "SecurityGroupVpcAssociationReference":
        '''(experimental) A reference to a SecurityGroupVpcAssociation resource.

        :stability: experimental
        '''
        ...


class _ISecurityGroupVpcAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroupVpcAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISecurityGroupVpcAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="securityGroupVpcAssociationRef")
    def security_group_vpc_association_ref(
        self,
    ) -> "SecurityGroupVpcAssociationReference":
        '''(experimental) A reference to a SecurityGroupVpcAssociation resource.

        :stability: experimental
        '''
        return typing.cast("SecurityGroupVpcAssociationReference", jsii.get(self, "securityGroupVpcAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityGroupVpcAssociationRef).__jsii_proxy_class__ = lambda : _ISecurityGroupVpcAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISnapshotBlockPublicAccessRef"
)
class ISnapshotBlockPublicAccessRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SnapshotBlockPublicAccess.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="snapshotBlockPublicAccessRef")
    def snapshot_block_public_access_ref(self) -> "SnapshotBlockPublicAccessReference":
        '''(experimental) A reference to a SnapshotBlockPublicAccess resource.

        :stability: experimental
        '''
        ...


class _ISnapshotBlockPublicAccessRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SnapshotBlockPublicAccess.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISnapshotBlockPublicAccessRef"

    @builtins.property
    @jsii.member(jsii_name="snapshotBlockPublicAccessRef")
    def snapshot_block_public_access_ref(self) -> "SnapshotBlockPublicAccessReference":
        '''(experimental) A reference to a SnapshotBlockPublicAccess resource.

        :stability: experimental
        '''
        return typing.cast("SnapshotBlockPublicAccessReference", jsii.get(self, "snapshotBlockPublicAccessRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISnapshotBlockPublicAccessRef).__jsii_proxy_class__ = lambda : _ISnapshotBlockPublicAccessRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISpotFleetRef")
class ISpotFleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SpotFleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="spotFleetRef")
    def spot_fleet_ref(self) -> "SpotFleetReference":
        '''(experimental) A reference to a SpotFleet resource.

        :stability: experimental
        '''
        ...


class _ISpotFleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SpotFleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISpotFleetRef"

    @builtins.property
    @jsii.member(jsii_name="spotFleetRef")
    def spot_fleet_ref(self) -> "SpotFleetReference":
        '''(experimental) A reference to a SpotFleet resource.

        :stability: experimental
        '''
        return typing.cast("SpotFleetReference", jsii.get(self, "spotFleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISpotFleetRef).__jsii_proxy_class__ = lambda : _ISpotFleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISubnetCidrBlockRef")
class ISubnetCidrBlockRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SubnetCidrBlock.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subnetCidrBlockRef")
    def subnet_cidr_block_ref(self) -> "SubnetCidrBlockReference":
        '''(experimental) A reference to a SubnetCidrBlock resource.

        :stability: experimental
        '''
        ...


class _ISubnetCidrBlockRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SubnetCidrBlock.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISubnetCidrBlockRef"

    @builtins.property
    @jsii.member(jsii_name="subnetCidrBlockRef")
    def subnet_cidr_block_ref(self) -> "SubnetCidrBlockReference":
        '''(experimental) A reference to a SubnetCidrBlock resource.

        :stability: experimental
        '''
        return typing.cast("SubnetCidrBlockReference", jsii.get(self, "subnetCidrBlockRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubnetCidrBlockRef).__jsii_proxy_class__ = lambda : _ISubnetCidrBlockRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISubnetNetworkAclAssociationRef"
)
class ISubnetNetworkAclAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SubnetNetworkAclAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subnetNetworkAclAssociationRef")
    def subnet_network_acl_association_ref(
        self,
    ) -> "SubnetNetworkAclAssociationReference":
        '''(experimental) A reference to a SubnetNetworkAclAssociation resource.

        :stability: experimental
        '''
        ...


class _ISubnetNetworkAclAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SubnetNetworkAclAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISubnetNetworkAclAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="subnetNetworkAclAssociationRef")
    def subnet_network_acl_association_ref(
        self,
    ) -> "SubnetNetworkAclAssociationReference":
        '''(experimental) A reference to a SubnetNetworkAclAssociation resource.

        :stability: experimental
        '''
        return typing.cast("SubnetNetworkAclAssociationReference", jsii.get(self, "subnetNetworkAclAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubnetNetworkAclAssociationRef).__jsii_proxy_class__ = lambda : _ISubnetNetworkAclAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISubnetRef")
class ISubnetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Subnet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subnetRef")
    def subnet_ref(self) -> "SubnetReference":
        '''(experimental) A reference to a Subnet resource.

        :stability: experimental
        '''
        ...


class _ISubnetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Subnet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISubnetRef"

    @builtins.property
    @jsii.member(jsii_name="subnetRef")
    def subnet_ref(self) -> "SubnetReference":
        '''(experimental) A reference to a Subnet resource.

        :stability: experimental
        '''
        return typing.cast("SubnetReference", jsii.get(self, "subnetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubnetRef).__jsii_proxy_class__ = lambda : _ISubnetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ISubnetRouteTableAssociationRef"
)
class ISubnetRouteTableAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SubnetRouteTableAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subnetRouteTableAssociationRef")
    def subnet_route_table_association_ref(
        self,
    ) -> "SubnetRouteTableAssociationReference":
        '''(experimental) A reference to a SubnetRouteTableAssociation resource.

        :stability: experimental
        '''
        ...


class _ISubnetRouteTableAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SubnetRouteTableAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ISubnetRouteTableAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="subnetRouteTableAssociationRef")
    def subnet_route_table_association_ref(
        self,
    ) -> "SubnetRouteTableAssociationReference":
        '''(experimental) A reference to a SubnetRouteTableAssociation resource.

        :stability: experimental
        '''
        return typing.cast("SubnetRouteTableAssociationReference", jsii.get(self, "subnetRouteTableAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubnetRouteTableAssociationRef).__jsii_proxy_class__ = lambda : _ISubnetRouteTableAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITrafficMirrorFilterRef")
class ITrafficMirrorFilterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficMirrorFilter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trafficMirrorFilterRef")
    def traffic_mirror_filter_ref(self) -> "TrafficMirrorFilterReference":
        '''(experimental) A reference to a TrafficMirrorFilter resource.

        :stability: experimental
        '''
        ...


class _ITrafficMirrorFilterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficMirrorFilter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITrafficMirrorFilterRef"

    @builtins.property
    @jsii.member(jsii_name="trafficMirrorFilterRef")
    def traffic_mirror_filter_ref(self) -> "TrafficMirrorFilterReference":
        '''(experimental) A reference to a TrafficMirrorFilter resource.

        :stability: experimental
        '''
        return typing.cast("TrafficMirrorFilterReference", jsii.get(self, "trafficMirrorFilterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrafficMirrorFilterRef).__jsii_proxy_class__ = lambda : _ITrafficMirrorFilterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITrafficMirrorFilterRuleRef")
class ITrafficMirrorFilterRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficMirrorFilterRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trafficMirrorFilterRuleRef")
    def traffic_mirror_filter_rule_ref(self) -> "TrafficMirrorFilterRuleReference":
        '''(experimental) A reference to a TrafficMirrorFilterRule resource.

        :stability: experimental
        '''
        ...


class _ITrafficMirrorFilterRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficMirrorFilterRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITrafficMirrorFilterRuleRef"

    @builtins.property
    @jsii.member(jsii_name="trafficMirrorFilterRuleRef")
    def traffic_mirror_filter_rule_ref(self) -> "TrafficMirrorFilterRuleReference":
        '''(experimental) A reference to a TrafficMirrorFilterRule resource.

        :stability: experimental
        '''
        return typing.cast("TrafficMirrorFilterRuleReference", jsii.get(self, "trafficMirrorFilterRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrafficMirrorFilterRuleRef).__jsii_proxy_class__ = lambda : _ITrafficMirrorFilterRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITrafficMirrorSessionRef")
class ITrafficMirrorSessionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficMirrorSession.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trafficMirrorSessionRef")
    def traffic_mirror_session_ref(self) -> "TrafficMirrorSessionReference":
        '''(experimental) A reference to a TrafficMirrorSession resource.

        :stability: experimental
        '''
        ...


class _ITrafficMirrorSessionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficMirrorSession.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITrafficMirrorSessionRef"

    @builtins.property
    @jsii.member(jsii_name="trafficMirrorSessionRef")
    def traffic_mirror_session_ref(self) -> "TrafficMirrorSessionReference":
        '''(experimental) A reference to a TrafficMirrorSession resource.

        :stability: experimental
        '''
        return typing.cast("TrafficMirrorSessionReference", jsii.get(self, "trafficMirrorSessionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrafficMirrorSessionRef).__jsii_proxy_class__ = lambda : _ITrafficMirrorSessionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITrafficMirrorTargetRef")
class ITrafficMirrorTargetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficMirrorTarget.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trafficMirrorTargetRef")
    def traffic_mirror_target_ref(self) -> "TrafficMirrorTargetReference":
        '''(experimental) A reference to a TrafficMirrorTarget resource.

        :stability: experimental
        '''
        ...


class _ITrafficMirrorTargetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrafficMirrorTarget.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITrafficMirrorTargetRef"

    @builtins.property
    @jsii.member(jsii_name="trafficMirrorTargetRef")
    def traffic_mirror_target_ref(self) -> "TrafficMirrorTargetReference":
        '''(experimental) A reference to a TrafficMirrorTarget resource.

        :stability: experimental
        '''
        return typing.cast("TrafficMirrorTargetReference", jsii.get(self, "trafficMirrorTargetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrafficMirrorTargetRef).__jsii_proxy_class__ = lambda : _ITrafficMirrorTargetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayAttachmentRef"
)
class ITransitGatewayAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayAttachmentRef")
    def transit_gateway_attachment_ref(self) -> "TransitGatewayAttachmentReference":
        '''(experimental) A reference to a TransitGatewayAttachment resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayAttachmentRef")
    def transit_gateway_attachment_ref(self) -> "TransitGatewayAttachmentReference":
        '''(experimental) A reference to a TransitGatewayAttachment resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayAttachmentReference", jsii.get(self, "transitGatewayAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayAttachmentRef).__jsii_proxy_class__ = lambda : _ITransitGatewayAttachmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayConnectPeerRef"
)
class ITransitGatewayConnectPeerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayConnectPeer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayConnectPeerRef")
    def transit_gateway_connect_peer_ref(self) -> "TransitGatewayConnectPeerReference":
        '''(experimental) A reference to a TransitGatewayConnectPeer resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayConnectPeerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayConnectPeer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayConnectPeerRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayConnectPeerRef")
    def transit_gateway_connect_peer_ref(self) -> "TransitGatewayConnectPeerReference":
        '''(experimental) A reference to a TransitGatewayConnectPeer resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayConnectPeerReference", jsii.get(self, "transitGatewayConnectPeerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayConnectPeerRef).__jsii_proxy_class__ = lambda : _ITransitGatewayConnectPeerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayConnectRef")
class ITransitGatewayConnectRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayConnect.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayConnectRef")
    def transit_gateway_connect_ref(self) -> "TransitGatewayConnectReference":
        '''(experimental) A reference to a TransitGatewayConnect resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayConnectRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayConnect.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayConnectRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayConnectRef")
    def transit_gateway_connect_ref(self) -> "TransitGatewayConnectReference":
        '''(experimental) A reference to a TransitGatewayConnect resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayConnectReference", jsii.get(self, "transitGatewayConnectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayConnectRef).__jsii_proxy_class__ = lambda : _ITransitGatewayConnectRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMeteringPolicyEntryRef"
)
class ITransitGatewayMeteringPolicyEntryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMeteringPolicyEntry.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMeteringPolicyEntryRef")
    def transit_gateway_metering_policy_entry_ref(
        self,
    ) -> "TransitGatewayMeteringPolicyEntryReference":
        '''(experimental) A reference to a TransitGatewayMeteringPolicyEntry resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayMeteringPolicyEntryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMeteringPolicyEntry.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMeteringPolicyEntryRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMeteringPolicyEntryRef")
    def transit_gateway_metering_policy_entry_ref(
        self,
    ) -> "TransitGatewayMeteringPolicyEntryReference":
        '''(experimental) A reference to a TransitGatewayMeteringPolicyEntry resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayMeteringPolicyEntryReference", jsii.get(self, "transitGatewayMeteringPolicyEntryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayMeteringPolicyEntryRef).__jsii_proxy_class__ = lambda : _ITransitGatewayMeteringPolicyEntryRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMeteringPolicyRef"
)
class ITransitGatewayMeteringPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMeteringPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMeteringPolicyRef")
    def transit_gateway_metering_policy_ref(
        self,
    ) -> "TransitGatewayMeteringPolicyReference":
        '''(experimental) A reference to a TransitGatewayMeteringPolicy resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayMeteringPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMeteringPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMeteringPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMeteringPolicyRef")
    def transit_gateway_metering_policy_ref(
        self,
    ) -> "TransitGatewayMeteringPolicyReference":
        '''(experimental) A reference to a TransitGatewayMeteringPolicy resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayMeteringPolicyReference", jsii.get(self, "transitGatewayMeteringPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayMeteringPolicyRef).__jsii_proxy_class__ = lambda : _ITransitGatewayMeteringPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMulticastDomainAssociationRef"
)
class ITransitGatewayMulticastDomainAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMulticastDomainAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMulticastDomainAssociationRef")
    def transit_gateway_multicast_domain_association_ref(
        self,
    ) -> "TransitGatewayMulticastDomainAssociationReference":
        '''(experimental) A reference to a TransitGatewayMulticastDomainAssociation resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayMulticastDomainAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMulticastDomainAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMulticastDomainAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMulticastDomainAssociationRef")
    def transit_gateway_multicast_domain_association_ref(
        self,
    ) -> "TransitGatewayMulticastDomainAssociationReference":
        '''(experimental) A reference to a TransitGatewayMulticastDomainAssociation resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayMulticastDomainAssociationReference", jsii.get(self, "transitGatewayMulticastDomainAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayMulticastDomainAssociationRef).__jsii_proxy_class__ = lambda : _ITransitGatewayMulticastDomainAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMulticastDomainRef"
)
class ITransitGatewayMulticastDomainRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMulticastDomain.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMulticastDomainRef")
    def transit_gateway_multicast_domain_ref(
        self,
    ) -> "TransitGatewayMulticastDomainReference":
        '''(experimental) A reference to a TransitGatewayMulticastDomain resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayMulticastDomainRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMulticastDomain.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMulticastDomainRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMulticastDomainRef")
    def transit_gateway_multicast_domain_ref(
        self,
    ) -> "TransitGatewayMulticastDomainReference":
        '''(experimental) A reference to a TransitGatewayMulticastDomain resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayMulticastDomainReference", jsii.get(self, "transitGatewayMulticastDomainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayMulticastDomainRef).__jsii_proxy_class__ = lambda : _ITransitGatewayMulticastDomainRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMulticastGroupMemberRef"
)
class ITransitGatewayMulticastGroupMemberRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMulticastGroupMember.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMulticastGroupMemberRef")
    def transit_gateway_multicast_group_member_ref(
        self,
    ) -> "TransitGatewayMulticastGroupMemberReference":
        '''(experimental) A reference to a TransitGatewayMulticastGroupMember resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayMulticastGroupMemberRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMulticastGroupMember.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMulticastGroupMemberRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMulticastGroupMemberRef")
    def transit_gateway_multicast_group_member_ref(
        self,
    ) -> "TransitGatewayMulticastGroupMemberReference":
        '''(experimental) A reference to a TransitGatewayMulticastGroupMember resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayMulticastGroupMemberReference", jsii.get(self, "transitGatewayMulticastGroupMemberRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayMulticastGroupMemberRef).__jsii_proxy_class__ = lambda : _ITransitGatewayMulticastGroupMemberRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMulticastGroupSourceRef"
)
class ITransitGatewayMulticastGroupSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMulticastGroupSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMulticastGroupSourceRef")
    def transit_gateway_multicast_group_source_ref(
        self,
    ) -> "TransitGatewayMulticastGroupSourceReference":
        '''(experimental) A reference to a TransitGatewayMulticastGroupSource resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayMulticastGroupSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayMulticastGroupSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayMulticastGroupSourceRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayMulticastGroupSourceRef")
    def transit_gateway_multicast_group_source_ref(
        self,
    ) -> "TransitGatewayMulticastGroupSourceReference":
        '''(experimental) A reference to a TransitGatewayMulticastGroupSource resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayMulticastGroupSourceReference", jsii.get(self, "transitGatewayMulticastGroupSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayMulticastGroupSourceRef).__jsii_proxy_class__ = lambda : _ITransitGatewayMulticastGroupSourceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayPeeringAttachmentRef"
)
class ITransitGatewayPeeringAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayPeeringAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayPeeringAttachmentRef")
    def transit_gateway_peering_attachment_ref(
        self,
    ) -> "TransitGatewayPeeringAttachmentReference":
        '''(experimental) A reference to a TransitGatewayPeeringAttachment resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayPeeringAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayPeeringAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayPeeringAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayPeeringAttachmentRef")
    def transit_gateway_peering_attachment_ref(
        self,
    ) -> "TransitGatewayPeeringAttachmentReference":
        '''(experimental) A reference to a TransitGatewayPeeringAttachment resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayPeeringAttachmentReference", jsii.get(self, "transitGatewayPeeringAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayPeeringAttachmentRef).__jsii_proxy_class__ = lambda : _ITransitGatewayPeeringAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRef")
class ITransitGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRef")
    def transit_gateway_ref(self) -> "TransitGatewayReference":
        '''(experimental) A reference to a TransitGateway resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRef")
    def transit_gateway_ref(self) -> "TransitGatewayReference":
        '''(experimental) A reference to a TransitGateway resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayReference", jsii.get(self, "transitGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayRef).__jsii_proxy_class__ = lambda : _ITransitGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRouteRef")
class ITransitGatewayRouteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRoute.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteRef")
    def transit_gateway_route_ref(self) -> "TransitGatewayRouteReference":
        '''(experimental) A reference to a TransitGatewayRoute resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayRouteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRoute.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRouteRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteRef")
    def transit_gateway_route_ref(self) -> "TransitGatewayRouteReference":
        '''(experimental) A reference to a TransitGatewayRoute resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayRouteReference", jsii.get(self, "transitGatewayRouteRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayRouteRef).__jsii_proxy_class__ = lambda : _ITransitGatewayRouteRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRouteTableAssociationRef"
)
class ITransitGatewayRouteTableAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRouteTableAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableAssociationRef")
    def transit_gateway_route_table_association_ref(
        self,
    ) -> "TransitGatewayRouteTableAssociationReference":
        '''(experimental) A reference to a TransitGatewayRouteTableAssociation resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayRouteTableAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRouteTableAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRouteTableAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableAssociationRef")
    def transit_gateway_route_table_association_ref(
        self,
    ) -> "TransitGatewayRouteTableAssociationReference":
        '''(experimental) A reference to a TransitGatewayRouteTableAssociation resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayRouteTableAssociationReference", jsii.get(self, "transitGatewayRouteTableAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayRouteTableAssociationRef).__jsii_proxy_class__ = lambda : _ITransitGatewayRouteTableAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRouteTablePropagationRef"
)
class ITransitGatewayRouteTablePropagationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRouteTablePropagation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTablePropagationRef")
    def transit_gateway_route_table_propagation_ref(
        self,
    ) -> "TransitGatewayRouteTablePropagationReference":
        '''(experimental) A reference to a TransitGatewayRouteTablePropagation resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayRouteTablePropagationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRouteTablePropagation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRouteTablePropagationRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTablePropagationRef")
    def transit_gateway_route_table_propagation_ref(
        self,
    ) -> "TransitGatewayRouteTablePropagationReference":
        '''(experimental) A reference to a TransitGatewayRouteTablePropagation resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayRouteTablePropagationReference", jsii.get(self, "transitGatewayRouteTablePropagationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayRouteTablePropagationRef).__jsii_proxy_class__ = lambda : _ITransitGatewayRouteTablePropagationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRouteTableRef"
)
class ITransitGatewayRouteTableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRouteTable.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableRef")
    def transit_gateway_route_table_ref(self) -> "TransitGatewayRouteTableReference":
        '''(experimental) A reference to a TransitGatewayRouteTable resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayRouteTableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRouteTable.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayRouteTableRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableRef")
    def transit_gateway_route_table_ref(self) -> "TransitGatewayRouteTableReference":
        '''(experimental) A reference to a TransitGatewayRouteTable resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayRouteTableReference", jsii.get(self, "transitGatewayRouteTableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayRouteTableRef).__jsii_proxy_class__ = lambda : _ITransitGatewayRouteTableRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayVpcAttachmentRef"
)
class ITransitGatewayVpcAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayVpcAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayVpcAttachmentRef")
    def transit_gateway_vpc_attachment_ref(
        self,
    ) -> "TransitGatewayVpcAttachmentReference":
        '''(experimental) A reference to a TransitGatewayVpcAttachment resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayVpcAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayVpcAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.ITransitGatewayVpcAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayVpcAttachmentRef")
    def transit_gateway_vpc_attachment_ref(
        self,
    ) -> "TransitGatewayVpcAttachmentReference":
        '''(experimental) A reference to a TransitGatewayVpcAttachment resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayVpcAttachmentReference", jsii.get(self, "transitGatewayVpcAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayVpcAttachmentRef).__jsii_proxy_class__ = lambda : _ITransitGatewayVpcAttachmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCBlockPublicAccessExclusionRef"
)
class IVPCBlockPublicAccessExclusionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCBlockPublicAccessExclusion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcBlockPublicAccessExclusionRef")
    def vpc_block_public_access_exclusion_ref(
        self,
    ) -> "VPCBlockPublicAccessExclusionReference":
        '''(experimental) A reference to a VPCBlockPublicAccessExclusion resource.

        :stability: experimental
        '''
        ...


class _IVPCBlockPublicAccessExclusionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCBlockPublicAccessExclusion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCBlockPublicAccessExclusionRef"

    @builtins.property
    @jsii.member(jsii_name="vpcBlockPublicAccessExclusionRef")
    def vpc_block_public_access_exclusion_ref(
        self,
    ) -> "VPCBlockPublicAccessExclusionReference":
        '''(experimental) A reference to a VPCBlockPublicAccessExclusion resource.

        :stability: experimental
        '''
        return typing.cast("VPCBlockPublicAccessExclusionReference", jsii.get(self, "vpcBlockPublicAccessExclusionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCBlockPublicAccessExclusionRef).__jsii_proxy_class__ = lambda : _IVPCBlockPublicAccessExclusionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCBlockPublicAccessOptionsRef"
)
class IVPCBlockPublicAccessOptionsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCBlockPublicAccessOptions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcBlockPublicAccessOptionsRef")
    def vpc_block_public_access_options_ref(
        self,
    ) -> "VPCBlockPublicAccessOptionsReference":
        '''(experimental) A reference to a VPCBlockPublicAccessOptions resource.

        :stability: experimental
        '''
        ...


class _IVPCBlockPublicAccessOptionsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCBlockPublicAccessOptions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCBlockPublicAccessOptionsRef"

    @builtins.property
    @jsii.member(jsii_name="vpcBlockPublicAccessOptionsRef")
    def vpc_block_public_access_options_ref(
        self,
    ) -> "VPCBlockPublicAccessOptionsReference":
        '''(experimental) A reference to a VPCBlockPublicAccessOptions resource.

        :stability: experimental
        '''
        return typing.cast("VPCBlockPublicAccessOptionsReference", jsii.get(self, "vpcBlockPublicAccessOptionsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCBlockPublicAccessOptionsRef).__jsii_proxy_class__ = lambda : _IVPCBlockPublicAccessOptionsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCCidrBlockRef")
class IVPCCidrBlockRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCCidrBlock.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcCidrBlockRef")
    def vpc_cidr_block_ref(self) -> "VPCCidrBlockReference":
        '''(experimental) A reference to a VPCCidrBlock resource.

        :stability: experimental
        '''
        ...


class _IVPCCidrBlockRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCCidrBlock.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCCidrBlockRef"

    @builtins.property
    @jsii.member(jsii_name="vpcCidrBlockRef")
    def vpc_cidr_block_ref(self) -> "VPCCidrBlockReference":
        '''(experimental) A reference to a VPCCidrBlock resource.

        :stability: experimental
        '''
        return typing.cast("VPCCidrBlockReference", jsii.get(self, "vpcCidrBlockRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCCidrBlockRef).__jsii_proxy_class__ = lambda : _IVPCCidrBlockRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCDHCPOptionsAssociationRef"
)
class IVPCDHCPOptionsAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCDHCPOptionsAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcdhcpOptionsAssociationRef")
    def vpcdhcp_options_association_ref(self) -> "VPCDHCPOptionsAssociationReference":
        '''(experimental) A reference to a VPCDHCPOptionsAssociation resource.

        :stability: experimental
        '''
        ...


class _IVPCDHCPOptionsAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCDHCPOptionsAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCDHCPOptionsAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="vpcdhcpOptionsAssociationRef")
    def vpcdhcp_options_association_ref(self) -> "VPCDHCPOptionsAssociationReference":
        '''(experimental) A reference to a VPCDHCPOptionsAssociation resource.

        :stability: experimental
        '''
        return typing.cast("VPCDHCPOptionsAssociationReference", jsii.get(self, "vpcdhcpOptionsAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCDHCPOptionsAssociationRef).__jsii_proxy_class__ = lambda : _IVPCDHCPOptionsAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCEncryptionControlRef")
class IVPCEncryptionControlRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEncryptionControl.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcEncryptionControlRef")
    def vpc_encryption_control_ref(self) -> "VPCEncryptionControlReference":
        '''(experimental) A reference to a VPCEncryptionControl resource.

        :stability: experimental
        '''
        ...


class _IVPCEncryptionControlRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEncryptionControl.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCEncryptionControlRef"

    @builtins.property
    @jsii.member(jsii_name="vpcEncryptionControlRef")
    def vpc_encryption_control_ref(self) -> "VPCEncryptionControlReference":
        '''(experimental) A reference to a VPCEncryptionControl resource.

        :stability: experimental
        '''
        return typing.cast("VPCEncryptionControlReference", jsii.get(self, "vpcEncryptionControlRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCEncryptionControlRef).__jsii_proxy_class__ = lambda : _IVPCEncryptionControlRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCEndpointConnectionNotificationRef"
)
class IVPCEndpointConnectionNotificationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEndpointConnectionNotification.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointConnectionNotificationRef")
    def vpc_endpoint_connection_notification_ref(
        self,
    ) -> "VPCEndpointConnectionNotificationReference":
        '''(experimental) A reference to a VPCEndpointConnectionNotification resource.

        :stability: experimental
        '''
        ...


class _IVPCEndpointConnectionNotificationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEndpointConnectionNotification.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCEndpointConnectionNotificationRef"

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointConnectionNotificationRef")
    def vpc_endpoint_connection_notification_ref(
        self,
    ) -> "VPCEndpointConnectionNotificationReference":
        '''(experimental) A reference to a VPCEndpointConnectionNotification resource.

        :stability: experimental
        '''
        return typing.cast("VPCEndpointConnectionNotificationReference", jsii.get(self, "vpcEndpointConnectionNotificationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCEndpointConnectionNotificationRef).__jsii_proxy_class__ = lambda : _IVPCEndpointConnectionNotificationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCEndpointRef")
class IVPCEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointRef")
    def vpc_endpoint_ref(self) -> "VPCEndpointReference":
        '''(experimental) A reference to a VPCEndpoint resource.

        :stability: experimental
        '''
        ...


class _IVPCEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointRef")
    def vpc_endpoint_ref(self) -> "VPCEndpointReference":
        '''(experimental) A reference to a VPCEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("VPCEndpointReference", jsii.get(self, "vpcEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCEndpointRef).__jsii_proxy_class__ = lambda : _IVPCEndpointRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCEndpointServicePermissionsRef"
)
class IVPCEndpointServicePermissionsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEndpointServicePermissions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointServicePermissionsRef")
    def vpc_endpoint_service_permissions_ref(
        self,
    ) -> "VPCEndpointServicePermissionsReference":
        '''(experimental) A reference to a VPCEndpointServicePermissions resource.

        :stability: experimental
        '''
        ...


class _IVPCEndpointServicePermissionsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEndpointServicePermissions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCEndpointServicePermissionsRef"

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointServicePermissionsRef")
    def vpc_endpoint_service_permissions_ref(
        self,
    ) -> "VPCEndpointServicePermissionsReference":
        '''(experimental) A reference to a VPCEndpointServicePermissions resource.

        :stability: experimental
        '''
        return typing.cast("VPCEndpointServicePermissionsReference", jsii.get(self, "vpcEndpointServicePermissionsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCEndpointServicePermissionsRef).__jsii_proxy_class__ = lambda : _IVPCEndpointServicePermissionsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCEndpointServiceRef")
class IVPCEndpointServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEndpointService.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointServiceRef")
    def vpc_endpoint_service_ref(self) -> "VPCEndpointServiceReference":
        '''(experimental) A reference to a VPCEndpointService resource.

        :stability: experimental
        '''
        ...


class _IVPCEndpointServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEndpointService.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCEndpointServiceRef"

    @builtins.property
    @jsii.member(jsii_name="vpcEndpointServiceRef")
    def vpc_endpoint_service_ref(self) -> "VPCEndpointServiceReference":
        '''(experimental) A reference to a VPCEndpointService resource.

        :stability: experimental
        '''
        return typing.cast("VPCEndpointServiceReference", jsii.get(self, "vpcEndpointServiceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCEndpointServiceRef).__jsii_proxy_class__ = lambda : _IVPCEndpointServiceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCGatewayAttachmentRef")
class IVPCGatewayAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCGatewayAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcGatewayAttachmentRef")
    def vpc_gateway_attachment_ref(self) -> "VPCGatewayAttachmentReference":
        '''(experimental) A reference to a VPCGatewayAttachment resource.

        :stability: experimental
        '''
        ...


class _IVPCGatewayAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCGatewayAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCGatewayAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="vpcGatewayAttachmentRef")
    def vpc_gateway_attachment_ref(self) -> "VPCGatewayAttachmentReference":
        '''(experimental) A reference to a VPCGatewayAttachment resource.

        :stability: experimental
        '''
        return typing.cast("VPCGatewayAttachmentReference", jsii.get(self, "vpcGatewayAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCGatewayAttachmentRef).__jsii_proxy_class__ = lambda : _IVPCGatewayAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCPeeringConnectionRef")
class IVPCPeeringConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCPeeringConnection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConnectionRef")
    def vpc_peering_connection_ref(self) -> "VPCPeeringConnectionReference":
        '''(experimental) A reference to a VPCPeeringConnection resource.

        :stability: experimental
        '''
        ...


class _IVPCPeeringConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCPeeringConnection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCPeeringConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="vpcPeeringConnectionRef")
    def vpc_peering_connection_ref(self) -> "VPCPeeringConnectionReference":
        '''(experimental) A reference to a VPCPeeringConnection resource.

        :stability: experimental
        '''
        return typing.cast("VPCPeeringConnectionReference", jsii.get(self, "vpcPeeringConnectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCPeeringConnectionRef).__jsii_proxy_class__ = lambda : _IVPCPeeringConnectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPCRef")
class IVPCRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPC.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcRef")
    def vpc_ref(self) -> "VPCReference":
        '''(experimental) A reference to a VPC resource.

        :stability: experimental
        '''
        ...


class _IVPCRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPC.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPCRef"

    @builtins.property
    @jsii.member(jsii_name="vpcRef")
    def vpc_ref(self) -> "VPCReference":
        '''(experimental) A reference to a VPC resource.

        :stability: experimental
        '''
        return typing.cast("VPCReference", jsii.get(self, "vpcRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCRef).__jsii_proxy_class__ = lambda : _IVPCRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPNConcentratorRef")
class IVPNConcentratorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPNConcentrator.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpnConcentratorRef")
    def vpn_concentrator_ref(self) -> "VPNConcentratorReference":
        '''(experimental) A reference to a VPNConcentrator resource.

        :stability: experimental
        '''
        ...


class _IVPNConcentratorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPNConcentrator.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPNConcentratorRef"

    @builtins.property
    @jsii.member(jsii_name="vpnConcentratorRef")
    def vpn_concentrator_ref(self) -> "VPNConcentratorReference":
        '''(experimental) A reference to a VPNConcentrator resource.

        :stability: experimental
        '''
        return typing.cast("VPNConcentratorReference", jsii.get(self, "vpnConcentratorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPNConcentratorRef).__jsii_proxy_class__ = lambda : _IVPNConcentratorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPNConnectionRef")
class IVPNConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPNConnection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpnConnectionRef")
    def vpn_connection_ref(self) -> "VPNConnectionReference":
        '''(experimental) A reference to a VPNConnection resource.

        :stability: experimental
        '''
        ...


class _IVPNConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPNConnection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPNConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="vpnConnectionRef")
    def vpn_connection_ref(self) -> "VPNConnectionReference":
        '''(experimental) A reference to a VPNConnection resource.

        :stability: experimental
        '''
        return typing.cast("VPNConnectionReference", jsii.get(self, "vpnConnectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPNConnectionRef).__jsii_proxy_class__ = lambda : _IVPNConnectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPNConnectionRouteRef")
class IVPNConnectionRouteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPNConnectionRoute.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpnConnectionRouteRef")
    def vpn_connection_route_ref(self) -> "VPNConnectionRouteReference":
        '''(experimental) A reference to a VPNConnectionRoute resource.

        :stability: experimental
        '''
        ...


class _IVPNConnectionRouteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPNConnectionRoute.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPNConnectionRouteRef"

    @builtins.property
    @jsii.member(jsii_name="vpnConnectionRouteRef")
    def vpn_connection_route_ref(self) -> "VPNConnectionRouteReference":
        '''(experimental) A reference to a VPNConnectionRoute resource.

        :stability: experimental
        '''
        return typing.cast("VPNConnectionRouteReference", jsii.get(self, "vpnConnectionRouteRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPNConnectionRouteRef).__jsii_proxy_class__ = lambda : _IVPNConnectionRouteRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPNGatewayRef")
class IVPNGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPNGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayRef")
    def vpn_gateway_ref(self) -> "VPNGatewayReference":
        '''(experimental) A reference to a VPNGateway resource.

        :stability: experimental
        '''
        ...


class _IVPNGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPNGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPNGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayRef")
    def vpn_gateway_ref(self) -> "VPNGatewayReference":
        '''(experimental) A reference to a VPNGateway resource.

        :stability: experimental
        '''
        return typing.cast("VPNGatewayReference", jsii.get(self, "vpnGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPNGatewayRef).__jsii_proxy_class__ = lambda : _IVPNGatewayRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVPNGatewayRoutePropagationRef"
)
class IVPNGatewayRoutePropagationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPNGatewayRoutePropagation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayRoutePropagationRef")
    def vpn_gateway_route_propagation_ref(
        self,
    ) -> "VPNGatewayRoutePropagationReference":
        '''(experimental) A reference to a VPNGatewayRoutePropagation resource.

        :stability: experimental
        '''
        ...


class _IVPNGatewayRoutePropagationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPNGatewayRoutePropagation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVPNGatewayRoutePropagationRef"

    @builtins.property
    @jsii.member(jsii_name="vpnGatewayRoutePropagationRef")
    def vpn_gateway_route_propagation_ref(
        self,
    ) -> "VPNGatewayRoutePropagationReference":
        '''(experimental) A reference to a VPNGatewayRoutePropagation resource.

        :stability: experimental
        '''
        return typing.cast("VPNGatewayRoutePropagationReference", jsii.get(self, "vpnGatewayRoutePropagationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPNGatewayRoutePropagationRef).__jsii_proxy_class__ = lambda : _IVPNGatewayRoutePropagationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVerifiedAccessEndpointRef")
class IVerifiedAccessEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VerifiedAccessEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="verifiedAccessEndpointRef")
    def verified_access_endpoint_ref(self) -> "VerifiedAccessEndpointReference":
        '''(experimental) A reference to a VerifiedAccessEndpoint resource.

        :stability: experimental
        '''
        ...


class _IVerifiedAccessEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VerifiedAccessEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVerifiedAccessEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="verifiedAccessEndpointRef")
    def verified_access_endpoint_ref(self) -> "VerifiedAccessEndpointReference":
        '''(experimental) A reference to a VerifiedAccessEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("VerifiedAccessEndpointReference", jsii.get(self, "verifiedAccessEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVerifiedAccessEndpointRef).__jsii_proxy_class__ = lambda : _IVerifiedAccessEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVerifiedAccessGroupRef")
class IVerifiedAccessGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VerifiedAccessGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="verifiedAccessGroupRef")
    def verified_access_group_ref(self) -> "VerifiedAccessGroupReference":
        '''(experimental) A reference to a VerifiedAccessGroup resource.

        :stability: experimental
        '''
        ...


class _IVerifiedAccessGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VerifiedAccessGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVerifiedAccessGroupRef"

    @builtins.property
    @jsii.member(jsii_name="verifiedAccessGroupRef")
    def verified_access_group_ref(self) -> "VerifiedAccessGroupReference":
        '''(experimental) A reference to a VerifiedAccessGroup resource.

        :stability: experimental
        '''
        return typing.cast("VerifiedAccessGroupReference", jsii.get(self, "verifiedAccessGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVerifiedAccessGroupRef).__jsii_proxy_class__ = lambda : _IVerifiedAccessGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVerifiedAccessInstanceRef")
class IVerifiedAccessInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VerifiedAccessInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="verifiedAccessInstanceRef")
    def verified_access_instance_ref(self) -> "VerifiedAccessInstanceReference":
        '''(experimental) A reference to a VerifiedAccessInstance resource.

        :stability: experimental
        '''
        ...


class _IVerifiedAccessInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VerifiedAccessInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVerifiedAccessInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="verifiedAccessInstanceRef")
    def verified_access_instance_ref(self) -> "VerifiedAccessInstanceReference":
        '''(experimental) A reference to a VerifiedAccessInstance resource.

        :stability: experimental
        '''
        return typing.cast("VerifiedAccessInstanceReference", jsii.get(self, "verifiedAccessInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVerifiedAccessInstanceRef).__jsii_proxy_class__ = lambda : _IVerifiedAccessInstanceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVerifiedAccessTrustProviderRef"
)
class IVerifiedAccessTrustProviderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VerifiedAccessTrustProvider.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="verifiedAccessTrustProviderRef")
    def verified_access_trust_provider_ref(
        self,
    ) -> "VerifiedAccessTrustProviderReference":
        '''(experimental) A reference to a VerifiedAccessTrustProvider resource.

        :stability: experimental
        '''
        ...


class _IVerifiedAccessTrustProviderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VerifiedAccessTrustProvider.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVerifiedAccessTrustProviderRef"

    @builtins.property
    @jsii.member(jsii_name="verifiedAccessTrustProviderRef")
    def verified_access_trust_provider_ref(
        self,
    ) -> "VerifiedAccessTrustProviderReference":
        '''(experimental) A reference to a VerifiedAccessTrustProvider resource.

        :stability: experimental
        '''
        return typing.cast("VerifiedAccessTrustProviderReference", jsii.get(self, "verifiedAccessTrustProviderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVerifiedAccessTrustProviderRef).__jsii_proxy_class__ = lambda : _IVerifiedAccessTrustProviderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVolumeAttachmentRef")
class IVolumeAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VolumeAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="volumeAttachmentRef")
    def volume_attachment_ref(self) -> "VolumeAttachmentReference":
        '''(experimental) A reference to a VolumeAttachment resource.

        :stability: experimental
        '''
        ...


class _IVolumeAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VolumeAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVolumeAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="volumeAttachmentRef")
    def volume_attachment_ref(self) -> "VolumeAttachmentReference":
        '''(experimental) A reference to a VolumeAttachment resource.

        :stability: experimental
        '''
        return typing.cast("VolumeAttachmentReference", jsii.get(self, "volumeAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVolumeAttachmentRef).__jsii_proxy_class__ = lambda : _IVolumeAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ec2.IVolumeRef")
class IVolumeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        ...


class _IVolumeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ec2.IVolumeRef"

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        return typing.cast("VolumeReference", jsii.get(self, "volumeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVolumeRef).__jsii_proxy_class__ = lambda : _IVolumeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.InstanceConnectEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"instance_connect_endpoint_id": "instanceConnectEndpointId"},
)
class InstanceConnectEndpointReference:
    def __init__(self, *, instance_connect_endpoint_id: builtins.str) -> None:
        '''A reference to a InstanceConnectEndpoint resource.

        :param instance_connect_endpoint_id: The Id of the InstanceConnectEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            instance_connect_endpoint_reference = interfaces_ec2.InstanceConnectEndpointReference(
                instance_connect_endpoint_id="instanceConnectEndpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04da4a11a170a51c13416eafbc1b7d6de587ae16bc76f69212089fec3dfd9e2d)
            check_type(argname="argument instance_connect_endpoint_id", value=instance_connect_endpoint_id, expected_type=type_hints["instance_connect_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_connect_endpoint_id": instance_connect_endpoint_id,
        }

    @builtins.property
    def instance_connect_endpoint_id(self) -> builtins.str:
        '''The Id of the InstanceConnectEndpoint resource.'''
        result = self._values.get("instance_connect_endpoint_id")
        assert result is not None, "Required property 'instance_connect_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceConnectEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.InstanceReference",
    jsii_struct_bases=[],
    name_mapping={"instance_id": "instanceId"},
)
class InstanceReference:
    def __init__(self, *, instance_id: builtins.str) -> None:
        '''A reference to a Instance resource.

        :param instance_id: The InstanceId of the Instance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            instance_reference = interfaces_ec2.InstanceReference(
                instance_id="instanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f06433ab2ca29228d26a3591c15861f26cba4cd81aba9c2d95cda5f8b7ddb93)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
        }

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The InstanceId of the Instance resource.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.InternetGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"internet_gateway_id": "internetGatewayId"},
)
class InternetGatewayReference:
    def __init__(self, *, internet_gateway_id: builtins.str) -> None:
        '''A reference to a InternetGateway resource.

        :param internet_gateway_id: The InternetGatewayId of the InternetGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            internet_gateway_reference = interfaces_ec2.InternetGatewayReference(
                internet_gateway_id="internetGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44bb15a882c5a2c056f5f6ae2f3ea1217cad905768d2e54391ba3718f7a8c283)
            check_type(argname="argument internet_gateway_id", value=internet_gateway_id, expected_type=type_hints["internet_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "internet_gateway_id": internet_gateway_id,
        }

    @builtins.property
    def internet_gateway_id(self) -> builtins.str:
        '''The InternetGatewayId of the InternetGateway resource.'''
        result = self._values.get("internet_gateway_id")
        assert result is not None, "Required property 'internet_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InternetGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.IpPoolRouteTableAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"association_id": "associationId"},
)
class IpPoolRouteTableAssociationReference:
    def __init__(self, *, association_id: builtins.str) -> None:
        '''A reference to a IpPoolRouteTableAssociation resource.

        :param association_id: The AssociationId of the IpPoolRouteTableAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            ip_pool_route_table_association_reference = interfaces_ec2.IpPoolRouteTableAssociationReference(
                association_id="associationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71fccb9d8f2781c81145acb20d4e9edac01046a309260fa70dfd46e9491669a0)
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_id": association_id,
        }

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the IpPoolRouteTableAssociation resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IpPoolRouteTableAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.KeyPairReference",
    jsii_struct_bases=[],
    name_mapping={"key_name": "keyName"},
)
class KeyPairReference:
    def __init__(self, *, key_name: builtins.str) -> None:
        '''A reference to a KeyPair resource.

        :param key_name: The KeyName of the KeyPair resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            key_pair_reference = interfaces_ec2.KeyPairReference(
                key_name="keyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61e5782f64150528470b5920f05080292456f4ab0004df01a7d5afe7c860185d)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key_name": key_name,
        }

    @builtins.property
    def key_name(self) -> builtins.str:
        '''The KeyName of the KeyPair resource.'''
        result = self._values.get("key_name")
        assert result is not None, "Required property 'key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyPairReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.LaunchTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"launch_template_id": "launchTemplateId"},
)
class LaunchTemplateReference:
    def __init__(self, *, launch_template_id: builtins.str) -> None:
        '''A reference to a LaunchTemplate resource.

        :param launch_template_id: The LaunchTemplateId of the LaunchTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            launch_template_reference = interfaces_ec2.LaunchTemplateReference(
                launch_template_id="launchTemplateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf47688316c53ea06bfbe8962e54c57c82ca920e2a4490a900c685306cb1a87b)
            check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_template_id": launch_template_id,
        }

    @builtins.property
    def launch_template_id(self) -> builtins.str:
        '''The LaunchTemplateId of the LaunchTemplate resource.'''
        result = self._values.get("launch_template_id")
        assert result is not None, "Required property 'launch_template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.LocalGatewayRouteReference",
    jsii_struct_bases=[],
    name_mapping={
        "destination_cidr_block": "destinationCidrBlock",
        "local_gateway_route_table_id": "localGatewayRouteTableId",
    },
)
class LocalGatewayRouteReference:
    def __init__(
        self,
        *,
        destination_cidr_block: builtins.str,
        local_gateway_route_table_id: builtins.str,
    ) -> None:
        '''A reference to a LocalGatewayRoute resource.

        :param destination_cidr_block: The DestinationCidrBlock of the LocalGatewayRoute resource.
        :param local_gateway_route_table_id: The LocalGatewayRouteTableId of the LocalGatewayRoute resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            local_gateway_route_reference = interfaces_ec2.LocalGatewayRouteReference(
                destination_cidr_block="destinationCidrBlock",
                local_gateway_route_table_id="localGatewayRouteTableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ba56b317ffe4dc9f02859993fc6b89e6bbbcc41dd1a50a72d27cd2dae68daff)
            check_type(argname="argument destination_cidr_block", value=destination_cidr_block, expected_type=type_hints["destination_cidr_block"])
            check_type(argname="argument local_gateway_route_table_id", value=local_gateway_route_table_id, expected_type=type_hints["local_gateway_route_table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_cidr_block": destination_cidr_block,
            "local_gateway_route_table_id": local_gateway_route_table_id,
        }

    @builtins.property
    def destination_cidr_block(self) -> builtins.str:
        '''The DestinationCidrBlock of the LocalGatewayRoute resource.'''
        result = self._values.get("destination_cidr_block")
        assert result is not None, "Required property 'destination_cidr_block' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def local_gateway_route_table_id(self) -> builtins.str:
        '''The LocalGatewayRouteTableId of the LocalGatewayRoute resource.'''
        result = self._values.get("local_gateway_route_table_id")
        assert result is not None, "Required property 'local_gateway_route_table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocalGatewayRouteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.LocalGatewayRouteTableReference",
    jsii_struct_bases=[],
    name_mapping={
        "local_gateway_route_table_arn": "localGatewayRouteTableArn",
        "local_gateway_route_table_id": "localGatewayRouteTableId",
    },
)
class LocalGatewayRouteTableReference:
    def __init__(
        self,
        *,
        local_gateway_route_table_arn: builtins.str,
        local_gateway_route_table_id: builtins.str,
    ) -> None:
        '''A reference to a LocalGatewayRouteTable resource.

        :param local_gateway_route_table_arn: The ARN of the LocalGatewayRouteTable resource.
        :param local_gateway_route_table_id: The LocalGatewayRouteTableId of the LocalGatewayRouteTable resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            local_gateway_route_table_reference = interfaces_ec2.LocalGatewayRouteTableReference(
                local_gateway_route_table_arn="localGatewayRouteTableArn",
                local_gateway_route_table_id="localGatewayRouteTableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4d3ef1777d1ce52dbb1979acf4bb44d1f866b94d6fce26dcda3c6bbdbeed15e)
            check_type(argname="argument local_gateway_route_table_arn", value=local_gateway_route_table_arn, expected_type=type_hints["local_gateway_route_table_arn"])
            check_type(argname="argument local_gateway_route_table_id", value=local_gateway_route_table_id, expected_type=type_hints["local_gateway_route_table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "local_gateway_route_table_arn": local_gateway_route_table_arn,
            "local_gateway_route_table_id": local_gateway_route_table_id,
        }

    @builtins.property
    def local_gateway_route_table_arn(self) -> builtins.str:
        '''The ARN of the LocalGatewayRouteTable resource.'''
        result = self._values.get("local_gateway_route_table_arn")
        assert result is not None, "Required property 'local_gateway_route_table_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def local_gateway_route_table_id(self) -> builtins.str:
        '''The LocalGatewayRouteTableId of the LocalGatewayRouteTable resource.'''
        result = self._values.get("local_gateway_route_table_id")
        assert result is not None, "Required property 'local_gateway_route_table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocalGatewayRouteTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.LocalGatewayRouteTableVPCAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "local_gateway_route_table_vpc_association_id": "localGatewayRouteTableVpcAssociationId",
    },
)
class LocalGatewayRouteTableVPCAssociationReference:
    def __init__(
        self,
        *,
        local_gateway_route_table_vpc_association_id: builtins.str,
    ) -> None:
        '''A reference to a LocalGatewayRouteTableVPCAssociation resource.

        :param local_gateway_route_table_vpc_association_id: The LocalGatewayRouteTableVpcAssociationId of the LocalGatewayRouteTableVPCAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            local_gateway_route_table_vPCAssociation_reference = interfaces_ec2.LocalGatewayRouteTableVPCAssociationReference(
                local_gateway_route_table_vpc_association_id="localGatewayRouteTableVpcAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723ff6293ea9c624c32784a1606ec5d4a9a0ce6894e65dd54743fbb3288df447)
            check_type(argname="argument local_gateway_route_table_vpc_association_id", value=local_gateway_route_table_vpc_association_id, expected_type=type_hints["local_gateway_route_table_vpc_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "local_gateway_route_table_vpc_association_id": local_gateway_route_table_vpc_association_id,
        }

    @builtins.property
    def local_gateway_route_table_vpc_association_id(self) -> builtins.str:
        '''The LocalGatewayRouteTableVpcAssociationId of the LocalGatewayRouteTableVPCAssociation resource.'''
        result = self._values.get("local_gateway_route_table_vpc_association_id")
        assert result is not None, "Required property 'local_gateway_route_table_vpc_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocalGatewayRouteTableVPCAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.LocalGatewayRouteTableVirtualInterfaceGroupAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "local_gateway_route_table_virtual_interface_group_association_id": "localGatewayRouteTableVirtualInterfaceGroupAssociationId",
    },
)
class LocalGatewayRouteTableVirtualInterfaceGroupAssociationReference:
    def __init__(
        self,
        *,
        local_gateway_route_table_virtual_interface_group_association_id: builtins.str,
    ) -> None:
        '''A reference to a LocalGatewayRouteTableVirtualInterfaceGroupAssociation resource.

        :param local_gateway_route_table_virtual_interface_group_association_id: The LocalGatewayRouteTableVirtualInterfaceGroupAssociationId of the LocalGatewayRouteTableVirtualInterfaceGroupAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            local_gateway_route_table_virtual_interface_group_association_reference = interfaces_ec2.LocalGatewayRouteTableVirtualInterfaceGroupAssociationReference(
                local_gateway_route_table_virtual_interface_group_association_id="localGatewayRouteTableVirtualInterfaceGroupAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0076a6af4d4d2b3e177ad2bcea7af4a8750788c36d756571817af42a9bc1795)
            check_type(argname="argument local_gateway_route_table_virtual_interface_group_association_id", value=local_gateway_route_table_virtual_interface_group_association_id, expected_type=type_hints["local_gateway_route_table_virtual_interface_group_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "local_gateway_route_table_virtual_interface_group_association_id": local_gateway_route_table_virtual_interface_group_association_id,
        }

    @builtins.property
    def local_gateway_route_table_virtual_interface_group_association_id(
        self,
    ) -> builtins.str:
        '''The LocalGatewayRouteTableVirtualInterfaceGroupAssociationId of the LocalGatewayRouteTableVirtualInterfaceGroupAssociation resource.'''
        result = self._values.get("local_gateway_route_table_virtual_interface_group_association_id")
        assert result is not None, "Required property 'local_gateway_route_table_virtual_interface_group_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocalGatewayRouteTableVirtualInterfaceGroupAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.LocalGatewayVirtualInterfaceGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "local_gateway_virtual_interface_group_arn": "localGatewayVirtualInterfaceGroupArn",
        "local_gateway_virtual_interface_group_id": "localGatewayVirtualInterfaceGroupId",
    },
)
class LocalGatewayVirtualInterfaceGroupReference:
    def __init__(
        self,
        *,
        local_gateway_virtual_interface_group_arn: builtins.str,
        local_gateway_virtual_interface_group_id: builtins.str,
    ) -> None:
        '''A reference to a LocalGatewayVirtualInterfaceGroup resource.

        :param local_gateway_virtual_interface_group_arn: The ARN of the LocalGatewayVirtualInterfaceGroup resource.
        :param local_gateway_virtual_interface_group_id: The LocalGatewayVirtualInterfaceGroupId of the LocalGatewayVirtualInterfaceGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            local_gateway_virtual_interface_group_reference = interfaces_ec2.LocalGatewayVirtualInterfaceGroupReference(
                local_gateway_virtual_interface_group_arn="localGatewayVirtualInterfaceGroupArn",
                local_gateway_virtual_interface_group_id="localGatewayVirtualInterfaceGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c90fb542fdb8637b80e36f928d9aeceac19bf3776dfe903d370479c61f0d98e)
            check_type(argname="argument local_gateway_virtual_interface_group_arn", value=local_gateway_virtual_interface_group_arn, expected_type=type_hints["local_gateway_virtual_interface_group_arn"])
            check_type(argname="argument local_gateway_virtual_interface_group_id", value=local_gateway_virtual_interface_group_id, expected_type=type_hints["local_gateway_virtual_interface_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "local_gateway_virtual_interface_group_arn": local_gateway_virtual_interface_group_arn,
            "local_gateway_virtual_interface_group_id": local_gateway_virtual_interface_group_id,
        }

    @builtins.property
    def local_gateway_virtual_interface_group_arn(self) -> builtins.str:
        '''The ARN of the LocalGatewayVirtualInterfaceGroup resource.'''
        result = self._values.get("local_gateway_virtual_interface_group_arn")
        assert result is not None, "Required property 'local_gateway_virtual_interface_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def local_gateway_virtual_interface_group_id(self) -> builtins.str:
        '''The LocalGatewayVirtualInterfaceGroupId of the LocalGatewayVirtualInterfaceGroup resource.'''
        result = self._values.get("local_gateway_virtual_interface_group_id")
        assert result is not None, "Required property 'local_gateway_virtual_interface_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocalGatewayVirtualInterfaceGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.LocalGatewayVirtualInterfaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "local_gateway_virtual_interface_id": "localGatewayVirtualInterfaceId",
    },
)
class LocalGatewayVirtualInterfaceReference:
    def __init__(self, *, local_gateway_virtual_interface_id: builtins.str) -> None:
        '''A reference to a LocalGatewayVirtualInterface resource.

        :param local_gateway_virtual_interface_id: The LocalGatewayVirtualInterfaceId of the LocalGatewayVirtualInterface resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            local_gateway_virtual_interface_reference = interfaces_ec2.LocalGatewayVirtualInterfaceReference(
                local_gateway_virtual_interface_id="localGatewayVirtualInterfaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d5bf34161cfcac3c7f30d5f7b7235fdbb2ef9fbd82094e8dab5402940143604)
            check_type(argname="argument local_gateway_virtual_interface_id", value=local_gateway_virtual_interface_id, expected_type=type_hints["local_gateway_virtual_interface_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "local_gateway_virtual_interface_id": local_gateway_virtual_interface_id,
        }

    @builtins.property
    def local_gateway_virtual_interface_id(self) -> builtins.str:
        '''The LocalGatewayVirtualInterfaceId of the LocalGatewayVirtualInterface resource.'''
        result = self._values.get("local_gateway_virtual_interface_id")
        assert result is not None, "Required property 'local_gateway_virtual_interface_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocalGatewayVirtualInterfaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NatGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"nat_gateway_id": "natGatewayId"},
)
class NatGatewayReference:
    def __init__(self, *, nat_gateway_id: builtins.str) -> None:
        '''A reference to a NatGateway resource.

        :param nat_gateway_id: The NatGatewayId of the NatGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            nat_gateway_reference = interfaces_ec2.NatGatewayReference(
                nat_gateway_id="natGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9284f94b93190b143fb72727e011f823e94d36b5c25f65e1bd8cee3b963d87b6)
            check_type(argname="argument nat_gateway_id", value=nat_gateway_id, expected_type=type_hints["nat_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "nat_gateway_id": nat_gateway_id,
        }

    @builtins.property
    def nat_gateway_id(self) -> builtins.str:
        '''The NatGatewayId of the NatGateway resource.'''
        result = self._values.get("nat_gateway_id")
        assert result is not None, "Required property 'nat_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NatGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkAclEntryReference",
    jsii_struct_bases=[],
    name_mapping={"network_acl_entry_id": "networkAclEntryId"},
)
class NetworkAclEntryReference:
    def __init__(self, *, network_acl_entry_id: builtins.str) -> None:
        '''A reference to a NetworkAclEntry resource.

        :param network_acl_entry_id: The Id of the NetworkAclEntry resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_acl_entry_reference = interfaces_ec2.NetworkAclEntryReference(
                network_acl_entry_id="networkAclEntryId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27f02a8f8524fa23ca08af1d692e0639a10fc0d9e01667fcd46edd61ce7c70ba)
            check_type(argname="argument network_acl_entry_id", value=network_acl_entry_id, expected_type=type_hints["network_acl_entry_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_acl_entry_id": network_acl_entry_id,
        }

    @builtins.property
    def network_acl_entry_id(self) -> builtins.str:
        '''The Id of the NetworkAclEntry resource.'''
        result = self._values.get("network_acl_entry_id")
        assert result is not None, "Required property 'network_acl_entry_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkAclEntryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkAclReference",
    jsii_struct_bases=[],
    name_mapping={"network_acl_id": "networkAclId"},
)
class NetworkAclReference:
    def __init__(self, *, network_acl_id: builtins.str) -> None:
        '''A reference to a NetworkAcl resource.

        :param network_acl_id: The Id of the NetworkAcl resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_acl_reference = interfaces_ec2.NetworkAclReference(
                network_acl_id="networkAclId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c66ff6eb994eb559c72f9480f9db93a2eeb06c8c6d37ef4e6525316539cc49e5)
            check_type(argname="argument network_acl_id", value=network_acl_id, expected_type=type_hints["network_acl_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_acl_id": network_acl_id,
        }

    @builtins.property
    def network_acl_id(self) -> builtins.str:
        '''The Id of the NetworkAcl resource.'''
        result = self._values.get("network_acl_id")
        assert result is not None, "Required property 'network_acl_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkAclReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkInsightsAccessScopeAnalysisReference",
    jsii_struct_bases=[],
    name_mapping={
        "network_insights_access_scope_analysis_arn": "networkInsightsAccessScopeAnalysisArn",
        "network_insights_access_scope_analysis_id": "networkInsightsAccessScopeAnalysisId",
    },
)
class NetworkInsightsAccessScopeAnalysisReference:
    def __init__(
        self,
        *,
        network_insights_access_scope_analysis_arn: builtins.str,
        network_insights_access_scope_analysis_id: builtins.str,
    ) -> None:
        '''A reference to a NetworkInsightsAccessScopeAnalysis resource.

        :param network_insights_access_scope_analysis_arn: The ARN of the NetworkInsightsAccessScopeAnalysis resource.
        :param network_insights_access_scope_analysis_id: The NetworkInsightsAccessScopeAnalysisId of the NetworkInsightsAccessScopeAnalysis resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_insights_access_scope_analysis_reference = interfaces_ec2.NetworkInsightsAccessScopeAnalysisReference(
                network_insights_access_scope_analysis_arn="networkInsightsAccessScopeAnalysisArn",
                network_insights_access_scope_analysis_id="networkInsightsAccessScopeAnalysisId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b304b9f1134521a55ecdd3ca088bf067a718845c1201a93e296c0ab9a63efd7)
            check_type(argname="argument network_insights_access_scope_analysis_arn", value=network_insights_access_scope_analysis_arn, expected_type=type_hints["network_insights_access_scope_analysis_arn"])
            check_type(argname="argument network_insights_access_scope_analysis_id", value=network_insights_access_scope_analysis_id, expected_type=type_hints["network_insights_access_scope_analysis_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_insights_access_scope_analysis_arn": network_insights_access_scope_analysis_arn,
            "network_insights_access_scope_analysis_id": network_insights_access_scope_analysis_id,
        }

    @builtins.property
    def network_insights_access_scope_analysis_arn(self) -> builtins.str:
        '''The ARN of the NetworkInsightsAccessScopeAnalysis resource.'''
        result = self._values.get("network_insights_access_scope_analysis_arn")
        assert result is not None, "Required property 'network_insights_access_scope_analysis_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_insights_access_scope_analysis_id(self) -> builtins.str:
        '''The NetworkInsightsAccessScopeAnalysisId of the NetworkInsightsAccessScopeAnalysis resource.'''
        result = self._values.get("network_insights_access_scope_analysis_id")
        assert result is not None, "Required property 'network_insights_access_scope_analysis_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInsightsAccessScopeAnalysisReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkInsightsAccessScopeReference",
    jsii_struct_bases=[],
    name_mapping={
        "network_insights_access_scope_arn": "networkInsightsAccessScopeArn",
        "network_insights_access_scope_id": "networkInsightsAccessScopeId",
    },
)
class NetworkInsightsAccessScopeReference:
    def __init__(
        self,
        *,
        network_insights_access_scope_arn: builtins.str,
        network_insights_access_scope_id: builtins.str,
    ) -> None:
        '''A reference to a NetworkInsightsAccessScope resource.

        :param network_insights_access_scope_arn: The ARN of the NetworkInsightsAccessScope resource.
        :param network_insights_access_scope_id: The NetworkInsightsAccessScopeId of the NetworkInsightsAccessScope resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_insights_access_scope_reference = interfaces_ec2.NetworkInsightsAccessScopeReference(
                network_insights_access_scope_arn="networkInsightsAccessScopeArn",
                network_insights_access_scope_id="networkInsightsAccessScopeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df6fa29d56c295e8cc643265a349fa9299af85d29a099b44f05f728333bc7d68)
            check_type(argname="argument network_insights_access_scope_arn", value=network_insights_access_scope_arn, expected_type=type_hints["network_insights_access_scope_arn"])
            check_type(argname="argument network_insights_access_scope_id", value=network_insights_access_scope_id, expected_type=type_hints["network_insights_access_scope_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_insights_access_scope_arn": network_insights_access_scope_arn,
            "network_insights_access_scope_id": network_insights_access_scope_id,
        }

    @builtins.property
    def network_insights_access_scope_arn(self) -> builtins.str:
        '''The ARN of the NetworkInsightsAccessScope resource.'''
        result = self._values.get("network_insights_access_scope_arn")
        assert result is not None, "Required property 'network_insights_access_scope_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_insights_access_scope_id(self) -> builtins.str:
        '''The NetworkInsightsAccessScopeId of the NetworkInsightsAccessScope resource.'''
        result = self._values.get("network_insights_access_scope_id")
        assert result is not None, "Required property 'network_insights_access_scope_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInsightsAccessScopeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkInsightsAnalysisReference",
    jsii_struct_bases=[],
    name_mapping={
        "network_insights_analysis_arn": "networkInsightsAnalysisArn",
        "network_insights_analysis_id": "networkInsightsAnalysisId",
    },
)
class NetworkInsightsAnalysisReference:
    def __init__(
        self,
        *,
        network_insights_analysis_arn: builtins.str,
        network_insights_analysis_id: builtins.str,
    ) -> None:
        '''A reference to a NetworkInsightsAnalysis resource.

        :param network_insights_analysis_arn: The ARN of the NetworkInsightsAnalysis resource.
        :param network_insights_analysis_id: The NetworkInsightsAnalysisId of the NetworkInsightsAnalysis resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_insights_analysis_reference = interfaces_ec2.NetworkInsightsAnalysisReference(
                network_insights_analysis_arn="networkInsightsAnalysisArn",
                network_insights_analysis_id="networkInsightsAnalysisId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41c5de5540a2b0098d268fa120f8031f855048589a832d2a31a668185bbddab1)
            check_type(argname="argument network_insights_analysis_arn", value=network_insights_analysis_arn, expected_type=type_hints["network_insights_analysis_arn"])
            check_type(argname="argument network_insights_analysis_id", value=network_insights_analysis_id, expected_type=type_hints["network_insights_analysis_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_insights_analysis_arn": network_insights_analysis_arn,
            "network_insights_analysis_id": network_insights_analysis_id,
        }

    @builtins.property
    def network_insights_analysis_arn(self) -> builtins.str:
        '''The ARN of the NetworkInsightsAnalysis resource.'''
        result = self._values.get("network_insights_analysis_arn")
        assert result is not None, "Required property 'network_insights_analysis_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_insights_analysis_id(self) -> builtins.str:
        '''The NetworkInsightsAnalysisId of the NetworkInsightsAnalysis resource.'''
        result = self._values.get("network_insights_analysis_id")
        assert result is not None, "Required property 'network_insights_analysis_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInsightsAnalysisReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkInsightsPathReference",
    jsii_struct_bases=[],
    name_mapping={
        "network_insights_path_arn": "networkInsightsPathArn",
        "network_insights_path_id": "networkInsightsPathId",
    },
)
class NetworkInsightsPathReference:
    def __init__(
        self,
        *,
        network_insights_path_arn: builtins.str,
        network_insights_path_id: builtins.str,
    ) -> None:
        '''A reference to a NetworkInsightsPath resource.

        :param network_insights_path_arn: The ARN of the NetworkInsightsPath resource.
        :param network_insights_path_id: The NetworkInsightsPathId of the NetworkInsightsPath resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_insights_path_reference = interfaces_ec2.NetworkInsightsPathReference(
                network_insights_path_arn="networkInsightsPathArn",
                network_insights_path_id="networkInsightsPathId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66a7973f92c21942c518f8eeb207fddd4f05cd8a3b3d6d4b882c4fec4bcd415b)
            check_type(argname="argument network_insights_path_arn", value=network_insights_path_arn, expected_type=type_hints["network_insights_path_arn"])
            check_type(argname="argument network_insights_path_id", value=network_insights_path_id, expected_type=type_hints["network_insights_path_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_insights_path_arn": network_insights_path_arn,
            "network_insights_path_id": network_insights_path_id,
        }

    @builtins.property
    def network_insights_path_arn(self) -> builtins.str:
        '''The ARN of the NetworkInsightsPath resource.'''
        result = self._values.get("network_insights_path_arn")
        assert result is not None, "Required property 'network_insights_path_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_insights_path_id(self) -> builtins.str:
        '''The NetworkInsightsPathId of the NetworkInsightsPath resource.'''
        result = self._values.get("network_insights_path_id")
        assert result is not None, "Required property 'network_insights_path_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInsightsPathReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkInterfaceAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"attachment_id": "attachmentId"},
)
class NetworkInterfaceAttachmentReference:
    def __init__(self, *, attachment_id: builtins.str) -> None:
        '''A reference to a NetworkInterfaceAttachment resource.

        :param attachment_id: The AttachmentId of the NetworkInterfaceAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_interface_attachment_reference = interfaces_ec2.NetworkInterfaceAttachmentReference(
                attachment_id="attachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c88066168b198ea6639664fda4fc84ed5b24c2b90541bb4cc402eacbcf26c1a)
            check_type(argname="argument attachment_id", value=attachment_id, expected_type=type_hints["attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attachment_id": attachment_id,
        }

    @builtins.property
    def attachment_id(self) -> builtins.str:
        '''The AttachmentId of the NetworkInterfaceAttachment resource.'''
        result = self._values.get("attachment_id")
        assert result is not None, "Required property 'attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInterfaceAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkInterfacePermissionReference",
    jsii_struct_bases=[],
    name_mapping={"network_interface_permission_id": "networkInterfacePermissionId"},
)
class NetworkInterfacePermissionReference:
    def __init__(self, *, network_interface_permission_id: builtins.str) -> None:
        '''A reference to a NetworkInterfacePermission resource.

        :param network_interface_permission_id: The Id of the NetworkInterfacePermission resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_interface_permission_reference = interfaces_ec2.NetworkInterfacePermissionReference(
                network_interface_permission_id="networkInterfacePermissionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd3c3c5b9969f763f0c64ce39c680f2e98370b3255f0d5a443eae02ab17ce9bd)
            check_type(argname="argument network_interface_permission_id", value=network_interface_permission_id, expected_type=type_hints["network_interface_permission_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_interface_permission_id": network_interface_permission_id,
        }

    @builtins.property
    def network_interface_permission_id(self) -> builtins.str:
        '''The Id of the NetworkInterfacePermission resource.'''
        result = self._values.get("network_interface_permission_id")
        assert result is not None, "Required property 'network_interface_permission_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInterfacePermissionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkInterfaceReference",
    jsii_struct_bases=[],
    name_mapping={"network_interface_id": "networkInterfaceId"},
)
class NetworkInterfaceReference:
    def __init__(self, *, network_interface_id: builtins.str) -> None:
        '''A reference to a NetworkInterface resource.

        :param network_interface_id: The Id of the NetworkInterface resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_interface_reference = interfaces_ec2.NetworkInterfaceReference(
                network_interface_id="networkInterfaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5919adb4a6febe429841e83e6060ccb4cbef8c3abc4f8e3b6d90e67f7774664b)
            check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_interface_id": network_interface_id,
        }

    @builtins.property
    def network_interface_id(self) -> builtins.str:
        '''The Id of the NetworkInterface resource.'''
        result = self._values.get("network_interface_id")
        assert result is not None, "Required property 'network_interface_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkInterfaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.NetworkPerformanceMetricSubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "metric": "metric",
        "source": "source",
        "statistic": "statistic",
    },
)
class NetworkPerformanceMetricSubscriptionReference:
    def __init__(
        self,
        *,
        destination: builtins.str,
        metric: builtins.str,
        source: builtins.str,
        statistic: builtins.str,
    ) -> None:
        '''A reference to a NetworkPerformanceMetricSubscription resource.

        :param destination: The Destination of the NetworkPerformanceMetricSubscription resource.
        :param metric: The Metric of the NetworkPerformanceMetricSubscription resource.
        :param source: The Source of the NetworkPerformanceMetricSubscription resource.
        :param statistic: The Statistic of the NetworkPerformanceMetricSubscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            network_performance_metric_subscription_reference = interfaces_ec2.NetworkPerformanceMetricSubscriptionReference(
                destination="destination",
                metric="metric",
                source="source",
                statistic="statistic"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae7ca3b2520848fb208f1f073b999fa18862f731f22e0ed61b0f33e113e84314)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument statistic", value=statistic, expected_type=type_hints["statistic"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "metric": metric,
            "source": source,
            "statistic": statistic,
        }

    @builtins.property
    def destination(self) -> builtins.str:
        '''The Destination of the NetworkPerformanceMetricSubscription resource.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric(self) -> builtins.str:
        '''The Metric of the NetworkPerformanceMetricSubscription resource.'''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''The Source of the NetworkPerformanceMetricSubscription resource.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statistic(self) -> builtins.str:
        '''The Statistic of the NetworkPerformanceMetricSubscription resource.'''
        result = self._values.get("statistic")
        assert result is not None, "Required property 'statistic' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkPerformanceMetricSubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.PlacementGroupReference",
    jsii_struct_bases=[],
    name_mapping={"group_name": "groupName"},
)
class PlacementGroupReference:
    def __init__(self, *, group_name: builtins.str) -> None:
        '''A reference to a PlacementGroup resource.

        :param group_name: The GroupName of the PlacementGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            placement_group_reference = interfaces_ec2.PlacementGroupReference(
                group_name="groupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5765f3379a78633c12e5a0f7f44b8607e7ec0673147343d6ed57ff461fe296d5)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
        }

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The GroupName of the PlacementGroup resource.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlacementGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.PrefixListReference",
    jsii_struct_bases=[],
    name_mapping={
        "prefix_list_arn": "prefixListArn",
        "prefix_list_id": "prefixListId",
    },
)
class PrefixListReference:
    def __init__(
        self,
        *,
        prefix_list_arn: builtins.str,
        prefix_list_id: builtins.str,
    ) -> None:
        '''A reference to a PrefixList resource.

        :param prefix_list_arn: The ARN of the PrefixList resource.
        :param prefix_list_id: The PrefixListId of the PrefixList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            prefix_list_reference = interfaces_ec2.PrefixListReference(
                prefix_list_arn="prefixListArn",
                prefix_list_id="prefixListId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5511f84caafda82a5823be04257a6bc66b8e650cafde60346ea5dba962bbe45f)
            check_type(argname="argument prefix_list_arn", value=prefix_list_arn, expected_type=type_hints["prefix_list_arn"])
            check_type(argname="argument prefix_list_id", value=prefix_list_id, expected_type=type_hints["prefix_list_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prefix_list_arn": prefix_list_arn,
            "prefix_list_id": prefix_list_id,
        }

    @builtins.property
    def prefix_list_arn(self) -> builtins.str:
        '''The ARN of the PrefixList resource.'''
        result = self._values.get("prefix_list_arn")
        assert result is not None, "Required property 'prefix_list_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def prefix_list_id(self) -> builtins.str:
        '''The PrefixListId of the PrefixList resource.'''
        result = self._values.get("prefix_list_id")
        assert result is not None, "Required property 'prefix_list_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrefixListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.RouteReference",
    jsii_struct_bases=[],
    name_mapping={"cidr_block": "cidrBlock", "route_table_id": "routeTableId"},
)
class RouteReference:
    def __init__(
        self,
        *,
        cidr_block: builtins.str,
        route_table_id: builtins.str,
    ) -> None:
        '''A reference to a Route resource.

        :param cidr_block: The CidrBlock of the Route resource.
        :param route_table_id: The RouteTableId of the Route resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            route_reference = interfaces_ec2.RouteReference(
                cidr_block="cidrBlock",
                route_table_id="routeTableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071d8281200dbc8a56815f028a15047533e43d4006bd454bb2112a062187aab6)
            check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
            check_type(argname="argument route_table_id", value=route_table_id, expected_type=type_hints["route_table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cidr_block": cidr_block,
            "route_table_id": route_table_id,
        }

    @builtins.property
    def cidr_block(self) -> builtins.str:
        '''The CidrBlock of the Route resource.'''
        result = self._values.get("cidr_block")
        assert result is not None, "Required property 'cidr_block' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_table_id(self) -> builtins.str:
        '''The RouteTableId of the Route resource.'''
        result = self._values.get("route_table_id")
        assert result is not None, "Required property 'route_table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.RouteServerAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"route_server_id": "routeServerId", "vpc_id": "vpcId"},
)
class RouteServerAssociationReference:
    def __init__(self, *, route_server_id: builtins.str, vpc_id: builtins.str) -> None:
        '''A reference to a RouteServerAssociation resource.

        :param route_server_id: The RouteServerId of the RouteServerAssociation resource.
        :param vpc_id: The VpcId of the RouteServerAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            route_server_association_reference = interfaces_ec2.RouteServerAssociationReference(
                route_server_id="routeServerId",
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32c2b597b0ef56b2be955617b20c204c3229f2200a027ab101729b15cdd488fa)
            check_type(argname="argument route_server_id", value=route_server_id, expected_type=type_hints["route_server_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "route_server_id": route_server_id,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def route_server_id(self) -> builtins.str:
        '''The RouteServerId of the RouteServerAssociation resource.'''
        result = self._values.get("route_server_id")
        assert result is not None, "Required property 'route_server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VpcId of the RouteServerAssociation resource.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteServerAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.RouteServerEndpointReference",
    jsii_struct_bases=[],
    name_mapping={
        "route_server_endpoint_arn": "routeServerEndpointArn",
        "route_server_endpoint_id": "routeServerEndpointId",
    },
)
class RouteServerEndpointReference:
    def __init__(
        self,
        *,
        route_server_endpoint_arn: builtins.str,
        route_server_endpoint_id: builtins.str,
    ) -> None:
        '''A reference to a RouteServerEndpoint resource.

        :param route_server_endpoint_arn: The ARN of the RouteServerEndpoint resource.
        :param route_server_endpoint_id: The Id of the RouteServerEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            route_server_endpoint_reference = interfaces_ec2.RouteServerEndpointReference(
                route_server_endpoint_arn="routeServerEndpointArn",
                route_server_endpoint_id="routeServerEndpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__604ffb342b3bdc73a00058584dee047a0c158a0fa83d67bf2ec1d41fcbb63ebc)
            check_type(argname="argument route_server_endpoint_arn", value=route_server_endpoint_arn, expected_type=type_hints["route_server_endpoint_arn"])
            check_type(argname="argument route_server_endpoint_id", value=route_server_endpoint_id, expected_type=type_hints["route_server_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "route_server_endpoint_arn": route_server_endpoint_arn,
            "route_server_endpoint_id": route_server_endpoint_id,
        }

    @builtins.property
    def route_server_endpoint_arn(self) -> builtins.str:
        '''The ARN of the RouteServerEndpoint resource.'''
        result = self._values.get("route_server_endpoint_arn")
        assert result is not None, "Required property 'route_server_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_server_endpoint_id(self) -> builtins.str:
        '''The Id of the RouteServerEndpoint resource.'''
        result = self._values.get("route_server_endpoint_id")
        assert result is not None, "Required property 'route_server_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteServerEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.RouteServerPeerReference",
    jsii_struct_bases=[],
    name_mapping={
        "route_server_peer_arn": "routeServerPeerArn",
        "route_server_peer_id": "routeServerPeerId",
    },
)
class RouteServerPeerReference:
    def __init__(
        self,
        *,
        route_server_peer_arn: builtins.str,
        route_server_peer_id: builtins.str,
    ) -> None:
        '''A reference to a RouteServerPeer resource.

        :param route_server_peer_arn: The ARN of the RouteServerPeer resource.
        :param route_server_peer_id: The Id of the RouteServerPeer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            route_server_peer_reference = interfaces_ec2.RouteServerPeerReference(
                route_server_peer_arn="routeServerPeerArn",
                route_server_peer_id="routeServerPeerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6236f4a0ba03f39efd5e1046cbc3f9787eab627bd9c7605cbb239e875dff53f)
            check_type(argname="argument route_server_peer_arn", value=route_server_peer_arn, expected_type=type_hints["route_server_peer_arn"])
            check_type(argname="argument route_server_peer_id", value=route_server_peer_id, expected_type=type_hints["route_server_peer_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "route_server_peer_arn": route_server_peer_arn,
            "route_server_peer_id": route_server_peer_id,
        }

    @builtins.property
    def route_server_peer_arn(self) -> builtins.str:
        '''The ARN of the RouteServerPeer resource.'''
        result = self._values.get("route_server_peer_arn")
        assert result is not None, "Required property 'route_server_peer_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_server_peer_id(self) -> builtins.str:
        '''The Id of the RouteServerPeer resource.'''
        result = self._values.get("route_server_peer_id")
        assert result is not None, "Required property 'route_server_peer_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteServerPeerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.RouteServerPropagationReference",
    jsii_struct_bases=[],
    name_mapping={
        "route_server_id": "routeServerId",
        "route_table_id": "routeTableId",
    },
)
class RouteServerPropagationReference:
    def __init__(
        self,
        *,
        route_server_id: builtins.str,
        route_table_id: builtins.str,
    ) -> None:
        '''A reference to a RouteServerPropagation resource.

        :param route_server_id: The RouteServerId of the RouteServerPropagation resource.
        :param route_table_id: The RouteTableId of the RouteServerPropagation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            route_server_propagation_reference = interfaces_ec2.RouteServerPropagationReference(
                route_server_id="routeServerId",
                route_table_id="routeTableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec6dc1a55da909a26dc9a339b304e6d77d5744cf4ff250a9f9be3d9b775a66e4)
            check_type(argname="argument route_server_id", value=route_server_id, expected_type=type_hints["route_server_id"])
            check_type(argname="argument route_table_id", value=route_table_id, expected_type=type_hints["route_table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "route_server_id": route_server_id,
            "route_table_id": route_table_id,
        }

    @builtins.property
    def route_server_id(self) -> builtins.str:
        '''The RouteServerId of the RouteServerPropagation resource.'''
        result = self._values.get("route_server_id")
        assert result is not None, "Required property 'route_server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_table_id(self) -> builtins.str:
        '''The RouteTableId of the RouteServerPropagation resource.'''
        result = self._values.get("route_table_id")
        assert result is not None, "Required property 'route_table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteServerPropagationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.RouteServerReference",
    jsii_struct_bases=[],
    name_mapping={
        "route_server_arn": "routeServerArn",
        "route_server_id": "routeServerId",
    },
)
class RouteServerReference:
    def __init__(
        self,
        *,
        route_server_arn: builtins.str,
        route_server_id: builtins.str,
    ) -> None:
        '''A reference to a RouteServer resource.

        :param route_server_arn: The ARN of the RouteServer resource.
        :param route_server_id: The Id of the RouteServer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            route_server_reference = interfaces_ec2.RouteServerReference(
                route_server_arn="routeServerArn",
                route_server_id="routeServerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efff2c3f9e57b3b247745af2b155b69f9d9e3ead1daec3dd115ce2158e01e375)
            check_type(argname="argument route_server_arn", value=route_server_arn, expected_type=type_hints["route_server_arn"])
            check_type(argname="argument route_server_id", value=route_server_id, expected_type=type_hints["route_server_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "route_server_arn": route_server_arn,
            "route_server_id": route_server_id,
        }

    @builtins.property
    def route_server_arn(self) -> builtins.str:
        '''The ARN of the RouteServer resource.'''
        result = self._values.get("route_server_arn")
        assert result is not None, "Required property 'route_server_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_server_id(self) -> builtins.str:
        '''The Id of the RouteServer resource.'''
        result = self._values.get("route_server_id")
        assert result is not None, "Required property 'route_server_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteServerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.RouteTableReference",
    jsii_struct_bases=[],
    name_mapping={"route_table_id": "routeTableId"},
)
class RouteTableReference:
    def __init__(self, *, route_table_id: builtins.str) -> None:
        '''A reference to a RouteTable resource.

        :param route_table_id: The RouteTableId of the RouteTable resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            route_table_reference = interfaces_ec2.RouteTableReference(
                route_table_id="routeTableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__188eecb4e01c772367f802e75fe78a87fe1af4420eb919a629db4f794178d131)
            check_type(argname="argument route_table_id", value=route_table_id, expected_type=type_hints["route_table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "route_table_id": route_table_id,
        }

    @builtins.property
    def route_table_id(self) -> builtins.str:
        '''The RouteTableId of the RouteTable resource.'''
        result = self._values.get("route_table_id")
        assert result is not None, "Required property 'route_table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SecurityGroupEgressReference",
    jsii_struct_bases=[],
    name_mapping={"security_group_egress_id": "securityGroupEgressId"},
)
class SecurityGroupEgressReference:
    def __init__(self, *, security_group_egress_id: builtins.str) -> None:
        '''A reference to a SecurityGroupEgress resource.

        :param security_group_egress_id: The Id of the SecurityGroupEgress resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            security_group_egress_reference = interfaces_ec2.SecurityGroupEgressReference(
                security_group_egress_id="securityGroupEgressId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0be0b2564d7c31d9bc03311d9327527e8e38438583c1dddcc84256ea3117542)
            check_type(argname="argument security_group_egress_id", value=security_group_egress_id, expected_type=type_hints["security_group_egress_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_egress_id": security_group_egress_id,
        }

    @builtins.property
    def security_group_egress_id(self) -> builtins.str:
        '''The Id of the SecurityGroupEgress resource.'''
        result = self._values.get("security_group_egress_id")
        assert result is not None, "Required property 'security_group_egress_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupEgressReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SecurityGroupIngressReference",
    jsii_struct_bases=[],
    name_mapping={"security_group_ingress_id": "securityGroupIngressId"},
)
class SecurityGroupIngressReference:
    def __init__(self, *, security_group_ingress_id: builtins.str) -> None:
        '''A reference to a SecurityGroupIngress resource.

        :param security_group_ingress_id: The Id of the SecurityGroupIngress resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            security_group_ingress_reference = interfaces_ec2.SecurityGroupIngressReference(
                security_group_ingress_id="securityGroupIngressId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65e5c9332b43e9c0da2df0fc5e03d679f818b14c48802afad4a3142afd64c3be)
            check_type(argname="argument security_group_ingress_id", value=security_group_ingress_id, expected_type=type_hints["security_group_ingress_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ingress_id": security_group_ingress_id,
        }

    @builtins.property
    def security_group_ingress_id(self) -> builtins.str:
        '''The Id of the SecurityGroupIngress resource.'''
        result = self._values.get("security_group_ingress_id")
        assert result is not None, "Required property 'security_group_ingress_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupIngressReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SecurityGroupReference",
    jsii_struct_bases=[],
    name_mapping={"security_group_id": "securityGroupId"},
)
class SecurityGroupReference:
    def __init__(self, *, security_group_id: builtins.str) -> None:
        '''A reference to a SecurityGroup resource.

        :param security_group_id: The Id of the SecurityGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            security_group_reference = interfaces_ec2.SecurityGroupReference(
                security_group_id="securityGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0db1d7cd391a8af80a1fb9ff07216b42a4dd0046e0970b88a8c980e5fc5dba6f)
            check_type(argname="argument security_group_id", value=security_group_id, expected_type=type_hints["security_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_id": security_group_id,
        }

    @builtins.property
    def security_group_id(self) -> builtins.str:
        '''The Id of the SecurityGroup resource.'''
        result = self._values.get("security_group_id")
        assert result is not None, "Required property 'security_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SecurityGroupVpcAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"group_id": "groupId", "vpc_id": "vpcId"},
)
class SecurityGroupVpcAssociationReference:
    def __init__(self, *, group_id: builtins.str, vpc_id: builtins.str) -> None:
        '''A reference to a SecurityGroupVpcAssociation resource.

        :param group_id: The GroupId of the SecurityGroupVpcAssociation resource.
        :param vpc_id: The VpcId of the SecurityGroupVpcAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            security_group_vpc_association_reference = interfaces_ec2.SecurityGroupVpcAssociationReference(
                group_id="groupId",
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99b958e983f4c514199c4bea21e7fb7965cfcb29980b1b4db814bdbab612a999)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The GroupId of the SecurityGroupVpcAssociation resource.'''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VpcId of the SecurityGroupVpcAssociation resource.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupVpcAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SnapshotBlockPublicAccessReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class SnapshotBlockPublicAccessReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a SnapshotBlockPublicAccess resource.

        :param account_id: The AccountId of the SnapshotBlockPublicAccess resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            snapshot_block_public_access_reference = interfaces_ec2.SnapshotBlockPublicAccessReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ad7a412bb4a7b19786369fbb394c471b2636bbcb63104a8ad0494d4e1333101)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the SnapshotBlockPublicAccess resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnapshotBlockPublicAccessReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SpotFleetReference",
    jsii_struct_bases=[],
    name_mapping={"spot_fleet_id": "spotFleetId"},
)
class SpotFleetReference:
    def __init__(self, *, spot_fleet_id: builtins.str) -> None:
        '''A reference to a SpotFleet resource.

        :param spot_fleet_id: The Id of the SpotFleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            spot_fleet_reference = interfaces_ec2.SpotFleetReference(
                spot_fleet_id="spotFleetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e118107621a5bd1c8bc349d74994c79a1a88962c110757dc9faba1d47504c73a)
            check_type(argname="argument spot_fleet_id", value=spot_fleet_id, expected_type=type_hints["spot_fleet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "spot_fleet_id": spot_fleet_id,
        }

    @builtins.property
    def spot_fleet_id(self) -> builtins.str:
        '''The Id of the SpotFleet resource.'''
        result = self._values.get("spot_fleet_id")
        assert result is not None, "Required property 'spot_fleet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SpotFleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SubnetCidrBlockReference",
    jsii_struct_bases=[],
    name_mapping={"subnet_cidr_block_id": "subnetCidrBlockId"},
)
class SubnetCidrBlockReference:
    def __init__(self, *, subnet_cidr_block_id: builtins.str) -> None:
        '''A reference to a SubnetCidrBlock resource.

        :param subnet_cidr_block_id: The Id of the SubnetCidrBlock resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            subnet_cidr_block_reference = interfaces_ec2.SubnetCidrBlockReference(
                subnet_cidr_block_id="subnetCidrBlockId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6afd0bd0b6454ebc029c534dc448712d3ba20ac3ab16969fba368228dfe49c40)
            check_type(argname="argument subnet_cidr_block_id", value=subnet_cidr_block_id, expected_type=type_hints["subnet_cidr_block_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnet_cidr_block_id": subnet_cidr_block_id,
        }

    @builtins.property
    def subnet_cidr_block_id(self) -> builtins.str:
        '''The Id of the SubnetCidrBlock resource.'''
        result = self._values.get("subnet_cidr_block_id")
        assert result is not None, "Required property 'subnet_cidr_block_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetCidrBlockReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SubnetNetworkAclAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"association_id": "associationId"},
)
class SubnetNetworkAclAssociationReference:
    def __init__(self, *, association_id: builtins.str) -> None:
        '''A reference to a SubnetNetworkAclAssociation resource.

        :param association_id: The AssociationId of the SubnetNetworkAclAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            subnet_network_acl_association_reference = interfaces_ec2.SubnetNetworkAclAssociationReference(
                association_id="associationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33b2d56f1de8c36fb8b18796caf24be422cd959f3d196021081df0f784129620)
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_id": association_id,
        }

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the SubnetNetworkAclAssociation resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetNetworkAclAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SubnetReference",
    jsii_struct_bases=[],
    name_mapping={"subnet_id": "subnetId"},
)
class SubnetReference:
    def __init__(self, *, subnet_id: builtins.str) -> None:
        '''A reference to a Subnet resource.

        :param subnet_id: The SubnetId of the Subnet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            subnet_reference = interfaces_ec2.SubnetReference(
                subnet_id="subnetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c11ffeb00d907db6208591d4cb8554a1a39e42d75f3167e4dcbd07f49ae5a8aa)
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnet_id": subnet_id,
        }

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''The SubnetId of the Subnet resource.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.SubnetRouteTableAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "subnet_route_table_association_id": "subnetRouteTableAssociationId",
    },
)
class SubnetRouteTableAssociationReference:
    def __init__(self, *, subnet_route_table_association_id: builtins.str) -> None:
        '''A reference to a SubnetRouteTableAssociation resource.

        :param subnet_route_table_association_id: The Id of the SubnetRouteTableAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            subnet_route_table_association_reference = interfaces_ec2.SubnetRouteTableAssociationReference(
                subnet_route_table_association_id="subnetRouteTableAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afa99ad2bc407d92eb9c3198a931831d5546abe03377f0579d8446168cb939e4)
            check_type(argname="argument subnet_route_table_association_id", value=subnet_route_table_association_id, expected_type=type_hints["subnet_route_table_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnet_route_table_association_id": subnet_route_table_association_id,
        }

    @builtins.property
    def subnet_route_table_association_id(self) -> builtins.str:
        '''The Id of the SubnetRouteTableAssociation resource.'''
        result = self._values.get("subnet_route_table_association_id")
        assert result is not None, "Required property 'subnet_route_table_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetRouteTableAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TrafficMirrorFilterReference",
    jsii_struct_bases=[],
    name_mapping={"traffic_mirror_filter_id": "trafficMirrorFilterId"},
)
class TrafficMirrorFilterReference:
    def __init__(self, *, traffic_mirror_filter_id: builtins.str) -> None:
        '''A reference to a TrafficMirrorFilter resource.

        :param traffic_mirror_filter_id: The Id of the TrafficMirrorFilter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            traffic_mirror_filter_reference = interfaces_ec2.TrafficMirrorFilterReference(
                traffic_mirror_filter_id="trafficMirrorFilterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0402b0873722cf0cf79c419e8abf4342bb2693c80a72aa75fa35e89dd6a4978f)
            check_type(argname="argument traffic_mirror_filter_id", value=traffic_mirror_filter_id, expected_type=type_hints["traffic_mirror_filter_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "traffic_mirror_filter_id": traffic_mirror_filter_id,
        }

    @builtins.property
    def traffic_mirror_filter_id(self) -> builtins.str:
        '''The Id of the TrafficMirrorFilter resource.'''
        result = self._values.get("traffic_mirror_filter_id")
        assert result is not None, "Required property 'traffic_mirror_filter_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficMirrorFilterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TrafficMirrorFilterRuleReference",
    jsii_struct_bases=[],
    name_mapping={"traffic_mirror_filter_rule_id": "trafficMirrorFilterRuleId"},
)
class TrafficMirrorFilterRuleReference:
    def __init__(self, *, traffic_mirror_filter_rule_id: builtins.str) -> None:
        '''A reference to a TrafficMirrorFilterRule resource.

        :param traffic_mirror_filter_rule_id: The TrafficMirrorFilterRuleId of the TrafficMirrorFilterRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            traffic_mirror_filter_rule_reference = interfaces_ec2.TrafficMirrorFilterRuleReference(
                traffic_mirror_filter_rule_id="trafficMirrorFilterRuleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f48e3d119ce3b20c46298a4e32d4308e1c544570d3335943e89cc9b985cce45b)
            check_type(argname="argument traffic_mirror_filter_rule_id", value=traffic_mirror_filter_rule_id, expected_type=type_hints["traffic_mirror_filter_rule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "traffic_mirror_filter_rule_id": traffic_mirror_filter_rule_id,
        }

    @builtins.property
    def traffic_mirror_filter_rule_id(self) -> builtins.str:
        '''The TrafficMirrorFilterRuleId of the TrafficMirrorFilterRule resource.'''
        result = self._values.get("traffic_mirror_filter_rule_id")
        assert result is not None, "Required property 'traffic_mirror_filter_rule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficMirrorFilterRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TrafficMirrorSessionReference",
    jsii_struct_bases=[],
    name_mapping={"traffic_mirror_session_id": "trafficMirrorSessionId"},
)
class TrafficMirrorSessionReference:
    def __init__(self, *, traffic_mirror_session_id: builtins.str) -> None:
        '''A reference to a TrafficMirrorSession resource.

        :param traffic_mirror_session_id: The Id of the TrafficMirrorSession resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            traffic_mirror_session_reference = interfaces_ec2.TrafficMirrorSessionReference(
                traffic_mirror_session_id="trafficMirrorSessionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef09d27d4ecc067dd0ecc3aaf93fa5b28de397da0443888e4044c29b20c3ecb0)
            check_type(argname="argument traffic_mirror_session_id", value=traffic_mirror_session_id, expected_type=type_hints["traffic_mirror_session_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "traffic_mirror_session_id": traffic_mirror_session_id,
        }

    @builtins.property
    def traffic_mirror_session_id(self) -> builtins.str:
        '''The Id of the TrafficMirrorSession resource.'''
        result = self._values.get("traffic_mirror_session_id")
        assert result is not None, "Required property 'traffic_mirror_session_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficMirrorSessionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TrafficMirrorTargetReference",
    jsii_struct_bases=[],
    name_mapping={"traffic_mirror_target_id": "trafficMirrorTargetId"},
)
class TrafficMirrorTargetReference:
    def __init__(self, *, traffic_mirror_target_id: builtins.str) -> None:
        '''A reference to a TrafficMirrorTarget resource.

        :param traffic_mirror_target_id: The Id of the TrafficMirrorTarget resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            traffic_mirror_target_reference = interfaces_ec2.TrafficMirrorTargetReference(
                traffic_mirror_target_id="trafficMirrorTargetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3ab01ca9a5683fa84e2013c5b5dd1998daa11eb9d67b91630464d8c40e967cb)
            check_type(argname="argument traffic_mirror_target_id", value=traffic_mirror_target_id, expected_type=type_hints["traffic_mirror_target_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "traffic_mirror_target_id": traffic_mirror_target_id,
        }

    @builtins.property
    def traffic_mirror_target_id(self) -> builtins.str:
        '''The Id of the TrafficMirrorTarget resource.'''
        result = self._values.get("traffic_mirror_target_id")
        assert result is not None, "Required property 'traffic_mirror_target_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficMirrorTargetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"transit_gateway_attachment_id": "transitGatewayAttachmentId"},
)
class TransitGatewayAttachmentReference:
    def __init__(self, *, transit_gateway_attachment_id: builtins.str) -> None:
        '''A reference to a TransitGatewayAttachment resource.

        :param transit_gateway_attachment_id: The Id of the TransitGatewayAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_attachment_reference = interfaces_ec2.TransitGatewayAttachmentReference(
                transit_gateway_attachment_id="transitGatewayAttachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d00c8241f7c73c4c87059cfd039d51f5660c67a6100348cac3bd46760ada98c)
            check_type(argname="argument transit_gateway_attachment_id", value=transit_gateway_attachment_id, expected_type=type_hints["transit_gateway_attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_attachment_id": transit_gateway_attachment_id,
        }

    @builtins.property
    def transit_gateway_attachment_id(self) -> builtins.str:
        '''The Id of the TransitGatewayAttachment resource.'''
        result = self._values.get("transit_gateway_attachment_id")
        assert result is not None, "Required property 'transit_gateway_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayConnectPeerReference",
    jsii_struct_bases=[],
    name_mapping={"transit_gateway_connect_peer_id": "transitGatewayConnectPeerId"},
)
class TransitGatewayConnectPeerReference:
    def __init__(self, *, transit_gateway_connect_peer_id: builtins.str) -> None:
        '''A reference to a TransitGatewayConnectPeer resource.

        :param transit_gateway_connect_peer_id: The TransitGatewayConnectPeerId of the TransitGatewayConnectPeer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_connect_peer_reference = interfaces_ec2.TransitGatewayConnectPeerReference(
                transit_gateway_connect_peer_id="transitGatewayConnectPeerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd6c8f8f03f34359b5ba738fbf290977b3fe4bc7cb209923bf5cec9052480554)
            check_type(argname="argument transit_gateway_connect_peer_id", value=transit_gateway_connect_peer_id, expected_type=type_hints["transit_gateway_connect_peer_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_connect_peer_id": transit_gateway_connect_peer_id,
        }

    @builtins.property
    def transit_gateway_connect_peer_id(self) -> builtins.str:
        '''The TransitGatewayConnectPeerId of the TransitGatewayConnectPeer resource.'''
        result = self._values.get("transit_gateway_connect_peer_id")
        assert result is not None, "Required property 'transit_gateway_connect_peer_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayConnectPeerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayConnectReference",
    jsii_struct_bases=[],
    name_mapping={"transit_gateway_attachment_id": "transitGatewayAttachmentId"},
)
class TransitGatewayConnectReference:
    def __init__(self, *, transit_gateway_attachment_id: builtins.str) -> None:
        '''A reference to a TransitGatewayConnect resource.

        :param transit_gateway_attachment_id: The TransitGatewayAttachmentId of the TransitGatewayConnect resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_connect_reference = interfaces_ec2.TransitGatewayConnectReference(
                transit_gateway_attachment_id="transitGatewayAttachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8890329f7e30c11a4944c99fc332973f5280ac00a0222b1631d4e50bd7f262d)
            check_type(argname="argument transit_gateway_attachment_id", value=transit_gateway_attachment_id, expected_type=type_hints["transit_gateway_attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_attachment_id": transit_gateway_attachment_id,
        }

    @builtins.property
    def transit_gateway_attachment_id(self) -> builtins.str:
        '''The TransitGatewayAttachmentId of the TransitGatewayConnect resource.'''
        result = self._values.get("transit_gateway_attachment_id")
        assert result is not None, "Required property 'transit_gateway_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayConnectReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayMeteringPolicyEntryReference",
    jsii_struct_bases=[],
    name_mapping={
        "policy_rule_number": "policyRuleNumber",
        "transit_gateway_metering_policy_id": "transitGatewayMeteringPolicyId",
    },
)
class TransitGatewayMeteringPolicyEntryReference:
    def __init__(
        self,
        *,
        policy_rule_number: builtins.str,
        transit_gateway_metering_policy_id: builtins.str,
    ) -> None:
        '''A reference to a TransitGatewayMeteringPolicyEntry resource.

        :param policy_rule_number: The PolicyRuleNumber of the TransitGatewayMeteringPolicyEntry resource.
        :param transit_gateway_metering_policy_id: The TransitGatewayMeteringPolicyId of the TransitGatewayMeteringPolicyEntry resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_metering_policy_entry_reference = interfaces_ec2.TransitGatewayMeteringPolicyEntryReference(
                policy_rule_number="policyRuleNumber",
                transit_gateway_metering_policy_id="transitGatewayMeteringPolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b5ab879ac9cab67aeb0a61553565ffea8f306e89f552a533dfd930f59d7ed24)
            check_type(argname="argument policy_rule_number", value=policy_rule_number, expected_type=type_hints["policy_rule_number"])
            check_type(argname="argument transit_gateway_metering_policy_id", value=transit_gateway_metering_policy_id, expected_type=type_hints["transit_gateway_metering_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_rule_number": policy_rule_number,
            "transit_gateway_metering_policy_id": transit_gateway_metering_policy_id,
        }

    @builtins.property
    def policy_rule_number(self) -> builtins.str:
        '''The PolicyRuleNumber of the TransitGatewayMeteringPolicyEntry resource.'''
        result = self._values.get("policy_rule_number")
        assert result is not None, "Required property 'policy_rule_number' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_metering_policy_id(self) -> builtins.str:
        '''The TransitGatewayMeteringPolicyId of the TransitGatewayMeteringPolicyEntry resource.'''
        result = self._values.get("transit_gateway_metering_policy_id")
        assert result is not None, "Required property 'transit_gateway_metering_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayMeteringPolicyEntryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayMeteringPolicyReference",
    jsii_struct_bases=[],
    name_mapping={
        "transit_gateway_metering_policy_id": "transitGatewayMeteringPolicyId",
    },
)
class TransitGatewayMeteringPolicyReference:
    def __init__(self, *, transit_gateway_metering_policy_id: builtins.str) -> None:
        '''A reference to a TransitGatewayMeteringPolicy resource.

        :param transit_gateway_metering_policy_id: The TransitGatewayMeteringPolicyId of the TransitGatewayMeteringPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_metering_policy_reference = interfaces_ec2.TransitGatewayMeteringPolicyReference(
                transit_gateway_metering_policy_id="transitGatewayMeteringPolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01cc92df7f25b3e6a54bc6e93fbabb355be5b5f7dec1c6e4fc273e7f663f7d38)
            check_type(argname="argument transit_gateway_metering_policy_id", value=transit_gateway_metering_policy_id, expected_type=type_hints["transit_gateway_metering_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_metering_policy_id": transit_gateway_metering_policy_id,
        }

    @builtins.property
    def transit_gateway_metering_policy_id(self) -> builtins.str:
        '''The TransitGatewayMeteringPolicyId of the TransitGatewayMeteringPolicy resource.'''
        result = self._values.get("transit_gateway_metering_policy_id")
        assert result is not None, "Required property 'transit_gateway_metering_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayMeteringPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayMulticastDomainAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "subnet_id": "subnetId",
        "transit_gateway_attachment_id": "transitGatewayAttachmentId",
        "transit_gateway_multicast_domain_id": "transitGatewayMulticastDomainId",
    },
)
class TransitGatewayMulticastDomainAssociationReference:
    def __init__(
        self,
        *,
        subnet_id: builtins.str,
        transit_gateway_attachment_id: builtins.str,
        transit_gateway_multicast_domain_id: builtins.str,
    ) -> None:
        '''A reference to a TransitGatewayMulticastDomainAssociation resource.

        :param subnet_id: The SubnetId of the TransitGatewayMulticastDomainAssociation resource.
        :param transit_gateway_attachment_id: The TransitGatewayAttachmentId of the TransitGatewayMulticastDomainAssociation resource.
        :param transit_gateway_multicast_domain_id: The TransitGatewayMulticastDomainId of the TransitGatewayMulticastDomainAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_multicast_domain_association_reference = interfaces_ec2.TransitGatewayMulticastDomainAssociationReference(
                subnet_id="subnetId",
                transit_gateway_attachment_id="transitGatewayAttachmentId",
                transit_gateway_multicast_domain_id="transitGatewayMulticastDomainId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__095a9cdfacf328704a9d19f22212da96cbb6e9c6e1ec4bc67d2a0d960e1ec805)
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument transit_gateway_attachment_id", value=transit_gateway_attachment_id, expected_type=type_hints["transit_gateway_attachment_id"])
            check_type(argname="argument transit_gateway_multicast_domain_id", value=transit_gateway_multicast_domain_id, expected_type=type_hints["transit_gateway_multicast_domain_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnet_id": subnet_id,
            "transit_gateway_attachment_id": transit_gateway_attachment_id,
            "transit_gateway_multicast_domain_id": transit_gateway_multicast_domain_id,
        }

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''The SubnetId of the TransitGatewayMulticastDomainAssociation resource.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_attachment_id(self) -> builtins.str:
        '''The TransitGatewayAttachmentId of the TransitGatewayMulticastDomainAssociation resource.'''
        result = self._values.get("transit_gateway_attachment_id")
        assert result is not None, "Required property 'transit_gateway_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_multicast_domain_id(self) -> builtins.str:
        '''The TransitGatewayMulticastDomainId of the TransitGatewayMulticastDomainAssociation resource.'''
        result = self._values.get("transit_gateway_multicast_domain_id")
        assert result is not None, "Required property 'transit_gateway_multicast_domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayMulticastDomainAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayMulticastDomainReference",
    jsii_struct_bases=[],
    name_mapping={
        "transit_gateway_multicast_domain_arn": "transitGatewayMulticastDomainArn",
        "transit_gateway_multicast_domain_id": "transitGatewayMulticastDomainId",
    },
)
class TransitGatewayMulticastDomainReference:
    def __init__(
        self,
        *,
        transit_gateway_multicast_domain_arn: builtins.str,
        transit_gateway_multicast_domain_id: builtins.str,
    ) -> None:
        '''A reference to a TransitGatewayMulticastDomain resource.

        :param transit_gateway_multicast_domain_arn: The ARN of the TransitGatewayMulticastDomain resource.
        :param transit_gateway_multicast_domain_id: The TransitGatewayMulticastDomainId of the TransitGatewayMulticastDomain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_multicast_domain_reference = interfaces_ec2.TransitGatewayMulticastDomainReference(
                transit_gateway_multicast_domain_arn="transitGatewayMulticastDomainArn",
                transit_gateway_multicast_domain_id="transitGatewayMulticastDomainId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f5a19765b0859abb7dae874b479771317759b9e92e4cc5f27ae398b2afb775c)
            check_type(argname="argument transit_gateway_multicast_domain_arn", value=transit_gateway_multicast_domain_arn, expected_type=type_hints["transit_gateway_multicast_domain_arn"])
            check_type(argname="argument transit_gateway_multicast_domain_id", value=transit_gateway_multicast_domain_id, expected_type=type_hints["transit_gateway_multicast_domain_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_multicast_domain_arn": transit_gateway_multicast_domain_arn,
            "transit_gateway_multicast_domain_id": transit_gateway_multicast_domain_id,
        }

    @builtins.property
    def transit_gateway_multicast_domain_arn(self) -> builtins.str:
        '''The ARN of the TransitGatewayMulticastDomain resource.'''
        result = self._values.get("transit_gateway_multicast_domain_arn")
        assert result is not None, "Required property 'transit_gateway_multicast_domain_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_multicast_domain_id(self) -> builtins.str:
        '''The TransitGatewayMulticastDomainId of the TransitGatewayMulticastDomain resource.'''
        result = self._values.get("transit_gateway_multicast_domain_id")
        assert result is not None, "Required property 'transit_gateway_multicast_domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayMulticastDomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayMulticastGroupMemberReference",
    jsii_struct_bases=[],
    name_mapping={
        "group_ip_address": "groupIpAddress",
        "network_interface_id": "networkInterfaceId",
        "transit_gateway_multicast_domain_id": "transitGatewayMulticastDomainId",
    },
)
class TransitGatewayMulticastGroupMemberReference:
    def __init__(
        self,
        *,
        group_ip_address: builtins.str,
        network_interface_id: builtins.str,
        transit_gateway_multicast_domain_id: builtins.str,
    ) -> None:
        '''A reference to a TransitGatewayMulticastGroupMember resource.

        :param group_ip_address: The GroupIpAddress of the TransitGatewayMulticastGroupMember resource.
        :param network_interface_id: The NetworkInterfaceId of the TransitGatewayMulticastGroupMember resource.
        :param transit_gateway_multicast_domain_id: The TransitGatewayMulticastDomainId of the TransitGatewayMulticastGroupMember resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_multicast_group_member_reference = interfaces_ec2.TransitGatewayMulticastGroupMemberReference(
                group_ip_address="groupIpAddress",
                network_interface_id="networkInterfaceId",
                transit_gateway_multicast_domain_id="transitGatewayMulticastDomainId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c224bd05272e424c61d5175c14f8f89e49fa9d16676a2eff3ad0883ffd152668)
            check_type(argname="argument group_ip_address", value=group_ip_address, expected_type=type_hints["group_ip_address"])
            check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
            check_type(argname="argument transit_gateway_multicast_domain_id", value=transit_gateway_multicast_domain_id, expected_type=type_hints["transit_gateway_multicast_domain_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_ip_address": group_ip_address,
            "network_interface_id": network_interface_id,
            "transit_gateway_multicast_domain_id": transit_gateway_multicast_domain_id,
        }

    @builtins.property
    def group_ip_address(self) -> builtins.str:
        '''The GroupIpAddress of the TransitGatewayMulticastGroupMember resource.'''
        result = self._values.get("group_ip_address")
        assert result is not None, "Required property 'group_ip_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface_id(self) -> builtins.str:
        '''The NetworkInterfaceId of the TransitGatewayMulticastGroupMember resource.'''
        result = self._values.get("network_interface_id")
        assert result is not None, "Required property 'network_interface_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_multicast_domain_id(self) -> builtins.str:
        '''The TransitGatewayMulticastDomainId of the TransitGatewayMulticastGroupMember resource.'''
        result = self._values.get("transit_gateway_multicast_domain_id")
        assert result is not None, "Required property 'transit_gateway_multicast_domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayMulticastGroupMemberReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayMulticastGroupSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "group_ip_address": "groupIpAddress",
        "network_interface_id": "networkInterfaceId",
        "transit_gateway_multicast_domain_id": "transitGatewayMulticastDomainId",
    },
)
class TransitGatewayMulticastGroupSourceReference:
    def __init__(
        self,
        *,
        group_ip_address: builtins.str,
        network_interface_id: builtins.str,
        transit_gateway_multicast_domain_id: builtins.str,
    ) -> None:
        '''A reference to a TransitGatewayMulticastGroupSource resource.

        :param group_ip_address: The GroupIpAddress of the TransitGatewayMulticastGroupSource resource.
        :param network_interface_id: The NetworkInterfaceId of the TransitGatewayMulticastGroupSource resource.
        :param transit_gateway_multicast_domain_id: The TransitGatewayMulticastDomainId of the TransitGatewayMulticastGroupSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_multicast_group_source_reference = interfaces_ec2.TransitGatewayMulticastGroupSourceReference(
                group_ip_address="groupIpAddress",
                network_interface_id="networkInterfaceId",
                transit_gateway_multicast_domain_id="transitGatewayMulticastDomainId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4289e401a4bd5d88d9c836aee8d224ff8c8f11d601afe36b0f89e72cb3c14aa6)
            check_type(argname="argument group_ip_address", value=group_ip_address, expected_type=type_hints["group_ip_address"])
            check_type(argname="argument network_interface_id", value=network_interface_id, expected_type=type_hints["network_interface_id"])
            check_type(argname="argument transit_gateway_multicast_domain_id", value=transit_gateway_multicast_domain_id, expected_type=type_hints["transit_gateway_multicast_domain_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_ip_address": group_ip_address,
            "network_interface_id": network_interface_id,
            "transit_gateway_multicast_domain_id": transit_gateway_multicast_domain_id,
        }

    @builtins.property
    def group_ip_address(self) -> builtins.str:
        '''The GroupIpAddress of the TransitGatewayMulticastGroupSource resource.'''
        result = self._values.get("group_ip_address")
        assert result is not None, "Required property 'group_ip_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_interface_id(self) -> builtins.str:
        '''The NetworkInterfaceId of the TransitGatewayMulticastGroupSource resource.'''
        result = self._values.get("network_interface_id")
        assert result is not None, "Required property 'network_interface_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_multicast_domain_id(self) -> builtins.str:
        '''The TransitGatewayMulticastDomainId of the TransitGatewayMulticastGroupSource resource.'''
        result = self._values.get("transit_gateway_multicast_domain_id")
        assert result is not None, "Required property 'transit_gateway_multicast_domain_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayMulticastGroupSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayPeeringAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"transit_gateway_attachment_id": "transitGatewayAttachmentId"},
)
class TransitGatewayPeeringAttachmentReference:
    def __init__(self, *, transit_gateway_attachment_id: builtins.str) -> None:
        '''A reference to a TransitGatewayPeeringAttachment resource.

        :param transit_gateway_attachment_id: The TransitGatewayAttachmentId of the TransitGatewayPeeringAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_peering_attachment_reference = interfaces_ec2.TransitGatewayPeeringAttachmentReference(
                transit_gateway_attachment_id="transitGatewayAttachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64897c67231def1034314d171a43235f95e68fe614b1f5d838fb9917e3da522)
            check_type(argname="argument transit_gateway_attachment_id", value=transit_gateway_attachment_id, expected_type=type_hints["transit_gateway_attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_attachment_id": transit_gateway_attachment_id,
        }

    @builtins.property
    def transit_gateway_attachment_id(self) -> builtins.str:
        '''The TransitGatewayAttachmentId of the TransitGatewayPeeringAttachment resource.'''
        result = self._values.get("transit_gateway_attachment_id")
        assert result is not None, "Required property 'transit_gateway_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayPeeringAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayReference",
    jsii_struct_bases=[],
    name_mapping={
        "transit_gateway_arn": "transitGatewayArn",
        "transit_gateway_id": "transitGatewayId",
    },
)
class TransitGatewayReference:
    def __init__(
        self,
        *,
        transit_gateway_arn: builtins.str,
        transit_gateway_id: builtins.str,
    ) -> None:
        '''A reference to a TransitGateway resource.

        :param transit_gateway_arn: The ARN of the TransitGateway resource.
        :param transit_gateway_id: The Id of the TransitGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_reference = interfaces_ec2.TransitGatewayReference(
                transit_gateway_arn="transitGatewayArn",
                transit_gateway_id="transitGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d42ecfd465267df55b09ea969ba78c292f56d9299bc36fff859bc519571119ae)
            check_type(argname="argument transit_gateway_arn", value=transit_gateway_arn, expected_type=type_hints["transit_gateway_arn"])
            check_type(argname="argument transit_gateway_id", value=transit_gateway_id, expected_type=type_hints["transit_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_arn": transit_gateway_arn,
            "transit_gateway_id": transit_gateway_id,
        }

    @builtins.property
    def transit_gateway_arn(self) -> builtins.str:
        '''The ARN of the TransitGateway resource.'''
        result = self._values.get("transit_gateway_arn")
        assert result is not None, "Required property 'transit_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_id(self) -> builtins.str:
        '''The Id of the TransitGateway resource.'''
        result = self._values.get("transit_gateway_id")
        assert result is not None, "Required property 'transit_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayRouteReference",
    jsii_struct_bases=[],
    name_mapping={
        "destination_cidr_block": "destinationCidrBlock",
        "transit_gateway_route_table_id": "transitGatewayRouteTableId",
    },
)
class TransitGatewayRouteReference:
    def __init__(
        self,
        *,
        destination_cidr_block: builtins.str,
        transit_gateway_route_table_id: builtins.str,
    ) -> None:
        '''A reference to a TransitGatewayRoute resource.

        :param destination_cidr_block: The DestinationCidrBlock of the TransitGatewayRoute resource.
        :param transit_gateway_route_table_id: The TransitGatewayRouteTableId of the TransitGatewayRoute resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_route_reference = interfaces_ec2.TransitGatewayRouteReference(
                destination_cidr_block="destinationCidrBlock",
                transit_gateway_route_table_id="transitGatewayRouteTableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cd7817dd4938ea0b305988047341a875562b9b0809ef57097bc4e4ffd4460fb)
            check_type(argname="argument destination_cidr_block", value=destination_cidr_block, expected_type=type_hints["destination_cidr_block"])
            check_type(argname="argument transit_gateway_route_table_id", value=transit_gateway_route_table_id, expected_type=type_hints["transit_gateway_route_table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_cidr_block": destination_cidr_block,
            "transit_gateway_route_table_id": transit_gateway_route_table_id,
        }

    @builtins.property
    def destination_cidr_block(self) -> builtins.str:
        '''The DestinationCidrBlock of the TransitGatewayRoute resource.'''
        result = self._values.get("destination_cidr_block")
        assert result is not None, "Required property 'destination_cidr_block' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_route_table_id(self) -> builtins.str:
        '''The TransitGatewayRouteTableId of the TransitGatewayRoute resource.'''
        result = self._values.get("transit_gateway_route_table_id")
        assert result is not None, "Required property 'transit_gateway_route_table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayRouteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayRouteTableAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "transit_gateway_attachment_id": "transitGatewayAttachmentId",
        "transit_gateway_route_table_id": "transitGatewayRouteTableId",
    },
)
class TransitGatewayRouteTableAssociationReference:
    def __init__(
        self,
        *,
        transit_gateway_attachment_id: builtins.str,
        transit_gateway_route_table_id: builtins.str,
    ) -> None:
        '''A reference to a TransitGatewayRouteTableAssociation resource.

        :param transit_gateway_attachment_id: The TransitGatewayAttachmentId of the TransitGatewayRouteTableAssociation resource.
        :param transit_gateway_route_table_id: The TransitGatewayRouteTableId of the TransitGatewayRouteTableAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_route_table_association_reference = interfaces_ec2.TransitGatewayRouteTableAssociationReference(
                transit_gateway_attachment_id="transitGatewayAttachmentId",
                transit_gateway_route_table_id="transitGatewayRouteTableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c33d3d19d0e848e40b21297daa62bca5880d7bc107c8facc1dd71b21ff33ce67)
            check_type(argname="argument transit_gateway_attachment_id", value=transit_gateway_attachment_id, expected_type=type_hints["transit_gateway_attachment_id"])
            check_type(argname="argument transit_gateway_route_table_id", value=transit_gateway_route_table_id, expected_type=type_hints["transit_gateway_route_table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_attachment_id": transit_gateway_attachment_id,
            "transit_gateway_route_table_id": transit_gateway_route_table_id,
        }

    @builtins.property
    def transit_gateway_attachment_id(self) -> builtins.str:
        '''The TransitGatewayAttachmentId of the TransitGatewayRouteTableAssociation resource.'''
        result = self._values.get("transit_gateway_attachment_id")
        assert result is not None, "Required property 'transit_gateway_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_route_table_id(self) -> builtins.str:
        '''The TransitGatewayRouteTableId of the TransitGatewayRouteTableAssociation resource.'''
        result = self._values.get("transit_gateway_route_table_id")
        assert result is not None, "Required property 'transit_gateway_route_table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayRouteTableAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayRouteTablePropagationReference",
    jsii_struct_bases=[],
    name_mapping={
        "transit_gateway_attachment_id": "transitGatewayAttachmentId",
        "transit_gateway_route_table_id": "transitGatewayRouteTableId",
    },
)
class TransitGatewayRouteTablePropagationReference:
    def __init__(
        self,
        *,
        transit_gateway_attachment_id: builtins.str,
        transit_gateway_route_table_id: builtins.str,
    ) -> None:
        '''A reference to a TransitGatewayRouteTablePropagation resource.

        :param transit_gateway_attachment_id: The TransitGatewayAttachmentId of the TransitGatewayRouteTablePropagation resource.
        :param transit_gateway_route_table_id: The TransitGatewayRouteTableId of the TransitGatewayRouteTablePropagation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_route_table_propagation_reference = interfaces_ec2.TransitGatewayRouteTablePropagationReference(
                transit_gateway_attachment_id="transitGatewayAttachmentId",
                transit_gateway_route_table_id="transitGatewayRouteTableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26cc3fa7b96f8ff924a971f4c6aba753df2b70d2228ac1957647f1bdbbf93ddd)
            check_type(argname="argument transit_gateway_attachment_id", value=transit_gateway_attachment_id, expected_type=type_hints["transit_gateway_attachment_id"])
            check_type(argname="argument transit_gateway_route_table_id", value=transit_gateway_route_table_id, expected_type=type_hints["transit_gateway_route_table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_attachment_id": transit_gateway_attachment_id,
            "transit_gateway_route_table_id": transit_gateway_route_table_id,
        }

    @builtins.property
    def transit_gateway_attachment_id(self) -> builtins.str:
        '''The TransitGatewayAttachmentId of the TransitGatewayRouteTablePropagation resource.'''
        result = self._values.get("transit_gateway_attachment_id")
        assert result is not None, "Required property 'transit_gateway_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_route_table_id(self) -> builtins.str:
        '''The TransitGatewayRouteTableId of the TransitGatewayRouteTablePropagation resource.'''
        result = self._values.get("transit_gateway_route_table_id")
        assert result is not None, "Required property 'transit_gateway_route_table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayRouteTablePropagationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayRouteTableReference",
    jsii_struct_bases=[],
    name_mapping={"transit_gateway_route_table_id": "transitGatewayRouteTableId"},
)
class TransitGatewayRouteTableReference:
    def __init__(self, *, transit_gateway_route_table_id: builtins.str) -> None:
        '''A reference to a TransitGatewayRouteTable resource.

        :param transit_gateway_route_table_id: The TransitGatewayRouteTableId of the TransitGatewayRouteTable resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_route_table_reference = interfaces_ec2.TransitGatewayRouteTableReference(
                transit_gateway_route_table_id="transitGatewayRouteTableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d136220ebea5c59d10453273ed8808e0d88ffa850ad4d4e3c6c3b0e5b44f71a0)
            check_type(argname="argument transit_gateway_route_table_id", value=transit_gateway_route_table_id, expected_type=type_hints["transit_gateway_route_table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_route_table_id": transit_gateway_route_table_id,
        }

    @builtins.property
    def transit_gateway_route_table_id(self) -> builtins.str:
        '''The TransitGatewayRouteTableId of the TransitGatewayRouteTable resource.'''
        result = self._values.get("transit_gateway_route_table_id")
        assert result is not None, "Required property 'transit_gateway_route_table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayRouteTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.TransitGatewayVpcAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "transit_gateway_vpc_attachment_id": "transitGatewayVpcAttachmentId",
    },
)
class TransitGatewayVpcAttachmentReference:
    def __init__(self, *, transit_gateway_vpc_attachment_id: builtins.str) -> None:
        '''A reference to a TransitGatewayVpcAttachment resource.

        :param transit_gateway_vpc_attachment_id: The Id of the TransitGatewayVpcAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            transit_gateway_vpc_attachment_reference = interfaces_ec2.TransitGatewayVpcAttachmentReference(
                transit_gateway_vpc_attachment_id="transitGatewayVpcAttachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e885276231a10adb8fbe57ea37365132400a9fdca6f023b139de68a78ba903e6)
            check_type(argname="argument transit_gateway_vpc_attachment_id", value=transit_gateway_vpc_attachment_id, expected_type=type_hints["transit_gateway_vpc_attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "transit_gateway_vpc_attachment_id": transit_gateway_vpc_attachment_id,
        }

    @builtins.property
    def transit_gateway_vpc_attachment_id(self) -> builtins.str:
        '''The Id of the TransitGatewayVpcAttachment resource.'''
        result = self._values.get("transit_gateway_vpc_attachment_id")
        assert result is not None, "Required property 'transit_gateway_vpc_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayVpcAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCBlockPublicAccessExclusionReference",
    jsii_struct_bases=[],
    name_mapping={"exclusion_id": "exclusionId"},
)
class VPCBlockPublicAccessExclusionReference:
    def __init__(self, *, exclusion_id: builtins.str) -> None:
        '''A reference to a VPCBlockPublicAccessExclusion resource.

        :param exclusion_id: The ExclusionId of the VPCBlockPublicAccessExclusion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCBlock_public_access_exclusion_reference = interfaces_ec2.VPCBlockPublicAccessExclusionReference(
                exclusion_id="exclusionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64ac34d1e793b8a1d8cd1d1a75292e5b7b029250a6390d5ca27acedbd3fecb4f)
            check_type(argname="argument exclusion_id", value=exclusion_id, expected_type=type_hints["exclusion_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "exclusion_id": exclusion_id,
        }

    @builtins.property
    def exclusion_id(self) -> builtins.str:
        '''The ExclusionId of the VPCBlockPublicAccessExclusion resource.'''
        result = self._values.get("exclusion_id")
        assert result is not None, "Required property 'exclusion_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCBlockPublicAccessExclusionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCBlockPublicAccessOptionsReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class VPCBlockPublicAccessOptionsReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a VPCBlockPublicAccessOptions resource.

        :param account_id: The AccountId of the VPCBlockPublicAccessOptions resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCBlock_public_access_options_reference = interfaces_ec2.VPCBlockPublicAccessOptionsReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e2a531906cb95c5eef8a6c02d378c377fd729bc96102c0833ec0ab0e2d7f254)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the VPCBlockPublicAccessOptions resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCBlockPublicAccessOptionsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCCidrBlockReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_cidr_block_id": "vpcCidrBlockId", "vpc_id": "vpcId"},
)
class VPCCidrBlockReference:
    def __init__(
        self,
        *,
        vpc_cidr_block_id: builtins.str,
        vpc_id: builtins.str,
    ) -> None:
        '''A reference to a VPCCidrBlock resource.

        :param vpc_cidr_block_id: The Id of the VPCCidrBlock resource.
        :param vpc_id: The VpcId of the VPCCidrBlock resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCCidr_block_reference = interfaces_ec2.VPCCidrBlockReference(
                vpc_cidr_block_id="vpcCidrBlockId",
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32e1c330fb9834ac94e8aa6803768ee36f502b213c52c48c0933f09b30b57ea1)
            check_type(argname="argument vpc_cidr_block_id", value=vpc_cidr_block_id, expected_type=type_hints["vpc_cidr_block_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_cidr_block_id": vpc_cidr_block_id,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def vpc_cidr_block_id(self) -> builtins.str:
        '''The Id of the VPCCidrBlock resource.'''
        result = self._values.get("vpc_cidr_block_id")
        assert result is not None, "Required property 'vpc_cidr_block_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VpcId of the VPCCidrBlock resource.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCCidrBlockReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCDHCPOptionsAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"dhcp_options_id": "dhcpOptionsId", "vpc_id": "vpcId"},
)
class VPCDHCPOptionsAssociationReference:
    def __init__(self, *, dhcp_options_id: builtins.str, vpc_id: builtins.str) -> None:
        '''A reference to a VPCDHCPOptionsAssociation resource.

        :param dhcp_options_id: The DhcpOptionsId of the VPCDHCPOptionsAssociation resource.
        :param vpc_id: The VpcId of the VPCDHCPOptionsAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCDHCPOptions_association_reference = interfaces_ec2.VPCDHCPOptionsAssociationReference(
                dhcp_options_id="dhcpOptionsId",
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28adc76405810a691e2dce4b43c95660c0222b01d8b1608d5d87395daec6db7a)
            check_type(argname="argument dhcp_options_id", value=dhcp_options_id, expected_type=type_hints["dhcp_options_id"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dhcp_options_id": dhcp_options_id,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def dhcp_options_id(self) -> builtins.str:
        '''The DhcpOptionsId of the VPCDHCPOptionsAssociation resource.'''
        result = self._values.get("dhcp_options_id")
        assert result is not None, "Required property 'dhcp_options_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VpcId of the VPCDHCPOptionsAssociation resource.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCDHCPOptionsAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCEncryptionControlReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_encryption_control_id": "vpcEncryptionControlId"},
)
class VPCEncryptionControlReference:
    def __init__(self, *, vpc_encryption_control_id: builtins.str) -> None:
        '''A reference to a VPCEncryptionControl resource.

        :param vpc_encryption_control_id: The VpcEncryptionControlId of the VPCEncryptionControl resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCEncryption_control_reference = interfaces_ec2.VPCEncryptionControlReference(
                vpc_encryption_control_id="vpcEncryptionControlId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50ed3ca4369a94bd67b33fd9728c1616ecc391d119a17b6a19ab268a1aca8e83)
            check_type(argname="argument vpc_encryption_control_id", value=vpc_encryption_control_id, expected_type=type_hints["vpc_encryption_control_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_encryption_control_id": vpc_encryption_control_id,
        }

    @builtins.property
    def vpc_encryption_control_id(self) -> builtins.str:
        '''The VpcEncryptionControlId of the VPCEncryptionControl resource.'''
        result = self._values.get("vpc_encryption_control_id")
        assert result is not None, "Required property 'vpc_encryption_control_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCEncryptionControlReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCEndpointConnectionNotificationReference",
    jsii_struct_bases=[],
    name_mapping={
        "vpc_endpoint_connection_notification_id": "vpcEndpointConnectionNotificationId",
    },
)
class VPCEndpointConnectionNotificationReference:
    def __init__(
        self,
        *,
        vpc_endpoint_connection_notification_id: builtins.str,
    ) -> None:
        '''A reference to a VPCEndpointConnectionNotification resource.

        :param vpc_endpoint_connection_notification_id: The VPCEndpointConnectionNotificationId of the VPCEndpointConnectionNotification resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCEndpoint_connection_notification_reference = interfaces_ec2.VPCEndpointConnectionNotificationReference(
                vpc_endpoint_connection_notification_id="vpcEndpointConnectionNotificationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b45a1f3c71e5b9b9649f83833be2f40dc9cf8841b63e22009a2633c261982ea)
            check_type(argname="argument vpc_endpoint_connection_notification_id", value=vpc_endpoint_connection_notification_id, expected_type=type_hints["vpc_endpoint_connection_notification_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_endpoint_connection_notification_id": vpc_endpoint_connection_notification_id,
        }

    @builtins.property
    def vpc_endpoint_connection_notification_id(self) -> builtins.str:
        '''The VPCEndpointConnectionNotificationId of the VPCEndpointConnectionNotification resource.'''
        result = self._values.get("vpc_endpoint_connection_notification_id")
        assert result is not None, "Required property 'vpc_endpoint_connection_notification_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCEndpointConnectionNotificationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_endpoint_id": "vpcEndpointId"},
)
class VPCEndpointReference:
    def __init__(self, *, vpc_endpoint_id: builtins.str) -> None:
        '''A reference to a VPCEndpoint resource.

        :param vpc_endpoint_id: The Id of the VPCEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCEndpoint_reference = interfaces_ec2.VPCEndpointReference(
                vpc_endpoint_id="vpcEndpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a81418feee4b7635ba4140c24db110bc53e15bf753a79d0166d5354282595c2)
            check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_endpoint_id": vpc_endpoint_id,
        }

    @builtins.property
    def vpc_endpoint_id(self) -> builtins.str:
        '''The Id of the VPCEndpoint resource.'''
        result = self._values.get("vpc_endpoint_id")
        assert result is not None, "Required property 'vpc_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCEndpointServicePermissionsReference",
    jsii_struct_bases=[],
    name_mapping={"service_id": "serviceId"},
)
class VPCEndpointServicePermissionsReference:
    def __init__(self, *, service_id: builtins.str) -> None:
        '''A reference to a VPCEndpointServicePermissions resource.

        :param service_id: The ServiceId of the VPCEndpointServicePermissions resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCEndpoint_service_permissions_reference = interfaces_ec2.VPCEndpointServicePermissionsReference(
                service_id="serviceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__722a1440530819cc37aa35cb38e324750dd1ca13f95b4198238e1c6e4c45b5b9)
            check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_id": service_id,
        }

    @builtins.property
    def service_id(self) -> builtins.str:
        '''The ServiceId of the VPCEndpointServicePermissions resource.'''
        result = self._values.get("service_id")
        assert result is not None, "Required property 'service_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCEndpointServicePermissionsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCEndpointServiceReference",
    jsii_struct_bases=[],
    name_mapping={"service_id": "serviceId"},
)
class VPCEndpointServiceReference:
    def __init__(self, *, service_id: builtins.str) -> None:
        '''A reference to a VPCEndpointService resource.

        :param service_id: The ServiceId of the VPCEndpointService resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCEndpoint_service_reference = interfaces_ec2.VPCEndpointServiceReference(
                service_id="serviceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1efcd12a0cc1df35811dc764325f9bce362912be0e055d83f68803ed158167de)
            check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_id": service_id,
        }

    @builtins.property
    def service_id(self) -> builtins.str:
        '''The ServiceId of the VPCEndpointService resource.'''
        result = self._values.get("service_id")
        assert result is not None, "Required property 'service_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCEndpointServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCGatewayAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"attachment_type": "attachmentType", "vpc_id": "vpcId"},
)
class VPCGatewayAttachmentReference:
    def __init__(self, *, attachment_type: builtins.str, vpc_id: builtins.str) -> None:
        '''A reference to a VPCGatewayAttachment resource.

        :param attachment_type: The AttachmentType of the VPCGatewayAttachment resource.
        :param vpc_id: The VpcId of the VPCGatewayAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCGateway_attachment_reference = interfaces_ec2.VPCGatewayAttachmentReference(
                attachment_type="attachmentType",
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0683bb8dcc4090236382f6417afb8c7a6f1b028b789970abf6518876d8ece05)
            check_type(argname="argument attachment_type", value=attachment_type, expected_type=type_hints["attachment_type"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attachment_type": attachment_type,
            "vpc_id": vpc_id,
        }

    @builtins.property
    def attachment_type(self) -> builtins.str:
        '''The AttachmentType of the VPCGatewayAttachment resource.'''
        result = self._values.get("attachment_type")
        assert result is not None, "Required property 'attachment_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VpcId of the VPCGatewayAttachment resource.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCGatewayAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCPeeringConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_peering_connection_id": "vpcPeeringConnectionId"},
)
class VPCPeeringConnectionReference:
    def __init__(self, *, vpc_peering_connection_id: builtins.str) -> None:
        '''A reference to a VPCPeeringConnection resource.

        :param vpc_peering_connection_id: The Id of the VPCPeeringConnection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCPeering_connection_reference = interfaces_ec2.VPCPeeringConnectionReference(
                vpc_peering_connection_id="vpcPeeringConnectionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e223c0b1eeb03afe708e1dfb3a2d0d857eed62cf5a55e4f8ae20a75afe6e2435)
            check_type(argname="argument vpc_peering_connection_id", value=vpc_peering_connection_id, expected_type=type_hints["vpc_peering_connection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_peering_connection_id": vpc_peering_connection_id,
        }

    @builtins.property
    def vpc_peering_connection_id(self) -> builtins.str:
        '''The Id of the VPCPeeringConnection resource.'''
        result = self._values.get("vpc_peering_connection_id")
        assert result is not None, "Required property 'vpc_peering_connection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCPeeringConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPCReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_id": "vpcId"},
)
class VPCReference:
    def __init__(self, *, vpc_id: builtins.str) -> None:
        '''A reference to a VPC resource.

        :param vpc_id: The VpcId of the VPC resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pCReference = interfaces_ec2.VPCReference(
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eebcb09c1a21f835d06e0bc7c5cb0b566f1c84adaf87a8ad692fff4be8a5c6ff)
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_id": vpc_id,
        }

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VpcId of the VPC resource.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPNConcentratorReference",
    jsii_struct_bases=[],
    name_mapping={"vpn_concentrator_id": "vpnConcentratorId"},
)
class VPNConcentratorReference:
    def __init__(self, *, vpn_concentrator_id: builtins.str) -> None:
        '''A reference to a VPNConcentrator resource.

        :param vpn_concentrator_id: The VpnConcentratorId of the VPNConcentrator resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pNConcentrator_reference = interfaces_ec2.VPNConcentratorReference(
                vpn_concentrator_id="vpnConcentratorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf28dff327f18ae4342188e770ccb6c452865572f40526391ed06f1edfedcc2c)
            check_type(argname="argument vpn_concentrator_id", value=vpn_concentrator_id, expected_type=type_hints["vpn_concentrator_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpn_concentrator_id": vpn_concentrator_id,
        }

    @builtins.property
    def vpn_concentrator_id(self) -> builtins.str:
        '''The VpnConcentratorId of the VPNConcentrator resource.'''
        result = self._values.get("vpn_concentrator_id")
        assert result is not None, "Required property 'vpn_concentrator_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPNConcentratorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPNConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"vpn_connection_id": "vpnConnectionId"},
)
class VPNConnectionReference:
    def __init__(self, *, vpn_connection_id: builtins.str) -> None:
        '''A reference to a VPNConnection resource.

        :param vpn_connection_id: The VpnConnectionId of the VPNConnection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pNConnection_reference = interfaces_ec2.VPNConnectionReference(
                vpn_connection_id="vpnConnectionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4d9cf45193f00d245a613110cda3f4a881f72d8c00abbeb935c2280eaa78b66)
            check_type(argname="argument vpn_connection_id", value=vpn_connection_id, expected_type=type_hints["vpn_connection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpn_connection_id": vpn_connection_id,
        }

    @builtins.property
    def vpn_connection_id(self) -> builtins.str:
        '''The VpnConnectionId of the VPNConnection resource.'''
        result = self._values.get("vpn_connection_id")
        assert result is not None, "Required property 'vpn_connection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPNConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPNConnectionRouteReference",
    jsii_struct_bases=[],
    name_mapping={
        "destination_cidr_block": "destinationCidrBlock",
        "vpn_connection_id": "vpnConnectionId",
    },
)
class VPNConnectionRouteReference:
    def __init__(
        self,
        *,
        destination_cidr_block: builtins.str,
        vpn_connection_id: builtins.str,
    ) -> None:
        '''A reference to a VPNConnectionRoute resource.

        :param destination_cidr_block: The DestinationCidrBlock of the VPNConnectionRoute resource.
        :param vpn_connection_id: The VpnConnectionId of the VPNConnectionRoute resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pNConnection_route_reference = interfaces_ec2.VPNConnectionRouteReference(
                destination_cidr_block="destinationCidrBlock",
                vpn_connection_id="vpnConnectionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5418a3e3d502676e61ccb4a41db85956ba34b47557ef8ea770f0910743f9846b)
            check_type(argname="argument destination_cidr_block", value=destination_cidr_block, expected_type=type_hints["destination_cidr_block"])
            check_type(argname="argument vpn_connection_id", value=vpn_connection_id, expected_type=type_hints["vpn_connection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_cidr_block": destination_cidr_block,
            "vpn_connection_id": vpn_connection_id,
        }

    @builtins.property
    def destination_cidr_block(self) -> builtins.str:
        '''The DestinationCidrBlock of the VPNConnectionRoute resource.'''
        result = self._values.get("destination_cidr_block")
        assert result is not None, "Required property 'destination_cidr_block' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpn_connection_id(self) -> builtins.str:
        '''The VpnConnectionId of the VPNConnectionRoute resource.'''
        result = self._values.get("vpn_connection_id")
        assert result is not None, "Required property 'vpn_connection_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPNConnectionRouteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPNGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"vpn_gateway_id": "vpnGatewayId"},
)
class VPNGatewayReference:
    def __init__(self, *, vpn_gateway_id: builtins.str) -> None:
        '''A reference to a VPNGateway resource.

        :param vpn_gateway_id: The VPNGatewayId of the VPNGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pNGateway_reference = interfaces_ec2.VPNGatewayReference(
                vpn_gateway_id="vpnGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bd8afece8203d01cc095d20caf9bdef6bbf03a1e3f942d508190dcc3cd88fa5)
            check_type(argname="argument vpn_gateway_id", value=vpn_gateway_id, expected_type=type_hints["vpn_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpn_gateway_id": vpn_gateway_id,
        }

    @builtins.property
    def vpn_gateway_id(self) -> builtins.str:
        '''The VPNGatewayId of the VPNGateway resource.'''
        result = self._values.get("vpn_gateway_id")
        assert result is not None, "Required property 'vpn_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPNGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VPNGatewayRoutePropagationReference",
    jsii_struct_bases=[],
    name_mapping={"vpn_gateway_route_propagation_id": "vpnGatewayRoutePropagationId"},
)
class VPNGatewayRoutePropagationReference:
    def __init__(self, *, vpn_gateway_route_propagation_id: builtins.str) -> None:
        '''A reference to a VPNGatewayRoutePropagation resource.

        :param vpn_gateway_route_propagation_id: The Id of the VPNGatewayRoutePropagation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            v_pNGateway_route_propagation_reference = interfaces_ec2.VPNGatewayRoutePropagationReference(
                vpn_gateway_route_propagation_id="vpnGatewayRoutePropagationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fad5fd83b7e306265db68f7eccd5e0df0448e18217d065355e4d3147a79369c)
            check_type(argname="argument vpn_gateway_route_propagation_id", value=vpn_gateway_route_propagation_id, expected_type=type_hints["vpn_gateway_route_propagation_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpn_gateway_route_propagation_id": vpn_gateway_route_propagation_id,
        }

    @builtins.property
    def vpn_gateway_route_propagation_id(self) -> builtins.str:
        '''The Id of the VPNGatewayRoutePropagation resource.'''
        result = self._values.get("vpn_gateway_route_propagation_id")
        assert result is not None, "Required property 'vpn_gateway_route_propagation_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPNGatewayRoutePropagationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VerifiedAccessEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"verified_access_endpoint_id": "verifiedAccessEndpointId"},
)
class VerifiedAccessEndpointReference:
    def __init__(self, *, verified_access_endpoint_id: builtins.str) -> None:
        '''A reference to a VerifiedAccessEndpoint resource.

        :param verified_access_endpoint_id: The VerifiedAccessEndpointId of the VerifiedAccessEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            verified_access_endpoint_reference = interfaces_ec2.VerifiedAccessEndpointReference(
                verified_access_endpoint_id="verifiedAccessEndpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85ecc9afe5fbda6fa04024d3d80e183ff29e91a92d20dfc1140bdc996140de87)
            check_type(argname="argument verified_access_endpoint_id", value=verified_access_endpoint_id, expected_type=type_hints["verified_access_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "verified_access_endpoint_id": verified_access_endpoint_id,
        }

    @builtins.property
    def verified_access_endpoint_id(self) -> builtins.str:
        '''The VerifiedAccessEndpointId of the VerifiedAccessEndpoint resource.'''
        result = self._values.get("verified_access_endpoint_id")
        assert result is not None, "Required property 'verified_access_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerifiedAccessEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VerifiedAccessGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "verified_access_group_arn": "verifiedAccessGroupArn",
        "verified_access_group_id": "verifiedAccessGroupId",
    },
)
class VerifiedAccessGroupReference:
    def __init__(
        self,
        *,
        verified_access_group_arn: builtins.str,
        verified_access_group_id: builtins.str,
    ) -> None:
        '''A reference to a VerifiedAccessGroup resource.

        :param verified_access_group_arn: The ARN of the VerifiedAccessGroup resource.
        :param verified_access_group_id: The VerifiedAccessGroupId of the VerifiedAccessGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            verified_access_group_reference = interfaces_ec2.VerifiedAccessGroupReference(
                verified_access_group_arn="verifiedAccessGroupArn",
                verified_access_group_id="verifiedAccessGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fef9fe84154b9d4ff637f01793f165ccc0a606d42f823be80cfc517d8b164869)
            check_type(argname="argument verified_access_group_arn", value=verified_access_group_arn, expected_type=type_hints["verified_access_group_arn"])
            check_type(argname="argument verified_access_group_id", value=verified_access_group_id, expected_type=type_hints["verified_access_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "verified_access_group_arn": verified_access_group_arn,
            "verified_access_group_id": verified_access_group_id,
        }

    @builtins.property
    def verified_access_group_arn(self) -> builtins.str:
        '''The ARN of the VerifiedAccessGroup resource.'''
        result = self._values.get("verified_access_group_arn")
        assert result is not None, "Required property 'verified_access_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def verified_access_group_id(self) -> builtins.str:
        '''The VerifiedAccessGroupId of the VerifiedAccessGroup resource.'''
        result = self._values.get("verified_access_group_id")
        assert result is not None, "Required property 'verified_access_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerifiedAccessGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VerifiedAccessInstanceReference",
    jsii_struct_bases=[],
    name_mapping={"verified_access_instance_id": "verifiedAccessInstanceId"},
)
class VerifiedAccessInstanceReference:
    def __init__(self, *, verified_access_instance_id: builtins.str) -> None:
        '''A reference to a VerifiedAccessInstance resource.

        :param verified_access_instance_id: The VerifiedAccessInstanceId of the VerifiedAccessInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            verified_access_instance_reference = interfaces_ec2.VerifiedAccessInstanceReference(
                verified_access_instance_id="verifiedAccessInstanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__028ce8f85d9922da12b435f8f369c360fd406edd22e248398f659ddadef6d19a)
            check_type(argname="argument verified_access_instance_id", value=verified_access_instance_id, expected_type=type_hints["verified_access_instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "verified_access_instance_id": verified_access_instance_id,
        }

    @builtins.property
    def verified_access_instance_id(self) -> builtins.str:
        '''The VerifiedAccessInstanceId of the VerifiedAccessInstance resource.'''
        result = self._values.get("verified_access_instance_id")
        assert result is not None, "Required property 'verified_access_instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerifiedAccessInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VerifiedAccessTrustProviderReference",
    jsii_struct_bases=[],
    name_mapping={
        "verified_access_trust_provider_id": "verifiedAccessTrustProviderId",
    },
)
class VerifiedAccessTrustProviderReference:
    def __init__(self, *, verified_access_trust_provider_id: builtins.str) -> None:
        '''A reference to a VerifiedAccessTrustProvider resource.

        :param verified_access_trust_provider_id: The VerifiedAccessTrustProviderId of the VerifiedAccessTrustProvider resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            verified_access_trust_provider_reference = interfaces_ec2.VerifiedAccessTrustProviderReference(
                verified_access_trust_provider_id="verifiedAccessTrustProviderId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c2d7cfcee71ba991341eb870c161ff0526f7cf949d8a80fddd7285c12bf1e99)
            check_type(argname="argument verified_access_trust_provider_id", value=verified_access_trust_provider_id, expected_type=type_hints["verified_access_trust_provider_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "verified_access_trust_provider_id": verified_access_trust_provider_id,
        }

    @builtins.property
    def verified_access_trust_provider_id(self) -> builtins.str:
        '''The VerifiedAccessTrustProviderId of the VerifiedAccessTrustProvider resource.'''
        result = self._values.get("verified_access_trust_provider_id")
        assert result is not None, "Required property 'verified_access_trust_provider_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VerifiedAccessTrustProviderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VolumeAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"instance_id": "instanceId", "volume_id": "volumeId"},
)
class VolumeAttachmentReference:
    def __init__(self, *, instance_id: builtins.str, volume_id: builtins.str) -> None:
        '''A reference to a VolumeAttachment resource.

        :param instance_id: The InstanceId of the VolumeAttachment resource.
        :param volume_id: The VolumeId of the VolumeAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            volume_attachment_reference = interfaces_ec2.VolumeAttachmentReference(
                instance_id="instanceId",
                volume_id="volumeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d705bbd7e7c8da982741cbdc4293faebde0fbc97f74c5042697e55eebd73f25d)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_id": instance_id,
            "volume_id": volume_id,
        }

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''The InstanceId of the VolumeAttachment resource.'''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The VolumeId of the VolumeAttachment resource.'''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ec2.VolumeReference",
    jsii_struct_bases=[],
    name_mapping={"volume_id": "volumeId"},
)
class VolumeReference:
    def __init__(self, *, volume_id: builtins.str) -> None:
        '''A reference to a Volume resource.

        :param volume_id: The VolumeId of the Volume resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ec2 as interfaces_ec2
            
            volume_reference = interfaces_ec2.VolumeReference(
                volume_id="volumeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bdce5af9d1e135e7564b00f4d9b2945ac4e23e3d35d3e993e24d29db0830b42)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The VolumeId of the Volume resource.'''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CapacityManagerDataExportReference",
    "CapacityReservationFleetReference",
    "CapacityReservationReference",
    "CarrierGatewayReference",
    "ClientVpnAuthorizationRuleReference",
    "ClientVpnEndpointReference",
    "ClientVpnRouteReference",
    "ClientVpnTargetNetworkAssociationReference",
    "CustomerGatewayReference",
    "DHCPOptionsReference",
    "EC2FleetReference",
    "EIPAssociationReference",
    "EIPReference",
    "EgressOnlyInternetGatewayReference",
    "EnclaveCertificateIamRoleAssociationReference",
    "FlowLogReference",
    "GatewayRouteTableAssociationReference",
    "HostReference",
    "ICapacityManagerDataExportRef",
    "ICapacityReservationFleetRef",
    "ICapacityReservationRef",
    "ICarrierGatewayRef",
    "IClientVpnAuthorizationRuleRef",
    "IClientVpnEndpointRef",
    "IClientVpnRouteRef",
    "IClientVpnTargetNetworkAssociationRef",
    "ICustomerGatewayRef",
    "IDHCPOptionsRef",
    "IEC2FleetRef",
    "IEIPAssociationRef",
    "IEIPRef",
    "IEgressOnlyInternetGatewayRef",
    "IEnclaveCertificateIamRoleAssociationRef",
    "IFlowLogRef",
    "IGatewayRouteTableAssociationRef",
    "IHostRef",
    "IIPAMAllocationRef",
    "IIPAMPoolCidrRef",
    "IIPAMPoolRef",
    "IIPAMPrefixListResolverRef",
    "IIPAMRef",
    "IIPAMResourceDiscoveryAssociationRef",
    "IIPAMResourceDiscoveryRef",
    "IIPAMScopeRef",
    "IInstanceConnectEndpointRef",
    "IInstanceRef",
    "IInternetGatewayRef",
    "IIpPoolRouteTableAssociationRef",
    "IKeyPairRef",
    "ILaunchTemplateRef",
    "ILocalGatewayRouteRef",
    "ILocalGatewayRouteTableRef",
    "ILocalGatewayRouteTableVPCAssociationRef",
    "ILocalGatewayRouteTableVirtualInterfaceGroupAssociationRef",
    "ILocalGatewayVirtualInterfaceGroupRef",
    "ILocalGatewayVirtualInterfaceRef",
    "INatGatewayRef",
    "INetworkAclEntryRef",
    "INetworkAclRef",
    "INetworkInsightsAccessScopeAnalysisRef",
    "INetworkInsightsAccessScopeRef",
    "INetworkInsightsAnalysisRef",
    "INetworkInsightsPathRef",
    "INetworkInterfaceAttachmentRef",
    "INetworkInterfacePermissionRef",
    "INetworkInterfaceRef",
    "INetworkPerformanceMetricSubscriptionRef",
    "IPAMAllocationReference",
    "IPAMPoolCidrReference",
    "IPAMPoolReference",
    "IPAMPrefixListResolverReference",
    "IPAMReference",
    "IPAMResourceDiscoveryAssociationReference",
    "IPAMResourceDiscoveryReference",
    "IPAMScopeReference",
    "IPlacementGroupRef",
    "IPrefixListRef",
    "IRouteRef",
    "IRouteServerAssociationRef",
    "IRouteServerEndpointRef",
    "IRouteServerPeerRef",
    "IRouteServerPropagationRef",
    "IRouteServerRef",
    "IRouteTableRef",
    "ISecurityGroupEgressRef",
    "ISecurityGroupIngressRef",
    "ISecurityGroupRef",
    "ISecurityGroupVpcAssociationRef",
    "ISnapshotBlockPublicAccessRef",
    "ISpotFleetRef",
    "ISubnetCidrBlockRef",
    "ISubnetNetworkAclAssociationRef",
    "ISubnetRef",
    "ISubnetRouteTableAssociationRef",
    "ITrafficMirrorFilterRef",
    "ITrafficMirrorFilterRuleRef",
    "ITrafficMirrorSessionRef",
    "ITrafficMirrorTargetRef",
    "ITransitGatewayAttachmentRef",
    "ITransitGatewayConnectPeerRef",
    "ITransitGatewayConnectRef",
    "ITransitGatewayMeteringPolicyEntryRef",
    "ITransitGatewayMeteringPolicyRef",
    "ITransitGatewayMulticastDomainAssociationRef",
    "ITransitGatewayMulticastDomainRef",
    "ITransitGatewayMulticastGroupMemberRef",
    "ITransitGatewayMulticastGroupSourceRef",
    "ITransitGatewayPeeringAttachmentRef",
    "ITransitGatewayRef",
    "ITransitGatewayRouteRef",
    "ITransitGatewayRouteTableAssociationRef",
    "ITransitGatewayRouteTablePropagationRef",
    "ITransitGatewayRouteTableRef",
    "ITransitGatewayVpcAttachmentRef",
    "IVPCBlockPublicAccessExclusionRef",
    "IVPCBlockPublicAccessOptionsRef",
    "IVPCCidrBlockRef",
    "IVPCDHCPOptionsAssociationRef",
    "IVPCEncryptionControlRef",
    "IVPCEndpointConnectionNotificationRef",
    "IVPCEndpointRef",
    "IVPCEndpointServicePermissionsRef",
    "IVPCEndpointServiceRef",
    "IVPCGatewayAttachmentRef",
    "IVPCPeeringConnectionRef",
    "IVPCRef",
    "IVPNConcentratorRef",
    "IVPNConnectionRef",
    "IVPNConnectionRouteRef",
    "IVPNGatewayRef",
    "IVPNGatewayRoutePropagationRef",
    "IVerifiedAccessEndpointRef",
    "IVerifiedAccessGroupRef",
    "IVerifiedAccessInstanceRef",
    "IVerifiedAccessTrustProviderRef",
    "IVolumeAttachmentRef",
    "IVolumeRef",
    "InstanceConnectEndpointReference",
    "InstanceReference",
    "InternetGatewayReference",
    "IpPoolRouteTableAssociationReference",
    "KeyPairReference",
    "LaunchTemplateReference",
    "LocalGatewayRouteReference",
    "LocalGatewayRouteTableReference",
    "LocalGatewayRouteTableVPCAssociationReference",
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationReference",
    "LocalGatewayVirtualInterfaceGroupReference",
    "LocalGatewayVirtualInterfaceReference",
    "NatGatewayReference",
    "NetworkAclEntryReference",
    "NetworkAclReference",
    "NetworkInsightsAccessScopeAnalysisReference",
    "NetworkInsightsAccessScopeReference",
    "NetworkInsightsAnalysisReference",
    "NetworkInsightsPathReference",
    "NetworkInterfaceAttachmentReference",
    "NetworkInterfacePermissionReference",
    "NetworkInterfaceReference",
    "NetworkPerformanceMetricSubscriptionReference",
    "PlacementGroupReference",
    "PrefixListReference",
    "RouteReference",
    "RouteServerAssociationReference",
    "RouteServerEndpointReference",
    "RouteServerPeerReference",
    "RouteServerPropagationReference",
    "RouteServerReference",
    "RouteTableReference",
    "SecurityGroupEgressReference",
    "SecurityGroupIngressReference",
    "SecurityGroupReference",
    "SecurityGroupVpcAssociationReference",
    "SnapshotBlockPublicAccessReference",
    "SpotFleetReference",
    "SubnetCidrBlockReference",
    "SubnetNetworkAclAssociationReference",
    "SubnetReference",
    "SubnetRouteTableAssociationReference",
    "TrafficMirrorFilterReference",
    "TrafficMirrorFilterRuleReference",
    "TrafficMirrorSessionReference",
    "TrafficMirrorTargetReference",
    "TransitGatewayAttachmentReference",
    "TransitGatewayConnectPeerReference",
    "TransitGatewayConnectReference",
    "TransitGatewayMeteringPolicyEntryReference",
    "TransitGatewayMeteringPolicyReference",
    "TransitGatewayMulticastDomainAssociationReference",
    "TransitGatewayMulticastDomainReference",
    "TransitGatewayMulticastGroupMemberReference",
    "TransitGatewayMulticastGroupSourceReference",
    "TransitGatewayPeeringAttachmentReference",
    "TransitGatewayReference",
    "TransitGatewayRouteReference",
    "TransitGatewayRouteTableAssociationReference",
    "TransitGatewayRouteTablePropagationReference",
    "TransitGatewayRouteTableReference",
    "TransitGatewayVpcAttachmentReference",
    "VPCBlockPublicAccessExclusionReference",
    "VPCBlockPublicAccessOptionsReference",
    "VPCCidrBlockReference",
    "VPCDHCPOptionsAssociationReference",
    "VPCEncryptionControlReference",
    "VPCEndpointConnectionNotificationReference",
    "VPCEndpointReference",
    "VPCEndpointServicePermissionsReference",
    "VPCEndpointServiceReference",
    "VPCGatewayAttachmentReference",
    "VPCPeeringConnectionReference",
    "VPCReference",
    "VPNConcentratorReference",
    "VPNConnectionReference",
    "VPNConnectionRouteReference",
    "VPNGatewayReference",
    "VPNGatewayRoutePropagationReference",
    "VerifiedAccessEndpointReference",
    "VerifiedAccessGroupReference",
    "VerifiedAccessInstanceReference",
    "VerifiedAccessTrustProviderReference",
    "VolumeAttachmentReference",
    "VolumeReference",
]

publication.publish()

def _typecheckingstub__6b9a5eb41f01361d654103936a1b9162b653c840153b29de7c1a9fd3b59192fb(
    *,
    capacity_manager_data_export_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a639beaf30f994702c8cce7edf0705ad867304287d6ef4b89b9d26288bcf32dc(
    *,
    capacity_reservation_fleet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c9ad69aaf7d522f4991de0383043ae158e9356f51e89f794bed440c4a0e47da(
    *,
    capacity_reservation_arn: builtins.str,
    capacity_reservation_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0e46133742af7c64acb96c7643cdd4b68523b466749e2e2f37a9b8fb3c3e311(
    *,
    carrier_gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57fa36bad5ea59002afc4e1ffe1f5e727fc3229f1b2cfb394708c3fe01884cd7(
    *,
    client_vpn_authorization_rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3483bfe3b3da3b5359fa2a5ef1fcb0071cbabc25dc4825b83c857cc83437b76(
    *,
    client_vpn_endpoint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955d0e41ede8d58fe3f1e03206fcc6cf2c837c6a701c1cdbfcdb58c18e7fef2f(
    *,
    client_vpn_route_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3c7fcd523c40c46f0da3e82691f5dd7318f305bacc934e54d00ced4247cdc9d(
    *,
    client_vpn_target_network_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3af586fe619a2c65fed2a5927f842d40e7d8218e2affcc6d9632c1f96c1a5f08(
    *,
    customer_gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e883f4c5fc03af683cd9793dfbd9657b07f02feb74e5fc9ccaaa558e82d8b1cb(
    *,
    dhcp_options_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a9a7b73ab5651dd8a52334ffb8d29401dc3fa34c2fe49e7a22e3dfcd471697(
    *,
    fleet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa3055e31c0189eeb8900337e9a55041990b609176240fdfb650e8d6ea71ce4f(
    *,
    eip_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a670552386e3bc70dcecf664a8471c2e1ae1e3d6daecb073bb63f3a449edf2e(
    *,
    allocation_id: builtins.str,
    public_ip: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d13b682c8162d3e06226c015673682f4ca0b635bf82debdfa16df85ebff4c9c4(
    *,
    egress_only_internet_gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52a31f01eec480fc55294e086132d2231213830dc4e9ffe9768bac28e14e514b(
    *,
    certificate_arn: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c7f7816dd23c5966fe0b62e931bf88b8f149b9f474737f0550657e967cf640f(
    *,
    flow_log_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d71f159bc2caf82458bd401787c04be0e393554b0767a258a4c1f03a7254ee(
    *,
    gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d7ca0868625d89fec5ae55e8e630cc64fa2b42416142c1e2df8e9388dc41c50(
    *,
    host_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7feb4439f565248f1d51f179a7e018bb0fb9c2a8a48ea0d41c27aed11307ea75(
    *,
    cidr: builtins.str,
    ipam_pool_allocation_id: builtins.str,
    ipam_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3683b95716ecb232814e443e685b635edbf9643420649ae07689e14b51dfcc17(
    *,
    ipam_pool_cidr_id: builtins.str,
    ipam_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54638f34ae06307f1bc4313c2916619169655bbba473fe8a9c1bc2378c38dbc8(
    *,
    ipam_pool_arn: builtins.str,
    ipam_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ac17af28aa1061e001efd103ab675ccb82fc60c97079265f5fdddbcde5fdd3(
    *,
    ipam_prefix_list_resolver_arn: builtins.str,
    ipam_prefix_list_resolver_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4b18eb7f984a38a0d1b97de048402fd4bff3a9c791619a68aa7bba3b69b606c(
    *,
    ipam_arn: builtins.str,
    ipam_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc737e46a3649729021f88f43561d31e8fdcefc112469a6222d8a7681574227(
    *,
    ipam_resource_discovery_association_arn: builtins.str,
    ipam_resource_discovery_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2ea9e66efdddfa8669cc157e45981e03ce182eab234c9a9ea016baa95bd4659(
    *,
    ipam_resource_discovery_arn: builtins.str,
    ipam_resource_discovery_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da183a6f045185e65fe67a7bb0f4e74662c652173a7c3c2d9103452e54ccbbbf(
    *,
    ipam_scope_arn: builtins.str,
    ipam_scope_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04da4a11a170a51c13416eafbc1b7d6de587ae16bc76f69212089fec3dfd9e2d(
    *,
    instance_connect_endpoint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f06433ab2ca29228d26a3591c15861f26cba4cd81aba9c2d95cda5f8b7ddb93(
    *,
    instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44bb15a882c5a2c056f5f6ae2f3ea1217cad905768d2e54391ba3718f7a8c283(
    *,
    internet_gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71fccb9d8f2781c81145acb20d4e9edac01046a309260fa70dfd46e9491669a0(
    *,
    association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61e5782f64150528470b5920f05080292456f4ab0004df01a7d5afe7c860185d(
    *,
    key_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf47688316c53ea06bfbe8962e54c57c82ca920e2a4490a900c685306cb1a87b(
    *,
    launch_template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ba56b317ffe4dc9f02859993fc6b89e6bbbcc41dd1a50a72d27cd2dae68daff(
    *,
    destination_cidr_block: builtins.str,
    local_gateway_route_table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4d3ef1777d1ce52dbb1979acf4bb44d1f866b94d6fce26dcda3c6bbdbeed15e(
    *,
    local_gateway_route_table_arn: builtins.str,
    local_gateway_route_table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723ff6293ea9c624c32784a1606ec5d4a9a0ce6894e65dd54743fbb3288df447(
    *,
    local_gateway_route_table_vpc_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0076a6af4d4d2b3e177ad2bcea7af4a8750788c36d756571817af42a9bc1795(
    *,
    local_gateway_route_table_virtual_interface_group_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c90fb542fdb8637b80e36f928d9aeceac19bf3776dfe903d370479c61f0d98e(
    *,
    local_gateway_virtual_interface_group_arn: builtins.str,
    local_gateway_virtual_interface_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d5bf34161cfcac3c7f30d5f7b7235fdbb2ef9fbd82094e8dab5402940143604(
    *,
    local_gateway_virtual_interface_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9284f94b93190b143fb72727e011f823e94d36b5c25f65e1bd8cee3b963d87b6(
    *,
    nat_gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27f02a8f8524fa23ca08af1d692e0639a10fc0d9e01667fcd46edd61ce7c70ba(
    *,
    network_acl_entry_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c66ff6eb994eb559c72f9480f9db93a2eeb06c8c6d37ef4e6525316539cc49e5(
    *,
    network_acl_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b304b9f1134521a55ecdd3ca088bf067a718845c1201a93e296c0ab9a63efd7(
    *,
    network_insights_access_scope_analysis_arn: builtins.str,
    network_insights_access_scope_analysis_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df6fa29d56c295e8cc643265a349fa9299af85d29a099b44f05f728333bc7d68(
    *,
    network_insights_access_scope_arn: builtins.str,
    network_insights_access_scope_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41c5de5540a2b0098d268fa120f8031f855048589a832d2a31a668185bbddab1(
    *,
    network_insights_analysis_arn: builtins.str,
    network_insights_analysis_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66a7973f92c21942c518f8eeb207fddd4f05cd8a3b3d6d4b882c4fec4bcd415b(
    *,
    network_insights_path_arn: builtins.str,
    network_insights_path_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c88066168b198ea6639664fda4fc84ed5b24c2b90541bb4cc402eacbcf26c1a(
    *,
    attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3c3c5b9969f763f0c64ce39c680f2e98370b3255f0d5a443eae02ab17ce9bd(
    *,
    network_interface_permission_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5919adb4a6febe429841e83e6060ccb4cbef8c3abc4f8e3b6d90e67f7774664b(
    *,
    network_interface_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae7ca3b2520848fb208f1f073b999fa18862f731f22e0ed61b0f33e113e84314(
    *,
    destination: builtins.str,
    metric: builtins.str,
    source: builtins.str,
    statistic: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5765f3379a78633c12e5a0f7f44b8607e7ec0673147343d6ed57ff461fe296d5(
    *,
    group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5511f84caafda82a5823be04257a6bc66b8e650cafde60346ea5dba962bbe45f(
    *,
    prefix_list_arn: builtins.str,
    prefix_list_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071d8281200dbc8a56815f028a15047533e43d4006bd454bb2112a062187aab6(
    *,
    cidr_block: builtins.str,
    route_table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32c2b597b0ef56b2be955617b20c204c3229f2200a027ab101729b15cdd488fa(
    *,
    route_server_id: builtins.str,
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__604ffb342b3bdc73a00058584dee047a0c158a0fa83d67bf2ec1d41fcbb63ebc(
    *,
    route_server_endpoint_arn: builtins.str,
    route_server_endpoint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6236f4a0ba03f39efd5e1046cbc3f9787eab627bd9c7605cbb239e875dff53f(
    *,
    route_server_peer_arn: builtins.str,
    route_server_peer_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec6dc1a55da909a26dc9a339b304e6d77d5744cf4ff250a9f9be3d9b775a66e4(
    *,
    route_server_id: builtins.str,
    route_table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efff2c3f9e57b3b247745af2b155b69f9d9e3ead1daec3dd115ce2158e01e375(
    *,
    route_server_arn: builtins.str,
    route_server_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__188eecb4e01c772367f802e75fe78a87fe1af4420eb919a629db4f794178d131(
    *,
    route_table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0be0b2564d7c31d9bc03311d9327527e8e38438583c1dddcc84256ea3117542(
    *,
    security_group_egress_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e5c9332b43e9c0da2df0fc5e03d679f818b14c48802afad4a3142afd64c3be(
    *,
    security_group_ingress_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0db1d7cd391a8af80a1fb9ff07216b42a4dd0046e0970b88a8c980e5fc5dba6f(
    *,
    security_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99b958e983f4c514199c4bea21e7fb7965cfcb29980b1b4db814bdbab612a999(
    *,
    group_id: builtins.str,
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ad7a412bb4a7b19786369fbb394c471b2636bbcb63104a8ad0494d4e1333101(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e118107621a5bd1c8bc349d74994c79a1a88962c110757dc9faba1d47504c73a(
    *,
    spot_fleet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6afd0bd0b6454ebc029c534dc448712d3ba20ac3ab16969fba368228dfe49c40(
    *,
    subnet_cidr_block_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33b2d56f1de8c36fb8b18796caf24be422cd959f3d196021081df0f784129620(
    *,
    association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c11ffeb00d907db6208591d4cb8554a1a39e42d75f3167e4dcbd07f49ae5a8aa(
    *,
    subnet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa99ad2bc407d92eb9c3198a931831d5546abe03377f0579d8446168cb939e4(
    *,
    subnet_route_table_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0402b0873722cf0cf79c419e8abf4342bb2693c80a72aa75fa35e89dd6a4978f(
    *,
    traffic_mirror_filter_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f48e3d119ce3b20c46298a4e32d4308e1c544570d3335943e89cc9b985cce45b(
    *,
    traffic_mirror_filter_rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef09d27d4ecc067dd0ecc3aaf93fa5b28de397da0443888e4044c29b20c3ecb0(
    *,
    traffic_mirror_session_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3ab01ca9a5683fa84e2013c5b5dd1998daa11eb9d67b91630464d8c40e967cb(
    *,
    traffic_mirror_target_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d00c8241f7c73c4c87059cfd039d51f5660c67a6100348cac3bd46760ada98c(
    *,
    transit_gateway_attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd6c8f8f03f34359b5ba738fbf290977b3fe4bc7cb209923bf5cec9052480554(
    *,
    transit_gateway_connect_peer_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8890329f7e30c11a4944c99fc332973f5280ac00a0222b1631d4e50bd7f262d(
    *,
    transit_gateway_attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b5ab879ac9cab67aeb0a61553565ffea8f306e89f552a533dfd930f59d7ed24(
    *,
    policy_rule_number: builtins.str,
    transit_gateway_metering_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01cc92df7f25b3e6a54bc6e93fbabb355be5b5f7dec1c6e4fc273e7f663f7d38(
    *,
    transit_gateway_metering_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__095a9cdfacf328704a9d19f22212da96cbb6e9c6e1ec4bc67d2a0d960e1ec805(
    *,
    subnet_id: builtins.str,
    transit_gateway_attachment_id: builtins.str,
    transit_gateway_multicast_domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f5a19765b0859abb7dae874b479771317759b9e92e4cc5f27ae398b2afb775c(
    *,
    transit_gateway_multicast_domain_arn: builtins.str,
    transit_gateway_multicast_domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c224bd05272e424c61d5175c14f8f89e49fa9d16676a2eff3ad0883ffd152668(
    *,
    group_ip_address: builtins.str,
    network_interface_id: builtins.str,
    transit_gateway_multicast_domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4289e401a4bd5d88d9c836aee8d224ff8c8f11d601afe36b0f89e72cb3c14aa6(
    *,
    group_ip_address: builtins.str,
    network_interface_id: builtins.str,
    transit_gateway_multicast_domain_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64897c67231def1034314d171a43235f95e68fe614b1f5d838fb9917e3da522(
    *,
    transit_gateway_attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d42ecfd465267df55b09ea969ba78c292f56d9299bc36fff859bc519571119ae(
    *,
    transit_gateway_arn: builtins.str,
    transit_gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cd7817dd4938ea0b305988047341a875562b9b0809ef57097bc4e4ffd4460fb(
    *,
    destination_cidr_block: builtins.str,
    transit_gateway_route_table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c33d3d19d0e848e40b21297daa62bca5880d7bc107c8facc1dd71b21ff33ce67(
    *,
    transit_gateway_attachment_id: builtins.str,
    transit_gateway_route_table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26cc3fa7b96f8ff924a971f4c6aba753df2b70d2228ac1957647f1bdbbf93ddd(
    *,
    transit_gateway_attachment_id: builtins.str,
    transit_gateway_route_table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d136220ebea5c59d10453273ed8808e0d88ffa850ad4d4e3c6c3b0e5b44f71a0(
    *,
    transit_gateway_route_table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e885276231a10adb8fbe57ea37365132400a9fdca6f023b139de68a78ba903e6(
    *,
    transit_gateway_vpc_attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64ac34d1e793b8a1d8cd1d1a75292e5b7b029250a6390d5ca27acedbd3fecb4f(
    *,
    exclusion_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e2a531906cb95c5eef8a6c02d378c377fd729bc96102c0833ec0ab0e2d7f254(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32e1c330fb9834ac94e8aa6803768ee36f502b213c52c48c0933f09b30b57ea1(
    *,
    vpc_cidr_block_id: builtins.str,
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28adc76405810a691e2dce4b43c95660c0222b01d8b1608d5d87395daec6db7a(
    *,
    dhcp_options_id: builtins.str,
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ed3ca4369a94bd67b33fd9728c1616ecc391d119a17b6a19ab268a1aca8e83(
    *,
    vpc_encryption_control_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b45a1f3c71e5b9b9649f83833be2f40dc9cf8841b63e22009a2633c261982ea(
    *,
    vpc_endpoint_connection_notification_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a81418feee4b7635ba4140c24db110bc53e15bf753a79d0166d5354282595c2(
    *,
    vpc_endpoint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__722a1440530819cc37aa35cb38e324750dd1ca13f95b4198238e1c6e4c45b5b9(
    *,
    service_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1efcd12a0cc1df35811dc764325f9bce362912be0e055d83f68803ed158167de(
    *,
    service_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0683bb8dcc4090236382f6417afb8c7a6f1b028b789970abf6518876d8ece05(
    *,
    attachment_type: builtins.str,
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e223c0b1eeb03afe708e1dfb3a2d0d857eed62cf5a55e4f8ae20a75afe6e2435(
    *,
    vpc_peering_connection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eebcb09c1a21f835d06e0bc7c5cb0b566f1c84adaf87a8ad692fff4be8a5c6ff(
    *,
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf28dff327f18ae4342188e770ccb6c452865572f40526391ed06f1edfedcc2c(
    *,
    vpn_concentrator_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d9cf45193f00d245a613110cda3f4a881f72d8c00abbeb935c2280eaa78b66(
    *,
    vpn_connection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5418a3e3d502676e61ccb4a41db85956ba34b47557ef8ea770f0910743f9846b(
    *,
    destination_cidr_block: builtins.str,
    vpn_connection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd8afece8203d01cc095d20caf9bdef6bbf03a1e3f942d508190dcc3cd88fa5(
    *,
    vpn_gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fad5fd83b7e306265db68f7eccd5e0df0448e18217d065355e4d3147a79369c(
    *,
    vpn_gateway_route_propagation_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ecc9afe5fbda6fa04024d3d80e183ff29e91a92d20dfc1140bdc996140de87(
    *,
    verified_access_endpoint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fef9fe84154b9d4ff637f01793f165ccc0a606d42f823be80cfc517d8b164869(
    *,
    verified_access_group_arn: builtins.str,
    verified_access_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__028ce8f85d9922da12b435f8f369c360fd406edd22e248398f659ddadef6d19a(
    *,
    verified_access_instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c2d7cfcee71ba991341eb870c161ff0526f7cf949d8a80fddd7285c12bf1e99(
    *,
    verified_access_trust_provider_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d705bbd7e7c8da982741cbdc4293faebde0fbc97f74c5042697e55eebd73f25d(
    *,
    instance_id: builtins.str,
    volume_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bdce5af9d1e135e7564b00f4d9b2945ac4e23e3d35d3e993e24d29db0830b42(
    *,
    volume_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICapacityManagerDataExportRef, ICapacityReservationFleetRef, ICapacityReservationRef, ICarrierGatewayRef, IClientVpnAuthorizationRuleRef, IClientVpnEndpointRef, IClientVpnRouteRef, IClientVpnTargetNetworkAssociationRef, ICustomerGatewayRef, IDHCPOptionsRef, IEC2FleetRef, IEIPAssociationRef, IEIPRef, IEgressOnlyInternetGatewayRef, IEnclaveCertificateIamRoleAssociationRef, IFlowLogRef, IGatewayRouteTableAssociationRef, IHostRef, IIPAMAllocationRef, IIPAMPoolCidrRef, IIPAMPoolRef, IIPAMPrefixListResolverRef, IIPAMRef, IIPAMResourceDiscoveryAssociationRef, IIPAMResourceDiscoveryRef, IIPAMScopeRef, IInstanceConnectEndpointRef, IInstanceRef, IInternetGatewayRef, IIpPoolRouteTableAssociationRef, IKeyPairRef, ILaunchTemplateRef, ILocalGatewayRouteRef, ILocalGatewayRouteTableRef, ILocalGatewayRouteTableVPCAssociationRef, ILocalGatewayRouteTableVirtualInterfaceGroupAssociationRef, ILocalGatewayVirtualInterfaceGroupRef, ILocalGatewayVirtualInterfaceRef, INatGatewayRef, INetworkAclEntryRef, INetworkAclRef, INetworkInsightsAccessScopeAnalysisRef, INetworkInsightsAccessScopeRef, INetworkInsightsAnalysisRef, INetworkInsightsPathRef, INetworkInterfaceAttachmentRef, INetworkInterfacePermissionRef, INetworkInterfaceRef, INetworkPerformanceMetricSubscriptionRef, IPlacementGroupRef, IPrefixListRef, IRouteRef, IRouteServerAssociationRef, IRouteServerEndpointRef, IRouteServerPeerRef, IRouteServerPropagationRef, IRouteServerRef, IRouteTableRef, ISecurityGroupEgressRef, ISecurityGroupIngressRef, ISecurityGroupRef, ISecurityGroupVpcAssociationRef, ISnapshotBlockPublicAccessRef, ISpotFleetRef, ISubnetCidrBlockRef, ISubnetNetworkAclAssociationRef, ISubnetRef, ISubnetRouteTableAssociationRef, ITrafficMirrorFilterRef, ITrafficMirrorFilterRuleRef, ITrafficMirrorSessionRef, ITrafficMirrorTargetRef, ITransitGatewayAttachmentRef, ITransitGatewayConnectPeerRef, ITransitGatewayConnectRef, ITransitGatewayMeteringPolicyEntryRef, ITransitGatewayMeteringPolicyRef, ITransitGatewayMulticastDomainAssociationRef, ITransitGatewayMulticastDomainRef, ITransitGatewayMulticastGroupMemberRef, ITransitGatewayMulticastGroupSourceRef, ITransitGatewayPeeringAttachmentRef, ITransitGatewayRef, ITransitGatewayRouteRef, ITransitGatewayRouteTableAssociationRef, ITransitGatewayRouteTablePropagationRef, ITransitGatewayRouteTableRef, ITransitGatewayVpcAttachmentRef, IVPCBlockPublicAccessExclusionRef, IVPCBlockPublicAccessOptionsRef, IVPCCidrBlockRef, IVPCDHCPOptionsAssociationRef, IVPCEncryptionControlRef, IVPCEndpointConnectionNotificationRef, IVPCEndpointRef, IVPCEndpointServicePermissionsRef, IVPCEndpointServiceRef, IVPCGatewayAttachmentRef, IVPCPeeringConnectionRef, IVPCRef, IVPNConcentratorRef, IVPNConnectionRef, IVPNConnectionRouteRef, IVPNGatewayRef, IVPNGatewayRoutePropagationRef, IVerifiedAccessEndpointRef, IVerifiedAccessGroupRef, IVerifiedAccessInstanceRef, IVerifiedAccessTrustProviderRef, IVolumeAttachmentRef, IVolumeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
