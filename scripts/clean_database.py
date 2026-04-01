"""
Clean Database — Wipe all data from DynamoDB tables except Users and BotCredentials.

Tables cleared:
  - Skills, AgentSkills, Agents, Personalities, Projects, ProjectUsers
  - Sessions, Transcripts, QAPairs, SuggestedQuestions
  - GapAnalysisResults, KbDocuments, AgentConfigHistory
  - AdminChangelog, TokenUsage, BotPool

Tables preserved:
  - Users (user accounts)
  - BotCredentials (Gmail bot accounts)

Also clears the OpenSearch knowledge-vectors index.

Run:
    AWS_SHARED_CREDENTIALS_FILE=.aws/credentials python scripts/clean_database.py
    AWS_SHARED_CREDENTIALS_FILE=.aws/credentials python scripts/clean_database.py --confirm
"""

import argparse
import sys
import time

import boto3
from botocore.exceptions import ClientError

REGION = "ap-southeast-1"
ENV = "dev"

dynamodb = boto3.resource("dynamodb", region_name=REGION)

# Table name → (partition_key, sort_key or None)
TABLES_TO_CLEAR = {
    f"{ENV}-Skills":               ("skill_id", None),
    f"{ENV}-AgentSkills":          ("agent_id", "skill_id"),
    f"{ENV}-Agents":               ("agent_id", None),
    f"{ENV}-Personalities":        ("personality_id", None),
    f"{ENV}-Projects":             ("project_id", None),
    f"{ENV}-ProjectUsers":         ("project_user_id", None),
    f"{ENV}-Sessions":             ("session_id", None),
    f"{ENV}-Transcripts":          ("session_id", "timestamp"),
    f"{ENV}-QAPairs":              ("qa_pair_id", None),
    f"{ENV}-SuggestedQuestions":   ("question_id", None),
    f"{ENV}-GapAnalysisResults":   ("session_id", None),
    f"{ENV}-KbDocuments":          ("document_id", None),
    f"{ENV}-AgentConfigHistory":   ("agent_id", "version"),
    f"{ENV}-AdminChangelog":       ("changelog_id", None),
    f"{ENV}-TokenUsage":           ("usage_id", None),
    f"{ENV}-BotPool":              ("container_id", None),
}

PRESERVED = [f"{ENV}-Users", f"{ENV}-BotCredentials"]


def _clear_table(table_name, pk, sk=None):
    """Delete all items from a DynamoDB table using batch_writer."""
    table = dynamodb.Table(table_name)
    deleted = 0
    scan_kwargs = {"ProjectionExpression": f"#pk{', #sk' if sk else ''}",
                   "ExpressionAttributeNames": {"#pk": pk, **({"#sk": sk} if sk else {})}}

    while True:
        resp = table.scan(**scan_kwargs)
        items = resp.get("Items", [])
        if not items:
            break

        with table.batch_writer() as batch:
            for item in items:
                key = {pk: item[pk]}
                if sk:
                    key[sk] = item[sk]
                batch.delete_item(Key=key)
                deleted += 1

        if "LastEvaluatedKey" not in resp:
            break
        scan_kwargs["ExclusiveStartKey"] = resp["LastEvaluatedKey"]

    return deleted


def _clear_opensearch():
    """Delete all documents from the knowledge-vectors index."""
    try:
        import requests
        from requests_aws4auth import AWS4Auth

        credentials = boto3.Session(region_name=REGION).get_credentials().get_frozen_credentials()
        auth = AWS4Auth(credentials.access_key, credentials.secret_key, REGION, "es",
                        session_token=credentials.token)

        # Get the OpenSearch endpoint from CloudFormation exports
        cf = boto3.client("cloudformation", region_name=REGION)
        exports = {}
        paginator = cf.get_paginator("list_exports")
        for page in paginator.paginate():
            for exp in page["Exports"]:
                exports[exp["Name"]] = exp["Value"]

        endpoint = exports.get(f"AXRAIL-OpenSearchDomainEndpoint-{ENV}", "")
        if not endpoint:
            print("  OpenSearch endpoint not found in exports, skipping")
            return 0

        url = f"https://{endpoint}/knowledge-vectors/_delete_by_query"
        resp = requests.post(url, json={"query": {"match_all": {}}}, auth=auth,
                             headers={"Content-Type": "application/json"}, timeout=30)
        if resp.status_code == 200:
            deleted = resp.json().get("deleted", 0)
            return deleted
        else:
            print(f"  OpenSearch delete failed: {resp.status_code} {resp.text[:200]}")
            return 0
    except ImportError:
        print("  requests/requests_aws4auth not available, skipping OpenSearch")
        return 0
    except Exception as e:
        print(f"  OpenSearch error: {e}")
        return 0


def main():
    parser = argparse.ArgumentParser(description="Clean all data tables (preserves Users & BotCredentials)")
    parser.add_argument("--confirm", action="store_true", help="Actually delete. Without this flag, dry-run only.")
    args = parser.parse_args()
    dry_run = not args.confirm

    print(f"Mode: {'DRY RUN' if dry_run else '⚠️  LIVE DELETE'}")
    print(f"Region: {REGION}, Env: {ENV}")
    print(f"\nPreserved: {', '.join(PRESERVED)}")
    print(f"Tables to clear: {len(TABLES_TO_CLEAR)}\n")

    if not dry_run:
        print("⚠️  This will permanently delete all data from the listed tables.")
        print("    Press Ctrl+C within 5 seconds to abort...")
        time.sleep(5)
        print()

    total = 0
    for table_name, (pk, sk) in TABLES_TO_CLEAR.items():
        table = dynamodb.Table(table_name)
        try:
            count = table.scan(Select="COUNT").get("Count", 0)
        except ClientError:
            print(f"  SKIP {table_name} (table not found)")
            continue

        if count == 0:
            print(f"  {table_name}: empty")
            continue

        if dry_run:
            print(f"  {table_name}: {count} items (would delete)")
            total += count
        else:
            deleted = _clear_table(table_name, pk, sk)
            print(f"  {table_name}: deleted {deleted} items")
            total += deleted

    # OpenSearch
    print()
    if dry_run:
        print("  OpenSearch knowledge-vectors: (would clear)")
    else:
        os_deleted = _clear_opensearch()
        print(f"  OpenSearch knowledge-vectors: deleted {os_deleted} documents")

    print(f"\n{'Would delete' if dry_run else 'Deleted'} {total} total DynamoDB items")
    if dry_run and total > 0:
        print("Run with --confirm to execute.")


if __name__ == "__main__":
    main()
