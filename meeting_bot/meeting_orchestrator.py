"""
Meeting Orchestrator Module

Orchestrate meeting bot and transcription simultaneously.
Supports two modes:
1. Warm Pool Mode: Container stays alive, polls SQS for meeting requests
2. Cold Start Mode: Single meeting per container (legacy)
"""

import asyncio
import json
import logging
import signal
import sys
import uuid
import time
from datetime import datetime, timezone
from typing import Optional

import boto3
import requests

from browser_manager import BrowserManager
from transcribe_handler import TranscribeStreamingManager
from config import (
    SESSION_ID,
    PROJECT_ID,
    CREDENTIAL_ID,
    MEETING_URL,
    KEEP_ALIVE_INTERVAL,
    LOG_LEVEL,
    ENABLE_TRANSCRIPTION,
    AWS_REGION,
    ENVIRONMENT,
    SESSIONS_TABLE,
    SQS_QUEUE_URL,
    BOT_POOL_TABLE,
    WARM_POOL_MODE,
    ECS_CONTAINER_METADATA_URI,
)

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
sessions_table = dynamodb.Table(SESSIONS_TABLE)
sqs_client = boto3.client("sqs", region_name=AWS_REGION)
secrets_client = boto3.client("secretsmanager", region_name=AWS_REGION)

bot_pool_table = dynamodb.Table(BOT_POOL_TABLE) if BOT_POOL_TABLE else None


def get_task_arn() -> Optional[str]:
    """Get ECS task ARN from metadata endpoint."""
    if not ECS_CONTAINER_METADATA_URI:
        return None
    
    try:
        response = requests.get(f"{ECS_CONTAINER_METADATA_URI}/task", timeout=5)
        if response.status_code == 200:
            metadata = response.json()
            return metadata.get("TaskARN")
    except Exception as e:
        logger.warning(f"Failed to get task ARN from metadata: {e}")
    
    return None


def get_gmail_credentials(credential_id: str) -> tuple:
    """Get Gmail credentials from Secrets Manager."""
    secret_name = f"{ENVIRONMENT}/bot-credentials/{credential_id}"
    logger.info(f"Fetching Gmail credentials from: {secret_name}")

    try:
        response = secrets_client.get_secret_value(SecretId=secret_name)
        secret = json.loads(response["SecretString"])

        dynamodb_client = boto3.resource("dynamodb", region_name=AWS_REGION)
        bot_credentials_table = dynamodb_client.Table(f"{ENVIRONMENT}-BotCredentials")
        cred_response = bot_credentials_table.get_item(Key={"credential_id": credential_id})

        if "Item" not in cred_response:
            raise ValueError(f"Bot credential {credential_id} not found in DynamoDB")

        email = cred_response["Item"].get("email", "")
        password = secret.get("password", "")

        return email, password
    except Exception as e:
        logger.error(f"Failed to get Gmail credentials: {e}")
        raise


def update_session_status(session_id: str, status: str, task_arn: str = None, container_id: str = None) -> None:
    """Update session status in DynamoDB."""
    try:
        now = datetime.now(timezone.utc).isoformat()
        update_expr = "SET bot_status = :status, updated_at = :updated_at"
        expr_values = {
            ":status": status,
            ":updated_at": now,
        }

        if task_arn:
            update_expr += ", task_arn = :task_arn"
            expr_values[":task_arn"] = task_arn

        if container_id:
            update_expr += ", container_id = :container_id"
            expr_values[":container_id"] = container_id

        # Set start_time when bot joins meeting
        if status == "in_meeting":
            update_expr += ", start_time = :start_time"
            expr_values[":start_time"] = now

        # Set end_time when session completes
        if status == "completed":
            update_expr += ", end_time = :end_time"
            expr_values[":end_time"] = now

        sessions_table.update_item(
            Key={"session_id": session_id},
            UpdateExpression=update_expr,
            ConditionExpression="attribute_exists(session_id)",
            ExpressionAttributeValues=expr_values,
        )
        logger.info(f"Updated session {session_id} status to: {status}")
    except sessions_table.meta.client.exceptions.ConditionalCheckFailedException:
        logger.warning(f"Session {session_id} not found, skipping status update")
    except Exception as e:
        logger.error(f"Failed to update session status: {e}")


