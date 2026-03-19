"""
Transcribe Handler Module

Handle streaming to Amazon Transcribe and save to DynamoDB.
Real-time mode: saves each sentence immediately without buffering.
"""

import asyncio
import logging
import os
import uuid
from datetime import datetime, timezone
from typing import List, Optional

import boto3
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent, TranscriptResultStream

from audio_capture import AudioCapture, SAMPLE_RATE
from config import AWS_REGION, TRANSCRIPTS_TABLE, TRANSCRIBE_LANGUAGE

logger = logging.getLogger(__name__)

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
        """Save transcript to DynamoDB immediately."""
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

    def __init__(self, similarity_threshold: float = 0.9, time_window: float = 0.5):
        self._processed_result_ids: set = set()
        self._recent_texts: List[dict] = []
        self._similarity_threshold = similarity_threshold
        self._time_window = time_window
        self._max_history = 10

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
            if text_lower == recent["text"].lower():
                logger.debug(f"Skipping exact duplicate: {text[:50]}...")
                return True

            if start_time and recent.get("end_time"):
                time_diff = abs(start_time - recent["end_time"])
                if time_diff < self._time_window:
                    similarity = self._calculate_similarity(
                        text_lower, recent["text"].lower()
                    )
                    if similarity >= self._similarity_threshold:
                        logger.debug(
                            f"Skipping similar text (sim={similarity:.2f}): {text[:50]}..."
                        )
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
            if len(self._processed_result_ids) > 500:
                self._processed_result_ids = set(
                    list(self._processed_result_ids)[-250:]
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


class MeetingTranscriptHandler(TranscriptResultStreamHandler):
    """
    Handler for processing transcript events from Transcribe.
    
    Real-time mode: saves each final sentence immediately to DynamoDB
    without any buffering delay.
    """

    def __init__(
        self,
        transcript_result_stream: TranscriptResultStream,
        dynamodb_handler: DynamoDBHandler,
    ):
        super().__init__(transcript_result_stream)
        self._dynamodb = dynamodb_handler
        self._deduplicator = TranscriptDeduplicator()

    async def handle_transcript_event(self, transcript_event: TranscriptEvent) -> None:
        """
        Handle transcript event from Transcribe.
        
        Saves each final (non-partial) result immediately to DynamoDB.
        """
        results = transcript_event.transcript.results

        for result in results:
            # Skip partial results - only process final sentences
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

            # Check for duplicates
            if self._deduplicator.is_duplicate(
                result_id, transcript_text, result.start_time, result.end_time
            ):
                continue

            # Mark as processed
            self._deduplicator.mark_processed(
                result_id, transcript_text, result.start_time, result.end_time
            )

            speaker_label = f"spk_{speaker}" if speaker else None
            speaker_info = f" [Speaker {speaker}]" if speaker else ""
            logger.info(f"🎤{speaker_info} {transcript_text}")

            # Save immediately to DynamoDB - no buffering
            self._dynamodb.save_transcript(
                text=transcript_text,
                speaker=speaker_label,
                start_time=result.start_time,
                end_time=result.end_time,
            )

    def _extract_speaker(self, alternative) -> Optional[str]:
        """Extract speaker ID from alternative items."""
        if not hasattr(alternative, "items") or not alternative.items:
            return None

        for item in alternative.items:
            if hasattr(item, "speaker") and item.speaker is not None:
                return str(item.speaker)

        return None

    def flush_remaining(self) -> None:
        """No-op since we save immediately without buffering."""
        pass


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
