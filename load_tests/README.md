# AXRAIL API Load Test Suite

Performance load tests using [Locust](https://locust.io/).

## Setup

```bash
cd load_tests
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

## Running Tests

```bash
# Normal load (50 users)
locust -f locustfile.py --headless -u 50 -r 5 --run-time 5m --csv=results/normal

# Peak load (200 users)
locust -f locustfile.py --headless -u 200 -r 20 --run-time 5m --csv=results/peak

# Stress test (ramp until failure)
locust -f locustfile.py --headless -u 1000 -r 50 --run-time 10m --csv=results/stress

# Web UI mode
locust -f locustfile.py
```

Open `http://localhost:8089` for the Locust web UI.
