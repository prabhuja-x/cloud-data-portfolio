import boto3
import json
import time
import random
import datetime

# Configure AWS credentials and region
kinesis_client = boto3.client('kinesis', region_name='us-east-1')  # Replace with your region
stream_name = 'log-analytics-stream'  # Replace with your Kinesis stream name

def generate_log_data():
    log_levels = ['INFO', 'WARNING', 'ERROR']
    services = ['Authentication', 'OrderProcessing', 'Inventory', 'Payment']
    
    timestamp = datetime.datetime.now().isoformat()
    level = random.choice(log_levels)
    service = random.choice(services)
    message = f'Log message from {service}: {level} - This is a sample log message.'
    
    log_data = {
        'timestamp': timestamp,
        'level': level,
        'service': service,
        'message': message
    }
    return log_data

def send_to_kinesis(data):
    try:
        response = kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey=str(random.randint(1, 10))  # Simple partition key
        )
        print(f"Sent log: {data}")
    except Exception as e:
        print(f"Error sending to Kinesis: {e}")

if __name__ == "__main__":
    while True:
        log_data = generate_log_data()
        send_to_kinesis(log_data)
        time.sleep(1)  # Send logs every 1 second
