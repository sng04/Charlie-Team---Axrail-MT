"""Shared constants and environment configuration for the Strands agent."""

import os

# ---------------------------------------------------------------------------
# Environment variables
# ---------------------------------------------------------------------------

AGENTS_TABLE_NAME = os.environ.get("AGENTS_TABLE_NAME", "")
PERSONALITIES_TABLE_NAME = os.environ.get("PERSONALITIES_TABLE_NAME", "")
SESSIONS_TABLE_NAME = os.environ.get("SESSIONS_TABLE_NAME", "")
TRANSCRIPTS_TABLE_NAME = os.environ.get("TRANSCRIPTS_TABLE_NAME", "")
SUGGESTED_QUESTIONS_TABLE_NAME = os.environ.get("SUGGESTED_QUESTIONS_TABLE_NAME", "")
BEDROCK_REGION = os.environ.get("BEDROCK_REGION", "us-east-1")
WEBSOCKET_ENDPOINT = os.environ.get("WEBSOCKET_ENDPOINT", "")

# ---------------------------------------------------------------------------
# Semantic similarity threshold for question matching
# ---------------------------------------------------------------------------

MATCH_THRESHOLD = 0.80

# ---------------------------------------------------------------------------
# Heuristic patterns for client question detection
# ---------------------------------------------------------------------------

_QUESTION_INDICATORS = {
    "what", "how", "why", "when", "where", "who", "which",
    "can you", "could you", "would you", "is there", "are there",
    "do you", "does it", "have you", "will you", "is it",
    "tell me", "explain", "describe",
}

# ---------------------------------------------------------------------------
# Default agent / personality fallbacks
# ---------------------------------------------------------------------------

DEFAULT_AGENT = {
    "agent_name": "General Meeting Assistant",
    "role_prompt": (
        "You are an AI Meeting Assistant. You help meeting participants "
        "by answering questions, providing context from the knowledge base, "
        "and summarizing discussions."
    ),
    "task_prompt": (
        "1. Answer questions from participants using the knowledge base.\n"
        "2. Provide context from session transcripts when relevant.\n"
        "3. Summarize discussions when asked.\n"
        "4. Be helpful and accurate in all responses."
    ),
    "personality_id": None,
    "model_id": "amazon.nova-pro-v1:0",
}

DEFAULT_PERSONALITY_PROMPT = (
    "Use formal, structured language. Write in complete sentences "
    "with proper terminology. Maintain a polished, business-appropriate tone."
)

# ---------------------------------------------------------------------------
# Task-specific instruction overlays
# ---------------------------------------------------------------------------

TASK_PROMPTS = {
    "detectQuestion": (
        "You are answering a question detected in a live meeting transcript. "
        "Use the knowledge base to provide an accurate, concise answer. "
        "If you cannot find relevant information, say so clearly."
    ),
    "extractQAPair": (
        "Extract and save the following question-answer exchange as a QA pair. "
        "Use the save_qa_pair tool to persist it. Determine the source field: "
        "use 'participant' if a meeting attendee asked the question, "
        "or 'agent' if the AI assistant generated the answer."
    ),
    "analyzeGaps": (
        "You are performing a knowledge gap analysis for a live meeting. "
        "1. Retrieve the session transcript using get_session_transcript. "
        "2. Identify the key topics discussed in the transcript. "
        "3. For each topic, search the knowledge base using search_knowledge_base. "
        "4. Identify topics with no results or low-relevance results as knowledge gaps. "
        "5. Return your analysis as valid JSON with this exact structure:\n"
        '{"gaps": [{"topic": "...", "description": "...", "confidence": "high|medium|low"}], '
        '"suggested_questions": ["..."]}\n'
        "Do not include any text outside the JSON object."
    ),
    "endMeeting": (
        "You are generating a comprehensive meeting summary. "
        "1. Retrieve the full session transcript using get_session_transcript. "
        "2. Retrieve QA pairs for this session using get_session_qa_pairs. "
        "3. Generate a markdown summary with these sections:\n"
        "   - Meeting Title (derived from main discussion topics)\n"
        "   - Date (ISO 8601 format)\n"
        "   - Attendees (from speaker labels in transcript)\n"
        "   - Key Discussion Topics\n"
        "   - Decisions Made\n"
        "   - Action Items (with owners where identifiable)\n"
        "   - Unresolved Questions\n"
        "   - QA Pairs (from the session)\n"
        "4. Save the summary to S3 using save_summary_to_s3. "
        "Return the full markdown summary text."
    ),
    "retroAnalysis": (
        "You are performing a retrospective analysis of a completed meeting. "
        "1. Retrieve the full session transcript using get_session_transcript. "
        "2. Retrieve the meeting summary using get_meeting_summary. "
        "3. Retrieve QA pairs for the session using get_session_qa_pairs. "
        "4. Generate structured feedback with these sections:\n"
        "   a) Missed Agenda Items — topics that should have been covered but were not\n"
        "   b) Communication Effectiveness — score 1-10 with specific feedback referencing transcript moments\n"
        "   c) Question Handling Quality — were questions answered well? were important questions missed?\n"
        "   d) Action Item Completeness — were action items clearly defined with owners?\n"
        "   e) Knowledge Gap Assessment — topics that lacked KB coverage during the meeting\n"
        "   f) Coaching Insights — specific, actionable improvement suggestions referencing transcript moments\n"
        "   g) Overall Meeting Effectiveness — rating 1-10 with justification\n"
        "Be specific and reference actual moments from the transcript. "
        "Avoid generic platitudes — every suggestion should be grounded in evidence from the meeting data."
    ),
    "suggestResponse": (
        "A client just asked a question during a live meeting. "
        "Search the knowledge base to find relevant information and provide "
        "a concise, factual suggested response that the meeting host can "
        "paraphrase in conversation. Keep it to 2-3 sentences max. "
        "If the knowledge base has no relevant information, clearly state: "
        "'No relevant KB information found — answer from your own knowledge.' "
        "Include the source document names if available."
    ),
    "retroChat": (
        "You are in retro mode for a completed meeting. The user is asking "
        "follow-up questions about the retrospective analysis. "
        "Use the meeting context provided (transcript, summary, QA pairs, "
        "and retro feedback) to give specific, evidence-based answers. "
        "Reference specific moments from the transcript when relevant. "
        "Be conversational but precise."
    ),
}
