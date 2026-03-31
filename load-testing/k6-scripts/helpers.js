// ============================================================
// AXRAIL Load Testing — Helper Functions
// ============================================================

import http from "k6/http";
import { sleep } from "k6";
import { THINK_TIME_MIN, THINK_TIME_MAX } from "./config.js";

/**
 * Authenticate as admin and return JWT access token.
 */
export function getAdminToken(baseUrl, username, password) {
  const res = http.post(
    `${baseUrl}/auth/admin/login`,
    JSON.stringify({ username, password }),
    { headers: { "Content-Type": "application/json" } }
  );

  if (res.status !== 200) {
    console.error(`Auth failed: ${res.status} ${res.body}`);
    return null;
  }

  const body = JSON.parse(res.body);
  return body.data?.access_token || body.data?.AccessToken || null;
}

/**
 * Build standard headers with auth token.
 */
export function authHeaders(token) {
  return {
    headers: {
      "Content-Type": "application/json",
      Authorization: token,
    },
  };
}

/**
 * Random think time between requests.
 */
export function thinkTime() {
  sleep(THINK_TIME_MIN + Math.random() * (THINK_TIME_MAX - THINK_TIME_MIN));
}

/**
 * Generate a random UUID v4.
 */
export function uuid() {
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (c) => {
    const r = (Math.random() * 16) | 0;
    const v = c === "x" ? r : (r & 0x3) | 0x8;
    return v.toString(16);
  });
}

/**
 * Pick a random element from an array.
 */
export function randomItem(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

/**
 * Generate random meeting link.
 */
export function randomMeetingLink() {
  const code = Math.random().toString(36).substring(2, 12);
  return `https://meet.google.com/${code.slice(0, 3)}-${code.slice(3, 7)}-${code.slice(7)}`;
}

/**
 * Generate random project name.
 */
export function randomProjectName() {
  const adjectives = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta"];
  const nouns = ["Phoenix", "Titan", "Atlas", "Nova", "Orion", "Vega"];
  return `${randomItem(adjectives)} ${randomItem(nouns)} ${Date.now() % 10000}`;
}

/**
 * Generate random transcript lines for processTranscript testing.
 */
export function generateTranscriptLines(count) {
  const speakers = ["spk_0", "spk_1"];
  const phrases = [
    "What is the pricing model for the enterprise tier?",
    "Our enterprise tier starts at two hundred dollars per seat.",
    "Can you explain the integration with Salesforce?",
    "We support native Salesforce integration via REST API.",
    "What security certifications do you have?",
    "We hold SOC 2 Type II and ISO 27001 certifications.",
    "How does the onboarding process work?",
    "The onboarding takes approximately two weeks.",
    "What is the expected uptime SLA?",
    "We guarantee 99.9% uptime for enterprise customers.",
  ];

  const lines = [];
  let startTime = 10.0;

  for (let i = 0; i < count; i++) {
    const duration = 2 + Math.random() * 4;
    lines.push({
      speaker: speakers[i % 2],
      text: phrases[i % phrases.length],
      start_time: startTime.toFixed(2),
      end_time: (startTime + duration).toFixed(2),
      confidence: (0.8 + Math.random() * 0.2).toFixed(3),
      is_partial: false,
    });
    startTime += duration + 0.5;
  }

  return lines;
}
