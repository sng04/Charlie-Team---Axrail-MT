// ============================================================
// Scenario 4: WebSocket Load Test
// Simulates concurrent meeting sessions with live transcript processing
// ============================================================

import ws from "k6/ws";
import { check, sleep } from "k6";
import { Rate, Trend, Counter } from "k6/metrics";
import { WS_URL, TEST_SESSION_ID } from "../config.js";
import { generateTranscriptLines, uuid } from "../helpers.js";

const wsErrors = new Rate("ws_errors");
const wsLatency = new Trend("ws_message_latency", true);
const wsMessages = new Counter("ws_messages_sent");

export const options = {
  scenarios: {
    websocket_sessions: {
      executor: "ramping-vus",
      startVUs: 0,
      stages: [
        { duration: "1m", target: 10 },  // 10 concurrent WS connections
        { duration: "5m", target: 10 },  // steady state
        { duration: "1m", target: 30 },  // scale to 30 connections
        { duration: "3m", target: 30 },  // hold
        { duration: "1m", target: 0 },   // ramp down
      ],
    },
  },
  thresholds: {
    ws_errors: ["rate<0.05"],
    ws_message_latency: ["p(95)<5000"],  // 5s for AI-powered responses
  },
};

export default function () {
  const sessionId = TEST_SESSION_ID || uuid();
  const url = `${WS_URL}?session_id=${sessionId}`;

  const res = ws.connect(url, {}, function (socket) {
    socket.on("open", () => {
      // --- Phase 1: Send a chat message ---
      const chatMsg = JSON.stringify({
        action: "sendMessage",
        session_id: sessionId,
        message: "What topics should we cover in this meeting?",
      });

      const start1 = Date.now();
      socket.send(chatMsg);
      wsMessages.add(1);

      socket.on("message", (msg) => {
        wsLatency.add(Date.now() - start1);
        try {
          const data = JSON.parse(msg);
          check(data, {
            "has type field": (d) => d.type !== undefined,
            "not error": (d) => d.type !== "error",
          });
          wsErrors.add(data.type === "error");
        } catch (_) {
          wsErrors.add(1);
        }
      });

      sleep(3);

      // --- Phase 2: Process transcript lines (simulates live meeting) ---
      const lines = generateTranscriptLines(5);
      const transcriptMsg = JSON.stringify({
        action: "processTranscript",
        session_id: sessionId,
        lines: lines,
      });

      socket.send(transcriptMsg);
      wsMessages.add(1);

      sleep(5);

      // --- Phase 3: Detect a question ---
      const detectMsg = JSON.stringify({
        action: "detectQuestion",
        session_id: sessionId,
        question: "What is the pricing model for the enterprise tier?",
      });

      socket.send(detectMsg);
      wsMessages.add(1);

      sleep(5);

      // --- Phase 4: Analyze gaps ---
      const gapMsg = JSON.stringify({
        action: "analyzeGaps",
        session_id: sessionId,
      });

      socket.send(gapMsg);
      wsMessages.add(1);

      // Hold connection open to simulate active meeting
      sleep(10);
    });

    socket.on("error", (e) => {
      wsErrors.add(1);
      console.error(`WebSocket error: ${e.error()}`);
    });

    socket.setTimeout(() => {
      socket.close();
    }, 30000);
  });

  check(res, { "ws status 101": (r) => r && r.status === 101 });
}
