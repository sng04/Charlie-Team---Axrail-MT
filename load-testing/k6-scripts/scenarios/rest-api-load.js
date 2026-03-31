// ============================================================
// Scenario 1: REST API Load Test
// Normal traffic simulation across all major endpoints
// ============================================================

import http from "k6/http";
import { check, group } from "k6";
import { Rate, Trend } from "k6/metrics";
import { BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD, SLA } from "../config.js";
import {
  getAdminToken,
  authHeaders,
  thinkTime,
  uuid,
  randomProjectName,
  randomMeetingLink,
} from "../helpers.js";

// Custom metrics
const errorRate = new Rate("errors");
const authLatency = new Trend("auth_latency", true);
const crudLatency = new Trend("crud_latency", true);

export const options = {
  scenarios: {
    // Normal load: ramp up to 20 VUs over 2 min, hold 5 min, ramp down
    normal_load: {
      executor: "ramping-vus",
      startVUs: 0,
      stages: [
        { duration: "2m", target: 20 },  // ramp up
        { duration: "5m", target: 20 },  // steady state
        { duration: "1m", target: 0 },   // ramp down
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
  if (!token) {
    throw new Error("Failed to authenticate — cannot proceed with load test");
  }
  return { token };
}

export default function (data) {
  const params = authHeaders(data.token);

  // --- Authentication Flow ---
  group("Authentication", () => {
    const start = Date.now();
    const res = http.post(
      `${BASE_URL}/auth/admin/login`,
      JSON.stringify({
        username: ADMIN_USERNAME,
        password: ADMIN_PASSWORD,
      }),
      { headers: { "Content-Type": "application/json" } }
    );
    authLatency.add(Date.now() - start);
    check(res, { "login status 200": (r) => r.status === 200 });
    errorRate.add(res.status !== 200);
  });

  thinkTime();

  // --- Project CRUD ---
  group("Projects", () => {
    // List projects
    let res = http.get(`${BASE_URL}/projects`, params);
    check(res, { "list projects 200": (r) => r.status === 200 });
    errorRate.add(res.status !== 200);
    crudLatency.add(res.timings.duration);

    thinkTime();

    // Create project
    const projectName = randomProjectName();
    res = http.post(
      `${BASE_URL}/projects`,
      JSON.stringify({
        name: projectName,
        email: `test-${uuid().slice(0, 8)}@example.com`,
        description: "Load test project",
      }),
      params
    );
    check(res, { "create project 200": (r) => r.status === 200 });
    errorRate.add(res.status !== 200);
    crudLatency.add(res.timings.duration);

    let projectId = null;
    if (res.status === 200) {
      try {
        projectId = JSON.parse(res.body).data?.project_id;
      } catch (_) {}
    }

    thinkTime();

    // Get project
    if (projectId) {
      res = http.get(`${BASE_URL}/projects/${projectId}`, params);
      check(res, { "get project 200": (r) => r.status === 200 });
      errorRate.add(res.status !== 200);
      crudLatency.add(res.timings.duration);

      thinkTime();

      // Update project
      res = http.put(
        `${BASE_URL}/projects/${projectId}`,
        JSON.stringify({ description: "Updated by load test" }),
        params
      );
      check(res, { "update project 200": (r) => r.status === 200 });
      errorRate.add(res.status !== 200);

      thinkTime();

      // Get project sessions (empty)
      res = http.get(`${BASE_URL}/projects/${projectId}/sessions`, params);
      check(res, { "get project sessions 200": (r) => r.status === 200 });
      errorRate.add(res.status !== 200);

      thinkTime();

      // Delete project (cleanup)
      res = http.del(`${BASE_URL}/projects/${projectId}`, null, params);
      check(res, { "delete project 200": (r) => r.status === 200 });
      errorRate.add(res.status !== 200);
    }
  });

  thinkTime();

  // --- Users CRUD ---
  group("Users", () => {
    const res = http.get(`${BASE_URL}/users`, params);
    check(res, { "list users 200": (r) => r.status === 200 });
    errorRate.add(res.status !== 200);
    crudLatency.add(res.timings.duration);
  });

  thinkTime();

  // --- Agents CRUD ---
  group("Agents", () => {
    let res = http.get(`${BASE_URL}/agents?page=1&limit=10`, params);
    check(res, { "list agents 200": (r) => r.status === 200 });
    errorRate.add(res.status !== 200);
    crudLatency.add(res.timings.duration);
  });

  thinkTime();

  // --- Personalities CRUD ---
  group("Personalities", () => {
    let res = http.get(`${BASE_URL}/personalities?page=1&limit=10`, params);
    check(res, { "list personalities 200": (r) => r.status === 200 });
    errorRate.add(res.status !== 200);
    crudLatency.add(res.timings.duration);
  });

  thinkTime();

  // --- Bot Credentials ---
  group("Bot Credentials", () => {
    let res = http.get(`${BASE_URL}/bot-credentials`, params);
    check(res, { "list bot credentials 200": (r) => r.status === 200 });
    errorRate.add(res.status !== 200);
    crudLatency.add(res.timings.duration);
  });
}
