# Cloud Mastery Journey

A structured hands-on learning journey toward becoming a DevOps and MLOps Cloud Engineer.

**Author:** Ahmed (@aofouad-dev)
**Track:** DevOps and Cloud Engineering + Data and ML on Cloud
**Internship:** National Telecommunication Institute of Egypt -- AWS
**Started:** March 2026

---

## Roadmap Overview

| Phase | Focus | Duration | Status |
|---|---|---|---|
| Phase 1 | Linux, Python, Git, AWS CLI, Boto3, AWS Core Services | 2-3 months | In Progress |
| Phase 2 | Docker, CI/CD, Terraform, AWS Deep Dive | 3-4 months | Upcoming |
| Phase 3 | ML Basics, SageMaker, MLOps | 3-4 months | Upcoming |
| Phase 4 | Certifications and Job Prep | Ongoing | Upcoming |

---

## Repository Structure

Each file is a real hands-on session with actual AWS services using Python and Boto3.

- notes.txt                -- Day 1 - First Linux notes
- hello_cloud.py           -- Day 2 - First Python script
- list_s3.py               -- Day 3 - First AWS automation (S3 listing)
- s3_operations.py         -- Day 4 - S3 inspection and operations
- ec2_explore.py           -- Day 5 - EC2 and VPC exploration
- vpc_explore.py           -- Day 5 - VPC, subnets and internet gateways
- vpc_details.py           -- Day 5 - Route tables, security groups, instances
- iam_explore.py           -- Day 6 - IAM users, roles, policies and groups
- iam_policy.py            -- Day 6 - IAM role policies and trust documents
- cloudwatch_explore.py    -- Day 7 - CloudWatch namespaces, alarms and logs
- cloudwatch_metrics.py    -- Day 7 - EC2 metrics, billing and service usage

---

## Session Log

### Day 1 -- Linux Environment Setup
- Installed WSL2 and Ubuntu 22.04 LTS on Windows
- Resolved WSL2 kernel error (0x800701bc)
- Learned core Linux commands: pwd, ls, mkdir, cd, touch, rm, echo, cat

### Day 2 -- Git, GitHub and Python Setup
- Configured Git identity and generated SSH keys (ed25519)
- Connected laptop to GitHub via SSH authentication
- Completed full Git workflow: add, commit, push
- Installed pip and wrote first Python script

### Day 3 -- AWS CLI and Boto3 Setup
- Installed AWS CLI v2 from Amazon official source
- Installed Boto3 (AWS Python SDK)
- Configured AWS Academy credentials
- Wrote first AWS automation script listing real S3 buckets

### Day 4 -- S3 Deep Dive
- Explored S3 operations: list_objects_v2, get_bucket_location, get_bucket_versioning
- Encountered and understood AccessDenied and NoSuchBucket errors
- Learned why hardcoding AWS resource names is bad practice
- Built dynamic S3 inspection script that works across any session

### Day 5 -- EC2 and VPC Exploration
- Mapped a real AWS VPC networking environment using Python
- Discovered a running EC2 Bastion Host instance
- Listed subnets, route tables, internet gateways and security groups
- Understood CIDR blocks, availability zones and VPC architecture

### Day 6 -- IAM and AWS Security
- Listed all 20 IAM roles in a real AWS account
- Discovered voclabs role has ReadOnlyAccess explaining all previous errors
- Understood managed vs inline policies and trust policies
- Learned the principle of least privilege

### Day 7 -- CloudWatch Monitoring
- Listed 15 CloudWatch metric namespaces across a real AWS account
- Discovered 17 EC2 metrics tracked automatically per instance
- Found billing data for 15 services using get_metric_statistics
- Mapped 90+ AWS services in the Usage namespace

---

## Tech Stack

- OS: Ubuntu 22.04 LTS (WSL2 on Windows)
- Language: Python 3.10
- AWS SDK: Boto3 1.42.68
- AWS CLI: v2.34.9
- Version Control: Git and GitHub (SSH)
- AWS Platform: AWS Academy Learner Labs

---

## Setup and Usage

Install dependencies:
pip3 install boto3

Configure AWS credentials:
aws configure
aws configure set aws_session_token YOUR_SESSION_TOKEN

Verify connection:
aws sts get-caller-identity

Run any script:
python3 list_s3.py

---

## Progress Stats

| Metric | Value |
|---|---|
| Days Completed | 7 |
| Scripts Written | 11 |
| AWS Services Explored | S3, EC2, VPC, IAM, CloudWatch, STS |
| Commands Learned | 68+ |
| GitHub Commits | 7 |

---

## What is Next

- Day 8: Networking fundamentals (DNS, HTTP/S, TCP/IP)
- Day 9: AWS Lambda -- first serverless function
- Phase 2: Docker, CI/CD, Terraform
- Phase 3: SageMaker, MLOps pipelines

---

## Connect

GitHub: https://github.com/aofouad-dev

---

Built with consistency -- one session at a time.
