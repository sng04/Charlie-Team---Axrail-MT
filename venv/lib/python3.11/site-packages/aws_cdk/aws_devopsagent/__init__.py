r'''
# AWS::DevOpsAgent Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_devopsagent as devopsagent
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DevOpsAgent construct libraries](https://constructs.dev/search?q=devopsagent)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DevOpsAgent resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DevOpsAgent.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DevOpsAgent](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DevOpsAgent.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
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

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_devopsagent import (
    AgentSpaceReference as _AgentSpaceReference_4cf55ea9,
    AssociationReference as _AssociationReference_249ec236,
    IAgentSpaceRef as _IAgentSpaceRef_2ffb48ed,
    IAssociationRef as _IAssociationRef_ac0997e3,
    IServiceRef as _IServiceRef_a4cfa131,
    ServiceReference as _ServiceReference_cb07f28f,
)


@jsii.implements(_IInspectable_c2943556, _IAgentSpaceRef_2ffb48ed)
class CfnAgentSpace(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devopsagent.CfnAgentSpace",
):
    '''The ``AWS::DevOpsAgent::AgentSpace`` resource specifies an Agent Space for the AWS DevOps Agent Service.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-agentspace.html
    :cloudformationResource: AWS::DevOpsAgent::AgentSpace
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devopsagent as devopsagent
        
        cfn_agent_space = devopsagent.CfnAgentSpace(self, "MyCfnAgentSpace",
            name="name",
        
            # the properties below are optional
            description="description",
            operator_app=devopsagent.CfnAgentSpace.OperatorAppProperty(
                iam=devopsagent.CfnAgentSpace.IamAuthConfigurationProperty(
                    operator_app_role_arn="operatorAppRoleArn",
        
                    # the properties below are optional
                    created_at="createdAt",
                    updated_at="updatedAt"
                ),
                idc=devopsagent.CfnAgentSpace.IdcAuthConfigurationProperty(
                    idc_instance_arn="idcInstanceArn",
                    operator_app_role_arn="operatorAppRoleArn",
        
                    # the properties below are optional
                    created_at="createdAt",
                    idc_application_arn="idcApplicationArn",
                    updated_at="updatedAt"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        operator_app: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.OperatorAppProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DevOpsAgent::AgentSpace``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the Agent Space.
        :param description: The description of the Agent Space.
        :param operator_app: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3897cdc52c2bc2a74bdd32702e32905947b3c0fc36798edcdac7875cc9939456)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAgentSpaceProps(
            name=name, description=description, operator_app=operator_app
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAgentSpace")
    @builtins.classmethod
    def arn_for_agent_space(cls, resource: "_IAgentSpaceRef_2ffb48ed") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3fd19a72161f0ef8cc6732b6e9205e1c9f41b50d57a659a84461dcdde223423)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAgentSpace", [resource]))

    @jsii.member(jsii_name="fromAgentSpaceArn")
    @builtins.classmethod
    def from_agent_space_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IAgentSpaceRef_2ffb48ed":
        '''Creates a new IAgentSpaceRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dc004d63d73274933efa9e02989941984735e5426f7c063d97b0b415406d8d4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IAgentSpaceRef_2ffb48ed", jsii.sinvoke(cls, "fromAgentSpaceArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromAgentSpaceId")
    @builtins.classmethod
    def from_agent_space_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        agent_space_id: builtins.str,
    ) -> "_IAgentSpaceRef_2ffb48ed":
        '''Creates a new IAgentSpaceRef from a agentSpaceId.

        :param scope: -
        :param id: -
        :param agent_space_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c0f8fde84620afc53f90b3672d7f693a2e66909624772cab6d4c2337a64aa65)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
        return typing.cast("_IAgentSpaceRef_2ffb48ed", jsii.sinvoke(cls, "fromAgentSpaceId", [scope, id, agent_space_id]))

    @jsii.member(jsii_name="isCfnAgentSpace")
    @builtins.classmethod
    def is_cfn_agent_space(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAgentSpace.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62b6182298920242aa320928b58b0b5bc6ee7fe37ab398df5dd8f138f81638f6)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAgentSpace", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c3714a879ff931c53d9540f49cb04b7551032f6754505380b7064cbcb7719f)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aca7931f7e8a8dc031f895c3bf121e4253f0443d5d02865c48e259d41303518b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "_AgentSpaceReference_4cf55ea9":
        '''A reference to a AgentSpace resource.'''
        return typing.cast("_AgentSpaceReference_4cf55ea9", jsii.get(self, "agentSpaceRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentSpaceId")
    def attr_agent_space_id(self) -> builtins.str:
        '''The unique identifier of the Agent Space.

        :cloudformationAttribute: AgentSpaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentSpaceId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Agent Space.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the resource was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrOperatorAppIamCreatedAt")
    def attr_operator_app_iam_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: OperatorApp.Iam.CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOperatorAppIamCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrOperatorAppIamUpdatedAt")
    def attr_operator_app_iam_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: OperatorApp.Iam.UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOperatorAppIamUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrOperatorAppIdcCreatedAt")
    def attr_operator_app_idc_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: OperatorApp.Idc.CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOperatorAppIdcCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrOperatorAppIdcIdcApplicationArn")
    def attr_operator_app_idc_idc_application_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: OperatorApp.Idc.IdcApplicationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOperatorAppIdcIdcApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrOperatorAppIdcUpdatedAt")
    def attr_operator_app_idc_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: OperatorApp.Idc.UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOperatorAppIdcUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the resource was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Agent Space.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80e1593c483d80afbaaf07c646b5d5ede131e360f81f0dde9fa486f5c749e58f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the Agent Space.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b7561d8cdcaf93c81d1cf0a9a4cc5790c03232e494d49db5171a93599b8f575)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="operatorApp")
    def operator_app(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.OperatorAppProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.OperatorAppProperty"]], jsii.get(self, "operatorApp"))

    @operator_app.setter
    def operator_app(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.OperatorAppProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__833bedcb900be3dc99153bbcef5866a753457156d32ebc2661b687708cf7f6fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatorApp", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAgentSpace.IamAuthConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "operator_app_role_arn": "operatorAppRoleArn",
            "created_at": "createdAt",
            "updated_at": "updatedAt",
        },
    )
    class IamAuthConfigurationProperty:
        def __init__(
            self,
            *,
            operator_app_role_arn: builtins.str,
            created_at: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param operator_app_role_arn: 
            :param created_at: 
            :param updated_at: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-iamauthconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                iam_auth_configuration_property = devopsagent.CfnAgentSpace.IamAuthConfigurationProperty(
                    operator_app_role_arn="operatorAppRoleArn",
                
                    # the properties below are optional
                    created_at="createdAt",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4beb411197d70233cb23add12a5f3b652beb521a346992040d7d02b2b1ddd228)
                check_type(argname="argument operator_app_role_arn", value=operator_app_role_arn, expected_type=type_hints["operator_app_role_arn"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "operator_app_role_arn": operator_app_role_arn,
            }
            if created_at is not None:
                self._values["created_at"] = created_at
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def operator_app_role_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-iamauthconfiguration.html#cfn-devopsagent-agentspace-iamauthconfiguration-operatorapprolearn
            '''
            result = self._values.get("operator_app_role_arn")
            assert result is not None, "Required property 'operator_app_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-iamauthconfiguration.html#cfn-devopsagent-agentspace-iamauthconfiguration-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-iamauthconfiguration.html#cfn-devopsagent-agentspace-iamauthconfiguration-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamAuthConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAgentSpace.IdcAuthConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "idc_instance_arn": "idcInstanceArn",
            "operator_app_role_arn": "operatorAppRoleArn",
            "created_at": "createdAt",
            "idc_application_arn": "idcApplicationArn",
            "updated_at": "updatedAt",
        },
    )
    class IdcAuthConfigurationProperty:
        def __init__(
            self,
            *,
            idc_instance_arn: builtins.str,
            operator_app_role_arn: builtins.str,
            created_at: typing.Optional[builtins.str] = None,
            idc_application_arn: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param idc_instance_arn: 
            :param operator_app_role_arn: 
            :param created_at: 
            :param idc_application_arn: 
            :param updated_at: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-idcauthconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                idc_auth_configuration_property = devopsagent.CfnAgentSpace.IdcAuthConfigurationProperty(
                    idc_instance_arn="idcInstanceArn",
                    operator_app_role_arn="operatorAppRoleArn",
                
                    # the properties below are optional
                    created_at="createdAt",
                    idc_application_arn="idcApplicationArn",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__54cfce91472eb9681ce65a0ce7a6d266ecbcafccbd8e1842288a0f262a4d5755)
                check_type(argname="argument idc_instance_arn", value=idc_instance_arn, expected_type=type_hints["idc_instance_arn"])
                check_type(argname="argument operator_app_role_arn", value=operator_app_role_arn, expected_type=type_hints["operator_app_role_arn"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument idc_application_arn", value=idc_application_arn, expected_type=type_hints["idc_application_arn"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "idc_instance_arn": idc_instance_arn,
                "operator_app_role_arn": operator_app_role_arn,
            }
            if created_at is not None:
                self._values["created_at"] = created_at
            if idc_application_arn is not None:
                self._values["idc_application_arn"] = idc_application_arn
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def idc_instance_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-idcauthconfiguration.html#cfn-devopsagent-agentspace-idcauthconfiguration-idcinstancearn
            '''
            result = self._values.get("idc_instance_arn")
            assert result is not None, "Required property 'idc_instance_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def operator_app_role_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-idcauthconfiguration.html#cfn-devopsagent-agentspace-idcauthconfiguration-operatorapprolearn
            '''
            result = self._values.get("operator_app_role_arn")
            assert result is not None, "Required property 'operator_app_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-idcauthconfiguration.html#cfn-devopsagent-agentspace-idcauthconfiguration-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def idc_application_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-idcauthconfiguration.html#cfn-devopsagent-agentspace-idcauthconfiguration-idcapplicationarn
            '''
            result = self._values.get("idc_application_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-idcauthconfiguration.html#cfn-devopsagent-agentspace-idcauthconfiguration-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdcAuthConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAgentSpace.OperatorAppProperty",
        jsii_struct_bases=[],
        name_mapping={"iam": "iam", "idc": "idc"},
    )
    class OperatorAppProperty:
        def __init__(
            self,
            *,
            iam: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.IamAuthConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            idc: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.IdcAuthConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param iam: 
            :param idc: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-operatorapp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                operator_app_property = devopsagent.CfnAgentSpace.OperatorAppProperty(
                    iam=devopsagent.CfnAgentSpace.IamAuthConfigurationProperty(
                        operator_app_role_arn="operatorAppRoleArn",
                
                        # the properties below are optional
                        created_at="createdAt",
                        updated_at="updatedAt"
                    ),
                    idc=devopsagent.CfnAgentSpace.IdcAuthConfigurationProperty(
                        idc_instance_arn="idcInstanceArn",
                        operator_app_role_arn="operatorAppRoleArn",
                
                        # the properties below are optional
                        created_at="createdAt",
                        idc_application_arn="idcApplicationArn",
                        updated_at="updatedAt"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__163f48e2381f16154d3ed1a507d7fa1b64898c9ada42152eb65e4a5a869c805c)
                check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
                check_type(argname="argument idc", value=idc, expected_type=type_hints["idc"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam is not None:
                self._values["iam"] = iam
            if idc is not None:
                self._values["idc"] = idc

        @builtins.property
        def iam(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.IamAuthConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-operatorapp.html#cfn-devopsagent-agentspace-operatorapp-iam
            '''
            result = self._values.get("iam")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.IamAuthConfigurationProperty"]], result)

        @builtins.property
        def idc(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.IdcAuthConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-agentspace-operatorapp.html#cfn-devopsagent-agentspace-operatorapp-idc
            '''
            result = self._values.get("idc")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.IdcAuthConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OperatorAppProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devopsagent.CfnAgentSpaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "operator_app": "operatorApp",
    },
)
class CfnAgentSpaceProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        operator_app: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAgentSpace.OperatorAppProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAgentSpace``.

        :param name: The name of the Agent Space.
        :param description: The description of the Agent Space.
        :param operator_app: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-agentspace.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devopsagent as devopsagent
            
            cfn_agent_space_props = devopsagent.CfnAgentSpaceProps(
                name="name",
            
                # the properties below are optional
                description="description",
                operator_app=devopsagent.CfnAgentSpace.OperatorAppProperty(
                    iam=devopsagent.CfnAgentSpace.IamAuthConfigurationProperty(
                        operator_app_role_arn="operatorAppRoleArn",
            
                        # the properties below are optional
                        created_at="createdAt",
                        updated_at="updatedAt"
                    ),
                    idc=devopsagent.CfnAgentSpace.IdcAuthConfigurationProperty(
                        idc_instance_arn="idcInstanceArn",
                        operator_app_role_arn="operatorAppRoleArn",
            
                        # the properties below are optional
                        created_at="createdAt",
                        idc_application_arn="idcApplicationArn",
                        updated_at="updatedAt"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea00a21cf40eafce14a4e6e1a4cd3e9f843a2f2e416299a20a2159ce8cdb6d5f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument operator_app", value=operator_app, expected_type=type_hints["operator_app"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if operator_app is not None:
            self._values["operator_app"] = operator_app

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Agent Space.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-agentspace.html#cfn-devopsagent-agentspace-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the Agent Space.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-agentspace.html#cfn-devopsagent-agentspace-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator_app(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.OperatorAppProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-agentspace.html#cfn-devopsagent-agentspace-operatorapp
        '''
        result = self._values.get("operator_app")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAgentSpace.OperatorAppProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAgentSpaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IAssociationRef_ac0997e3)
class CfnAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation",
):
    '''The ``AWS::DevOpsAgent::Association`` resource specifies an association between an Agent Space and a service, defining how the Agent Space interacts with external services like GitHub, Slack, AWS accounts, and others.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-association.html
    :cloudformationResource: AWS::DevOpsAgent::Association
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devopsagent as devopsagent
        
        # resource_metadata: Any
        
        cfn_association = devopsagent.CfnAssociation(self, "MyCfnAssociation",
            agent_space_id="agentSpaceId",
            configuration=devopsagent.CfnAssociation.ServiceConfigurationProperty(
                aws=devopsagent.CfnAssociation.AWSConfigurationProperty(
                    account_id="accountId",
                    account_type="accountType",
                    assumable_role_arn="assumableRoleArn",
        
                    # the properties below are optional
                    resources=[devopsagent.CfnAssociation.AWSResourceProperty(
                        resource_arn="resourceArn",
        
                        # the properties below are optional
                        resource_metadata=resource_metadata,
                        resource_type="resourceType"
                    )],
                    tags=[devopsagent.CfnAssociation.KeyValuePairProperty(
                        key="key",
                        value="value"
                    )]
                ),
                dynatrace=devopsagent.CfnAssociation.DynatraceConfigurationProperty(
                    env_id="envId",
        
                    # the properties below are optional
                    enable_webhook_updates=False,
                    resources=["resources"]
                ),
                event_channel=devopsagent.CfnAssociation.EventChannelConfigurationProperty(
                    enable_webhook_updates=False
                ),
                git_hub=devopsagent.CfnAssociation.GitHubConfigurationProperty(
                    owner="owner",
                    owner_type="ownerType",
                    repo_id="repoId",
                    repo_name="repoName"
                ),
                git_lab=devopsagent.CfnAssociation.GitLabConfigurationProperty(
                    project_id="projectId",
                    project_path="projectPath",
        
                    # the properties below are optional
                    enable_webhook_updates=False,
                    instance_identifier="instanceIdentifier"
                ),
                mcp_server=devopsagent.CfnAssociation.MCPServerConfigurationProperty(
                    endpoint="endpoint",
                    name="name",
                    tools=["tools"],
        
                    # the properties below are optional
                    description="description",
                    enable_webhook_updates=False
                ),
                mcp_server_datadog=devopsagent.CfnAssociation.MCPServerDatadogConfigurationProperty(
                    endpoint="endpoint",
                    name="name",
        
                    # the properties below are optional
                    description="description",
                    enable_webhook_updates=False
                ),
                mcp_server_new_relic=devopsagent.CfnAssociation.MCPServerNewRelicConfigurationProperty(
                    account_id="accountId",
                    endpoint="endpoint"
                ),
                mcp_server_splunk=devopsagent.CfnAssociation.MCPServerSplunkConfigurationProperty(
                    endpoint="endpoint",
                    name="name",
        
                    # the properties below are optional
                    description="description",
                    enable_webhook_updates=False
                ),
                service_now=devopsagent.CfnAssociation.ServiceNowConfigurationProperty(
                    enable_webhook_updates=False,
                    instance_id="instanceId"
                ),
                slack=devopsagent.CfnAssociation.SlackConfigurationProperty(
                    transmission_target=devopsagent.CfnAssociation.SlackTransmissionTargetProperty(
                        incident_response_target=devopsagent.CfnAssociation.SlackChannelProperty(
                            channel_id="channelId",
        
                            # the properties below are optional
                            channel_name="channelName"
                        )
                    ),
                    workspace_id="workspaceId",
                    workspace_name="workspaceName"
                ),
                source_aws=devopsagent.CfnAssociation.SourceAwsConfigurationProperty(
                    account_id="accountId",
                    account_type="accountType",
                    assumable_role_arn="assumableRoleArn",
        
                    # the properties below are optional
                    resources=[devopsagent.CfnAssociation.AWSResourceProperty(
                        resource_arn="resourceArn",
        
                        # the properties below are optional
                        resource_metadata=resource_metadata,
                        resource_type="resourceType"
                    )],
                    tags=[devopsagent.CfnAssociation.KeyValuePairProperty(
                        key="key",
                        value="value"
                    )]
                )
            ),
            service_id="serviceId",
        
            # the properties below are optional
            linked_association_ids=["linkedAssociationIds"]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        agent_space_id: builtins.str,
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.ServiceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        service_id: builtins.str,
        linked_association_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::DevOpsAgent::Association``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_space_id: The unique identifier of the Agent Space.
        :param configuration: The configuration that directs how the Agent Space interacts with the given service. You can specify only one configuration type per association. *Allowed Values* : ``SourceAws`` | ``Aws`` | ``GitHub`` | ``GitLab`` | ``Slack`` | ``Dynatrace`` | ``ServiceNow`` | ``MCPServer`` | ``MCPServerNewRelic`` | ``MCPServerDatadog`` | ``MCPServerSplunk`` | ``EventChannel``
        :param service_id: The identifier for the associated service. For ``SourceAws`` and ``Aws`` configurations, this must be ``aws`` . For all other service types, this is a UUID generated from the RegisterService command.
        :param linked_association_ids: Set of linked association IDs for parent-child relationships.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9507e77277cf05febf82ccf8829d008e3d5bca6bfbb5c229a629346a34d445ff)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAssociationProps(
            agent_space_id=agent_space_id,
            configuration=configuration,
            service_id=service_id,
            linked_association_ids=linked_association_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnAssociation")
    @builtins.classmethod
    def is_cfn_association(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAssociation.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89cae44481f5807f4bcf3fcf5d08b660423111da523b22ba60bcaacf43a50aa9)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAssociation", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd21b036854f8ed65af7b88356ee2787b8f2fb60324e8b7f39b6edf4992ce967)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea0d4a7651eb08ad3bc11db7886a5718c26e72c5b665acd6183227b87adf00e4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="associationRef")
    def association_ref(self) -> "_AssociationReference_249ec236":
        '''A reference to a Association resource.'''
        return typing.cast("_AssociationReference_249ec236", jsii.get(self, "associationRef"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationId")
    def attr_association_id(self) -> builtins.str:
        '''The unique identifier of the association.

        :cloudformationAttribute: AssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the association was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the association was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="agentSpaceId")
    def agent_space_id(self) -> builtins.str:
        '''The unique identifier of the Agent Space.'''
        return typing.cast(builtins.str, jsii.get(self, "agentSpaceId"))

    @agent_space_id.setter
    def agent_space_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aac4f12f5965b47ff3162eacbbbebb04e5d1595483e00e0e29ace1cd733b8156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentSpaceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnAssociation.ServiceConfigurationProperty"]:
        '''The configuration that directs how the Agent Space interacts with the given service.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAssociation.ServiceConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnAssociation.ServiceConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b224d34e655755660b3f83f1ef3ad78de31336ef41e61cf24dfb47a3d5e00b96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serviceId")
    def service_id(self) -> builtins.str:
        '''The identifier for the associated service.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceId"))

    @service_id.setter
    def service_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08d88d472b1933bfd27859b1b634111a6667c50bedacee3234cfc98a8a05797a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="linkedAssociationIds")
    def linked_association_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of linked association IDs for parent-child relationships.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "linkedAssociationIds"))

    @linked_association_ids.setter
    def linked_association_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a926a8cb577bf81233b764232f042b444bc6a9e989283355f36b9faf248fe46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedAssociationIds", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.AWSConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "account_type": "accountType",
            "assumable_role_arn": "assumableRoleArn",
            "resources": "resources",
            "tags": "tags",
        },
    )
    class AWSConfigurationProperty:
        def __init__(
            self,
            *,
            account_id: builtins.str,
            account_type: builtins.str,
            assumable_role_arn: builtins.str,
            resources: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.AWSResourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tags: typing.Optional[typing.Sequence[typing.Union["CfnAssociation.KeyValuePairProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration for AWS monitor account integration.

            Specifies the account ID, assumable role ARN, and resources to be monitored in the primary monitoring account.

            :param account_id: Account ID corresponding to the provided resources.
            :param account_type: Account Type 'monitor' for AWS DevOps Agent monitoring.
            :param assumable_role_arn: Role ARN used by AWS DevOps Agent to access resources in the primary account.
            :param resources: List of resources to monitor.
            :param tags: List of tags as key-value pairs, used to identify resources for topology crawl.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # resource_metadata: Any
                
                a_wSConfiguration_property = devopsagent.CfnAssociation.AWSConfigurationProperty(
                    account_id="accountId",
                    account_type="accountType",
                    assumable_role_arn="assumableRoleArn",
                
                    # the properties below are optional
                    resources=[devopsagent.CfnAssociation.AWSResourceProperty(
                        resource_arn="resourceArn",
                
                        # the properties below are optional
                        resource_metadata=resource_metadata,
                        resource_type="resourceType"
                    )],
                    tags=[devopsagent.CfnAssociation.KeyValuePairProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9f1d632ade69849147b75fe20e7412c90e54c9e84dafe76046f35e5fa880436f)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument account_type", value=account_type, expected_type=type_hints["account_type"])
                check_type(argname="argument assumable_role_arn", value=assumable_role_arn, expected_type=type_hints["assumable_role_arn"])
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_id": account_id,
                "account_type": account_type,
                "assumable_role_arn": assumable_role_arn,
            }
            if resources is not None:
                self._values["resources"] = resources
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def account_id(self) -> builtins.str:
            '''Account ID corresponding to the provided resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsconfiguration.html#cfn-devopsagent-association-awsconfiguration-accountid
            '''
            result = self._values.get("account_id")
            assert result is not None, "Required property 'account_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account_type(self) -> builtins.str:
            '''Account Type 'monitor' for AWS DevOps Agent monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsconfiguration.html#cfn-devopsagent-association-awsconfiguration-accounttype
            '''
            result = self._values.get("account_type")
            assert result is not None, "Required property 'account_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def assumable_role_arn(self) -> builtins.str:
            '''Role ARN used by AWS DevOps Agent to access resources in the primary account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsconfiguration.html#cfn-devopsagent-association-awsconfiguration-assumablerolearn
            '''
            result = self._values.get("assumable_role_arn")
            assert result is not None, "Required property 'assumable_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resources(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAssociation.AWSResourceProperty"]]]]:
            '''List of resources to monitor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsconfiguration.html#cfn-devopsagent-association-awsconfiguration-resources
            '''
            result = self._values.get("resources")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAssociation.AWSResourceProperty"]]]], result)

        @builtins.property
        def tags(
            self,
        ) -> typing.Optional[typing.List["CfnAssociation.KeyValuePairProperty"]]:
            '''List of tags as key-value pairs, used to identify resources for topology crawl.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsconfiguration.html#cfn-devopsagent-association-awsconfiguration-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List["CfnAssociation.KeyValuePairProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AWSConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.AWSResourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_arn": "resourceArn",
            "resource_metadata": "resourceMetadata",
            "resource_type": "resourceType",
        },
    )
    class AWSResourceProperty:
        def __init__(
            self,
            *,
            resource_arn: builtins.str,
            resource_metadata: typing.Any = None,
            resource_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines an AWS resource to be monitored, including its type, ARN, and optional metadata.

            :param resource_arn: The Amazon Resource Name (ARN) of the resource.
            :param resource_metadata: Additional metadata specific to the resource. This is an optional JSON object that can include resource-specific information to provide additional context for monitoring and management.
            :param resource_type: Resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsresource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # resource_metadata: Any
                
                a_wSResource_property = devopsagent.CfnAssociation.AWSResourceProperty(
                    resource_arn="resourceArn",
                
                    # the properties below are optional
                    resource_metadata=resource_metadata,
                    resource_type="resourceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c83865c7f5f4d4caa82576ab7efaac17f6225904d0ac52970333a1906f6ed0cb)
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument resource_metadata", value=resource_metadata, expected_type=type_hints["resource_metadata"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_arn": resource_arn,
            }
            if resource_metadata is not None:
                self._values["resource_metadata"] = resource_metadata
            if resource_type is not None:
                self._values["resource_type"] = resource_type

        @builtins.property
        def resource_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsresource.html#cfn-devopsagent-association-awsresource-resourcearn
            '''
            result = self._values.get("resource_arn")
            assert result is not None, "Required property 'resource_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resource_metadata(self) -> typing.Any:
            '''Additional metadata specific to the resource.

            This is an optional JSON object that can include resource-specific information to provide additional context for monitoring and management.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsresource.html#cfn-devopsagent-association-awsresource-resourcemetadata
            '''
            result = self._values.get("resource_metadata")
            return typing.cast(typing.Any, result)

        @builtins.property
        def resource_type(self) -> typing.Optional[builtins.str]:
            '''Resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-awsresource.html#cfn-devopsagent-association-awsresource-resourcetype
            '''
            result = self._values.get("resource_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AWSResourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.DynatraceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "env_id": "envId",
            "enable_webhook_updates": "enableWebhookUpdates",
            "resources": "resources",
        },
    )
    class DynatraceConfigurationProperty:
        def __init__(
            self,
            *,
            env_id: builtins.str,
            enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration for Dynatrace monitoring integration.

            Defines the Dynatrace environment ID, list of resources to monitor, and webhook update settings required for the Agent Space to access metrics, traces, and logs from Dynatrace.

            :param env_id: Dynatrace environment id.
            :param enable_webhook_updates: When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.
            :param resources: List of Dynatrace resources to monitor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-dynatraceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                dynatrace_configuration_property = devopsagent.CfnAssociation.DynatraceConfigurationProperty(
                    env_id="envId",
                
                    # the properties below are optional
                    enable_webhook_updates=False,
                    resources=["resources"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__af533dc830c7a5f8fd17b5170cecf1e7dd483fe076400d57927aca27831a0ca8)
                check_type(argname="argument env_id", value=env_id, expected_type=type_hints["env_id"])
                check_type(argname="argument enable_webhook_updates", value=enable_webhook_updates, expected_type=type_hints["enable_webhook_updates"])
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "env_id": env_id,
            }
            if enable_webhook_updates is not None:
                self._values["enable_webhook_updates"] = enable_webhook_updates
            if resources is not None:
                self._values["resources"] = resources

        @builtins.property
        def env_id(self) -> builtins.str:
            '''Dynatrace environment id.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-dynatraceconfiguration.html#cfn-devopsagent-association-dynatraceconfiguration-envid
            '''
            result = self._values.get("env_id")
            assert result is not None, "Required property 'env_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def enable_webhook_updates(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-dynatraceconfiguration.html#cfn-devopsagent-association-dynatraceconfiguration-enablewebhookupdates
            '''
            result = self._values.get("enable_webhook_updates")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def resources(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of Dynatrace resources to monitor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-dynatraceconfiguration.html#cfn-devopsagent-association-dynatraceconfiguration-resources
            '''
            result = self._values.get("resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynatraceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.EventChannelConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enable_webhook_updates": "enableWebhookUpdates"},
    )
    class EventChannelConfigurationProperty:
        def __init__(
            self,
            *,
            enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''Configuration for Event Channel integration.

            Defines webhook update settings to enable the Agent Space to receive real-time event notifications from event channel integrations.

            :param enable_webhook_updates: When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-eventchannelconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                event_channel_configuration_property = devopsagent.CfnAssociation.EventChannelConfigurationProperty(
                    enable_webhook_updates=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5d900735d86a3a2a681d9eba7f3ce7754e8cdfbc47df16370253e165583cd41)
                check_type(argname="argument enable_webhook_updates", value=enable_webhook_updates, expected_type=type_hints["enable_webhook_updates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_webhook_updates is not None:
                self._values["enable_webhook_updates"] = enable_webhook_updates

        @builtins.property
        def enable_webhook_updates(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-eventchannelconfiguration.html#cfn-devopsagent-association-eventchannelconfiguration-enablewebhookupdates
            '''
            result = self._values.get("enable_webhook_updates")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventChannelConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.GitHubConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "owner": "owner",
            "owner_type": "ownerType",
            "repo_id": "repoId",
            "repo_name": "repoName",
        },
    )
    class GitHubConfigurationProperty:
        def __init__(
            self,
            *,
            owner: builtins.str,
            owner_type: builtins.str,
            repo_id: builtins.str,
            repo_name: builtins.str,
        ) -> None:
            '''Configuration for GitHub repository integration.

            Defines the repository name, numeric repository ID, owner name, and owner type (user or organization) required for the Agent Space to access and interact with the GitHub repository.

            :param owner: Repository owner.
            :param owner_type: Type of repository owner.
            :param repo_id: Associated Github repo ID.
            :param repo_name: Associated Github repo name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-githubconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                git_hub_configuration_property = devopsagent.CfnAssociation.GitHubConfigurationProperty(
                    owner="owner",
                    owner_type="ownerType",
                    repo_id="repoId",
                    repo_name="repoName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f52e2bfd74e3e041299304fca2e11acf7c77935cb3d81768bd90034e89f0c1f3)
                check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
                check_type(argname="argument owner_type", value=owner_type, expected_type=type_hints["owner_type"])
                check_type(argname="argument repo_id", value=repo_id, expected_type=type_hints["repo_id"])
                check_type(argname="argument repo_name", value=repo_name, expected_type=type_hints["repo_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "owner": owner,
                "owner_type": owner_type,
                "repo_id": repo_id,
                "repo_name": repo_name,
            }

        @builtins.property
        def owner(self) -> builtins.str:
            '''Repository owner.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-githubconfiguration.html#cfn-devopsagent-association-githubconfiguration-owner
            '''
            result = self._values.get("owner")
            assert result is not None, "Required property 'owner' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def owner_type(self) -> builtins.str:
            '''Type of repository owner.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-githubconfiguration.html#cfn-devopsagent-association-githubconfiguration-ownertype
            '''
            result = self._values.get("owner_type")
            assert result is not None, "Required property 'owner_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def repo_id(self) -> builtins.str:
            '''Associated Github repo ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-githubconfiguration.html#cfn-devopsagent-association-githubconfiguration-repoid
            '''
            result = self._values.get("repo_id")
            assert result is not None, "Required property 'repo_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def repo_name(self) -> builtins.str:
            '''Associated Github repo name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-githubconfiguration.html#cfn-devopsagent-association-githubconfiguration-reponame
            '''
            result = self._values.get("repo_name")
            assert result is not None, "Required property 'repo_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GitHubConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.GitLabConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "project_id": "projectId",
            "project_path": "projectPath",
            "enable_webhook_updates": "enableWebhookUpdates",
            "instance_identifier": "instanceIdentifier",
        },
    )
    class GitLabConfigurationProperty:
        def __init__(
            self,
            *,
            project_id: builtins.str,
            project_path: builtins.str,
            enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            instance_identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for GitLab project integration.

            Defines the numeric project ID, full project path (namespace/project-name), GitLab instance identifier, and webhook update settings required for the Agent Space to access and interact with the GitLab project.

            :param project_id: GitLab numeric project ID.
            :param project_path: Full GitLab project path (e.g., namespace/project-name).
            :param enable_webhook_updates: When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.
            :param instance_identifier: GitLab instance identifier (e.g., gitlab.com).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-gitlabconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                git_lab_configuration_property = devopsagent.CfnAssociation.GitLabConfigurationProperty(
                    project_id="projectId",
                    project_path="projectPath",
                
                    # the properties below are optional
                    enable_webhook_updates=False,
                    instance_identifier="instanceIdentifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d0bf76d18d2da5c1a7b65fd908fdd6aa4ca798335d0ef9f07ec4c064ccb5241)
                check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
                check_type(argname="argument project_path", value=project_path, expected_type=type_hints["project_path"])
                check_type(argname="argument enable_webhook_updates", value=enable_webhook_updates, expected_type=type_hints["enable_webhook_updates"])
                check_type(argname="argument instance_identifier", value=instance_identifier, expected_type=type_hints["instance_identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "project_id": project_id,
                "project_path": project_path,
            }
            if enable_webhook_updates is not None:
                self._values["enable_webhook_updates"] = enable_webhook_updates
            if instance_identifier is not None:
                self._values["instance_identifier"] = instance_identifier

        @builtins.property
        def project_id(self) -> builtins.str:
            '''GitLab numeric project ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-gitlabconfiguration.html#cfn-devopsagent-association-gitlabconfiguration-projectid
            '''
            result = self._values.get("project_id")
            assert result is not None, "Required property 'project_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def project_path(self) -> builtins.str:
            '''Full GitLab project path (e.g., namespace/project-name).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-gitlabconfiguration.html#cfn-devopsagent-association-gitlabconfiguration-projectpath
            '''
            result = self._values.get("project_path")
            assert result is not None, "Required property 'project_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def enable_webhook_updates(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-gitlabconfiguration.html#cfn-devopsagent-association-gitlabconfiguration-enablewebhookupdates
            '''
            result = self._values.get("enable_webhook_updates")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def instance_identifier(self) -> typing.Optional[builtins.str]:
            '''GitLab instance identifier (e.g., gitlab.com).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-gitlabconfiguration.html#cfn-devopsagent-association-gitlabconfiguration-instanceidentifier
            '''
            result = self._values.get("instance_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GitLabConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.KeyValuePairProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class KeyValuePairProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A key-value pair for tags.

            :param key: The key name of the tag.
            :param value: The value for the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-keyvaluepair.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                key_value_pair_property = devopsagent.CfnAssociation.KeyValuePairProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ded74f7f3af261fdfeb1ca20f0589b46cd28465b569b567f86c794c6d2010df2)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key name of the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-keyvaluepair.html#cfn-devopsagent-association-keyvaluepair-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value for the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-keyvaluepair.html#cfn-devopsagent-association-keyvaluepair-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValuePairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.MCPServerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "name": "name",
            "tools": "tools",
            "description": "description",
            "enable_webhook_updates": "enableWebhookUpdates",
        },
    )
    class MCPServerConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            name: builtins.str,
            tools: typing.Sequence[builtins.str],
            description: typing.Optional[builtins.str] = None,
            enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''Configuration for MCP (Model Context Protocol) server integration.

            Defines the server name, endpoint URL, available tools, optional description, and webhook update settings for custom MCP servers.

            :param endpoint: MCP server endpoint URL.
            :param name: The name of the MCP server.
            :param tools: List of MCP tools that can be used with the association.
            :param description: The description of the MCP server.
            :param enable_webhook_updates: When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                m_cPServer_configuration_property = devopsagent.CfnAssociation.MCPServerConfigurationProperty(
                    endpoint="endpoint",
                    name="name",
                    tools=["tools"],
                
                    # the properties below are optional
                    description="description",
                    enable_webhook_updates=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__97d8de94964f9d444ce60e60c71a8386873d9d717628a8b450e0463922b08600)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument tools", value=tools, expected_type=type_hints["tools"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument enable_webhook_updates", value=enable_webhook_updates, expected_type=type_hints["enable_webhook_updates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint": endpoint,
                "name": name,
                "tools": tools,
            }
            if description is not None:
                self._values["description"] = description
            if enable_webhook_updates is not None:
                self._values["enable_webhook_updates"] = enable_webhook_updates

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''MCP server endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverconfiguration.html#cfn-devopsagent-association-mcpserverconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverconfiguration.html#cfn-devopsagent-association-mcpserverconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tools(self) -> typing.List[builtins.str]:
            '''List of MCP tools that can be used with the association.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverconfiguration.html#cfn-devopsagent-association-mcpserverconfiguration-tools
            '''
            result = self._values.get("tools")
            assert result is not None, "Required property 'tools' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverconfiguration.html#cfn-devopsagent-association-mcpserverconfiguration-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_webhook_updates(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverconfiguration.html#cfn-devopsagent-association-mcpserverconfiguration-enablewebhookupdates
            '''
            result = self._values.get("enable_webhook_updates")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPServerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.MCPServerDatadogConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "name": "name",
            "description": "description",
            "enable_webhook_updates": "enableWebhookUpdates",
        },
    )
    class MCPServerDatadogConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
            enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''Configuration for Datadog MCP server integration.

            Defines the server name, endpoint URL, optional description, and webhook update settings.

            :param endpoint: MCP server endpoint URL.
            :param name: The name of the MCP server.
            :param description: The description of the MCP server.
            :param enable_webhook_updates: When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverdatadogconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                m_cPServer_datadog_configuration_property = devopsagent.CfnAssociation.MCPServerDatadogConfigurationProperty(
                    endpoint="endpoint",
                    name="name",
                
                    # the properties below are optional
                    description="description",
                    enable_webhook_updates=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94bdd66d2ae6508b6fa75de77b1b7bd044d6bf7b9e0c60cb573f57ca7faa1817)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument enable_webhook_updates", value=enable_webhook_updates, expected_type=type_hints["enable_webhook_updates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint": endpoint,
                "name": name,
            }
            if description is not None:
                self._values["description"] = description
            if enable_webhook_updates is not None:
                self._values["enable_webhook_updates"] = enable_webhook_updates

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''MCP server endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverdatadogconfiguration.html#cfn-devopsagent-association-mcpserverdatadogconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverdatadogconfiguration.html#cfn-devopsagent-association-mcpserverdatadogconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverdatadogconfiguration.html#cfn-devopsagent-association-mcpserverdatadogconfiguration-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_webhook_updates(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserverdatadogconfiguration.html#cfn-devopsagent-association-mcpserverdatadogconfiguration-enablewebhookupdates
            '''
            result = self._values.get("enable_webhook_updates")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPServerDatadogConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.MCPServerNewRelicConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"account_id": "accountId", "endpoint": "endpoint"},
    )
    class MCPServerNewRelicConfigurationProperty:
        def __init__(self, *, account_id: builtins.str, endpoint: builtins.str) -> None:
            '''Configuration for New Relic MCP server integration.

            Defines the New Relic account ID and MCP server endpoint URL required for the Agent Space to authenticate and query observability data from New Relic.

            :param account_id: New Relic Account ID.
            :param endpoint: MCP server endpoint URL (e.g., https://mcp.newrelic.com/mcp/).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpservernewrelicconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                m_cPServer_new_relic_configuration_property = devopsagent.CfnAssociation.MCPServerNewRelicConfigurationProperty(
                    account_id="accountId",
                    endpoint="endpoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d60c2241968bd47959618d5fef16076f92aa6b8c2e1932e3d7d5e3983c4108a8)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_id": account_id,
                "endpoint": endpoint,
            }

        @builtins.property
        def account_id(self) -> builtins.str:
            '''New Relic Account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpservernewrelicconfiguration.html#cfn-devopsagent-association-mcpservernewrelicconfiguration-accountid
            '''
            result = self._values.get("account_id")
            assert result is not None, "Required property 'account_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''MCP server endpoint URL (e.g., https://mcp.newrelic.com/mcp/).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpservernewrelicconfiguration.html#cfn-devopsagent-association-mcpservernewrelicconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPServerNewRelicConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.MCPServerSplunkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint": "endpoint",
            "name": "name",
            "description": "description",
            "enable_webhook_updates": "enableWebhookUpdates",
        },
    )
    class MCPServerSplunkConfigurationProperty:
        def __init__(
            self,
            *,
            endpoint: builtins.str,
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
            enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''Configuration for Splunk MCP server integration.

            Defines the server name, endpoint URL, optional description, and webhook update settings.

            :param endpoint: MCP server endpoint URL.
            :param name: The name of the MCP server.
            :param description: The description of the MCP server.
            :param enable_webhook_updates: When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserversplunkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                m_cPServer_splunk_configuration_property = devopsagent.CfnAssociation.MCPServerSplunkConfigurationProperty(
                    endpoint="endpoint",
                    name="name",
                
                    # the properties below are optional
                    description="description",
                    enable_webhook_updates=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5251bb56068759277d9b99b06c4d20b0e0434473774eeb3d825f9ed5301ba970)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument enable_webhook_updates", value=enable_webhook_updates, expected_type=type_hints["enable_webhook_updates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint": endpoint,
                "name": name,
            }
            if description is not None:
                self._values["description"] = description
            if enable_webhook_updates is not None:
                self._values["enable_webhook_updates"] = enable_webhook_updates

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''MCP server endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserversplunkconfiguration.html#cfn-devopsagent-association-mcpserversplunkconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserversplunkconfiguration.html#cfn-devopsagent-association-mcpserversplunkconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserversplunkconfiguration.html#cfn-devopsagent-association-mcpserversplunkconfiguration-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_webhook_updates(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-mcpserversplunkconfiguration.html#cfn-devopsagent-association-mcpserversplunkconfiguration-enablewebhookupdates
            '''
            result = self._values.get("enable_webhook_updates")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPServerSplunkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.ServiceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws": "aws",
            "dynatrace": "dynatrace",
            "event_channel": "eventChannel",
            "git_hub": "gitHub",
            "git_lab": "gitLab",
            "mcp_server": "mcpServer",
            "mcp_server_datadog": "mcpServerDatadog",
            "mcp_server_new_relic": "mcpServerNewRelic",
            "mcp_server_splunk": "mcpServerSplunk",
            "service_now": "serviceNow",
            "slack": "slack",
            "source_aws": "sourceAws",
        },
    )
    class ServiceConfigurationProperty:
        def __init__(
            self,
            *,
            aws: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.AWSConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynatrace: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.DynatraceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            event_channel: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.EventChannelConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            git_hub: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.GitHubConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            git_lab: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.GitLabConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.MCPServerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server_datadog: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.MCPServerDatadogConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server_new_relic: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.MCPServerNewRelicConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server_splunk: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.MCPServerSplunkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_now: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.ServiceNowConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            slack: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.SlackConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            source_aws: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.SourceAwsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration that directs how Agent Space interacts with the given service.

            You can specify only one configuration type per association.

            :param aws: Configuration for AWS monitor account integration. Specifies the account ID, assumable role ARN, and resources to be monitored in the primary monitoring account.
            :param dynatrace: Configuration for Dynatrace monitoring integration. Specifies the environment ID, resources to monitor, and webhook settings to enable the Agent Space to access Dynatrace metrics, traces, and logs.
            :param event_channel: Configuration for Event Channel integration. Specifies webhook settings to enable the Agent Space to receive and process real-time events from external systems.
            :param git_hub: Configuration for GitHub repository integration. Specifies the repository name, repository ID, owner, and owner type to enable the Agent Space to access code, pull requests, and issues.
            :param git_lab: Configuration for GitLab project integration. Specifies the project ID, project path, instance identifier, and webhook settings to enable the Agent Space to access code, merge requests, and issues.
            :param mcp_server: Configuration for custom MCP (Model Context Protocol) server integration. Specifies the server name, endpoint URL, available tools, description, and webhook settings to enable the Agent Space to interact with custom MCP servers.
            :param mcp_server_datadog: Configuration for Datadog MCP server integration. Specifies the server name, endpoint URL, optional description, and webhook settings to enable the Agent Space to query metrics, traces, and logs from Datadog.
            :param mcp_server_new_relic: Configuration for New Relic MCP server integration. Specifies the New Relic account ID and MCP endpoint URL to enable the Agent Space to query metrics, traces, and logs from New Relic.
            :param mcp_server_splunk: Configuration for Splunk MCP server integration. Specifies the server name, endpoint URL, optional description, and webhook settings to enable the Agent Space to query logs, metrics, and events from Splunk.
            :param service_now: Configuration for ServiceNow instance integration. Specifies the instance URL, instance ID, and webhook settings to enable the Agent Space to create, update, and manage ServiceNow incidents and change requests.
            :param slack: Configuration for Slack workspace integration. Specifies the workspace ID, workspace name, and transmission targets to enable the Agent Space to send notifications to designated Slack channels.
            :param source_aws: Configuration for AWS source account integration. Specifies the account ID, assumable role ARN, and resources to be monitored in the source account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # resource_metadata: Any
                
                service_configuration_property = devopsagent.CfnAssociation.ServiceConfigurationProperty(
                    aws=devopsagent.CfnAssociation.AWSConfigurationProperty(
                        account_id="accountId",
                        account_type="accountType",
                        assumable_role_arn="assumableRoleArn",
                
                        # the properties below are optional
                        resources=[devopsagent.CfnAssociation.AWSResourceProperty(
                            resource_arn="resourceArn",
                
                            # the properties below are optional
                            resource_metadata=resource_metadata,
                            resource_type="resourceType"
                        )],
                        tags=[devopsagent.CfnAssociation.KeyValuePairProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    dynatrace=devopsagent.CfnAssociation.DynatraceConfigurationProperty(
                        env_id="envId",
                
                        # the properties below are optional
                        enable_webhook_updates=False,
                        resources=["resources"]
                    ),
                    event_channel=devopsagent.CfnAssociation.EventChannelConfigurationProperty(
                        enable_webhook_updates=False
                    ),
                    git_hub=devopsagent.CfnAssociation.GitHubConfigurationProperty(
                        owner="owner",
                        owner_type="ownerType",
                        repo_id="repoId",
                        repo_name="repoName"
                    ),
                    git_lab=devopsagent.CfnAssociation.GitLabConfigurationProperty(
                        project_id="projectId",
                        project_path="projectPath",
                
                        # the properties below are optional
                        enable_webhook_updates=False,
                        instance_identifier="instanceIdentifier"
                    ),
                    mcp_server=devopsagent.CfnAssociation.MCPServerConfigurationProperty(
                        endpoint="endpoint",
                        name="name",
                        tools=["tools"],
                
                        # the properties below are optional
                        description="description",
                        enable_webhook_updates=False
                    ),
                    mcp_server_datadog=devopsagent.CfnAssociation.MCPServerDatadogConfigurationProperty(
                        endpoint="endpoint",
                        name="name",
                
                        # the properties below are optional
                        description="description",
                        enable_webhook_updates=False
                    ),
                    mcp_server_new_relic=devopsagent.CfnAssociation.MCPServerNewRelicConfigurationProperty(
                        account_id="accountId",
                        endpoint="endpoint"
                    ),
                    mcp_server_splunk=devopsagent.CfnAssociation.MCPServerSplunkConfigurationProperty(
                        endpoint="endpoint",
                        name="name",
                
                        # the properties below are optional
                        description="description",
                        enable_webhook_updates=False
                    ),
                    service_now=devopsagent.CfnAssociation.ServiceNowConfigurationProperty(
                        enable_webhook_updates=False,
                        instance_id="instanceId"
                    ),
                    slack=devopsagent.CfnAssociation.SlackConfigurationProperty(
                        transmission_target=devopsagent.CfnAssociation.SlackTransmissionTargetProperty(
                            incident_response_target=devopsagent.CfnAssociation.SlackChannelProperty(
                                channel_id="channelId",
                
                                # the properties below are optional
                                channel_name="channelName"
                            )
                        ),
                        workspace_id="workspaceId",
                        workspace_name="workspaceName"
                    ),
                    source_aws=devopsagent.CfnAssociation.SourceAwsConfigurationProperty(
                        account_id="accountId",
                        account_type="accountType",
                        assumable_role_arn="assumableRoleArn",
                
                        # the properties below are optional
                        resources=[devopsagent.CfnAssociation.AWSResourceProperty(
                            resource_arn="resourceArn",
                
                            # the properties below are optional
                            resource_metadata=resource_metadata,
                            resource_type="resourceType"
                        )],
                        tags=[devopsagent.CfnAssociation.KeyValuePairProperty(
                            key="key",
                            value="value"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__534ff66bec4c3f764380e71fc8dbccb3b6b0319f301032fa7e975aa1842a74e1)
                check_type(argname="argument aws", value=aws, expected_type=type_hints["aws"])
                check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
                check_type(argname="argument event_channel", value=event_channel, expected_type=type_hints["event_channel"])
                check_type(argname="argument git_hub", value=git_hub, expected_type=type_hints["git_hub"])
                check_type(argname="argument git_lab", value=git_lab, expected_type=type_hints["git_lab"])
                check_type(argname="argument mcp_server", value=mcp_server, expected_type=type_hints["mcp_server"])
                check_type(argname="argument mcp_server_datadog", value=mcp_server_datadog, expected_type=type_hints["mcp_server_datadog"])
                check_type(argname="argument mcp_server_new_relic", value=mcp_server_new_relic, expected_type=type_hints["mcp_server_new_relic"])
                check_type(argname="argument mcp_server_splunk", value=mcp_server_splunk, expected_type=type_hints["mcp_server_splunk"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
                check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
                check_type(argname="argument source_aws", value=source_aws, expected_type=type_hints["source_aws"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws is not None:
                self._values["aws"] = aws
            if dynatrace is not None:
                self._values["dynatrace"] = dynatrace
            if event_channel is not None:
                self._values["event_channel"] = event_channel
            if git_hub is not None:
                self._values["git_hub"] = git_hub
            if git_lab is not None:
                self._values["git_lab"] = git_lab
            if mcp_server is not None:
                self._values["mcp_server"] = mcp_server
            if mcp_server_datadog is not None:
                self._values["mcp_server_datadog"] = mcp_server_datadog
            if mcp_server_new_relic is not None:
                self._values["mcp_server_new_relic"] = mcp_server_new_relic
            if mcp_server_splunk is not None:
                self._values["mcp_server_splunk"] = mcp_server_splunk
            if service_now is not None:
                self._values["service_now"] = service_now
            if slack is not None:
                self._values["slack"] = slack
            if source_aws is not None:
                self._values["source_aws"] = source_aws

        @builtins.property
        def aws(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.AWSConfigurationProperty"]]:
            '''Configuration for AWS monitor account integration.

            Specifies the account ID, assumable role ARN, and resources to be monitored in the primary monitoring account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-aws
            '''
            result = self._values.get("aws")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.AWSConfigurationProperty"]], result)

        @builtins.property
        def dynatrace(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.DynatraceConfigurationProperty"]]:
            '''Configuration for Dynatrace monitoring integration.

            Specifies the environment ID, resources to monitor, and webhook settings to enable the Agent Space to access Dynatrace metrics, traces, and logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-dynatrace
            '''
            result = self._values.get("dynatrace")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.DynatraceConfigurationProperty"]], result)

        @builtins.property
        def event_channel(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.EventChannelConfigurationProperty"]]:
            '''Configuration for Event Channel integration.

            Specifies webhook settings to enable the Agent Space to receive and process real-time events from external systems.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-eventchannel
            '''
            result = self._values.get("event_channel")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.EventChannelConfigurationProperty"]], result)

        @builtins.property
        def git_hub(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.GitHubConfigurationProperty"]]:
            '''Configuration for GitHub repository integration.

            Specifies the repository name, repository ID, owner, and owner type to enable the Agent Space to access code, pull requests, and issues.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-github
            '''
            result = self._values.get("git_hub")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.GitHubConfigurationProperty"]], result)

        @builtins.property
        def git_lab(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.GitLabConfigurationProperty"]]:
            '''Configuration for GitLab project integration.

            Specifies the project ID, project path, instance identifier, and webhook settings to enable the Agent Space to access code, merge requests, and issues.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-gitlab
            '''
            result = self._values.get("git_lab")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.GitLabConfigurationProperty"]], result)

        @builtins.property
        def mcp_server(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.MCPServerConfigurationProperty"]]:
            '''Configuration for custom MCP (Model Context Protocol) server integration.

            Specifies the server name, endpoint URL, available tools, description, and webhook settings to enable the Agent Space to interact with custom MCP servers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-mcpserver
            '''
            result = self._values.get("mcp_server")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.MCPServerConfigurationProperty"]], result)

        @builtins.property
        def mcp_server_datadog(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.MCPServerDatadogConfigurationProperty"]]:
            '''Configuration for Datadog MCP server integration.

            Specifies the server name, endpoint URL, optional description, and webhook settings to enable the Agent Space to query metrics, traces, and logs from Datadog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-mcpserverdatadog
            '''
            result = self._values.get("mcp_server_datadog")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.MCPServerDatadogConfigurationProperty"]], result)

        @builtins.property
        def mcp_server_new_relic(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.MCPServerNewRelicConfigurationProperty"]]:
            '''Configuration for New Relic MCP server integration.

            Specifies the New Relic account ID and MCP endpoint URL to enable the Agent Space to query metrics, traces, and logs from New Relic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-mcpservernewrelic
            '''
            result = self._values.get("mcp_server_new_relic")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.MCPServerNewRelicConfigurationProperty"]], result)

        @builtins.property
        def mcp_server_splunk(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.MCPServerSplunkConfigurationProperty"]]:
            '''Configuration for Splunk MCP server integration.

            Specifies the server name, endpoint URL, optional description, and webhook settings to enable the Agent Space to query logs, metrics, and events from Splunk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-mcpserversplunk
            '''
            result = self._values.get("mcp_server_splunk")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.MCPServerSplunkConfigurationProperty"]], result)

        @builtins.property
        def service_now(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.ServiceNowConfigurationProperty"]]:
            '''Configuration for ServiceNow instance integration.

            Specifies the instance URL, instance ID, and webhook settings to enable the Agent Space to create, update, and manage ServiceNow incidents and change requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.ServiceNowConfigurationProperty"]], result)

        @builtins.property
        def slack(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.SlackConfigurationProperty"]]:
            '''Configuration for Slack workspace integration.

            Specifies the workspace ID, workspace name, and transmission targets to enable the Agent Space to send notifications to designated Slack channels.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-slack
            '''
            result = self._values.get("slack")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.SlackConfigurationProperty"]], result)

        @builtins.property
        def source_aws(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.SourceAwsConfigurationProperty"]]:
            '''Configuration for AWS source account integration.

            Specifies the account ID, assumable role ARN, and resources to be monitored in the source account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-serviceconfiguration.html#cfn-devopsagent-association-serviceconfiguration-sourceaws
            '''
            result = self._values.get("source_aws")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAssociation.SourceAwsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.ServiceNowConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_webhook_updates": "enableWebhookUpdates",
            "instance_id": "instanceId",
        },
    )
    class ServiceNowConfigurationProperty:
        def __init__(
            self,
            *,
            enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            instance_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for ServiceNow integration.

            Defines the ServiceNow instance URL, instance ID, and webhook update settings required for the Agent Space to create, update, and manage incidents and change requests.

            :param enable_webhook_updates: When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.
            :param instance_id: ServiceNow instance ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-servicenowconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                service_now_configuration_property = devopsagent.CfnAssociation.ServiceNowConfigurationProperty(
                    enable_webhook_updates=False,
                    instance_id="instanceId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9767ae84f8f9ac8fbffe3c19d1ac1dc61d581770deb87d97b058eb73cc671511)
                check_type(argname="argument enable_webhook_updates", value=enable_webhook_updates, expected_type=type_hints["enable_webhook_updates"])
                check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_webhook_updates is not None:
                self._values["enable_webhook_updates"] = enable_webhook_updates
            if instance_id is not None:
                self._values["instance_id"] = instance_id

        @builtins.property
        def enable_webhook_updates(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''When set to true, enables the Agent Space to create and update webhooks for receiving notifications and events from the service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-servicenowconfiguration.html#cfn-devopsagent-association-servicenowconfiguration-enablewebhookupdates
            '''
            result = self._values.get("enable_webhook_updates")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def instance_id(self) -> typing.Optional[builtins.str]:
            '''ServiceNow instance ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-servicenowconfiguration.html#cfn-devopsagent-association-servicenowconfiguration-instanceid
            '''
            result = self._values.get("instance_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.SlackChannelProperty",
        jsii_struct_bases=[],
        name_mapping={"channel_id": "channelId", "channel_name": "channelName"},
    )
    class SlackChannelProperty:
        def __init__(
            self,
            *,
            channel_id: builtins.str,
            channel_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents a Slack channel with its unique identifier and optional display name.

            :param channel_id: Slack channel ID.
            :param channel_name: Slack channel name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-slackchannel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                slack_channel_property = devopsagent.CfnAssociation.SlackChannelProperty(
                    channel_id="channelId",
                
                    # the properties below are optional
                    channel_name="channelName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__06cf6d0fee94466c60ffb3cbfb9f571fb9f69201085fc5de6cd2f0d6e4b8d633)
                check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
                check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "channel_id": channel_id,
            }
            if channel_name is not None:
                self._values["channel_name"] = channel_name

        @builtins.property
        def channel_id(self) -> builtins.str:
            '''Slack channel ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-slackchannel.html#cfn-devopsagent-association-slackchannel-channelid
            '''
            result = self._values.get("channel_id")
            assert result is not None, "Required property 'channel_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def channel_name(self) -> typing.Optional[builtins.str]:
            '''Slack channel name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-slackchannel.html#cfn-devopsagent-association-slackchannel-channelname
            '''
            result = self._values.get("channel_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlackChannelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.SlackConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "transmission_target": "transmissionTarget",
            "workspace_id": "workspaceId",
            "workspace_name": "workspaceName",
        },
    )
    class SlackConfigurationProperty:
        def __init__(
            self,
            *,
            transmission_target: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.SlackTransmissionTargetProperty", typing.Dict[builtins.str, typing.Any]]],
            workspace_id: builtins.str,
            workspace_name: builtins.str,
        ) -> None:
            '''Configuration for Slack workspace integration.

            Defines the workspace ID, workspace name, and transmission targets that specify which Slack channels receive notifications.

            :param transmission_target: Transmission targets for agent notifications.
            :param workspace_id: Associated Slack workspace ID.
            :param workspace_name: Associated Slack workspace name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-slackconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                slack_configuration_property = devopsagent.CfnAssociation.SlackConfigurationProperty(
                    transmission_target=devopsagent.CfnAssociation.SlackTransmissionTargetProperty(
                        incident_response_target=devopsagent.CfnAssociation.SlackChannelProperty(
                            channel_id="channelId",
                
                            # the properties below are optional
                            channel_name="channelName"
                        )
                    ),
                    workspace_id="workspaceId",
                    workspace_name="workspaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__28eb759dbeb853e46c5ba811aba401a06c7b87554a3bac255792e3d13c3f0c23)
                check_type(argname="argument transmission_target", value=transmission_target, expected_type=type_hints["transmission_target"])
                check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
                check_type(argname="argument workspace_name", value=workspace_name, expected_type=type_hints["workspace_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "transmission_target": transmission_target,
                "workspace_id": workspace_id,
                "workspace_name": workspace_name,
            }

        @builtins.property
        def transmission_target(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnAssociation.SlackTransmissionTargetProperty"]:
            '''Transmission targets for agent notifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-slackconfiguration.html#cfn-devopsagent-association-slackconfiguration-transmissiontarget
            '''
            result = self._values.get("transmission_target")
            assert result is not None, "Required property 'transmission_target' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAssociation.SlackTransmissionTargetProperty"], result)

        @builtins.property
        def workspace_id(self) -> builtins.str:
            '''Associated Slack workspace ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-slackconfiguration.html#cfn-devopsagent-association-slackconfiguration-workspaceid
            '''
            result = self._values.get("workspace_id")
            assert result is not None, "Required property 'workspace_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def workspace_name(self) -> builtins.str:
            '''Associated Slack workspace name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-slackconfiguration.html#cfn-devopsagent-association-slackconfiguration-workspacename
            '''
            result = self._values.get("workspace_name")
            assert result is not None, "Required property 'workspace_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlackConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.SlackTransmissionTargetProperty",
        jsii_struct_bases=[],
        name_mapping={"incident_response_target": "incidentResponseTarget"},
    )
    class SlackTransmissionTargetProperty:
        def __init__(
            self,
            *,
            incident_response_target: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.SlackChannelProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Defines the Slack channels where different types of agent notifications will be sent.

            :param incident_response_target: Destination for AWS DevOps Agent Incident Response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-slacktransmissiontarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                slack_transmission_target_property = devopsagent.CfnAssociation.SlackTransmissionTargetProperty(
                    incident_response_target=devopsagent.CfnAssociation.SlackChannelProperty(
                        channel_id="channelId",
                
                        # the properties below are optional
                        channel_name="channelName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4224928b94c6f3a7e8aeb21f4d921f668ae91ec705e4026d010b1813687b20c5)
                check_type(argname="argument incident_response_target", value=incident_response_target, expected_type=type_hints["incident_response_target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "incident_response_target": incident_response_target,
            }

        @builtins.property
        def incident_response_target(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnAssociation.SlackChannelProperty"]:
            '''Destination for AWS DevOps Agent Incident Response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-slacktransmissiontarget.html#cfn-devopsagent-association-slacktransmissiontarget-incidentresponsetarget
            '''
            result = self._values.get("incident_response_target")
            assert result is not None, "Required property 'incident_response_target' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAssociation.SlackChannelProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlackTransmissionTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociation.SourceAwsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "account_type": "accountType",
            "assumable_role_arn": "assumableRoleArn",
            "resources": "resources",
            "tags": "tags",
        },
    )
    class SourceAwsConfigurationProperty:
        def __init__(
            self,
            *,
            account_id: builtins.str,
            account_type: builtins.str,
            assumable_role_arn: builtins.str,
            resources: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.AWSResourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            tags: typing.Optional[typing.Sequence[typing.Union["CfnAssociation.KeyValuePairProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration for AWS source account integration.

            Specifies the account ID, assumable role ARN, and resources to be monitored in the source account.

            :param account_id: Account ID corresponding to the provided resources.
            :param account_type: Account Type 'source' for AWS DevOps Agent monitoring.
            :param assumable_role_arn: Role ARN to be assumed by AWS DevOps Agent to operate on behalf of customer.
            :param resources: List of resources to monitor.
            :param tags: List of tags as key-value pairs, used to identify resources for topology crawl.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-sourceawsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # resource_metadata: Any
                
                source_aws_configuration_property = devopsagent.CfnAssociation.SourceAwsConfigurationProperty(
                    account_id="accountId",
                    account_type="accountType",
                    assumable_role_arn="assumableRoleArn",
                
                    # the properties below are optional
                    resources=[devopsagent.CfnAssociation.AWSResourceProperty(
                        resource_arn="resourceArn",
                
                        # the properties below are optional
                        resource_metadata=resource_metadata,
                        resource_type="resourceType"
                    )],
                    tags=[devopsagent.CfnAssociation.KeyValuePairProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7f309a9bf78a2704dbd1fd90dfdf8ff7ac7091cdb4572312fad3281cfcbd5ac)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument account_type", value=account_type, expected_type=type_hints["account_type"])
                check_type(argname="argument assumable_role_arn", value=assumable_role_arn, expected_type=type_hints["assumable_role_arn"])
                check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_id": account_id,
                "account_type": account_type,
                "assumable_role_arn": assumable_role_arn,
            }
            if resources is not None:
                self._values["resources"] = resources
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def account_id(self) -> builtins.str:
            '''Account ID corresponding to the provided resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-sourceawsconfiguration.html#cfn-devopsagent-association-sourceawsconfiguration-accountid
            '''
            result = self._values.get("account_id")
            assert result is not None, "Required property 'account_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account_type(self) -> builtins.str:
            '''Account Type 'source' for AWS DevOps Agent monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-sourceawsconfiguration.html#cfn-devopsagent-association-sourceawsconfiguration-accounttype
            '''
            result = self._values.get("account_type")
            assert result is not None, "Required property 'account_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def assumable_role_arn(self) -> builtins.str:
            '''Role ARN to be assumed by AWS DevOps Agent to operate on behalf of customer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-sourceawsconfiguration.html#cfn-devopsagent-association-sourceawsconfiguration-assumablerolearn
            '''
            result = self._values.get("assumable_role_arn")
            assert result is not None, "Required property 'assumable_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def resources(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAssociation.AWSResourceProperty"]]]]:
            '''List of resources to monitor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-sourceawsconfiguration.html#cfn-devopsagent-association-sourceawsconfiguration-resources
            '''
            result = self._values.get("resources")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAssociation.AWSResourceProperty"]]]], result)

        @builtins.property
        def tags(
            self,
        ) -> typing.Optional[typing.List["CfnAssociation.KeyValuePairProperty"]]:
            '''List of tags as key-value pairs, used to identify resources for topology crawl.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-association-sourceawsconfiguration.html#cfn-devopsagent-association-sourceawsconfiguration-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List["CfnAssociation.KeyValuePairProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceAwsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devopsagent.CfnAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_space_id": "agentSpaceId",
        "configuration": "configuration",
        "service_id": "serviceId",
        "linked_association_ids": "linkedAssociationIds",
    },
)
class CfnAssociationProps:
    def __init__(
        self,
        *,
        agent_space_id: builtins.str,
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAssociation.ServiceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        service_id: builtins.str,
        linked_association_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAssociation``.

        :param agent_space_id: The unique identifier of the Agent Space.
        :param configuration: The configuration that directs how the Agent Space interacts with the given service. You can specify only one configuration type per association. *Allowed Values* : ``SourceAws`` | ``Aws`` | ``GitHub`` | ``GitLab`` | ``Slack`` | ``Dynatrace`` | ``ServiceNow`` | ``MCPServer`` | ``MCPServerNewRelic`` | ``MCPServerDatadog`` | ``MCPServerSplunk`` | ``EventChannel``
        :param service_id: The identifier for the associated service. For ``SourceAws`` and ``Aws`` configurations, this must be ``aws`` . For all other service types, this is a UUID generated from the RegisterService command.
        :param linked_association_ids: Set of linked association IDs for parent-child relationships.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-association.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devopsagent as devopsagent
            
            # resource_metadata: Any
            
            cfn_association_props = devopsagent.CfnAssociationProps(
                agent_space_id="agentSpaceId",
                configuration=devopsagent.CfnAssociation.ServiceConfigurationProperty(
                    aws=devopsagent.CfnAssociation.AWSConfigurationProperty(
                        account_id="accountId",
                        account_type="accountType",
                        assumable_role_arn="assumableRoleArn",
            
                        # the properties below are optional
                        resources=[devopsagent.CfnAssociation.AWSResourceProperty(
                            resource_arn="resourceArn",
            
                            # the properties below are optional
                            resource_metadata=resource_metadata,
                            resource_type="resourceType"
                        )],
                        tags=[devopsagent.CfnAssociation.KeyValuePairProperty(
                            key="key",
                            value="value"
                        )]
                    ),
                    dynatrace=devopsagent.CfnAssociation.DynatraceConfigurationProperty(
                        env_id="envId",
            
                        # the properties below are optional
                        enable_webhook_updates=False,
                        resources=["resources"]
                    ),
                    event_channel=devopsagent.CfnAssociation.EventChannelConfigurationProperty(
                        enable_webhook_updates=False
                    ),
                    git_hub=devopsagent.CfnAssociation.GitHubConfigurationProperty(
                        owner="owner",
                        owner_type="ownerType",
                        repo_id="repoId",
                        repo_name="repoName"
                    ),
                    git_lab=devopsagent.CfnAssociation.GitLabConfigurationProperty(
                        project_id="projectId",
                        project_path="projectPath",
            
                        # the properties below are optional
                        enable_webhook_updates=False,
                        instance_identifier="instanceIdentifier"
                    ),
                    mcp_server=devopsagent.CfnAssociation.MCPServerConfigurationProperty(
                        endpoint="endpoint",
                        name="name",
                        tools=["tools"],
            
                        # the properties below are optional
                        description="description",
                        enable_webhook_updates=False
                    ),
                    mcp_server_datadog=devopsagent.CfnAssociation.MCPServerDatadogConfigurationProperty(
                        endpoint="endpoint",
                        name="name",
            
                        # the properties below are optional
                        description="description",
                        enable_webhook_updates=False
                    ),
                    mcp_server_new_relic=devopsagent.CfnAssociation.MCPServerNewRelicConfigurationProperty(
                        account_id="accountId",
                        endpoint="endpoint"
                    ),
                    mcp_server_splunk=devopsagent.CfnAssociation.MCPServerSplunkConfigurationProperty(
                        endpoint="endpoint",
                        name="name",
            
                        # the properties below are optional
                        description="description",
                        enable_webhook_updates=False
                    ),
                    service_now=devopsagent.CfnAssociation.ServiceNowConfigurationProperty(
                        enable_webhook_updates=False,
                        instance_id="instanceId"
                    ),
                    slack=devopsagent.CfnAssociation.SlackConfigurationProperty(
                        transmission_target=devopsagent.CfnAssociation.SlackTransmissionTargetProperty(
                            incident_response_target=devopsagent.CfnAssociation.SlackChannelProperty(
                                channel_id="channelId",
            
                                # the properties below are optional
                                channel_name="channelName"
                            )
                        ),
                        workspace_id="workspaceId",
                        workspace_name="workspaceName"
                    ),
                    source_aws=devopsagent.CfnAssociation.SourceAwsConfigurationProperty(
                        account_id="accountId",
                        account_type="accountType",
                        assumable_role_arn="assumableRoleArn",
            
                        # the properties below are optional
                        resources=[devopsagent.CfnAssociation.AWSResourceProperty(
                            resource_arn="resourceArn",
            
                            # the properties below are optional
                            resource_metadata=resource_metadata,
                            resource_type="resourceType"
                        )],
                        tags=[devopsagent.CfnAssociation.KeyValuePairProperty(
                            key="key",
                            value="value"
                        )]
                    )
                ),
                service_id="serviceId",
            
                # the properties below are optional
                linked_association_ids=["linkedAssociationIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b9c7866e61a4a7267964c2e97d2c2f23071408ae1546eca41521d60b1273549)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
            check_type(argname="argument linked_association_ids", value=linked_association_ids, expected_type=type_hints["linked_association_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
            "configuration": configuration,
            "service_id": service_id,
        }
        if linked_association_ids is not None:
            self._values["linked_association_ids"] = linked_association_ids

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The unique identifier of the Agent Space.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-association.html#cfn-devopsagent-association-agentspaceid
        '''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnAssociation.ServiceConfigurationProperty"]:
        '''The configuration that directs how the Agent Space interacts with the given service.

        You can specify only one configuration type per association.

        *Allowed Values* : ``SourceAws`` | ``Aws`` | ``GitHub`` | ``GitLab`` | ``Slack`` | ``Dynatrace`` | ``ServiceNow`` | ``MCPServer`` | ``MCPServerNewRelic`` | ``MCPServerDatadog`` | ``MCPServerSplunk`` | ``EventChannel``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-association.html#cfn-devopsagent-association-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAssociation.ServiceConfigurationProperty"], result)

    @builtins.property
    def service_id(self) -> builtins.str:
        '''The identifier for the associated service.

        For ``SourceAws`` and ``Aws`` configurations, this must be ``aws`` . For all other service types, this is a UUID generated from the RegisterService command.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-association.html#cfn-devopsagent-association-serviceid
        '''
        result = self._values.get("service_id")
        assert result is not None, "Required property 'service_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def linked_association_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Set of linked association IDs for parent-child relationships.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-association.html#cfn-devopsagent-association-linkedassociationids
        '''
        result = self._values.get("linked_association_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IServiceRef_a4cfa131)
class CfnService(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_devopsagent.CfnService",
):
    '''The AWS::DevOpsAgent::Service resource registers external services (like Dynatrace, MCP servers, GitLab) for integration with DevOpsAgent.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-service.html
    :cloudformationResource: AWS::DevOpsAgent::Service
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_devopsagent as devopsagent
        
        # exchange_parameters: Any
        
        cfn_service = devopsagent.CfnService(self, "MyCfnService",
            service_type="serviceType",
        
            # the properties below are optional
            service_details=devopsagent.CfnService.ServiceDetailsProperty(
                dynatrace=devopsagent.CfnService.DynatraceServiceDetailsProperty(
                    account_urn="accountUrn",
        
                    # the properties below are optional
                    authorization_config=devopsagent.CfnService.DynatraceAuthorizationConfigProperty(
                        o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
        
                            # the properties below are optional
                            client_name="clientName",
                            exchange_parameters=exchange_parameters
                        )
                    )
                ),
                git_lab=devopsagent.CfnService.GitLabDetailsProperty(
                    target_url="targetUrl",
                    token_type="tokenType",
                    token_value="tokenValue",
        
                    # the properties below are optional
                    group_id="groupId"
                ),
                mcp_server=devopsagent.CfnService.MCPServerDetailsProperty(
                    authorization_config=devopsagent.CfnService.MCPServerAuthorizationConfigProperty(
                        api_key=devopsagent.CfnService.ApiKeyDetailsProperty(
                            api_key_header="apiKeyHeader",
                            api_key_name="apiKeyName",
                            api_key_value="apiKeyValue"
                        ),
                        o_auth_client_credentials=devopsagent.CfnService.MCPServerOAuthClientCredentialsConfigProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
                            exchange_url="exchangeUrl",
        
                            # the properties below are optional
                            client_name="clientName",
                            exchange_parameters=exchange_parameters,
                            scopes=["scopes"]
                        )
                    ),
                    endpoint="endpoint",
                    name="name",
        
                    # the properties below are optional
                    description="description"
                ),
                mcp_server_new_relic=devopsagent.CfnService.NewRelicServiceDetailsProperty(
                    authorization_config=devopsagent.CfnService.NewRelicAuthorizationConfigProperty(
                        api_key=devopsagent.CfnService.NewRelicApiKeyConfigProperty(
                            account_id="accountId",
                            api_key="apiKey",
                            region="region",
        
                            # the properties below are optional
                            alert_policy_ids=["alertPolicyIds"],
                            application_ids=["applicationIds"],
                            entity_guids=["entityGuids"]
                        )
                    )
                ),
                mcp_server_splunk=devopsagent.CfnService.MCPServerSplunkDetailsProperty(
                    authorization_config=devopsagent.CfnService.MCPServerSplunkAuthorizationConfigProperty(
                        bearer_token=devopsagent.CfnService.BearerTokenDetailsProperty(
                            token_name="tokenName",
                            token_value="tokenValue",
        
                            # the properties below are optional
                            authorization_header="authorizationHeader"
                        )
                    ),
                    endpoint="endpoint",
                    name="name",
        
                    # the properties below are optional
                    description="description"
                ),
                service_now=devopsagent.CfnService.ServiceNowServiceDetailsProperty(
                    instance_url="instanceUrl",
        
                    # the properties below are optional
                    authorization_config=devopsagent.CfnService.ServiceNowAuthorizationConfigProperty(
                        o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
        
                            # the properties below are optional
                            client_name="clientName",
                            exchange_parameters=exchange_parameters
                        )
                    )
                )
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        service_type: builtins.str,
        service_details: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.ServiceDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DevOpsAgent::Service``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param service_type: The type of service being registered.
        :param service_details: Service-specific configuration details.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76700bf71c0ca9d7d21edc970f56dd1c8a41f67b248c3228096feb30580cca07)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceProps(
            service_type=service_type, service_details=service_details
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnService")
    @builtins.classmethod
    def is_cfn_service(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnService.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4747cf77eaeb36736a2ca00fd2ce576b093ee7f10e64c38001e2eac5a33d8149)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnService", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae6a60e2418d472a473b14d2bbcbd2350af8fed2083a2938616370c1e08ed3e0)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2740d5b9657545f92bc9b54f5c97b22d107226f26deef1c36cbd652d62b9aba0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccessibleResources")
    def attr_accessible_resources(self) -> "_IResolvable_da3f097b":
        '''List of accessible resources for this service.

        :cloudformationAttribute: AccessibleResources
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrAccessibleResources"))

    @builtins.property
    @jsii.member(jsii_name="attrAdditionalServiceDetails")
    def attr_additional_service_details(self) -> "_IResolvable_da3f097b":
        '''Additional details specific to the service type returned after registration.

        :cloudformationAttribute: AdditionalServiceDetails
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrAdditionalServiceDetails"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceId")
    def attr_service_id(self) -> builtins.str:
        '''The unique identifier of the service.

        :cloudformationAttribute: ServiceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "_ServiceReference_cb07f28f":
        '''A reference to a Service resource.'''
        return typing.cast("_ServiceReference_cb07f28f", jsii.get(self, "serviceRef"))

    @builtins.property
    @jsii.member(jsii_name="serviceType")
    def service_type(self) -> builtins.str:
        '''The type of service being registered.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceType"))

    @service_type.setter
    def service_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a87d815016e64b5bdf47334ae0b9ef194602b4aa5a9e6cd5a5d9b1d6b516b9a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serviceDetails")
    def service_details(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ServiceDetailsProperty"]]:
        '''Service-specific configuration details.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ServiceDetailsProperty"]], jsii.get(self, "serviceDetails"))

    @service_details.setter
    def service_details(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ServiceDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38b28b2539546ba11e45199a6bde41e432e6246da9ea58bba29ece3bbf5c4193)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceDetails", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.AdditionalServiceDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dynatrace": "dynatrace",
            "git_lab": "gitLab",
            "mcp_server": "mcpServer",
            "mcp_server_new_relic": "mcpServerNewRelic",
            "mcp_server_splunk": "mcpServerSplunk",
            "service_now": "serviceNow",
        },
    )
    class AdditionalServiceDetailsProperty:
        def __init__(
            self,
            *,
            dynatrace: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.RegisteredDynatraceDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            git_lab: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.RegisteredGitLabServiceDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.RegisteredMCPServerDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server_new_relic: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.RegisteredNewRelicDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server_splunk: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.RegisteredMCPServerDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_now: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.RegisteredServiceNowDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param dynatrace: Dynatrace service details returned after registration.
            :param git_lab: GitLab service details returned after registration.
            :param mcp_server: MCP server details returned after registration.
            :param mcp_server_new_relic: New Relic service details returned after registration.
            :param mcp_server_splunk: MCP server details returned after registration.
            :param service_now: ServiceNow service details returned after registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-additionalservicedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                additional_service_details_property = devopsagent.CfnService.AdditionalServiceDetailsProperty(
                    dynatrace=devopsagent.CfnService.RegisteredDynatraceDetailsProperty(
                        account_urn="accountUrn"
                    ),
                    git_lab=devopsagent.CfnService.RegisteredGitLabServiceDetailsProperty(
                        target_url="targetUrl",
                        token_type="tokenType",
                
                        # the properties below are optional
                        group_id="groupId"
                    ),
                    mcp_server=devopsagent.CfnService.RegisteredMCPServerDetailsProperty(
                        authorization_method="authorizationMethod",
                        endpoint="endpoint",
                        name="name",
                
                        # the properties below are optional
                        api_key_header="apiKeyHeader",
                        description="description"
                    ),
                    mcp_server_new_relic=devopsagent.CfnService.RegisteredNewRelicDetailsProperty(
                        account_id="accountId",
                        region="region",
                
                        # the properties below are optional
                        description="description"
                    ),
                    mcp_server_splunk=devopsagent.CfnService.RegisteredMCPServerDetailsProperty(
                        authorization_method="authorizationMethod",
                        endpoint="endpoint",
                        name="name",
                
                        # the properties below are optional
                        api_key_header="apiKeyHeader",
                        description="description"
                    ),
                    service_now=devopsagent.CfnService.RegisteredServiceNowDetailsProperty(
                        instance_url="instanceUrl"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35d2aa127fac97efcf9f5ae815fbac6244f4de11a1b85beb8acc053b8eb8edee)
                check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
                check_type(argname="argument git_lab", value=git_lab, expected_type=type_hints["git_lab"])
                check_type(argname="argument mcp_server", value=mcp_server, expected_type=type_hints["mcp_server"])
                check_type(argname="argument mcp_server_new_relic", value=mcp_server_new_relic, expected_type=type_hints["mcp_server_new_relic"])
                check_type(argname="argument mcp_server_splunk", value=mcp_server_splunk, expected_type=type_hints["mcp_server_splunk"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dynatrace is not None:
                self._values["dynatrace"] = dynatrace
            if git_lab is not None:
                self._values["git_lab"] = git_lab
            if mcp_server is not None:
                self._values["mcp_server"] = mcp_server
            if mcp_server_new_relic is not None:
                self._values["mcp_server_new_relic"] = mcp_server_new_relic
            if mcp_server_splunk is not None:
                self._values["mcp_server_splunk"] = mcp_server_splunk
            if service_now is not None:
                self._values["service_now"] = service_now

        @builtins.property
        def dynatrace(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredDynatraceDetailsProperty"]]:
            '''Dynatrace service details returned after registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-additionalservicedetails.html#cfn-devopsagent-service-additionalservicedetails-dynatrace
            '''
            result = self._values.get("dynatrace")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredDynatraceDetailsProperty"]], result)

        @builtins.property
        def git_lab(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredGitLabServiceDetailsProperty"]]:
            '''GitLab service details returned after registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-additionalservicedetails.html#cfn-devopsagent-service-additionalservicedetails-gitlab
            '''
            result = self._values.get("git_lab")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredGitLabServiceDetailsProperty"]], result)

        @builtins.property
        def mcp_server(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredMCPServerDetailsProperty"]]:
            '''MCP server details returned after registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-additionalservicedetails.html#cfn-devopsagent-service-additionalservicedetails-mcpserver
            '''
            result = self._values.get("mcp_server")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredMCPServerDetailsProperty"]], result)

        @builtins.property
        def mcp_server_new_relic(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredNewRelicDetailsProperty"]]:
            '''New Relic service details returned after registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-additionalservicedetails.html#cfn-devopsagent-service-additionalservicedetails-mcpservernewrelic
            '''
            result = self._values.get("mcp_server_new_relic")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredNewRelicDetailsProperty"]], result)

        @builtins.property
        def mcp_server_splunk(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredMCPServerDetailsProperty"]]:
            '''MCP server details returned after registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-additionalservicedetails.html#cfn-devopsagent-service-additionalservicedetails-mcpserversplunk
            '''
            result = self._values.get("mcp_server_splunk")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredMCPServerDetailsProperty"]], result)

        @builtins.property
        def service_now(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredServiceNowDetailsProperty"]]:
            '''ServiceNow service details returned after registration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-additionalservicedetails.html#cfn-devopsagent-service-additionalservicedetails-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.RegisteredServiceNowDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdditionalServiceDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.ApiKeyDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "api_key_header": "apiKeyHeader",
            "api_key_name": "apiKeyName",
            "api_key_value": "apiKeyValue",
        },
    )
    class ApiKeyDetailsProperty:
        def __init__(
            self,
            *,
            api_key_header: builtins.str,
            api_key_name: builtins.str,
            api_key_value: builtins.str,
        ) -> None:
            '''API key authentication details.

            :param api_key_header: HTTP header name to send the API key.
            :param api_key_name: User friendly API key name.
            :param api_key_value: API key value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-apikeydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                api_key_details_property = devopsagent.CfnService.ApiKeyDetailsProperty(
                    api_key_header="apiKeyHeader",
                    api_key_name="apiKeyName",
                    api_key_value="apiKeyValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76e209fab46047902f46ddb19cd603ac6794e4e730c2326df60b5016370583cf)
                check_type(argname="argument api_key_header", value=api_key_header, expected_type=type_hints["api_key_header"])
                check_type(argname="argument api_key_name", value=api_key_name, expected_type=type_hints["api_key_name"])
                check_type(argname="argument api_key_value", value=api_key_value, expected_type=type_hints["api_key_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_key_header": api_key_header,
                "api_key_name": api_key_name,
                "api_key_value": api_key_value,
            }

        @builtins.property
        def api_key_header(self) -> builtins.str:
            '''HTTP header name to send the API key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-apikeydetails.html#cfn-devopsagent-service-apikeydetails-apikeyheader
            '''
            result = self._values.get("api_key_header")
            assert result is not None, "Required property 'api_key_header' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def api_key_name(self) -> builtins.str:
            '''User friendly API key name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-apikeydetails.html#cfn-devopsagent-service-apikeydetails-apikeyname
            '''
            result = self._values.get("api_key_name")
            assert result is not None, "Required property 'api_key_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def api_key_value(self) -> builtins.str:
            '''API key value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-apikeydetails.html#cfn-devopsagent-service-apikeydetails-apikeyvalue
            '''
            result = self._values.get("api_key_value")
            assert result is not None, "Required property 'api_key_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiKeyDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.BearerTokenDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "token_name": "tokenName",
            "token_value": "tokenValue",
            "authorization_header": "authorizationHeader",
        },
    )
    class BearerTokenDetailsProperty:
        def __init__(
            self,
            *,
            token_name: builtins.str,
            token_value: builtins.str,
            authorization_header: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Bearer token authentication details.

            :param token_name: User friendly bearer token name.
            :param token_value: Bearer token value.
            :param authorization_header: HTTP header name to send the bearer token. Default: - "Authorization"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-bearertokendetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                bearer_token_details_property = devopsagent.CfnService.BearerTokenDetailsProperty(
                    token_name="tokenName",
                    token_value="tokenValue",
                
                    # the properties below are optional
                    authorization_header="authorizationHeader"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b1ed3f342895156ff05fa55fe762ca658173862cfba9138b08506eef2da17f21)
                check_type(argname="argument token_name", value=token_name, expected_type=type_hints["token_name"])
                check_type(argname="argument token_value", value=token_value, expected_type=type_hints["token_value"])
                check_type(argname="argument authorization_header", value=authorization_header, expected_type=type_hints["authorization_header"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "token_name": token_name,
                "token_value": token_value,
            }
            if authorization_header is not None:
                self._values["authorization_header"] = authorization_header

        @builtins.property
        def token_name(self) -> builtins.str:
            '''User friendly bearer token name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-bearertokendetails.html#cfn-devopsagent-service-bearertokendetails-tokenname
            '''
            result = self._values.get("token_name")
            assert result is not None, "Required property 'token_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def token_value(self) -> builtins.str:
            '''Bearer token value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-bearertokendetails.html#cfn-devopsagent-service-bearertokendetails-tokenvalue
            '''
            result = self._values.get("token_value")
            assert result is not None, "Required property 'token_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authorization_header(self) -> typing.Optional[builtins.str]:
            '''HTTP header name to send the bearer token.

            :default: - "Authorization"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-bearertokendetails.html#cfn-devopsagent-service-bearertokendetails-authorizationheader
            '''
            result = self._values.get("authorization_header")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BearerTokenDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.DynatraceAuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"o_auth_client_credentials": "oAuthClientCredentials"},
    )
    class DynatraceAuthorizationConfigProperty:
        def __init__(
            self,
            *,
            o_auth_client_credentials: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.OAuthClientDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Dynatrace OAuth authorization configuration.

            :param o_auth_client_credentials: OAuth client credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-dynatraceauthorizationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # exchange_parameters: Any
                
                dynatrace_authorization_config_property = devopsagent.CfnService.DynatraceAuthorizationConfigProperty(
                    o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
                
                        # the properties below are optional
                        client_name="clientName",
                        exchange_parameters=exchange_parameters
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d4c94d9ef2811300fc8439f749f5e0b012380780ff3ee8da59d63a89012981e4)
                check_type(argname="argument o_auth_client_credentials", value=o_auth_client_credentials, expected_type=type_hints["o_auth_client_credentials"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if o_auth_client_credentials is not None:
                self._values["o_auth_client_credentials"] = o_auth_client_credentials

        @builtins.property
        def o_auth_client_credentials(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.OAuthClientDetailsProperty"]]:
            '''OAuth client credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-dynatraceauthorizationconfig.html#cfn-devopsagent-service-dynatraceauthorizationconfig-oauthclientcredentials
            '''
            result = self._values.get("o_auth_client_credentials")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.OAuthClientDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynatraceAuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.DynatraceServiceDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_urn": "accountUrn",
            "authorization_config": "authorizationConfig",
        },
    )
    class DynatraceServiceDetailsProperty:
        def __init__(
            self,
            *,
            account_urn: builtins.str,
            authorization_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.DynatraceAuthorizationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Dynatrace service configuration.

            :param account_urn: Dynatrace resource account URN.
            :param authorization_config: Dynatrace OAuth authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-dynatraceservicedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # exchange_parameters: Any
                
                dynatrace_service_details_property = devopsagent.CfnService.DynatraceServiceDetailsProperty(
                    account_urn="accountUrn",
                
                    # the properties below are optional
                    authorization_config=devopsagent.CfnService.DynatraceAuthorizationConfigProperty(
                        o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
                
                            # the properties below are optional
                            client_name="clientName",
                            exchange_parameters=exchange_parameters
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1093f5ca4a6437d94226499a72d7ed498cbf6c82d31179c14e9526707fa4f8c0)
                check_type(argname="argument account_urn", value=account_urn, expected_type=type_hints["account_urn"])
                check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_urn": account_urn,
            }
            if authorization_config is not None:
                self._values["authorization_config"] = authorization_config

        @builtins.property
        def account_urn(self) -> builtins.str:
            '''Dynatrace resource account URN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-dynatraceservicedetails.html#cfn-devopsagent-service-dynatraceservicedetails-accounturn
            '''
            result = self._values.get("account_urn")
            assert result is not None, "Required property 'account_urn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.DynatraceAuthorizationConfigProperty"]]:
            '''Dynatrace OAuth authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-dynatraceservicedetails.html#cfn-devopsagent-service-dynatraceservicedetails-authorizationconfig
            '''
            result = self._values.get("authorization_config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.DynatraceAuthorizationConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynatraceServiceDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.GitLabDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_url": "targetUrl",
            "token_type": "tokenType",
            "token_value": "tokenValue",
            "group_id": "groupId",
        },
    )
    class GitLabDetailsProperty:
        def __init__(
            self,
            *,
            target_url: builtins.str,
            token_type: builtins.str,
            token_value: builtins.str,
            group_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''GitLab service configuration.

            :param target_url: GitLab instance URL.
            :param token_type: Type of GitLab access token.
            :param token_value: GitLab access token value.
            :param group_id: Optional GitLab group ID for group-level access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-gitlabdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                git_lab_details_property = devopsagent.CfnService.GitLabDetailsProperty(
                    target_url="targetUrl",
                    token_type="tokenType",
                    token_value="tokenValue",
                
                    # the properties below are optional
                    group_id="groupId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6b58d9276d7725a7b2a814720d881a8dd974b0d85b18fe425efb863bc1d25a08)
                check_type(argname="argument target_url", value=target_url, expected_type=type_hints["target_url"])
                check_type(argname="argument token_type", value=token_type, expected_type=type_hints["token_type"])
                check_type(argname="argument token_value", value=token_value, expected_type=type_hints["token_value"])
                check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_url": target_url,
                "token_type": token_type,
                "token_value": token_value,
            }
            if group_id is not None:
                self._values["group_id"] = group_id

        @builtins.property
        def target_url(self) -> builtins.str:
            '''GitLab instance URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-gitlabdetails.html#cfn-devopsagent-service-gitlabdetails-targeturl
            '''
            result = self._values.get("target_url")
            assert result is not None, "Required property 'target_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def token_type(self) -> builtins.str:
            '''Type of GitLab access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-gitlabdetails.html#cfn-devopsagent-service-gitlabdetails-tokentype
            '''
            result = self._values.get("token_type")
            assert result is not None, "Required property 'token_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def token_value(self) -> builtins.str:
            '''GitLab access token value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-gitlabdetails.html#cfn-devopsagent-service-gitlabdetails-tokenvalue
            '''
            result = self._values.get("token_value")
            assert result is not None, "Required property 'token_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_id(self) -> typing.Optional[builtins.str]:
            '''Optional GitLab group ID for group-level access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-gitlabdetails.html#cfn-devopsagent-service-gitlabdetails-groupid
            '''
            result = self._values.get("group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GitLabDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.MCPServerAuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "api_key": "apiKey",
            "o_auth_client_credentials": "oAuthClientCredentials",
        },
    )
    class MCPServerAuthorizationConfigProperty:
        def __init__(
            self,
            *,
            api_key: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.ApiKeyDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            o_auth_client_credentials: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.MCPServerOAuthClientCredentialsConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param api_key: API key authentication details.
            :param o_auth_client_credentials: MCP server OAuth client credentials configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserverauthorizationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # exchange_parameters: Any
                
                m_cPServer_authorization_config_property = devopsagent.CfnService.MCPServerAuthorizationConfigProperty(
                    api_key=devopsagent.CfnService.ApiKeyDetailsProperty(
                        api_key_header="apiKeyHeader",
                        api_key_name="apiKeyName",
                        api_key_value="apiKeyValue"
                    ),
                    o_auth_client_credentials=devopsagent.CfnService.MCPServerOAuthClientCredentialsConfigProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
                        exchange_url="exchangeUrl",
                
                        # the properties below are optional
                        client_name="clientName",
                        exchange_parameters=exchange_parameters,
                        scopes=["scopes"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d23407dd8b2083d432d8db1552b2c86a3325b7151f0c72016ef6edc6a6fd65e8)
                check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
                check_type(argname="argument o_auth_client_credentials", value=o_auth_client_credentials, expected_type=type_hints["o_auth_client_credentials"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if api_key is not None:
                self._values["api_key"] = api_key
            if o_auth_client_credentials is not None:
                self._values["o_auth_client_credentials"] = o_auth_client_credentials

        @builtins.property
        def api_key(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ApiKeyDetailsProperty"]]:
            '''API key authentication details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserverauthorizationconfig.html#cfn-devopsagent-service-mcpserverauthorizationconfig-apikey
            '''
            result = self._values.get("api_key")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ApiKeyDetailsProperty"]], result)

        @builtins.property
        def o_auth_client_credentials(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerOAuthClientCredentialsConfigProperty"]]:
            '''MCP server OAuth client credentials configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserverauthorizationconfig.html#cfn-devopsagent-service-mcpserverauthorizationconfig-oauthclientcredentials
            '''
            result = self._values.get("o_auth_client_credentials")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerOAuthClientCredentialsConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPServerAuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.MCPServerDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_config": "authorizationConfig",
            "endpoint": "endpoint",
            "name": "name",
            "description": "description",
        },
    )
    class MCPServerDetailsProperty:
        def __init__(
            self,
            *,
            authorization_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.MCPServerAuthorizationConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            endpoint: builtins.str,
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''MCP server configuration.

            :param authorization_config: MCP server authorization configuration.
            :param endpoint: MCP server endpoint URL.
            :param name: MCP server name.
            :param description: Optional description for the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserverdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # exchange_parameters: Any
                
                m_cPServer_details_property = devopsagent.CfnService.MCPServerDetailsProperty(
                    authorization_config=devopsagent.CfnService.MCPServerAuthorizationConfigProperty(
                        api_key=devopsagent.CfnService.ApiKeyDetailsProperty(
                            api_key_header="apiKeyHeader",
                            api_key_name="apiKeyName",
                            api_key_value="apiKeyValue"
                        ),
                        o_auth_client_credentials=devopsagent.CfnService.MCPServerOAuthClientCredentialsConfigProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
                            exchange_url="exchangeUrl",
                
                            # the properties below are optional
                            client_name="clientName",
                            exchange_parameters=exchange_parameters,
                            scopes=["scopes"]
                        )
                    ),
                    endpoint="endpoint",
                    name="name",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8254611fd4c93bda748b35259025cc559c3ff3316f16d3a4c6b8742407842e77)
                check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorization_config": authorization_config,
                "endpoint": endpoint,
                "name": name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerAuthorizationConfigProperty"]:
            '''MCP server authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserverdetails.html#cfn-devopsagent-service-mcpserverdetails-authorizationconfig
            '''
            result = self._values.get("authorization_config")
            assert result is not None, "Required property 'authorization_config' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerAuthorizationConfigProperty"], result)

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''MCP server endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserverdetails.html#cfn-devopsagent-service-mcpserverdetails-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''MCP server name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserverdetails.html#cfn-devopsagent-service-mcpserverdetails-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''Optional description for the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserverdetails.html#cfn-devopsagent-service-mcpserverdetails-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPServerDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.MCPServerOAuthClientCredentialsConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "exchange_url": "exchangeUrl",
            "client_name": "clientName",
            "exchange_parameters": "exchangeParameters",
            "scopes": "scopes",
        },
    )
    class MCPServerOAuthClientCredentialsConfigProperty:
        def __init__(
            self,
            *,
            client_id: builtins.str,
            client_secret: builtins.str,
            exchange_url: builtins.str,
            client_name: typing.Optional[builtins.str] = None,
            exchange_parameters: typing.Any = None,
            scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''MCP server OAuth client credentials configuration.

            :param client_id: OAuth client ID.
            :param client_secret: OAuth client secret.
            :param exchange_url: OAuth token exchange URL.
            :param client_name: User friendly OAuth client name.
            :param exchange_parameters: OAuth token exchange parameters.
            :param scopes: OAuth scopes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # exchange_parameters: Any
                
                m_cPServer_oAuth_client_credentials_config_property = devopsagent.CfnService.MCPServerOAuthClientCredentialsConfigProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                    exchange_url="exchangeUrl",
                
                    # the properties below are optional
                    client_name="clientName",
                    exchange_parameters=exchange_parameters,
                    scopes=["scopes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__198a110da941ce87aaecb0a0b1ba18fa10731b81d29b4a768fd8f795ff2b76f5)
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument exchange_url", value=exchange_url, expected_type=type_hints["exchange_url"])
                check_type(argname="argument client_name", value=client_name, expected_type=type_hints["client_name"])
                check_type(argname="argument exchange_parameters", value=exchange_parameters, expected_type=type_hints["exchange_parameters"])
                check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_id": client_id,
                "client_secret": client_secret,
                "exchange_url": exchange_url,
            }
            if client_name is not None:
                self._values["client_name"] = client_name
            if exchange_parameters is not None:
                self._values["exchange_parameters"] = exchange_parameters
            if scopes is not None:
                self._values["scopes"] = scopes

        @builtins.property
        def client_id(self) -> builtins.str:
            '''OAuth client ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig.html#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientid
            '''
            result = self._values.get("client_id")
            assert result is not None, "Required property 'client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_secret(self) -> builtins.str:
            '''OAuth client secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig.html#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientsecret
            '''
            result = self._values.get("client_secret")
            assert result is not None, "Required property 'client_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def exchange_url(self) -> builtins.str:
            '''OAuth token exchange URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig.html#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-exchangeurl
            '''
            result = self._values.get("exchange_url")
            assert result is not None, "Required property 'exchange_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_name(self) -> typing.Optional[builtins.str]:
            '''User friendly OAuth client name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig.html#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-clientname
            '''
            result = self._values.get("client_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exchange_parameters(self) -> typing.Any:
            '''OAuth token exchange parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig.html#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-exchangeparameters
            '''
            result = self._values.get("exchange_parameters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''OAuth scopes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserveroauthclientcredentialsconfig.html#cfn-devopsagent-service-mcpserveroauthclientcredentialsconfig-scopes
            '''
            result = self._values.get("scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPServerOAuthClientCredentialsConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.MCPServerSplunkAuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"bearer_token": "bearerToken"},
    )
    class MCPServerSplunkAuthorizationConfigProperty:
        def __init__(
            self,
            *,
            bearer_token: typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.BearerTokenDetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''MCP server splunk authorization configuration.

            :param bearer_token: Bearer token authentication details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserversplunkauthorizationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                m_cPServer_splunk_authorization_config_property = devopsagent.CfnService.MCPServerSplunkAuthorizationConfigProperty(
                    bearer_token=devopsagent.CfnService.BearerTokenDetailsProperty(
                        token_name="tokenName",
                        token_value="tokenValue",
                
                        # the properties below are optional
                        authorization_header="authorizationHeader"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c92e97e3c227e3467ecb452f408839f30cb1b85644fbd8f96962ea3606723a1)
                check_type(argname="argument bearer_token", value=bearer_token, expected_type=type_hints["bearer_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bearer_token": bearer_token,
            }

        @builtins.property
        def bearer_token(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnService.BearerTokenDetailsProperty"]:
            '''Bearer token authentication details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserversplunkauthorizationconfig.html#cfn-devopsagent-service-mcpserversplunkauthorizationconfig-bearertoken
            '''
            result = self._values.get("bearer_token")
            assert result is not None, "Required property 'bearer_token' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnService.BearerTokenDetailsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPServerSplunkAuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.MCPServerSplunkDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_config": "authorizationConfig",
            "endpoint": "endpoint",
            "name": "name",
            "description": "description",
        },
    )
    class MCPServerSplunkDetailsProperty:
        def __init__(
            self,
            *,
            authorization_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.MCPServerSplunkAuthorizationConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            endpoint: builtins.str,
            name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Splunk MCP server configuration.

            :param authorization_config: MCP server splunk authorization configuration.
            :param endpoint: MCP server endpoint URL.
            :param name: MCP server name.
            :param description: Optional description for the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserversplunkdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                m_cPServer_splunk_details_property = devopsagent.CfnService.MCPServerSplunkDetailsProperty(
                    authorization_config=devopsagent.CfnService.MCPServerSplunkAuthorizationConfigProperty(
                        bearer_token=devopsagent.CfnService.BearerTokenDetailsProperty(
                            token_name="tokenName",
                            token_value="tokenValue",
                
                            # the properties below are optional
                            authorization_header="authorizationHeader"
                        )
                    ),
                    endpoint="endpoint",
                    name="name",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__53d93e87f0f22c03aa42a187eee24ad101676f59eb3e0ca8d617001ea054e7d1)
                check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorization_config": authorization_config,
                "endpoint": endpoint,
                "name": name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerSplunkAuthorizationConfigProperty"]:
            '''MCP server splunk authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserversplunkdetails.html#cfn-devopsagent-service-mcpserversplunkdetails-authorizationconfig
            '''
            result = self._values.get("authorization_config")
            assert result is not None, "Required property 'authorization_config' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerSplunkAuthorizationConfigProperty"], result)

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''MCP server endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserversplunkdetails.html#cfn-devopsagent-service-mcpserversplunkdetails-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''MCP server name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserversplunkdetails.html#cfn-devopsagent-service-mcpserversplunkdetails-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''Optional description for the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-mcpserversplunkdetails.html#cfn-devopsagent-service-mcpserversplunkdetails-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPServerSplunkDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.NewRelicApiKeyConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "api_key": "apiKey",
            "region": "region",
            "alert_policy_ids": "alertPolicyIds",
            "application_ids": "applicationIds",
            "entity_guids": "entityGuids",
        },
    )
    class NewRelicApiKeyConfigProperty:
        def __init__(
            self,
            *,
            account_id: builtins.str,
            api_key: builtins.str,
            region: builtins.str,
            alert_policy_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            application_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''New Relic API key configuration.

            :param account_id: New Relic Account ID.
            :param api_key: New Relic User API Key.
            :param region: New Relic region.
            :param alert_policy_ids: List of alert policy IDs.
            :param application_ids: List of monitored APM application IDs.
            :param entity_guids: List of globally unique IDs for New Relic resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicapikeyconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                new_relic_api_key_config_property = devopsagent.CfnService.NewRelicApiKeyConfigProperty(
                    account_id="accountId",
                    api_key="apiKey",
                    region="region",
                
                    # the properties below are optional
                    alert_policy_ids=["alertPolicyIds"],
                    application_ids=["applicationIds"],
                    entity_guids=["entityGuids"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4540b44ec165187fba7151d272d0adb7a00d610661a528aea957f435fc7864dd)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument alert_policy_ids", value=alert_policy_ids, expected_type=type_hints["alert_policy_ids"])
                check_type(argname="argument application_ids", value=application_ids, expected_type=type_hints["application_ids"])
                check_type(argname="argument entity_guids", value=entity_guids, expected_type=type_hints["entity_guids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_id": account_id,
                "api_key": api_key,
                "region": region,
            }
            if alert_policy_ids is not None:
                self._values["alert_policy_ids"] = alert_policy_ids
            if application_ids is not None:
                self._values["application_ids"] = application_ids
            if entity_guids is not None:
                self._values["entity_guids"] = entity_guids

        @builtins.property
        def account_id(self) -> builtins.str:
            '''New Relic Account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicapikeyconfig.html#cfn-devopsagent-service-newrelicapikeyconfig-accountid
            '''
            result = self._values.get("account_id")
            assert result is not None, "Required property 'account_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def api_key(self) -> builtins.str:
            '''New Relic User API Key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicapikeyconfig.html#cfn-devopsagent-service-newrelicapikeyconfig-apikey
            '''
            result = self._values.get("api_key")
            assert result is not None, "Required property 'api_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def region(self) -> builtins.str:
            '''New Relic region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicapikeyconfig.html#cfn-devopsagent-service-newrelicapikeyconfig-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def alert_policy_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of alert policy IDs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicapikeyconfig.html#cfn-devopsagent-service-newrelicapikeyconfig-alertpolicyids
            '''
            result = self._values.get("alert_policy_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def application_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of monitored APM application IDs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicapikeyconfig.html#cfn-devopsagent-service-newrelicapikeyconfig-applicationids
            '''
            result = self._values.get("application_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def entity_guids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of globally unique IDs for New Relic resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicapikeyconfig.html#cfn-devopsagent-service-newrelicapikeyconfig-entityguids
            '''
            result = self._values.get("entity_guids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NewRelicApiKeyConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.NewRelicAuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"api_key": "apiKey"},
    )
    class NewRelicAuthorizationConfigProperty:
        def __init__(
            self,
            *,
            api_key: typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.NewRelicApiKeyConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''New Relic authorization configuration.

            :param api_key: New Relic API key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicauthorizationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                new_relic_authorization_config_property = devopsagent.CfnService.NewRelicAuthorizationConfigProperty(
                    api_key=devopsagent.CfnService.NewRelicApiKeyConfigProperty(
                        account_id="accountId",
                        api_key="apiKey",
                        region="region",
                
                        # the properties below are optional
                        alert_policy_ids=["alertPolicyIds"],
                        application_ids=["applicationIds"],
                        entity_guids=["entityGuids"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d02b1a5660e7d89e5617cc435ae1a1785a9d793dd158e69f86d868f5bda2b17)
                check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_key": api_key,
            }

        @builtins.property
        def api_key(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnService.NewRelicApiKeyConfigProperty"]:
            '''New Relic API key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicauthorizationconfig.html#cfn-devopsagent-service-newrelicauthorizationconfig-apikey
            '''
            result = self._values.get("api_key")
            assert result is not None, "Required property 'api_key' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnService.NewRelicApiKeyConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NewRelicAuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.NewRelicServiceDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"authorization_config": "authorizationConfig"},
    )
    class NewRelicServiceDetailsProperty:
        def __init__(
            self,
            *,
            authorization_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.NewRelicAuthorizationConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''New Relic service configuration.

            :param authorization_config: New Relic authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicservicedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                new_relic_service_details_property = devopsagent.CfnService.NewRelicServiceDetailsProperty(
                    authorization_config=devopsagent.CfnService.NewRelicAuthorizationConfigProperty(
                        api_key=devopsagent.CfnService.NewRelicApiKeyConfigProperty(
                            account_id="accountId",
                            api_key="apiKey",
                            region="region",
                
                            # the properties below are optional
                            alert_policy_ids=["alertPolicyIds"],
                            application_ids=["applicationIds"],
                            entity_guids=["entityGuids"]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6cbaca433d39be3f05d6d65edb9b3be293ab0c26466a109e90955d317343e3a1)
                check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorization_config": authorization_config,
            }

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnService.NewRelicAuthorizationConfigProperty"]:
            '''New Relic authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-newrelicservicedetails.html#cfn-devopsagent-service-newrelicservicedetails-authorizationconfig
            '''
            result = self._values.get("authorization_config")
            assert result is not None, "Required property 'authorization_config' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnService.NewRelicAuthorizationConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NewRelicServiceDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.OAuthClientDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "client_name": "clientName",
            "exchange_parameters": "exchangeParameters",
        },
    )
    class OAuthClientDetailsProperty:
        def __init__(
            self,
            *,
            client_id: builtins.str,
            client_secret: builtins.str,
            client_name: typing.Optional[builtins.str] = None,
            exchange_parameters: typing.Any = None,
        ) -> None:
            '''OAuth client credentials.

            :param client_id: OAuth client ID.
            :param client_secret: OAuth client secret.
            :param client_name: User friendly OAuth client name.
            :param exchange_parameters: OAuth token exchange parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-oauthclientdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # exchange_parameters: Any
                
                o_auth_client_details_property = devopsagent.CfnService.OAuthClientDetailsProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                
                    # the properties below are optional
                    client_name="clientName",
                    exchange_parameters=exchange_parameters
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69d30adb9097619b550fc8e2637f42ea3cd647e1f1847d2932439a6b3a7a859e)
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument client_name", value=client_name, expected_type=type_hints["client_name"])
                check_type(argname="argument exchange_parameters", value=exchange_parameters, expected_type=type_hints["exchange_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_id": client_id,
                "client_secret": client_secret,
            }
            if client_name is not None:
                self._values["client_name"] = client_name
            if exchange_parameters is not None:
                self._values["exchange_parameters"] = exchange_parameters

        @builtins.property
        def client_id(self) -> builtins.str:
            '''OAuth client ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-oauthclientdetails.html#cfn-devopsagent-service-oauthclientdetails-clientid
            '''
            result = self._values.get("client_id")
            assert result is not None, "Required property 'client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_secret(self) -> builtins.str:
            '''OAuth client secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-oauthclientdetails.html#cfn-devopsagent-service-oauthclientdetails-clientsecret
            '''
            result = self._values.get("client_secret")
            assert result is not None, "Required property 'client_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_name(self) -> typing.Optional[builtins.str]:
            '''User friendly OAuth client name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-oauthclientdetails.html#cfn-devopsagent-service-oauthclientdetails-clientname
            '''
            result = self._values.get("client_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exchange_parameters(self) -> typing.Any:
            '''OAuth token exchange parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-oauthclientdetails.html#cfn-devopsagent-service-oauthclientdetails-exchangeparameters
            '''
            result = self._values.get("exchange_parameters")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuthClientDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.RegisteredDynatraceDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"account_urn": "accountUrn"},
    )
    class RegisteredDynatraceDetailsProperty:
        def __init__(self, *, account_urn: builtins.str) -> None:
            '''Dynatrace service details returned after registration.

            :param account_urn: Dynatrace resource account URN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registereddynatracedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                registered_dynatrace_details_property = devopsagent.CfnService.RegisteredDynatraceDetailsProperty(
                    account_urn="accountUrn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__699f5a8b23e937bb3b578edf7c8136622218b1b1889514fbae9a950886329586)
                check_type(argname="argument account_urn", value=account_urn, expected_type=type_hints["account_urn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_urn": account_urn,
            }

        @builtins.property
        def account_urn(self) -> builtins.str:
            '''Dynatrace resource account URN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registereddynatracedetails.html#cfn-devopsagent-service-registereddynatracedetails-accounturn
            '''
            result = self._values.get("account_urn")
            assert result is not None, "Required property 'account_urn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegisteredDynatraceDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.RegisteredGitLabServiceDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_url": "targetUrl",
            "token_type": "tokenType",
            "group_id": "groupId",
        },
    )
    class RegisteredGitLabServiceDetailsProperty:
        def __init__(
            self,
            *,
            target_url: builtins.str,
            token_type: builtins.str,
            group_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''GitLab service details returned after registration.

            :param target_url: GitLab instance URL.
            :param token_type: Type of GitLab access token.
            :param group_id: Optional GitLab group ID for group-level access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredgitlabservicedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                registered_git_lab_service_details_property = devopsagent.CfnService.RegisteredGitLabServiceDetailsProperty(
                    target_url="targetUrl",
                    token_type="tokenType",
                
                    # the properties below are optional
                    group_id="groupId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d854446e4c62fec988f432899059d4e43ccb4fc2c2abfed1d4da911d0c348df)
                check_type(argname="argument target_url", value=target_url, expected_type=type_hints["target_url"])
                check_type(argname="argument token_type", value=token_type, expected_type=type_hints["token_type"])
                check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_url": target_url,
                "token_type": token_type,
            }
            if group_id is not None:
                self._values["group_id"] = group_id

        @builtins.property
        def target_url(self) -> builtins.str:
            '''GitLab instance URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredgitlabservicedetails.html#cfn-devopsagent-service-registeredgitlabservicedetails-targeturl
            '''
            result = self._values.get("target_url")
            assert result is not None, "Required property 'target_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def token_type(self) -> builtins.str:
            '''Type of GitLab access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredgitlabservicedetails.html#cfn-devopsagent-service-registeredgitlabservicedetails-tokentype
            '''
            result = self._values.get("token_type")
            assert result is not None, "Required property 'token_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def group_id(self) -> typing.Optional[builtins.str]:
            '''Optional GitLab group ID for group-level access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredgitlabservicedetails.html#cfn-devopsagent-service-registeredgitlabservicedetails-groupid
            '''
            result = self._values.get("group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegisteredGitLabServiceDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.RegisteredMCPServerDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_method": "authorizationMethod",
            "endpoint": "endpoint",
            "name": "name",
            "api_key_header": "apiKeyHeader",
            "description": "description",
        },
    )
    class RegisteredMCPServerDetailsProperty:
        def __init__(
            self,
            *,
            authorization_method: builtins.str,
            endpoint: builtins.str,
            name: builtins.str,
            api_key_header: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''MCP server details returned after registration.

            :param authorization_method: MCP server authorization method.
            :param endpoint: MCP server endpoint URL.
            :param name: MCP server name.
            :param api_key_header: API key header name if using API key authentication.
            :param description: Optional description for the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredmcpserverdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                registered_mCPServer_details_property = devopsagent.CfnService.RegisteredMCPServerDetailsProperty(
                    authorization_method="authorizationMethod",
                    endpoint="endpoint",
                    name="name",
                
                    # the properties below are optional
                    api_key_header="apiKeyHeader",
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__64842feca3ddfa950e85ba4c6de1af968036678a7ccca7400342a6c0f3560eae)
                check_type(argname="argument authorization_method", value=authorization_method, expected_type=type_hints["authorization_method"])
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument api_key_header", value=api_key_header, expected_type=type_hints["api_key_header"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorization_method": authorization_method,
                "endpoint": endpoint,
                "name": name,
            }
            if api_key_header is not None:
                self._values["api_key_header"] = api_key_header
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def authorization_method(self) -> builtins.str:
            '''MCP server authorization method.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredmcpserverdetails.html#cfn-devopsagent-service-registeredmcpserverdetails-authorizationmethod
            '''
            result = self._values.get("authorization_method")
            assert result is not None, "Required property 'authorization_method' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''MCP server endpoint URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredmcpserverdetails.html#cfn-devopsagent-service-registeredmcpserverdetails-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''MCP server name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredmcpserverdetails.html#cfn-devopsagent-service-registeredmcpserverdetails-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def api_key_header(self) -> typing.Optional[builtins.str]:
            '''API key header name if using API key authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredmcpserverdetails.html#cfn-devopsagent-service-registeredmcpserverdetails-apikeyheader
            '''
            result = self._values.get("api_key_header")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''Optional description for the MCP server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredmcpserverdetails.html#cfn-devopsagent-service-registeredmcpserverdetails-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegisteredMCPServerDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.RegisteredNewRelicDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_id": "accountId",
            "region": "region",
            "description": "description",
        },
    )
    class RegisteredNewRelicDetailsProperty:
        def __init__(
            self,
            *,
            account_id: builtins.str,
            region: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''New Relic service details returned after registration.

            :param account_id: New Relic account ID.
            :param region: New Relic region.
            :param description: Optional user description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registerednewrelicdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                registered_new_relic_details_property = devopsagent.CfnService.RegisteredNewRelicDetailsProperty(
                    account_id="accountId",
                    region="region",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9deb554de08ee49b5922b70dd0b785627adafa9ad66a8f39d7cf9b406b3b7499)
                check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_id": account_id,
                "region": region,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def account_id(self) -> builtins.str:
            '''New Relic account ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registerednewrelicdetails.html#cfn-devopsagent-service-registerednewrelicdetails-accountid
            '''
            result = self._values.get("account_id")
            assert result is not None, "Required property 'account_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def region(self) -> builtins.str:
            '''New Relic region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registerednewrelicdetails.html#cfn-devopsagent-service-registerednewrelicdetails-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''Optional user description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registerednewrelicdetails.html#cfn-devopsagent-service-registerednewrelicdetails-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegisteredNewRelicDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.RegisteredServiceNowDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_url": "instanceUrl"},
    )
    class RegisteredServiceNowDetailsProperty:
        def __init__(self, *, instance_url: builtins.str) -> None:
            '''ServiceNow service details returned after registration.

            :param instance_url: ServiceNow instance URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredservicenowdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                registered_service_now_details_property = devopsagent.CfnService.RegisteredServiceNowDetailsProperty(
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69bbba76b884f0dd1a6039cedb012b79e9c976c7d68746f12a249175306115fc)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''ServiceNow instance URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-registeredservicenowdetails.html#cfn-devopsagent-service-registeredservicenowdetails-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegisteredServiceNowDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.ServiceDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dynatrace": "dynatrace",
            "git_lab": "gitLab",
            "mcp_server": "mcpServer",
            "mcp_server_new_relic": "mcpServerNewRelic",
            "mcp_server_splunk": "mcpServerSplunk",
            "service_now": "serviceNow",
        },
    )
    class ServiceDetailsProperty:
        def __init__(
            self,
            *,
            dynatrace: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.DynatraceServiceDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            git_lab: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.GitLabDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.MCPServerDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server_new_relic: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.NewRelicServiceDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server_splunk: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.MCPServerSplunkDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_now: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.ServiceNowServiceDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param dynatrace: Dynatrace service configuration.
            :param git_lab: GitLab service configuration.
            :param mcp_server: MCP server configuration.
            :param mcp_server_new_relic: New Relic service configuration.
            :param mcp_server_splunk: Splunk MCP server configuration.
            :param service_now: ServiceNow service configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # exchange_parameters: Any
                
                service_details_property = devopsagent.CfnService.ServiceDetailsProperty(
                    dynatrace=devopsagent.CfnService.DynatraceServiceDetailsProperty(
                        account_urn="accountUrn",
                
                        # the properties below are optional
                        authorization_config=devopsagent.CfnService.DynatraceAuthorizationConfigProperty(
                            o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                                client_id="clientId",
                                client_secret="clientSecret",
                
                                # the properties below are optional
                                client_name="clientName",
                                exchange_parameters=exchange_parameters
                            )
                        )
                    ),
                    git_lab=devopsagent.CfnService.GitLabDetailsProperty(
                        target_url="targetUrl",
                        token_type="tokenType",
                        token_value="tokenValue",
                
                        # the properties below are optional
                        group_id="groupId"
                    ),
                    mcp_server=devopsagent.CfnService.MCPServerDetailsProperty(
                        authorization_config=devopsagent.CfnService.MCPServerAuthorizationConfigProperty(
                            api_key=devopsagent.CfnService.ApiKeyDetailsProperty(
                                api_key_header="apiKeyHeader",
                                api_key_name="apiKeyName",
                                api_key_value="apiKeyValue"
                            ),
                            o_auth_client_credentials=devopsagent.CfnService.MCPServerOAuthClientCredentialsConfigProperty(
                                client_id="clientId",
                                client_secret="clientSecret",
                                exchange_url="exchangeUrl",
                
                                # the properties below are optional
                                client_name="clientName",
                                exchange_parameters=exchange_parameters,
                                scopes=["scopes"]
                            )
                        ),
                        endpoint="endpoint",
                        name="name",
                
                        # the properties below are optional
                        description="description"
                    ),
                    mcp_server_new_relic=devopsagent.CfnService.NewRelicServiceDetailsProperty(
                        authorization_config=devopsagent.CfnService.NewRelicAuthorizationConfigProperty(
                            api_key=devopsagent.CfnService.NewRelicApiKeyConfigProperty(
                                account_id="accountId",
                                api_key="apiKey",
                                region="region",
                
                                # the properties below are optional
                                alert_policy_ids=["alertPolicyIds"],
                                application_ids=["applicationIds"],
                                entity_guids=["entityGuids"]
                            )
                        )
                    ),
                    mcp_server_splunk=devopsagent.CfnService.MCPServerSplunkDetailsProperty(
                        authorization_config=devopsagent.CfnService.MCPServerSplunkAuthorizationConfigProperty(
                            bearer_token=devopsagent.CfnService.BearerTokenDetailsProperty(
                                token_name="tokenName",
                                token_value="tokenValue",
                
                                # the properties below are optional
                                authorization_header="authorizationHeader"
                            )
                        ),
                        endpoint="endpoint",
                        name="name",
                
                        # the properties below are optional
                        description="description"
                    ),
                    service_now=devopsagent.CfnService.ServiceNowServiceDetailsProperty(
                        instance_url="instanceUrl",
                
                        # the properties below are optional
                        authorization_config=devopsagent.CfnService.ServiceNowAuthorizationConfigProperty(
                            o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                                client_id="clientId",
                                client_secret="clientSecret",
                
                                # the properties below are optional
                                client_name="clientName",
                                exchange_parameters=exchange_parameters
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d3cc706658e74f84415c4cda29e3f1af191a52f1dbbf8701c25e0091302740f)
                check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
                check_type(argname="argument git_lab", value=git_lab, expected_type=type_hints["git_lab"])
                check_type(argname="argument mcp_server", value=mcp_server, expected_type=type_hints["mcp_server"])
                check_type(argname="argument mcp_server_new_relic", value=mcp_server_new_relic, expected_type=type_hints["mcp_server_new_relic"])
                check_type(argname="argument mcp_server_splunk", value=mcp_server_splunk, expected_type=type_hints["mcp_server_splunk"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dynatrace is not None:
                self._values["dynatrace"] = dynatrace
            if git_lab is not None:
                self._values["git_lab"] = git_lab
            if mcp_server is not None:
                self._values["mcp_server"] = mcp_server
            if mcp_server_new_relic is not None:
                self._values["mcp_server_new_relic"] = mcp_server_new_relic
            if mcp_server_splunk is not None:
                self._values["mcp_server_splunk"] = mcp_server_splunk
            if service_now is not None:
                self._values["service_now"] = service_now

        @builtins.property
        def dynatrace(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.DynatraceServiceDetailsProperty"]]:
            '''Dynatrace service configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicedetails.html#cfn-devopsagent-service-servicedetails-dynatrace
            '''
            result = self._values.get("dynatrace")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.DynatraceServiceDetailsProperty"]], result)

        @builtins.property
        def git_lab(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.GitLabDetailsProperty"]]:
            '''GitLab service configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicedetails.html#cfn-devopsagent-service-servicedetails-gitlab
            '''
            result = self._values.get("git_lab")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.GitLabDetailsProperty"]], result)

        @builtins.property
        def mcp_server(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerDetailsProperty"]]:
            '''MCP server configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicedetails.html#cfn-devopsagent-service-servicedetails-mcpserver
            '''
            result = self._values.get("mcp_server")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerDetailsProperty"]], result)

        @builtins.property
        def mcp_server_new_relic(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.NewRelicServiceDetailsProperty"]]:
            '''New Relic service configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicedetails.html#cfn-devopsagent-service-servicedetails-mcpservernewrelic
            '''
            result = self._values.get("mcp_server_new_relic")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.NewRelicServiceDetailsProperty"]], result)

        @builtins.property
        def mcp_server_splunk(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerSplunkDetailsProperty"]]:
            '''Splunk MCP server configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicedetails.html#cfn-devopsagent-service-servicedetails-mcpserversplunk
            '''
            result = self._values.get("mcp_server_splunk")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.MCPServerSplunkDetailsProperty"]], result)

        @builtins.property
        def service_now(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ServiceNowServiceDetailsProperty"]]:
            '''ServiceNow service configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicedetails.html#cfn-devopsagent-service-servicedetails-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ServiceNowServiceDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.ServiceNowAuthorizationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"o_auth_client_credentials": "oAuthClientCredentials"},
    )
    class ServiceNowAuthorizationConfigProperty:
        def __init__(
            self,
            *,
            o_auth_client_credentials: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.OAuthClientDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''ServiceNow OAuth authorization configuration.

            :param o_auth_client_credentials: OAuth client credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicenowauthorizationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # exchange_parameters: Any
                
                service_now_authorization_config_property = devopsagent.CfnService.ServiceNowAuthorizationConfigProperty(
                    o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
                
                        # the properties below are optional
                        client_name="clientName",
                        exchange_parameters=exchange_parameters
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff2fade9fa308db855d28957e382348359076946ed4f567ccc0909401bc9757f)
                check_type(argname="argument o_auth_client_credentials", value=o_auth_client_credentials, expected_type=type_hints["o_auth_client_credentials"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if o_auth_client_credentials is not None:
                self._values["o_auth_client_credentials"] = o_auth_client_credentials

        @builtins.property
        def o_auth_client_credentials(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.OAuthClientDetailsProperty"]]:
            '''OAuth client credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicenowauthorizationconfig.html#cfn-devopsagent-service-servicenowauthorizationconfig-oauthclientcredentials
            '''
            result = self._values.get("o_auth_client_credentials")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.OAuthClientDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowAuthorizationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_devopsagent.CfnService.ServiceNowServiceDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_url": "instanceUrl",
            "authorization_config": "authorizationConfig",
        },
    )
    class ServiceNowServiceDetailsProperty:
        def __init__(
            self,
            *,
            instance_url: builtins.str,
            authorization_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.ServiceNowAuthorizationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''ServiceNow service configuration.

            :param instance_url: ServiceNow instance URL.
            :param authorization_config: ServiceNow OAuth authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicenowservicedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_devopsagent as devopsagent
                
                # exchange_parameters: Any
                
                service_now_service_details_property = devopsagent.CfnService.ServiceNowServiceDetailsProperty(
                    instance_url="instanceUrl",
                
                    # the properties below are optional
                    authorization_config=devopsagent.CfnService.ServiceNowAuthorizationConfigProperty(
                        o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
                
                            # the properties below are optional
                            client_name="clientName",
                            exchange_parameters=exchange_parameters
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d187ccd94caa63f84c780709217fd146f3bb8a30928a00c86283e0e434a2df54)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
                check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }
            if authorization_config is not None:
                self._values["authorization_config"] = authorization_config

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''ServiceNow instance URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicenowservicedetails.html#cfn-devopsagent-service-servicenowservicedetails-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def authorization_config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ServiceNowAuthorizationConfigProperty"]]:
            '''ServiceNow OAuth authorization configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-devopsagent-service-servicenowservicedetails.html#cfn-devopsagent-service-servicenowservicedetails-authorizationconfig
            '''
            result = self._values.get("authorization_config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ServiceNowAuthorizationConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowServiceDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_devopsagent.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={"service_type": "serviceType", "service_details": "serviceDetails"},
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        service_type: builtins.str,
        service_details: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnService.ServiceDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnService``.

        :param service_type: The type of service being registered.
        :param service_details: Service-specific configuration details.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-service.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_devopsagent as devopsagent
            
            # exchange_parameters: Any
            
            cfn_service_props = devopsagent.CfnServiceProps(
                service_type="serviceType",
            
                # the properties below are optional
                service_details=devopsagent.CfnService.ServiceDetailsProperty(
                    dynatrace=devopsagent.CfnService.DynatraceServiceDetailsProperty(
                        account_urn="accountUrn",
            
                        # the properties below are optional
                        authorization_config=devopsagent.CfnService.DynatraceAuthorizationConfigProperty(
                            o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                                client_id="clientId",
                                client_secret="clientSecret",
            
                                # the properties below are optional
                                client_name="clientName",
                                exchange_parameters=exchange_parameters
                            )
                        )
                    ),
                    git_lab=devopsagent.CfnService.GitLabDetailsProperty(
                        target_url="targetUrl",
                        token_type="tokenType",
                        token_value="tokenValue",
            
                        # the properties below are optional
                        group_id="groupId"
                    ),
                    mcp_server=devopsagent.CfnService.MCPServerDetailsProperty(
                        authorization_config=devopsagent.CfnService.MCPServerAuthorizationConfigProperty(
                            api_key=devopsagent.CfnService.ApiKeyDetailsProperty(
                                api_key_header="apiKeyHeader",
                                api_key_name="apiKeyName",
                                api_key_value="apiKeyValue"
                            ),
                            o_auth_client_credentials=devopsagent.CfnService.MCPServerOAuthClientCredentialsConfigProperty(
                                client_id="clientId",
                                client_secret="clientSecret",
                                exchange_url="exchangeUrl",
            
                                # the properties below are optional
                                client_name="clientName",
                                exchange_parameters=exchange_parameters,
                                scopes=["scopes"]
                            )
                        ),
                        endpoint="endpoint",
                        name="name",
            
                        # the properties below are optional
                        description="description"
                    ),
                    mcp_server_new_relic=devopsagent.CfnService.NewRelicServiceDetailsProperty(
                        authorization_config=devopsagent.CfnService.NewRelicAuthorizationConfigProperty(
                            api_key=devopsagent.CfnService.NewRelicApiKeyConfigProperty(
                                account_id="accountId",
                                api_key="apiKey",
                                region="region",
            
                                # the properties below are optional
                                alert_policy_ids=["alertPolicyIds"],
                                application_ids=["applicationIds"],
                                entity_guids=["entityGuids"]
                            )
                        )
                    ),
                    mcp_server_splunk=devopsagent.CfnService.MCPServerSplunkDetailsProperty(
                        authorization_config=devopsagent.CfnService.MCPServerSplunkAuthorizationConfigProperty(
                            bearer_token=devopsagent.CfnService.BearerTokenDetailsProperty(
                                token_name="tokenName",
                                token_value="tokenValue",
            
                                # the properties below are optional
                                authorization_header="authorizationHeader"
                            )
                        ),
                        endpoint="endpoint",
                        name="name",
            
                        # the properties below are optional
                        description="description"
                    ),
                    service_now=devopsagent.CfnService.ServiceNowServiceDetailsProperty(
                        instance_url="instanceUrl",
            
                        # the properties below are optional
                        authorization_config=devopsagent.CfnService.ServiceNowAuthorizationConfigProperty(
                            o_auth_client_credentials=devopsagent.CfnService.OAuthClientDetailsProperty(
                                client_id="clientId",
                                client_secret="clientSecret",
            
                                # the properties below are optional
                                client_name="clientName",
                                exchange_parameters=exchange_parameters
                            )
                        )
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a12adbc62e2ac0f5b7caf0c232882e56ee71ed33922d8b268e225ddc848413f6)
            check_type(argname="argument service_type", value=service_type, expected_type=type_hints["service_type"])
            check_type(argname="argument service_details", value=service_details, expected_type=type_hints["service_details"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_type": service_type,
        }
        if service_details is not None:
            self._values["service_details"] = service_details

    @builtins.property
    def service_type(self) -> builtins.str:
        '''The type of service being registered.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-service.html#cfn-devopsagent-service-servicetype
        '''
        result = self._values.get("service_type")
        assert result is not None, "Required property 'service_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_details(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ServiceDetailsProperty"]]:
        '''Service-specific configuration details.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-devopsagent-service.html#cfn-devopsagent-service-servicedetails
        '''
        result = self._values.get("service_details")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnService.ServiceDetailsProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAgentSpace",
    "CfnAgentSpaceProps",
    "CfnAssociation",
    "CfnAssociationProps",
    "CfnService",
    "CfnServiceProps",
]

publication.publish()

def _typecheckingstub__3897cdc52c2bc2a74bdd32702e32905947b3c0fc36798edcdac7875cc9939456(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    operator_app: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.OperatorAppProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3fd19a72161f0ef8cc6732b6e9205e1c9f41b50d57a659a84461dcdde223423(
    resource: _IAgentSpaceRef_2ffb48ed,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dc004d63d73274933efa9e02989941984735e5426f7c063d97b0b415406d8d4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c0f8fde84620afc53f90b3672d7f693a2e66909624772cab6d4c2337a64aa65(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    agent_space_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62b6182298920242aa320928b58b0b5bc6ee7fe37ab398df5dd8f138f81638f6(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c3714a879ff931c53d9540f49cb04b7551032f6754505380b7064cbcb7719f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aca7931f7e8a8dc031f895c3bf121e4253f0443d5d02865c48e259d41303518b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80e1593c483d80afbaaf07c646b5d5ede131e360f81f0dde9fa486f5c749e58f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b7561d8cdcaf93c81d1cf0a9a4cc5790c03232e494d49db5171a93599b8f575(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__833bedcb900be3dc99153bbcef5866a753457156d32ebc2661b687708cf7f6fa(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAgentSpace.OperatorAppProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4beb411197d70233cb23add12a5f3b652beb521a346992040d7d02b2b1ddd228(
    *,
    operator_app_role_arn: builtins.str,
    created_at: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54cfce91472eb9681ce65a0ce7a6d266ecbcafccbd8e1842288a0f262a4d5755(
    *,
    idc_instance_arn: builtins.str,
    operator_app_role_arn: builtins.str,
    created_at: typing.Optional[builtins.str] = None,
    idc_application_arn: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__163f48e2381f16154d3ed1a507d7fa1b64898c9ada42152eb65e4a5a869c805c(
    *,
    iam: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.IamAuthConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    idc: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.IdcAuthConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea00a21cf40eafce14a4e6e1a4cd3e9f843a2f2e416299a20a2159ce8cdb6d5f(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    operator_app: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAgentSpace.OperatorAppProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9507e77277cf05febf82ccf8829d008e3d5bca6bfbb5c229a629346a34d445ff(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_space_id: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.ServiceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    service_id: builtins.str,
    linked_association_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89cae44481f5807f4bcf3fcf5d08b660423111da523b22ba60bcaacf43a50aa9(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd21b036854f8ed65af7b88356ee2787b8f2fb60324e8b7f39b6edf4992ce967(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea0d4a7651eb08ad3bc11db7886a5718c26e72c5b665acd6183227b87adf00e4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac4f12f5965b47ff3162eacbbbebb04e5d1595483e00e0e29ace1cd733b8156(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b224d34e655755660b3f83f1ef3ad78de31336ef41e61cf24dfb47a3d5e00b96(
    value: typing.Union[_IResolvable_da3f097b, CfnAssociation.ServiceConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08d88d472b1933bfd27859b1b634111a6667c50bedacee3234cfc98a8a05797a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a926a8cb577bf81233b764232f042b444bc6a9e989283355f36b9faf248fe46(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f1d632ade69849147b75fe20e7412c90e54c9e84dafe76046f35e5fa880436f(
    *,
    account_id: builtins.str,
    account_type: builtins.str,
    assumable_role_arn: builtins.str,
    resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.AWSResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnAssociation.KeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c83865c7f5f4d4caa82576ab7efaac17f6225904d0ac52970333a1906f6ed0cb(
    *,
    resource_arn: builtins.str,
    resource_metadata: typing.Any = None,
    resource_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af533dc830c7a5f8fd17b5170cecf1e7dd483fe076400d57927aca27831a0ca8(
    *,
    env_id: builtins.str,
    enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    resources: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d900735d86a3a2a681d9eba7f3ce7754e8cdfbc47df16370253e165583cd41(
    *,
    enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f52e2bfd74e3e041299304fca2e11acf7c77935cb3d81768bd90034e89f0c1f3(
    *,
    owner: builtins.str,
    owner_type: builtins.str,
    repo_id: builtins.str,
    repo_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0bf76d18d2da5c1a7b65fd908fdd6aa4ca798335d0ef9f07ec4c064ccb5241(
    *,
    project_id: builtins.str,
    project_path: builtins.str,
    enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    instance_identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ded74f7f3af261fdfeb1ca20f0589b46cd28465b569b567f86c794c6d2010df2(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97d8de94964f9d444ce60e60c71a8386873d9d717628a8b450e0463922b08600(
    *,
    endpoint: builtins.str,
    name: builtins.str,
    tools: typing.Sequence[builtins.str],
    description: typing.Optional[builtins.str] = None,
    enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94bdd66d2ae6508b6fa75de77b1b7bd044d6bf7b9e0c60cb573f57ca7faa1817(
    *,
    endpoint: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d60c2241968bd47959618d5fef16076f92aa6b8c2e1932e3d7d5e3983c4108a8(
    *,
    account_id: builtins.str,
    endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5251bb56068759277d9b99b06c4d20b0e0434473774eeb3d825f9ed5301ba970(
    *,
    endpoint: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534ff66bec4c3f764380e71fc8dbccb3b6b0319f301032fa7e975aa1842a74e1(
    *,
    aws: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.AWSConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynatrace: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.DynatraceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_channel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.EventChannelConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    git_hub: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.GitHubConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    git_lab: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.GitLabConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.MCPServerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server_datadog: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.MCPServerDatadogConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server_new_relic: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.MCPServerNewRelicConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server_splunk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.MCPServerSplunkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.ServiceNowConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    slack: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.SlackConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_aws: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.SourceAwsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9767ae84f8f9ac8fbffe3c19d1ac1dc61d581770deb87d97b058eb73cc671511(
    *,
    enable_webhook_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    instance_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06cf6d0fee94466c60ffb3cbfb9f571fb9f69201085fc5de6cd2f0d6e4b8d633(
    *,
    channel_id: builtins.str,
    channel_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28eb759dbeb853e46c5ba811aba401a06c7b87554a3bac255792e3d13c3f0c23(
    *,
    transmission_target: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.SlackTransmissionTargetProperty, typing.Dict[builtins.str, typing.Any]]],
    workspace_id: builtins.str,
    workspace_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4224928b94c6f3a7e8aeb21f4d921f668ae91ec705e4026d010b1813687b20c5(
    *,
    incident_response_target: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.SlackChannelProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7f309a9bf78a2704dbd1fd90dfdf8ff7ac7091cdb4572312fad3281cfcbd5ac(
    *,
    account_id: builtins.str,
    account_type: builtins.str,
    assumable_role_arn: builtins.str,
    resources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.AWSResourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnAssociation.KeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b9c7866e61a4a7267964c2e97d2c2f23071408ae1546eca41521d60b1273549(
    *,
    agent_space_id: builtins.str,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAssociation.ServiceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    service_id: builtins.str,
    linked_association_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76700bf71c0ca9d7d21edc970f56dd1c8a41f67b248c3228096feb30580cca07(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    service_type: builtins.str,
    service_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ServiceDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4747cf77eaeb36736a2ca00fd2ce576b093ee7f10e64c38001e2eac5a33d8149(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6a60e2418d472a473b14d2bbcbd2350af8fed2083a2938616370c1e08ed3e0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2740d5b9657545f92bc9b54f5c97b22d107226f26deef1c36cbd652d62b9aba0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87d815016e64b5bdf47334ae0b9ef194602b4aa5a9e6cd5a5d9b1d6b516b9a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38b28b2539546ba11e45199a6bde41e432e6246da9ea58bba29ece3bbf5c4193(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.ServiceDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d2aa127fac97efcf9f5ae815fbac6244f4de11a1b85beb8acc053b8eb8edee(
    *,
    dynatrace: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.RegisteredDynatraceDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    git_lab: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.RegisteredGitLabServiceDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.RegisteredMCPServerDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server_new_relic: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.RegisteredNewRelicDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server_splunk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.RegisteredMCPServerDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.RegisteredServiceNowDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76e209fab46047902f46ddb19cd603ac6794e4e730c2326df60b5016370583cf(
    *,
    api_key_header: builtins.str,
    api_key_name: builtins.str,
    api_key_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ed3f342895156ff05fa55fe762ca658173862cfba9138b08506eef2da17f21(
    *,
    token_name: builtins.str,
    token_value: builtins.str,
    authorization_header: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c94d9ef2811300fc8439f749f5e0b012380780ff3ee8da59d63a89012981e4(
    *,
    o_auth_client_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.OAuthClientDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1093f5ca4a6437d94226499a72d7ed498cbf6c82d31179c14e9526707fa4f8c0(
    *,
    account_urn: builtins.str,
    authorization_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.DynatraceAuthorizationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b58d9276d7725a7b2a814720d881a8dd974b0d85b18fe425efb863bc1d25a08(
    *,
    target_url: builtins.str,
    token_type: builtins.str,
    token_value: builtins.str,
    group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d23407dd8b2083d432d8db1552b2c86a3325b7151f0c72016ef6edc6a6fd65e8(
    *,
    api_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ApiKeyDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    o_auth_client_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.MCPServerOAuthClientCredentialsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8254611fd4c93bda748b35259025cc559c3ff3316f16d3a4c6b8742407842e77(
    *,
    authorization_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.MCPServerAuthorizationConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    endpoint: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__198a110da941ce87aaecb0a0b1ba18fa10731b81d29b4a768fd8f795ff2b76f5(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    exchange_url: builtins.str,
    client_name: typing.Optional[builtins.str] = None,
    exchange_parameters: typing.Any = None,
    scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c92e97e3c227e3467ecb452f408839f30cb1b85644fbd8f96962ea3606723a1(
    *,
    bearer_token: typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.BearerTokenDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53d93e87f0f22c03aa42a187eee24ad101676f59eb3e0ca8d617001ea054e7d1(
    *,
    authorization_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.MCPServerSplunkAuthorizationConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    endpoint: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4540b44ec165187fba7151d272d0adb7a00d610661a528aea957f435fc7864dd(
    *,
    account_id: builtins.str,
    api_key: builtins.str,
    region: builtins.str,
    alert_policy_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    application_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    entity_guids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d02b1a5660e7d89e5617cc435ae1a1785a9d793dd158e69f86d868f5bda2b17(
    *,
    api_key: typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.NewRelicApiKeyConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cbaca433d39be3f05d6d65edb9b3be293ab0c26466a109e90955d317343e3a1(
    *,
    authorization_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.NewRelicAuthorizationConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69d30adb9097619b550fc8e2637f42ea3cd647e1f1847d2932439a6b3a7a859e(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    client_name: typing.Optional[builtins.str] = None,
    exchange_parameters: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__699f5a8b23e937bb3b578edf7c8136622218b1b1889514fbae9a950886329586(
    *,
    account_urn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d854446e4c62fec988f432899059d4e43ccb4fc2c2abfed1d4da911d0c348df(
    *,
    target_url: builtins.str,
    token_type: builtins.str,
    group_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64842feca3ddfa950e85ba4c6de1af968036678a7ccca7400342a6c0f3560eae(
    *,
    authorization_method: builtins.str,
    endpoint: builtins.str,
    name: builtins.str,
    api_key_header: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9deb554de08ee49b5922b70dd0b785627adafa9ad66a8f39d7cf9b406b3b7499(
    *,
    account_id: builtins.str,
    region: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69bbba76b884f0dd1a6039cedb012b79e9c976c7d68746f12a249175306115fc(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3cc706658e74f84415c4cda29e3f1af191a52f1dbbf8701c25e0091302740f(
    *,
    dynatrace: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.DynatraceServiceDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    git_lab: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.GitLabDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.MCPServerDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server_new_relic: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.NewRelicServiceDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server_splunk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.MCPServerSplunkDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ServiceNowServiceDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff2fade9fa308db855d28957e382348359076946ed4f567ccc0909401bc9757f(
    *,
    o_auth_client_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.OAuthClientDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d187ccd94caa63f84c780709217fd146f3bb8a30928a00c86283e0e434a2df54(
    *,
    instance_url: builtins.str,
    authorization_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ServiceNowAuthorizationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a12adbc62e2ac0f5b7caf0c232882e56ee71ed33922d8b268e225ddc848413f6(
    *,
    service_type: builtins.str,
    service_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ServiceDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
