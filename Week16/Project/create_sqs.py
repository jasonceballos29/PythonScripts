# 1) Create a Standard SQS Queue using Python.

import boto3
import json

AWS_REGION = "us-east-1"

sqs_client = boto3.client("sqs", region_name=AWS_REGION)

response = sqs_client.create_queue(
    QueueName='SQSQueue',
    Attributes={
        'DelaySeconds': '0',
    },
    tags={
        'CreatedBy': 'Jason Ceballos'
    }
)
urlresponse = sqs_client.get_queue_url(QueueName='SQSQueue', QueueOwnerAWSAccountId='12345678910111')

print("The Queue URL is", urlresponse)

# 2) Create a Lambda function in the console with a Python 3.7 or higher runtime
#Lamdba named "SQSQueue" in my AWS Account
# 3) Modify the Lambda to send a message to the SQS queue. Your message should contain either the current time or a random number. You can use the built-in test function for testing.

# 4) Create an API gateway HTTP API type trigger.
# 5) Test the trigger to verify the message was sent.