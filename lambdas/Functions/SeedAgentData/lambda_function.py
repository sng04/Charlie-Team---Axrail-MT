"""Seed Agent Data Lambda — CloudFormation Custom Resource.

Populates initial Agent and Personality records with deterministic UUIDs
(uuid5) so the seed is idempotent across Create/Update events.
"""

import json
import os
import uuid

import boto3

AGENTS_TABLE_NAME = os.environ.get("AGENTS_TABLE_NAME", "")
PERSONALITIES_TABLE_NAME = os.environ.get("PERSONALITIES_TABLE_NAME", "")

dynamodb = boto3.resource("dynamodb")
agents_table = dynamodb.Table(AGENTS_TABLE_NAME)
personalities_table = dynamodb.Table(PERSONALITIES_TABLE_NAME)

NAMESPACE = uuid.UUID("a1b2c3d4-e5f6-7890-abcd-ef1234567890")

PERSONALITIES = [
    {
        "personality_id": str(uuid.uuid5(NAMESPACE, "casual")),
        "personality_name": "casual",
        "personality_prompt": (
            "Use relaxed, conversational language. Use contractions, "
            "informal phrasing, and a friendly tone. Keep things "
            "approachable and easy to read."
        ),
    },
    {
        "personality_id": str(uuid.uuid5(NAMESPACE, "concise")),
        "personality_name": "concise",
        "personality_prompt": (
            "Use minimal words. Prefer short sentences and bullet points. "
            "Omit filler words. Get straight to the point."
        ),
    },
    {
        "personality_id": str(uuid.uuid5(NAMESPACE, "professional")),
        "personality_name": "professional",
        "personality_prompt": (
            "Use formal, structured language. Write in complete sentences "
            "with proper terminology. Maintain a polished, "
            "business-appropriate tone."
        ),
    },
]

PERSONALITY_MAP = {p["personality_name"]: p["personality_id"] for p in PERSONALITIES}

AGENTS = [
    {
        "agent_id": str(uuid.uuid5(NAMESPACE, "live_transcription")),
        "agent_name": "Live Transcription Agent",
        "role_prompt": (
            "You are an AI Meeting Agent designed for live meeting "
            "transcription. You monitor ongoing conversations in real time "
            "and maintain awareness of the discussion context."
        ),
        "task_prompt": (
            "1. Detect questions raised by meeting participants.\n"
            "2. Query relevant knowledge bases for accurate answers.\n"
            "3. Generate clear responses without disrupting the meeting.\n"
            "4. Track action items, decisions, and key discussion points.\n"
            "5. Provide summaries when requested."
        ),
        "personality_id": PERSONALITY_MAP["professional"],
        "model_id": "amazon.nova-pro-v1:0",
        "use_case": "live_meeting_transcription",
    },
    {
        "agent_id": str(uuid.uuid5(NAMESPACE, "meeting_qa")),
        "agent_name": "Q&A Assistant Agent",
        "role_prompt": (
            "You are an AI Meeting Q&A Assistant. You help meeting "
            "participants get quick, accurate answers to questions raised "
            "during discussions."
        ),
        "task_prompt": (
            "1. Listen for questions from participants.\n"
            "2. Search the knowledge base for relevant information.\n"
            "3. Provide accurate, referenced answers.\n"
            "4. Flag low-confidence answers for verification."
        ),
        "personality_id": PERSONALITY_MAP["concise"],
        "model_id": "amazon.nova-pro-v1:0",
        "use_case": "meeting_qa",
    },
    {
        "agent_id": str(uuid.uuid5(NAMESPACE, "meeting_summary")),
        "agent_name": "Meeting Summary Agent",
        "role_prompt": (
            "You are an AI Meeting Summarizer. You create helpful "
            "summaries of meetings, capturing the key points so "
            "participants can review them later."
        ),
        "task_prompt": (
            "1. Generate meeting summaries after discussions.\n"
            "2. Track action items and owners.\n"
            "3. Highlight decisions made during the meeting.\n"
            "4. Note unresolved questions and follow-ups."
        ),
        "personality_id": PERSONALITY_MAP["casual"],
        "model_id": "amazon.nova-pro-v1:0",
        "use_case": "meeting_summary",
    },
]


def lambda_handler(event, context):
    """Seed agent and personality records on Create/Update."""
    print(f"Event: {json.dumps(event)}")
    request_type = event.get("RequestType", "")
    physical_id = event.get("PhysicalResourceId", str(uuid.uuid4()))

    if request_type == "Delete":
        return {"Status": "SUCCESS", "PhysicalResourceId": physical_id}

    if request_type in ("Create", "Update"):
        for personality in PERSONALITIES:
            personalities_table.put_item(Item=personality)
            print(f"Seeded personality: {personality['personality_name']}")

        for agent in AGENTS:
            agents_table.put_item(Item=agent)
            print(f"Seeded agent: {agent['agent_name']}")

        physical_id = "seed-agent-data-complete"

    return {
        "Status": "SUCCESS",
        "PhysicalResourceId": physical_id,
        "Data": {"Message": "Agent seed data loaded"},
    }
