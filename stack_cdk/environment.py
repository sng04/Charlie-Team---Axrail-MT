import os

from aws_cdk import RemovalPolicy

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
        # DynamoDB lifecycle
        "removal_policy": RemovalPolicy.DESTROY,
        "point_in_time_recovery": False,
        # OpenSearch config
        "opensearch_instance_type": "t3.small.search",
        "opensearch_data_nodes": 1,
        "opensearch_ebs_volume_size": 20,
        # Bedrock config
        "bedrock_region": "us-east-1",
        "embedding_model_id": "amazon.titan-embed-text-v2:0",
        "llm_model_id": "amazon.nova-pro-v1:0",
        # AI Lambda config
        "strands_agent_memory": 512,
        "strands_agent_timeout": 120,
        "ingestion_memory": 512,
        "gap_scheduler_rate": "rate(5 minutes)",
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
        # DynamoDB lifecycle
        "removal_policy": RemovalPolicy.RETAIN,
        "point_in_time_recovery": True,
        # OpenSearch config
        "opensearch_instance_type": "t3.medium.search",
        "opensearch_data_nodes": 2,
        "opensearch_ebs_volume_size": 50,
        # Bedrock config
        "bedrock_region": "us-east-1",
        "embedding_model_id": "amazon.titan-embed-text-v2:0",
        "llm_model_id": "amazon.nova-pro-v1:0",
        # AI Lambda config
        "strands_agent_memory": 512,
        "strands_agent_timeout": 120,
        "ingestion_memory": 512,
        "gap_scheduler_rate": "rate(5 minutes)",
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
        # DynamoDB lifecycle
        "removal_policy": RemovalPolicy.RETAIN,
        "point_in_time_recovery": True,
        # OpenSearch config
        "opensearch_instance_type": "r6g.xlarge.search",
        "opensearch_data_nodes": 3,
        "opensearch_ebs_volume_size": 100,
        # Bedrock config
        "bedrock_region": "us-east-1",
        "embedding_model_id": "amazon.titan-embed-text-v2:0",
        "llm_model_id": "amazon.nova-pro-v1:0",
        # AI Lambda config
        "strands_agent_memory": 1024,
        "strands_agent_timeout": 120,
        "ingestion_memory": 1024,
        "gap_scheduler_rate": "rate(5 minutes)",
    },
}


def get_environment(env_name: str) -> dict:
    return ENVIRONMENTS.get(env_name, ENVIRONMENTS["dev"])
