---
inclusion: auto
name: coding-standards
description: Clean-code standards for Python serverless projects. Covers naming conventions, module structure, function design, error handling, logging, DynamoDB patterns, and code smells.
---

# Coding Standards & Best Practices

General-purpose clean-code standards for Python serverless projects. These rules apply to all Lambda functions, shared layers, CDK stacks, and utility modules.

## Naming Conventions

### Files & Directories
- Lambda handler files: `lambda_function.py` (one per directory)
- Lambda directories: `PascalCase` matching the action (e.g., `CreateItem/`, `GetOrder/`)
- Layer modules: `snake_case.py` (e.g., `response_utils.py`, `custom_exceptions.py`)
- CDK stacks: `snake_case.py` with `_stack` suffix (e.g., `api_services_stack.py`)
- Test files: `test_<domain>.py` or `test_<stack_name>.py`

### Python Identifiers
- Functions and methods: `snake_case` (e.g., `lambda_handler`, `get_parameter`)
- Private/internal helpers: `_leading_underscore` (e.g., `_get_client`, `_create_resources`)
- Classes: `PascalCase` (e.g., `SharedResourcesStack`, `RetryableError`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `TABLE_NAME`, `MAX_RETRIES`)
- Variables: `snake_case` (e.g., `order_id`, `total_amount`)
- Boolean variables: use `is_`, `has_`, or `should_` prefixes (e.g., `is_valid`, `has_items`)

### AWS Resource Naming
- Lambda functions: `{PROJECT}-{FunctionName}` (e.g., `MYAPP-GetItem`)
- DynamoDB tables: `{environment}-{TableName}` (e.g., `dev-Orders`)
- SSM parameters: `/{project}/{environment}/{category}/{name}` (e.g., `/{project}/dev/layers/base-arn`)
- CDK construct IDs: `PascalCase` descriptive names (e.g., `CrudLambdaRole`, `OrdersQueue`)

## Module Structure

### Lambda Handler Files

Follow this exact ordering in every handler file:

```python
"""
{FunctionName} Lambda Function

Brief description of what this function does.
"""

# 1. Standard library imports
import json
import os
import uuid
from datetime import datetime

# 2. Third-party imports
from aws_lambda_powertools import Logger, Tracer
import boto3

# 3. Layer / local imports
from custom_exceptions import BadRequestError, NotFoundError
from response_utils import createResponse

# 4. Module-level initialization (outside handler for warm starts)
logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('TABLE_NAME')
table = dynamodb.Table(table_name)


# 5. Private helper functions
def _validate_input(data):
    ...


# 6. Handler (always last)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    ...
```

### CDK Stack Files

```python
"""
Stack description.
"""

# Imports
from aws_cdk import ...

class MyStack(Stack):
    def __init__(self, scope, construct_id, *, environment, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        # Orchestrate via private methods
        self._create_resources()
        self._create_exports()
        self._apply_tags()

    # Private methods grouped by concern
    def _create_resources(self):
        ...
```

## Function Design

### Keep Functions Small and Focused
- Each function does one thing. If a docstring needs "and", split it.
- Handler functions orchestrate; helpers do the work.
- Target under 30 lines per function. Refactor if it grows beyond 50.

### Docstrings
- Every public function and class gets a docstring.
- Use Google-style format with `Args`, `Returns`, and `Raises` sections.
- Module-level docstrings describe the file's purpose and key behaviors.
- Private helpers get a one-liner docstring unless the logic is non-obvious.

```python
def get_parameter(parameter_name: str, use_cache: bool = True) -> Optional[str]:
    """
    Retrieve a parameter from SSM Parameter Store.

    Args:
        parameter_name: Full parameter path (e.g., '/{project}/dev/layers/base-arn')
        use_cache: Whether to use cached value. Defaults to True.

    Returns:
        Parameter value, or None if not found.
    """
```

### Type Hints
- Use type hints on all public function signatures.
- Use `typing` module types (`Optional`, `Dict`, `List`, `Any`, `Union`) for complex signatures.
- Private helpers should have type hints when the types aren't obvious from context.

## Error Handling

### Exception Hierarchy
Map custom exceptions to HTTP status codes consistently:

| Exception | Status Code | When to Raise |
|---|---|---|
| `BadRequestError` | 400 | Missing/invalid input |
| `UnauthorizedError` | 401 | Missing or invalid auth token |
| `ForbiddenError` | 403 | Authenticated but insufficient permissions |
| `NotFoundError` | 404 | Resource doesn't exist |
| `ConflictError` | 409 | Duplicate or concurrent modification |
| `Exception` (catch-all) | 500 | Unexpected failures |

