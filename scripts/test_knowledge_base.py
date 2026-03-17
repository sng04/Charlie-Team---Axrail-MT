"""
Integration test for the GMeetAgent Strands agent via WebSocket.

Validates:
1. WebSocket connection succeeds (with and without agent_id)
2. Agent responds to knowledge-base questions
3. Fallback behavior works when no agent_id is provided

Usage:
    python3 scripts/test_knowledge_base.py

Requires:
    - websocket-client: pip3 install websocket-client
    - The GMeetAgentStack deployed with the WebSocket API
    - AWS credentials are NOT needed client-side (WebSocket is public)

Set WS_URL environment variable to override the default endpoint, e.g.:
    export WS_URL="wss://abc123.execute-api.ap-southeast-1.amazonaws.com/production"
"""

import json
import os
import ssl
import sys
import time

import certifi
import websocket

# --- Configuration ---
WS_URL = os.environ.get(
    "WS_URL",
    "",  # Set after deployment or via env var
)

# Agent ID from the Agents table (Live Transcription Agent)
TEST_AGENT_ID = "b538b8b5-ade4-4cb0-a411-d7f38c8e8450"

TIMEOUT = 30  # seconds to wait for a response

# SSL context using certifi CA bundle (fixes macOS certificate issues)
SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())

passed = 0
failed = 0


def send_and_receive(ws_url: str, message: str, session_id: str = "test-session") -> dict:
    """Connect to WebSocket, send a message, wait for response, and close."""
    ws = websocket.create_connection(ws_url, timeout=TIMEOUT, sslopt={"context": SSL_CONTEXT})
    try:
        payload = json.dumps({
            "action": "sendMessage",
            "message": message,
            "session_id": session_id,
            "project_id": "default-project",
        })
        ws.send(payload)
        raw = ws.recv()
        return json.loads(raw)
    finally:
        ws.close()


def run_test(name, fn):
    """Run a test function and track pass/fail."""
    global passed, failed
    try:
        fn()
        print(f"  ✅ {name}")
        passed += 1
    except Exception as e:
        print(f"  ❌ {name}: {e}")
        failed += 1


# ---------------------------------------------------------------
# Tests
# ---------------------------------------------------------------

def test_connect_without_agent_id():
    """WebSocket connection succeeds without agent_id (fallback)."""
    ws = websocket.create_connection(WS_URL, timeout=TIMEOUT, sslopt={"context": SSL_CONTEXT})
    ws.close()


def test_connect_with_agent_id():
    """WebSocket connection succeeds with agent_id query parameter."""
    url = f"{WS_URL}?agent_id={TEST_AGENT_ID}"
    ws = websocket.create_connection(url, timeout=TIMEOUT, sslopt={"context": SSL_CONTEXT})
    ws.close()


def test_knowledge_base_question():
    """Agent responds to a knowledge-base question with relevant content."""
    response = send_and_receive(
        WS_URL,
        "What is the AI Meeting Assistant and what does it do?",
    )
    assert response.get("type") == "response", (
        f"Expected type='response', got {response.get('type')!r}"
    )
    assert len(response.get("message", "")) > 0, "Response message is empty"
    print(f"    → Agent: {response.get('agent_name', 'unknown')}")
    print(f"    → Response preview: {response['message'][:120]}...")


def test_agent_specific_response():
    """Agent responds when connected with a specific agent_id."""
    url = f"{WS_URL}?agent_id={TEST_AGENT_ID}"
    response = send_and_receive(
        url,
        "Summarize the key features of the project.",
    )
    assert response.get("type") == "response", (
        f"Expected type='response', got {response.get('type')!r}"
    )
    assert len(response.get("message", "")) > 0, "Response message is empty"
    print(f"    → Agent: {response.get('agent_name', 'unknown')}")


def test_fallback_response():
    """Agent responds with fallback defaults when no agent_id is provided."""
    response = send_and_receive(
        WS_URL,
        "Hello, can you help me?",
    )
    assert response.get("type") == "response", (
        f"Expected type='response', got {response.get('type')!r}"
    )
    assert len(response.get("message", "")) > 0, "Response message is empty"


# ---------------------------------------------------------------
# Main
# ---------------------------------------------------------------

if __name__ == "__main__":
    if not WS_URL:
        print("❌ WS_URL environment variable is not set.")
        print("   Set it to your WebSocket endpoint, e.g.:")
        print('   export WS_URL="wss://abc123.execute-api.ap-southeast-1.amazonaws.com/production"')
        sys.exit(1)

    print(f"\n🔍 GMeetAgent Strands WebSocket Integration Tests")
    print(f"   Endpoint: {WS_URL}\n")

    print("[1] WebSocket Connectivity")
    run_test("Connect without agent_id", test_connect_without_agent_id)
    run_test("Connect with agent_id", test_connect_with_agent_id)

    print("\n[2] Agent Responses")
    run_test("Knowledge base question", test_knowledge_base_question)
    run_test("Agent-specific response", test_agent_specific_response)

    print("\n[3] Fallback Behavior")
    run_test("Fallback response (no agent_id)", test_fallback_response)

    print(f"\n{'='*50}")
    total = passed + failed
    print(f"Results: {passed}/{total} passed, {failed}/{total} failed")

    if failed > 0:
        print("❌ Some tests failed.")
        sys.exit(1)
    else:
        print("✅ All tests passed.")
        sys.exit(0)
