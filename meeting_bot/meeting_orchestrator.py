"""
Meeting Orchestrator Module

Orchestrate meeting bot and transcription simultaneously.
"""

import asyncio
import json
import logging
import re
import signal
import sys
from datetime import datetime, timezone
from typing import Optional

import boto3

from browser_manager import BrowserManager
from transcribe_handler import TranscribeStreamingManager
from config import (
    SESSION_ID,
    PROJECT_ID,
    MEETING_URL,
    GMAIL_EMAIL,
    GMAIL_PASSWORD,
    KEEP_ALIVE_INTERVAL,
    LOG_LEVEL,
    ENABLE_TRANSCRIPTION,
    AWS_REGION,
    ENVIRONMENT,
    SESSIONS_TABLE,
)

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
sessions_table = dynamodb.Table(SESSIONS_TABLE)

secrets_client = boto3.client("secretsmanager", region_name=AWS_REGION)


def get_gmail_credentials(project_id: str) -> tuple:
    """
    Get Gmail credentials from Secrets Manager.

    Args:
        project_id: Project ID for secret lookup

    Returns:
        tuple: (email, password)
    """
    secret_name = f"{ENVIRONMENT}/{project_id}/gmail-credentials"
    logger.info(f"Fetching Gmail credentials from: {secret_name}")

    try:
        response = secrets_client.get_secret_value(SecretId=secret_name)
        secret = json.loads(response["SecretString"])
        return secret.get("email", ""), secret.get("password", "")
    except Exception as e:
        logger.error(f"Failed to get Gmail credentials: {e}")
        raise


def update_session_status(session_id: str, status: str, task_arn: str = None) -> None:
    """Update session status in DynamoDB."""
    try:
        update_expr = "SET bot_status = :status, updated_at = :updated_at"
        expr_values = {
            ":status": status,
            ":updated_at": datetime.now(timezone.utc).isoformat(),
        }

        if task_arn:
            update_expr += ", task_arn = :task_arn"
            expr_values[":task_arn"] = task_arn

        sessions_table.update_item(
            Key={"session_id": session_id},
            UpdateExpression=update_expr,
            ExpressionAttributeValues=expr_values,
        )
        logger.info(f"Updated session {session_id} status to: {status}")
    except Exception as e:
        logger.error(f"Failed to update session status: {e}")


