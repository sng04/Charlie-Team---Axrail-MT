// ============================================================
// Scenario 2: Stress Test
// Push beyond expected capacity to find breaking points
// ============================================================

import http from "k6/http";
import { check, group } from "k6";
import { Rate, Trend } from "k6/metrics";
import { BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD } from "../config.js";
import { getAdminToken, authHeaders, thinkTime, randomProjectName, uuid } from "../helpers.js";

const errorRate = new Rate("errors");
const latencyTrend = new Trend("request_latency", true);

export const options = {
  scenarios: {
    stress: {
      executor: "ramping-vus",
      startVUs: 0,
      stages: [
        { duration: "2m", target: 20 },   // warm up
        { duration: "3m", target: 50 },   // push to 2.5x normal
        { duration: "3m", target: 100 },  // push to 5x normal
        { duration: "3m", target: 150 },  // push to 7.5x — expect degradation
        { duration: "2m", target: 200 },  // extreme — find breaking point
        { duration: "2m", target: 0 },    // recovery
      ],
      gracefulRampDown: "30s",
    },
  },
  thresholds: {
    // Relaxed thresholds — we expect failures at high load
    http_req_duration: ["p(95)<2000"],
    errors: ["rate<0.20"],  // up to 20% errors acceptable during stress
  },
};

export function setup() {
  const token = getAdminToken(BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD);
  if (!token) throw new Error("Auth failed");
  return { token };
}

export default function (data) {
  const params = authHeaders(data.token);

  // Mix of read-heavy and write operations
  const roll = Math.random();

  if (roll < 0.4) {
    // 40% — List operations (read-heavy)
    group("Read Operations", () => {
      const endpoints = [
        "/projects",
        "/users",
        "/agents?page=1&limit=20",
        "/personalities?page=1&limit=20",
        "/bot-credentials",
      ];
      const endpoint = endpoints[Math.floor(Math.random() * endpoints.length)];
      const res = http.get(`${BASE_URL}${endpoint}`, params);
      check(res, { "read ok": (r) => r.status === 200 });
      errorRate.add(res.status !== 200);
      latencyTrend.add(res.timings.duration);
    });
  } else if (roll < 0.7) {
    // 30% — Auth operations (Cognito pressure)
    group("Auth Pressure", () => {
      const res = http.post(
        `${BASE_URL}/auth/admin/login`,
        JSON.stringify({ username: ADMIN_USERNAME, password: ADMIN_PASSWORD }),
        { headers: { "Content-Type": "application/json" } }
      );
      check(res, { "auth ok": (r) => r.status === 200 });
      errorRate.add(res.status !== 200);
      latencyTrend.add(res.timings.duration);
    });
  } else {
    // 30% — Write operations (DynamoDB pressure)
    group("Write Operations", () => {
      const res = http.post(
        `${BASE_URL}/projects`,
        JSON.stringify({
          name: randomProjectName(),
          email: `stress-${uuid().slice(0, 8)}@example.com`,
          description: "Stress test project",
        }),
        params
      );
      check(res, { "write ok": (r) => r.status === 200 });
      errorRate.add(res.status !== 200);
      latencyTrend.add(res.timings.duration);

      // Cleanup if created
      if (res.status === 200) {
        try {
          const projectId = JSON.parse(res.body).data?.project_id;
          if (projectId) {
            http.del(`${BASE_URL}/projects/${projectId}`, null, params);
          }
        } catch (_) {}
      }
    });
  }

  thinkTime();
}
