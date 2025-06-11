import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd

default_args = {
    'owner': 'mayconpaz',
    'start_date': dt.datetime(2025, 6, 10),
    'retries': 2,
    'retry_delay': dt.timedelta(minutes=3),
 }

dag = DAG(
    dag_id="minha_csv_para_json",
    default_args=default_args, 
    schedule_interval=timedelta(minutes=5),      
    # '0 * * * *',
    catchup=False,
    tags=['csv', 'json', 'data_processing']
)

# Task to convert CSV to JSON
def csv_to_json():
    # Read the CSV file
    df = pd.read_csv('/opt/airflow/dags/data/sipeagroprodutoveterinario.csv', sep=';', encoding='latin1')
    
    # Convert to JSON format
    json_data = df.to_json(orient='records', date_format='iso')
    
    # Save the JSON data to a file
    with open('/opt/airflow/dags/data/siapeagro.json', 'w') as f:
        f.write(json_data)

print_starting = BashOperator(
    task_id='starting',
    bash_command='echo "I am reading the CSV now....."',
    dag=dag   
)

CSVJson = PythonOperator(
    task_id='convertCSVtoJson',
    python_callable=csv_to_json,
    dag=dag
)
print_starting >> CSVJson



