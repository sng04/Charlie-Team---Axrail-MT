"""Shared response utility for API Gateway Lambda handlers."""

import json
from decimal import Decimal


class _DecimalEncoder(json.JSONEncoder):
    """Encode Decimal values as float for JSON serialization."""

    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super().default(o)


def createResponse(status_code: int, message: str, data=None) -> dict:
    """Build a standard API Gateway response with CORS headers.

    Args:
        status_code: HTTP status code.
        message: Human-readable message.
        data: Optional payload to include in the response body.

    Returns:
        API Gateway proxy response dict.
    """
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS",
        },
        "body": json.dumps(
            {
                "statusCode": status_code,
                "status": status_code < 400,
                "message": message,
                "data": data,
            },
            cls=_DecimalEncoder,
        ),
    }