class BotPoolManager:
    """Manage bot pool registration and status updates."""

    def __init__(self, container_id: str, credential_id: str, task_arn: str = None):
        self._container_id = container_id
        self._credential_id = credential_id
        self._task_arn = task_arn
        self._current_session_id: Optional[str] = None

    def register(self) -> None:
        """Update container status to idle (record created by StartWarmPool Lambda)."""
        if not bot_pool_table:
            return

        try:
            container_id = self._task_arn.split("/")[-1] if self._task_arn else self._container_id
            
            bot_pool_table.update_item(
                Key={"container_id": container_id},
                UpdateExpression="SET #status = :status, last_heartbeat = :hb",
                ExpressionAttributeNames={"#status": "status"},
                ExpressionAttributeValues={
                    ":status": "idle",
                    ":hb": datetime.now(timezone.utc).isoformat(),
                },
            )
            self._container_id = container_id
            logger.info(f"Updated container {container_id} status to 'idle'")
        except Exception as e:
            logger.error(f"Failed to update status to idle: {e}")
            # Fallback: create new entry if update fails
            self._register_fallback()

    def _register_fallback(self) -> None:
        """Fallback: create new entry if update fails."""
        try:
            container_id = self._task_arn.split("/")[-1] if self._task_arn else self._container_id
            
            bot_pool_table.put_item(Item={
                "container_id": container_id,
                "credential_id": self._credential_id,
                "task_arn": self._task_arn,
                "status": "idle",
                "current_session_id": None,
                "registered_at": datetime.now(timezone.utc).isoformat(),
                "last_heartbeat": datetime.now(timezone.utc).isoformat(),
                "ttl": int(time.time()) + 86400,
            })
            self._container_id = container_id
            logger.info(f"Fallback: Created new bot pool entry for {container_id}")
        except Exception as e:
            logger.error(f"Fallback registration also failed: {e}")

    def set_busy(self, session_id: str) -> None:
        """Mark container as busy with a session."""
        if not bot_pool_table:
            return

        self._current_session_id = session_id
        try:
            bot_pool_table.update_item(
                Key={"container_id": self._container_id},
                UpdateExpression="SET #status = :status, current_session_id = :sid, last_heartbeat = :hb",
                ConditionExpression="attribute_exists(container_id)",
                ExpressionAttributeNames={"#status": "status"},
                ExpressionAttributeValues={
                    ":status": "busy",
                    ":sid": session_id,
                    ":hb": datetime.now(timezone.utc).isoformat(),
                },
            )
        except bot_pool_table.meta.client.exceptions.ConditionalCheckFailedException:
            logger.warning(f"Container {self._container_id} not found in pool")
        except Exception as e:
            logger.error(f"Failed to set busy status: {e}")

    def set_idle(self) -> None:
        """Mark container as idle (ready for new meeting)."""
        if not bot_pool_table:
            return

        self._current_session_id = None
        try:
            bot_pool_table.update_item(
                Key={"container_id": self._container_id},
                UpdateExpression="SET #status = :status, current_session_id = :sid, last_heartbeat = :hb",
                ConditionExpression="attribute_exists(container_id)",
                ExpressionAttributeNames={"#status": "status"},
                ExpressionAttributeValues={
                    ":status": "idle",
                    ":sid": None,
                    ":hb": datetime.now(timezone.utc).isoformat(),
                },
            )
        except bot_pool_table.meta.client.exceptions.ConditionalCheckFailedException:
            logger.warning(f"Container {self._container_id} not found in pool")
        except Exception as e:
            logger.error(f"Failed to set idle status: {e}")

    def heartbeat(self) -> None:
        """Update heartbeat timestamp."""
        if not bot_pool_table:
            return

        try:
            bot_pool_table.update_item(
                Key={"container_id": self._container_id},
                UpdateExpression="SET last_heartbeat = :hb, #ttl = :ttl",
                ConditionExpression="attribute_exists(container_id)",
                ExpressionAttributeNames={"#ttl": "ttl"},
                ExpressionAttributeValues={
                    ":hb": datetime.now(timezone.utc).isoformat(),
                    ":ttl": int(time.time()) + 86400,
                },
            )
        except bot_pool_table.meta.client.exceptions.ConditionalCheckFailedException:
            logger.warning(f"Container {self._container_id} not found in pool, skipping heartbeat")
        except Exception as e:
            logger.error(f"Failed to update heartbeat: {e}")

    def deregister(self) -> None:
        """Remove container from bot pool."""
        if not bot_pool_table:
            return

        try:
            bot_pool_table.delete_item(Key={"container_id": self._container_id})
            logger.info(f"Deregistered container {self._container_id} from bot pool")
        except Exception as e:
            logger.error(f"Failed to deregister from bot pool: {e}")


