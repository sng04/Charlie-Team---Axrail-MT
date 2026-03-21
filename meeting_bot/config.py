"""
Meeting Bot Configuration

Configuration for Meeting Bot.
"""

import os

# ==============================================================================
# Session Configuration (passed from ECS task)
# ==============================================================================
SESSION_ID = os.environ.get("SESSION_ID", "")
PROJECT_ID = os.environ.get("PROJECT_ID", "")
CREDENTIAL_ID = os.environ.get("CREDENTIAL_ID", "")
MEETING_URL = os.environ.get("MEETING_URL", "")

# ==============================================================================
# Gmail Credentials (fetched from Secrets Manager at runtime)
# ==============================================================================
GMAIL_EMAIL = os.environ.get("GMAIL_EMAIL", "")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD", "")

# ==============================================================================
# AWS Configuration
# ==============================================================================
AWS_REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
SESSIONS_TABLE = os.environ.get("SESSIONS_TABLE", f"{ENVIRONMENT}-Sessions")
TRANSCRIPTS_TABLE = os.environ.get("TRANSCRIPTS_TABLE", f"{ENVIRONMENT}-Transcripts")

# ==============================================================================
# Warm Pool Configuration
# ==============================================================================
WARM_POOL_MODE = os.environ.get("WARM_POOL_MODE", "false").lower() == "true"
SQS_QUEUE_URL = os.environ.get("SQS_QUEUE_URL", "")
BOT_POOL_TABLE = os.environ.get("BOT_POOL_TABLE", f"{ENVIRONMENT}-BotPool")

# ECS Task ARN (from metadata endpoint or environment)
ECS_CONTAINER_METADATA_URI = os.environ.get("ECS_CONTAINER_METADATA_URI_V4", "")

# ==============================================================================
# Browser Configuration
# ==============================================================================
BROWSER_HEADLESS = os.environ.get("BROWSER_HEADLESS", "true").lower() == "true"
BROWSER_TIMEOUT = int(os.environ.get("BROWSER_TIMEOUT", "30000"))
BROWSER_TYPE = os.environ.get("BROWSER_TYPE", "firefox")

# ==============================================================================
# Meeting Configuration
# ==============================================================================
KEEP_ALIVE_INTERVAL = int(os.environ.get("KEEP_ALIVE_INTERVAL", "30"))

# ==============================================================================
# Transcription Configuration
# ==============================================================================
ENABLE_TRANSCRIPTION = os.environ.get("ENABLE_TRANSCRIPTION", "true").lower() == "true"
TRANSCRIBE_LANGUAGE = os.environ.get("TRANSCRIBE_LANGUAGE", "en-US")

# ==============================================================================
# Logging Configuration
# ==============================================================================
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
