import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = 'Students'  # Change this to your DynamoDB table name
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    # Parse student data from POST request body
    body = json.loads(event['body'])
    name = body['name']
    age = body['age']
    email = body['email']
    country = body['country']

    # Insert data into DynamoDB
    table.put_item(
        Item={
            'email': email,  # Assuming email is the primary key for the table
            'name': name,
            'age': age,
            'country': country
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Student signed up successfully'),
        'headers': {
            'Access-Control-Allow-Origin': '*',  # Ensure CORS is enabled for frontend domain
            'Content-Type': 'application/json'
        }
    }
