---
inclusion: manual
name: frontend-live-transcript-integration
description: Frontend integration guide for Live Transcript feature. Covers WebSocket real-time streaming, REST API for historical transcripts, message formats, and page structure for displaying meeting transcripts.
---

# Frontend Live Transcript Integration Guide

## Overview

Panduan integrasi frontend untuk fitur Live Transcript. Fitur ini memiliki dua mode:

1. **Real-Time (WebSocket)** — Transcript ditampilkan langsung saat bot menangkap audio di meeting
2. **Historical (REST API)** — Fetch transcript yang sudah tersimpan di DynamoDB untuk session yang sudah selesai

Data yang diterima via WebSocket 100% identik dengan yang tersimpan di DynamoDB — tidak perlu transformasi tambahan.

Key concepts:
- **Live Transcript**: Real-time transcript line yang di-push dari bot via WebSocket
- **Historical Transcript**: Transcript yang sudah tersimpan, di-fetch via REST API
- **Session Scope**: Setiap WebSocket connection di-scope ke satu session via `session_id` query param
- **Partial vs Final**: Transcript line bisa `is_partial: true` (masih berubah) atau `false` (final)

---

## Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  Meeting Bot │────▶│   Amazon     │────▶│  Transcribe  │
│  (ECS Task)  │     │  Transcribe  │     │   Handler    │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                  │
                                          ┌───────┴───────┐
                                          │               │
                                          ▼               ▼
                                   ┌────────────┐  ┌─────────────┐
                                   │  DynamoDB   │  │  WebSocket  │
                                   │   Write     │  │  Broadcast  │
                                   └────────────┘  └──────┬──────┘
                                          │               │
                                          ▼               ▼
                                   ┌────────────┐  ┌─────────────┐
                                   │ Transcripts │  │  Frontend   │
                                   │   Table     │  │  (Client)   │
                                   └────────────┘  └─────────────┘
```

Flow:
1. Bot capture audio → Amazon Transcribe → TranscribeHandler
2. TranscribeHandler build transcript item, lalu **parallel**:
   - Simpan ke DynamoDB (TranscriptsTable)
   - Broadcast ke WebSocket client
3. Frontend terima real-time via WebSocket
4. Frontend juga bisa fetch historical via REST API

---

## WebSocket Connection

### URL Format

```
wss://{api-id}.execute-api.{region}.amazonaws.com/production?session_id={sessionId}
```

**Penting:**
- `session_id` query param **wajib** — menentukan session mana yang akan di-subscribe
- WebSocket URL **tidak perlu dikirim dari frontend ke backend** — sudah dikonfigurasi server-side via environment variable
- Setiap client hanya menerima transcript untuk session yang di-subscribe

### Connect

```javascript
const WEBSOCKET_URL = process.env.REACT_APP_WEBSOCKET_URL; 
// e.g., "wss://abc123.execute-api.ap-southeast-1.amazonaws.com/production"

