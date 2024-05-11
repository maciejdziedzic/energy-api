from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import json
from kafka import KafkaProducer
import time
import logging

default_args = {
    'owner': 'maciek',
    'start_date': datetime(2024, 5, 7, 10, 00)
}


def get_data():

    res = requests.get(
        "https://api.energidataservice.dk/dataset/powersystemrightnow")
    res = res.json()
    res_dict = res['records'][::][0]

    extracted_dict = {k: v for k, v in res_dict.items() if k in [
        "Minutes1UTC", "SolarPower", "OnshoreWindPower"]}

    return extracted_dict


def stream_data():
    producer = KafkaProducer(
        bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 30:
            break
        try:
            res = get_data()

            producer.send('energy_data', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue


with DAG('kafka_produce_electricity',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )
