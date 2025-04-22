from airflow import DAG
from airflow import Dataset
from airflow.operators.python import PythonOperator
import numpy 
import pandas as pd 
from datetime import datetime
import pandas as pd

dag = DAG(
    'producer',
    description="producer",
    schedule_interval=None,
    start_date=datetime(2025, 4, 10),
    catchup=False
)

mydatasey = dataset('/opt/airflow/data/Churn_new.csv')

def my_file():
    dataset = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
  

