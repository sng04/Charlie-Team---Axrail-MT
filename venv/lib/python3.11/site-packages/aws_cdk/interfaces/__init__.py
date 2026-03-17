r'''
# CDK Resource Interfaces

This module contains resource interfaces for all AWS service resources.

These are interfaces that look like this:

```
/**
 * Indicates that this resource can be referenced as a Bucket.
 */
interface IBucketRef {
  /**
   * A reference to a Bucket resource.
   */
  readonly bucketRef: BucketReference;
}

interface BucketReference {
  /**
   * The BucketName of the Bucket resource.
   */
  readonly bucketName: string;

  /**
   * The ARN of the Bucket resource.
   */
  readonly bucketArn: string;
}
```

These are in a separate submodule so that they can be referenced from all other
service submodules without introducing cyclic dependencies between them.
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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.IEnvironmentAware")
class IEnvironmentAware(typing_extensions.Protocol):
    '''Used to indicate that a particular construct has an resource environment.'''

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> "ResourceEnvironment":
        '''The environment this resource belongs to.

        For resources that are created and managed in a Stack (those created by
        creating new class instances like ``new Role()``, ``new Bucket()``, etc.), this
        is always the same as the environment of the stack they belong to.

        For referenced resources (those obtained from referencing methods like
        ``Role.fromRoleArn()``, ``Bucket.fromBucketName()``, etc.), they might be
        different than the stack they were imported into.
        '''
        ...


class _IEnvironmentAwareProxy:
    '''Used to indicate that a particular construct has an resource environment.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.IEnvironmentAware"

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> "ResourceEnvironment":
        '''The environment this resource belongs to.

        For resources that are created and managed in a Stack (those created by
        creating new class instances like ``new Role()``, ``new Bucket()``, etc.), this
        is always the same as the environment of the stack they belong to.

        For referenced resources (those obtained from referencing methods like
        ``Role.fromRoleArn()``, ``Bucket.fromBucketName()``, etc.), they might be
        different than the stack they were imported into.
        '''
        return typing.cast("ResourceEnvironment", jsii.get(self, "env"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentAware).__jsii_proxy_class__ = lambda : _IEnvironmentAwareProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.ResourceEnvironment",
    jsii_struct_bases=[],
    name_mapping={"account": "account", "region": "region"},
)
class ResourceEnvironment:
    def __init__(self, *, account: builtins.str, region: builtins.str) -> None:
        '''Represents the environment a given resource lives in.

        Used as the return value for the ``IEnvironmentAware.env`` property.

        :param account: The AWS Account ID that this resource belongs to. Since this can be a Token (for example, when the account is CloudFormation's ``AWS::AccountId`` intrinsic), make sure to use ``Token.compareStrings()`` instead of comparing the values with direct string equality.
        :param region: The AWS Region that this resource belongs to. Since this can be a Token (for example, when the region is CloudFormation's ``AWS::Region`` intrinsic), make sure to use ``Token.compareStrings()`` instead of comparing the values with direct string equality.

        :exampleMetadata: nofixture infused

        Example::

            from aws_cdk.aws_iam import AddToResourcePolicyResult
            from aws_cdk import CfnResource
            from aws_cdk.aws_iam import IResourcePolicyFactory, IResourceWithPolicyV2, PolicyStatement, ResourceWithPolicies
            from constructs import Construct, IConstruct
            
            # scope: Construct
            @jsii.implements(IResourcePolicyFactory)
            class MyFactory:
                def for_resource(self, resource):
                    return {
                        "env": resource.env,
                        def add_to_resource_policy(self, statement):
                            # custom implementation to add the statement to the resource policy
                            return AddToResourcePolicyResult("statement_added"=True, "policy_dependable"=resource)
                    }
            
            ResourceWithPolicies.register(scope, "AWS::KMS::Key", MyFactory())
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5aaa43a6d0a198f8a3f9e8ab7ee8ce8d940df80e550839a285b920b7d6e816f)
            check_type(argname="argument account", value=account, expected_type=type_hints["account"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account": account,
            "region": region,
        }

    @builtins.property
    def account(self) -> builtins.str:
        '''The AWS Account ID that this resource belongs to.

        Since this can be a Token (for example, when the account is
        CloudFormation's ``AWS::AccountId`` intrinsic), make sure to use
        ``Token.compareStrings()`` instead of comparing the values with direct
        string equality.
        '''
        result = self._values.get("account")
        assert result is not None, "Required property 'account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The AWS Region that this resource belongs to.

        Since this can be a Token (for example, when the region is CloudFormation's
        ``AWS::Region`` intrinsic), make sure to use ``Token.compareStrings()`` instead
        of comparing the values with direct string equality.
        '''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceEnvironment(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IEnvironmentAware",
    "ResourceEnvironment",
    "alexa_ask",
    "aws_accessanalyzer",
    "aws_acmpca",
    "aws_aiops",
    "aws_amazonmq",
    "aws_amplify",
    "aws_amplifyuibuilder",
    "aws_apigateway",
    "aws_apigatewayv2",
    "aws_appconfig",
    "aws_appflow",
    "aws_appintegrations",
    "aws_applicationautoscaling",
    "aws_applicationinsights",
    "aws_applicationsignals",
    "aws_appmesh",
    "aws_apprunner",
    "aws_appstream",
    "aws_appsync",
    "aws_apptest",
    "aws_aps",
    "aws_arcregionswitch",
    "aws_arczonalshift",
    "aws_athena",
    "aws_auditmanager",
    "aws_autoscaling",
    "aws_autoscalingplans",
    "aws_b2bi",
    "aws_backup",
    "aws_backupgateway",
    "aws_batch",
    "aws_bcmdataexports",
    "aws_bedrock",
    "aws_bedrockagentcore",
    "aws_bedrockmantle",
    "aws_billing",
    "aws_billingconductor",
    "aws_budgets",
    "aws_cases",
    "aws_cassandra",
    "aws_ce",
    "aws_certificatemanager",
    "aws_chatbot",
    "aws_cleanrooms",
    "aws_cleanroomsml",
    "aws_cloud9",
    "aws_cloudformation",
    "aws_cloudfront",
    "aws_cloudtrail",
    "aws_cloudwatch",
    "aws_codeartifact",
    "aws_codebuild",
    "aws_codecommit",
    "aws_codeconnections",
    "aws_codedeploy",
    "aws_codeguruprofiler",
    "aws_codegurureviewer",
    "aws_codepipeline",
    "aws_codestar",
    "aws_codestarconnections",
    "aws_codestarnotifications",
    "aws_cognito",
    "aws_comprehend",
    "aws_computeoptimizer",
    "aws_config",
    "aws_connect",
    "aws_connectcampaigns",
    "aws_connectcampaignsv2",
    "aws_controltower",
    "aws_cur",
    "aws_customerprofiles",
    "aws_databrew",
    "aws_datapipeline",
    "aws_datasync",
    "aws_datazone",
    "aws_dax",
    "aws_deadline",
    "aws_detective",
    "aws_devicefarm",
    "aws_devopsagent",
    "aws_devopsguru",
    "aws_directconnect",
    "aws_directoryservice",
    "aws_dlm",
    "aws_dms",
    "aws_docdb",
    "aws_docdbelastic",
    "aws_dsql",
    "aws_dynamodb",
    "aws_ec2",
    "aws_ecr",
    "aws_ecs",
    "aws_efs",
    "aws_eks",
    "aws_elasticache",
    "aws_elasticbeanstalk",
    "aws_elasticloadbalancing",
    "aws_elasticloadbalancingv2",
    "aws_elasticsearch",
    "aws_emr",
    "aws_emrcontainers",
    "aws_emrserverless",
    "aws_entityresolution",
    "aws_events",
    "aws_eventschemas",
    "aws_evidently",
    "aws_evs",
    "aws_finspace",
    "aws_fis",
    "aws_fms",
    "aws_forecast",
    "aws_frauddetector",
    "aws_fsx",
    "aws_gamelift",
    "aws_gameliftstreams",
    "aws_globalaccelerator",
    "aws_glue",
    "aws_grafana",
    "aws_greengrass",
    "aws_greengrassv2",
    "aws_groundstation",
    "aws_guardduty",
    "aws_healthimaging",
    "aws_healthlake",
    "aws_iam",
    "aws_identitystore",
    "aws_imagebuilder",
    "aws_inspector",
    "aws_inspectorv2",
    "aws_internetmonitor",
    "aws_invoicing",
    "aws_iot",
    "aws_iotanalytics",
    "aws_iotcoredeviceadvisor",
    "aws_iotevents",
    "aws_iotfleethub",
    "aws_iotfleetwise",
    "aws_iotsitewise",
    "aws_iotthingsgraph",
    "aws_iottwinmaker",
    "aws_iotwireless",
    "aws_ivs",
    "aws_ivschat",
    "aws_kafkaconnect",
    "aws_kendra",
    "aws_kendraranking",
    "aws_kinesis",
    "aws_kinesisanalytics",
    "aws_kinesisanalyticsv2",
    "aws_kinesisfirehose",
    "aws_kinesisvideo",
    "aws_kms",
    "aws_lakeformation",
    "aws_lambda",
    "aws_launchwizard",
    "aws_lex",
    "aws_licensemanager",
    "aws_lightsail",
    "aws_location",
    "aws_logs",
    "aws_lookoutequipment",
    "aws_lookoutmetrics",
    "aws_lookoutvision",
    "aws_m2",
    "aws_macie",
    "aws_managedblockchain",
    "aws_mediaconnect",
    "aws_mediaconvert",
    "aws_medialive",
    "aws_mediapackage",
    "aws_mediapackagev2",
    "aws_mediastore",
    "aws_mediatailor",
    "aws_memorydb",
    "aws_mpa",
    "aws_msk",
    "aws_mwaa",
    "aws_mwaaserverless",
    "aws_neptune",
    "aws_neptunegraph",
    "aws_networkfirewall",
    "aws_networkmanager",
    "aws_nimblestudio",
    "aws_notifications",
    "aws_notificationscontacts",
    "aws_oam",
    "aws_observabilityadmin",
    "aws_odb",
    "aws_omics",
    "aws_opensearchserverless",
    "aws_opensearchservice",
    "aws_opsworks",
    "aws_opsworkscm",
    "aws_organizations",
    "aws_osis",
    "aws_panorama",
    "aws_paymentcryptography",
    "aws_pcaconnectorad",
    "aws_pcaconnectorscep",
    "aws_pcs",
    "aws_personalize",
    "aws_pinpoint",
    "aws_pinpointemail",
    "aws_pipes",
    "aws_proton",
    "aws_qbusiness",
    "aws_qldb",
    "aws_quicksight",
    "aws_ram",
    "aws_rbin",
    "aws_rds",
    "aws_redshift",
    "aws_redshiftserverless",
    "aws_refactorspaces",
    "aws_rekognition",
    "aws_resiliencehub",
    "aws_resourceexplorer2",
    "aws_resourcegroups",
    "aws_robomaker",
    "aws_rolesanywhere",
    "aws_route53",
    "aws_route53profiles",
    "aws_route53recoverycontrol",
    "aws_route53recoveryreadiness",
    "aws_route53resolver",
    "aws_rtbfabric",
    "aws_rum",
    "aws_s3",
    "aws_s3express",
    "aws_s3objectlambda",
    "aws_s3outposts",
    "aws_s3tables",
    "aws_s3vectors",
    "aws_sagemaker",
    "aws_sam",
    "aws_scheduler",
    "aws_sdb",
    "aws_secretsmanager",
    "aws_securityhub",
    "aws_securitylake",
    "aws_servicecatalog",
    "aws_servicecatalogappregistry",
    "aws_servicediscovery",
    "aws_ses",
    "aws_shield",
    "aws_signer",
    "aws_simspaceweaver",
    "aws_smsvoice",
    "aws_sns",
    "aws_sqs",
    "aws_ssm",
    "aws_ssmcontacts",
    "aws_ssmguiconnect",
    "aws_ssmincidents",
    "aws_ssmquicksetup",
    "aws_sso",
    "aws_stepfunctions",
    "aws_supportapp",
    "aws_synthetics",
    "aws_systemsmanagersap",
    "aws_timestream",
    "aws_transfer",
    "aws_verifiedpermissions",
    "aws_voiceid",
    "aws_vpclattice",
    "aws_waf",
    "aws_wafregional",
    "aws_wafv2",
    "aws_wisdom",
    "aws_workspaces",
    "aws_workspacesinstances",
    "aws_workspacesthinclient",
    "aws_workspacesweb",
    "aws_xray",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import alexa_ask
from . import aws_accessanalyzer
from . import aws_acmpca
from . import aws_aiops
from . import aws_amazonmq
from . import aws_amplify
from . import aws_amplifyuibuilder
from . import aws_apigateway
from . import aws_apigatewayv2
from . import aws_appconfig
from . import aws_appflow
from . import aws_appintegrations
from . import aws_applicationautoscaling
from . import aws_applicationinsights
from . import aws_applicationsignals
from . import aws_appmesh
from . import aws_apprunner
from . import aws_appstream
from . import aws_appsync
from . import aws_apptest
from . import aws_aps
from . import aws_arcregionswitch
from . import aws_arczonalshift
from . import aws_athena
from . import aws_auditmanager
from . import aws_autoscaling
from . import aws_autoscalingplans
from . import aws_b2bi
from . import aws_backup
from . import aws_backupgateway
from . import aws_batch
from . import aws_bcmdataexports
from . import aws_bedrock
from . import aws_bedrockagentcore
from . import aws_bedrockmantle
from . import aws_billing
from . import aws_billingconductor
from . import aws_budgets
from . import aws_cases
from . import aws_cassandra
from . import aws_ce
from . import aws_certificatemanager
from . import aws_chatbot
from . import aws_cleanrooms
from . import aws_cleanroomsml
from . import aws_cloud9
from . import aws_cloudformation
from . import aws_cloudfront
from . import aws_cloudtrail
from . import aws_cloudwatch
from . import aws_codeartifact
from . import aws_codebuild
from . import aws_codecommit
from . import aws_codeconnections
from . import aws_codedeploy
from . import aws_codeguruprofiler
from . import aws_codegurureviewer
from . import aws_codepipeline
from . import aws_codestar
from . import aws_codestarconnections
from . import aws_codestarnotifications
from . import aws_cognito
from . import aws_comprehend
from . import aws_computeoptimizer
from . import aws_config
from . import aws_connect
from . import aws_connectcampaigns
from . import aws_connectcampaignsv2
from . import aws_controltower
from . import aws_cur
from . import aws_customerprofiles
from . import aws_databrew
from . import aws_datapipeline
from . import aws_datasync
from . import aws_datazone
from . import aws_dax
from . import aws_deadline
from . import aws_detective
from . import aws_devicefarm
from . import aws_devopsagent
from . import aws_devopsguru
from . import aws_directconnect
from . import aws_directoryservice
from . import aws_dlm
from . import aws_dms
from . import aws_docdb
from . import aws_docdbelastic
from . import aws_dsql
from . import aws_dynamodb
from . import aws_ec2
from . import aws_ecr
from . import aws_ecs
from . import aws_efs
from . import aws_eks
from . import aws_elasticache
from . import aws_elasticbeanstalk
from . import aws_elasticloadbalancing
from . import aws_elasticloadbalancingv2
from . import aws_elasticsearch
from . import aws_emr
from . import aws_emrcontainers
from . import aws_emrserverless
from . import aws_entityresolution
from . import aws_events
from . import aws_eventschemas
from . import aws_evidently
from . import aws_evs
from . import aws_finspace
from . import aws_fis
from . import aws_fms
from . import aws_forecast
from . import aws_frauddetector
from . import aws_fsx
from . import aws_gamelift
from . import aws_gameliftstreams
from . import aws_globalaccelerator
from . import aws_glue
from . import aws_grafana
from . import aws_greengrass
from . import aws_greengrassv2
from . import aws_groundstation
from . import aws_guardduty
from . import aws_healthimaging
from . import aws_healthlake
from . import aws_iam
from . import aws_identitystore
from . import aws_imagebuilder
from . import aws_inspector
from . import aws_inspectorv2
from . import aws_internetmonitor
from . import aws_invoicing
from . import aws_iot
from . import aws_iotanalytics
from . import aws_iotcoredeviceadvisor
from . import aws_iotevents
from . import aws_iotfleethub
from . import aws_iotfleetwise
from . import aws_iotsitewise
from . import aws_iotthingsgraph
from . import aws_iottwinmaker
from . import aws_iotwireless
from . import aws_ivs
from . import aws_ivschat
from . import aws_kafkaconnect
from . import aws_kendra
from . import aws_kendraranking
from . import aws_kinesis
from . import aws_kinesisanalytics
from . import aws_kinesisanalyticsv2
from . import aws_kinesisfirehose
from . import aws_kinesisvideo
from . import aws_kms
from . import aws_lakeformation
from . import aws_lambda
from . import aws_launchwizard
from . import aws_lex
from . import aws_licensemanager
from . import aws_lightsail
from . import aws_location
from . import aws_logs
from . import aws_lookoutequipment
from . import aws_lookoutmetrics
from . import aws_lookoutvision
from . import aws_m2
from . import aws_macie
from . import aws_managedblockchain
from . import aws_mediaconnect
from . import aws_mediaconvert
from . import aws_medialive
from . import aws_mediapackage
from . import aws_mediapackagev2
from . import aws_mediastore
from . import aws_mediatailor
from . import aws_memorydb
from . import aws_mpa
from . import aws_msk
from . import aws_mwaa
from . import aws_mwaaserverless
from . import aws_neptune
from . import aws_neptunegraph
from . import aws_networkfirewall
from . import aws_networkmanager
from . import aws_nimblestudio
from . import aws_notifications
from . import aws_notificationscontacts
from . import aws_oam
from . import aws_observabilityadmin
from . import aws_odb
from . import aws_omics
from . import aws_opensearchserverless
from . import aws_opensearchservice
from . import aws_opsworks
from . import aws_opsworkscm
from . import aws_organizations
from . import aws_osis
from . import aws_panorama
from . import aws_paymentcryptography
from . import aws_pcaconnectorad
from . import aws_pcaconnectorscep
from . import aws_pcs
from . import aws_personalize
from . import aws_pinpoint
from . import aws_pinpointemail
from . import aws_pipes
from . import aws_proton
from . import aws_qbusiness
from . import aws_qldb
from . import aws_quicksight
from . import aws_ram
from . import aws_rbin
from . import aws_rds
from . import aws_redshift
from . import aws_redshiftserverless
from . import aws_refactorspaces
from . import aws_rekognition
from . import aws_resiliencehub
from . import aws_resourceexplorer2
from . import aws_resourcegroups
from . import aws_robomaker
from . import aws_rolesanywhere
from . import aws_route53
from . import aws_route53profiles
from . import aws_route53recoverycontrol
from . import aws_route53recoveryreadiness
from . import aws_route53resolver
from . import aws_rtbfabric
from . import aws_rum
from . import aws_s3
from . import aws_s3express
from . import aws_s3objectlambda
from . import aws_s3outposts
from . import aws_s3tables
from . import aws_s3vectors
from . import aws_sagemaker
from . import aws_sam
from . import aws_scheduler
from . import aws_sdb
from . import aws_secretsmanager
from . import aws_securityhub
from . import aws_securitylake
from . import aws_servicecatalog
from . import aws_servicecatalogappregistry
from . import aws_servicediscovery
from . import aws_ses
from . import aws_shield
from . import aws_signer
from . import aws_simspaceweaver
from . import aws_smsvoice
from . import aws_sns
from . import aws_sqs
from . import aws_ssm
from . import aws_ssmcontacts
from . import aws_ssmguiconnect
from . import aws_ssmincidents
from . import aws_ssmquicksetup
from . import aws_sso
from . import aws_stepfunctions
from . import aws_supportapp
from . import aws_synthetics
from . import aws_systemsmanagersap
from . import aws_timestream
from . import aws_transfer
from . import aws_verifiedpermissions
from . import aws_voiceid
from . import aws_vpclattice
from . import aws_waf
from . import aws_wafregional
from . import aws_wafv2
from . import aws_wisdom
from . import aws_workspaces
from . import aws_workspacesinstances
from . import aws_workspacesthinclient
from . import aws_workspacesweb
from . import aws_xray

def _typecheckingstub__c5aaa43a6d0a198f8a3f9e8ab7ee8ce8d940df80e550839a285b920b7d6e816f(
    *,
    account: builtins.str,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IEnvironmentAware]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
