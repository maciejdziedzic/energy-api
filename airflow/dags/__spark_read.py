# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType
# import pyspark.sql.functions as F
# import pyspark.sql.types as T
# from pyspark.sql import SparkSession
# import os
# from pyspark.sql.functions import from_json
# os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.1,org.apache.spark:spark-avro_2.12:3.3.1 pyspark-shell'


# default_args = {
#     'owner': 'maciek',
#     'start_date': datetime(2024, 5, 7, 10, 00)
# }


# def get_data():
#     print('hello')

#     spark = SparkSession \
#         .builder \
#         .appName("Spark-Notebook") \
#         .getOrCreate()


# with DAG('spark_read',
#          default_args=default_args,
#          schedule_interval='@daily',
#          catchup=False) as dag:

#     streaming_task = PythonOperator(
#         task_id='stream_data_from_api',
#         python_callable=get_data
#     )
