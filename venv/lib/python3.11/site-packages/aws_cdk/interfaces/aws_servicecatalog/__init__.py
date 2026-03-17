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
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.AcceptedPortfolioShareReference",
    jsii_struct_bases=[],
    name_mapping={"accepted_portfolio_share_id": "acceptedPortfolioShareId"},
)
class AcceptedPortfolioShareReference:
    def __init__(self, *, accepted_portfolio_share_id: builtins.str) -> None:
        '''A reference to a AcceptedPortfolioShare resource.

        :param accepted_portfolio_share_id: The Id of the AcceptedPortfolioShare resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            accepted_portfolio_share_reference = interfaces_servicecatalog.AcceptedPortfolioShareReference(
                accepted_portfolio_share_id="acceptedPortfolioShareId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6326f3888119e6783b8c2f3210c345520ccc67dd5064e23514085258059f2c2)
            check_type(argname="argument accepted_portfolio_share_id", value=accepted_portfolio_share_id, expected_type=type_hints["accepted_portfolio_share_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "accepted_portfolio_share_id": accepted_portfolio_share_id,
        }

    @builtins.property
    def accepted_portfolio_share_id(self) -> builtins.str:
        '''The Id of the AcceptedPortfolioShare resource.'''
        result = self._values.get("accepted_portfolio_share_id")
        assert result is not None, "Required property 'accepted_portfolio_share_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AcceptedPortfolioShareReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.CloudFormationProductReference",
    jsii_struct_bases=[],
    name_mapping={"cloud_formation_product_id": "cloudFormationProductId"},
)
class CloudFormationProductReference:
    def __init__(self, *, cloud_formation_product_id: builtins.str) -> None:
        '''A reference to a CloudFormationProduct resource.

        :param cloud_formation_product_id: The Id of the CloudFormationProduct resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            cloud_formation_product_reference = interfaces_servicecatalog.CloudFormationProductReference(
                cloud_formation_product_id="cloudFormationProductId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62967c3e411db25daf0417852c200a39e2e4dd0f789a69eec9bdab47433f04fc)
            check_type(argname="argument cloud_formation_product_id", value=cloud_formation_product_id, expected_type=type_hints["cloud_formation_product_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_formation_product_id": cloud_formation_product_id,
        }

    @builtins.property
    def cloud_formation_product_id(self) -> builtins.str:
        '''The Id of the CloudFormationProduct resource.'''
        result = self._values.get("cloud_formation_product_id")
        assert result is not None, "Required property 'cloud_formation_product_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationProductReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.CloudFormationProvisionedProductReference",
    jsii_struct_bases=[],
    name_mapping={"provisioned_product_id": "provisionedProductId"},
)
class CloudFormationProvisionedProductReference:
    def __init__(self, *, provisioned_product_id: builtins.str) -> None:
        '''A reference to a CloudFormationProvisionedProduct resource.

        :param provisioned_product_id: The ProvisionedProductId of the CloudFormationProvisionedProduct resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            cloud_formation_provisioned_product_reference = interfaces_servicecatalog.CloudFormationProvisionedProductReference(
                provisioned_product_id="provisionedProductId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b6367dc67edf9798c223a04eeb171c5fa2b7131fb4c3aa71d7434b4efd2ebdc)
            check_type(argname="argument provisioned_product_id", value=provisioned_product_id, expected_type=type_hints["provisioned_product_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "provisioned_product_id": provisioned_product_id,
        }

    @builtins.property
    def provisioned_product_id(self) -> builtins.str:
        '''The ProvisionedProductId of the CloudFormationProvisionedProduct resource.'''
        result = self._values.get("provisioned_product_id")
        assert result is not None, "Required property 'provisioned_product_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudFormationProvisionedProductReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.IAcceptedPortfolioShareRef"
)
class IAcceptedPortfolioShareRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AcceptedPortfolioShare.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="acceptedPortfolioShareRef")
    def accepted_portfolio_share_ref(self) -> "AcceptedPortfolioShareReference":
        '''(experimental) A reference to a AcceptedPortfolioShare resource.

        :stability: experimental
        '''
        ...


class _IAcceptedPortfolioShareRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AcceptedPortfolioShare.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.IAcceptedPortfolioShareRef"

    @builtins.property
    @jsii.member(jsii_name="acceptedPortfolioShareRef")
    def accepted_portfolio_share_ref(self) -> "AcceptedPortfolioShareReference":
        '''(experimental) A reference to a AcceptedPortfolioShare resource.

        :stability: experimental
        '''
        return typing.cast("AcceptedPortfolioShareReference", jsii.get(self, "acceptedPortfolioShareRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAcceptedPortfolioShareRef).__jsii_proxy_class__ = lambda : _IAcceptedPortfolioShareRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ICloudFormationProductRef"
)
class ICloudFormationProductRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CloudFormationProduct.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cloudFormationProductRef")
    def cloud_formation_product_ref(self) -> "CloudFormationProductReference":
        '''(experimental) A reference to a CloudFormationProduct resource.

        :stability: experimental
        '''
        ...


class _ICloudFormationProductRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CloudFormationProduct.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.ICloudFormationProductRef"

    @builtins.property
    @jsii.member(jsii_name="cloudFormationProductRef")
    def cloud_formation_product_ref(self) -> "CloudFormationProductReference":
        '''(experimental) A reference to a CloudFormationProduct resource.

        :stability: experimental
        '''
        return typing.cast("CloudFormationProductReference", jsii.get(self, "cloudFormationProductRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICloudFormationProductRef).__jsii_proxy_class__ = lambda : _ICloudFormationProductRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ICloudFormationProvisionedProductRef"
)
class ICloudFormationProvisionedProductRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CloudFormationProvisionedProduct.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cloudFormationProvisionedProductRef")
    def cloud_formation_provisioned_product_ref(
        self,
    ) -> "CloudFormationProvisionedProductReference":
        '''(experimental) A reference to a CloudFormationProvisionedProduct resource.

        :stability: experimental
        '''
        ...


class _ICloudFormationProvisionedProductRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CloudFormationProvisionedProduct.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.ICloudFormationProvisionedProductRef"

    @builtins.property
    @jsii.member(jsii_name="cloudFormationProvisionedProductRef")
    def cloud_formation_provisioned_product_ref(
        self,
    ) -> "CloudFormationProvisionedProductReference":
        '''(experimental) A reference to a CloudFormationProvisionedProduct resource.

        :stability: experimental
        '''
        return typing.cast("CloudFormationProvisionedProductReference", jsii.get(self, "cloudFormationProvisionedProductRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICloudFormationProvisionedProductRef).__jsii_proxy_class__ = lambda : _ICloudFormationProvisionedProductRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ILaunchNotificationConstraintRef"
)
class ILaunchNotificationConstraintRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchNotificationConstraint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="launchNotificationConstraintRef")
    def launch_notification_constraint_ref(
        self,
    ) -> "LaunchNotificationConstraintReference":
        '''(experimental) A reference to a LaunchNotificationConstraint resource.

        :stability: experimental
        '''
        ...


class _ILaunchNotificationConstraintRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchNotificationConstraint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.ILaunchNotificationConstraintRef"

    @builtins.property
    @jsii.member(jsii_name="launchNotificationConstraintRef")
    def launch_notification_constraint_ref(
        self,
    ) -> "LaunchNotificationConstraintReference":
        '''(experimental) A reference to a LaunchNotificationConstraint resource.

        :stability: experimental
        '''
        return typing.cast("LaunchNotificationConstraintReference", jsii.get(self, "launchNotificationConstraintRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILaunchNotificationConstraintRef).__jsii_proxy_class__ = lambda : _ILaunchNotificationConstraintRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ILaunchRoleConstraintRef"
)
class ILaunchRoleConstraintRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchRoleConstraint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="launchRoleConstraintRef")
    def launch_role_constraint_ref(self) -> "LaunchRoleConstraintReference":
        '''(experimental) A reference to a LaunchRoleConstraint resource.

        :stability: experimental
        '''
        ...


class _ILaunchRoleConstraintRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchRoleConstraint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.ILaunchRoleConstraintRef"

    @builtins.property
    @jsii.member(jsii_name="launchRoleConstraintRef")
    def launch_role_constraint_ref(self) -> "LaunchRoleConstraintReference":
        '''(experimental) A reference to a LaunchRoleConstraint resource.

        :stability: experimental
        '''
        return typing.cast("LaunchRoleConstraintReference", jsii.get(self, "launchRoleConstraintRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILaunchRoleConstraintRef).__jsii_proxy_class__ = lambda : _ILaunchRoleConstraintRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ILaunchTemplateConstraintRef"
)
class ILaunchTemplateConstraintRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchTemplateConstraint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="launchTemplateConstraintRef")
    def launch_template_constraint_ref(self) -> "LaunchTemplateConstraintReference":
        '''(experimental) A reference to a LaunchTemplateConstraint resource.

        :stability: experimental
        '''
        ...


class _ILaunchTemplateConstraintRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchTemplateConstraint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.ILaunchTemplateConstraintRef"

    @builtins.property
    @jsii.member(jsii_name="launchTemplateConstraintRef")
    def launch_template_constraint_ref(self) -> "LaunchTemplateConstraintReference":
        '''(experimental) A reference to a LaunchTemplateConstraint resource.

        :stability: experimental
        '''
        return typing.cast("LaunchTemplateConstraintReference", jsii.get(self, "launchTemplateConstraintRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILaunchTemplateConstraintRef).__jsii_proxy_class__ = lambda : _ILaunchTemplateConstraintRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.IPortfolioPrincipalAssociationRef"
)
class IPortfolioPrincipalAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PortfolioPrincipalAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="portfolioPrincipalAssociationRef")
    def portfolio_principal_association_ref(
        self,
    ) -> "PortfolioPrincipalAssociationReference":
        '''(experimental) A reference to a PortfolioPrincipalAssociation resource.

        :stability: experimental
        '''
        ...


class _IPortfolioPrincipalAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PortfolioPrincipalAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.IPortfolioPrincipalAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="portfolioPrincipalAssociationRef")
    def portfolio_principal_association_ref(
        self,
    ) -> "PortfolioPrincipalAssociationReference":
        '''(experimental) A reference to a PortfolioPrincipalAssociation resource.

        :stability: experimental
        '''
        return typing.cast("PortfolioPrincipalAssociationReference", jsii.get(self, "portfolioPrincipalAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPortfolioPrincipalAssociationRef).__jsii_proxy_class__ = lambda : _IPortfolioPrincipalAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.IPortfolioProductAssociationRef"
)
class IPortfolioProductAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PortfolioProductAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="portfolioProductAssociationRef")
    def portfolio_product_association_ref(
        self,
    ) -> "PortfolioProductAssociationReference":
        '''(experimental) A reference to a PortfolioProductAssociation resource.

        :stability: experimental
        '''
        ...


class _IPortfolioProductAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PortfolioProductAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.IPortfolioProductAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="portfolioProductAssociationRef")
    def portfolio_product_association_ref(
        self,
    ) -> "PortfolioProductAssociationReference":
        '''(experimental) A reference to a PortfolioProductAssociation resource.

        :stability: experimental
        '''
        return typing.cast("PortfolioProductAssociationReference", jsii.get(self, "portfolioProductAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPortfolioProductAssociationRef).__jsii_proxy_class__ = lambda : _IPortfolioProductAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.IPortfolioRef")
class IPortfolioRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Portfolio.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="portfolioRef")
    def portfolio_ref(self) -> "PortfolioReference":
        '''(experimental) A reference to a Portfolio resource.

        :stability: experimental
        '''
        ...


class _IPortfolioRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Portfolio.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.IPortfolioRef"

    @builtins.property
    @jsii.member(jsii_name="portfolioRef")
    def portfolio_ref(self) -> "PortfolioReference":
        '''(experimental) A reference to a Portfolio resource.

        :stability: experimental
        '''
        return typing.cast("PortfolioReference", jsii.get(self, "portfolioRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPortfolioRef).__jsii_proxy_class__ = lambda : _IPortfolioRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.IPortfolioShareRef"
)
class IPortfolioShareRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PortfolioShare.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="portfolioShareRef")
    def portfolio_share_ref(self) -> "PortfolioShareReference":
        '''(experimental) A reference to a PortfolioShare resource.

        :stability: experimental
        '''
        ...


class _IPortfolioShareRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PortfolioShare.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.IPortfolioShareRef"

    @builtins.property
    @jsii.member(jsii_name="portfolioShareRef")
    def portfolio_share_ref(self) -> "PortfolioShareReference":
        '''(experimental) A reference to a PortfolioShare resource.

        :stability: experimental
        '''
        return typing.cast("PortfolioShareReference", jsii.get(self, "portfolioShareRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPortfolioShareRef).__jsii_proxy_class__ = lambda : _IPortfolioShareRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.IResourceUpdateConstraintRef"
)
class IResourceUpdateConstraintRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceUpdateConstraint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceUpdateConstraintRef")
    def resource_update_constraint_ref(self) -> "ResourceUpdateConstraintReference":
        '''(experimental) A reference to a ResourceUpdateConstraint resource.

        :stability: experimental
        '''
        ...


class _IResourceUpdateConstraintRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceUpdateConstraint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.IResourceUpdateConstraintRef"

    @builtins.property
    @jsii.member(jsii_name="resourceUpdateConstraintRef")
    def resource_update_constraint_ref(self) -> "ResourceUpdateConstraintReference":
        '''(experimental) A reference to a ResourceUpdateConstraint resource.

        :stability: experimental
        '''
        return typing.cast("ResourceUpdateConstraintReference", jsii.get(self, "resourceUpdateConstraintRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceUpdateConstraintRef).__jsii_proxy_class__ = lambda : _IResourceUpdateConstraintRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.IServiceActionAssociationRef"
)
class IServiceActionAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceActionAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceActionAssociationRef")
    def service_action_association_ref(self) -> "ServiceActionAssociationReference":
        '''(experimental) A reference to a ServiceActionAssociation resource.

        :stability: experimental
        '''
        ...


class _IServiceActionAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceActionAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.IServiceActionAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="serviceActionAssociationRef")
    def service_action_association_ref(self) -> "ServiceActionAssociationReference":
        '''(experimental) A reference to a ServiceActionAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ServiceActionAssociationReference", jsii.get(self, "serviceActionAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceActionAssociationRef).__jsii_proxy_class__ = lambda : _IServiceActionAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.IServiceActionRef"
)
class IServiceActionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceAction.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceActionRef")
    def service_action_ref(self) -> "ServiceActionReference":
        '''(experimental) A reference to a ServiceAction resource.

        :stability: experimental
        '''
        ...


