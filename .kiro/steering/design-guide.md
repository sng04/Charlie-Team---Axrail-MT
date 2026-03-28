---
inclusion: auto
name: architecture-patterns
description: Serverless architecture principles, Lambda handler patterns, data access patterns, CDK stack design, API design, environment management, performance optimization, and design decision records.
---

# Design Patterns & Architecture

## Architectural Principles

### Serverless-First Architecture
- Lambda functions as primary compute layer
- Event-driven design with API Gateway triggers
- Stateless function design — no local state persistence
- Cold start optimization through layer usage and minimal dependencies

### Security by Design
- Cognito integration for authentication
- IAM roles with least privilege principle
- VPC isolation for Lambda functions in private subnets
- API Gateway authorization at endpoint level

### Observability
- AWS X-Ray tracing enabled on all Lambda functions
- Structured logging with aws-lambda-powertools Logger
- CloudWatch metrics and alarms for monitoring
- Tracer annotations for error tracking and debugging

## Lambda Function Design Patterns

### Handler Pattern
All Lambda functions follow a consistent structure:

1. **Initialization** (outside handler for warm starts):
```python
from aws_lambda_powertools import Logger, Tracer
import boto3

logger = Logger()
tracer = Tracer()
dynamodb = boto3.resource('dynamodb')
```

2. **Handler with decorator**:
```python
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    # Implementation
```
3. **Error handling hierarchy**:
- Custom exceptions (BadRequestError, NotFoundError, UnauthorizedError)
- Specific HTTP status codes per exception type
- Generic Exception catch-all with 500 status
- Tracer annotations on errors for debugging

### Response Standardization
All API responses use `createResponse()` helper:
```python
{
    'statusCode': int,      # HTTP status code
    'status': bool,         # Success/failure flag
    'message': str,         # Human-readable message
    'data': dict           # Optional payload
}
```

### Authentication Pattern
```python
headers = event.get('headers', {})
authorization = headers.get('Authorization') or headers.get('authorization')
if not authorization:
    raise UnauthorizedError("Authorization header missing")
```

## Data Access Patterns

### DynamoDB Best Practices
- Use consistent table naming: `{environment}-{TableName}` (e.g., `dev-Orders`)
- Leverage GSIs for alternate access patterns
- Use batch operations for multiple item reads/writes
- Handle conditional writes for optimistic locking
- Use Decimal type for numeric precision

### Cascade Delete Pattern
When deleting a parent resource that owns child resources, follow this pattern:
1. Check for blocking conditions first (e.g., active meetings prevent project deletion)
2. Return 409 Conflict with a descriptive message if blocked
3. Delete children bottom-up: grandchildren → children → parent
4. Use paginated queries + batch_writer for efficient bulk deletes
5. Log deletion counts for observability

Current cascade rules:
- **DeleteProject**: rejects if any session has `bot_status = "in_meeting"`. Deletes transcripts → sessions → project_users → project. Bot credentials are NOT deleted.
- **DeleteSession**: deletes session only (transcripts are not cascade-deleted yet)

### Error Handling for Data Operations
```python
try:
    response = table.get_item(Key={'id': item_id})
    if 'Item' not in response:
        raise NotFoundError(f"Item {item_id} not found")
except ClientError as e:
    logger.error(f"DynamoDB error: {e}")
    raise
```

## CDK Stack Design

### Stack Organization
- Separation of concerns: shared resources stack separate from API stack
- Environment-driven: configuration externalized to a config module
- Reusability: Lambda layers for shared code and dependencies

### Resource Naming Convention
- Stacks: `{ProjectName}-{StackPurpose}-{Environment}`
- Lambda functions: `{PROJECT}-{FunctionName}`
- DynamoDB tables: `{environment}-{TableName}`
- IAM roles: `{FunctionName}Role`

### Cross-Stack References
- Use SSM Parameter Store for Lambda layer ARNs
- Export VPC configuration from network stack
- Share security groups across functions

## API Design Patterns

### RESTful Endpoint Structure
- Resource-based URLs: `/{resources}/{resourceId}`
- HTTP methods aligned with operations (GET, POST, PUT, DELETE)
- Versioning strategy: path-based when breaking changes are needed

### Request Validation
- Validate required fields early in handler
- Use custom exceptions for validation failures
- Return 400 Bad Request with descriptive messages

### Idempotency
- Use idempotency tokens for write operations
- Conditional writes in DynamoDB to prevent duplicates
- Return existing resource on duplicate creation attempts

## Environment Management

### Multi-Environment Strategy
- Separate or isolated resources per environment
- Environment-specific configuration in a dedicated config module
- Consistent deployment process across environments
- Use CDK context for environment selection

### Configuration Hierarchy
1. CDK context (deployment time)
2. Environment variables (Lambda runtime)
3. SSM Parameter Store (dynamic configuration)
4. DynamoDB (application data)

## Performance Optimization

### Cold Start Mitigation
- Minimize Lambda package size
- Use layers for heavy dependencies
- Initialize SDK clients outside handler
- Consider provisioned concurrency for critical paths

### DynamoDB Optimization
- Design partition keys for even distribution
- Use projection expressions to fetch only needed attributes
- Implement caching layer for frequently accessed data
- Monitor and adjust read/write capacity

## Error Handling Strategy

### Exception Hierarchy
```
Exception (500 - Internal Server Error)
├── BadRequestError (400 - Bad Request)
├── UnauthorizedError (401 - Unauthorized)
├── ForbiddenError (403 - Forbidden)
├── NotFoundError (404 - Not Found)
└── ConflictError (409 - Conflict)
```

### Graceful Degradation
- Return partial results when possible
- Provide meaningful error messages to clients
- Implement retry logic with exponential backoff
- Use circuit breaker pattern for external dependencies

## Testing Strategy

See `testing-standards` for full testing standards, mocking patterns, and test quantity guidelines.

## Deployment Practices

See `deployment-workflow` for full deployment procedures, environment configs, and rollback strategies.

## Common Pitfalls to Avoid

- Don't store state in Lambda function memory
- Don't use synchronous calls between Lambda functions
- Don't hardcode environment-specific values
- Don't ignore cold start performance
- Don't over-provision DynamoDB capacity
- Don't log sensitive information
- Don't skip error handling for AWS SDK calls
- Don't use blocking operations in Lambda handlers

## Design Decision Records

### Why Lambda Layers?
- Reduces deployment package size per function
- Enables code reuse across functions
- Separates business logic from dependencies
- Faster deployment times for function code changes

### Why VPC for Lambda?
- Required for private resource access
- Enhanced security through network isolation
- Controlled egress through NAT Gateway
- Trade-off: increased cold start time

### Why DynamoDB over RDS?
- Serverless scaling without capacity planning
- Pay-per-request pricing model
- Single-digit millisecond latency
- No connection pooling complexity
- Better fit for key-value access patterns

### Why API Gateway REST API?
- Mature feature set for RESTful APIs
- Built-in request/response transformation
- Native Cognito integration
- Comprehensive monitoring and logging
