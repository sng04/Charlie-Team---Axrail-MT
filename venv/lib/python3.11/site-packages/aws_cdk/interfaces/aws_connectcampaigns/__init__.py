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
    jsii_type="aws-cdk-lib.interfaces.aws_connectcampaigns.CampaignReference",
    jsii_struct_bases=[],
    name_mapping={"campaign_arn": "campaignArn"},
)
class CampaignReference:
    def __init__(self, *, campaign_arn: builtins.str) -> None:
        '''A reference to a Campaign resource.

        :param campaign_arn: The Arn of the Campaign resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_connectcampaigns as interfaces_connectcampaigns
            
            campaign_reference = interfaces_connectcampaigns.CampaignReference(
                campaign_arn="campaignArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d45c99134eca4f878613d39d6cbfa1765f90ca4bdefc8ade799295bd3b6007f)
            check_type(argname="argument campaign_arn", value=campaign_arn, expected_type=type_hints["campaign_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "campaign_arn": campaign_arn,
        }

    @builtins.property
    def campaign_arn(self) -> builtins.str:
        '''The Arn of the Campaign resource.'''
        result = self._values.get("campaign_arn")
        assert result is not None, "Required property 'campaign_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CampaignReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_connectcampaigns.ICampaignRef")
class ICampaignRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Campaign.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="campaignRef")
    def campaign_ref(self) -> "CampaignReference":
        '''(experimental) A reference to a Campaign resource.

        :stability: experimental
        '''
        ...


class _ICampaignRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Campaign.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_connectcampaigns.ICampaignRef"

    @builtins.property
    @jsii.member(jsii_name="campaignRef")
    def campaign_ref(self) -> "CampaignReference":
        '''(experimental) A reference to a Campaign resource.

        :stability: experimental
        '''
        return typing.cast("CampaignReference", jsii.get(self, "campaignRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICampaignRef).__jsii_proxy_class__ = lambda : _ICampaignRefProxy


__all__ = [
    "CampaignReference",
    "ICampaignRef",
]

publication.publish()

def _typecheckingstub__2d45c99134eca4f878613d39d6cbfa1765f90ca4bdefc8ade799295bd3b6007f(
    *,
    campaign_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICampaignRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
