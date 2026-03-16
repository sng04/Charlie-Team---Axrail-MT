"""
AdminAuthorizer Lambda Function

Custom Lambda Authorizer that validates JWT token and checks for admin role.
Returns IAM policy to allow/deny access to API Gateway resources.
"""

import base64
import json
import os

from aws_lambda_powertools import Logger, Tracer

logger = Logger()
tracer = Tracer()


def _decode_jwt_payload(token: str) -> dict:
    """Decode JWT payload without verification (API Gateway already validated)."""
    try:
        # Remove Bearer prefix if present
        if token.startswith("Bearer "):
            token = token[7:]
        
        # JWT format: header.payload.signature
        parts = token.split(".")
        if len(parts) != 3:
            raise ValueError("Invalid JWT format")
        
        payload = parts[1]
        # Add padding if needed for base64 decoding
        payload += "=" * (4 - len(payload) % 4)
        decoded = base64.urlsafe_b64decode(payload)
        return json.loads(decoded)
    except Exception as e:
        logger.error(f"Failed to decode JWT: {e}")
        raise ValueError("Invalid token")


def _generate_policy(principal_id: str, effect: str, resource: str, context: dict = None) -> dict:
    """Generate IAM policy document for API Gateway."""
    policy = {
        "principalId": principal_id,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": resource,
                }
            ],
        },
    }
    
    if context:
        policy["context"] = context
    
    return policy


def _get_wildcard_resource(method_arn: str) -> str:
    """Convert specific method ARN to wildcard for caching."""
    # arn:aws:execute-api:region:account:api-id/stage/method/resource
    parts = method_arn.split("/")
    # Return wildcard to allow caching across all methods
    return f"{parts[0]}/*"


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Authorizer handler that checks if user has admin role.
    
    Returns Allow policy if user is admin, Deny otherwise.
    """
    try:
        token = event.get("authorizationToken", "")
        method_arn = event.get("methodArn", "")
        
        if not token:
            logger.warning("No authorization token provided")
            raise Exception("Unauthorized")
        
        # Decode JWT to get claims
        payload = _decode_jwt_payload(token)
        
        # Extract user info
        username = payload.get("username") or payload.get("cognito:username", "unknown")
        user_id = payload.get("sub", "unknown")
        groups = payload.get("cognito:groups", [])
        
        logger.info(f"Authorizing user: {username}, groups: {groups}")
        
        # Check if user is admin
        if "admin" not in groups:
            logger.warning(f"User {username} is not admin, denying access")
            return _generate_policy(
                principal_id=user_id,
                effect="Deny",
                resource=method_arn,
            )
        
        # User is admin, allow access
        logger.info(f"User {username} is admin, allowing access")
        
        # Use wildcard resource for better caching
        wildcard_resource = _get_wildcard_resource(method_arn)
        
        return _generate_policy(
            principal_id=user_id,
            effect="Allow",
            resource=wildcard_resource,
            context={
                "user_id": user_id,
                "username": username,
                "groups": ",".join(groups),
            },
        )
        
    except ValueError as e:
        logger.error(f"Token validation error: {e}")
        raise Exception("Unauthorized")
    except Exception as e:
        logger.exception(f"Authorizer error: {e}")
        raise Exception("Unauthorized")
