// ============================================================
// Scenario 5: Soak Test
// Sustained moderate load over 2 hours to detect degradation
// ============================================================

import http from "k6/http";
import { check } from "k6";
import { Rate, Trend } from "k6/metrics";
import { BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD, SLA } from "../config.js";
import { getAdminToken, authHeaders, thinkTime, randomProjectName, uuid } from "../helpers.js";

const errorRate = new Rate("errors");
const soakLatency = new Trend("soak_latency", true);

export const options = {
  scenarios: {
    soak: {
      executor: "ramping-vus",
      startVUs: 0,
      stages: [
        { duration: "5m", target: 15 },    // ramp up
        { duration: "110m", target: 15 },   // hold for ~2 hours
        { duration: "5m", target: 0 },      // ramp down
      ],
      gracefulRampDown: "30s",
    },
  },
  thresholds: {
    http_req_duration: [`p(95)<${SLA.p95_latency_ms}`],
    errors: [`rate<${SLA.error_rate}`],
  },
};

export function setup() {
  const token = getAdminToken(BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD);
  if (!token) throw new Error("Auth failed");
  return { token };
}

export default function (data) {
  const params = authHeaders(data.token);

  // Realistic user journey: browse → create → read → delete
  const endpoints = [
    { method: "GET", path: "/projects" },
    { method: "GET", path: "/users" },
    { method: "GET", path: "/agents?page=1&limit=10" },
    { method: "GET", path: "/personalities?page=1&limit=10" },
    { method: "GET", path: "/bot-credentials" },
  ];

  // 70% reads
  const ep = endpoints[Math.floor(Math.random() * endpoints.length)];
  const res = http.get(`${BASE_URL}${ep.path}`, params);
  check(res, { [`${ep.path} ok`]: (r) => r.status === 200 });
  errorRate.add(res.status !== 200);
  soakLatency.add(res.timings.duration);

  thinkTime();

  // 30% write + cleanup
  if (Math.random() < 0.3) {
    const createRes = http.post(
      `${BASE_URL}/projects`,
      JSON.stringify({
        name: randomProjectName(),
        email: `soak-${uuid().slice(0, 8)}@example.com`,
      }),
      params
    );
    errorRate.add(createRes.status !== 200);
    soakLatency.add(createRes.timings.duration);

    if (createRes.status === 200) {
      try {
        const pid = JSON.parse(createRes.body).data?.project_id;
        if (pid) {
          thinkTime();
          http.del(`${BASE_URL}/projects/${pid}`, null, params);
        }
      } catch (_) {}
    }
  }

  thinkTime();
}
