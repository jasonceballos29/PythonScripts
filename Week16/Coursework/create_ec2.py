import boto3
ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageID='ami-02042030c439f33e3',
    InstanceType='t2.micro',
    KeyName='us-east-1',
    Mincount=1,
    Maxcount=1
)


response 
#This shoudl spin up an instance and verify it in the console to see it spun up.