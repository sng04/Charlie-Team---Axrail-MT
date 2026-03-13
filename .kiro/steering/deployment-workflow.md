---
inclusion: auto
---

# Deployment Workflow

Build, deploy, and rollback procedures for all environments.

## Environments

| Environment | Auto-Deploy | Approval | DynamoDB Billing | Lambda Memory | OpenSearch |
|-------------|-------------|----------|------------------|---------------|------------|
| dev | Yes (on push) | None | PAY_PER_REQUEST | 256 MB | t3.small × 1 |
| staging | Yes (pipeline) | Manual | PROVISIONED | 512 MB | t3.medium × 2 |
| prod | Yes (pipeline) | Manual | PROVISIONED | 1024 MB | r6g.xlarge × 3 |

All environment configs live in `stack_cdk/environment.py`. Never hardcode account IDs or region — these resolve from `CDK_DEFAULT_ACCOUNT` and `CDK_DEFAULT_REGION` at synth time.

## Stack Dependency Order

Stacks must deploy in this order (CDK enforces via `add_dependency`):

```
1. SharedResources  (layers, IAM roles, SNS alarms)
2. DynamoDB          (tables, OpenSearch domain)
3. UsEast1Resources  (Knowledge Base — cross-region)
4. ApiServices       (API Gateway, Lambda functions, SQS, WebSocket)
   AsyncJobs         (Step Functions, EventBridge rules)
   Frontend          (S3 SPA hosting)
```

## Local Development Deploy

For iterating on dev, deploy directly from your machine:

```bash
# Synth first to catch errors early
cdk synth

# Review what will change
cdk diff

# Deploy all stacks with auto-approval and concurrency of 3
cdk deploy --all --require-approval never --concurrency 3

# Or target a single stack for faster iteration
cdk deploy PokeMart-ApiServices-dev --require-approval never
```

### Hotswap (Lambda-Only Changes)
When only Lambda code changed (no infra), skip CloudFormation entirely:
```bash
cdk deploy PokeMart-ApiServices-dev --hotswap
```
This updates Lambda function code in seconds instead of minutes. Do not use hotswap for infra changes — it will silently skip them.

## CI/CD Pipeline

The pipeline lives in a separate repo (`savio_phase2_codepipeline/`) and uses CDK Pipelines:

1. Push to `main` on the App Repo triggers the pipeline.
2. Pipeline runs `cdk synth` and self-mutates if the pipeline definition changed.
3. Automated `pytest` suite runs against the synthesized app.
4. On success, deploys to `dev` automatically with `--require-approval never --concurrency 3`.
5. Staging and prod stages require manual approval (`manual_approval_enabled: True`).

### Pipeline Deploy Flags
All pipeline-triggered deployments use:
- `--require-approval never` — auto-approve all changes
- `--concurrency 3` — deploy up to 3 independent stacks in parallel

## CDK Deploy Defaults

When deploying (locally or via pipeline), always use these flags:

```bash
cdk deploy --require-approval never --concurrency 3
```

- `--require-approval never`: skip interactive approval prompts. The pipeline and dev workflow both auto-approve.
- `--concurrency 3`: deploy up to 3 stacks in parallel where dependency order allows.

## Pre-Deploy Checklist

Before deploying any change:

1. `cdk synth` — validates templates compile without errors.
2. `cdk diff` — review the changeset. Look for unexpected resource replacements or deletions.
3. `pytest tests/unit/ -v` — run unit tests (should pass before any deploy).
4. Commit with a descriptive message following conventional commits: `feat:`, `fix:`, `chore:`.

## Rollback Strategy

### Automatic (Pipeline)
CDK Pipelines monitors CloudFormation stack events. If a stack update fails, CloudFormation automatically rolls back to the previous known-good state.

### Manual Rollback
If a deployment succeeds but the feature is broken:

```bash
# Revert the commit
git revert HEAD
git push origin main
```

This triggers a new pipeline run that deploys the previous code. For Lambda-only rollbacks, you can also redeploy the previous version via hotswap.

### DynamoDB Rollback Considerations
- DynamoDB table deletions are protected in staging/prod (`RemovalPolicy.RETAIN`).
- Schema changes (new GSIs, key changes) cannot be rolled back — plan these carefully.
- Data migrations should be backward-compatible so the previous code version still works.

## Environment-Specific Notes

### Dev
- PAY_PER_REQUEST billing — no capacity planning needed.
- 7-day CloudWatch log retention.
- Single OpenSearch node — no HA.
- Fastest iteration: use `--hotswap` for Lambda changes.

### Staging
- Provisioned capacity (100 RCU / 100 WCU) — mirrors prod patterns.
- 30-day log retention.
- 2-node OpenSearch cluster.
- Manual approval gate in pipeline.

### Prod
- Provisioned capacity (1000 RCU / 1000 WCU).
- 90-day log retention.
- 3-node OpenSearch cluster with `r6g.xlarge` instances.
- Manual approval gate in pipeline.
- 3 private subnets for higher availability.

## Post-Deploy Verification

After deploying to any environment:
1. Check CloudWatch for Lambda errors or elevated latency.
2. Verify API Gateway stage is serving traffic (hit a GET endpoint).
3. Check X-Ray service map for broken traces.
4. Monitor SNS alarm topic for any triggered alarms.
