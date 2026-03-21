# Product Overview

## What is AXRAIL Meeting Tool?

AXRAIL Meeting Tool (MT) is an AI-powered meeting assistant platform that joins Google Meet calls, transcribes conversations in real time, and provides intelligent support to meeting hosts.

## Core Capabilities

- Real-time transcript processing with speaker classification
- Knowledge base search during live meetings (suggested responses to client questions)
- Pre-set question matching against meeting topics
- Automatic QA pair extraction from conversations
- Knowledge gap analysis (on-demand and scheduled)
- Post-meeting retrospective coaching with follow-up chat
- Agent-specific skill documents for domain-scoped knowledge
- Meeting summary generation with action items

## User Roles

- Admin: Full access to all resources (agents, personalities, skills, projects, users, bot credentials, warm pool)
- User: Access to assigned projects, sessions, and meeting features

## Key Workflows

1. Admin creates an agent with a personality and uploads skill documents
2. Admin creates a project and session with a Google Meet link
3. Meeting bot joins the call and streams transcript to the WebSocket API
4. The AI agent processes transcript lines, detects questions, and provides real-time assistance
5. After the meeting, the host reviews the summary, QA pairs, and coaching feedback via retro mode

## Product Requirements

The original PRD is available at `resources/prd.pdf` in the DEVELOPER 2 archive.
