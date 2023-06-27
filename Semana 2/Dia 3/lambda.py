import json
import boto3
from datetime import datetime
client = boto3.client('sqs')


def lambda_handler(event, context):
    # Get the current date & time
    response = "The time and date is: "
    date_time = datetime.now()

    # send sqs message with the current date & time
    message = client.send_message(
        QueueUrl='https://sqs.us-west-2.amazonaws.com/085598268584/week15-sqs-queue',
        MessageBody=("This was sent on: " +
                     str(date_time.strftime('%Y-%m-%d %H:%M:%S')))
    )
    return {
        'statusCode': 200,
        'body': json.dumps(message, indent=2)
    }
https://sqs.us-east-1.amazonaws.com/797844572213/MySQS_Time
arn:aws:sqs:us-east-1:797844572213:MySQS_Time