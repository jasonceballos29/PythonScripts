# Authored by Jason Ceballos
# 05-23-22

#Modify the Lambda to send a message to the SQS queue. Your message should contain either the current time or a random number. You can use the built-in test function for testing.
#Created custom IAM role with standard Lambda permissions as well as SQS permissions to write messages. JSON Below

import os
import json
import boto3
import datetime


# Create SQS client
sqs_client = boto3.client('sqs')
current_time = datetime.datetime.now()
QUEUE_NAME = os.environ['QUEUE_NAME']
QUEUE_URL = os.environ['QUEUE_URL']

print(current_time)

def lambda_handler(event, context):
    #res = sqs_client.get_queue_url(QueueName=QUEUE_NAME)
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
        'This is a test message from Jason Ceballos.'
        'Week 16 Project. Thank you!'
    )
)
