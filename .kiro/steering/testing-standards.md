---
inclusion: auto
name: testing-standards
description: Unit testing approach, task ordering (tests are optional and last), mocking strategies, test quantity guidelines, naming conventions, and anti-patterns.
---

# Unit Testing Standards

## When to Write Tests

Tests are optional and always come last in the task order. When building a feature:
1. Implement the feature end-to-end until it works.
2. Only after the feature is confirmed working, define unit tests to examine edge cases.
3. Never block feature delivery on test coverage — tests validate, they don't gate progress.

## Framework & Tooling
- **Pytest** as the test runner
- **unittest.mock** for mocking AWS services and external dependencies
- Run tests: `pytest tests/unit/ -v`

## Project Layout
```
tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures and module-level mocks
│   ├── test_<domain>.py     # Lambda handler tests grouped by domain
│   └── test_<stack>.py      # CDK stack assertion tests
```

## conftest.py — Module-Level Mocking

Lambda functions initialize `Logger()`, `Tracer()`, and boto3 clients at module scope for warm-start optimization. These must be mocked in `conftest.py` before any Lambda module is imported.

### Required mocks:
1. `aws_lambda_powertools` — Logger and Tracer as passthroughs
2. Any third-party library initialized at module scope (OpenSearch, AI SDKs, etc.)

### Layer path injection:
Add Lambda layer paths to `sys.path` so shared utilities resolve correctly:
```python
_layers_path = os.path.join(os.path.dirname(__file__), '../../lambdas/Layers/{LayerName}/python')
sys.path.insert(0, os.path.abspath(_layers_path))
```

### Environment variables:
Set defaults for all env vars that Lambda modules read at import time via `os.environ.setdefault()`.

## Lambda Handler Tests

### Test class structure
Group tests by Lambda function using classes:
```python
class TestCreateItem:
    @patch('lambdas.Functions.CreateItem.lambda_function.table')
    def test_success(self, mock_table):
        from lambdas.Functions.CreateItem.lambda_function import lambda_handler
        # ...
```

### What to test per handler (keep it lean)
For each Lambda handler, write tests covering these paths only:
1. **Happy path** — valid input returns expected status code and response shape
2. **Validation failure** — missing or invalid required fields return 400
3. **Not found** — resource lookup misses return 404 (where applicable)
4. **Error handling** — AWS SDK or external service errors return 500

Do NOT write exhaustive edge-case tests for every field combination. The goal is deployment confidence, not 100% branch coverage.

### Mocking strategy
- Patch boto3 resources/clients at the **module attribute** level (e.g., `lambda_function.table`), not at `boto3.resource`
- Use `MagicMock` for DynamoDB tables, SQS clients, S3 clients
- For AI/agent SDKs, mock the agent class and its return value
- For WebSocket handlers, mock the management API client

### Response assertion pattern
```python
def _parse_body(response):
    return json.loads(response['body'])

response = lambda_handler(event, None)
body = _parse_body(response)
assert response['statusCode'] == 200
assert body['status'] is True
```

## CDK Stack Tests

### Pattern
Use `aws_cdk.assertions.Template` to validate synthesized CloudFormation:
```python
from aws_cdk import App, assertions
from stack_cdk.my_stack import MyStack

class TestMyStack:
    def test_resource_created(self):
        app = App()
        stack = MyStack(app, "TestStack", environment="dev")
        template = assertions.Template.from_stack(stack)
        template.has_resource_properties("AWS::DynamoDB::Table", {
            "TableName": "dev-MyTable"
        })
```

### What to test per stack
1. **Resource creation** — key resources exist with correct properties
2. **Environment variance** — dev vs prod differences (e.g., deletion protection)
3. **IAM permissions** — roles have expected policy statements
4. **Exports** — cross-stack references are exported correctly

## Layer Utility Tests

Test shared layer modules directly:
- Import from the layer path (already on `sys.path` via conftest)
- Mock `boto3` clients where needed
- Test type conversions, caching behavior, and error cases

## Test Quantity Guidelines

Keep the test suite lean to avoid slowing down CI/CD deployment:

| Component Type | Tests Per Component | Focus |
|---|---|---|
| Lambda handler (CRUD) | 3–4 | success, validation, not-found, error |
| Lambda handler (async/ETL) | 2–3 | success, partial failure |
| Lambda handler (AI/agent) | 4–5 | success, validation, session mgmt, service errors |
| CDK stack | 3–5 per resource | creation, env variance, permissions |
| Layer utility | 2–3 per function | happy path, edge case, error |

## Naming Conventions
- Test files: `test_<domain>.py` or `test_<stack_name>.py`
- Test classes: `Test<FunctionName>` or `Test<StackName>`
- Test methods: `test_<scenario>` (e.g., `test_success`, `test_missing_required_field`, `test_not_found`)

## Anti-Patterns to Avoid
- Testing implementation details (internal variable names, call order) instead of behavior
- Duplicating the same assertion across many near-identical tests
- Mocking so deeply that the test validates mocks, not logic
- Writing integration-style tests in the unit test suite (no real AWS calls)
- Testing third-party library behavior (e.g., verifying boto3 serialization)
