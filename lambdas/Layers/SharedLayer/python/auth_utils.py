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

# Account lockout settings
MAX_FAILED_ATTEMPTS = 3
LOCKOUT_DURATION_MINUTES = 30


def _get_users_table():
    return dynamodb.Table(DYNAMODB_TABLE)


def _check_account_lockout(username: str) -> None:
    """Check if the account is locked due to failed login attempts.

    Raises UnauthorizedError if locked.
    """
    try:
        from boto3.dynamodb.conditions import Attr

        table = _get_users_table()
        resp = table.scan(
            FilterExpression=Attr("username").eq(username) | Attr("email").eq(username),
            ProjectionExpression="user_id, failed_login_attempts, locked_until",
        )
        items = resp.get("Items", [])
        if not items:
            return

        user = items[0]
        locked_until = user.get("locked_until", "")

        if locked_until:
            from datetime import timezone
            lock_time = datetime.fromisoformat(locked_until.replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            if now < lock_time:
                remaining = int((lock_time - now).total_seconds() // 60) + 1
                raise UnauthorizedError(
                    f"Account locked due to too many failed attempts. Try again in {remaining} minutes."
                )
            # Lock expired — reset
            table.update_item(
                Key={"user_id": user["user_id"]},
                UpdateExpression="SET failed_login_attempts = :z REMOVE locked_until",
                ExpressionAttributeValues={":z": 0},
            )
    except UnauthorizedError:
        raise
    except Exception:
        pass


def _record_failed_login(username: str) -> None:
    """Increment failed login counter and lock account if threshold reached."""
    try:
        from boto3.dynamodb.conditions import Attr
        from datetime import timedelta, timezone

        table = _get_users_table()
        resp = table.scan(
            FilterExpression=Attr("username").eq(username) | Attr("email").eq(username),
            ProjectionExpression="user_id, failed_login_attempts",
        )
        items = resp.get("Items", [])
        if not items:
            return

        user = items[0]
        new_count = int(user.get("failed_login_attempts", 0)) + 1

        if new_count >= MAX_FAILED_ATTEMPTS:
            locked_until = (datetime.now(timezone.utc) + timedelta(minutes=LOCKOUT_DURATION_MINUTES)).isoformat()
            table.update_item(
                Key={"user_id": user["user_id"]},
                UpdateExpression="SET failed_login_attempts = :c, locked_until = :l",
                ExpressionAttributeValues={":c": new_count, ":l": locked_until},
            )
        else:
            table.update_item(
                Key={"user_id": user["user_id"]},
                UpdateExpression="SET failed_login_attempts = :c",
                ExpressionAttributeValues={":c": new_count},
            )
    except Exception:
        pass


def _reset_failed_login(username: str) -> None:
    """Reset failed login counter on successful login."""
    try:
        from boto3.dynamodb.conditions import Attr

        table = _get_users_table()
        resp = table.scan(
            FilterExpression=Attr("username").eq(username) | Attr("email").eq(username),
            ProjectionExpression="user_id, failed_login_attempts, locked_until",
        )
        items = resp.get("Items", [])
        if not items:
            return

        user = items[0]
        if int(user.get("failed_login_attempts", 0)) > 0 or user.get("locked_until"):
            table.update_item(
                Key={"user_id": user["user_id"]},
                UpdateExpression="SET failed_login_attempts = :z REMOVE locked_until",
                ExpressionAttributeValues={":z": 0},
            )
    except Exception:
        pass


def admin_login(username: str, password: str) -> dict:
    _check_account_lockout(username)
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
        
        _reset_failed_login(username)
        return {
            "access_token": response["AuthenticationResult"]["AccessToken"],
            "id_token": response["AuthenticationResult"]["IdToken"],
            "refresh_token": response["AuthenticationResult"]["RefreshToken"],
            "token_type": response["AuthenticationResult"]["TokenType"],
            "expires_in": response["AuthenticationResult"]["ExpiresIn"],
        }
    except cognito_client.exceptions.NotAuthorizedException:
        _record_failed_login(username)
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
    _check_account_lockout(username)
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
        
        _reset_failed_login(username)
        return {
            "access_token": response["AuthenticationResult"]["AccessToken"],
            "id_token": response["AuthenticationResult"]["IdToken"],
            "refresh_token": response["AuthenticationResult"]["RefreshToken"],
            "token_type": response["AuthenticationResult"]["TokenType"],
            "expires_in": response["AuthenticationResult"]["ExpiresIn"],
        }
    except cognito_client.exceptions.NotAuthorizedException:
        _record_failed_login(username)
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


def logout_user(access_token: str) -> None:
    """Invalidate user's Cognito tokens using global sign out."""
    try:
        cognito_client.global_sign_out(AccessToken=access_token)
    except cognito_client.exceptions.NotAuthorizedException:
        raise UnauthorizedError("Invalid or expired token")
    except ClientError as e:
        raise BadRequestError(f"Failed to logout: {e.response['Error']['Message']}")
