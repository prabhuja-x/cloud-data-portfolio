from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import time

# Configure Spark session
spark = SparkSession.builder \
    .appName("LogAnalytics") \
    .getOrCreate()

# S3 bucket details
s3_bucket = "your-s3-bucket"  # Replace with your S3 bucket name
s3_raw_logs_path = f"s3a://{s3_bucket}/raw_logs/"
s3_aggregated_path = f"s3a://{s3_bucket}/aggregated_logs/"

def process_logs():
    try:
        # Read data from S3
        logs_df = spark.read.json(s3_raw_logs_path)

        # Print the schema for debugging
        logs_df.printSchema()

        # Basic transformations
        logs_df = logs_df.withColumn("timestamp", to_timestamp("timestamp"))
        logs_df = logs_df.withColumn("date", to_date("timestamp"))

        # Aggregate error counts by service and date
        error_counts = logs_df.filter(col("level") == "ERROR") \
            .groupBy("date", "service") \
            .count() \
            .withColumnRenamed("count", "error_count")

        # Write aggregated data to S3
        error_counts.write.mode("overwrite").parquet(s3_aggregated_path)

        print("Log processing completed.")

    except Exception as e:
        print(f"Error processing logs: {e}")

if __name__ == "__main__":
    process_logs()
    time.sleep(10)
    spark.stop()
