import boto3
from datetime import datetime, timedelta

cw = boto3.client('cloudwatch')
logs = boto3.client('logs')

# Step 1 - List available metrics namespaces
print("=== CloudWatch Metric Namespaces ===")
try:
    namespaces = set()
    paginator = cw.get_paginator('list_metrics')
    for page in paginator.paginate():
        for metric in page['Metrics']:
            namespaces.add(metric['Namespace'])
    for ns in sorted(namespaces):
        print(f"  - {ns}")
except Exception as e:
    print(f"  Access denied: {e}")

# Step 2 - List CloudWatch alarms
print("\n=== CloudWatch Alarms ===")
try:
    alarms = cw.describe_alarms()
    if alarms['MetricAlarms']:
        for alarm in alarms['MetricAlarms']:
            print(f"\nAlarm:     {alarm['AlarmName']}")
            print(f"State:     {alarm['StateValue']}")
            print(f"Metric:    {alarm['MetricName']}")
            print(f"Threshold: {alarm['Threshold']}")
            print(f"Condition: {alarm['ComparisonOperator']}")
    else:
        print("  No alarms found.")
except Exception as e:
    print(f"  Access denied: {e}")

# Step 3 - List log groups
print("\n=== CloudWatch Log Groups ===")
try:
    log_groups = logs.describe_log_groups()
    if log_groups['logGroups']:
        for group in log_groups['logGroups']:
            size_mb = group.get('storedBytes', 0) / (1024 * 1024)
            print(f"\nLog Group:  {group['logGroupName']}")
            print(f"Size:       {size_mb:.2f} MB")
            if 'retentionInDays' in group:
                print(f"Retention:  {group['retentionInDays']} days")
            else:
                print(f"Retention:  Never expires")
    else:
        print("  No log groups found.")
except Exception as e:
    print(f"  Access denied: {e}")

# Step 4 - Get EC2 CPU metrics if available
print("\n=== EC2 CPU Utilization (last 1 hour) ===")
try:
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=1)
    metrics = cw.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        StartTime=start_time,
        EndTime=end_time,
        Period=300,
        Statistics=['Average', 'Maximum']
    )
    if metrics['Datapoints']:
        for point in sorted(metrics['Datapoints'],
                           key=lambda x: x['Timestamp']):
            print(f"  Time: {point['Timestamp']} | "
                  f"Avg: {point['Average']:.2f}% | "
                  f"Max: {point['Maximum']:.2f}%")
    else:
        print("  No EC2 CPU data found in the last hour.")
except Exception as e:
    print(f"  Access denied: {e}")
