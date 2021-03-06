import json
import boto3

ec2client = boto3.client('ec2')
snsclient = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    
    ec2_instance_id=event['detail']['instance-id']
    
    response = ec2client.describe_tags(
    Filters=[
        {
            'Name': 'resource-id',
            'Values': [ec2_instance_id]
        }
        ]
                                    )
    
    print(response)
    
    alltags=response['Tags']
    
    flag='STOP'
    for item in alltags:
        print(item['Key'])
        if item['Key']=='SPECIAL_EXCEPTION':
            flag='DONT_STOP'
            break
        
    print(flag)    
    
    #Decision Making
    
    if flag=='STOP':
        #Stop EC2
        response = ec2client.stop_instances(InstanceIds=[ec2_instance_id])
    
        
        #Send threatening email
        snsarn='arn:aws:sns:us-east-1:254452634027:Default_CloudWatch_Alarms_Topic'
        errormsg= "EC2 " + ec2_instance_id + " Stopped"
        snsresponse = snsclient.publish(TopicArn=snsarn,
                                    Message=errormsg,
                                    Subject='EC2 Violated Company Policy!! Manager will be Notified!!',
                                    )

    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    