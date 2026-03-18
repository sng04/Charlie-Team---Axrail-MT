"""
Transcribe Handler Module

Handle streaming to Amazon Transcribe and save to DynamoDB.
"""

import asyncio
import logging
import os
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from typing import Dict, List, Optional

import boto3
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent, TranscriptResultStream

from audio_capture import AudioCapture, SAMPLE_RATE
from config import AWS_REGION, TRANSCRIPTS_TABLE, TRANSCRIBE_LANGUAGE

logger = logging.getLogger(__name__)

BUFFER_TIMEOUT_SECONDS = float(os.environ.get("BUFFER_TIMEOUT", "2.0"))
ENABLE_SPEAKER_ID = os.environ.get("ENABLE_SPEAKER_ID", "true").lower() == "true"


class DynamoDBHandler:
    """Handle saving transcripts to DynamoDB."""

    def __init__(self, table_name: str, session_id: str):
        self._dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
        self._table = self._dynamodb.Table(table_name)
        self._session_id = session_id
        logger.info(f"DynamoDB handler initialized for table: {table_name}")

    def save_transcript(
        self,
        text: str,
        speaker: Optional[str] = None,
        start_time: Optional[float] = None,
        end_time: Optional[float] = None,
    ) -> None:
        """Save transcript to DynamoDB."""
        if not text.strip():
            return

        timestamp = datetime.now(timezone.utc).isoformat()

        item = {
            "session_id": self._session_id,
            "timestamp": timestamp,
            "transcript_id": str(uuid.uuid4()),
            "text": text.strip(),
            "is_partial": False,
            "created_at": timestamp,
        }

        if speaker:
            item["speaker"] = speaker
        if start_time is not None:
            item["start_time"] = str(round(start_time, 2))
        if end_time is not None:
            item["end_time"] = str(round(end_time, 2))

        try:
            self._table.put_item(Item=item)
            speaker_info = f" [{speaker}]" if speaker else ""
            logger.info(f"💾 Saved{speaker_info}: {text}")
        except Exception as e:
            logger.error(f"Failed to save transcript: {e}")


