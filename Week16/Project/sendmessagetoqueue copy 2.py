# Authored by Jason Ceballos
# 05-23-22

#Modify the Lambda to send a message to the SQS queue. Your message should contain either the current time or a random number. You can use the built-in test function for testing.
#Created custom IAM role with standard Lambda permissions as well as SQS permissions to write messages. JSON Below

import os
import json
import boto3
import datetime

QUEUE_NAME = os.environ['QUEUE_NAME']
QUEUE_URL = os.environ['QUEUE_URL']


# Create SQS client
client = boto3.client('sqs')
current_time = datetime.datetime.now()

print(current_time)

def lambda_handler(event, context):
    # Get the event information to send to the queue
    print(event.keys())
    
    for k , v in event.items():
        print(k, v)
        
   # Get the queue
    #queue = sqs_client.get_queue_by_name(QueueName='QUEUE_NAME')
    queue = client.get_queue_url(QueueName='SQSQueue')
    
    # Send message to SQS queue
    response = client.send_message(
    QueueUrl = queue,
    DelaySeconds=10,
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
  
   
    
