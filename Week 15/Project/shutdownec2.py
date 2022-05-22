import sys
import boto3

# Boto3
# Use the filter() method of the instances collection to retrieve
# all running EC2 instances.
response = client.stop_instances(
    InstanceIds=[
        'string',
    ],
    Hibernate=True|False,
    DryRun=True|False,
    Force=True|False
)