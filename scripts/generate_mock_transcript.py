#!/usr/bin/env python3
"""Generate a realistic ~10 minute mock meeting transcript.

Two speakers discuss the GMeet Agent project — its features, knowledge base,
QA detection, meeting summaries, and retro mode. Output is a JSON array
with speaker and text fields per line, matching the cleaned format after
AWS Transcribe processing.
"""

import json

LINES = [
    ("Speaker A", "Hey, thanks for joining. I wanted to walk you through our GMeet Agent platform today."),
    ("Speaker B", "Sure, happy to be here. I've been curious about what you've built since our last call."),
    ("Speaker A", "Great. So at a high level, GMeet Agent is an AI-powered meeting assistant that sits in your Google Meet calls and provides real-time support."),
    ("Speaker B", "What kind of support are we talking about? Like transcription?"),
    ("Speaker A", "Transcription is part of it, but it goes way beyond that. The system has a knowledge base powered by OpenSearch, and during the meeting it can answer questions using documents you've uploaded."),
    ("Speaker B", "Interesting. So if I upload our product docs, the agent can reference them live?"),
    ("Speaker A", "Exactly. You upload PDFs or markdown files to an S3 bucket, they get chunked and vectorized using Amazon Titan embeddings, and indexed into OpenSearch. Then during a call, the agent searches that index."),
    ("Speaker B", "How does the question detection work? Does someone have to manually ask the agent?"),
    ("Speaker A", "Not at all. We have a detect question action that the frontend triggers when it picks up a question from the transcript. The agent then searches the knowledge base and sends back an answer over WebSocket."),
    ("Speaker B", "That's pretty slick. What about saving those Q and A pairs for later?"),
    ("Speaker A", "We have a QA pairs table in DynamoDB. Every question-answer exchange gets saved with metadata like who asked it, the session ID, project ID, and a timestamp. You can query them later via our REST API."),
    ("Speaker B", "Can you tell me more about the project scoping? How do you keep different clients' data separate?"),
    ("Speaker A", "Each session belongs to a project. When you connect via WebSocket, you pass a session ID, and we look up the project ID from the sessions table. All knowledge base searches are filtered by project ID."),
    ("Speaker B", "That makes sense. What happens when the meeting ends?"),
    ("Speaker A", "We have an end meeting action. The agent pulls the full transcript and all QA pairs, generates a comprehensive markdown summary, and saves it to S3. The summary gets ingested back into the knowledge base too."),
    ("Speaker B", "So the summaries become searchable for future meetings?"),
    ("Speaker A", "Exactly. It's a feedback loop. The more meetings you have, the richer your knowledge base gets."),
    ("Speaker B", "What about the gap analysis feature you mentioned last time?"),
    ("Speaker A", "Right, so we run periodic gap analysis every two minutes via EventBridge. It checks active sessions, pulls the transcript, searches the KB for discussed topics, and identifies gaps where the knowledge base doesn't have good coverage."),
    ("Speaker B", "And it suggests questions to ask?"),
    ("Speaker A", "Yes, the output includes a list of suggested questions. These are topics where the KB is thin, so the host knows what to dig into during the conversation."),
    ("Speaker B", "How do you handle the different agent personalities? I remember you had multiple modes."),
    ("Speaker A", "We have a personalities table. Each personality defines a communication style — casual, concise, or professional. When you create an agent, you assign it a personality, and that shapes how it responds."),
    ("Speaker B", "Can we create custom personalities?"),
    ("Speaker A", "Absolutely. The REST API has full CRUD for both agents and personalities. You can create, update, delete, and list them."),
    ("Speaker B", "What about after the meeting? Is there any way to review how it went?"),
    ("Speaker A", "That's our retro mode. After a meeting is marked complete, you can trigger a retrospective analysis. The agent reviews the transcript, summary, and QA pairs, then gives structured feedback."),
    ("Speaker B", "What kind of feedback?"),
    ("Speaker A", "Communication effectiveness scores, question handling quality, missed agenda items, action item completeness, knowledge gap assessment, and specific coaching insights. All grounded in actual transcript moments."),
    ("Speaker B", "That's really comprehensive. Can you ask follow-up questions about the retro?"),
    ("Speaker A", "Yes, we have a retro chat action. Once the analysis is generated, you can have a conversation about it. The agent has all the meeting context cached so it can give specific answers."),
    ("Speaker B", "I'm curious about the tech stack. What model are you using?"),
    ("Speaker A", "Amazon Nova Pro through Bedrock. All model calls go to us-east-1 since that's where we have access. The rest of the infrastructure is in ap-southeast-1."),
    ("Speaker B", "And the agent framework?"),
    ("Speaker A", "Strands SDK. It gives us tool-use capabilities out of the box. Each action handler creates a Strands agent with the right tools and a task-specific prompt overlay."),
    ("Speaker B", "How many concurrent sessions can it handle?"),
    ("Speaker A", "The Lambda scales automatically. Each WebSocket connection gets its own invocation. We cache the system prompt and connection data in memory for the duration of the connection."),
    ("Speaker B", "What's the latency like for question answering?"),
    ("Speaker A", "Typically two to four seconds. The embedding generation is fast, the OpenSearch query is sub-second, and then Nova Pro generates the response. Most of the time is in the model inference."),
    ("Speaker B", "That's acceptable for a live meeting. One more question — how do you handle the WebSocket routing?"),
    ("Speaker A", "We use API Gateway WebSocket API with route selection on the action field in the message body. Each action like sendMessage, detectQuestion, analyzeGaps gets its own route that maps to the same Lambda."),
    ("Speaker B", "And the Lambda figures out what to do based on the action?"),
    ("Speaker A", "Right, we have a task router pattern. The handler dispatches to action-specific functions. Each one gets a task prompt overlay prepended to the message before the agent processes it."),
    ("Speaker B", "This looks really solid. I think we could pilot this with our sales team next quarter."),
    ("Speaker A", "That would be great. We can set up a dedicated project for your team, upload your product docs, and configure agents with the right personalities."),
    ("Speaker B", "Perfect. Let me sync with my team and we'll schedule a follow-up to discuss the pilot scope."),
    ("Speaker A", "Sounds good. I'll send over the API documentation and some example WebSocket payloads so your devs can start looking at the integration."),
    ("Speaker B", "Appreciate it. This has been really helpful."),
    ("Speaker A", "Thanks for your time. Talk soon."),
]


def generate():
    output = [{"speaker": speaker, "text": text} for speaker, text in LINES]

    with open("scripts/mock_transcript.json", "w") as f:
        json.dump(output, f, indent=2)

    print(f"Generated {len(output)} lines → scripts/mock_transcript.json")


if __name__ == "__main__":
    generate()
