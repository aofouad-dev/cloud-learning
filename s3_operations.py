import boto3
from datetime import datetime

s3 = boto3.client('s3')

# Step 1 - Find the Academy bucket automatically
response = s3.list_buckets()
bucket_name = response['Buckets'][0]['Name']
print(f"Found bucket: {bucket_name}")
print(f"Bucket created: {response['Buckets'][0]['CreationDate']}")

# Step 2 - List all objects in the bucket
print("\nScanning bucket contents...")
response = s3.list_objects_v2(Bucket=bucket_name)
count = response.get('KeyCount', 0)
print(f"Total objects found: {count}")

if count > 0:
    for obj in response['Contents']:
        size_kb = obj['Size'] / 1024
        print(f"  - {obj['Key']} | {size_kb:.2f} KB | {obj['LastModified']}")

# Step 3 - Get bucket location
location = s3.get_bucket_location(Bucket=bucket_name)
print(f"\nBucket region: {location['LocationConstraint'] or 'us-east-1'}")

# Step 4 - Get bucket versioning status
versioning = s3.get_bucket_versioning(Bucket=bucket_name)
status = versioning.get('Status', 'Not enabled')
print(f"Versioning: {status}")

print("\nS3 inspection complete!")
