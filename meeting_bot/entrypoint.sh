#!/bin/bash
# ==============================================================================
# Entrypoint script - Start Xvfb, PulseAudio, and run the meeting bot
# ==============================================================================

echo "=========================================="
echo "Starting Meeting Bot Container"
echo "=========================================="

# Start Xvfb (virtual display)
echo "[1/5] Starting Xvfb..."
Xvfb :99 -screen 0 1280x720x24 &
XVFB_PID=$!
sleep 2

# Verify Xvfb is running
if ! kill -0 $XVFB_PID 2>/dev/null; then
    echo "ERROR: Xvfb failed to start"
    exit 1
fi
echo "Xvfb started with PID: $XVFB_PID"

# Start D-Bus (required for PulseAudio)
echo "[2/5] Starting D-Bus..."
mkdir -p /var/run/dbus
dbus-daemon --system --fork 2>/dev/null || true
sleep 1

# Start PulseAudio
echo "[3/5] Starting PulseAudio..."

# Clean up any stale files
rm -rf /tmp/pulse-* /var/run/pulse /root/.config/pulse /root/.pulse* 2>/dev/null || true
mkdir -p /var/run/pulse
chmod 777 /var/run/pulse

# Create PulseAudio system config with explicit socket path
cat > /etc/pulse/system.pa << 'EOF'
load-module module-null-sink sink_name=auto_null sink_properties=device.description="Virtual_Sink"
load-module module-native-protocol-unix auth-anonymous=1 socket=/var/run/pulse/native
set-default-sink auto_null
EOF

# Set environment for PulseAudio socket
export PULSE_SERVER=unix:/var/run/pulse/native
export PULSE_RUNTIME_PATH=/var/run/pulse

# Start PulseAudio in system mode with explicit config
echo "Starting PulseAudio daemon..."
pulseaudio --system --disallow-exit -F /etc/pulse/system.pa &
PA_PID=$!
sleep 3

# Fix socket permissions
chmod 777 /var/run/pulse/native 2>/dev/null || true

# Check if PulseAudio is running
echo "[4/5] Configuring audio..."
for i in {1..10}; do
    if pactl info > /dev/null 2>&1; then
        echo "PulseAudio connected (attempt $i)"
        break
    fi
    echo "Waiting for PulseAudio... (attempt $i)"
    chmod 777 /var/run/pulse/native 2>/dev/null || true
    sleep 1
done

if pactl info > /dev/null 2>&1; then
    echo ""
    echo "Audio Sinks:"
    pactl list short sinks
    echo ""
    echo "Audio Sources (for capture):"
    pactl list short sources
    echo ""
    
    if pactl list short sources | grep -q "auto_null.monitor"; then
        echo "✓ Monitor source 'auto_null.monitor' is available for capture"
    else
        echo "Creating virtual sink..."
        pactl load-module module-null-sink sink_name=auto_null 2>/dev/null || true
        pactl list short sources
    fi
else
    echo "WARNING: PulseAudio not responding"
    echo "PulseAudio PID: $PA_PID"
    ls -la /var/run/pulse/ 2>/dev/null || true
fi

echo "[5/5] Setup complete"

echo "=========================================="
echo "Environment:"
echo "  SESSION_ID: ${SESSION_ID}"
echo "  PROJECT_ID: ${PROJECT_ID}"
echo "  MEETING_URL: ${MEETING_URL}"
echo "  ENABLE_TRANSCRIPTION: ${ENABLE_TRANSCRIPTION}"
echo "  TRANSCRIBE_LANGUAGE: ${TRANSCRIBE_LANGUAGE}"
echo "  AWS_REGION: ${AWS_REGION}"
echo "  ENVIRONMENT: ${ENVIRONMENT}"
echo "  BROWSER_TYPE: ${BROWSER_TYPE:-firefox}"
echo "  PULSE_SERVER: ${PULSE_SERVER}"
echo "=========================================="

sleep 1

# Run the meeting orchestrator
echo "Starting Meeting Orchestrator..."
exec python meeting_orchestrator.py
