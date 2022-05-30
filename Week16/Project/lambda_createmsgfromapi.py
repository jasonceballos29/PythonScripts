# Authored by Jason Ceballos
# 05-23-22

import os
import json
import boto3
import datetime


# Create SQS client
sqs_client = boto3.client('sqs')
current_time = datetime.datetime.now()
QUEUE_NAME = os.environ['QUEUE_NAME']
QUEUE_URL = os.environ['QUEUE_URL']

def lambda_handler(event, context):
    
    Records = event.keys()
    response = sqs_client.send_message(
    QueueUrl= QUEUE_URL,
    DelaySeconds=3,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'Test Message from Jason Ceballos'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'Jason Ceballos'
        },
        'WeeksIn': {
            'DataType': 'Number',
            'StringValue': '16'
        }
    },
    MessageBody=(
        'API Gateway access Notification from AWS Lambda function.'
        'Week 16 Project. Thank you!'
    )
)
    #print(event.keys())
    #print(current_time)
    #print(Records)
    print(response)
  
    #for k, v in event.items():
    #    print(k, v)
    #print(response)
    