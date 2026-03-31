"""
Transcribe Handler Module

Handle streaming to Amazon Transcribe and save to DynamoDB.
Merges fragmented results into complete sentences before saving.

Preprocessing:
- Filler word removal (um, uh, hm, etc.)
- Noise pattern filtering (random numbers, repeated chars)
- Confidence threshold filtering
- Sentence merging (fragments → full sentences based on punctuation/time gap)
"""

import asyncio
import logging
import os
import re
import time
import uuid
from datetime import datetime, timezone
from typing import List, Optional

import boto3
from amazon_transcribe.client import TranscribeStreamingClient
from amazon_transcribe.handlers import TranscriptResultStreamHandler
from amazon_transcribe.model import TranscriptEvent, TranscriptResultStream

from audio_capture import AudioCapture, SAMPLE_RATE
from config import AWS_REGION, TRANSCRIPTS_TABLE, TRANSCRIBE_LANGUAGE, TRANSCRIBE_VOCABULARY_NAME, WEBSOCKET_API_URL
from websocket_broadcaster import WebSocketBroadcaster

logger = logging.getLogger(__name__)

ENABLE_SPEAKER_ID = os.environ.get("ENABLE_SPEAKER_ID", "true").lower() == "true"
CONFIDENCE_THRESHOLD = float(os.environ.get("CONFIDENCE_THRESHOLD", "0.5"))

# Filler words to remove
FILLER_WORDS = {
    "um", "uh", "hm", "hmm", "eh", "ah", "er", "erm",
    "um,", "uh,", "hm,", "hmm,", "eh,", "ah,",
}

# Noise patterns (regex)
NOISE_PATTERNS = [
    r"^[0-9]+$",                   
    r"^[0-9\s\.]+$",               
    r"^(.)\1+$",                   
    r"^(yo\s*)+$",                 
    r"^(oh\s*)+$",                  
    r"^[^a-zA-Z]*$",               
]


class TextPreprocessor:
    """Preprocess transcript text before saving."""

    def __init__(self, confidence_threshold: float = 0.5):
        self._confidence_threshold = confidence_threshold
        self._noise_patterns = [re.compile(p, re.IGNORECASE) for p in NOISE_PATTERNS]

    def preprocess(
        self, text: str, confidence: Optional[float] = None
    ) -> Optional[str]:
        """
        Preprocess transcript text.

        Args:
            text: Raw transcript text
            confidence: Average confidence score (0.0-1.0)

        Returns:
            Cleaned text or None if should be filtered out
        """
        if not text:
            return None

        if confidence is not None and confidence < self._confidence_threshold:
            logger.debug(f"Filtered low confidence ({confidence:.2f}): {text}")
            return None

        cleaned = text.strip()

        if cleaned.lower().rstrip(",.!?") in FILLER_WORDS:
            logger.debug(f"Filtered filler word: {text}")
            return None

        cleaned = self._remove_edge_fillers(cleaned)

        if self._is_noise(cleaned):
            logger.debug(f"Filtered noise pattern: {text}")
            return None

        if not cleaned or len(cleaned.strip()) == 0:
            return None

        return cleaned

    def _remove_edge_fillers(self, text: str) -> str:
        """Remove filler words from start and end of text."""
        words = text.split()
        if not words:
            return text

        while words and words[0].lower().rstrip(",.!?") in FILLER_WORDS:
            words.pop(0)

        while words and words[-1].lower().rstrip(",.!?") in FILLER_WORDS:
            words.pop()

        return " ".join(words)

    def _is_noise(self, text: str) -> bool:
        """Check if text matches noise patterns."""
        for pattern in self._noise_patterns:
            if pattern.match(text):
                return True
        return False