class _IServiceActionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceAction.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.IServiceActionRef"

    @builtins.property
    @jsii.member(jsii_name="serviceActionRef")
    def service_action_ref(self) -> "ServiceActionReference":
        '''(experimental) A reference to a ServiceAction resource.

        :stability: experimental
        '''
        return typing.cast("ServiceActionReference", jsii.get(self, "serviceActionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceActionRef).__jsii_proxy_class__ = lambda : _IServiceActionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.IStackSetConstraintRef"
)
class IStackSetConstraintRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StackSetConstraint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stackSetConstraintRef")
    def stack_set_constraint_ref(self) -> "StackSetConstraintReference":
        '''(experimental) A reference to a StackSetConstraint resource.

        :stability: experimental
        '''
        ...


class _IStackSetConstraintRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StackSetConstraint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.IStackSetConstraintRef"

    @builtins.property
    @jsii.member(jsii_name="stackSetConstraintRef")
    def stack_set_constraint_ref(self) -> "StackSetConstraintReference":
        '''(experimental) A reference to a StackSetConstraint resource.

        :stability: experimental
        '''
        return typing.cast("StackSetConstraintReference", jsii.get(self, "stackSetConstraintRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackSetConstraintRef).__jsii_proxy_class__ = lambda : _IStackSetConstraintRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ITagOptionAssociationRef"
)
class ITagOptionAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TagOptionAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tagOptionAssociationRef")
    def tag_option_association_ref(self) -> "TagOptionAssociationReference":
        '''(experimental) A reference to a TagOptionAssociation resource.

        :stability: experimental
        '''
        ...


class _ITagOptionAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TagOptionAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.ITagOptionAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="tagOptionAssociationRef")
    def tag_option_association_ref(self) -> "TagOptionAssociationReference":
        '''(experimental) A reference to a TagOptionAssociation resource.

        :stability: experimental
        '''
        return typing.cast("TagOptionAssociationReference", jsii.get(self, "tagOptionAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITagOptionAssociationRef).__jsii_proxy_class__ = lambda : _ITagOptionAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ITagOptionRef")
class ITagOptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TagOption.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tagOptionRef")
    def tag_option_ref(self) -> "TagOptionReference":
        '''(experimental) A reference to a TagOption resource.

        :stability: experimental
        '''
        ...


class _ITagOptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TagOption.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_servicecatalog.ITagOptionRef"

    @builtins.property
    @jsii.member(jsii_name="tagOptionRef")
    def tag_option_ref(self) -> "TagOptionReference":
        '''(experimental) A reference to a TagOption resource.

        :stability: experimental
        '''
        return typing.cast("TagOptionReference", jsii.get(self, "tagOptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITagOptionRef).__jsii_proxy_class__ = lambda : _ITagOptionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.LaunchNotificationConstraintReference",
    jsii_struct_bases=[],
    name_mapping={
        "launch_notification_constraint_id": "launchNotificationConstraintId",
    },
)
class LaunchNotificationConstraintReference:
    def __init__(self, *, launch_notification_constraint_id: builtins.str) -> None:
        '''A reference to a LaunchNotificationConstraint resource.

        :param launch_notification_constraint_id: The Id of the LaunchNotificationConstraint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            launch_notification_constraint_reference = interfaces_servicecatalog.LaunchNotificationConstraintReference(
                launch_notification_constraint_id="launchNotificationConstraintId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d23d73f6bfcf8369dd83ca8779e9cebde80cf4d1b701bbe1a19f27df378d2919)
            check_type(argname="argument launch_notification_constraint_id", value=launch_notification_constraint_id, expected_type=type_hints["launch_notification_constraint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_notification_constraint_id": launch_notification_constraint_id,
        }

    @builtins.property
    def launch_notification_constraint_id(self) -> builtins.str:
        '''The Id of the LaunchNotificationConstraint resource.'''
        result = self._values.get("launch_notification_constraint_id")
        assert result is not None, "Required property 'launch_notification_constraint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchNotificationConstraintReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.LaunchRoleConstraintReference",
    jsii_struct_bases=[],
    name_mapping={"launch_role_constraint_id": "launchRoleConstraintId"},
)
class LaunchRoleConstraintReference:
    def __init__(self, *, launch_role_constraint_id: builtins.str) -> None:
        '''A reference to a LaunchRoleConstraint resource.

        :param launch_role_constraint_id: The Id of the LaunchRoleConstraint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            launch_role_constraint_reference = interfaces_servicecatalog.LaunchRoleConstraintReference(
                launch_role_constraint_id="launchRoleConstraintId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c2c57a260f4b58d42cf5470f1bad68aca6463764ced7236f80e5e204fe9b261)
            check_type(argname="argument launch_role_constraint_id", value=launch_role_constraint_id, expected_type=type_hints["launch_role_constraint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_role_constraint_id": launch_role_constraint_id,
        }

    @builtins.property
    def launch_role_constraint_id(self) -> builtins.str:
        '''The Id of the LaunchRoleConstraint resource.'''
        result = self._values.get("launch_role_constraint_id")
        assert result is not None, "Required property 'launch_role_constraint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchRoleConstraintReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.LaunchTemplateConstraintReference",
    jsii_struct_bases=[],
    name_mapping={"launch_template_constraint_id": "launchTemplateConstraintId"},
)
class LaunchTemplateConstraintReference:
    def __init__(self, *, launch_template_constraint_id: builtins.str) -> None:
        '''A reference to a LaunchTemplateConstraint resource.

        :param launch_template_constraint_id: The Id of the LaunchTemplateConstraint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            launch_template_constraint_reference = interfaces_servicecatalog.LaunchTemplateConstraintReference(
                launch_template_constraint_id="launchTemplateConstraintId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1397b1bb181bb13d3d4aaa76f85fb268a9d24ee93f9173cdc449f320d8b0fc40)
            check_type(argname="argument launch_template_constraint_id", value=launch_template_constraint_id, expected_type=type_hints["launch_template_constraint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_template_constraint_id": launch_template_constraint_id,
        }

    @builtins.property
    def launch_template_constraint_id(self) -> builtins.str:
        '''The Id of the LaunchTemplateConstraint resource.'''
        result = self._values.get("launch_template_constraint_id")
        assert result is not None, "Required property 'launch_template_constraint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchTemplateConstraintReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.PortfolioPrincipalAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"portfolio_id": "portfolioId", "principal_arn": "principalArn"},
)
class PortfolioPrincipalAssociationReference:
    def __init__(
        self,
        *,
        portfolio_id: builtins.str,
        principal_arn: builtins.str,
    ) -> None:
        '''A reference to a PortfolioPrincipalAssociation resource.

        :param portfolio_id: The PortfolioId of the PortfolioPrincipalAssociation resource.
        :param principal_arn: The PrincipalARN of the PortfolioPrincipalAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            portfolio_principal_association_reference = interfaces_servicecatalog.PortfolioPrincipalAssociationReference(
                portfolio_id="portfolioId",
                principal_arn="principalArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6329e48ce6818b8186ead3569a441ee7acab931e0635be0e1b27be1604987726)
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument principal_arn", value=principal_arn, expected_type=type_hints["principal_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "principal_arn": principal_arn,
        }

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The PortfolioId of the PortfolioPrincipalAssociation resource.'''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal_arn(self) -> builtins.str:
        '''The PrincipalARN of the PortfolioPrincipalAssociation resource.'''
        result = self._values.get("principal_arn")
        assert result is not None, "Required property 'principal_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortfolioPrincipalAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.PortfolioProductAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"portfolio_id": "portfolioId", "product_id": "productId"},
)
class PortfolioProductAssociationReference:
    def __init__(self, *, portfolio_id: builtins.str, product_id: builtins.str) -> None:
        '''A reference to a PortfolioProductAssociation resource.

        :param portfolio_id: The PortfolioId of the PortfolioProductAssociation resource.
        :param product_id: The ProductId of the PortfolioProductAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            portfolio_product_association_reference = interfaces_servicecatalog.PortfolioProductAssociationReference(
                portfolio_id="portfolioId",
                product_id="productId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a73688126d00eb08b21f732051540f4b33a20693c610ec4510cecdf691da400c)
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "portfolio_id": portfolio_id,
            "product_id": product_id,
        }

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The PortfolioId of the PortfolioProductAssociation resource.'''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The ProductId of the PortfolioProductAssociation resource.'''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortfolioProductAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.PortfolioReference",
    jsii_struct_bases=[],
    name_mapping={"portfolio_id": "portfolioId"},
)
class PortfolioReference:
    def __init__(self, *, portfolio_id: builtins.str) -> None:
        '''A reference to a Portfolio resource.

        :param portfolio_id: The Id of the Portfolio resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            portfolio_reference = interfaces_servicecatalog.PortfolioReference(
                portfolio_id="portfolioId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e2a1a05c6f45cbcc6e26bc8e9ba31df37e50441bd062936d3f6d9f121dfba97)
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "portfolio_id": portfolio_id,
        }

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The Id of the Portfolio resource.'''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortfolioReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.PortfolioShareReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId", "portfolio_id": "portfolioId"},
)
class PortfolioShareReference:
    def __init__(self, *, account_id: builtins.str, portfolio_id: builtins.str) -> None:
        '''A reference to a PortfolioShare resource.

        :param account_id: The AccountId of the PortfolioShare resource.
        :param portfolio_id: The PortfolioId of the PortfolioShare resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            portfolio_share_reference = interfaces_servicecatalog.PortfolioShareReference(
                account_id="accountId",
                portfolio_id="portfolioId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2c1792d5771696524059cc9a437c824b7a47315a76f5c196151ace03bb43b7c)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument portfolio_id", value=portfolio_id, expected_type=type_hints["portfolio_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "portfolio_id": portfolio_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the PortfolioShare resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def portfolio_id(self) -> builtins.str:
        '''The PortfolioId of the PortfolioShare resource.'''
        result = self._values.get("portfolio_id")
        assert result is not None, "Required property 'portfolio_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PortfolioShareReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ResourceUpdateConstraintReference",
    jsii_struct_bases=[],
    name_mapping={"resource_update_constraint_id": "resourceUpdateConstraintId"},
)
class ResourceUpdateConstraintReference:
    def __init__(self, *, resource_update_constraint_id: builtins.str) -> None:
        '''A reference to a ResourceUpdateConstraint resource.

        :param resource_update_constraint_id: The Id of the ResourceUpdateConstraint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            resource_update_constraint_reference = interfaces_servicecatalog.ResourceUpdateConstraintReference(
                resource_update_constraint_id="resourceUpdateConstraintId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be0eeeb2b4a37db981dfc6b0b6f1a522cc98ae2529b7d6c33cf31933696eeef7)
            check_type(argname="argument resource_update_constraint_id", value=resource_update_constraint_id, expected_type=type_hints["resource_update_constraint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_update_constraint_id": resource_update_constraint_id,
        }

    @builtins.property
    def resource_update_constraint_id(self) -> builtins.str:
        '''The Id of the ResourceUpdateConstraint resource.'''
        result = self._values.get("resource_update_constraint_id")
        assert result is not None, "Required property 'resource_update_constraint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceUpdateConstraintReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ServiceActionAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "product_id": "productId",
        "provisioning_artifact_id": "provisioningArtifactId",
        "service_action_id": "serviceActionId",
    },
)
class ServiceActionAssociationReference:
    def __init__(
        self,
        *,
        product_id: builtins.str,
        provisioning_artifact_id: builtins.str,
        service_action_id: builtins.str,
    ) -> None:
        '''A reference to a ServiceActionAssociation resource.

        :param product_id: The ProductId of the ServiceActionAssociation resource.
        :param provisioning_artifact_id: The ProvisioningArtifactId of the ServiceActionAssociation resource.
        :param service_action_id: The ServiceActionId of the ServiceActionAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            service_action_association_reference = interfaces_servicecatalog.ServiceActionAssociationReference(
                product_id="productId",
                provisioning_artifact_id="provisioningArtifactId",
                service_action_id="serviceActionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c7ff9aea497f318ecdfdd96d1694ada3828eefde0f3be173df54639473ceeda)
            check_type(argname="argument product_id", value=product_id, expected_type=type_hints["product_id"])
            check_type(argname="argument provisioning_artifact_id", value=provisioning_artifact_id, expected_type=type_hints["provisioning_artifact_id"])
            check_type(argname="argument service_action_id", value=service_action_id, expected_type=type_hints["service_action_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "product_id": product_id,
            "provisioning_artifact_id": provisioning_artifact_id,
            "service_action_id": service_action_id,
        }

    @builtins.property
    def product_id(self) -> builtins.str:
        '''The ProductId of the ServiceActionAssociation resource.'''
        result = self._values.get("product_id")
        assert result is not None, "Required property 'product_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def provisioning_artifact_id(self) -> builtins.str:
        '''The ProvisioningArtifactId of the ServiceActionAssociation resource.'''
        result = self._values.get("provisioning_artifact_id")
        assert result is not None, "Required property 'provisioning_artifact_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_action_id(self) -> builtins.str:
        '''The ServiceActionId of the ServiceActionAssociation resource.'''
        result = self._values.get("service_action_id")
        assert result is not None, "Required property 'service_action_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceActionAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.ServiceActionReference",
    jsii_struct_bases=[],
    name_mapping={"service_action_id": "serviceActionId"},
)
class ServiceActionReference:
    def __init__(self, *, service_action_id: builtins.str) -> None:
        '''A reference to a ServiceAction resource.

        :param service_action_id: The Id of the ServiceAction resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            service_action_reference = interfaces_servicecatalog.ServiceActionReference(
                service_action_id="serviceActionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fa108cd4bbb228b6de17863a92fe1a38df9682a71cfbcb03f1c9f565bddd10f)
            check_type(argname="argument service_action_id", value=service_action_id, expected_type=type_hints["service_action_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_action_id": service_action_id,
        }

    @builtins.property
    def service_action_id(self) -> builtins.str:
        '''The Id of the ServiceAction resource.'''
        result = self._values.get("service_action_id")
        assert result is not None, "Required property 'service_action_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceActionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.StackSetConstraintReference",
    jsii_struct_bases=[],
    name_mapping={"stack_set_constraint_id": "stackSetConstraintId"},
)
class StackSetConstraintReference:
    def __init__(self, *, stack_set_constraint_id: builtins.str) -> None:
        '''A reference to a StackSetConstraint resource.

        :param stack_set_constraint_id: The Id of the StackSetConstraint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            stack_set_constraint_reference = interfaces_servicecatalog.StackSetConstraintReference(
                stack_set_constraint_id="stackSetConstraintId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20539a60ac78bce6dc8f9f7b2cfbd96ee6732b5b4b6cc9f9720d710656231b14)
            check_type(argname="argument stack_set_constraint_id", value=stack_set_constraint_id, expected_type=type_hints["stack_set_constraint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stack_set_constraint_id": stack_set_constraint_id,
        }

    @builtins.property
    def stack_set_constraint_id(self) -> builtins.str:
        '''The Id of the StackSetConstraint resource.'''
        result = self._values.get("stack_set_constraint_id")
        assert result is not None, "Required property 'stack_set_constraint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackSetConstraintReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.TagOptionAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"resource_id": "resourceId", "tag_option_id": "tagOptionId"},
)
class TagOptionAssociationReference:
    def __init__(
        self,
        *,
        resource_id: builtins.str,
        tag_option_id: builtins.str,
    ) -> None:
        '''A reference to a TagOptionAssociation resource.

        :param resource_id: The ResourceId of the TagOptionAssociation resource.
        :param tag_option_id: The TagOptionId of the TagOptionAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            tag_option_association_reference = interfaces_servicecatalog.TagOptionAssociationReference(
                resource_id="resourceId",
                tag_option_id="tagOptionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce84a4c975f0b55dc777c14f90bce899e703adebfbfe13c4a9c19b71819877df)
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument tag_option_id", value=tag_option_id, expected_type=type_hints["tag_option_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_id": resource_id,
            "tag_option_id": tag_option_id,
        }

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The ResourceId of the TagOptionAssociation resource.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tag_option_id(self) -> builtins.str:
        '''The TagOptionId of the TagOptionAssociation resource.'''
        result = self._values.get("tag_option_id")
        assert result is not None, "Required property 'tag_option_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagOptionAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_servicecatalog.TagOptionReference",
    jsii_struct_bases=[],
    name_mapping={"tag_option_id": "tagOptionId"},
)
class TagOptionReference:
    def __init__(self, *, tag_option_id: builtins.str) -> None:
        '''A reference to a TagOption resource.

        :param tag_option_id: The Id of the TagOption resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_servicecatalog as interfaces_servicecatalog
            
            tag_option_reference = interfaces_servicecatalog.TagOptionReference(
                tag_option_id="tagOptionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47d8abc47d9ddd060282a0a556fe7f0fe1923d2e898d128ad587f8b031ce749e)
            check_type(argname="argument tag_option_id", value=tag_option_id, expected_type=type_hints["tag_option_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tag_option_id": tag_option_id,
        }

    @builtins.property
    def tag_option_id(self) -> builtins.str:
        '''The Id of the TagOption resource.'''
        result = self._values.get("tag_option_id")
        assert result is not None, "Required property 'tag_option_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagOptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AcceptedPortfolioShareReference",
    "CloudFormationProductReference",
    "CloudFormationProvisionedProductReference",
    "IAcceptedPortfolioShareRef",
    "ICloudFormationProductRef",
    "ICloudFormationProvisionedProductRef",
    "ILaunchNotificationConstraintRef",
    "ILaunchRoleConstraintRef",
    "ILaunchTemplateConstraintRef",
    "IPortfolioPrincipalAssociationRef",
    "IPortfolioProductAssociationRef",
    "IPortfolioRef",
    "IPortfolioShareRef",
    "IResourceUpdateConstraintRef",
    "IServiceActionAssociationRef",
    "IServiceActionRef",
    "IStackSetConstraintRef",
    "ITagOptionAssociationRef",
    "ITagOptionRef",
    "LaunchNotificationConstraintReference",
    "LaunchRoleConstraintReference",
    "LaunchTemplateConstraintReference",
    "PortfolioPrincipalAssociationReference",
    "PortfolioProductAssociationReference",
    "PortfolioReference",
    "PortfolioShareReference",
    "ResourceUpdateConstraintReference",
    "ServiceActionAssociationReference",
    "ServiceActionReference",
    "StackSetConstraintReference",
    "TagOptionAssociationReference",
    "TagOptionReference",
]

publication.publish()

def _typecheckingstub__b6326f3888119e6783b8c2f3210c345520ccc67dd5064e23514085258059f2c2(
    *,
    accepted_portfolio_share_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62967c3e411db25daf0417852c200a39e2e4dd0f789a69eec9bdab47433f04fc(
    *,
    cloud_formation_product_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b6367dc67edf9798c223a04eeb171c5fa2b7131fb4c3aa71d7434b4efd2ebdc(
    *,
    provisioned_product_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d23d73f6bfcf8369dd83ca8779e9cebde80cf4d1b701bbe1a19f27df378d2919(
    *,
    launch_notification_constraint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c2c57a260f4b58d42cf5470f1bad68aca6463764ced7236f80e5e204fe9b261(
    *,
    launch_role_constraint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1397b1bb181bb13d3d4aaa76f85fb268a9d24ee93f9173cdc449f320d8b0fc40(
    *,
    launch_template_constraint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6329e48ce6818b8186ead3569a441ee7acab931e0635be0e1b27be1604987726(
    *,
    portfolio_id: builtins.str,
    principal_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73688126d00eb08b21f732051540f4b33a20693c610ec4510cecdf691da400c(
    *,
    portfolio_id: builtins.str,
    product_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2a1a05c6f45cbcc6e26bc8e9ba31df37e50441bd062936d3f6d9f121dfba97(
    *,
    portfolio_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2c1792d5771696524059cc9a437c824b7a47315a76f5c196151ace03bb43b7c(
    *,
    account_id: builtins.str,
    portfolio_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be0eeeb2b4a37db981dfc6b0b6f1a522cc98ae2529b7d6c33cf31933696eeef7(
    *,
    resource_update_constraint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c7ff9aea497f318ecdfdd96d1694ada3828eefde0f3be173df54639473ceeda(
    *,
    product_id: builtins.str,
    provisioning_artifact_id: builtins.str,
    service_action_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa108cd4bbb228b6de17863a92fe1a38df9682a71cfbcb03f1c9f565bddd10f(
    *,
    service_action_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20539a60ac78bce6dc8f9f7b2cfbd96ee6732b5b4b6cc9f9720d710656231b14(
    *,
    stack_set_constraint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce84a4c975f0b55dc777c14f90bce899e703adebfbfe13c4a9c19b71819877df(
    *,
    resource_id: builtins.str,
    tag_option_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d8abc47d9ddd060282a0a556fe7f0fe1923d2e898d128ad587f8b031ce749e(
    *,
    tag_option_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAcceptedPortfolioShareRef, ICloudFormationProductRef, ICloudFormationProvisionedProductRef, ILaunchNotificationConstraintRef, ILaunchRoleConstraintRef, ILaunchTemplateConstraintRef, IPortfolioPrincipalAssociationRef, IPortfolioProductAssociationRef, IPortfolioRef, IPortfolioShareRef, IResourceUpdateConstraintRef, IServiceActionAssociationRef, IServiceActionRef, IStackSetConstraintRef, ITagOptionAssociationRef, ITagOptionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
