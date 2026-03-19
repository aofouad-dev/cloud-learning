import boto3

ec2 = boto3.client('ec2')

# Step 1 - List available regions (always allowed)
print ("=== Available AWS Regions ===")
regions = ec2.describe_regions()
for region in regions['Regions']:
    print (f"  - {region['RegionName']}")

# Step 2 - List availability zones in us-east-1
print ("\n=== Availability Zones in us-east-1 ===")
zones = ec2.describe_availability_zones()
for zone in zones['AvailabilityZones']:
    print (f"  - {zone['ZoneName']} | State: {zone['State']}")

# Step 3 - List key pairs (SSH keys registered in AWS)
print ("\n=== Key Pairs ===")
try:
    keys = ec2.describe_key_pairs()
    if keys['KeyPairs']:
        for key in keys['KeyPairs']:
            print (f"  - {key['KeyName']} | Type: {key['KeyType']}")
    else:
        print ("  No key pairs found.")
except Exception as e:
    print (f"  Access denied: {e}")

# Step 4 - List VPCs (Virtual Private Clouds)
print ("\n=== VPCs (Your Private Networks) ===")
try:
    vpcs = ec2.describe_vpcs()
    for vpc in vpcs['Vpcs']:
        default = "Yes" if vpc['IsDefault'] else "No"
        print (f"  - VPC ID: {vpc['VpcId']}")
        print (f"    CIDR:   {vpc['CidrBlock']}")
        print (f"    Default: {default}")
except Exception as e:
    print (f"  Access denied: {e}")
