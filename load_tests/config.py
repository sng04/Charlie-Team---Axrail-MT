"""Load test configuration loaded from environment."""

import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://sjsd378hbd.execute-api.ap-southeast-1.amazonaws.com/dev")
WS_URL = os.getenv("WS_URL", "wss://hey8o0q9tb.execute-api.ap-southeast-1.amazonaws.com/production")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "admin@example.com")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "changeme")
USER_USERNAME = os.getenv("USER_USERNAME", "user@example.com")
USER_PASSWORD = os.getenv("USER_PASSWORD", "changeme")

PROJECT_ID = os.getenv("PROJECT_ID", "")
SESSION_ID = os.getenv("SESSION_ID", "")
AGENT_ID = os.getenv("AGENT_ID", "")