function connectTranscriptWebSocket(sessionId) {
  const ws = new WebSocket(`${WEBSOCKET_URL}?session_id=${sessionId}`);
  
  ws.onopen = () => {
    console.log('WebSocket connected for session:', sessionId);
  };
  
  ws.onclose = (event) => {
    console.log('WebSocket closed:', event.code, event.reason);
  };
  
  ws.onerror = (error) => {
    console.error('WebSocket error:', error);
  };
  
  return ws;
}
```

### Disconnect

```javascript
function disconnectWebSocket(ws) {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.close(1000, 'Client disconnecting');
  }
}
```

---

## WebSocket Message Format

### Incoming: transcriptLine

Setiap kali bot menangkap transcript baru, client menerima:

```json
{
  "type": "transcriptLine",
  "line": {
    "session_id": "abc123",
    "transcript_id": "550e8400-e29b-41d4-a716-446655440000",
    "text": "Hello, welcome to the meeting.",
    "speaker": "spk_0",
    "start_time": "10.25",
    "end_time": "12.50",
    "confidence": "0.923",
    "timestamp": "2025-01-15T10:30:15.123Z",
    "is_partial": false,
    "created_at": "2025-01-15T10:30:15.123Z"
  }
}
```

### Transcript Line Fields

| Field | Type | Description |
|-------|------|-------------|
| `session_id` | string | Session ID |
| `transcript_id` | string | Unique ID untuk transcript line |
| `text` | string | Teks transcript |
| `speaker` | string | Speaker label (`spk_0`, `spk_1`, dst.) |
| `start_time` | string | Waktu mulai dalam detik (dari awal meeting) |
| `end_time` | string | Waktu selesai dalam detik |
| `confidence` | string | Confidence score (0-1) |
| `timestamp` | string | ISO 8601 timestamp |
| `is_partial` | boolean | `true` = masih berubah, `false` = final |
| `created_at` | string | ISO 8601 creation timestamp |

### Handling Partial vs Final Lines

```javascript
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  if (data.type === 'transcriptLine') {
    const line = data.line;
    
    if (line.is_partial) {
      // Update existing partial line (replace text in-place)
      updatePartialLine(line);
    } else {
      // Final line — add to transcript list permanently
      addFinalLine(line);
    }
  }
};
```

**Partial line behavior:**
- Partial line = teks yang masih berubah saat speaker masih berbicara
- Saat partial baru datang, **replace** partial sebelumnya dari speaker yang sama
- Saat final datang (`is_partial: false`), commit sebagai line permanen dan hapus partial

---

## REST API: Historical Transcripts

### GET /sessions/{sessionId}/transcripts

Fetch transcript yang sudah tersimpan di DynamoDB. Gunakan untuk:
- Load transcript saat pertama kali buka halaman session
- Session yang sudah selesai (historical view)
- Fallback jika WebSocket disconnect

**Headers:**
```
Authorization: Bearer {access_token}
```

**Query Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `limit` | integer | 50 | Max items per page (max: 100) |
| `lastKey` | string | - | Pagination key dari response sebelumnya |

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Transcripts retrieved successfully",
  "data": {
    "session_id": "abc123",
    "items": [
      {
        "session_id": "abc123",
        "transcript_id": "550e8400-e29b-41d4-a716-446655440000",
        "text": "Hello, welcome to the meeting.",
        "speaker": "spk_0",
        "start_time": "10.25",
        "end_time": "12.50",
        "confidence": "0.923",
        "timestamp": "2025-01-15T10:30:15.123Z",
        "is_partial": false,
        "created_at": "2025-01-15T10:30:15.123Z"
      }
    ],
    "count": 1,
    "lastKey": "2025-01-15T10:30:15.123Z"
  }
}
```

**Pagination:**
```javascript
async function fetchAllTranscripts(sessionId) {
  let allItems = [];
  let lastKey = null;
  
  do {
    const params = new URLSearchParams({ limit: '100' });
    if (lastKey) params.set('lastKey', lastKey);
    
    const response = await apiCall(
      'GET', 
      `/sessions/${sessionId}/transcripts?${params}`
    );
    
    allItems = [...allItems, ...response.data.items];
    lastKey = response.data.lastKey || null;
  } while (lastKey);
  
  return allItems;
}
```

**Error Responses:**

| Code | Meaning | Action |
|------|---------|--------|
| 400 | Session ID missing | Validasi sebelum request |
| 403 | User tidak punya akses ke session | Tampilkan access denied |
| 404 | Session tidak ditemukan | Tampilkan not found |
| 500 | Server error | Tampilkan generic error |

**Authorization:**
- Admin: bisa akses transcript session manapun
- User: hanya bisa akses transcript dari session di project yang di-assign

---

## Frontend Implementation

### 1. Transcript State Management

```javascript
// State structure
const [transcriptLines, setTranscriptLines] = useState([]);  // Final lines
const [partialLine, setPartialLine] = useState(null);         // Current partial
const [isLive, setIsLive] = useState(false);                  // WebSocket connected
const [isLoading, setIsLoading] = useState(true);             // Initial load
const wsRef = useRef(null);
```

### 2. Load Historical + Connect WebSocket

```javascript
async function initializeTranscriptView(sessionId, sessionStatus) {
  setIsLoading(true);
  
  try {
    // Step 1: Fetch historical transcripts
    const historical = await fetchAllTranscripts(sessionId);
    setTranscriptLines(historical);
    
    // Step 2: Connect WebSocket if session is active
    if (sessionStatus === 'active' || sessionStatus === 'in_meeting') {
      connectLiveTranscript(sessionId);
    }
  } catch (error) {
    console.error('Failed to load transcripts:', error);
    showError('Failed to load transcripts');
  } finally {
    setIsLoading(false);
  }
}
```