class MeetingOrchestrator:
    """Orchestrator for running meeting bot and transcription."""

    def __init__(self, gmail_email: str, gmail_password: str):
        """Initialize MeetingOrchestrator."""
        self._browser_manager = BrowserManager()
        self._transcribe_manager: Optional[TranscribeStreamingManager] = None
        self._is_running = False
        self._gmail_email = gmail_email
        self._gmail_password = gmail_password
        self._page = None
        self._is_logged_in = False

    async def initialize(self) -> None:
        """Initialize browser and login to Gmail (for warm pool mode)."""
        logger.info("Initializing browser and logging in...")
        self._page = await self._browser_manager.start()
        await self._login_gmail(self._page)
        self._is_logged_in = True
        logger.info("Initialization complete, ready for meetings")

    async def run_single_meeting(self, session_id: str, meeting_url: str, container_id: str = None) -> None:
        """Run a single meeting session."""
        logger.info(f"Starting meeting for session: {session_id}")
        logger.info(f"Meeting URL: {meeting_url}")

        update_session_status(session_id, "joining", container_id=container_id)

        try:
            if not self._is_logged_in:
                self._page = await self._browser_manager.start()
                await self._login_gmail(self._page)
                self._is_logged_in = True

            await self._join_meeting(self._page, meeting_url)
            update_session_status(session_id, "in_meeting", container_id=container_id)

            if ENABLE_TRANSCRIPTION:
                await self._start_transcription(session_id)

            self._is_running = True
            await self._keep_alive(self._page, session_id)

        except Exception as e:
            logger.exception(f"Error in meeting: {e}")
            update_session_status(session_id, "failed", container_id=container_id)
            raise
        finally:
            update_session_status(session_id, "completed", container_id=container_id)
            await self._cleanup_meeting()

    async def _cleanup_meeting(self) -> None:
        """Cleanup after a meeting (but keep browser open for warm pool)."""
        logger.info("Cleaning up meeting...")

        if self._transcribe_manager:
            await self._transcribe_manager.stop()
            self._transcribe_manager = None

        # Leave the meeting but keep browser open
        if self._page and self._is_logged_in:
            await self._leave_meeting()

            try:
                await self._page.goto("https://meet.google.com")
                await self._page.wait_for_load_state("networkidle", timeout=10000)
            except Exception as e:
                logger.warning(f"Could not navigate to meet homepage: {e}")

        self._is_running = False
        logger.info("Meeting cleanup complete")

    async def _leave_meeting(self) -> None:
        """Click leave button to exit meeting."""
        leave_selectors = [
            '[aria-label*="Leave call"]',
            '[aria-label*="Tinggalkan panggilan"]',
            '[aria-label*="Keluar"]',
            'button[data-tooltip*="Leave"]',
            '[jsname="CQylAd"]',
            'button:has-text("Leave")',
            'button:has-text("Tinggalkan")',
        ]

        for selector in leave_selectors:
            try:
                btn = self._page.locator(selector)
                if await btn.count() > 0:
                    await btn.first.click()
                    logger.info(f"Clicked leave button: {selector}")
                    await asyncio.sleep(2)
                    return
            except Exception as e:
                logger.debug(f"Leave selector {selector} failed: {e}")
                continue

        logger.warning("Could not find leave button, trying keyboard shortcut")
        try:
            await self._page.keyboard.press("Control+d")
            await asyncio.sleep(2)
        except Exception as e:
            logger.warning(f"Keyboard shortcut failed: {e}")

    async def cleanup_full(self) -> None:
        """Full cleanup including browser shutdown."""
        logger.info("Full cleanup...")
        await self._cleanup_meeting()
        await self._browser_manager.stop()
        self._is_logged_in = False
        self._page = None
        logger.info("Full cleanup complete")

    async def stop(self) -> None:
        """Stop orchestrator gracefully."""
        logger.info("Stopping orchestrator...")
        self._is_running = False

    async def _start_transcription(self, session_id: str) -> None:
        """Start transcription service."""
        logger.info("Starting transcription service...")
        await asyncio.sleep(2)
        self._transcribe_manager = TranscribeStreamingManager(session_id)
        asyncio.create_task(self._run_transcription())
        logger.info("Transcription service started")

    async def _run_transcription(self) -> None:
        """Run transcription in background."""
        try:
            await self._transcribe_manager.start()
        except Exception as e:
            logger.error(f"Transcription error: {e}")

    async def _login_gmail(self, page) -> None:
        """Login to Gmail account."""
        logger.info("Logging in to Gmail...")

        await page.goto("https://accounts.google.com/signin")
        await page.wait_for_load_state("networkidle")

        logger.info("Entering email...")
        await page.fill('input[type="email"]', self._gmail_email)
        await page.click('button:has-text("Next"), #identifierNext')

        logger.info("Waiting for password field...")
        await page.wait_for_selector('input[type="password"]', state="visible", timeout=15000)

        logger.info("Entering password...")
        await page.fill('input[type="password"]', self._gmail_password)
        await page.click('button:has-text("Next"), #passwordNext')

        logger.info("Waiting for login to complete...")
        await page.wait_for_load_state("networkidle", timeout=15000)

        try:
            await page.wait_for_function(
                "() => !window.location.href.includes('accounts.google.com/signin')",
                timeout=10000
            )
        except Exception:
            logger.warning("Login redirect check timed out, continuing anyway")

        logger.info("Gmail login successful")

    async def _join_meeting(self, page, meeting_url: str) -> None:
        """Join Google Meet meeting."""
        logger.info(f"Joining meeting: {meeting_url}")

        await page.goto(meeting_url)
        await page.wait_for_load_state("networkidle", timeout=30000)

        try:
            await page.wait_for_selector(
                '[data-meeting-title], [aria-label*="Join"], button:has-text("Join"), button:has-text("Ask to join")',
                state="visible",
                timeout=15000
            )
        except Exception:
            logger.warning("Meet UI elements not found immediately, continuing...")

        try:
            dismiss_btn = page.locator('button:has-text("Dismiss")')
            if await dismiss_btn.count() > 0:
                await dismiss_btn.click()
                await asyncio.sleep(0.5)
        except Exception:
            pass

        await self._fill_name_if_needed(page)
        await self._disable_media(page)
        await self._click_join_button(page)

        logger.info("Successfully joined meeting")

    async def _fill_name_if_needed(self, page) -> None:
        """Fill in name if there is a prompt for guest."""
        try:
            name_input = page.locator('input[placeholder*="name"], input[aria-label*="name"]')
            if await name_input.count() > 0:
                await name_input.fill("Meeting Bot")
                await asyncio.sleep(1)
        except Exception:
            pass

    async def _disable_media(self, page) -> None:
        """Disable camera and microphone."""
        logger.info("Disabling camera and microphone...")

        try:
            camera_btn = page.locator('[aria-label*="camera"], [data-is-muted="false"][aria-label*="camera"]')
            if await camera_btn.count() > 0:
                await camera_btn.first.click()
                await asyncio.sleep(0.5)

            mic_btn = page.locator('[aria-label*="microphone"], [data-is-muted="false"][aria-label*="microphone"]')
            if await mic_btn.count() > 0:
                await mic_btn.first.click()
                await asyncio.sleep(0.5)
        except Exception as e:
            logger.warning(f"Could not disable media: {e}")

    async def _click_join_button(self, page) -> None:
        """Click join meeting button."""
        logger.info("Looking for join button...")

        join_selectors = [
            'button:has-text("Join now")',
            'button:has-text("Ask to join")',
            'button:has-text("Gabung sekarang")',
            'button:has-text("Minta untuk bergabung")',
            '[jsname="Qx7uuf"]',
        ]

        combined_selector = ", ".join(join_selectors)
        try:
            await page.wait_for_selector(combined_selector, state="visible", timeout=15000)
        except Exception:
            logger.warning("Join button not found within timeout")

        for selector in join_selectors:
            try:
                btn = page.locator(selector)
                if await btn.count() > 0:
                    await btn.first.click()
                    logger.info(f"Clicked join button: {selector}")

                    try:
                        await page.wait_for_selector(
                            '[aria-label*="Leave call"], [aria-label*="Turn off microphone"], [data-meeting-title]',
                            state="visible",
                            timeout=20000
                        )
                        logger.info("Successfully entered meeting room")
                    except Exception:
                        logger.info("Waiting for host to admit or meeting to start...")
                        await asyncio.sleep(3)
                    return
            except Exception:
                continue

        logger.warning("Could not find join button")

    async def _keep_alive(self, page, session_id: str) -> None:
        """Keep session alive while meeting is ongoing."""
        logger.info(f"Starting keep-alive loop (interval: {KEEP_ALIVE_INTERVAL}s)")

        while self._is_running:
            try:
                if await self._check_stop_signal(session_id):
                    logger.info("Stop signal received, ending meeting")
                    break

                is_in_meeting = await self._check_meeting_status(page)

                if not is_in_meeting:
                    logger.warning("No longer in meeting, stopping")
                    break

                logger.debug("Keep-alive check: Still in meeting")
                await asyncio.sleep(KEEP_ALIVE_INTERVAL)

            except Exception as e:
                logger.error(f"Keep-alive error: {e}")
                await asyncio.sleep(KEEP_ALIVE_INTERVAL)

    async def _check_stop_signal(self, session_id: str) -> bool:
        """Check if stop signal was sent for this session."""
        try:
            response = sessions_table.get_item(
                Key={"session_id": session_id},
                ProjectionExpression="stop_requested, bot_status"
            )
            item = response.get("Item", {})
            return item.get("stop_requested", False) or item.get("bot_status") == "stopping"
        except Exception as e:
            logger.warning(f"Error checking stop signal: {e}")
            return False

    async def _check_meeting_status(self, page) -> bool:
        """Check if still in meeting."""
        try:
            current_url = page.url
            logger.debug(f"Current URL: {current_url}")

            if "meet.google.com" not in current_url:
                logger.warning(f"URL changed, no longer on Google Meet: {current_url}")
                return False

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

            logger.debug("No meeting indicators found, assuming still in meeting")
            return True

        except Exception as e:
            logger.error(f"Error checking meeting status: {e}")
            return True


