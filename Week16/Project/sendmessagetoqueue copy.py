# Authored by Jason Ceballos
# 05-23-22

#Modify the Lambda to send a message to the SQS queue. Your message should contain either the current time or a random number. You can use the built-in test function for testing.
#Created custom IAM role with standard Lambda permissions as well as full SQS permissions to write messages.

import json
import os
import datetime

import boto3

QUEUE_NAME = os.environ['QUEUE_NAME']
QUEUE_URL = os.environ['QUEUE_URL']

# Create SQS client
sqs_client = boto3.client('sqs')
current_time = datetime.datetime.now()


def lambda_handler(event, context):
    
    # Get the queue
    #queue = sqs_client.get_queue_by_name(QueueName='QUEUE_NAME')
    queue = sqs_client.get_queue_url(QueueName='SQSQueue')
    
    # Create a new message
    response = queue.send_message(MessageBody='The current time is:')
    
    # Get the message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))
