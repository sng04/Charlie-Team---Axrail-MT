"""Stack to deploy AWS Security Agent verification files and CloudFront behavior.

Deploys verification files to the existing frontend S3 bucket and adds a
dedicated CloudFront cache behavior for ``.well-known/*`` so the SPA fallback
(403/404 → index.html) never intercepts verification requests.

A post-deploy custom resource validates that the file is reachable via
CloudFront with the correct Content-Type and token payload.
"""

import json
import time

from aws_cdk import (
    CfnOutput,
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

# Epoch timestamp forces BucketDeployment custom resources to re-execute on
# every ``cdk deploy``, guaranteeing the verification files are restored even
# when a frontend sync deleted them out-of-band.
_DEPLOY_EPOCH = str(int(time.time()))

VERIFICATION_PAYLOAD = json.dumps(
    {"tokens": ["jP2oeFgO9BqJJGZmVvkSXA"]},
    separators=(",", ":"),
)

# Managed cache policy ID for CachingDisabled
CACHING_DISABLED_POLICY_ID = "4135ea2d-6df8-44a3-9df3-4b5a84be39ad"


# ---------------------------------------------------------------------------
# Lambda: add / remove the .well-known/* CloudFront cache behavior
# ---------------------------------------------------------------------------
CF_BEHAVIOR_HANDLER = '''
import json
import boto3

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

    replaced = False
    for i, b in enumerate(items):
        if b["PathPattern"] == path_pattern:
            items[i] = behavior
            replaced = True
            break
    if not replaced:
        items.append(behavior)

    config["CacheBehaviors"] = {"Quantity": len(items), "Items": items}
    cf.update_distribution(Id=dist_id, IfMatch=etag, DistributionConfig=config)


def _remove_behavior(dist_id, path_pattern):
    resp = cf.get_distribution_config(Id=dist_id)
    config = resp["DistributionConfig"]
    etag = resp["ETag"]

    behaviors = config.get("CacheBehaviors", {"Quantity": 0})
    items = behaviors.get("Items", [])
    items = [b for b in items if b["PathPattern"] != path_pattern]

    config["CacheBehaviors"] = {"Quantity": len(items), "Items": items}
    cf.update_distribution(Id=dist_id, IfMatch=etag, DistributionConfig=config)
'''

# ---------------------------------------------------------------------------
# Lambda: post-deploy validation — HEAD the verification URL and assert
# HTTP 200, application/json Content-Type, and correct token payload.
# ---------------------------------------------------------------------------
VERIFICATION_VALIDATOR_HANDLER = '''
import json
import time
import urllib.request
import urllib.error

def on_event(event, context):
    if event["RequestType"] == "Delete":
        return {"PhysicalResourceId": event.get("PhysicalResourceId", "validator")}

    url = event["ResourceProperties"]["VerificationUrl"]
    expected_token = event["ResourceProperties"]["ExpectedToken"]
    max_retries = int(event["ResourceProperties"].get("MaxRetries", "5"))

    result = _validate(url, expected_token, max_retries)
    print(json.dumps(result))

    if result["status"] != "PASS":
        raise RuntimeError(
            f"Domain verification FAILED: {result['reason']}"
        )

    return {
        "PhysicalResourceId": "validator",
        "Data": result,
    }


def _validate(url, expected_token, max_retries):
    """Retry with back-off to allow CloudFront invalidation to propagate."""
    last_error = None
    for attempt in range(max_retries):
        if attempt > 0:
            time.sleep(min(2 ** attempt, 30))
        try:
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=10) as resp:
                status = resp.status
                content_type = resp.headers.get("Content-Type", "")
                body = resp.read().decode("utf-8")

            if status != 200:
                last_error = f"HTTP {status}"
                continue

            if "application/json" not in content_type:
                last_error = f"Content-Type is '{content_type}', expected application/json"
                continue

            try:
                payload = json.loads(body)
            except json.JSONDecodeError:
                last_error = "Response body is not valid JSON"
                continue

            tokens = payload.get("tokens", [])
            if expected_token not in tokens:
                last_error = f"Token '{expected_token}' not found in response"
                continue

            return {
                "status": "PASS",
                "http_status": status,
                "content_type": content_type,
                "token_present": True,
                "reason": "All checks passed",
            }

        except urllib.error.HTTPError as e:
            last_error = f"HTTP {e.code}"
        except Exception as e:
            last_error = str(e)

    return {
        "status": "FAIL",
        "reason": last_error or "Unknown error after retries",
    }
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

        # --- Deploy verification files to S3 (with correct Content-Type) ---

        # _DEPLOY_EPOCH in the marker file forces the custom resource to
        # re-execute on every deploy, restoring files deleted out-of-band.
        s3deploy.BucketDeployment(
            self,
            "SecurityAgentFile",
            sources=[
                s3deploy.Source.data("securityagent.json", VERIFICATION_PAYLOAD),
                s3deploy.Source.data(".deploy-marker", _DEPLOY_EPOCH),
            ],
            destination_bucket=bucket,
            prune=False,
            content_type="application/json",
            cache_control=[
                s3deploy.CacheControl.no_cache(),
            ],
            distribution=distribution,
            distribution_paths=["/securityagent.json"],
        )

        well_known_deployment = s3deploy.BucketDeployment(
            self,
            "SecurityAgentWellKnownFile",
            sources=[
                s3deploy.Source.data(
                    ".well-known/aws/securityagent-domain-verification.json",
                    VERIFICATION_PAYLOAD,
                ),
                s3deploy.Source.data(".well-known/.deploy-marker", _DEPLOY_EPOCH),
            ],
            destination_bucket=bucket,
            prune=False,
            content_type="application/json",
            cache_control=[
                s3deploy.CacheControl.no_cache(),
            ],
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

        well_known_behavior = CustomResource(
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

        # --- Post-deploy validation custom resource ---
        verification_url = (
            f"https://d2bed2yjnef4ve.cloudfront.net"
            f"/.well-known/aws/securityagent-domain-verification.json"
        )

        validator_fn = _lambda.Function(
            self,
            "VerificationValidatorFn",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.on_event",
            code=_lambda.Code.from_inline(VERIFICATION_VALIDATOR_HANDLER),
            timeout=Duration.minutes(5),
        )

        validator_provider = cr.Provider(
            self, "VerificationValidatorProvider", on_event_handler=validator_fn
        )

        validator = CustomResource(
            self,
            "VerificationValidator",
            service_token=validator_provider.service_token,
            properties={
                "VerificationUrl": verification_url,
                "ExpectedToken": "jP2oeFgO9BqJJGZmVvkSXA",
                "MaxRetries": "5",
                # Force re-validation on every deploy
                "DeployTimestamp": str(self.node.addr),
            },
        )

        # Validator must run after the file is deployed and behavior is set
        validator.node.add_dependency(well_known_deployment)
        validator.node.add_dependency(well_known_behavior)

        # --- Outputs ---
        CfnOutput(
            self,
            "VerificationFileUrl",
            value=verification_url,
            description="URL for AWS Security Agent domain verification",
        )

        CfnOutput(
            self,
            "VerificationStatus",
            value=validator.get_att_string("status"),
            description="Post-deploy verification result (PASS/FAIL)",
        )