async def poll_sqs_for_meetings(orchestrator: MeetingOrchestrator, pool_manager: BotPoolManager, credential_id: str) -> None:
    """Poll SQS for meeting requests (warm pool mode)."""
    logger.info(f"Starting SQS polling for credential: {credential_id}")

    while True:
        try:
            pool_manager.heartbeat()

            response = sqs_client.receive_message(
                QueueUrl=SQS_QUEUE_URL,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=20,
                MessageAttributeNames=["All"],
            )

            messages = response.get("Messages", [])

            if not messages:
                logger.debug("No messages in queue, continuing to poll...")
                continue

            message = messages[0]
            receipt_handle = message["ReceiptHandle"]

            try:
                body = json.loads(message["Body"])
                msg_credential_id = body.get("credential_id")

                if msg_credential_id != credential_id:
                    logger.debug(f"Message for different credential ({msg_credential_id}), skipping")
                    continue

                session_id = body.get("session_id")
                meeting_url = body.get("meeting_url")

                if not session_id or not meeting_url:
                    logger.warning(f"Invalid message format: {body}")
                    sqs_client.delete_message(QueueUrl=SQS_QUEUE_URL, ReceiptHandle=receipt_handle)
                    continue

                logger.info(f"Received meeting request: session={session_id}, url={meeting_url}")

                # Delete message from queue before processing
                sqs_client.delete_message(QueueUrl=SQS_QUEUE_URL, ReceiptHandle=receipt_handle)

                # Mark as busy and process meeting
                pool_manager.set_busy(session_id)

                try:
                    await orchestrator.run_single_meeting(
                        session_id=session_id,
                        meeting_url=meeting_url,
                        container_id=pool_manager._container_id,
                    )
                except Exception as e:
                    logger.error(f"Meeting failed: {e}")

                pool_manager.set_idle()
                logger.info("Ready for next meeting")

            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse message: {e}")
                sqs_client.delete_message(QueueUrl=SQS_QUEUE_URL, ReceiptHandle=receipt_handle)

        except Exception as e:
            logger.error(f"Error polling SQS: {e}")
            await asyncio.sleep(5)