class DynamoDBHandler:
    """Handle saving transcripts to DynamoDB with async write support."""

    def __init__(self, table_name: str, session_id: str, broadcaster: Optional["WebSocketBroadcaster"] = None):
        self._dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
        self._table = self._dynamodb.Table(table_name)
        self._session_id = session_id
        self._broadcaster = broadcaster
        self._pending_tasks: List[asyncio.Task] = []
        self._write_count = 0
        self._total_write_time = 0.0
        logger.info(f"DynamoDB handler initialized for table: {table_name}")

    def save_transcript_async(
        self,
        text: str,
        speaker: Optional[str] = None,
        start_time: Optional[float] = None,
        end_time: Optional[float] = None,
        confidence: Optional[float] = None,
    ) -> None:
        """
        Queue transcript for async save to DynamoDB and broadcast to WebSocket.
        
        Returns immediately without waiting for DynamoDB response.
        Both DynamoDB write and WebSocket broadcast happen in parallel.
        """
        if not text.strip():
            return

        timestamp = datetime.now(timezone.utc).isoformat()

        # Build item once - same structure for DDB and WebSocket
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
        if confidence is not None:
            item["confidence"] = str(round(confidence, 3))

        # Create task for parallel DDB write + WebSocket broadcast
        task = asyncio.create_task(self._async_save_and_broadcast(item, text, speaker))
        self._pending_tasks.append(task)
        
        self._cleanup_completed_tasks()
        
        speaker_info = f" [{speaker}]" if speaker else ""
        logger.info(f"📤 Queued{speaker_info}: {text}")

    async def _async_save_and_broadcast(
        self, item: dict, text: str, speaker: Optional[str]
    ) -> None:
        """Execute DynamoDB put_item and WebSocket broadcast in parallel."""
        tasks = [self._async_put_item(item, text, speaker)]
        
        # Broadcast to WebSocket if broadcaster is available
        if self._broadcaster:
            tasks.append(self._broadcaster.broadcast_transcript_line(item))
        
        await asyncio.gather(*tasks, return_exceptions=True)

    async def _async_put_item(
        self, item: dict, text: str, speaker: Optional[str]
    ) -> None:
        """Execute DynamoDB put_item in background."""
        try:
            save_start = time.perf_counter()
            
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(None, lambda: self._table.put_item(Item=item))
            
            save_duration = (time.perf_counter() - save_start) * 1000
            self._write_count += 1
            self._total_write_time += save_duration
            
            speaker_info = f" [{speaker}]" if speaker else ""
            logger.info(f"💾 Saved{speaker_info}: {text} (DDB: {save_duration:.0f}ms)")
            
        except Exception as e:
            logger.error(f"Failed to save transcript async: {e} - text: {text}")

    def _cleanup_completed_tasks(self) -> None:
        """Remove completed tasks from pending list."""
        self._pending_tasks = [t for t in self._pending_tasks if not t.done()]

    async def flush_pending(self) -> None:
        """Wait for all pending writes to complete."""
        if self._pending_tasks:
            logger.info(f"Flushing {len(self._pending_tasks)} pending writes...")
            await asyncio.gather(*self._pending_tasks, return_exceptions=True)
            self._pending_tasks.clear()
            
        if self._write_count > 0:
            avg_time = self._total_write_time / self._write_count
            logger.info(
                f"DynamoDB stats: {self._write_count} writes, "
                f"avg {avg_time:.0f}ms per write"
            )


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



class SentenceMerger:
    """
    Merge fragmented transcript results into complete sentences.

    Transcribe often splits a single sentence into multiple short fragments
    (e.g. "And" / "how" / "about the main feature we discussed.").
    This class buffers fragments and merges them when a sentence boundary
    is detected (punctuation or time gap).
    """

    # Max seconds of silence between fragments before flushing
    MERGE_GAP_THRESHOLD = float(os.environ.get("MERGE_GAP_THRESHOLD", "1.0"))
    # Min word count to consider a fragment "complete enough" on its own
    MIN_STANDALONE_WORDS = int(os.environ.get("MERGE_MIN_STANDALONE_WORDS", "4"))

    def __init__(self):
        self._buffer_text: List[str] = []
        self._buffer_speaker: Optional[str] = None
        self._buffer_start_time: Optional[float] = None
        self._buffer_end_time: Optional[float] = None
        self._buffer_confidences: List[float] = []
        self._flush_task: Optional[asyncio.TimerHandle] = None

    def _cancel_flush_timer(self) -> None:
        if self._flush_task is not None:
            self._flush_task.cancel()
            self._flush_task = None

    def _schedule_flush_timer(self, callback) -> None:
        """Schedule a delayed flush in case no more fragments arrive."""
        self._cancel_flush_timer()
        loop = asyncio.get_event_loop()
        self._flush_task = loop.call_later(self.MERGE_GAP_THRESHOLD, callback)

    def add_fragment(
        self,
        text: str,
        speaker: Optional[str],
        start_time: Optional[float],
        end_time: Optional[float],
        confidence: Optional[float],
        flush_callback,
    ) -> Optional[dict]:
        """
        Add a fragment. Returns a merged sentence dict if ready to flush,
        otherwise returns None (buffered).
        """
        self._cancel_flush_timer()

        flush_result = None

        # Check time gap — if too large, flush old buffer first
        if (
            self._buffer_text
            and self._buffer_end_time is not None
            and start_time is not None
        ):
            gap = start_time - self._buffer_end_time
            if gap > self.MERGE_GAP_THRESHOLD:
                flush_result = self._flush_buffer()

        # Append to buffer
        self._buffer_text.append(text)
        self._buffer_speaker = speaker
        if self._buffer_start_time is None:
            self._buffer_start_time = start_time
        self._buffer_end_time = end_time
        if confidence is not None:
            self._buffer_confidences.append(confidence)

        # Check if this fragment ends a sentence
        if self._is_sentence_end(text):
            merged = self._flush_buffer()
            # If we also flushed a previous buffer due to time gap,
            # return that one first — the caller should handle both
            if flush_result:
                return flush_result  # merged will be handled via timer or next call
            return merged

        # Schedule a timer flush in case nothing else arrives
        self._schedule_flush_timer(flush_callback)

        return flush_result

    def _is_sentence_end(self, text: str) -> bool:
        """Check if text ends with sentence-ending punctuation."""
        stripped = text.rstrip()
        if not stripped:
            return False
        return stripped[-1] in ".?!"

    def _flush_buffer(self) -> Optional[dict]:
        """Flush current buffer and return merged sentence."""
        if not self._buffer_text:
            return None

        self._cancel_flush_timer()

        merged_text = " ".join(self._buffer_text)
        avg_confidence = (
            sum(self._buffer_confidences) / len(self._buffer_confidences)
            if self._buffer_confidences
            else None
        )

        result = {
            "text": merged_text,
            "speaker": self._buffer_speaker,
            "start_time": self._buffer_start_time,
            "end_time": self._buffer_end_time,
            "confidence": avg_confidence,
        }

        # Reset buffer
        self._buffer_text = []
        self._buffer_speaker = None
        self._buffer_start_time = None
        self._buffer_end_time = None
        self._buffer_confidences = []

        return result

    def flush_remaining(self) -> Optional[dict]:
        """Flush any remaining buffered text (called at end of session)."""
        self._cancel_flush_timer()
        return self._flush_buffer()


