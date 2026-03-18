"""
Audio Capture Module

Capture audio from PulseAudio for streaming to Transcribe.
"""

import asyncio
import logging
import os
import subprocess
import threading
from typing import AsyncGenerator, Optional

logger = logging.getLogger(__name__)

SAMPLE_RATE = 16000  
CHANNELS = 1 
CHUNK_SIZE = 1024 * 2  
BYTES_PER_SAMPLE = 2 

AUDIO_SOURCE = os.environ.get("AUDIO_SOURCE", "auto_null.monitor")


class AudioCapture:
    """
    Capture audio from PulseAudio monitor source.

    Uses parec (PulseAudio recording tool) to capture
    audio output from system (meeting audio).
    """

    def __init__(self):
        """Initialize AudioCapture."""
        self._process: Optional[subprocess.Popen] = None
        self._is_running = False
        self._audio_queue: asyncio.Queue = None
        self._capture_thread: Optional[threading.Thread] = None
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._silence_count = 0
        self._max_silence = 100

    async def start(self) -> None:
        """Start audio capture from PulseAudio."""
        logger.info("Starting audio capture...")

        self._audio_queue = asyncio.Queue(maxsize=200)
        self._is_running = True
        self._loop = asyncio.get_event_loop()

        try:
            result = subprocess.run(
                ["pactl", "info"], capture_output=True, text=True, timeout=5
            )
            if result.returncode != 0:
                logger.error(f"PulseAudio not running: {result.stderr}")
                raise RuntimeError("PulseAudio not available")
            logger.info("PulseAudio is available")
        except Exception as e:
            logger.error(f"Failed to check PulseAudio: {e}")
            raise

        try:
            result = subprocess.run(
                ["pactl", "list", "short", "sources"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            logger.info(f"Available audio sources:\n{result.stdout}")
        except Exception as e:
            logger.warning(f"Could not list sources: {e}")

        cmd = [
            "parec",
            "--rate", str(SAMPLE_RATE),
            "--channels", str(CHANNELS),
            "--format", "s16le",
            "--latency-msec", "50",
            "--device", AUDIO_SOURCE,
            "--raw",
        ]

        logger.info(f"Starting parec with command: {' '.join(cmd)}")

        try:
            self._process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=CHUNK_SIZE,
            )
            logger.info(f"Started parec process with PID: {self._process.pid}")

            await asyncio.sleep(0.5)
            if self._process.poll() is not None:
                stderr = self._process.stderr.read().decode()
                logger.error(f"parec failed to start: {stderr}")
                raise RuntimeError(f"parec failed: {stderr}")

            self._capture_thread = threading.Thread(
                target=self._capture_loop, daemon=True, name="AudioCaptureThread"
            )
            self._capture_thread.start()

            logger.info("Audio capture started successfully")

        except Exception as e:
            logger.error(f"Failed to start audio capture: {e}")
            raise

    def _capture_loop(self) -> None:
        """Background thread to read audio from parec."""
        logger.info("Audio capture loop started")

        while self._is_running and self._process:
            try:
                if self._process.poll() is not None:
                    stderr = (
                        self._process.stderr.read().decode()
                        if self._process.stderr
                        else ""
                    )
                    logger.error(f"parec process died: {stderr}")
                    break

                chunk = self._process.stdout.read(CHUNK_SIZE)

                if not chunk:
                    logger.warning("No audio data received from parec")
                    self._silence_count += 1
                    if self._silence_count > self._max_silence:
                        logger.error(
                            "Too many silent chunks, audio capture may have failed"
                        )
                    continue

                is_silence = all(b == 0 for b in chunk)
                if is_silence:
                    self._silence_count += 1
                    if self._silence_count % 50 == 0:
                        logger.debug(f"Received {self._silence_count} silent chunks")
                else:
                    if self._silence_count > 0:
                        logger.debug(
                            f"Audio detected after {self._silence_count} silent chunks"
                        )
                    self._silence_count = 0

                try:
                    self._loop.call_soon_threadsafe(
                        lambda c=chunk: self._audio_queue.put_nowait(c)
                    )
                except asyncio.QueueFull:
                    logger.warning("Audio queue full, dropping oldest chunk")
                    try:
                        self._loop.call_soon_threadsafe(self._audio_queue.get_nowait)
                        self._loop.call_soon_threadsafe(
                            lambda c=chunk: self._audio_queue.put_nowait(c)
                        )
                    except Exception:
                        pass
                except Exception as e:
                    logger.error(f"Error putting chunk to queue: {e}")

            except Exception as e:
                logger.error(f"Error in capture loop: {e}")
                break

        logger.info("Audio capture loop ended")

    async def get_audio_stream(self) -> AsyncGenerator[bytes, None]:
        """
        Async generator to stream audio chunks.

        Yields:
            bytes: Audio chunk in PCM 16-bit format
        """
        empty_chunk_count = 0
        max_empty_chunks = 150

        while self._is_running:
            try:
                chunk = await asyncio.wait_for(self._audio_queue.get(), timeout=0.1)
                empty_chunk_count = 0
                yield chunk

            except asyncio.TimeoutError:
                empty_chunk_count += 1

                if empty_chunk_count < max_empty_chunks:
                    silence = bytes(CHUNK_SIZE)
                    yield silence
                else:
                    logger.warning(f"No audio for {empty_chunk_count * 0.1:.1f}s")
                    empty_chunk_count = 0

            except Exception as e:
                logger.error(f"Error getting audio chunk: {e}")
                break

    async def stop(self) -> None:
        """Stop audio capture."""
        logger.info("Stopping audio capture...")

        self._is_running = False

        if self._process:
            try:
                self._process.terminate()
                self._process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self._process.kill()
            except Exception as e:
                logger.error(f"Error stopping parec: {e}")
            self._process = None

        if self._capture_thread and self._capture_thread.is_alive():
            self._capture_thread.join(timeout=5)
            self._capture_thread = None

        logger.info("Audio capture stopped")

    @property
    def is_running(self) -> bool:
        """Check if capture is running."""
        return self._is_running
