---
inclusion: auto
name: tech-guide
description: Technologies to use and what to use them for. Also contains standard deployment and testing procedures as well as relevant commands.
---

# Technology Stack

## Infrastructure as Code
- **AWS CDK** (Python) - Infrastructure definition and deployment
- **CloudFormation** - Generated from CDK for AWS resource provisioning
- **CDK Pipelines** - Self-mutating CI/CD handling cross-repo source fetching, automated testing, and execution.

## Runtime & Language
- **Python 3.11** - Lambda function runtime
- **boto3** - AWS SDK for Python
- **Pytest** - Automated unit and integration testing

## AWS Services
- **Lambda** - Serverless compute for API handlers and workers
- **API Gateway** (REST API) - HTTP endpoint management
- **DynamoDB** - NoSQL database for products, orders, and member data
- **OpenSearch** - Advanced search and indexing engine
- **Cognito** - User authentication (Admin and Member pools)
- **S3** - Frontend SPA hosting, image storage, and CSV daily report storage
- **SQS** - Decoupled, asynchronous order processing queues
- **Step Functions** - Orchestration for multi-step ETL workflows (PokeAPI rotation)
- **EventBridge** - Serverless cron jobs triggering ETL and reporting
- **SES** - Automated email delivery for analytics reports
- **VPC** - Network isolation for Lambda functions
- **X-Ray** - Distributed tracing
- **CloudWatch** - Logging and monitoring, coupled with SNS for error alarms
- **SSM Parameter Store** - Configuration management

## Key Libraries
- **aws-lambda-powertools** - Logger, Tracer, and event handling utilities
- **simplejson** - JSON serialization with Decimal support
- **opensearch-py** & **requests-aws4auth** - OpenSearch connectivity and AWS Signature V4 authentication
- **Pillow** - Image processing and manipulation

## Common Commands

### Environment Setup
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
```

### CDK Operations
```bash
# List all stacks
cdk ls

# Synthesize CloudFormation template
cdk synth

# Compare deployed stack with current state
cdk diff

# Deploy to AWS (Local bypass for Dev environment)
cdk deploy

# Fast Hotswap deployment (Bypasses CloudFormation for rapid Lambda iteration)
cdk deploy PokeMartApplicationStage-Dev-ApiServicesStack --hotswap

# Open CDK documentation
cdk docs
```

### CI/CD Operations
Developers should push application code to the App Repo to trigger automated Pytest suites and deployment.
```bash
git add .
git commit -m "feat: added new product endpoint"
git push origin main
```

## Environment Configuration
Environments are configured in `stack_cdk/environment.py` to define safe multi-stage rollouts:
- `dev` - Development (CI/CD auto-deployment target)
- `staging` - Staging (Manual approval step in pipeline)
- `prod` - Production (Highly restricted, auto-scaled environment)