"""Strands agent tools for knowledge base search, transcript retrieval, and QA pairs."""

import json
import logging
import os
import uuid
from datetime import datetime, timezone

import boto3
from boto3.dynamodb.conditions import Key
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from strands import tool

logger = logging.getLogger()
logger.setLevel(logging.INFO)

OPENSEARCH_ENDPOINT = os.environ.get("OPENSEARCH_ENDPOINT", "")
INDEX_NAME = os.environ.get("INDEX_NAME", "knowledge-vectors")
BEDROCK_REGION = os.environ.get("BEDROCK_REGION", "us-east-1")
TRANSCRIPTS_TABLE_NAME = os.environ.get("TRANSCRIPTS_TABLE_NAME", "")
QA_PAIRS_TABLE_NAME = os.environ.get("QA_PAIRS_TABLE_NAME", "")
KB_BUCKET_NAME = os.environ.get("KB_BUCKET_NAME", "")
SKILLS_TABLE_NAME = os.environ.get("SKILLS_TABLE_NAME", "")

_os_client = None
_bedrock_client = None
_dynamodb = None
_s3_client = None


def _get_os_client() -> OpenSearch:
    """Build an IAM-authenticated OpenSearch client (cached)."""
    global _os_client
    if _os_client is not None:
        return _os_client
    credentials = boto3.Session().get_credentials()
    region = os.environ.get("AWS_REGION", "ap-southeast-1")
    awsauth = AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        region,
        "es",
        session_token=credentials.token,
    )
    _os_client = OpenSearch(
        hosts=[{"host": OPENSEARCH_ENDPOINT, "port": 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
    )
    return _os_client


def _get_bedrock_client():
    """Return a cached Bedrock runtime client for us-east-1."""
    global _bedrock_client
    if _bedrock_client is None:
        _bedrock_client = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)
    return _bedrock_client


def _get_transcripts_table():
    """Return a cached DynamoDB Table resource for transcripts."""
    global _dynamodb
    if _dynamodb is None:
        _dynamodb = boto3.resource("dynamodb")
    return _dynamodb.Table(TRANSCRIPTS_TABLE_NAME)


def _get_qa_pairs_table():
    """Return a cached DynamoDB Table resource for QA pairs."""
    global _dynamodb
    if _dynamodb is None:
        _dynamodb = boto3.resource("dynamodb")
    return _dynamodb.Table(QA_PAIRS_TABLE_NAME)


def _get_s3_client():
    """Return a cached S3 client."""
    global _s3_client
    if _s3_client is None:
        _s3_client = boto3.client("s3")
    return _s3_client


def _get_skills_table():
    """Return a cached DynamoDB Table resource for skills."""
    global _dynamodb
    if _dynamodb is None:
        _dynamodb = boto3.resource("dynamodb")
    return _dynamodb.Table(SKILLS_TABLE_NAME)


def _generate_embedding(text: str) -> list:
    """Generate a 1024-dim embedding via Bedrock Titan Embed V2."""
    client = _get_bedrock_client()
    payload = json.dumps({"inputText": text, "dimensions": 1024, "normalize": True})
    response = client.invoke_model(
        modelId="amazon.titan-embed-text-v2:0",
        contentType="application/json",
        accept="application/json",
        body=payload,
    )
    body = json.loads(response["body"].read())
    return body["embedding"]


@tool
def search_knowledge_base(query: str, project_id: str = "default-project") -> str:
    """Search the project knowledge base for relevant information.

    Args:
        query: The search query to find relevant documents.
        project_id: The project ID to filter results by.

    Returns:
        Formatted search results from the knowledge base.
    """
    try:
        embedding = _generate_embedding(query)
        search_body = {
            "size": 5,
            "query": {
                "bool": {
                    "must": [{"knn": {"embedding": {"vector": embedding, "k": 5}}}],
                    "filter": [{"term": {"project_id": project_id}}],
                }
            },
        }
        results = _get_os_client().search(index=INDEX_NAME, body=search_body)
        hits = results["hits"]["hits"]
        if not hits:
            return "No relevant documents found in the knowledge base."

        formatted = []
        for i, hit in enumerate(hits, 1):
            src = hit["_source"]
            score = hit["_score"]
            text = src.get("text", "")
            source_file = src.get("source_file", "unknown")
            formatted.append(
                f"[{i}] (score: {score:.4f}, source: {source_file})\n{text}"
            )
        return "\n\n".join(formatted)
    except Exception as exc:
        logger.exception("Knowledge base search failed")
        return f"Error searching knowledge base: {exc}"


@tool
def get_session_transcript(session_id: str) -> str:
    """Retrieve the transcript for a meeting session.

    Args:
        session_id: The session ID to retrieve transcripts for.

    Returns:
        Formatted transcript entries sorted by timestamp.
    """
    try:
        table = _get_transcripts_table()
        response = table.query(
            KeyConditionExpression=Key("session_id").eq(session_id),
        )
        items = response.get("Items", [])
        if not items:
            return f"No transcript entries found for session {session_id}."

        # No sort needed — composite key SK guarantees order
        formatted = []
        for item in items:
            speaker = item.get("speaker", "Unknown")
            text = item.get("text", "")
            ts = item.get("timestamp", "")
            formatted.append(f"[{ts}] {speaker}: {text}")
        return "\n".join(formatted)
    except Exception as exc:
        logger.exception("Transcript query failed")
        return f"Error retrieving transcript: {exc}"


@tool
def save_qa_pair(
    question: str,
    answer: str,
    session_id: str,
    project_id: str,
    source: str,
) -> str:
    """Save a question-answer pair detected during a meeting session.

    Args:
        question: The question text.
        answer: The answer text.
        session_id: The session ID for this meeting.
        project_id: The project ID to scope the QA pair under.
        source: Who asked the question — 'participant' or 'agent'.

    Returns:
        Confirmation message with the qa_pair_id, or error message on failure.
    """
    if not QA_PAIRS_TABLE_NAME:
        return "Error: QA_PAIRS_TABLE_NAME environment variable not configured"
    qa_pair_id = str(uuid.uuid4())
    detected_at = datetime.now(timezone.utc).isoformat()
    try:
        _get_qa_pairs_table().put_item(
            Item={
                "qa_pair_id": qa_pair_id,
                "session_id": session_id,
                "project_id": project_id,
                "question": question,
                "answer": answer,
                "source": source,
                "detected_at": detected_at,
            }
        )
        return f"QA pair saved with id {qa_pair_id}"
    except Exception as exc:
        logger.exception("Failed to save QA pair")
        return f"Error saving QA pair: {exc}"


@tool
def save_summary_to_s3(summary_markdown: str, session_id: str, project_id: str) -> str:
    """Save a meeting summary markdown file to the knowledge base S3 bucket.

    Args:
        summary_markdown: The full markdown content of the meeting summary.
        session_id: The session ID for this meeting.
        project_id: The project ID to scope the summary under.

    Returns:
        Confirmation message with the S3 key, or error message on failure.
    """
    if not KB_BUCKET_NAME:
        return "Error: KB_BUCKET_NAME environment variable not configured"
    s3_key = f"{project_id}/summaries/{session_id}.md"
    try:
        _get_s3_client().put_object(
            Bucket=KB_BUCKET_NAME,
            Key=s3_key,
            Body=summary_markdown.encode("utf-8"),
            ContentType="text/markdown",
        )
        return f"Summary saved to s3://{KB_BUCKET_NAME}/{s3_key}"
    except Exception as exc:
        logger.exception("Failed to save summary to S3")
        return f"Error saving summary to S3: {exc}"


@tool
def get_session_qa_pairs(session_id: str) -> str:
    """Retrieve QA pairs recorded during a meeting session.

    Args:
        session_id: The session ID to retrieve QA pairs for.

    Returns:
        Formatted QA pairs for inclusion in a meeting summary.
    """
    if not QA_PAIRS_TABLE_NAME:
        return "No QA pairs table configured."
    try:
        table = _get_qa_pairs_table()
        response = table.query(
            IndexName="session-index",
            KeyConditionExpression=Key("session_id").eq(session_id),
        )
        items = response.get("Items", [])
        if not items:
            return f"No QA pairs recorded for session {session_id}."

        items.sort(key=lambda x: x.get("detected_at", ""))
        formatted = []
        for item in items:
            q = item.get("question", "")
            a = item.get("answer", "")
            source = item.get("source", "unknown")
            ts = item.get("detected_at", "")
            formatted.append(f"Q ({source}, {ts}): {q}\nA: {a}")
        return "\n\n".join(formatted)
    except Exception as exc:
        logger.exception("QA pairs query failed")
        return f"Error retrieving QA pairs: {exc}"


@tool
def get_meeting_summary(session_id: str, project_id: str) -> str:
    """Retrieve a previously generated meeting summary from S3.

    Args:
        session_id: The session ID of the meeting.
        project_id: The project ID to scope the summary lookup.

    Returns:
        The full markdown content of the meeting summary, or a message
        if no summary was found.
    """
    if not KB_BUCKET_NAME:
        return "Error: KB_BUCKET_NAME environment variable not configured"
    s3_key = f"{project_id}/summaries/{session_id}.md"
    try:
        response = _get_s3_client().get_object(Bucket=KB_BUCKET_NAME, Key=s3_key)
        return response["Body"].read().decode("utf-8")
    except _get_s3_client().exceptions.NoSuchKey:
        return f"No meeting summary found for session {session_id} at {s3_key}"
    except Exception as exc:
        logger.exception("Failed to retrieve meeting summary from S3")
        return f"Error retrieving meeting summary: {exc}"


@tool
def search_agent_skills(query: str, agent_id: str) -> str:
    """Search skill documents attached to a specific agent.

    Args:
        query: The search query to find relevant skill content.
        agent_id: The agent ID to filter skill documents by.

    Returns:
        Formatted search results from the agent's skill documents.
    """
    try:
        embedding = _generate_embedding(query)
        search_body = {
            "size": 5,
            "query": {
                "bool": {
                    "must": [
                        {"knn": {"embedding": {"vector": embedding, "k": 5}}}
                    ],
                    "filter": [
                        {"term": {"agent_id": agent_id}},
                        {"term": {"doc_type": "agent_skill"}},
                    ],
                }
            },
        }
        results = _get_os_client().search(index=INDEX_NAME, body=search_body)
        hits = results["hits"]["hits"]
        if not hits:
            return "No relevant skill documents found for this agent."

        formatted = []
        for i, hit in enumerate(hits, 1):
            src = hit["_source"]
            score = hit["_score"]
            text = src.get("text", "")
            source_file = src.get("source_file", "unknown")
            formatted.append(
                f"[{i}] (score: {score:.4f}, source: {source_file})\n{text}"
            )
        return "\n\n".join(formatted)
    except Exception as exc:
        logger.exception("Agent skills search failed")
        return f"Error searching agent skills: {exc}"
