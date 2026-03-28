---
inclusion: auto
name: product-description
description: Description of the core product and its features. Include when relevant context or project requirements is needed to steer feature creation in the right direction.
---
# Product Steering Document: AI Meeting Assistant POC

## Overview
The AI Meeting Assistant is a cloud-based application deployed on AWS, designed to empower non-technical team members with AI-powered technical expertise during client meetings. 

By addressing the knowledge gap in live meetings, this solution maintains client confidence, speeds up decision-making, and provides systematic retrospective analysis to drive continuous team improvement. 

## Core System Components
The architecture consists of three major components:

**Meeting Agent Engine:** This engine automatically authenticates and joins Google Meet sessions using Gmail credentials. It captures real-time audio, processes it via a speech-to-text service, detects questions using natural language understanding, and generates responses utilizing configured knowledge bases and system instructions.
**Admin Portal:** A dedicated interface for administrators and solution architects to configure agent personalities, tune system prompts, and manage Gmail accounts. Administrators can also upload knowledge base documents (supporting PDF, TXT, and DOCX formats) and monitor question-answer analytics.
**User Portal:** An interface for meeting participants to monitor real-time transcriptions and review historical data. It features search and filtering capabilities for past interactions.

## Operational Modes
Users navigate the assistant through two primary modes:

**Live Output Mode:** Provides real-time assistance by displaying meeting transcriptions within 2 seconds of speech and delivering generated answers to detected questions within 1 second of generation. Transcription quality is enhanced by:
- **Sentence Merging**: Fragmented Transcribe results are buffered and merged into complete sentences based on punctuation and time gaps (configurable via `MERGE_GAP_THRESHOLD`, default 1.5s).
- **Custom Vocabulary**: AWS Transcribe Custom Vocabulary (`tech-vocab`) with 170+ technical terms across software engineering, cloud, IoT, AI/ML, and design domains. Configured via `TRANSCRIBE_VOCABULARY_NAME` environment variable on ECS tasks.
- **Text Preprocessing**: Filler word removal, noise pattern filtering, confidence threshold filtering, and deduplication.
**Retro Mode:** Allows teams to review completed meeting transcripts, identify missed agenda items, summarize action steps, and receive coaching insights based on rubrics. Users can also chat with the system to gain further insights into their performance.

## Key Success Metrics
**Connectivity & Uptime:** Agents must achieve a 95% success rate when joining meetings and maintain stable connections with less than a 1% disconnection rate. The system must maintain 99% uptime during active sessions.
**AI Performance:** The system must detect questions with at least 80% accuracy and generate contextually relevant responses with a minimum 80% relevance rating.
**Latency:** Audio response delivery must occur within 10 seconds of question detection.

## Scope Limitations & Constraints
**Language:** All content and interactions are strictly limited to English.
**Platform:** The solution exclusively supports Google Meet.
**Integrations:** Integration with external CRM, ERP, or ticketing systems is out of scope, as is mobile application development.