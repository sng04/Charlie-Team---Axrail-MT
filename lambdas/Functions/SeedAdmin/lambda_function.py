import os
import json
from datetime import datetime

import boto3
from botocore.exceptions import ClientError

cognito_client = boto3.client("cognito-idp")
dynamodb = boto3.resource("dynamodb")

USER_POOL_ID = os.environ.get("USER_POOL_ID")
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")
ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
ADMIN_TEMP_PASSWORD = os.environ.get("ADMIN_TEMP_PASSWORD")


def lambda_handler(event, context):
    print(f"Event: {json.dumps(event)}")
    print(f"USER_POOL_ID: {USER_POOL_ID}")
    print(f"DYNAMODB_TABLE: {DYNAMODB_TABLE}")
    print(f"ADMIN_EMAIL: {ADMIN_EMAIL}")
    
    request_type = event.get("RequestType", "Create")
    print(f"RequestType: {request_type}")
    
    if request_type == "Delete":
        return {"Status": "SUCCESS", "PhysicalResourceId": "seed-admin"}
    
    try:
        print("Creating admin user in Cognito...")
        response = cognito_client.admin_create_user(
            UserPoolId=USER_POOL_ID,
            Username="admin",
            UserAttributes=[
                {"Name": "email", "Value": ADMIN_EMAIL},
                {"Name": "email_verified", "Value": "true"},
            ],
            TemporaryPassword=ADMIN_TEMP_PASSWORD,
            MessageAction="SUPPRESS",
        )
        print(f"Cognito response: {json.dumps(response, default=str)}")
        
        user_sub = None
        for attr in response["User"]["Attributes"]:
            if attr["Name"] == "sub":
                user_sub = attr["Value"]
                break
        print(f"User sub: {user_sub}")
        
        print("Adding user to admin group...")
        cognito_client.admin_add_user_to_group(
            UserPoolId=USER_POOL_ID,
            Username="admin",
            GroupName="admin",
        )
        print("User added to admin group")
        
        print("Saving to DynamoDB...")
        table = dynamodb.Table(DYNAMODB_TABLE)
        table.put_item(
            Item={
                "user_id": user_sub,
                "email": ADMIN_EMAIL,
                "role": "admin",
                "created_by": "system",
                "created_at": datetime.utcnow().isoformat(),
            }
        )
        print("Saved to DynamoDB")
        
        return {
            "Status": "SUCCESS",
            "PhysicalResourceId": "seed-admin",
            "Data": {"AdminEmail": ADMIN_EMAIL},
        }
    except cognito_client.exceptions.UsernameExistsException:
        print("Admin already exists")
        return {
            "Status": "SUCCESS",
            "PhysicalResourceId": "seed-admin",
            "Data": {"Message": "Admin already exists"},
        }
    except ClientError as e:
        print(f"Error: {str(e)}")
        return {
            "Status": "FAILED",
            "PhysicalResourceId": "seed-admin",
            "Reason": str(e),
        }