### 3. WebSocket Message Handler

```javascript
function connectLiveTranscript(sessionId) {
  const ws = new WebSocket(`${WEBSOCKET_URL}?session_id=${sessionId}`);
  wsRef.current = ws;
  
  ws.onopen = () => {
    setIsLive(true);
  };
  
  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    
    if (data.type === 'transcriptLine') {
      const line = data.line;
      
      if (line.is_partial) {
        // Replace current partial line
        setPartialLine(line);
      } else {
        // Add final line, clear partial
        setPartialLine(null);
        setTranscriptLines(prev => {
          // Deduplicate by transcript_id (in case historical already has it)
          const exists = prev.some(l => l.transcript_id === line.transcript_id);
          if (exists) return prev;
          return [...prev, line];
        });
      }
    }
  };
  
  ws.onclose = () => {
    setIsLive(false);
    setPartialLine(null);
  };
  
  ws.onerror = (error) => {
    console.error('WebSocket error:', error);
  };
  
  return ws;
}
```

### 4. Auto-Reconnect Logic

```javascript
function useTranscriptWebSocket(sessionId, sessionStatus) {
  const wsRef = useRef(null);
  const reconnectAttempts = useRef(0);
  const maxReconnectAttempts = 5;
  const reconnectTimeoutRef = useRef(null);
  
  const connect = useCallback(() => {
    if (!sessionId || sessionStatus !== 'in_meeting') return;
    
    const ws = new WebSocket(`${WEBSOCKET_URL}?session_id=${sessionId}`);
    wsRef.current = ws;
    
    ws.onopen = () => {
      reconnectAttempts.current = 0;
      setIsLive(true);
    };
    
    ws.onmessage = (event) => {
      // ... handle message (same as above)
    };
    
    ws.onclose = (event) => {
      setIsLive(false);
      
      // Auto-reconnect with exponential backoff
      if (event.code !== 1000 && reconnectAttempts.current < maxReconnectAttempts) {
        const delay = Math.min(1000 * Math.pow(2, reconnectAttempts.current), 30000);
        reconnectAttempts.current++;
        
        console.log(`Reconnecting in ${delay}ms (attempt ${reconnectAttempts.current})`);
        reconnectTimeoutRef.current = setTimeout(connect, delay);
      }
    };
  }, [sessionId, sessionStatus]);
  
  useEffect(() => {
    connect();
    
    return () => {
      // Cleanup on unmount
      if (reconnectTimeoutRef.current) {
        clearTimeout(reconnectTimeoutRef.current);
      }
      if (wsRef.current) {
        wsRef.current.close(1000, 'Component unmounting');
      }
    };
  }, [connect]);
  
  return { wsRef, isLive };
}
```

### 5. Deduplication: Merge Historical + Live

Saat reconnect atau initial load, mungkin ada overlap antara historical data dan live data. Gunakan `transcript_id` sebagai unique key:

```javascript
function mergeTranscripts(historical, liveLines) {
  const merged = new Map();
  
  // Historical first
  historical.forEach(line => {
    merged.set(line.transcript_id, line);
  });
  
  // Live overwrites (same data, but ensures no duplicates)
  liveLines.forEach(line => {
    merged.set(line.transcript_id, line);
  });
  
  // Sort by timestamp
  return Array.from(merged.values()).sort(
    (a, b) => new Date(a.timestamp) - new Date(b.timestamp)
  );
}
```

---

## Frontend Pages

### 1. Session Transcript Page (`/sessions/{sessionId}/transcript`)

**Components:**
- Session info header (session name, status, meeting URL)
- Live indicator badge (green dot when WebSocket connected)
- Transcript list (scrollable, auto-scroll to bottom for live)
- Speaker labels with color coding
- Partial line indicator (typing animation)