class MeetingTranscriptHandler(TranscriptResultStreamHandler):
    """
    Handler for processing transcript events from Transcribe.

    Merges fragmented results into complete sentences before saving.

    Preprocessing:
    - Filler word removal
    - Noise pattern filtering
    - Confidence threshold filtering
    - Sentence merging (fragments → full sentences)
    """

    def __init__(
        self,
        transcript_result_stream: TranscriptResultStream,
        dynamodb_handler: DynamoDBHandler,
    ):
        super().__init__(transcript_result_stream)
        self._dynamodb = dynamodb_handler
        self._deduplicator = TranscriptDeduplicator()
        self._preprocessor = TextPreprocessor(CONFIDENCE_THRESHOLD)
        self._merger = SentenceMerger()

    def _save_merged(self, merged: dict) -> None:
        """Save a merged sentence to DynamoDB."""
        speaker_label = f"spk_{merged['speaker']}" if merged["speaker"] else None
        speaker_info = f" [Speaker {merged['speaker']}]" if merged["speaker"] else ""
        confidence_info = (
            f" (conf: {merged['confidence']:.2f})" if merged["confidence"] else ""
        )
        logger.info(f"🎤{speaker_info}{confidence_info} {merged['text']}")

        self._dynamodb.save_transcript_async(
            text=merged["text"],
            speaker=speaker_label,
            start_time=merged["start_time"],
            end_time=merged["end_time"],
            confidence=merged["confidence"],
        )

    def _on_flush_timer(self) -> None:
        """Called when the merge timer expires — flush buffered fragments."""
        merged = self._merger.flush_remaining()
        if merged:
            self._save_merged(merged)

    async def handle_transcript_event(self, transcript_event: TranscriptEvent) -> None:
        """
        Handle transcript event from Transcribe.

        Fragments are buffered and merged into complete sentences before saving.
        """
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
            confidence = self._extract_confidence(alternative)

            if self._deduplicator.is_duplicate(
                result_id, transcript_text, result.start_time, result.end_time
            ):
                continue

            cleaned_text = self._preprocessor.preprocess(transcript_text, confidence)
            if cleaned_text is None:
                logger.debug(f"Filtered out: {transcript_text}")
                continue

            self._deduplicator.mark_processed(
                result_id, transcript_text, result.start_time, result.end_time
            )

            # Feed into sentence merger instead of saving directly
            merged = self._merger.add_fragment(
                text=cleaned_text,
                speaker=speaker,
                start_time=result.start_time,
                end_time=result.end_time,
                confidence=confidence,
                flush_callback=self._on_flush_timer,
            )

            if merged:
                self._save_merged(merged)

    def _extract_speaker(self, alternative) -> Optional[str]:
        """Extract speaker ID from alternative items."""
        if not hasattr(alternative, "items") or not alternative.items:
            return None

        for item in alternative.items:
            if hasattr(item, "speaker") and item.speaker is not None:
                return str(item.speaker)

        return None

    def _extract_confidence(self, alternative) -> Optional[float]:
        """Extract average confidence score from alternative items."""
        if not hasattr(alternative, "items") or not alternative.items:
            return None

        confidences = []
        for item in alternative.items:
            if hasattr(item, "confidence") and item.confidence is not None:
                try:
                    confidences.append(float(item.confidence))
                except (ValueError, TypeError):
                    pass

        if not confidences:
            return None

        return sum(confidences) / len(confidences)

    def flush_remaining(self) -> None:
        """Flush any buffered sentence fragments and pending async writes."""
        try:
            # Flush any remaining merged fragments first
            merged = self._merger.flush_remaining()
            if merged:
                self._save_merged(merged)

            loop = asyncio.get_event_loop()
            if loop.is_running():
                asyncio.create_task(self._dynamodb.flush_pending())
            else:
                loop.run_until_complete(self._dynamodb.flush_pending())
        except Exception as e:
            logger.error(f"Error flushing pending writes: {e}")


