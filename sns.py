import json 
import boto3 

message = {"foo": "bar"} 

client = boto3.client('sns') 

arn = 'arn:aws:sns:us-east-1:844217490626:NotifyMe'

response = client.publish( TargetArn=arn, Message=json.dumps({'default': 
json.dumps(message)}), MessageStructure='json' )
