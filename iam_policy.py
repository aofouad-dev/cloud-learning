import boto3
import json

iam = boto3.client('iam')

# Step 1 - Get the voclabs role details
print("=== voclabs Role Details ===")
try:
    role = iam.get_role(RoleName='voclabs')
    r = role['Role']
    print(f"Role Name:   {r['RoleName']}")
    print(f"Role ID:     {r['RoleId']}")
    print(f"ARN:         {r['Arn']}")
    print(f"Created:     {r['CreateDate']}")

    # Trust policy -- who can assume this role
    trust = r['AssumeRolePolicyDocument']
    print(f"\nTrust Policy (who can use this role):")
    print(json.dumps(trust, indent=2, default=str))
except Exception as e:
    print(f"Access denied: {e}")

# Step 2 - List policies attached to voclabs role
print("\n=== Policies Attached to voclabs ===")
try:
    attached = iam.list_attached_role_policies(RoleName='voclabs')
    for policy in attached['AttachedPolicies']:
        print(f"\nPolicy Name: {policy['PolicyName']}")
        print(f"Policy ARN:  {policy['PolicyArn']}")
except Exception as e:
    print(f"Access denied: {e}")

# Step 3 - List inline policies on voclabs
print("\n=== Inline Policies on voclabs ===")
try:
    inline = iam.list_role_policies(RoleName='voclabs')
    if inline['PolicyNames']:
        for name in inline['PolicyNames']:
            print(f"\nInline Policy: {name}")
            policy_doc = iam.get_role_policy(
                RoleName='voclabs',
                PolicyName=name
            )
            print(json.dumps(
                policy_doc['PolicyDocument'],
                indent=2,
                default=str
            ))
    else:
        print("No inline policies found.")
except Exception as e:
    print(f"Access denied: {e}")

# Step 4 - Get EC2InstanceRole details
print("\n=== EC2InstanceRole Details ===")
try:
    role = iam.get_role(RoleName='EC2InstanceRole')
    r = role['Role']
    print(f"Role Name: {r['RoleName']}")
    print(f"ARN:       {r['Arn']}")
    attached = iam.list_attached_role_policies(
        RoleName='EC2InstanceRole'
    )
    print("Attached Policies:")
    for policy in attached['AttachedPolicies']:
        print(f"  - {policy['PolicyName']}")
except Exception as e:
    print(f"Access denied: {e}")
