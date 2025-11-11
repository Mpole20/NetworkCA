variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "my-webapp"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "production"
}