async def main_warm_pool():
    """Main function for warm pool mode."""
    if not CREDENTIAL_ID:
        logger.error("CREDENTIAL_ID must be set for warm pool mode")
        sys.exit(1)

    if not SQS_QUEUE_URL:
        logger.error("SQS_QUEUE_URL must be set for warm pool mode")
        sys.exit(1)

    container_id = str(uuid.uuid4())
    task_arn = get_task_arn()
    logger.info(f"Starting warm pool container: {container_id} (task_arn: {task_arn})")

    gmail_email, gmail_password = get_gmail_credentials(CREDENTIAL_ID)

    if not gmail_email or not gmail_password:
        logger.error("Gmail credentials not found")
        sys.exit(1)

    orchestrator = MeetingOrchestrator(gmail_email, gmail_password)
    pool_manager = BotPoolManager(container_id, CREDENTIAL_ID, task_arn)

    shutdown_event = asyncio.Event()

    def signal_handler(sig, frame):
        logger.info(f"Received signal {sig}, shutting down...")
        shutdown_event.set()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        await orchestrator.initialize()

        pool_manager.register()

        poll_task = asyncio.create_task(
            poll_sqs_for_meetings(orchestrator, pool_manager, CREDENTIAL_ID)
        )

        await shutdown_event.wait()

        poll_task.cancel()
        try:
            await poll_task
        except asyncio.CancelledError:
            pass

    finally:
        pool_manager.deregister()
        await orchestrator.cleanup_full()


