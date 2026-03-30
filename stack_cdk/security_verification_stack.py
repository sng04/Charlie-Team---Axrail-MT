"""Stack to deploy AWS Security Agent verification files and CloudFront behavior.

Deploys verification files to the existing frontend S3 bucket and adds a
dedicated CloudFront cache behavior for `.well-known/*` so the SPA fallback
(403/404 → index.html) never intercepts verification requests.
"""

import json

from aws_cdk import (
    Stack,
    CustomResource,
    Duration,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
    custom_resources as cr,
)
from constructs import Construct

VERIFICATION_PAYLOAD = json.dumps(
    {"tokens": ["jP2oeFgO9BqJJGZmVvkSXA"]},
    separators=(",", ":"),
)

# Managed cache policy ID for CachingDisabled
CACHING_DISABLED_POLICY_ID = "4135ea2d-6df8-44a3-9df3-4b5a84be39ad"


# Lambda code that adds/removes the .well-known/* behavior on the distribution
CF_BEHAVIOR_HANDLER = '''
import json
import boto3
import copy

cf = boto3.client("cloudfront")

def on_event(event, context):
    dist_id = event["ResourceProperties"]["DistributionId"]
    origin_id = event["ResourceProperties"]["OriginId"]
    path_pattern = event["ResourceProperties"]["PathPattern"]
    cache_policy_id = event["ResourceProperties"]["CachePolicyId"]
    request_type = event["RequestType"]

    if request_type in ("Create", "Update"):
        _ensure_behavior(dist_id, origin_id, path_pattern, cache_policy_id)
    elif request_type == "Delete":
        _remove_behavior(dist_id, path_pattern)

    return {"PhysicalResourceId": f"{dist_id}-{path_pattern}"}


def _ensure_behavior(dist_id, origin_id, path_pattern, cache_policy_id):
    resp = cf.get_distribution_config(Id=dist_id)
    config = resp["DistributionConfig"]
    etag = resp["ETag"]

    behavior = {
        "PathPattern": path_pattern,
        "TargetOriginId": origin_id,
        "ViewerProtocolPolicy": "redirect-to-https",
        "AllowedMethods": {
            "Quantity": 2,
            "Items": ["GET", "HEAD"],
            "CachedMethods": {"Quantity": 2, "Items": ["GET", "HEAD"]},
        },
        "Compress": True,
        "CachePolicyId": cache_policy_id,
        "SmoothStreaming": False,
        "FieldLevelEncryptionId": "",
        "LambdaFunctionAssociations": {"Quantity": 0},
        "FunctionAssociations": {"Quantity": 0},
    }

    behaviors = config.get("CacheBehaviors", {"Quantity": 0})
    items = behaviors.get("Items", [])

    # Replace existing behavior with same path pattern, or append
    replaced = False
    for i, b in enumerate(items):
        if b["PathPattern"] == path_pattern:
            items[i] = behavior
            replaced = True
            break
    if not replaced:
        items.append(behavior)

    config["CacheBehaviors"] = {"Quantity": len(items), "Items": items}

    cf.update_distribution(
        Id=dist_id, IfMatch=etag, DistributionConfig=config
    )


def _remove_behavior(dist_id, path_pattern):
    resp = cf.get_distribution_config(Id=dist_id)
    config = resp["DistributionConfig"]
    etag = resp["ETag"]

    behaviors = config.get("CacheBehaviors", {"Quantity": 0})
    items = behaviors.get("Items", [])
    items = [b for b in items if b["PathPattern"] != path_pattern]

    config["CacheBehaviors"] = {"Quantity": len(items), "Items": items}

    cf.update_distribution(
        Id=dist_id, IfMatch=etag, DistributionConfig=config
    )
'''


class SecurityVerificationStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        env_name: str,
        frontend_bucket_name: str,
        cloudfront_distribution_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Import the existing S3 bucket used as CloudFront origin
        bucket = s3.Bucket.from_bucket_name(
            self, "FrontendBucket", frontend_bucket_name
        )

        # Import the existing CloudFront distribution for cache invalidation
        distribution = cloudfront.Distribution.from_distribution_attributes(
            self,
            "FrontendDistribution",
            distribution_id=cloudfront_distribution_id,
            domain_name="d2bed2yjnef4ve.cloudfront.net",
        )

        # --- Deploy verification files to S3 ---

        s3deploy.BucketDeployment(
            self,
            "SecurityAgentFile",
            sources=[
                s3deploy.Source.data("securityagent.json", VERIFICATION_PAYLOAD),
            ],
            destination_bucket=bucket,
            prune=False,
            distribution=distribution,
            distribution_paths=["/securityagent.json"],
        )

        s3deploy.BucketDeployment(
            self,
            "SecurityAgentWellKnownFile",
            sources=[
                s3deploy.Source.data(
                    ".well-known/aws/securityagent-domain-verification.json",
                    VERIFICATION_PAYLOAD,
                ),
            ],
            destination_bucket=bucket,
            prune=False,
            distribution=distribution,
            distribution_paths=[
                "/.well-known/aws/securityagent-domain-verification.json",
            ],
        )

        # --- Add .well-known/* CloudFront behavior via custom resource ---
        # This ensures the SPA fallback (403/404 → index.html) never
        # intercepts requests to the verification path.

        behavior_fn = _lambda.Function(
            self,
            "CfBehaviorFn",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.on_event",
            code=_lambda.Code.from_inline(CF_BEHAVIOR_HANDLER),
            timeout=Duration.minutes(5),
        )

        behavior_fn.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "cloudfront:GetDistributionConfig",
                    "cloudfront:UpdateDistribution",
                ],
                resources=[
                    f"arn:aws:cloudfront::{self.account}:distribution/{cloudfront_distribution_id}"
                ],
            )
        )

        provider = cr.Provider(
            self, "CfBehaviorProvider", on_event_handler=behavior_fn
        )

        # Look up the origin ID from the distribution
        origin_id = "MeetAgentFrontendDistributionOrigin169D33FD7"

        CustomResource(
            self,
            "WellKnownBehavior",
            service_token=provider.service_token,
            properties={
                "DistributionId": cloudfront_distribution_id,
                "OriginId": origin_id,
                "PathPattern": ".well-known/*",
                "CachePolicyId": CACHING_DISABLED_POLICY_ID,
            },
        )
