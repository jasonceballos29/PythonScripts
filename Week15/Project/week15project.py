#!/usr/bin/env python3

# Stop EC2 Instances Python Script
# Also checks for Specific Tag before shutting down
# Authored by Jason Ceballos
# 05/22/22

#import AWS boto3 library
import boto3

#Connect with Boto3 client calling EC2 Service
client=boto3.client('ec2')

#Filter on any instances with the tag of 'Dev' and running
# resp=client.describe_instances(Filters=[{'Name': 'tag:Name', 
# 'Values': ['Dev']}])
resp=client.describe_instances(Filters=[{
    'Name': 'instance-state-name',
    'Values': ['running'] ,
    'Name': 'tag:Name',
    'Values': ['Dev']}])

#For loop appending this filtered list to the variable newlist
newlist=[]

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
            newlist.append(instance['InstanceId'])
            
#Print the output of this list for any instances that met this criteria. Then terminate them and display the instance ID for the user
print(newlist)
print(client.terminate_instances(InstanceIds=(newlist)))

