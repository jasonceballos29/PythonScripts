# Start AWS WorkSpaces Python Script
# Also checks for Specific Tag before shutting down
# Authored by Jason Ceballos
# 04/20/23

import boto3 #import AWS boto3 library
region='us-west-1'
AWSWorkSpaces = boto3.client('workspaces',region_name='region')
a = AWSWorkSpaces.describe_workspaces()


# Filter all running WorkSpaces

workspaces = AWSWorkSpaces.Client.describe_workspaces(Filters=[{'Name': 'State', 'Values': ['STOPPED']}])

# Declared list to store running instances
all_running_workspaces = []
specific_tag = 'MaintenanceWindow'  
for workspace in workspaces:
    
    # store all running WorkSpaces
     all_running_workspaces.append(workspace)
        
    # WorkSpaces with specific tags
     if workspaces.tags != None:
         for tags in workspaces.tags:
             
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