**Layout:**
```html
<div class="transcript-page">
  <!-- Header -->
  <div class="transcript-header">
    <h2>Weekly Team Standup</h2>
    <div class="session-meta">
      <span class="status-badge active">In Meeting</span>
      <span class="live-indicator" v-if="isLive">
        <span class="live-dot"></span> LIVE
      </span>
    </div>
  </div>
  
  <!-- Transcript List -->
  <div class="transcript-list" ref="transcriptContainer">
    <!-- Historical + Live lines -->
    <div v-for="line in transcriptLines" :key="line.transcript_id" class="transcript-line">
      <div class="line-meta">
        <span class="speaker" :style="{ color: getSpeakerColor(line.speaker) }">
          {{ formatSpeaker(line.speaker) }}
        </span>
        <span class="timestamp">{{ formatTime(line.start_time) }}</span>
      </div>
      <div class="line-text">{{ line.text }}</div>
    </div>
    
    <!-- Current partial line (typing indicator) -->
    <div v-if="partialLine" class="transcript-line partial">
      <div class="line-meta">
        <span class="speaker" :style="{ color: getSpeakerColor(partialLine.speaker) }">
          {{ formatSpeaker(partialLine.speaker) }}
        </span>
      </div>
      <div class="line-text">
        {{ partialLine.text }}
        <span class="typing-indicator">...</span>
      </div>
    </div>
  </div>
  
  <!-- Empty state -->
  <div v-if="!isLoading && transcriptLines.length === 0" class="empty-state">
    <p>No transcript yet. Waiting for meeting to start...</p>
  </div>
</div>
```

### 2. Speaker Color Mapping

```javascript
const SPEAKER_COLORS = [
  '#3B82F6', // blue
  '#10B981', // green
  '#F59E0B', // amber
  '#EF4444', // red
  '#8B5CF6', // purple
  '#EC4899', // pink
  '#06B6D4', // cyan
  '#F97316', // orange
];

function getSpeakerColor(speaker) {
  // Extract number from "spk_0", "spk_1", etc.
  const index = parseInt(speaker.replace('spk_', ''), 10) || 0;
  return SPEAKER_COLORS[index % SPEAKER_COLORS.length];
}

function formatSpeaker(speaker) {
  const index = parseInt(speaker.replace('spk_', ''), 10) || 0;
  return `Speaker ${index + 1}`;
}
```

### 3. Auto-Scroll Behavior

```javascript
const transcriptContainerRef = useRef(null);
const isUserScrolledUp = useRef(false);

// Detect if user scrolled up (disable auto-scroll)
function handleScroll() {
  const container = transcriptContainerRef.current;
  if (!container) return;
  
  const { scrollTop, scrollHeight, clientHeight } = container;
  const isAtBottom = scrollHeight - scrollTop - clientHeight < 50;
  isUserScrolledUp.current = !isAtBottom;
}

// Auto-scroll to bottom when new line arrives (unless user scrolled up)
useEffect(() => {
  if (!isUserScrolledUp.current) {
    const container = transcriptContainerRef.current;
    if (container) {
      container.scrollTop = container.scrollHeight;
    }
  }
}, [transcriptLines, partialLine]);
```

### 4. Time Formatting

```javascript
// Format seconds to MM:SS
function formatTime(startTimeSeconds) {
  const totalSeconds = parseFloat(startTimeSeconds);
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = Math.floor(totalSeconds % 60);
  return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

// Format ISO timestamp to readable time
function formatTimestamp(isoString) {
  return new Date(isoString).toLocaleTimeString('id-ID', {
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  });
}
```

---

## Styling

```css
/* Live indicator */
.live-indicator {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: #10B981;
  font-weight: 600;
  font-size: 12px;
}

.live-dot {
  width: 8px;
  height: 8px;
  background: #10B981;
  border-radius: 50%;
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}

/* Transcript list */
.transcript-list {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

/* Transcript line */
.transcript-line {
  padding: 8px 12px;
  border-radius: 8px;
  background: #F9FAFB;
}

.transcript-line.partial {
  opacity: 0.7;
  background: #F3F4F6;
}

.line-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.speaker {
  font-weight: 600;
  font-size: 13px;
}

.timestamp {
  font-size: 11px;
  color: #9CA3AF;
}

.line-text {
  font-size: 14px;
  line-height: 1.5;
  color: #1F2937;
}

.typing-indicator {
  animation: blink 1s infinite;
  color: #9CA3AF;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

/* Empty state */
.empty-state {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
  color: #9CA3AF;
}
```

---

## Complete Flow: Session Transcript Page

