import json

print('Loading function')

def lambda_handler(event, context):
    #1. Parse out query string params
    transactionId = event['queryStringParameters']['transactionID']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print('transactionId=', transactionId)
    print('transactionType', transactionType)
    print('transactionAmount', transactionAmount)

    #2. Construct the body of the response object
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = 'Hello From Lambda land'

    #3. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse) #converter object in to string 

    #4. Return the response object
    return responseObject

#Api Gateway -> arn:aws:lambda:us-east-1:797844572213:function:TransactionProcessor
#https://n1kg8q96yc.execute-api.us-east-1.amazonaws.com/teste/transactions?transactionId=5&type=PURCHASE&amount=500
#https://rwljxg42n6.execute-api.sa-east-1.amazonaws.com/teste/transactions?transactionId=5&type=PURCHASE&amount=500
#Retorno -> {"statusCode": 200, "body": "\"Hello from Lambda!\""}x
