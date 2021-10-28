

def handler(event, context):
    try:
        token = event.get('authorizationToken')

        effect = "Allow" if token.lower() == "allow" else "Deny"
        context = {
            "name": "Inigo Montoya"
        }

        return _build_policy(principal_id="user", effect=effect, resource=event['methodArn'], context=context)

    except Exception as e:
        raise Exception('Unauthenticated') from e


def _build_policy(principal_id: str, effect: str, resource: str, context: dict = None) -> dict:
    policy = {
        "principalId": principal_id,
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": resource

                }
            ]
        },
    }
    if context:
        policy["context"] = context

    print(f'{policy=}')
    return policy