### Handler Error Pattern
Every API-facing handler must follow this structure:

```python
try:
    # Business logic
    return createResponse(200, "Success message", data)
except BadRequestError as e:
    logger.warning(f"Bad request: {e}")
    return createResponse(400, str(e))
except NotFoundError as e:
    logger.warning(f"Not found: {e}")
    return createResponse(404, str(e))
except ClientError as e:
    if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
        return createResponse(404, "Resource not found")
    logger.exception("DynamoDB error")
    return createResponse(500, "Internal server error")
except Exception as e:
    logger.exception("Unexpected error")
    return createResponse(500, "Internal server error")
```

### Rules
- Never expose internal error details to the client. Log them, return a generic message.
- Use `logger.warning` for client errors (4xx), `logger.exception` for server errors (5xx).
- Annotate errors on the tracer for X-Ray visibility: `tracer.put_annotation("error", str(e))`
- For async/queue handlers, return partial batch failures instead of raising.

## Input Validation

### Validate Early, Fail Fast
- Validate all required fields at the top of the handler before any business logic.
- Use a reusable pattern for missing field checks:

```python
required_fields = ['name', 'price', 'category']
missing = [f for f in required_fields if f not in data or data[f] is None]
if missing:
    raise BadRequestError(f"Missing required fields: {', '.join(missing)}")
```

- Parse `event['body']` defensively — it may be a string or dict:

```python
body = event.get('body', '{}')
data = json.loads(body) if isinstance(body, str) else body
```

## Logging & Observability

### Structured Logging
- Use `aws_lambda_powertools.Logger` — never bare `print()` statements.
- Log at the right level: `info` for success paths, `warning` for client errors, `exception` for server errors.
- Include contextual data via `extra={}`, not string interpolation of sensitive fields.

```python
logger.info("Resource created", extra={'resource_id': resource_id})
```

### Tracing
- Decorate every handler with `@tracer.capture_lambda_handler`.
- Decorate significant helper functions with `@tracer.capture_method`.
- Add annotations on errors for X-Ray filtering.

### What NOT to Log
- Auth tokens, passwords, or secrets
- Full request/response bodies in production (use debug level if needed)
- PII without masking

## DynamoDB Patterns

### Client Initialization
- Initialize `boto3.resource('dynamodb')` and table references at module scope for connection reuse.
- Read table names from environment variables, never hardcode.

### Writes
- Use `ensure_decimal()` for all numeric values going into DynamoDB.
- Use `ConditionExpression='attribute_exists(pk)'` on updates/deletes to detect missing items.
- Always set `updatedAt` timestamp on mutations.

### Reads
- Check `'Item' in response` after `get_item` — raise `NotFoundError` if absent.
- Use projection expressions to fetch only needed attributes on large items.

### Dynamic Update Expressions
When updating arbitrary fields, build expressions dynamically:

```python
parts, names, values = [], {}, {}
for key, val in update_data.items():
    parts.append(f"#{key} = :{key}")
    names[f"#{key}"] = key
    values[f":{key}"] = val

table.update_item(
    Key={'id': item_id},
    UpdateExpression="SET " + ", ".join(parts),
    ExpressionAttributeNames=names,
    ExpressionAttributeValues=values,
    ReturnValues='ALL_NEW'
)
```

## Response Format

All API responses use the shared `createResponse()` utility. Never construct response dicts manually.

```python
return createResponse(status_code, message, data)  # data is optional
```

This ensures consistent shape, CORS headers, and Decimal serialization across every endpoint.

## Cold Start Optimization

- Initialize SDK clients, loggers, and table references outside the handler.
- Use lazy initialization (with a module-level `None` sentinel) for expensive clients that aren't always needed.
- Keep import footprint minimal — avoid importing unused modules.

```python
_client = None

def _get_expensive_client():
    global _client
    if _client is not None:
        return _client
    # expensive init here
    _client = SomeClient(...)
    return _client
```

## Idempotency

- Accept an `idempotencyToken` on write operations.
- Query for existing records with the same token before creating.
- Return the existing resource (with 202) if a duplicate is detected.

## Code Smells to Avoid

- Hardcoded AWS resource names, ARNs, or account IDs
- Bare `except:` or `except Exception: pass`
- Mutable default arguments in function signatures
- Business logic inside the handler's `try` block that should be in a helper
- Deeply nested conditionals — extract to named functions
- String concatenation for log messages instead of structured `extra={}`
- `print()` instead of `logger`
- Returning raw dicts instead of using `createResponse()`
- Catching `ClientError` without checking the error code
