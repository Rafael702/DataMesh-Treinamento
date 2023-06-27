from __future__ import print_function

import json
import urllib
import boto3
import datetime

print('Loading function')


def process_purchase(message, context):

    # Input Example
    # { 'TransactionType': 'PURCHASE'}

    # 1. Log input message
    print("Received message from Step Functions: ")
    print(message)

    #2. Construct response object
    response = {}
    response['TransactionType'] = message['TransactionType']
    # Carimbo do Lambda
    response['Timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    response['Message'] = 'Hello from lambda land inside the ProcessPurchase function'

    return response