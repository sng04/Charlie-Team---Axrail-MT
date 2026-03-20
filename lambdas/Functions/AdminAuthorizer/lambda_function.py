"""
AdminAuthorizer Lambda Function

Custom Lambda Authorizer that validates JWT token and checks for admin role.
Validates token against Cognito to ensure revoked tokens are rejected immediately.
Returns IAM policy to allow/deny access to API Gateway resources.
"""

import os

import boto3
from aws_lambda_powertools import Logger, Tracer

logger = Logger()
tracer = Tracer()

cognito_client = boto3.client("cognito-idp")
USER_POOL_ID = os.environ.get("USER_POOL_ID")


def _extract_token(auth_header: str) -> str:
    """Extract token from Authorization header."""
    if auth_header.startswith("Bearer "):
        return auth_header[7:]
    return auth_header


def _validate_token_with_cognito(access_token: str) -> dict:
    """
    Validate token by calling Cognito GetUser API.
    This ensures revoked tokens are rejected immediately.
    """
    try:
        response = cognito_client.get_user(AccessToken=access_token)
        
        user_info = {"username": response["Username"]}
        for attr in response["UserAttributes"]:
            if attr["Name"] == "sub":
                user_info["user_id"] = attr["Value"]
            elif attr["Name"] == "email":
                user_info["email"] = attr["Value"]
        
        return user_info
    except cognito_client.exceptions.NotAuthorizedException:
        raise ValueError("Token is invalid or revoked")
    except Exception as e:
        logger.error(f"Cognito validation error: {e}")
        raise ValueError("Token validation failed")


def _get_user_groups(username: str) -> list:
    """Get user's Cognito groups."""
    try:
        response = cognito_client.admin_list_groups_for_user(
            Username=username,
            UserPoolId=USER_POOL_ID,
        )
        return [group["GroupName"] for group in response["Groups"]]
    except Exception as e:
        logger.error(f"Failed to get user groups: {e}")
        return []


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
    """Convert specific method ARN to wildcard."""
    parts = method_arn.split("/")
    return f"{parts[0]}/*"


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Authorizer handler that checks if user has admin role.
    Validates token against Cognito to ensure revoked tokens are rejected.
    
    Returns Allow policy if user is admin, Deny otherwise.
    """
    try:
        token = event.get("authorizationToken", "")
        method_arn = event.get("methodArn", "")
        
        if not token:
            logger.warning("No authorization token provided")
            raise Exception("Unauthorized")
        
        access_token = _extract_token(token)
        
        user_info = _validate_token_with_cognito(access_token)
        
        username = user_info.get("username", "unknown")
        user_id = user_info.get("user_id", "unknown")
        
        groups = _get_user_groups(username)
        
        logger.info(f"Authorizing user: {username}, groups: {groups}")
        
        # Check if user is admin
        if "admin" not in groups:
            logger.warning(f"User {username} is not admin, denying access")
            return _generate_policy(
                principal_id=user_id,
                effect="Deny",
                resource=method_arn,
            )
        
        logger.info(f"User {username} is admin, allowing access")
        
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
