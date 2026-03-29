"""
Backfill KbDocuments DynamoDB table from existing S3 objects.

Scans the KB S3 bucket for all project files and creates DynamoDB records
for any that don't already have tracking entries.

Run:
    AWS_SHARED_CREDENTIALS_FILE=.aws/credentials python scripts/backfill_kb_documents.py
"""

import os
import uuid
from datetime import datetime, timezone

import boto3

REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
KB_BUCKET = os.environ.get("KB_BUCKET", "axrail-kb-dev-848332098006")
KB_DOCUMENTS_TABLE = os.environ.get("KB_DOCUMENTS_TABLE", "dev-KbDocuments")

s3 = boto3.client("s3", region_name=REGION)
dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(KB_DOCUMENTS_TABLE)


def get_existing_s3_keys():
    """Get all s3_keys already tracked in DynamoDB."""
    existing = set()
    resp = table.scan(ProjectionExpression="s3_key")
    existing.update(item["s3_key"] for item in resp.get("Items", []))
    while "LastEvaluatedKey" in resp:
        resp = table.scan(
            ProjectionExpression="s3_key",
            ExclusiveStartKey=resp["LastEvaluatedKey"],
        )
        existing.update(item["s3_key"] for item in resp.get("Items", []))
    return existing


def list_s3_objects():
    """List all objects in the KB bucket."""
    objects = []
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=KB_BUCKET):
        for obj in page.get("Contents", []):
            key = obj["Key"]
            # Skip summaries (auto-generated) and non-document files
            if "/summaries/" in key:
                continue
            parts = key.split("/")
            if len(parts) < 2:
                continue
            objects.append({
                "s3_key": key,
                "project_id": parts[0],
                "file_name": "/".join(parts[1:]),
                "size": obj["Size"],
                "last_modified": obj["LastModified"].isoformat(),
            })
    return objects


def backfill():
    existing_keys = get_existing_s3_keys()
    s3_objects = list_s3_objects()

    print(f"S3 objects found: {len(s3_objects)}")
    print(f"Already tracked: {len(existing_keys)}")

    created = 0
    for obj in s3_objects:
        if obj["s3_key"] in existing_keys:
            print(f"  SKIP (exists): {obj['s3_key']}")
            continue

        file_type = obj["file_name"].rsplit(".", 1)[-1].lower() if "." in obj["file_name"] else ""
        item = {
            "document_id": str(uuid.uuid4()),
            "project_id": obj["project_id"],
            "file_name": obj["file_name"],
            "description": "",
            "s3_key": obj["s3_key"],
            "file_type": file_type,
            "status": "active",
            "created_at": obj["last_modified"],
            "updated_at": obj["last_modified"],
        }
        table.put_item(Item=item)
        print(f"  CREATED: {obj['s3_key']} → {item['document_id']}")
        created += 1

    print(f"\nBackfill complete: {created} records created")


if __name__ == "__main__":
    backfill()
