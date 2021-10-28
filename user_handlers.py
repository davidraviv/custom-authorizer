from http import HTTPStatus
import json


def create_user(event, context={}):
    try:
        requestContext = event.get("requestContext", {})
        authorizer_context = requestContext.get("authorizer")
        body = json.loads(event["body"])

        print(f"Handling request to create user {body=} {authorizer_context=}")

        status_code = HTTPStatus.OK
        body = json.dumps(event)

    except Exception as e:
        status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        body = json.dumps({
            "message": e.msg
        })

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        },
        "body": body,
    }
