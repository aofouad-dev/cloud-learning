import boto3
import json

iam = boto3.client('iam')

# Step 1 - Get current user/role info
print ("=== Current Identity ===")
sts = boto3.client('sts')
identity = sts.get_caller_identity()
print (f"Account:  {identity['Account']}")
print (f"User ID:  {identity['UserId']}")
print (f"ARN:      {identity['Arn']}")

# Step 2 - List IAM users
print ("\n=== IAM Users ===")
try:
    users = iam.list_users()
    if users['Users']:
        for user in users['Users']:
            print (f"\nUsername:   {user['UserName']}")
            print (f"User ID:    {user['UserId']}")
            print (f"ARN:        {user['Arn']}")
            print (f"Created:    {user['CreateDate']}")
    else:
        print ("No IAM users found.")
except Exception as e:
    print (f"Access denied: {e}")

# Step 3 - List IAM roles
print ("\n=== IAM Roles ===")
try:
    roles = iam.list_roles()
    for role in roles['Roles']:
        print (f"\nRole Name:  {role['RoleName']}")
        print (f"Role ID:    {role['RoleId']}")
        print (f"ARN:        {role['Arn']}")
        print (f"Created:    {role['CreateDate']}")
except Exception as e:
    print (f"Access denied: {e}")

# Step 4 - List IAM policies (AWS managed)
print ("\n=== AWS Managed Policies (first 10) ===")
try:
    policies = iam.list_policies(Scope='AWS', MaxItems=10)
    for policy in policies['Policies']:
        print (f"  - {policy['PolicyName']}")
except Exception as e:
    print (f"Access denied: {e}")

# Step 5 - List groups
print ("\n=== IAM Groups ===")
try:
    groups = iam.list_groups()
    if groups['Groups']:
        for group in groups['Groups']:
            print (f"  - {group['GroupName']}")
    else:
        print ("No groups found.")
except Exception as e:
    print (f"Access denied: {e}")
