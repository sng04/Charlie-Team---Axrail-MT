#!/usr/bin/env python3
"""Delete duplicate and orphaned records from DynamoDB tables.

Cleans:
  - dev-Agents: dedup by agent_name, keep newest
  - dev-Personalities: dedup by personality_name, keep newest. Remove TestPersonality-* leftovers.
  - dev-Projects: dedup by name, keep newest. Remove TestProject-* leftovers.
  - dev-Skills: dedup by skill_name (global), keep newest. Remove UpdatedSkill leftovers.
  - dev-Sessions: dedup by name, keep newest. Remove test-ws-* and TestSession-* leftovers.

Usage:
    AWS_SHARED_CREDENTIALS_FILE=.aws/credentials python scripts/cleanup_duplicates.py
"""

import os

import boto3

REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
dynamodb = boto3.resource("dynamodb", region_name=REGION)


def _dedup_table(table_name, pk, name_field, group_fields=None, junk_prefixes=None):
    """Remove duplicates and junk records from a table."""
    if group_fields is None:
        group_fields = [name_field]
    if junk_prefixes is None:
        junk_prefixes = []

    table = dynamodb.Table(table_name)
    items = table.scan().get("Items", [])
    print(f"\n── {table_name} ({len(items)} items) ──")

    deleted = 0

    # Remove junk/test records first
    for item in items:
        name = item.get(name_field, "")
        if any(name.startswith(p) for p in junk_prefixes):
            print(f"  JUNK: deleting {item[pk][:12]}.. ({name})")
            table.delete_item(Key={pk: item[pk]})
            deleted += 1

    # Re-scan after junk removal
    items = table.scan().get("Items", [])

    # Group by name fields
    groups = {}
    for item in items:
        key = tuple(item.get(f, "") for f in group_fields)
        groups.setdefault(key, []).append(item)

    for key, group in groups.items():
        if len(group) <= 1:
            continue
        group.sort(key=lambda x: x.get("created_at", ""), reverse=True)
        keeper = group[0]
        name_display = " / ".join(str(k) for k in key)
        print(f"  DUP: {name_display} — {len(group)} copies, keeping {keeper[pk][:12]}.. ({keeper.get('created_at', 'N/A')})")
        for dup in group[1:]:
            table.delete_item(Key={pk: dup[pk]})
            deleted += 1

    remaining = table.scan(Select="COUNT").get("Count", 0)
    print(f"  Deleted: {deleted}, Remaining: {remaining}")
    return deleted


def main():
    total = 0

    total += _dedup_table(
        "dev-Agents", "agent_id", "agent_name",
        junk_prefixes=["UpdatedTest"],
    )

    total += _dedup_table(
        "dev-Personalities", "personality_id", "personality_name",
        junk_prefixes=["TestPersonality-"],
    )

    total += _dedup_table(
        "dev-Projects", "project_id", "name",
        junk_prefixes=["TestProject-"],
    )

    total += _dedup_table(
        "dev-Skills", "skill_id", "skill_name",
        group_fields=["skill_name"],
        junk_prefixes=["UpdatedSkill", "TestSkill-"],
    )

    total += _dedup_table(
        "dev-Sessions", "session_id", "name",
        junk_prefixes=["test-ws-", "TestSession-", "quick-test"],
    )

    print(f"\nDone. Total removed: {total}")


if __name__ == "__main__":
    main()
