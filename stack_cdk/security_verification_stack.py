"""Stack to deploy AWS Security Agent verification files to the existing frontend S3 bucket.

This places the verification files into the S3 bucket that serves as the
origin for the existing CloudFront distribution, then invalidates the
CloudFront cache so the files are immediately accessible.
"""

import json

from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_cloudfront as cloudfront,
)
from constructs import Construct

VERIFICATION_PAYLOAD = json.dumps(
    {"tokens": ["jP2oeFgO9BqJJGZmVvkSXA"]},
    separators=(",", ":"),
)


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

        # Deploy the verification JSON file to the bucket root.
        # BucketDeployment uses a Lambda-backed custom resource that
        # also triggers a CloudFront invalidation after upload.
        s3deploy.BucketDeployment(
            self,
            "SecurityAgentFile",
            sources=[
                s3deploy.Source.data(
                    "securityagent.json",
                    VERIFICATION_PAYLOAD,
                ),
            ],
            destination_bucket=bucket,
            # Only deploy this single file — do not prune other objects
            prune=False,
            # Invalidate CloudFront cache for this path after deployment
            distribution=distribution,
            distribution_paths=["/securityagent.json"],
        )

        # Deploy the .well-known verification file
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
                "/securityagent.json",
                "/.well-known/aws/securityagent-domain-verification.json",
            ],
        )
