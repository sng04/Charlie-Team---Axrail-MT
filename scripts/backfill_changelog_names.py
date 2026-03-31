"""
Backfill entity_name on AdminChangelog entries that are missing it.

For each entry without entity_name, looks up the entity's human-readable name
from the corresponding DynamoDB table based on entity_type and entity_id.

Run:
    AWS_SHARED_CREDENTIALS_FILE=.aws/credentials python scripts/backfill_changelog_names.py

Options:
    --dry-run    Show what would be updated without writing (default)
    --apply      Actually write updates to DynamoDB
"""

import argparse
import sys

import boto3

REGION = "ap-southeast-1"
ENV = "dev"

dynamodb = boto3.resource("dynamodb", region_name=REGION)

changelog_table = dynamodb.Table(f"{ENV}-AdminChangelog")
users_table = dynamodb.Table(f"{ENV}-Users")
projects_table = dynamodb.Table(f"{ENV}-Projects")
agents_table = dynamodb.Table(f"{ENV}-Agents")
personalities_table = dynamodb.Table(f"{ENV}-Personalities")
skills_table = dynamodb.Table(f"{ENV}-Skills")
bot_credentials_table = dynamodb.Table(f"{ENV}-BotCredentials")

# Caches to avoid repeated lookups
_cache = {}


def _lookup(table, key_name, key_value, name_field):
    """Look up a name field from a table, with caching."""
    cache_key = f"{table.table_name}:{key_value}"
    if cache_key in _cache:
        return _cache[cache_key]
    try:
        resp = table.get_item(Key={key_name: key_value})
        item = resp.get("Item", {})
        name = item.get(name_field, "")
        _cache[cache_key] = name
        return name
    except Exception:
        _cache[cache_key] = ""
        return ""


def _resolve_name(entry):
    """Resolve entity_name from entity_type + entity_id + data/previous_data."""
    entity_type = entry.get("entity_type", "")
    entity_id = entry.get("entity_id", "")
    data = entry.get("data") or {}
    prev = entry.get("previous_data") or {}

    if entity_type == "user":
        # Try data/previous_data first, then look up
        name = data.get("email") or prev.get("email") or ""
        if not name:
            name = _lookup(users_table, "user_id", entity_id, "email")
        return name

    if entity_type == "project":
        name = data.get("name") or prev.get("name") or ""
        if not name:
            name = _lookup(projects_table, "project_id", entity_id, "name")
        return name

    if entity_type == "agent":
        name = data.get("agent_name") or prev.get("agent_name") or ""
        if not name:
            name = _lookup(agents_table, "agent_id", entity_id, "agent_name")
        return name

    if entity_type == "personality":
        name = data.get("personality_name") or prev.get("personality_name") or ""
        if not name:
            name = _lookup(personalities_table, "personality_id", entity_id, "personality_name")
        return name

    if entity_type == "skill":
        name = data.get("skill_name") or prev.get("skill_name") or ""
        if not name:
            name = _lookup(skills_table, "skill_id", entity_id, "skill_name")
        return name

    if entity_type == "bot_credential":
        name = data.get("email") or prev.get("email") or ""
        if not name:
            name = _lookup(bot_credentials_table, "credential_id", entity_id, "email")
        return name

    if entity_type == "login_attempt":
        # entity_id is already the username/email
        return entry.get("admin_username") or entity_id

    if entity_type == "project_user_assignment":
        # Try to build "user_email → project_name" from data/previous_data
        rec = data or prev
        user_id = rec.get("user_id", "")
        project_id = rec.get("project_id", "")
        user_email = _lookup(users_table, "user_id", user_id, "email") if user_id else ""
        project_name = _lookup(projects_table, "project_id", project_id, "name") if project_id else ""
        if user_email and project_name:
            return f"{user_email} \u2192 {project_name}"
        return user_email or project_name or ""

    if entity_type == "agent_skill_assignment":
        # entity_id is "agent_id:skill_id"
        parts = entity_id.split(":", 1)
        if len(parts) == 2:
            agent_name = _lookup(agents_table, "agent_id", parts[0], "agent_name")
            skill_name = _lookup(skills_table, "skill_id", parts[1], "skill_name")
            if agent_name and skill_name:
                return f"{agent_name} \u2192 {skill_name}"
            return agent_name or skill_name or ""
        return ""

    return ""


def main():
    parser = argparse.ArgumentParser(description="Backfill entity_name on changelog entries")
    parser.add_argument("--apply", action="store_true", help="Write updates (default is dry-run)")
    args = parser.parse_args()
    dry_run = not args.apply

    print(f"Mode: {'DRY RUN' if dry_run else 'APPLY'}")
    print(f"Table: {changelog_table.table_name}\n")

    # Scan all entries missing entity_name
    scan_kwargs = {}
    total = 0
    updated = 0
    skipped = 0

    while True:
        resp = changelog_table.scan(**scan_kwargs)
        items = resp.get("Items", [])

        for entry in items:
            total += 1
            if entry.get("entity_name"):
                continue  # Already has a name

            name = _resolve_name(entry)
            if not name:
                skipped += 1
                cid = entry["changelog_id"][:8]
                print(f"  SKIP {cid}... {entry.get('entity_type')}/{entry.get('action')} — no name resolvable")
                continue

            updated += 1
            cid = entry["changelog_id"][:8]
            print(f"  {'WOULD UPDATE' if dry_run else 'UPDATE'} {cid}... {entry.get('entity_type')}/{entry.get('action')} → \"{name}\"")

            if not dry_run:
                changelog_table.update_item(
                    Key={"changelog_id": entry["changelog_id"]},
                    UpdateExpression="SET entity_name = :n",
                    ExpressionAttributeValues={":n": name},
                )

        if "LastEvaluatedKey" not in resp:
            break
        scan_kwargs["ExclusiveStartKey"] = resp["LastEvaluatedKey"]

    print(f"\nDone. Scanned {total}, {'would update' if dry_run else 'updated'} {updated}, skipped {skipped}")
    if dry_run and updated > 0:
        print("Run with --apply to write changes.")


if __name__ == "__main__":
    main()
