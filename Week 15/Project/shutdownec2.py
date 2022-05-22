# Stop EC2 Instances Python Script
# Also checks for Specific Tag before shutting down
# Authored by Jason Ceballos
# 05/22/22

import boto3 #import AWS boto3 library
region='us-east-1'
instance_state = 'running'
ec2 = boto3.client('ec2', region_name=region)
#ec2 = boto3.resource('ec2',"us-east-1") 

# Filter all running instances

instances = ec2.instances.all(Filters=[{'Name': 'instance-state-name', 'Values': [instance_state]}])

# Declared list to store running instances
all_running_instances = []
specific_tag = 'Dev'  
for instance in instances:
    
    # store all running instances
     all_running_instances.append(instance)
        
    # Instances with specific tags
     if instance.tags != None:
         for tags in instance.tags:
             
            # Instances with tag 'Dev'
             if tags["Key"] == specific_tag:
                
                # Remove instances with specfic tags from all running instances
                 all_running_instances.remove(instance)
                    
#print(all_running_instances)
for specific in all_running_instances:
    print(f'Stopping EC2 instance: {specific.id}')
    specific.wait_until_stopped()
    print(f'EC2 instance "{specific.id}" has been stopped')
    # print(specific)
    # specific.stop()