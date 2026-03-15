import os
import uuid
from datetime import datetime
from decimal import Decimal

import boto3
from botocore.exceptions import ClientError

from custom_exceptions import BadRequestError, UnauthorizedError, NotFoundError, ConflictError

cognito_client = boto3.client("cognito-idp")
dynamodb = boto3.resource("dynamodb")

USER_POOL_ID = os.environ.get("USER_POOL_ID")
CLIENT_ID = os.environ.get("CLIENT_ID")
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")


def admin_login(username: str, password: str) -> dict:
    try:
        response = cognito_client.initiate_auth(
            ClientId=CLIENT_ID,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": username,
                "PASSWORD": password,
            },
        )
        
        if "ChallengeName" in response:
            return {
                "challenge": response["ChallengeName"],
                "session": response["Session"],
                "username": username,
            }
        
        return {
            "access_token": response["AuthenticationResult"]["AccessToken"],
            "id_token": response["AuthenticationResult"]["IdToken"],
            "refresh_token": response["AuthenticationResult"]["RefreshToken"],
            "token_type": response["AuthenticationResult"]["TokenType"],
            "expires_in": response["AuthenticationResult"]["ExpiresIn"],
        }
    except cognito_client.exceptions.NotAuthorizedException:
        raise UnauthorizedError("Invalid username or password")
    except cognito_client.exceptions.UserNotFoundException:
        raise NotFoundError("User not found")
    except ClientError as e:
        raise BadRequestError(f"Authentication failed: {e.response['Error']['Message']}")


def _generate_username_from_email(email: str) -> str:
    local_part = email.split("@")[0]
    short_uuid = str(uuid.uuid4())[:8]
    return f"{local_part}_{short_uuid}"


def create_user_by_admin(email: str, created_by: str) -> dict:
    try:
        username = _generate_username_from_email(email)
        
        response = cognito_client.admin_create_user(
            UserPoolId=USER_POOL_ID,
            Username=username,
            UserAttributes=[
                {"Name": "email", "Value": email},
                {"Name": "email_verified", "Value": "true"},
            ],
            DesiredDeliveryMediums=["EMAIL"],
        )
        
        user_sub = None
        for attr in response["User"]["Attributes"]:
            if attr["Name"] == "sub":
                user_sub = attr["Value"]
                break
        
        add_user_to_group(username, "user")
        
        user_data = {
            "user_id": user_sub,
            "username": username,
            "email": email,
            "role": "user",
            "created_by": created_by,
            "created_at": datetime.utcnow().isoformat(),
        }
        save_user_to_dynamodb(user_data)
        
        return user_data
    except cognito_client.exceptions.UsernameExistsException:
        raise ConflictError(f"User with email {email} already exists")
    except ClientError as e:
        raise BadRequestError(f"Failed to create user: {e.response['Error']['Message']}")


def add_user_to_group(username: str, group_name: str) -> dict:
    try:
        cognito_client.admin_add_user_to_group(
            UserPoolId=USER_POOL_ID,
            Username=username,
            GroupName=group_name,
        )
        return {"username": username, "group": group_name}
    except cognito_client.exceptions.UserNotFoundException:
        raise NotFoundError(f"User {username} not found")
    except cognito_client.exceptions.ResourceNotFoundException:
        raise NotFoundError(f"Group {group_name} not found")
    except ClientError as e:
        raise BadRequestError(f"Failed to add user to group: {e.response['Error']['Message']}")


def save_user_to_dynamodb(user_data: dict) -> dict:
    table = dynamodb.Table(DYNAMODB_TABLE)
    
    item = {
        "user_id": user_data["user_id"],
        "email": user_data["email"],
        "role": user_data["role"],
        "created_by": user_data["created_by"],
        "created_at": user_data["created_at"],
    }
    
    if "username" in user_data:
        item["username"] = user_data["username"]
    
    table.put_item(Item=item)
    return item


def user_login(username: str, password: str) -> dict:
    try:
        response = cognito_client.initiate_auth(
            ClientId=CLIENT_ID,
            AuthFlow="USER_PASSWORD_AUTH",
            AuthParameters={
                "USERNAME": username,
                "PASSWORD": password,
            },
        )
        
        if "ChallengeName" in response:
            return {
                "challenge": response["ChallengeName"],
                "session": response["Session"],
                "username": username,
            }
        
        return {
            "access_token": response["AuthenticationResult"]["AccessToken"],
            "id_token": response["AuthenticationResult"]["IdToken"],
            "refresh_token": response["AuthenticationResult"]["RefreshToken"],
            "token_type": response["AuthenticationResult"]["TokenType"],
            "expires_in": response["AuthenticationResult"]["ExpiresIn"],
        }
    except cognito_client.exceptions.NotAuthorizedException:
        raise UnauthorizedError("Invalid username or password")
    except cognito_client.exceptions.UserNotFoundException:
        raise NotFoundError("User not found")
    except ClientError as e:
        raise BadRequestError(f"Authentication failed: {e.response['Error']['Message']}")


def respond_to_new_password_challenge(session: str, username: str, new_password: str) -> dict:
    try:
        response = cognito_client.respond_to_auth_challenge(
            ClientId=CLIENT_ID,
            ChallengeName="NEW_PASSWORD_REQUIRED",
            Session=session,
            ChallengeResponses={
                "USERNAME": username,
                "NEW_PASSWORD": new_password,
            },
        )
        
        return {
            "access_token": response["AuthenticationResult"]["AccessToken"],
            "id_token": response["AuthenticationResult"]["IdToken"],
            "refresh_token": response["AuthenticationResult"]["RefreshToken"],
            "token_type": response["AuthenticationResult"]["TokenType"],
            "expires_in": response["AuthenticationResult"]["ExpiresIn"],
        }
    except cognito_client.exceptions.InvalidPasswordException as e:
        raise BadRequestError(f"Invalid password: {e.response['Error']['Message']}")
    except cognito_client.exceptions.ExpiredCodeException:
        raise BadRequestError("Session expired, please login again")
    except ClientError as e:
        raise BadRequestError(f"Failed to change password: {e.response['Error']['Message']}")


def get_user_from_token(access_token: str) -> dict:
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
        raise UnauthorizedError("Invalid or expired token")
    except ClientError as e:
        raise BadRequestError(f"Failed to get user: {e.response['Error']['Message']}")


def verify_admin_role(access_token: str) -> dict:
    try:
        user_info = get_user_from_token(access_token)
        
        response = cognito_client.admin_list_groups_for_user(
            Username=user_info["username"],
            UserPoolId=USER_POOL_ID,
        )
        
        groups = [group["GroupName"] for group in response["Groups"]]
        
        if "admin" not in groups:
            raise UnauthorizedError("Admin access required")
        
        user_info["groups"] = groups
        return user_info
    except UnauthorizedError:
        raise
    except ClientError as e:
        raise BadRequestError(f"Failed to verify admin role: {e.response['Error']['Message']}")