class MeetingOrchestrator:
    """
    Orchestrator for running meeting bot and transcription.
    """

    def __init__(self, gmail_email: str, gmail_password: str):
        """Initialize MeetingOrchestrator."""
        self._browser_manager = BrowserManager()
        self._transcribe_manager: Optional[TranscribeStreamingManager] = None
        self._is_running = False
        self._gmail_email = gmail_email
        self._gmail_password = gmail_password

    async def run(self, session_id: str, meeting_url: str) -> None:
        """
        Main entry point for running the orchestrator.

        Args:
            session_id: Session ID from DynamoDB
            meeting_url: Google Meet URL to join
        """
        logger.info(f"Starting Meeting Orchestrator for session: {session_id}")
        logger.info(f"Meeting URL: {meeting_url}")

        update_session_status(session_id, "joining")

        try:
            # Step 1: Start browser dan join meeting
            page = await self._browser_manager.start()
            await self._login_gmail(page)
            await self._join_meeting(page, meeting_url)

            update_session_status(session_id, "in_meeting")

            # Step 2: Start transcription jika enabled
            if ENABLE_TRANSCRIPTION:
                await self._start_transcription(session_id)

            # Step 3: Keep session alive
            self._is_running = True
            await self._keep_alive(page, session_id)

        except Exception as e:
            logger.exception(f"Error running orchestrator: {e}")
            update_session_status(session_id, "failed")
            raise
        finally:
            update_session_status(session_id, "completed")
            await self._cleanup()

    async def _start_transcription(self, session_id: str) -> None:
        """Start transcription service."""
        logger.info("Starting transcription service...")

        await asyncio.sleep(5)

        self._transcribe_manager = TranscribeStreamingManager(session_id)

        asyncio.create_task(self._run_transcription())

        logger.info("Transcription service started")

    async def _run_transcription(self) -> None:
        """Run transcription in background."""
        try:
            await self._transcribe_manager.start()
        except Exception as e:
            logger.error(f"Transcription error: {e}")

    async def _cleanup(self) -> None:
        """Cleanup resources."""
        logger.info("Cleaning up...")

        if self._transcribe_manager:
            await self._transcribe_manager.stop()

        await self._browser_manager.stop()

        logger.info("Cleanup complete")

    async def stop(self) -> None:
        """Stop orchestrator gracefully."""
        logger.info("Stopping orchestrator...")
        self._is_running = False

    async def _login_gmail(self, page) -> None:
        """Login to Gmail account."""
        logger.info("Logging in to Gmail...")

        await page.goto("https://accounts.google.com/signin")
        await page.wait_for_load_state("networkidle")

        logger.info("Entering email...")
        await page.fill('input[type="email"]', self._gmail_email)
        await page.click('button:has-text("Next"), #identifierNext')
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(2)

        logger.info("Entering password...")
        await page.wait_for_selector('input[type="password"]', state="visible")
        await page.fill('input[type="password"]', self._gmail_password)
        await page.click('button:has-text("Next"), #passwordNext')
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(3)

        logger.info("Gmail login successful")

    async def _join_meeting(self, page, meeting_url: str) -> None:
        """Join Google Meet meeting."""
        logger.info(f"Joining meeting: {meeting_url}")

        await page.goto(meeting_url)
        await page.wait_for_load_state("networkidle")
        await asyncio.sleep(5)

        # Dismiss browser warning if present
        try:
            dismiss_btn = page.locator('button:has-text("Dismiss")')
            if await dismiss_btn.count() > 0:
                await dismiss_btn.click()
                await asyncio.sleep(1)
        except Exception:
            pass

        await self._fill_name_if_needed(page)
        await self._disable_media(page)
        await self._click_join_button(page)

        logger.info("Successfully joined meeting")

    async def _fill_name_if_needed(self, page) -> None:
        """Fill in name if there is a prompt for guest."""
        try:
            name_input = page.locator(
                'input[placeholder*="name"], input[aria-label*="name"]'
            )
            if await name_input.count() > 0:
                await name_input.fill("Meeting Bot")
                await asyncio.sleep(1)
        except Exception:
            pass

    async def _disable_media(self, page) -> None:
        """Disable camera and microphone."""
        logger.info("Disabling camera and microphone...")

        try:
            camera_btn = page.locator(
                '[aria-label*="camera"], [data-is-muted="false"][aria-label*="camera"]'
            )
            if await camera_btn.count() > 0:
                await camera_btn.first.click()
                await asyncio.sleep(0.5)

            mic_btn = page.locator(
                '[aria-label*="microphone"], [data-is-muted="false"][aria-label*="microphone"]'
            )
            if await mic_btn.count() > 0:
                await mic_btn.first.click()
                await asyncio.sleep(0.5)
        except Exception as e:
            logger.warning(f"Could not disable media: {e}")

    async def _click_join_button(self, page) -> None:
        """Click join meeting button."""
        logger.info("Looking for join button...")

        await asyncio.sleep(5)

        join_selectors = [
            'button:has-text("Join now")',
            'button:has-text("Ask to join")',
            'button:has-text("Gabung sekarang")',
            'button:has-text("Minta untuk bergabung")',
            '[jsname="Qx7uuf"]',
        ]

        for selector in join_selectors:
            try:
                btn = page.locator(selector)
                if await btn.count() > 0:
                    await btn.first.click()
                    logger.info(f"Clicked join button: {selector}")
                    await asyncio.sleep(10)
                    return
            except Exception:
                continue

        logger.warning("Could not find join button")

    async def _keep_alive(self, page, session_id: str) -> None:
        """Keep session alive while meeting is ongoing."""
        logger.info(f"Starting keep-alive loop (interval: {KEEP_ALIVE_INTERVAL}s)")

        while self._is_running:
            try:
                is_in_meeting = await self._check_meeting_status(page)

                if not is_in_meeting:
                    logger.warning("No longer in meeting, stopping")
                    break

                logger.debug("Keep-alive check: Still in meeting")
                await asyncio.sleep(KEEP_ALIVE_INTERVAL)

            except Exception as e:
                logger.error(f"Keep-alive error: {e}")
                await asyncio.sleep(KEEP_ALIVE_INTERVAL)

    async def _check_meeting_status(self, page) -> bool:
        """Check if still in meeting."""
        try:
            current_url = page.url
            logger.debug(f"Current URL: {current_url}")

            if "meet.google.com" not in current_url:
                logger.warning(f"URL changed, no longer on Google Meet: {current_url}")
                return False

            # Check for "removed from meeting" or "meeting ended" indicators
            removed_indicators = [
                'text="You\'ve been removed from the meeting"',
                'text="The meeting has ended"',
                'text="You left the meeting"',
                'text="Return to home screen"',
                '[data-call-ended="true"]',
            ]

            for indicator in removed_indicators:
                try:
                    if await page.locator(indicator).count() > 0:
                        logger.warning(f"Meeting ended indicator found: {indicator}")
                        return False
                except Exception:
                    pass

            # Check for active meeting indicators
            meeting_indicators = [
                "[data-meeting-title]",
                '[aria-label*="Leave call"]',
                '[aria-label*="Turn off camera"]',
                '[aria-label*="Turn off microphone"]',
            ]

            for indicator in meeting_indicators:
                try:
                    count = await page.locator(indicator).count()
                    if count > 0:
                        logger.debug(f"Meeting indicator found: {indicator}")
                        return True
                except Exception:
                    pass

            # If no indicators found, assume still in meeting (avoid false positives)
            logger.debug("No meeting indicators found, assuming still in meeting")
            return True

        except Exception as e:
            logger.error(f"Error checking meeting status: {e}")
            return True


async def main():
    """Main function."""
    if not SESSION_ID:
        logger.error("SESSION_ID must be set")
        sys.exit(1)

    if not PROJECT_ID:
        logger.error("PROJECT_ID must be set")
        sys.exit(1)

    if not MEETING_URL:
        logger.error("MEETING_URL must be set")
        sys.exit(1)

    # Get Gmail credentials from Secrets Manager
    gmail_email, gmail_password = get_gmail_credentials(PROJECT_ID)

    if not gmail_email or not gmail_password:
        logger.error("Gmail credentials not found in Secrets Manager")
        sys.exit(1)

    orchestrator = MeetingOrchestrator(gmail_email, gmail_password)

    def signal_handler(sig, frame):
        logger.info(f"Received signal {sig}, shutting down...")
        asyncio.create_task(orchestrator.stop())

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    await orchestrator.run(SESSION_ID, MEETING_URL)


if __name__ == "__main__":
    asyncio.run(main())
