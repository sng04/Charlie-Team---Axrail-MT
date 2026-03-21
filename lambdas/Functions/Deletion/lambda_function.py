"""
Deletion Lambda handler.

Triggered by S3 OBJECT_REMOVED events. Deletes all OpenSearch documents
that match the removed file's source_file field.
"""

import os

import boto3
from aws_lambda_powertools import Logger, Tracer
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

logger = Logger()
tracer = Tracer()

OPENSEARCH_ENDPOINT = os.environ.get("OPENSEARCH_ENDPOINT", "")
INDEX_NAME = os.environ.get("INDEX_NAME", "knowledge-vectors")


@tracer.capture_method
def _get_opensearch_client() -> OpenSearch:
    """Build an OpenSearch client authenticated with IAM SigV4."""
    credentials = boto3.Session().get_credentials()
    region = os.environ.get("AWS_REGION", "ap-southeast-1")
    awsauth = AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        region,
        "es",
        session_token=credentials.token,
    )
    return OpenSearch(
        hosts=[{"host": OPENSEARCH_ENDPOINT, "port": 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
    )


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Process S3 OBJECT_REMOVED events: delete matching OpenSearch docs."""
    os_client = _get_opensearch_client()

    for record in event.get("Records", []):
        key = record["s3"]["object"]["key"]
        source_file = key.split("/")[-1]
        logger.info("Processing deletion", extra={"source_file": source_file, "key": key})

        try:
            resp = os_client.search(
                index=INDEX_NAME,
                body={
                    "query": {"term": {"source_file": source_file}},
                    "_source": False,
                },
                size=10000,
            )

            hits = resp.get("hits", {}).get("hits", [])
            if not hits:
                logger.info("No documents found", extra={"source_file": source_file})
                continue

            for hit in hits:
                os_client.delete(index=INDEX_NAME, id=hit["_id"])

            logger.info(
                "Deleted documents",
                extra={"count": len(hits), "source_file": source_file},
            )

        except Exception:
            logger.exception(
                "Failed to delete vectors",
                extra={"source_file": source_file},
            )
            tracer.put_annotation("error", "deletion_failed")
            raise

    return {"statusCode": 200, "body": "Deletion complete"}
