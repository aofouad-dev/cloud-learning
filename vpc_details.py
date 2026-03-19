import boto3

ec2 = boto3.client('ec2')

# Step 1 - Check for EC2 instances
print ("=== EC2 Instances ===")
try:
    response = ec2.describe_instances()
    instance_count = 0
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_count += 1
            print (f"\nInstance ID:  {instance['InstanceId']}")
            print (f"State:        {instance['State']['Name']}")
            print (f"Type:         {instance['InstanceType']}")
            print (f"AMI:          {instance['ImageId']}")
            if 'PublicIpAddress' in instance:
                print (f"Public IP:    {instance['PublicIpAddress']}")
            if 'PrivateIpAddress' in instance:
                print (f"Private IP:   {instance['PrivateIpAddress']}")
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Key'] == 'Name':
                        print (f"Name:         {tag['Value']}")
    if instance_count == 0:
        print ("No instances found.")
except Exception as e:
    print (f"Access denied: {e}")


# Step 2 - Check route tables
print ("\n=== Route Tables ===")
try:
    routes = ec2.describe_route_tables()
    for rt in routes['RouteTables']:
        name = "Unnamed"
        if 'Tags' in rt:
            for tag in rt['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']
        print (f"\nRoute Table: {rt['RouteTableId']} | Name: {name}")
        print (f"VPC:         {rt['VpcId']}")
        for route in rt['Routes']:
            dest = route.get('DestinationCidrBlock', 'N/A')
            target = (
                route.get('GatewayId') or
                route.get('NatGatewayId') or
                route.get('InstanceId') or
                'local'
            )
            print (f"  Route: {dest} -> {target}")
except Exception as e:
    print (f"Access denied: {e}")


# Step 3 - Check security groups
print ("\n=== Security Groups ===")
try:
    sgs = ec2.describe_security_groups()
    for sg in sgs['SecurityGroups']:
        print (f"\nName:   {sg['GroupName']}")
        print (f"ID:     {sg['GroupId']}")
        print (f"VPC:    {sg['VpcId']}")
        if sg['IpPermissions']:
            print ("Inbound rules:")
            for rule in sg['IpPermissions']:
                proto = rule.get('IpProtocol', 'all')
                from_port = rule.get('FromPort', 'all')
                to_port = rule.get('ToPort', 'all')
                for ip in rule.get('IpRanges', []):
                    print (f"  Allow {proto} port {from_port}-{to_port} from {ip['CidrIp']}")
except Exception as e:
    print (f"Access denied: {e}")