```
┌─────────────────────────────────────────────────────────┐
│ 1. User buka halaman /sessions/{sessionId}/transcript   │
│                                                         │
│ 2. Fetch session detail (GET /sessions/{sessionId})     │
│    → Dapat session status                               │
│                                                         │
│ 3. Fetch historical transcripts                         │
│    GET /sessions/{sessionId}/transcripts?limit=100      │
│    → Paginate sampai semua data ter-load                │
│    → Tampilkan di transcript list                       │
│                                                         │
│ 4. Jika session status = "active" / "in_meeting":       │
│    → Connect WebSocket dengan session_id                │
│    → Tampilkan LIVE badge                               │
│    → Handle incoming transcriptLine messages             │
│    → Deduplicate dengan historical data                 │
│    → Auto-scroll ke bawah                               │
│                                                         │
│ 5. Jika session sudah selesai:                          │
│    → Hanya tampilkan historical data                    │
│    → Tidak perlu connect WebSocket                      │
│                                                         │
│ 6. Jika WebSocket disconnect:                           │
│    → Auto-reconnect dengan exponential backoff          │
│    → Fetch missing transcripts via REST saat reconnect  │
│    → Merge dan deduplicate                              │
└─────────────────────────────────────────────────────────┘
```

---

## Reconnect + Gap Fill Strategy

Saat WebSocket reconnect setelah disconnect, mungkin ada transcript yang terlewat. Strategy:

```javascript
async function handleReconnect(sessionId, lastTimestamp) {
  // Fetch transcripts yang mungkin terlewat saat disconnect
  const params = new URLSearchParams({ limit: '100' });
  if (lastTimestamp) {
    params.set('lastKey', lastTimestamp);
  }
  
  const response = await apiCall(
    'GET',
    `/sessions/${sessionId}/transcripts?${params}`
  );
  
  // Merge dengan existing lines (deduplicate by transcript_id)
  const newLines = response.data.items;
  setTranscriptLines(prev => {
    const existingIds = new Set(prev.map(l => l.transcript_id));
    const uniqueNew = newLines.filter(l => !existingIds.has(l.transcript_id));
    
    return [...prev, ...uniqueNew].sort(
      (a, b) => new Date(a.timestamp) - new Date(b.timestamp)
    );
  });
}
```

---

## Error Handling

### WebSocket Errors

| Scenario | Action |
|----------|--------|
| Connection refused | Tampilkan "Unable to connect to live stream" |
| Connection dropped | Auto-reconnect + gap fill |
| Max reconnect exceeded | Tampilkan "Live connection lost. Refresh to retry." + fallback ke polling REST |
| Invalid session_id | Server close connection, tampilkan error |

### REST API Errors

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Render transcript data |
| 400 | Bad Request | Validasi session ID |
| 403 | Forbidden | Tampilkan "You don't have access to this session" |
| 404 | Not Found | Tampilkan "Session not found" |
| 500 | Server Error | Tampilkan generic error, retry button |

### Error Handling Example

```javascript
async function apiCall(method, url, body = null) {
  try {
    const options = {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
      },
    };
    
    if (body) {
      options.body = JSON.stringify(body);
    }
    
    const response = await fetch(`${API_BASE_URL}${url}`, options);
    const data = await response.json();
    
    if (response.status === 401) {
      localStorage.clear();
      window.location.href = '/login';
      return;
    }
    
    if (!data.status) {
      throw new Error(data.message);
    }
    
    return data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
}
```

---

## Summary

### Data Sources:
1. **WebSocket** (`wss://...?session_id={id}`) — Real-time `transcriptLine` messages dari bot
2. **REST API** (`GET /sessions/{id}/transcripts`) — Historical transcript dari DynamoDB

### Key Points:
- Data WebSocket dan DynamoDB **100% identik** — tidak perlu transformasi
- WebSocket URL **tidak perlu dikirim dari FE ke backend** — dikonfigurasi server-side
- Gunakan `transcript_id` untuk deduplication antara live dan historical
- Handle `is_partial` untuk typing indicator (replace in-place, bukan append)
- Auto-reconnect dengan exponential backoff saat disconnect
- Gap fill via REST API saat reconnect untuk data yang terlewat

### Pages to Build:
1. Session Transcript Page (`/sessions/{sessionId}/transcript`) — Live + Historical view
