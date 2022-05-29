# Authored by Jason Ceballos
# 05-23-22

#Modify the Lambda to send a message to the SQS queue. Your message should contain either the current time or a random number. You can use the built-in test function for testing.
#Created custom IAM role with standard Lambda permissions as well as SQS permissions to write messages. JSON Below


import json
import boto3
import datetime


# Create SQS client
sqs_client = boto3.client('sqs')
current_time = datetime.datetime.now()

print(current_time)

def lambda_handler(event, context):
    # Get the queue
    #queue = sqs_client.get_queue_by_name(QueueName='SQSQueue')
    res = sqs_client.get_queue_url(QueueName='SQSQueue')
    
    # Create a new message
    # Send message to SQS queue
    response = res.send_message(
    QueueUrl=res,
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

    # Print the current date and time then get the message ID and MD5
   
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))
