import json
from decimal import Decimal


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)


ALLOWED_ORIGINS = {"http://localhost:3000", "https://d2bed2yjnef4ve.cloudfront.net"}


def createResponse(status_code: int, message: str, data: dict = None, event: dict = None) -> dict:
    body = {
        "statusCode": status_code,
        "status": status_code < 400,
        "message": message,
    }
    
    if data is not None:
        body["data"] = data

    # Determine CORS origin — match request origin against allowed list
    origin = "*"
    if event:
        request_origin = (event.get("headers") or {}).get("origin", "")
        if request_origin in ALLOWED_ORIGINS:
            origin = request_origin

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": origin,
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
            "Access-Control-Allow-Methods": "GET,POST,PUT,DELETE,OPTIONS",
            "Access-Control-Allow-Credentials": "true",
        },
        "body": json.dumps(body, cls=DecimalEncoder),
    }
