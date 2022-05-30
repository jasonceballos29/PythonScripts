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


def lambda_handler(event, context):
    print(current_time)    
    response = sqs_client.send_message(
    QueueUrl= QUEUE_URL,
    MessageAttributes={
        'Title': {
            'DataType': 'String',
            'StringValue': 'Visit from API Endpoint Logged'
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
        'Access of external API Endpoint detected.'
        'Week 16 Project. Thank you!'
    )
)
    #print(response)