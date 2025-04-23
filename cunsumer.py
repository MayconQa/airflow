from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.python import PythonOperator
import pandas as pd
from datetime import datetime

# Dataset que será observado
mydataset = Dataset('/opt/airflow/data/Churn_new.csv')

dag = DAG(
    dag_id='consumer',
    description="consumer",
    schedule=[mydataset],  # Executa quando esse dataset for atualizado
    start_date=datetime(2025, 4, 10),
    catchup=False
)

def my_file():
    df = pd.read_csv('/opt/airflow/data/Churn.csv', sep=';')
    df.to_csv('/opt/airflow/data/Churn_new2.csv', sep=';', index=False)

t1 = PythonOperator(
    task_id='t1',
    python_callable=my_file,
    dag=dag
)
t1