class TranscribeStreamingManager:
    """Manager for handling Transcribe streaming session."""

    def __init__(self, session_id: str, websocket_api_url: str = None):
        self._session_id = session_id
        self._websocket_api_url = websocket_api_url or WEBSOCKET_API_URL
        self._audio_capture = AudioCapture()
        self._broadcaster: Optional[WebSocketBroadcaster] = None
        self._dynamodb: Optional[DynamoDBHandler] = None
        self._is_running = False
        self._client: Optional[TranscribeStreamingClient] = None
        self._handler: Optional[MeetingTranscriptHandler] = None

    async def start(self) -> None:
        """Start transcription streaming."""
        logger.info(f"Starting transcription for session: {self._session_id}")
        logger.info(f"Speaker identification enabled: {ENABLE_SPEAKER_ID}")
        logger.info(f"Confidence threshold: {CONFIDENCE_THRESHOLD}")

        self._is_running = True

        # Initialize WebSocket broadcaster if endpoint is configured
        if self._websocket_api_url:
            logger.info(f"WebSocket broadcast enabled: {self._websocket_api_url[:50]}...")
            self._broadcaster = WebSocketBroadcaster(
                session_id=self._session_id,
                websocket_endpoint=self._websocket_api_url,
                region=AWS_REGION,
            )
            await self._broadcaster.initialize()
        else:
            logger.info("WebSocket broadcast disabled (no WEBSOCKET_API_URL)")

        # Initialize DynamoDB handler with broadcaster
        self._dynamodb = DynamoDBHandler(
            TRANSCRIPTS_TABLE,
            self._session_id,
            broadcaster=self._broadcaster,
        )

        await self._audio_capture.start()

        self._client = TranscribeStreamingClient(region=AWS_REGION)

        await self._stream_transcription()

    async def _stream_transcription(self) -> None:
        """Main streaming loop with timeout protection."""
        try:
            stream_params = {
                "language_code": TRANSCRIBE_LANGUAGE,
                "media_sample_rate_hz": SAMPLE_RATE,
                "media_encoding": "pcm",
            }

            if ENABLE_SPEAKER_ID:
                # Use speaker diarization (voice-based, not channel-based)
                # Note: Channel identification doesn't work for mixed audio streams
                stream_params["show_speaker_label"] = True

            if TRANSCRIBE_VOCABULARY_NAME:
                stream_params["vocabulary_name"] = TRANSCRIBE_VOCABULARY_NAME
                logger.info(f"Using custom vocabulary: {TRANSCRIBE_VOCABULARY_NAME}")

            logger.info(f"Starting Transcribe stream with params: {stream_params}")

            stream = await self._client.start_stream_transcription(**stream_params)

            self._handler = MeetingTranscriptHandler(
                stream.output_stream,
                self._dynamodb,
            )

            # Run with timeout to prevent infinite hang
            try:
                await asyncio.wait_for(
                    asyncio.gather(
                        self._send_audio(stream),
                        self._handler.handle_events(),
                    ),
                    timeout=7200  # 2 hour max meeting duration
                )
            except asyncio.TimeoutError:
                logger.warning("Transcription timed out after 2 hours")

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
        """Stop transcription and flush pending writes."""
        logger.info("Stopping transcription...")

        self._is_running = False

        if self._handler:
            await self._dynamodb.flush_pending()

        await self._audio_capture.stop()

        logger.info("Transcription stopped")

    @property
    def is_running(self) -> bool:
        return self._is_running
