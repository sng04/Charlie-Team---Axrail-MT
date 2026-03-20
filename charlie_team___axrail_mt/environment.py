import os

ENVIRONMENTS = {
    "dev": {
        "account": os.getenv("CDK_DEFAULT_ACCOUNT"),
        "region": os.getenv("CDK_DEFAULT_REGION", "ap-southeast-1"),
        "dynamodb_billing": "PAY_PER_REQUEST",
        "lambda_memory": 256,
        "log_retention_days": 7,
        "ses_sender_email": "richiereubenh@gmail.com",
        "admin_email": "admin@axrail.com",
        "admin_temp_password": "TempAdmin@123",
    },
    "staging": {
        "account": os.getenv("CDK_DEFAULT_ACCOUNT"),
        "region": os.getenv("CDK_DEFAULT_REGION", "ap-southeast-1"),
        "dynamodb_billing": "PROVISIONED",
        "lambda_memory": 512,
        "log_retention_days": 30,
        "ses_sender_email": "noreply@axrail.com",
        "admin_email": "admin@axrail.com",
        "admin_temp_password": "TempAdmin@123",
    },
    "prod": {
        "account": os.getenv("CDK_DEFAULT_ACCOUNT"),
        "region": os.getenv("CDK_DEFAULT_REGION", "ap-southeast-1"),
        "dynamodb_billing": "PROVISIONED",
        "lambda_memory": 1024,
        "log_retention_days": 90,
        "ses_sender_email": "noreply@axrail.com",
        "admin_email": "admin@axrail.com",
        "admin_temp_password": "TempAdmin@123",
    },
}


def get_environment(env_name: str) -> dict:
    return ENVIRONMENTS.get(env_name, ENVIRONMENTS["dev"])
