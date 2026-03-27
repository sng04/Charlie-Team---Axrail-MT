#!/usr/bin/env python3
"""Migrate agent-skill relationships from one-to-many to many-to-many.

For each skill with an agent_id:
1. Create a junction record in AgentSkills table
2. Copy S3 object from {agent_id}/{skill_id}/{filename} to {skill_id}/{filename}
3. Update skill record's s3_key to new format
4. Delete old S3 object
5. Remove agent_id attribute from skill record

Usage:
    AWS_SHARED_CREDENTIALS_FILE=.aws/credentials python scripts/migrate_agent_skills.py
"""

import os

import boto3

REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
SKILLS_TABLE = os.environ.get("SKILLS_TABLE_NAME", "dev-Skills")
AGENT_SKILLS_TABLE = os.environ.get("AGENT_SKILLS_TABLE_NAME", "dev-AgentSkills")
SKILLS_BUCKET = os.environ.get("SKILLS_BUCKET", "axrail-skills-dev-848332098006")

dynamodb = boto3.resource("dynamodb", region_name=REGION)
s3 = boto3.client("s3", region_name=REGION)

skills_table = dynamodb.Table(SKILLS_TABLE)
agent_skills_table = dynamodb.Table(AGENT_SKILLS_TABLE)


def main():
    items = skills_table.scan().get("Items", [])
    print(f"Found {len(items)} skills")

    migrated = 0
    skipped = 0

    for item in items:
        skill_id = item["skill_id"]
        agent_id = item.get("agent_id")
        old_s3_key = item.get("s3_key", "")

        if not agent_id:
            print(f"  SKIP {skill_id} — no agent_id")
            skipped += 1
            continue

        # 1. Create junction record
        from datetime import datetime, timezone
        agent_skills_table.put_item(Item={
            "agent_id": agent_id,
            "skill_id": skill_id,
            "assigned_at": datetime.now(timezone.utc).isoformat(),
        })
        print(f"  Junction: {agent_id} → {skill_id}")

        # 2. Copy S3 object to new key format if needed
        if old_s3_key and old_s3_key.count("/") >= 2:
            parts = old_s3_key.split("/")
            filename = "/".join(parts[2:])
            new_s3_key = f"{skill_id}/{filename}"

            if old_s3_key != new_s3_key:
                try:
                    s3.copy_object(
                        Bucket=SKILLS_BUCKET,
                        CopySource={"Bucket": SKILLS_BUCKET, "Key": old_s3_key},
                        Key=new_s3_key,
                    )
                    s3.delete_object(Bucket=SKILLS_BUCKET, Key=old_s3_key)
                    print(f"  S3: {old_s3_key} → {new_s3_key}")
                except Exception as e:
                    print(f"  S3 WARN: {e}")
                    new_s3_key = old_s3_key  # keep old key if copy fails
            else:
                new_s3_key = old_s3_key
        else:
            new_s3_key = old_s3_key

        # 3. Update skill record: new s3_key, remove agent_id
        skills_table.update_item(
            Key={"skill_id": skill_id},
            UpdateExpression="SET s3_key = :k REMOVE agent_id",
            ExpressionAttributeValues={":k": new_s3_key},
        )

        migrated += 1

    print(f"\nDone. Migrated: {migrated}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
