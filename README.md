# Real-Time Log Analytics Platform

This project demonstrates a real-time log analytics platform using AWS Kinesis, PySpark, and S3.

## Scripts

*   `kinesis_producer.py`: This script simulates sending log data to a Kinesis Data Stream. It generates random log messages with different levels (INFO, WARNING, ERROR) and services, and sends them to the specified Kinesis stream.

*   `pyspark_processor.py`: This script processes log data from S3 using PySpark. It reads JSON log data from an S3 bucket, performs transformations, aggregates error counts by service and date, and writes the aggregated data back to S3 in Parquet format.

*   `s3_bucket_setup.txt`: This file contains instructions for setting up the S3 bucket, including creating the bucket and the `raw_logs` and `aggregated_logs` folders.

## Setup Instructions

1.  Set up the AWS environment as described in the `s3_bucket_setup.txt` file.
2.  Create a Kinesis Data Stream named `log-analytics-stream`.
3.  Install the required Python packages:

    ```bash
    pip install boto3 pyspark
    ```

4.  Run the Kinesis producer to simulate sending log data:

    ```bash
    python kinesis_producer.py
    ```

5.  Configure and run a PySpark cluster (EMR or Glue).
6.  Update the `s3_bucket` variable in `pyspark_processor.py` with your S3 bucket name.
7.  Deploy and run the PySpark processor to read from S3, process the logs, and write the aggregated results back to S3.

## Alerting

Implement alerting based on error rates using CloudWatch Metrics and Alarms. Set up a CloudWatch Metric Filter on the Kinesis stream to count ERROR level logs. Create a CloudWatch Alarm to trigger notifications (e.g., via SNS) when the error rate exceeds a threshold.

## Reporting

Use AWS Athena to query the aggregated data in S3. Connect AWS QuickSight to Athena to create visualizations and dashboards for real-time error tracking and daily/weekly aggregation reports.
