## Simple serverless architectures and usecase

### 3-tier-architecture
1. Deploy backend create API Gateway (Lambda, DynamoDB, IAM, API Gateway)
2. Fill the API endpoint in the HTML file
3. Launch EC2 with userdata
4. Deploy the html file via ssh and test the whole flow



### s3-event-driven
1. Deploy the infra manually (s3, lambda, iam)
2. Create SES to send emails
3. Upload files in S3 to trigger emails for students in the DynamoDB