// ============================================================
// AXRAIL Load Testing — Shared Configuration
// ============================================================

// Update these values before running tests
export const BASE_URL = __ENV.BASE_URL || "https://YOUR-API-ID.execute-api.ap-southeast-1.amazonaws.com/dev";
export const WS_URL = __ENV.WS_URL || "wss://YOUR-WS-API-ID.execute-api.ap-southeast-1.amazonaws.com/production";

// Admin credentials (used to obtain JWT tokens)
export const ADMIN_USERNAME = __ENV.ADMIN_USERNAME || "admin@example.com";
export const ADMIN_PASSWORD = __ENV.ADMIN_PASSWORD || "ChangeMe123!";

// Test data IDs (populated during setup or from env)
export const TEST_PROJECT_ID = __ENV.TEST_PROJECT_ID || "";
export const TEST_SESSION_ID = __ENV.TEST_SESSION_ID || "";

// SLA Targets
export const SLA = {
  p95_latency_ms: 500,
  p99_latency_ms: 1000,
  error_rate: 0.01,       // 1%
  min_throughput_rps: 50,
};

// Think time range (seconds) — simulates real user pauses
export const THINK_TIME_MIN = 1;
export const THINK_TIME_MAX = 3;
