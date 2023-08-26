import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'Students'  # Change this to your DynamoDB table name
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Fetch all students from DynamoDB
    response = table.scan()
    
    # Extract the 'Items' list from the response
    students = response['Items']
    
    return {
        'statusCode': 200,
        'body': json.dumps(students),
        'headers': {
            'Access-Control-Allow-Origin': '*',  # Ensure CORS is enabled for frontend domain
            'Content-Type': 'application/json'
        }
    }
