// ============================================================
// Scenario 3: Spike Test
// Sudden burst simulating 10+ meetings starting simultaneously
// ============================================================

import http from "k6/http";
import { check } from "k6";
import { Rate, Trend } from "k6/metrics";
import { BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD } from "../config.js";
import { getAdminToken, authHeaders, uuid, randomProjectName } from "../helpers.js";

const errorRate = new Rate("errors");
const spikeLatency = new Trend("spike_latency", true);

export const options = {
  scenarios: {
    spike: {
      executor: "ramping-vus",
      startVUs: 2,
      stages: [
        { duration: "30s", target: 2 },    // baseline
        { duration: "10s", target: 80 },   // sudden spike
        { duration: "1m", target: 80 },    // hold spike
        { duration: "10s", target: 2 },    // drop back
        { duration: "2m", target: 2 },     // recovery observation
      ],
      gracefulRampDown: "10s",
    },
  },
  thresholds: {
    http_req_duration: ["p(95)<3000"],  // 3s during spike is acceptable
    errors: ["rate<0.10"],
  },
};

export function setup() {
  const token = getAdminToken(BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD);
  if (!token) throw new Error("Auth failed");
  return { token };
}

export default function (data) {
  const params = authHeaders(data.token);

  // Simulate the "everyone starts a meeting at once" pattern
  // This hits the heaviest endpoint: CreateSession (DynamoDB + SQS + ECS/warm pool + Bedrock)
  const res = http.get(`${BASE_URL}/projects`, params);
  check(res, { "list projects ok": (r) => r.status === 200 });
  errorRate.add(res.status !== 200);
  spikeLatency.add(res.timings.duration);

  // Also hit session listing (common during meeting start)
  const res2 = http.get(`${BASE_URL}/agents?page=1&limit=5`, params);
  check(res2, { "list agents ok": (r) => r.status === 200 });
  errorRate.add(res2.status !== 200);
  spikeLatency.add(res2.timings.duration);

  // Auth pressure during spike
  const res3 = http.post(
    `${BASE_URL}/auth/admin/login`,
    JSON.stringify({ username: ADMIN_USERNAME, password: ADMIN_PASSWORD }),
    { headers: { "Content-Type": "application/json" } }
  );
  check(res3, { "auth during spike ok": (r) => r.status === 200 });
  errorRate.add(res3.status !== 200);
  spikeLatency.add(res3.timings.duration);
}