async def main_cold_start():
    """Main function for cold start mode (legacy)."""
    if not SESSION_ID:
        logger.error("SESSION_ID must be set")
        sys.exit(1)

    if not PROJECT_ID:
        logger.error("PROJECT_ID must be set")
        sys.exit(1)

    if not CREDENTIAL_ID:
        logger.error("CREDENTIAL_ID must be set")
        sys.exit(1)

    if not MEETING_URL:
        logger.error("MEETING_URL must be set")
        sys.exit(1)

    gmail_email, gmail_password = get_gmail_credentials(CREDENTIAL_ID)

    if not gmail_email or not gmail_password:
        logger.error("Gmail credentials not found in Secrets Manager")
        sys.exit(1)

    orchestrator = MeetingOrchestrator(gmail_email, gmail_password)

    def signal_handler(sig, frame):
        logger.info(f"Received signal {sig}, shutting down...")
        asyncio.create_task(orchestrator.stop())

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        await orchestrator.run_single_meeting(SESSION_ID, MEETING_URL)
    finally:
        await orchestrator.cleanup_full()


async def main():
    """Main entry point - choose mode based on environment."""
    if WARM_POOL_MODE:
        logger.info("Running in WARM POOL mode")
        await main_warm_pool()
    else:
        logger.info("Running in COLD START mode")
        await main_cold_start()


if __name__ == "__main__":
    asyncio.run(main())
