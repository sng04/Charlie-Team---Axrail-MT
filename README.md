# Axrail Meeting Intelligence Platform

AI-powered meeting assistant that provides real-time question detection, knowledge base search, gap analysis, and post-meeting coaching. Built on AWS with CDK, Lambda, DynamoDB, OpenSearch, and Amazon Bedrock.

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+ (for CDK CLI)
- AWS credentials with admin access

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Deploy

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials \
  JSII_SILENCE_WARNING_UNTESTED_NODE_VERSION=1 \
  npx cdk deploy --all --require-approval never \
  -a ".venv/bin/python3 app.py"
```

### Run Tests

```bash
# Unit tests
pytest tests/unit/ -v

# Integration tests (requires deployed stack + test fixtures)
python scripts/test_case_1.py
python scripts/test_case_2.py
```

## Architecture

6 CDK stacks deployed to `ap-southeast-1` (Bedrock Agent to `us-east-1`):

| Stack | Key Resources |
|---|---|
| `AXRAIL-DynamoDB-{env}` | 12 DynamoDB tables, 1 OpenSearch domain |
| `AXRAIL-Cognito-{env}` | User Pool, App Client, Admin/User groups |
| `AXRAIL-MeetingBot-{env}` | ECS Cluster, Task Definition, VPC, SQS |
| `AXRAIL-Lambda-{env}` | 46 Lambda functions, 5 layers, WebSocket API, S3 buckets, EventBridge |
| `AXRAIL-ApiServices-{env}` | REST API Gateway, routes, Cognito authorizers |
| `AXRAIL-BedrockAgent-{env}` | Bedrock Agent (Nova Pro), Agent Alias, test Lambda |

See [docs/architecture/overview.md](docs/architecture/overview.md) for the full architecture diagram.

## Project Structure

```text
├── app.py                    # CDK app entry point
├── stack_cdk/                # CDK stack definitions
│   ├── environment.py        # Environment configs (dev/staging/prod)
│   ├── dynamodb_stack.py     # DynamoDB tables + OpenSearch
│   ├── cognito_stack.py      # Cognito User Pool
│   ├── meeting_bot_stack.py  # ECS Meeting Bot
│   ├── lambda_stack.py       # Lambda functions + WebSocket API + S3
│   ├── api_services_stack.py # REST API Gateway
│   └── bedrock_agent_stack.py# Bedrock Agent (us-east-1)
├── lambdas/
│   ├── Functions/            # 46 Lambda function packages
│   └── Layers/               # 5 shared Lambda layers
├── meeting_bot/              # ECS meeting bot container
├── resources/                # Test fixture data (KB files, transcripts)
├── scripts/                  # Integration test scripts
├── tests/unit/               # Unit tests (pytest)
└── docs/                     # Project documentation
```

## Documentation

| Document | Description |
|---|---|
| [Architecture Overview](docs/architecture/overview.md) | System diagram, stack composition, component summary |
| [Data Model](docs/architecture/data-model.md) | DynamoDB tables, OpenSearch index, entity relationships |
| [REST API Reference](docs/api/README.md) | All REST endpoints with request/response examples |
| [WebSocket API Reference](docs/api/websocket-api.md) | Real-time agent actions and message formats |
| [Deployment Runbook](docs/runbooks/deployment.md) | Deploy commands, failure scenarios, resolution steps |
| [Testing Runbook](docs/runbooks/end-to-end-tests.md) | Integration test execution and troubleshooting |
| [Test Plan](docs/testing/test-plan.md) | Comprehensive test cases for all agent functions |
| [ADR-007: Session State Fix](docs/architecture/adr/007-session-state-and-websocket-fixes.md) | Session lifecycle and WebSocket endpoint fix |

## Environments

| Environment | DynamoDB | Lambda Memory | OpenSearch | Log Retention |
|---|---|---|---|---|
| `dev` | PAY_PER_REQUEST | 256 MB | t3.small (1 node) | 7 days |
| `staging` | PROVISIONED | 512 MB | t3.medium (2 nodes) | 30 days |
| `prod` | PROVISIONED | 1024 MB | r6g.xlarge (3 nodes) | 90 days |

Deploy a specific environment:

```bash
npx cdk deploy --all -c environment=staging
```
