"""
WebSocket Broadcaster Module

Broadcast transcript lines to connected clients via API Gateway WebSocket.
Uses the same data structure as DynamoDB for consistency.
"""

import asyncio
import json
import logging
from typing import Optional

import boto3

logger = logging.getLogger(__name__)


class WebSocketBroadcaster:
    """Broadcast transcript lines to WebSocket clients watching a session."""

    def __init__(
        self,
        session_id: str,
        websocket_endpoint: str,
        region: str = "ap-southeast-1",
    ):
        """
        Initialize WebSocket broadcaster.

        Args:
            session_id: Session ID to broadcast for
            websocket_endpoint: API Gateway WebSocket endpoint (without wss://)
                               e.g., "abc123.execute-api.ap-southeast-1.amazonaws.com/production"
            region: AWS region
        """
        self._session_id = session_id
        self._endpoint = websocket_endpoint
        self._region = region
        self._apigw_client = None
        self._connection_id: Optional[str] = None
        self._is_initialized = False

    def _get_client(self):
        """Get or create API Gateway Management API client."""
        if self._apigw_client is None:
            # Endpoint format: https://{api-id}.execute-api.{region}.amazonaws.com/{stage}
            endpoint_url = f"https://{self._endpoint}"
            self._apigw_client = boto3.client(
                "apigatewaymanagementapi",
                endpoint_url=endpoint_url,
                region_name=self._region,
            )
        return self._apigw_client

    async def initialize(self) -> None:
        """Initialize broadcaster and fetch active connection for session."""
        try:
            # Get connection_id from Sessions table
            dynamodb = boto3.resource("dynamodb", region_name=self._region)
            from config import ENVIRONMENT
            sessions_table = dynamodb.Table(f"{ENVIRONMENT}-Sessions")
            
            response = sessions_table.get_item(
                Key={"session_id": self._session_id},
                ProjectionExpression="connection_id",
            )
            
            item = response.get("Item", {})
            self._connection_id = item.get("connection_id")
            
            self._is_initialized = True
            if self._connection_id:
                logger.info(
                    f"WebSocket broadcaster initialized for session {self._session_id}, "
                    f"connection: {self._connection_id[:8]}..."
                )
            else:
                logger.info(
                    f"WebSocket broadcaster initialized for session {self._session_id}, "
                    f"no active connection yet"
                )
        except Exception as e:
            logger.warning(f"Failed to initialize WebSocket broadcaster: {e}")
            self._is_initialized = True  # Continue anyway

    async def broadcast_transcript_line(self, item: dict) -> None:
        """
        Broadcast a transcript line to the connected client.

        Args:
            item: Transcript item (same structure as DynamoDB)
                  {session_id, transcript_id, text, speaker, start_time, end_time, confidence, timestamp, is_partial}
        """
        if not self._endpoint:
            logger.debug("No WebSocket endpoint configured, skipping broadcast")
            return

        # Refresh connection_id if not set (client may have connected after bot started)
        if not self._connection_id:
            await self._refresh_connection()
            
        if not self._connection_id:
            logger.debug("No active connection for session, skipping broadcast")
            return

        message = {
            "type": "transcriptLine",
            "line": item,
        }
        message_bytes = json.dumps(message).encode("utf-8")

        await self._send_to_connection(self._connection_id, message_bytes)

    async def _refresh_connection(self) -> None:
        """Refresh connection_id from Sessions table."""
        try:
            dynamodb = boto3.resource("dynamodb", region_name=self._region)
            from config import ENVIRONMENT
            sessions_table = dynamodb.Table(f"{ENVIRONMENT}-Sessions")
            
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None,
                lambda: sessions_table.get_item(
                    Key={"session_id": self._session_id},
                    ProjectionExpression="connection_id",
                ),
            )
            
            item = response.get("Item", {})
            new_conn_id = item.get("connection_id")
            
            if new_conn_id and new_conn_id != self._connection_id:
                self._connection_id = new_conn_id
                logger.info(f"Refreshed connection_id: {self._connection_id[:8]}...")
        except Exception as e:
            logger.debug(f"Failed to refresh connection: {e}")

    async def _send_to_connection(self, connection_id: str, data: bytes) -> None:
        """Send data to a specific connection."""
        try:
            client = self._get_client()
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(
                None,
                lambda: client.post_to_connection(
                    ConnectionId=connection_id,
                    Data=data,
                ),
            )
            logger.debug(f"Sent transcript to connection {connection_id[:8]}...")
        except client.exceptions.GoneException:
            # Connection is stale, clear it
            logger.debug(f"Connection {connection_id[:8]}... is gone, clearing")
            self._connection_id = None
        except Exception as e:
            logger.warning(f"Failed to send to connection {connection_id[:8]}...: {e}")
