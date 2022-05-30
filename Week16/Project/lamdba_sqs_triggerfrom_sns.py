# Authored by Jason Ceballos
# 05-23-22

# ADVANCED:
# 1) Create a SNS topic using Python.
# 2) Use an email to subscribe to the SNS topic.
# 3) Create a Lambda function with a Python 3.7 or higher runtime 
# 4) Modify the Lambda to trigger when new messages arrive in the SQS queue you created earlier.
# 5) The Lambda should publish the SQS message that triggered it to the SNS topic.
# 6) Validate the entire architecture works by triggering the API you created earlier. You should receive the notification from the SNS subscription.

import os
import json
import boto3
import datetime


# Create SQS client
client = boto3.client('sqs')
sns = boto3.client('sns')
current_time = datetime.datetime.now()
QUEUE_NAME = os.environ['QUEUE_NAME']
QUEUE_URL = os.environ['QUEUE_URL']

def lambda_handler(event, context):
    print(current_time)
    Records = event.keys()
    response = client.receive_message(
    QueueUrl=QUEUE_URL,
    AttributeNames=[
        'All'
    ]
)
    print(response)
    message = Records
    snsresponse = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:254452634027:lambda_sns_trigger',
        Message='string',
        Subject='New SQS Queue Message from SQSQueue',
        
        )