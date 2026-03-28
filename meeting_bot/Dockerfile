# ==============================================================================
# Meeting Bot Dockerfile
# ==============================================================================
# Base image dengan Python dan dependencies untuk Playwright/Firefox
# Build timestamp: 2026-03-18T16:30:00Z (force rebuild)
# ==============================================================================

FROM --platform=linux/amd64 mcr.microsoft.com/playwright/python:v1.41.0-jammy

# ==============================================================================
# Set working directory
# ==============================================================================
WORKDIR /app

# ==============================================================================
# Install Xvfb for virtual display and PulseAudio for audio capture
# ==============================================================================
RUN apt-get update && apt-get install -y \
    xvfb \
    pulseaudio \
    pulseaudio-utils \
    dbus \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /var/run/dbus \
    && dbus-uuidgen > /var/lib/dbus/machine-id

# ==============================================================================
# Copy requirements dan install dependencies
# ==============================================================================
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ==============================================================================
# Install Playwright browsers
# ==============================================================================
RUN playwright install chromium firefox
RUN playwright install-deps chromium firefox

# ==============================================================================
# Copy application code
# ==============================================================================
COPY config.py .
COPY browser_manager.py .
COPY audio_capture.py .
COPY transcribe_handler.py .
COPY websocket_broadcaster.py .
COPY meeting_orchestrator.py .
COPY entrypoint.sh .
COPY pulse-client.conf /etc/pulse/client.conf
RUN chmod +x entrypoint.sh

# ==============================================================================
# Environment variables (defaults, override at runtime)
# ==============================================================================
ENV BROWSER_HEADLESS=true
ENV BROWSER_TIMEOUT=30000
ENV BROWSER_TYPE=firefox
ENV KEEP_ALIVE_INTERVAL=30
ENV LOG_LEVEL=INFO
ENV DISPLAY=:99
ENV ENABLE_TRANSCRIPTION=true
ENV TRANSCRIBE_LANGUAGE=en-US
ENV AWS_REGION=ap-southeast-1
ENV AUDIO_SOURCE=auto_null.monitor

# ==============================================================================
# Health check
# ==============================================================================
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "print('healthy')" || exit 1

# ==============================================================================
# Run the agent with Xvfb
# ==============================================================================
CMD ["./entrypoint.sh"]
