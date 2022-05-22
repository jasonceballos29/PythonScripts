import boto3
import csv

def lambda_handler(event, context):
    region='us-east-1'
    recList=[]
    try:            
        s3=boto3.client('s3')            
        dyndb = boto3.client('dynamodb', region_name=region)
        confile= s3.get_object(Bucket='my-bucket', Key='employee.csv')
        recList = confile['Body'].read().split('\n')
        firstrecord=True
        csv_reader = csv.reader(recList, delimiter=',', quotechar='"')
        for row in csv_reader:
            if (firstrecord):
                firstrecord=False
                continue
            empid = row[0]
            name = row[1].replace(',','').replace('$','') if row[1] else '-'
            salary = row[2].replace(',','').replace('$','') if row[2] else 0
            response = dyndb.put_item(
                TableName='emplist',
                Item={
                'empid' : {'N':str(empid)},
                'name': {'S':name},
                'salary': {'N':str(salary)},
                'parttime': {'BOOL':False},
                }
            )
        print('Put succeeded:')
    except Exception, e:
        print (str(e))