import boto3

ec2 = boto3.client('ec2')

# Step 1 - Get all VPCs with details
print ("=== VPC Details ===")
vpcs = ec2.describe_vpcs()

for vpc in vpcs['Vpcs']:
    default = "DEFAULT" if vpc['IsDefault'] else "CUSTOM"
    print (f"\nVPC ID:  {vpc['VpcId']}  [{default}]")
    print (f"CIDR:    {vpc['CidrBlock']}")
    print (f"State:   {vpc['State']}")

    # Print tags if they exist
    if 'Tags' in vpc:
        for tag in vpc['Tags']:
            if tag['Key'] == 'Name':
                print (f"Name:    {tag['Value']}")


# Step 2 - Get all subnets
print ("\n=== Subnets ===")
subnets = ec2.describe_subnets()

for subnet in subnets['Subnets']:
    print (f"\nSubnet ID:   {subnet['SubnetId']}")
    print (f"VPC ID:      {subnet['VpcId']}")
    print (f"CIDR:        {subnet['CidrBlock']}")
    print (f"Zone:        {subnet['AvailabilityZone']}")
    print (f"Public IPs:  {subnet['MapPublicIpOnLaunch']}")

    if 'Tags' in subnet:
        for tag in subnet['Tags']:
            if tag['Key'] == 'Name':
                print (f"Name:        {tag['Value']}")


# Step 3 - Get internet gateways
print ("\n=== Internet Gateways ===")
igws = ec2.describe_internet_gateways()

if igws['InternetGateways']:
    for igw in igws['InternetGateways']:
        print (f"\nGateway ID: {igw['InternetGatewayId']}")
        if igw['Attachments']:
            print (f"Attached to VPC: {igw['Attachments'][0]['VpcId']}")
        if 'Tags' in igw:
            for tag in igw['Tags']:
                if tag['Key'] == 'Name':
                    print (f"Name: {tag['Value']}")
else:
    print ("  No internet gateways found.")
