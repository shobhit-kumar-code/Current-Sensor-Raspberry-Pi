import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table=dynamodb.Table('globalproject')


response = table.scan()

for x in response['Items']:
    print(float(x['current']),float(x['timestamp']))
    # print(float(x['timestamp']))
