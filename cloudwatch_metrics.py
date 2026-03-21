import boto3
from datetime import datetime, timedelta

cw = boto3.client('cloudwatch')

# Step 1 - List all metrics in AWS/EC2 namespace
print("=== EC2 Metrics Available ===")
try:
    response = cw.list_metrics(Namespace='AWS/EC2')
    metric_names = set()
    for metric in response['Metrics']:
        metric_names.add(metric['MetricName'])
    for name in sorted(metric_names):
        print(f"  - {name}")
except Exception as e:
    print(f"  Access denied: {e}")

# Step 2 - List all metrics in AWS/Billing namespace
print("\n=== Billing Metrics Available ===")
try:
    response = cw.list_metrics(Namespace='AWS/Billing')
    for metric in response['Metrics']:
        dims = {d['Name']: d['Value']
                for d in metric['Dimensions']}
        print(f"  - {metric['MetricName']} | {dims}")
except Exception as e:
    print(f"  Access denied: {e}")

# Step 3 - Get estimated billing charges
print("\n=== Estimated AWS Charges ===")
try:
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)
    billing = cw.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[
            {'Name': 'Currency', 'Value': 'USD'}
        ],
        StartTime=start_time,
        EndTime=end_time,
        Period=86400,
        Statistics=['Maximum']
    )
    if billing['Datapoints']:
        for point in billing['Datapoints']:
            print(f"  Estimated charges: ${point['Maximum']:.4f} USD")
            print(f"  As of: {point['Timestamp']}")
    else:
        print("  No billing data available.")
except Exception as e:
    print(f"  Access denied: {e}")

# Step 4 - List metrics in AWS/Usage namespace
print("\n=== Service Usage Metrics ===")
try:
    response = cw.list_metrics(Namespace='AWS/Usage')
    services = set()
    for metric in response['Metrics']:
        dims = {d['Name']: d['Value']
                for d in metric['Dimensions']}
        if 'Service' in dims:
            services.add(dims['Service'])
    print("  Services being tracked:")
    for svc in sorted(services):
        print(f"  - {svc}")
except Exception as e:
    print(f"  Access denied: {e}")

# Step 5 - List metrics in AWS/SecretsManager
print("\n=== Secrets Manager Metrics ===")
try:
    response = cw.list_metrics(Namespace='AWS/SecretsManager')
    for metric in response['Metrics']:
        dims = {d['Name']: d['Value']
                for d in metric['Dimensions']}
        print(f"  - {metric['MetricName']} | {dims}")
except Exception as e:
    print(f"  Access denied: {e}")
