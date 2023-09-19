import boto3
import json

def lambda_trigger(event, context):
    # Extract relevant information from the S3 event trigger
    S3bucket_name = event['Records'][0]['s3']['bucket']['name']
    bucket_object = event['Records'][0]['s3']['object']['key']

    # we will be uploading a file to perform desired operations
    print(f"File '{bucket_object}' was uploaded to bucket '{s3bucket_name}'")

    # Example: this file is used to send notifications using message
    sns_client = boto3.client('sns')
    topic_arn = 'arn:aws:sns:us-east-1:<account-id>:s3-lambda-sns'
    
    sns_client.publish(
       TopicArn=topic_arn,
       Subject='S3 Object Created',
       Message=f"File '{bucket_object}' was uploaded to bucket '{s3bucket_name}'"
    )

   )

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda function executed successfully')
    }

