# NetworkCA 
Brief overview of Automated Cloud Deployment Pipeline

File Structure:

<img width="359" height="572" alt="{97ED4552-1933-41A3-AD57-59F85ADE9D43}" src="https://github.com/user-attachments/assets/745d015e-66bf-44c6-8a28-d765cf398512" />

Components:
-AWS ECS
-Application Load Balancer
-AWS ECR
-Terraform
-GitHub Actions
-CloudWatch


Whats needed:
AWS account, with secret keys generated
Github account

1. AWS Credentials Setup

Create the following secrets in your GitHub repository:
-AWS_ACCESS_KEY_ID
-AWS_SECRET_ACCESS_KEY

2. Manual Infrastructure Deployment (First Time)

bash
cd infrastructure
terraform init
terraform plan
terraform apply

After the initial setup, when you need to update your app you run these commands in root folder /NetworkCA
git add .
git commit -m "Example push" 
git push

After these commands are run the app gets updated automatically and with no downtime.

