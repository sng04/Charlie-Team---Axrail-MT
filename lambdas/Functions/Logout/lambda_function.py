"""
Logout Lambda Function

Invalidates user's Cognito tokens using global sign out.
Works for both admin and user roles.
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse

logger = Logger()
tracer = Tracer()

cognito_client = boto3.client("cognito-idp")


def _get_access_token(event: dict) -> str:
    """Extract access token from Authorization header."""
    headers = event.get("headers") or {}
    auth_header = headers.get("Authorization") or headers.get("authorization", "")
    
    if auth_header.startswith("Bearer "):
        return auth_header[7:]
    return auth_header


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        access_token = _get_access_token(event)
        
        if not access_token:
            return createResponse(400, "Access token is required")
        
        cognito_client.global_sign_out(AccessToken=access_token)
        
        logger.info("User logged out successfully")
        return createResponse(200, "Logged out successfully")
        
    except cognito_client.exceptions.NotAuthorizedException:
        logger.warning("Invalid or expired token")
        return createResponse(401, "Invalid or expired token")
    except ClientError as e:
        logger.exception(f"Cognito error: {e}")
        return createResponse(500, "Failed to logout")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
