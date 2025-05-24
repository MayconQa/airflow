from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime
import requests

def query_api():
    response = requests.get('https://api.publicapis.org/entries')
    print(response.text)

with DAG(
    dag_id='http-sensor',
    description="http-sensor",
    schedule=None,
    start_date=datetime(2025, 4, 10),
    catchup=False
) as dag:

    check_api = HttpSensor(
        task_id='check_api',
        http_conn_id='connection',
        endpoint='entries',
        poke_interval=5,
        timeout=20
    )

    process_data = PythonOperator(
        task_id='process_data',
        python_callable=query_api
    )

    check_api >> process_data
