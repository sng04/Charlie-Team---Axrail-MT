"""
Browser Manager Module

Manages Playwright browser for Meeting Bot.
"""

import asyncio
import logging

from playwright.async_api import async_playwright, Browser, BrowserContext, Page

from config import BROWSER_HEADLESS, BROWSER_TIMEOUT, BROWSER_TYPE

logger = logging.getLogger(__name__)


class BrowserManager:
    """
    Manages browser lifecycle for Google Meet.

    Attributes:
        _playwright: Playwright instance
        _browser: Browser instance
        _context: Browser context with permissions
        _page: Active page for meeting
    """

    def __init__(self):
        """Initialize BrowserManager with empty state."""
        self._playwright = None
        self._browser: Browser = None
        self._context: BrowserContext = None
        self._page: Page = None

    async def start(self) -> Page:
        """
        Start browser with configuration for Google Meet.

        Returns:
            Page: Playwright page ready to use
        """
        logger.info(f"Starting {BROWSER_TYPE} browser (headless={BROWSER_HEADLESS})...")

        self._playwright = await async_playwright().start()

        if BROWSER_TYPE == "firefox":
            await self._start_firefox()
        else:
            await self._start_chromium()

        logger.info("Browser started successfully")
        return self._page

    async def _start_chromium(self) -> None:
        """Start Chromium browser dengan audio support."""
        chromium_args = [
            "--use-fake-ui-for-media-stream",
            "--use-fake-device-for-media-stream",
            "--autoplay-policy=no-user-gesture-required",
            "--disable-web-security",
            "--disable-features=IsolateOrigins,site-per-process",
            "--disable-blink-features=AutomationControlled",
            "--alsa-output-device=pulse",
            "--audio-output-channels=2",
            "--enable-audio-output",
        ]

        if not BROWSER_HEADLESS:
            chromium_args.append("--display=:99")

        self._browser = await self._playwright.chromium.launch(
            headless=BROWSER_HEADLESS,
            args=chromium_args,
        )

        self._context = await self._browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/121.0.0.0 Safari/537.36"
            ),
            locale="en-US",
            timezone_id="America/New_York",
            permissions=["microphone", "camera"],
            color_scheme="light",
        )

        self._context.set_default_timeout(BROWSER_TIMEOUT)
        self._page = await self._context.new_page()

        await self._page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });

            const originalQuery = window.navigator.permissions.query;
            window.navigator.permissions.query = (parameters) => (
                parameters.name === 'notifications' ?
                    Promise.resolve({ state: Notification.permission }) :
                    originalQuery(parameters)
            );
        """)

    async def _start_firefox(self) -> None:
        """Start Firefox browser."""
        self._browser = await self._playwright.firefox.launch(
            headless=BROWSER_HEADLESS,
            firefox_user_prefs={
                "media.navigator.permission.disabled": True,
                "media.navigator.streams.fake": True,
                "permissions.default.microphone": 1,
                "permissions.default.camera": 1,
                "media.volume_scale": "1.0",
                "media.autoplay.default": 0,
                "media.autoplay.enabled.user-gestures-needed": False,
            },
        )

        self._context = await self._browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) "
                "Gecko/20100101 Firefox/122.0"
            ),
            locale="en-US",
            timezone_id="America/New_York",
            color_scheme="light",
        )

        self._context.set_default_timeout(BROWSER_TIMEOUT)
        self._page = await self._context.new_page()

        await self._page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)

    async def stop(self):
        """Stop browser and cleanup resources."""
        logger.info("Stopping browser...")

        if self._context:
            await self._context.close()
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()

        logger.info("Browser stopped")

    @property
    def page(self) -> Page:
        """Get current page."""
        return self._page
