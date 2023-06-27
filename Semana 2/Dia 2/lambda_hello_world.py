import json

def lambda_handler(event, context):

    body = {
        "Message": "Hello World"
    }

    response = {
        "statusCode" : 200,
        "body" : json.dumps(body)
    }

    return response
