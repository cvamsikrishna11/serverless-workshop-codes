# Note: Fill SENDER_EMAIL by creating the SES sender email in AWS console
import json
import boto3

# Initialize S3, SES, and DynamoDB clients
s3 = boto3.client('s3')
ses = boto3.client('ses')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentsDryRun')

# Email details
SENDER_EMAIL = ""
AWS_REGION = "us-east-1"
SUBJECT = "Exciting Course Offers Just for Today!"

def lambda_handler(event, context):
    # Extract bucket and key details from the S3 PUT event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print(f"Reading file from Bucket: {bucket}, Key: {key}")

    # Fetch the uploaded JSON file from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    file_content = response['Body'].read().decode('utf-8')
    courses = json.loads(file_content)

    # Convert the JSON content into more visually appealing HTML
    html_content = """
    <style>
        /*... same style as before ...*/
    </style>
    <h2>🎉 Today's Exclusive Course Offers 🎉</h2>
    <p>Great news! We've slashed the prices on some of our most popular courses. Don't miss out on these amazing offers. Enroll today and accelerate your learning journey!</p>
    <table>
        <tr><th>Name</th><th>Original Price</th><th>Today's Discounted Price</th><th>Link</th></tr>
    """
    for course in courses:
        html_content += f"<tr><td>{course['name']}</td><td><strike>${course['actualPrice']}</strike></td><td>${course['discountedPrice']}</td><td><a href='{course['URL']}'>Go to Course</a></td></tr>"
    html_content += "</table>"
    html_content += "<p>Hurry, these offers won't last long! 🚀</p>"

    print("Converted courses data to HTML content")

    # Fetch all students' emails from DynamoDB
    response = table.scan(ProjectionExpression='email')
    emails = [item['email'] for item in response['Items']]
    print(f"Found {len(emails)} email addresses in the DynamoDB table.")

    # Send email to each student using SES
    for email in emails:
        ses.send_email(
            Source=SENDER_EMAIL,
            Destination={
                'ToAddresses': [email],
            },
            Message={
                'Subject': {
                    'Data': SUBJECT,
                },
                'Body': {
                    'Html': {
                        'Data': html_content
                    }
                }
            }
        )
        print(f"Email sent to {email}")

    return {
        'statusCode': 200,
        'body': json.dumps('Emails sent successfully!')
    }
