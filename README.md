## Simple serverless architectures and usecase

### 3-tier-architecture
1. Deploy backend create API Gateway (Lambda, DynamoDB, IAM, API Gateway)
2. Fill the API endpoint in the HTML file
3. Launch EC2 with userdata
4. Deploy the html file via ssh
5. Test the whole flow (Note: To put emails working with +1 sequence)



### s3-event-driven
1. Deploy the infra manually (S3 bucket, lambda, iam)
2. Create S3 Object Upload Events to trigger Lambda events
3. Create SES to send emails
4. Upload files in S3 to trigger emails for students in the DynamoDB