# Authored by Jason Ceballos
# 05-23-22

#Modify the Lambda to send a message to the SQS queue. Your message should contain either the current time or a random number. You can use the built-in test function for testing.
#Created custom IAM role with standard Lambda permissions as well as SQS permissions to write messages. JSON Below

import json
import boto3
import datetime


# Create SQS client
client = boto3.client('sqs')
current_time = datetime.datetime.now()

print(current_time)

def lambda_handler(event, context):
    # Get the queue
    print(event.keys())

    for k , v in event.items():
        print(k, v)