class TranscriptDeduplicator:
    """Deduplication to avoid duplicate transcripts."""

    def __init__(self, similarity_threshold: float = 0.8, time_window: float = 1.0):
        self._processed_result_ids: set = set()
        self._recent_texts: List[Dict] = []
        self._similarity_threshold = similarity_threshold
        self._time_window = time_window
        self._max_history = 20

    def is_duplicate(
        self,
        result_id: str,
        text: str,
        start_time: Optional[float],
        end_time: Optional[float],
    ) -> bool:
        """Check if this transcript is a duplicate."""
        if result_id and result_id in self._processed_result_ids:
            logger.debug(f"Skipping duplicate result_id: {result_id}")
            return True

        text_lower = text.lower().strip()
        for recent in self._recent_texts:
            similarity = self._calculate_similarity(text_lower, recent["text"].lower())
            if similarity >= self._similarity_threshold:
                if start_time and recent.get("end_time"):
                    time_diff = abs(start_time - recent["end_time"])
                    if time_diff < self._time_window:
                        logger.debug(
                            f"Skipping similar text (sim={similarity:.2f}): {text[:50]}..."
                        )
                        return True

        for recent in self._recent_texts:
            recent_lower = recent["text"].lower()
            if text_lower in recent_lower or recent_lower in text_lower:
                if start_time and recent.get("end_time"):
                    time_diff = abs(start_time - recent["end_time"])
                    if time_diff < self._time_window:
                        logger.debug(f"Skipping substring text: {text[:50]}...")
                        return True

        return False

    def mark_processed(
        self,
        result_id: str,
        text: str,
        start_time: Optional[float],
        end_time: Optional[float],
    ) -> None:
        """Mark transcript as already processed."""
        if result_id:
            self._processed_result_ids.add(result_id)
            if len(self._processed_result_ids) > 1000:
                self._processed_result_ids = set(
                    list(self._processed_result_ids)[-500:]
                )

        self._recent_texts.append(
            {"text": text, "time": start_time, "end_time": end_time}
        )

        if len(self._recent_texts) > self._max_history:
            self._recent_texts = self._recent_texts[-self._max_history :]

    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two texts."""
        if not text1 or not text2:
            return 0.0

        words1 = set(text1.split())
        words2 = set(text2.split())

        if not words1 or not words2:
            return 0.0

        intersection = words1 & words2
        union = words1 | words2

        return len(intersection) / len(union) if union else 0.0


class SpeakerBuffer:
    """Buffer for collecting transcripts per speaker."""

    def __init__(self, dynamodb_handler: DynamoDBHandler, timeout: float = 2.0):
        self._dynamodb = dynamodb_handler
        self._timeout = timeout
        self._buffers: Dict[str, Dict] = defaultdict(
            lambda: {
                "texts": [],
                "start_time": None,
                "end_time": None,
                "last_update": 0,
            }
        )
        self._current_speaker: Optional[str] = None
        self._segment_count = 0
        self._deduplicator = TranscriptDeduplicator()

    def add_segment(
        self,
        text: str,
        speaker: Optional[str],
        start_time: Optional[float],
        end_time: Optional[float],
        result_id: Optional[str] = None,
    ) -> None:
        """Add a transcript segment with deduplication."""
        if not text.strip():
            return

        if self._deduplicator.is_duplicate(result_id, text, start_time, end_time):
            logger.debug(f"Skipped duplicate: {text[:50]}...")
            return

        self._deduplicator.mark_processed(result_id, text, start_time, end_time)

        speaker_key = speaker or "unknown"
        current_time = asyncio.get_event_loop().time()
        self._segment_count += 1

        if self._current_speaker and speaker_key != self._current_speaker:
            logger.info(
                f"Speaker changed from {self._current_speaker} to {speaker_key}, flushing..."
            )
            self._flush_speaker(self._current_speaker)

        self._current_speaker = speaker_key

        buf = self._buffers[speaker_key]
        buf["texts"].append(text.strip())
        buf["last_update"] = current_time

        if buf["start_time"] is None:
            buf["start_time"] = start_time
        buf["end_time"] = end_time

        if self._segment_count >= 5:
            logger.info(f"Flushing after {self._segment_count} segments...")
            self._flush_speaker(speaker_key)
            self._segment_count = 0

    def _flush_speaker(self, speaker: str) -> None:
        """Flush buffer for a specific speaker."""
        if speaker not in self._buffers:
            return

        buf = self._buffers[speaker]
        if not buf["texts"]:
            return

        combined_text = " ".join(buf["texts"])

        self._dynamodb.save_transcript(
            text=combined_text,
            speaker=speaker if speaker != "unknown" else None,
            start_time=buf["start_time"],
            end_time=buf["end_time"],
        )

        buf["texts"] = []
        buf["start_time"] = None
        buf["end_time"] = None

    def check_timeouts(self) -> None:
        """Flush buffers that have timed out."""
        current_time = asyncio.get_event_loop().time()

        for speaker, buf in list(self._buffers.items()):
            if buf["texts"] and (current_time - buf["last_update"]) > self._timeout:
                self._flush_speaker(speaker)

    def flush_all(self) -> None:
        """Flush all buffers."""
        for speaker in list(self._buffers.keys()):
            self._flush_speaker(speaker)


class MeetingTranscriptHandler(TranscriptResultStreamHandler):
    """Handler for processing transcript events from Transcribe."""

    def __init__(
        self,
        transcript_result_stream: TranscriptResultStream,
        dynamodb_handler: DynamoDBHandler,
    ):
        super().__init__(transcript_result_stream)
        self._dynamodb = dynamodb_handler
        self._buffer = SpeakerBuffer(dynamodb_handler, BUFFER_TIMEOUT_SECONDS)

    async def handle_transcript_event(self, transcript_event: TranscriptEvent) -> None:
        """Handle transcript event from Transcribe."""
        results = transcript_event.transcript.results

        for result in results:
            if result.is_partial:
                continue

            if not result.alternatives:
                continue

            alternative = result.alternatives[0]
            transcript_text = alternative.transcript

            if not transcript_text or not transcript_text.strip():
                continue

            result_id = getattr(result, "result_id", None)
            speaker = self._extract_speaker(alternative)

            speaker_info = f" [Speaker {speaker}]" if speaker else ""
            logger.info(f"🎤{speaker_info} {transcript_text}")

            self._buffer.add_segment(
                text=transcript_text,
                speaker=f"spk_{speaker}" if speaker else None,
                start_time=result.start_time,
                end_time=result.end_time,
                result_id=result_id,
            )

            self._buffer.check_timeouts()

    def _extract_speaker(self, alternative) -> Optional[str]:
        """Extract speaker ID from alternative items."""
        if not hasattr(alternative, "items") or not alternative.items:
            return None

        for item in alternative.items:
            if hasattr(item, "speaker") and item.speaker is not None:
                return str(item.speaker)

        return None

    def flush_remaining(self) -> None:
        """Flush remaining buffered transcripts."""
        self._buffer.flush_all()


class TranscribeStreamingManager:
    """Manager for handling Transcribe streaming session."""

    def __init__(self, session_id: str):
        self._session_id = session_id
        self._audio_capture = AudioCapture()
        self._dynamodb = DynamoDBHandler(TRANSCRIPTS_TABLE, session_id)
        self._is_running = False
        self._client: Optional[TranscribeStreamingClient] = None
        self._handler: Optional[MeetingTranscriptHandler] = None

    async def start(self) -> None:
        """Start transcription streaming."""
        logger.info(f"Starting transcription for session: {self._session_id}")
        logger.info(f"Speaker identification enabled: {ENABLE_SPEAKER_ID}")

        self._is_running = True

        await self._audio_capture.start()

        self._client = TranscribeStreamingClient(region=AWS_REGION)

        await self._stream_transcription()

    async def _stream_transcription(self) -> None:
        """Main streaming loop."""
        try:
            stream_params = {
                "language_code": TRANSCRIBE_LANGUAGE,
                "media_sample_rate_hz": SAMPLE_RATE,
                "media_encoding": "pcm",
            }

            if ENABLE_SPEAKER_ID:
                stream_params["show_speaker_label"] = True

            logger.info(f"Starting Transcribe stream with params: {stream_params}")

            stream = await self._client.start_stream_transcription(**stream_params)

            self._handler = MeetingTranscriptHandler(
                stream.output_stream,
                self._dynamodb,
            )

            await asyncio.gather(
                self._send_audio(stream),
                self._handler.handle_events(),
            )

        except Exception as e:
            logger.error(f"Transcription error: {e}")
            raise
        finally:
            if self._handler:
                self._handler.flush_remaining()

    async def _send_audio(self, stream) -> None:
        """Send audio chunks to Transcribe."""
        try:
            async for chunk in self._audio_capture.get_audio_stream():
                if not self._is_running:
                    break
                await stream.input_stream.send_audio_event(audio_chunk=chunk)

            await stream.input_stream.end_stream()

        except Exception as e:
            logger.error(f"Error sending audio: {e}")
            raise

    async def stop(self) -> None:
        """Stop transcription."""
        logger.info("Stopping transcription...")

        self._is_running = False

        if self._handler:
            self._handler.flush_remaining()

        await self._audio_capture.stop()

        logger.info("Transcription stopped")

    @property
    def is_running(self) -> bool:
        return self._is_running
